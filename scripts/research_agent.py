#!/usr/bin/env python3
"""
Daily AI Research & Documentation Update Agent

What this does:
  1. Researches latest Claude/Anthropic/AI news via Perplexity sonar-pro
  2. Detects the current latest Claude model automatically
  3. Plans which files need updating AND which new skill files to create
  4. Updates ALL relevant files: skills, templates, docs, guides, READMEs
  5. Creates NEW skill files for newly relevant tools/frameworks
  6. Updates index files (skills/README.md, INDEX.md) for any new files
  7. Opens a PR with all changes for review

Required secrets (GitHub repo → Settings → Secrets → Actions):
  PERPLEXITY_API_KEY  — from console.perplexity.ai
  ANTHROPIC_API_KEY   — from console.anthropic.com
  GH_PAT              — GitHub PAT with repo + pull_requests scope
"""

import os
import sys
import json
import time
import subprocess
import requests
import anthropic
from datetime import datetime, timezone
from pathlib import Path

# ─── Config ──────────────────────────────────────────────────────────────────

TODAY     = datetime.now(timezone.utc).strftime("%Y-%m-%d")
REPO_ROOT = Path(__file__).parent.parent

PERPLEXITY_KEY = os.environ["PERPLEXITY_API_KEY"]
ANTHROPIC_KEY  = os.environ["ANTHROPIC_API_KEY"]
GH_TOKEN       = os.environ["GH_TOKEN"]

claude = anthropic.Anthropic(api_key=ANTHROPIC_KEY)
CLAUDE_MODEL = "claude-opus-4-6"  # always latest

# Files to never modify
SKIP_FILES = {
    "LICENSE",
    ".gitignore",
    ".gitattributes",
    "CONTRIBUTING.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    "planning/task.md",
    "planning/progress.md",
    "planning/activity.md",
    "scripts/research_agent.py",   # never self-modify
    "scripts/requirements.txt",
    ".github/workflows/daily-research-agent.yml",
}

SKIP_DIRS = {
    ".git",
    "node_modules",
    ".github/ISSUE_TEMPLATE",
    "scripts",
}

ELIGIBLE_EXTENSIONS = {".md", ".txt", ".yml", ".yaml", ".json"}

MAX_FILE_SIZE_BYTES = 150_000  # skip files >150 KB


# ─── Phase 1: Research ───────────────────────────────────────────────────────

RESEARCH_QUERIES = [
    (
        "latest_claude_model",
        (
            f"What is the absolute latest Claude model released by Anthropic as of {TODAY}? "
            "Give the exact model name (e.g. Claude Opus 4.6), the exact API model ID string "
            "(e.g. claude-opus-4-6-20250205), the release date, pricing per million tokens, "
            "and key new capabilities. Cover the latest Opus, Sonnet, and Haiku versions."
        ),
    ),
    (
        "claude_code_updates",
        (
            f"What are the latest Claude Code CLI updates as of {TODAY}? "
            "Include: exact version number, new slash commands, hooks system changes, "
            "plugin/skill system changes, agent features, worktree support, MCP changes "
            "inside Claude Code, and any deprecations or breaking changes."
        ),
    ),
    (
        "anthropic_api_changes",
        (
            f"What are the latest Anthropic API changes as of {TODAY}? "
            "Include: new model IDs, pricing changes, new parameters (effort, thinking, etc.), "
            "deprecated features, new beta headers, streaming updates, tool use changes, "
            "batch API updates, and prompt caching changes."
        ),
    ),
    (
        "mcp_ecosystem",
        (
            f"What are the latest MCP (Model Context Protocol) ecosystem updates as of {TODAY}? "
            "Include: total server counts on major registries (PulseMCP, mcp.so), "
            "new notable MCP servers, Anthropic official MCP announcements, "
            "protocol version changes, new transport methods, and Claude Code MCP features."
        ),
    ),
    (
        "new_tools_and_frameworks",
        (
            f"What are the most important NEW developer tools, frameworks, libraries, and "
            f"platforms that Claude Code users should know about as of {TODAY}? "
            "Focus on tools that would benefit from a dedicated Claude skill guide: "
            "new ORMs, full-stack frameworks, deployment platforms, AI tooling, "
            "testing frameworks, databases. Explain WHY each is newly relevant."
        ),
    ),
    (
        "superpowers_skills_plugins",
        (
            f"What are the latest updates to the Claude Code plugin ecosystem as of {TODAY}? "
            "Cover: Superpowers plugin new features, skills marketplace updates, "
            "new community plugins, hooks system improvements, ClaudeHub stats, "
            "and any notable new skills released by the community."
        ),
    ),
]


def perplexity_query(topic: str, query: str) -> dict:
    """Run a single Perplexity sonar-pro query. Returns content + citations."""
    try:
        resp = requests.post(
            "https://api.perplexity.ai/chat/completions",
            headers={
                "Authorization": f"Bearer {PERPLEXITY_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "sonar-pro",
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You are a professional AI research analyst. "
                            "Provide factual, precise, citation-backed findings. "
                            "Focus on concrete details: exact version numbers, dates, "
                            "feature names, pricing figures, API model IDs. "
                            "No speculation or filler."
                        ),
                    },
                    {"role": "user", "content": query},
                ],
            },
            timeout=60,
        )
        data = resp.json()
        return {
            "topic": topic,
            "content": data["choices"][0]["message"]["content"],
            "citations": data.get("citations", []),
        }
    except Exception as e:
        print(f"  ⚠️  Perplexity [{topic}] failed: {e}")
        return {"topic": topic, "content": "", "citations": []}


def gather_research() -> tuple[str, str]:
    """
    Run all research queries via Perplexity.
    Returns: (full_research_text, latest_opus_model_name)
    """
    print("  Querying Perplexity sonar-pro...")
    sections = []
    latest_model_raw = ""

    for topic, query in RESEARCH_QUERIES:
        print(f"    → {topic}...")
        result = perplexity_query(topic, query)
        if result["content"]:
            sources = "\n".join(f"  - {c}" for c in result["citations"][:6])
            sections.append(
                f"## {topic.upper()}\n{result['content']}\n\nSources:\n{sources}"
            )
            if topic == "latest_claude_model":
                latest_model_raw = result["content"]
        time.sleep(0.5)  # gentle rate limiting

    full_research = f"# Research — {TODAY}\n\n" + "\n\n---\n\n".join(sections)

    # Ask Claude to extract the canonical latest Opus model name
    latest_model = "Claude Opus 4.6"  # safe fallback
    if latest_model_raw:
        try:
            resp = claude.messages.create(
                model=CLAUDE_MODEL,
                max_tokens=50,
                messages=[{
                    "role": "user",
                    "content": (
                        "From this text, extract ONLY the latest Claude Opus model name "
                        "(e.g. 'Claude Opus 4.6' or 'Claude Opus 5'). "
                        "Return the model name only, nothing else.\n\n"
                        f"{latest_model_raw[:1000]}"
                    ),
                }],
            )
            extracted = resp.content[0].text.strip()
            if extracted:
                latest_model = extracted
        except Exception:
            pass  # use fallback

    return full_research, latest_model


# ─── Phase 2: Discover all repo files ────────────────────────────────────────

def get_all_eligible_files() -> list[Path]:
    """Return every file in the repo eligible for agent review."""
    eligible = []
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(REPO_ROOT)
        parts = rel.parts

        if any(part in SKIP_DIRS for part in parts):
            continue
        if str(rel) in SKIP_FILES or rel.name in SKIP_FILES:
            continue
        if path.suffix not in ELIGIBLE_EXTENSIONS:
            continue
        if path.stat().st_size > MAX_FILE_SIZE_BYTES:
            continue

        eligible.append(path)
    return sorted(eligible)


# ─── Phase 3: Planning ───────────────────────────────────────────────────────

def plan_all_updates(research: str, latest_model: str, files: list[Path]) -> dict:
    """
    Ask Claude to decide:
    - Which existing files need updating and why
    - Which brand new skill files to create
    """
    file_index = "\n".join(f"- {f.relative_to(REPO_ROOT)}" for f in files)

    resp = claude.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=6000,
        messages=[{
            "role": "user",
            "content": f"""You are the chief editor of a Claude/Anthropic prompt engineering repository.

Today is {TODAY}. The latest Claude Opus model is: {latest_model}

## Today's Research
{research[:10000]}

## All Files Currently in Repo
{file_index}

## Your Task
Produce a complete update plan as a JSON object with two keys:

### Key 1: "updates"
Array of EXISTING files that need changes. For each:
{{
  "file": "relative/path/from/repo/root",
  "reason": "specific description of what is outdated or missing",
  "priority": "high|medium|low",
  "update_compatibility": true
}}

Set "update_compatibility": true for ANY file that contains:
- Claude model names (Opus 4.5, Sonnet 4.5, etc.)
- Compatibility fields in frontmatter
- Model ID strings (claude-opus-4-5-..., etc.)
- Version numbers for Claude Code

Priority guide:
- "high"   = model names/IDs, version numbers, pricing, breaking changes, compatibility fields
- "medium" = new features, ecosystem stats, server counts, new commands
- "low"    = minor additions, supplementary info

### Key 2: "new_skills"
Array of brand NEW skill files to create under skills/examples/. Only include if the
research reveals a genuinely important tool not already covered in the repo. For each:
{{
  "filename": "tool-name-skill.md",
  "topic": "Human-readable topic name",
  "reason": "why this tool is newly important for Claude Code users"
}}

Return valid JSON only. No markdown code fences, no explanation.""",
        }],
    )

    try:
        text = resp.content[0].text.strip()
        # Strip markdown fences if Claude added them
        if text.startswith("```"):
            lines = text.split("\n")
            text = "\n".join(lines[1:])
            if text.endswith("```"):
                text = "\n".join(text.split("\n")[:-1])
        return json.loads(text)
    except Exception as e:
        print(f"  ⚠️  Planning JSON parse failed: {e}")
        return {"updates": [], "new_skills": []}


# ─── Phase 4: Update existing files ──────────────────────────────────────────

def update_existing_file(
    file_path: Path,
    research: str,
    latest_model: str,
    reason: str,
    update_compatibility: bool,
) -> bool:
    """
    Ask Claude to intelligently update a single file.
    Returns True if the file was actually changed.
    """
    rel = str(file_path.relative_to(REPO_ROOT))
    try:
        current = file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"     ⚠️  Could not read {rel}: {e}")
        return False

    compat_block = ""
    if update_compatibility:
        compat_block = f"""
COMPATIBILITY UPDATE (mandatory):
- Replace ALL occurrences of old Claude model names with "{latest_model}"
  e.g. "Claude Opus 4.5" → "{latest_model}", "Claude Opus 4.6" → keep if already latest
- Update frontmatter `compatibility:` to: "{latest_model}, Claude Code v2.x"
- Update frontmatter `updated:` to: {TODAY}
- Update model ID strings in code examples to latest (e.g. claude-opus-4-6-20250205)
- Update any inline text referring to old model versions
"""

    resp = claude.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=8192,
        messages=[{
            "role": "user",
            "content": f"""You are updating a file in a Claude/Anthropic prompt engineering guide repository.

## File: {rel}
## Current Content:
{current}

## Research (as of {TODAY}):
{research[:5000]}

## What needs updating:
{reason}
{compat_block}

## Rules:
1. Preserve ALL existing structure, formatting, and writing style exactly
2. Update version numbers, model IDs, pricing, feature lists, stats, dates
3. Update "Last Updated" / "Last Major Update" dates to {TODAY}
4. Add new information revealed by research that genuinely belongs in this file
5. Do NOT restructure, reformat, or rewrite content that is still accurate
6. Do NOT add padding, speculation, or content outside this file's scope
7. If nothing actually needs changing after careful review, return exactly: NO_CHANGES_NEEDED

Return the complete updated file content only (or NO_CHANGES_NEEDED). No preamble.""",
        }],
    )

    new_content = resp.content[0].text.strip()

    if new_content == "NO_CHANGES_NEEDED":
        return False
    if new_content == current.strip():
        return False

    file_path.write_text(new_content + "\n", encoding="utf-8")
    return True


# ─── Phase 5: Create new skill files ─────────────────────────────────────────

def create_new_skill(
    filename: str,
    topic: str,
    reason: str,
    research: str,
    latest_model: str,
    format_reference: str,
) -> bool:
    """
    Generate and write a new skill file under skills/examples/.
    Returns True if file was created.
    """
    skill_path = REPO_ROOT / "skills" / "examples" / filename

    if skill_path.exists():
        print(f"     – {filename} already exists, skipping")
        return False

    resp = claude.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=8192,
        messages=[{
            "role": "user",
            "content": f"""Create a complete, production-ready Claude Code skill file for: {topic}

Why this skill is needed (from research):
{reason}

Relevant research context:
{research[:3000]}

Use this existing skill as your exact format reference:
{format_reference}

Requirements:
- Frontmatter: name, description, allowed-tools, version (1.0.0), compatibility, updated
- Set compatibility to: "{latest_model}, Claude Code v2.x"
- Set updated to: {TODAY}
- Sections: Overview, core patterns with real code examples, anti-patterns, verification checklist, Resources
- Code examples must be practical and production-ready
- Match the exact writing style, depth, and format of the reference above
- End with a Resources section containing real, valid URLs

Return the complete skill file content only. No preamble or explanation.""",
        }],
    )

    content = resp.content[0].text.strip()
    skill_path.write_text(content + "\n", encoding="utf-8")
    return True


def update_skills_readme(new_skill_defs: list[dict], latest_model: str):
    """Add new skill entries to skills/README.md."""
    readme_path = REPO_ROOT / "skills" / "README.md"
    if not readme_path.exists():
        return

    current = readme_path.read_text(encoding="utf-8")
    skills_summary = "\n".join(
        f"- Filename: {s['filename']} | Topic: {s['topic']} | Reason: {s['reason']}"
        for s in new_skill_defs
    )

    resp = claude.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=6000,
        messages=[{
            "role": "user",
            "content": f"""Update this skills/README.md to include newly created skill files.

Current README:
{current}

New skills to add:
{skills_summary}

Rules:
1. Add each new skill to the appropriate table/section based on its topic category
2. Follow the exact existing table format: | [Name](./examples/filename.md) | Purpose | Status |
3. Update the total skill count mentioned in the intro text
4. Update any "Last Updated" date to {TODAY}
5. Preserve everything else exactly as-is

Return the complete updated README content only.""",
        }],
    )

    new_content = resp.content[0].text.strip()
    readme_path.write_text(new_content + "\n", encoding="utf-8")


# ─── Phase 6: PR creation ────────────────────────────────────────────────────

def create_pr(updated_files: list[str], created_files: list[str], latest_model: str):
    """Commit all changes to a new branch and open a PR."""
    branch = f"chore/research-update-{TODAY}"

    run = lambda cmd: subprocess.run(cmd, cwd=REPO_ROOT, check=True)

    run(["git", "config", "user.name",  "Research Agent"])
    run(["git", "config", "user.email", "agent@noreply.github.com"])
    run(["git", "checkout", "-b", branch])
    run(["git", "add", "-A"])
    run(["git", "commit", "-m", f"chore: daily research update {TODAY}"])
    run(["git", "push", "origin", branch])

    updated_list = "\n".join(f"- `{f}`" for f in updated_files) or "_None_"
    created_list = "\n".join(f"- `{f}` *(new)*" for f in created_files) or "_None_"

    pr_body = f"""## Daily Research Update — {TODAY}

Automated update by the Daily Research Agent.
**Latest Claude Model Applied:** `{latest_model}`

---

### Updated Files ({len(updated_files)})
{updated_list}

### New Files Created ({len(created_files)})
{created_list}

---

### Research Coverage
- Latest Claude model versions & API IDs
- Compatibility fields updated across all skill files
- Claude Code CLI — version, commands, features
- Anthropic API — models, pricing, parameters
- MCP Ecosystem — server counts, new integrations
- New tools/frameworks → new skill files
- Superpowers & skills marketplace updates

### Before Merging
- Verify model names and API IDs are accurate
- Review any new skill files for correctness
- Check pricing or stat changes against official sources

*Generated by `.github/workflows/daily-research-agent.yml`*"""

    env = {**os.environ, "GH_TOKEN": GH_TOKEN}
    subprocess.run(
        [
            "gh", "pr", "create",
            "--title", f"chore: Daily Research Update {TODAY}",
            "--body", pr_body,
            "--label", "automated,documentation",
        ],
        cwd=REPO_ROOT,
        check=True,
        env=env,
    )


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    print(f"\n🤖  Daily Research Agent — {TODAY}\n{'─' * 50}")

    # Phase 1 — Research
    print("\n[1/6] Gathering research via Perplexity sonar-pro...")
    research, latest_model = gather_research()
    print(f"  ✓ Research complete")
    print(f"  ✓ Latest model: {latest_model}")

    # Phase 2 — Discover files
    print("\n[2/6] Scanning repo files...")
    files = get_all_eligible_files()
    print(f"  ✓ {len(files)} eligible files found")

    # Phase 3 — Plan
    print("\n[3/6] Planning updates (Claude opus-4-6)...")
    plan       = plan_all_updates(research, latest_model, files)
    updates    = plan.get("updates", [])
    new_skills = plan.get("new_skills", [])
    print(f"  ✓ {len(updates)} files queued for update")
    print(f"  ✓ {len(new_skills)} new skill files to create")

    if not updates and not new_skills:
        print("\n✓ Repo is fully current. Nothing to do today.")
        sys.exit(0)

    # Phase 4 — Update existing files
    print("\n[4/6] Updating existing files...")
    updated_files = []
    for item in sorted(
        updates,
        key=lambda x: {"high": 0, "medium": 1, "low": 2}.get(x.get("priority", "low"), 2),
    ):
        fpath = REPO_ROOT / item["file"]
        priority = item.get("priority", "?")
        print(f"  → {item['file']} [{priority}]")

        changed = update_existing_file(
            fpath,
            research,
            latest_model,
            item["reason"],
            item.get("update_compatibility", False),
        )
        if changed:
            updated_files.append(item["file"])
            print(f"     ✓ updated")
        else:
            print(f"     – no changes needed")

    # Phase 5 — Create new skill files
    print("\n[5/6] Creating new skill files...")
    created_files = []

    # Load format reference from an existing skill
    format_ref = ""
    ref_path = REPO_ROOT / "skills" / "examples" / "api-development-skill.md"
    if ref_path.exists():
        format_ref = ref_path.read_text(encoding="utf-8")[:3000]

    for skill_def in new_skills:
        fname  = skill_def["filename"]
        topic  = skill_def["topic"]
        reason = skill_def["reason"]
        print(f"  → Creating: {fname} ({topic})")

        created = create_new_skill(
            fname, topic, reason, research, latest_model, format_ref
        )
        if created:
            rel = f"skills/examples/{fname}"
            created_files.append(rel)
            print(f"     ✓ created")

    # Update skills/README.md if new skills were added
    if created_files:
        print("  → Updating skills/README.md...")
        update_skills_readme(new_skills, latest_model)
        if "skills/README.md" not in updated_files:
            updated_files.append("skills/README.md")

    # Done?
    all_changed = updated_files + created_files
    if not all_changed:
        print("\n✓ No actual changes after processing. Repo is already current.")
        sys.exit(0)

    # Phase 6 — Open PR
    print(f"\n[6/6] Creating PR ({len(all_changed)} total changes)...")
    create_pr(updated_files, created_files, latest_model)

    print(f"\n{'─' * 50}")
    print(f"✅  Done.")
    print(f"   Updated : {len(updated_files)} files")
    print(f"   Created : {len(created_files)} new skill files")
    print(f"   Model   : {latest_model}")


if __name__ == "__main__":
    main()

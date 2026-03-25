#!/usr/bin/env python3
"""
Daily AI Research & Documentation Update Agent

What this does:
  1. Researches latest Claude/Anthropic/AI news via Perplexity sonar-pro (parallel)
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
import subprocess
import requests
import anthropic
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path


def log(msg: str) -> None:
    """Print with immediate flush so GitHub Actions shows output in real-time."""
    print(msg, flush=True)


# ─── Config ──────────────────────────────────────────────────────────────────

TODAY     = datetime.now(timezone.utc).strftime("%Y-%m-%d")
REPO_ROOT = Path(__file__).parent.parent

PERPLEXITY_KEY = os.environ["PERPLEXITY_API_KEY"]
ANTHROPIC_KEY  = os.environ["ANTHROPIC_API_KEY"]
GH_TOKEN       = os.environ["GH_TOKEN"]

# 180s timeout per Claude call — prevents infinite hangs on large files
claude = anthropic.Anthropic(api_key=ANTHROPIC_KEY, timeout=180.0)
CLAUDE_MODEL = "claude-opus-4-6"

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
    "scripts/research_agent.py",
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
MAX_FILE_SIZE_BYTES  = 150_000


# ─── Phase 1: Research (parallel) ────────────────────────────────────────────

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
    """Single Perplexity sonar-pro query with 60s timeout."""
    log(f"    → [{topic}] starting...")
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
                            "Focus on: exact version numbers, dates, feature names, "
                            "pricing figures, API model IDs. No speculation or filler."
                        ),
                    },
                    {"role": "user", "content": query},
                ],
            },
            timeout=60,
        )
        resp.raise_for_status()
        data = resp.json()
        content  = data["choices"][0]["message"]["content"]
        citations = data.get("citations", [])
        log(f"    ✓ [{topic}] done ({len(content)} chars, {len(citations)} sources)")
        return {"topic": topic, "content": content, "citations": citations}
    except Exception as e:
        log(f"    ⚠️  [{topic}] failed: {e}")
        return {"topic": topic, "content": "", "citations": []}


def gather_research() -> tuple[str, str]:
    """
    Run all Perplexity queries IN PARALLEL.
    Returns: (full_research_text, latest_opus_model_name)
    """
    log("  Launching 6 Perplexity queries in parallel...")
    results_map: dict[str, dict] = {}

    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = {
            pool.submit(perplexity_query, topic, query): topic
            for topic, query in RESEARCH_QUERIES
        }
        for future in as_completed(futures):
            result = future.result()
            results_map[result["topic"]] = result

    # Assemble in original query order for consistent research doc
    sections = []
    latest_model_raw = ""
    for topic, _ in RESEARCH_QUERIES:
        result = results_map.get(topic, {})
        if result.get("content"):
            sources = "\n".join(f"  - {c}" for c in result["citations"][:6])
            sections.append(
                f"## {topic.upper()}\n{result['content']}\n\nSources:\n{sources}"
            )
            if topic == "latest_claude_model":
                latest_model_raw = result["content"]

    full_research = f"# Research — {TODAY}\n\n" + "\n\n---\n\n".join(sections)

    # Abort if every Perplexity query failed — no research = no reliable updates
    successful = sum(1 for _, r in RESEARCH_QUERIES if results_map.get(r[0] if isinstance(r, tuple) else _, {}).get("content"))
    if not sections:
        log("\n❌  All Perplexity queries failed (401 Unauthorized).")
        log("   Check your PERPLEXITY_API_KEY secret:")
        log("   Repo → Settings → Secrets → Actions → PERPLEXITY_API_KEY")
        log("   Get a valid key from: https://console.perplexity.ai")
        sys.exit(1)

    # Extract canonical latest model name
    latest_model = "Claude Opus 4.6"  # safe fallback
    if latest_model_raw:
        try:
            log("  Extracting latest model name from research...")
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
        except Exception as e:
            log(f"  ⚠️  Model extraction failed ({e}), using fallback: {latest_model}")

    return full_research, latest_model


# ─── Phase 2: Discover files ──────────────────────────────────────────────────

def get_all_eligible_files() -> list[Path]:
    """Return every file in the repo eligible for agent review."""
    eligible = []
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel   = path.relative_to(REPO_ROOT)
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


# ─── Phase 3: Planning ────────────────────────────────────────────────────────

def plan_all_updates(research: str, latest_model: str, files: list[Path]) -> dict:
    """Ask Claude to decide which files to update and which new skills to create."""
    file_index = "\n".join(f"- {f.relative_to(REPO_ROOT)}" for f in files)
    log(f"  Sending plan request to Claude ({len(file_index)} chars file index)...")

    resp = claude.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=4096,
        messages=[{
            "role": "user",
            "content": f"""You are the chief editor of a Claude/Anthropic prompt engineering repository.

Today is {TODAY}. The latest Claude Opus model is: {latest_model}

## Today's Research
{research[:8000]}

## All Files in Repo
{file_index}

## Task
Return a JSON object with two keys:

"updates" — existing files that need changes:
{{
  "file": "relative/path",
  "reason": "specific description of what is outdated",
  "priority": "high|medium|low",
  "update_compatibility": true/false
}}

Set update_compatibility=true for files with Claude model names, compatibility frontmatter,
model ID strings, or Claude Code version numbers.

Priority:
- high   = model names/IDs, version numbers, pricing, breaking changes
- medium = new features, ecosystem stats, new commands
- low    = minor additions

"new_skills" — brand new skill files to create in skills/examples/:
{{
  "filename": "tool-name-skill.md",
  "topic": "Human-readable name",
  "reason": "why this is newly important"
}}

Only add new_skills if research reveals genuinely important tools not yet in the repo.

Return valid JSON only. No markdown fences.""",
        }],
    )

    try:
        text = resp.content[0].text.strip()
        if text.startswith("```"):
            text = "\n".join(text.split("\n")[1:])
        if text.endswith("```"):
            text = "\n".join(text.split("\n")[:-1])
        return json.loads(text)
    except Exception as e:
        log(f"  ⚠️  Plan JSON parse failed: {e}")
        log(f"  Raw response: {resp.content[0].text[:500]}")
        return {"updates": [], "new_skills": []}


# ─── Phase 4: Update existing files ──────────────────────────────────────────

def update_existing_file(
    file_path: Path,
    research: str,
    latest_model: str,
    reason: str,
    update_compatibility: bool,
) -> bool:
    """Update a single file. Returns True if file was changed."""
    rel = str(file_path.relative_to(REPO_ROOT))
    try:
        current = file_path.read_text(encoding="utf-8")
    except Exception as e:
        log(f"     ⚠️  Cannot read {rel}: {e}")
        return False

    compat_block = ""
    if update_compatibility:
        compat_block = f"""
COMPATIBILITY UPDATE (mandatory):
- Replace old Claude model names → "{latest_model}"
- Update frontmatter `compatibility:` → "{latest_model}, Claude Code v2.x"
- Update frontmatter `updated:` → {TODAY}
- Update model ID strings in code examples to the latest version
- Update any inline text referencing old model versions
"""

    log(f"     Calling Claude for {rel} ({len(current)} chars)...")
    try:
        resp = claude.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=8192,
            messages=[{
                "role": "user",
                "content": f"""Update this file from a Claude/Anthropic prompt engineering guide repository.

## File: {rel}
## Current Content:
{current}

## Research (as of {TODAY}):
{research[:4000]}

## What needs updating:
{reason}
{compat_block}

## Rules:
1. Preserve ALL existing structure, formatting, and writing style exactly
2. Update version numbers, model IDs, pricing, feature lists, stats, dates
3. Update "Last Updated" / "Last Major Update" dates to {TODAY}
4. Add new information from research that genuinely belongs in this file
5. Do NOT restructure or rewrite content that is already accurate
6. Do NOT add padding, speculation, or off-topic content
7. If nothing needs changing after review, return exactly: NO_CHANGES_NEEDED

Return the complete updated file content only (or NO_CHANGES_NEEDED). No preamble.""",
            }],
        )
    except Exception as e:
        log(f"     ⚠️  Claude call failed for {rel}: {e}")
        return False

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
    """Generate and write a new skill file. Returns True if created."""
    skill_path = REPO_ROOT / "skills" / "examples" / filename

    if skill_path.exists():
        log(f"     – {filename} already exists, skipping")
        return False

    log(f"     Generating skill file for: {topic}...")
    try:
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
- Match the exact writing style, depth, and format of the reference
- End with a Resources section with real valid URLs

Return the complete skill file content only. No preamble.""",
            }],
        )
    except Exception as e:
        log(f"     ⚠️  Skill generation failed for {filename}: {e}")
        return False

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

    log("     Updating skills/README.md index...")
    try:
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
1. Add each new skill to the appropriate table/section based on its topic
2. Follow the exact existing table format: | [Name](./examples/filename.md) | Purpose | Status |
3. Update the total skill count in the intro text
4. Update any "Last Updated" date to {TODAY}
5. Preserve everything else exactly

Return the complete updated README content only.""",
            }],
        )
        readme_path.write_text(resp.content[0].text.strip() + "\n", encoding="utf-8")
    except Exception as e:
        log(f"     ⚠️  skills/README.md update failed: {e}")


# ─── Phase 6: PR creation ────────────────────────────────────────────────────

def create_pr(updated_files: list[str], created_files: list[str], latest_model: str):
    """Commit all changes to a new branch and open a PR."""
    branch = f"chore/research-update-{TODAY}"

    def run(cmd: list[str]):
        log(f"  $ {' '.join(cmd)}")
        subprocess.run(cmd, cwd=REPO_ROOT, check=True)

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
- New tools/frameworks → new skill files created
- Superpowers & skills marketplace updates

### Before Merging
- Verify model names and API IDs are accurate
- Review any new skill files for correctness
- Check pricing or stat changes against official sources

*Generated by `.github/workflows/daily-research-agent.yml`*"""

    env = {**os.environ, "GH_TOKEN": GH_TOKEN}
    result = subprocess.run(
        [
            "gh", "pr", "create",
            "--title", f"chore: Daily Research Update {TODAY}",
            "--body", pr_body,
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        env=env,
    )
    if result.returncode == 0:
        log(f"  ✓ PR created: {result.stdout.strip()}")
    else:
        # Branch was already pushed — log the error but don't crash the run
        log(f"  ⚠️  gh pr create exited {result.returncode}: {result.stderr.strip()}")
        log("  Branch was pushed successfully. Create the PR manually if needed.")


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    log(f"\n🤖  Daily Research Agent — {TODAY}")
    log("─" * 50)

    # Phase 1 — Research (parallel)
    log("\n[1/6] Gathering research via Perplexity sonar-pro (parallel)...")
    research, latest_model = gather_research()
    log(f"  ✓ Research complete — {len(research)} chars gathered")
    log(f"  ✓ Latest model detected: {latest_model}")

    # Phase 2 — Discover files
    log("\n[2/6] Scanning repo files...")
    files = get_all_eligible_files()
    log(f"  ✓ {len(files)} eligible files found")
    for f in files:
        log(f"    - {f.relative_to(REPO_ROOT)}")

    # Phase 3 — Plan
    log("\n[3/6] Planning updates (Claude opus-4-6)...")
    plan       = plan_all_updates(research, latest_model, files)
    updates    = plan.get("updates", [])
    new_skills = plan.get("new_skills", [])
    log(f"  ✓ {len(updates)} files queued for update")
    log(f"  ✓ {len(new_skills)} new skill files to create")

    if not updates and not new_skills:
        log("\n✓ Repo is fully current. Nothing to do today.")
        sys.exit(0)

    # Phase 4 — Update existing files
    log("\n[4/6] Updating existing files...")
    updated_files = []
    for item in sorted(
        updates,
        key=lambda x: {"high": 0, "medium": 1, "low": 2}.get(x.get("priority", "low"), 2),
    ):
        fpath    = REPO_ROOT / item["file"]
        priority = item.get("priority", "?")
        log(f"  → {item['file']} [{priority}]")
        log(f"     reason: {item['reason'][:80]}...")

        changed = update_existing_file(
            fpath,
            research,
            latest_model,
            item["reason"],
            item.get("update_compatibility", False),
        )
        if changed:
            updated_files.append(item["file"])
            log(f"     ✓ updated")
        else:
            log(f"     – no changes needed")

    # Phase 5 — Create new skill files
    log("\n[5/6] Creating new skill files...")
    created_files = []

    format_ref = ""
    ref_path = REPO_ROOT / "skills" / "examples" / "api-development-skill.md"
    if ref_path.exists():
        format_ref = ref_path.read_text(encoding="utf-8")[:3000]

    for skill_def in new_skills:
        fname  = skill_def["filename"]
        topic  = skill_def["topic"]
        reason = skill_def["reason"]
        log(f"  → {fname} ({topic})")

        created = create_new_skill(
            fname, topic, reason, research, latest_model, format_ref
        )
        if created:
            created_files.append(f"skills/examples/{fname}")
            log(f"     ✓ created")

    if created_files:
        log("  → Updating skills/README.md...")
        update_skills_readme(new_skills, latest_model)
        if "skills/README.md" not in updated_files:
            updated_files.append("skills/README.md")

    all_changed = updated_files + created_files
    if not all_changed:
        log("\n✓ No actual changes after processing. Repo is already current.")
        sys.exit(0)

    # Phase 6 — Open PR
    log(f"\n[6/6] Creating PR ({len(all_changed)} total changes)...")
    create_pr(updated_files, created_files, latest_model)

    log("\n" + "─" * 50)
    log("✅  Done.")
    log(f"   Updated : {len(updated_files)} files")
    log(f"   Created : {len(created_files)} new skill files")
    log(f"   Model   : {latest_model}")


if __name__ == "__main__":
    main()

# CLAUDE.md — The Complete Guide

> **Last updated:** 26 March 2026

CLAUDE.md is the brain of your Claude Code project. It's a markdown file that Claude reads at the start of every session. It defines rules, conventions, constraints, and context that shape Claude's behavior.

---

## Table of Contents

- [What Is CLAUDE.md?](#what-is-claudemd)
- [File Locations & Scope](#file-locations--scope)
- [Rules Files](#rules-files)
- [Auto-Memory System](#auto-memory-system)
- [Best Practices](#best-practices)
- [Patterns & Templates](#patterns--templates)
- [Common Mistakes](#common-mistakes)

---

## What Is CLAUDE.md?

CLAUDE.md is a markdown file that Claude Code **always reads** at session start. It's your way of giving Claude persistent instructions that survive across conversations.

**What to put in it:**
- Project context and architecture
- Coding standards and conventions
- Tool preferences (e.g., "use pnpm, not npm")
- Safety constraints (e.g., "never delete production data")
- Workflow rules (e.g., "always run tests before committing")

**What NOT to put in it:**
- Code snippets (they bloat context)
- Long documentation (link to files instead)
- Temporary task state (use tasks/plans for that)

---

## File Locations & Scope

Claude Code reads instructions from multiple locations, in order of increasing specificity:

| File | Scope | Loaded When |
|------|-------|-------------|
| `~/.claude/CLAUDE.md` | **Global** — all projects, your machine | Every session |
| `~/.claude/rules/*.md` | **Global rules** — extend global CLAUDE.md | Every session |
| `/project/CLAUDE.md` | **Project root** — all work in this repo | When in this repo |
| `/project/.claude/CLAUDE.md` | **Project config** — same as above | When in this repo |
| `/project/src/CLAUDE.md` | **Directory** — only when working in `src/` | When reading/editing files in `src/` |

**Precedence:** More specific files override more general ones. A project CLAUDE.md can override global rules for that project.

### Global CLAUDE.md

Located at `~/.claude/CLAUDE.md`. Loaded for **every project**.

Good for:
- Your identity and preferences
- Package manager rules (`pnpm`, not `npm`)
- Default tech stack
- Communication style preferences
- Safety rules that apply everywhere

### Rules Files

Located at `~/.claude/rules/*.md`. Each file is loaded independently.

Good for:
- Separating concerns (one file per topic)
- Keeping global CLAUDE.md under 3,000 tokens
- Organizing by domain: `agents.md`, `security.md`, `git-workflow.md`, `coding-style.md`

### Project CLAUDE.md

Located at the project root or `.claude/` directory.

Good for:
- Project-specific architecture decisions
- Tech stack for this project
- Team conventions
- Integration details

---

## Rules Files

Rules files (`~/.claude/rules/*.md`) are the recommended way to organize complex configurations.

### Why Rules Files?

CLAUDE.md has a soft limit of ~3,000 tokens. Beyond that, Claude may not reliably follow all instructions. Rules files let you split your configuration into focused modules.

### Example Structure

```
~/.claude/
├── CLAUDE.md                    # Identity, mission, core preferences (~1,500 tokens)
├── rules/
│   ├── agents.md               # Agent routing and orchestration
│   ├── coding-style.md         # File size limits, immutability, organization
│   ├── git-workflow.md         # Commit conventions, PR discipline
│   ├── performance.md          # Context management, token budgets
│   ├── router.md               # Auto-dispatch to agents/skills
│   ├── security.md             # Sensitive path guards, secrets hygiene
│   └── testing-discipline.md   # TDD workflow, coverage floors
└── settings.json               # Hooks, permissions, tool configs
```

### Rules File Format

```markdown
# Topic Name

> This file extends CLAUDE.md. It does not replace any directive there.

## Rule Category

| Condition | Action |
|---|---|
| When X happens | Do Y |
| When Z is true | Apply W |

## Detailed Rules

- Rule 1: explanation
- Rule 2: explanation
```

---

## Auto-Memory System

Claude Code v2.1.x introduced **automatic memories** — persistent context that survives across sessions.

### How It Works

1. Claude observes patterns, corrections, and preferences during your sessions
2. It automatically saves key learnings to `~/.claude/projects/<project>/memory/`
3. Memories are loaded at session start for relevant projects

### Memory File Format

```markdown
---
name: memory-name
description: One-line description
type: user | feedback | project | reference
---

Memory content here.
```

### Memory Types

| Type | What It Stores | When to Save |
|------|---------------|--------------|
| `user` | Your role, preferences, expertise | When learning about you |
| `feedback` | Corrections and confirmed approaches | When you correct or validate |
| `project` | Ongoing work, goals, deadlines | When learning project context |
| `reference` | External resource pointers | When learning about external systems |

### Manual Memory

```
# Ask Claude to remember something
"Remember that we use Prisma, not Drizzle, for this project."

# Ask Claude to forget something
"Forget what I said about using Redis — we switched to Valkey."

# Check memories
"What do you remember about this project?"
```

---

## Best Practices

### 1. Keep CLAUDE.md Concise

**Target:** Under 3,000 tokens for global, under 2,000 for project.

```markdown
# Good: concise, actionable
- Use pnpm, not npm
- Always run tests before committing
- TypeScript strict mode required

# Bad: verbose, narrative
When working on this project, please always make sure to use pnpm
as our package manager because we had issues with npm in the past
and the team decided to standardize on pnpm for better performance
and disk space usage...
```

### 2. Use Hierarchical Structure

```markdown
# CLAUDE.md

## Critical Rules (never break these)
- Never commit .env files
- Never delete production data without confirmation

## Conventions (follow unless told otherwise)
- Use feature/ branch prefix
- Conventional commit messages

## Preferences (nice to have)
- Prefer early returns over nested conditionals
- Use const over let
```

### 3. Keep Constraints at the Top

Claude pays more attention to instructions at the top of the file. Put your most important constraints first.

### 4. Use Rules Files for Complexity

If your CLAUDE.md exceeds 3,000 tokens, split into rules files:

```
CLAUDE.md (1,500 tokens) — identity + critical rules
rules/coding.md — code style
rules/git.md — git conventions
rules/security.md — safety rules
```

### 5. Version Control Your CLAUDE.md

Commit project CLAUDE.md to git. It's documentation that the whole team benefits from.

---

## Patterns & Templates

### Minimal CLAUDE.md

```markdown
# CLAUDE.md

## Project
[One sentence: what this project is]

## Stack
- Framework: Next.js 15
- Language: TypeScript (strict)
- Database: PostgreSQL via Prisma
- Package manager: pnpm

## Rules
- Run `pnpm test` before committing
- Never commit .env files
- Use conventional commit messages
```

### Self-Evolving Pattern

```markdown
# CLAUDE.md

## Critical Rules
<!-- Immutable — do not auto-modify -->
- Never commit directly to main
- All changes require tests

## Learned Conventions
<!-- Claude updates this section automatically -->
### Code Style
### Architecture Patterns
### Testing Patterns

## Session Learnings
<!-- Temporary — review before committing -->
```

### Auto-Router Pattern

```markdown
# CLAUDE.md

## Agent Routing
| If the task is about... | Route to... |
|---|---|
| Planning a feature | superpowers:brainstorming |
| Code just written | everything-claude-code:code-reviewer |
| Build failing | everything-claude-code:build-error-resolver |
| Auth or security | everything-claude-code:security-reviewer |
```

See [templates/example-clauderules.md](../templates/example-clauderules.md) for a full self-evolving template.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Putting code blocks in CLAUDE.md | Link to files instead: "See `src/config.ts` for DB config" |
| Writing 10,000+ token CLAUDE.md | Split into rules files, keep main file under 3K tokens |
| Mixing project rules with personal preferences | Global CLAUDE.md for personal, project CLAUDE.md for project |
| Not version-controlling project CLAUDE.md | Commit it — it's team documentation |
| Putting temporary state in CLAUDE.md | Use auto-memory or tasks for transient information |
| Duplicating instructions across files | Rules files extend, never duplicate CLAUDE.md content |

---

## Sources

- [Claude Code Documentation](https://code.claude.com/docs/en/)
- [Memory System](https://code.claude.com/docs/en/memory)
- [Settings and Configuration](https://code.claude.com/docs/en/settings)

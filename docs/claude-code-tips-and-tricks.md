# Claude Code Power User Tips & Tricks

> **Last updated:** 26 March 2026 | **Claude Code version:** 2.1.83

Advanced techniques, hidden features, and community-discovered workflows for getting the most out of Claude Code. Now with **50 tips** across 12 categories.

---

## Table of Contents

- [Context Management](#context-management)
- [Remote & Cloud Execution](#remote--cloud-execution)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Model & Effort Optimization](#model--effort-optimization)
- [Git & Worktree Tricks](#git--worktree-tricks)
- [Hooks Power Patterns](#hooks-power-patterns)
- [Prompt Techniques](#prompt-techniques)
- [Session Management](#session-management)
- [CLI Flags & Commands](#cli-flags--commands)
- [MCP Optimization](#mcp-optimization)
- [Security & Permissions](#security--permissions)
- [Undocumented & Community-Discovered](#undocumented--community-discovered)

---

## Context Management

### 1. Use `/compact` Proactively

Don't wait for context to fill up. Run `/compact` at ~60% usage to summarize history and recover ~70% of usable context.

```
/compact
```

### 2. Use `/context` for Optimization Suggestions

New in v2.1.74. Shows actionable suggestions for reducing context usage:

```
/context
```

### 3. Read Files Strategically

Don't dump entire files into context. Use `offset` and `limit` to read only the relevant section:

```
"Read lines 50-120 of src/auth/middleware.ts"
```

### 4. Delegate Heavy Reads to Subagents

If you need to analyze 10+ files, spawn an `Explore` agent. The heavy reading stays in the subagent's context, and only the summary comes back.

### 5. Keep CLAUDE.md Under 3,000 Tokens

Split into rules files (`~/.claude/rules/`) to keep context overhead low. See the [CLAUDE.md Guide](./claude-md-guide.md).

### 6. Use --append-system-prompt-file for Caching

```bash
claude --append-system-prompt-file=~/.claude/system-prompt.md -p "Your prompt"
```

This enables better prompt caching than inline system prompts.

---

## Remote & Cloud Execution

### 7. Start Tasks from Terminal, Run in Cloud

```bash
# Start a task that runs in the cloud
claude --remote "Fix the failing auth tests in PR #42"
```

This creates a cloud VM on claude.ai/code, clones your repo, and runs the task.

### 8. Pull Cloud Sessions Back to Terminal

```
/teleport
```

Or use `/tasks` → press `t` to teleport a specific remote session back to your local terminal with full history.

### 9. Parallel Remote Tasks

```bash
# Each --remote creates an independent cloud session
claude --remote "Implement user profile endpoint"
claude --remote "Add email verification flow"
claude --remote "Write integration tests for auth"
```

All three run simultaneously in separate cloud VMs.

### 10. Background Agent Loops

```
/loop 5m /check-deploy-status
```

Runs `/check-deploy-status` every 5 minutes. Defaults to 10 minutes if interval not specified.

### 11. Scheduled Remote Agents

```
/schedule create "Run nightly security scan" --cron "0 2 * * *"
```

Creates a recurring remote agent that runs on a cron schedule.

---

## Keyboard Shortcuts

### 12. Essential Key Bindings

| Key | Action |
|-----|--------|
| `Escape` | Interrupt Claude mid-execution |
| `Escape` × 2 | Rewind dialog (jump to previous prompt) |
| `Shift+Tab` | Cycle: normal → auto-accept → plan mode |
| `Alt+P` (Win/Linux) | Quick model switch |
| `Option+P` (macOS) | Quick model switch |
| `Shift+Enter` | Newline in input |
| `Shift+Down` | Cycle through Agent Team teammates |
| `Ctrl+T` | Toggle task list (Agent Teams) |

### 13. Rebind Keys

```
/keybindings
```

Customize in `~/.claude/keybindings.json`.

---

## Model & Effort Optimization

### 14. Set Effort Per-Session

```
/effort low       # Simple tasks, fast responses
/effort medium    # Moderate tasks
/effort high      # Default — deep reasoning
/effort max       # Opus 4.6 only — maximum depth
```

### 15. Use `ultrathink` Only for Hard Problems

Adding `ultrathink` to your prompt triggers `max` effort. Reserve it for:
- Complex multi-file architecture
- Hard debugging with multiple hypotheses
- Security analysis

Don't waste it on simple edits — it costs significantly more tokens.

### 16. Fast Mode for Speed

```
/fast
```

Toggles 2.5x faster output with the same Opus 4.6 model. Costs $30/$150 per MTok. The `↯` icon appears when active.

### 17. Override Models Per-Context

In `settings.json`:
```json
{
  "modelOverrides": {
    "subagents": "sonnet",
    "mainSession": "opus"
  }
}
```

---

## Git & Worktree Tricks

### 18. Parallel Development with Worktrees

```bash
# Create isolated worktree for a feature
claude --worktree feature-auth "Implement JWT rotation"
```

Each worktree gets its own branch and isolated file state.

### 19. Sparse Checkout for Monorepos

In `settings.json`:
```json
{
  "worktree": {
    "sparsePaths": ["packages/api/", "packages/shared/"]
  }
}
```

Only checks out specified directories — critical for large monorepos.

### 20. tmux Integration

```bash
claude --worktree feature-x --tmux
```

Launches Claude in its own tmux session alongside the worktree.

---

## Hooks Power Patterns

### 21. Auto-Format Every Edit

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{
        "type": "command",
        "command": "npx prettier --write \"$CLAUDE_FILE_PATH\" 2>/dev/null || true"
      }]
    }]
  }
}
```

### 22. Re-inject Context After Compaction

```json
{
  "hooks": {
    "SessionStart": [{
      "matcher": "compact",
      "hooks": [{
        "type": "command",
        "command": "echo 'REMINDER: Use pnpm. TypeScript strict. Run tests before committing.'"
      }]
    }]
  }
}
```

### 23. Block Dangerous Commands

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "^Bash$",
      "hooks": [{
        "type": "command",
        "command": "echo $CLAUDE_TOOL_INPUT | grep -qE '(rm -rf|DROP TABLE|--force)' && echo 'Blocked dangerous command' >&2 && exit 2 || exit 0"
      }]
    }]
  }
}
```

### 24. Validate Tests Before Stop

```json
{
  "hooks": {
    "Stop": [{
      "matcher": "",
      "hooks": [{
        "type": "agent",
        "prompt": "Run tests. If any fail, fix them before stopping.",
        "timeout": 120000
      }]
    }]
  }
}
```

---

## Prompt Techniques

### 25. Plan Before Implementing

```
"Create a plan for implementing user notifications. Don't write any code yet."
```

Then after reviewing:
```
"Now implement the plan."
```

### 26. Use /plan for Read-Only Exploration

```
Shift+Tab → Plan Mode

"Explore the codebase and explain how authentication works."
```

Claude can only read — no accidental writes.

### 27. Course-Correct with Escape

Press `Escape` to interrupt Claude mid-execution. Context is preserved. Then redirect:

```
"Stop. Undo your last changes and try using Redis instead of Memcached."
```

### 28. Multi-Window Persistence

For long projects, save state explicitly:

```
"Save your progress to progress.txt and commit to git."
```

Next session:
```
"Read progress.txt and git log to understand where we left off."
```

---

## Session Management

### 29. Voice Mode

```
/voice
```

Hold spacebar to speak, release to send. Supports 20 languages.

### 30. Copy Specific Responses

```
/copy 3     # Copy 3rd assistant response to clipboard
```

### 31. Save and Resume Sessions (ECC plugin)

```
/save-session   # Save current session state
/resume-session # Resume a saved session
```

---

## CLI Flags & Commands

### 32. Useful Flags

| Flag | Description |
|------|-------------|
| `--remote` | Run task in cloud VM |
| `--worktree NAME` | Run in isolated git worktree |
| `--bare` | Minimal startup |
| `--console` | Console output mode |
| `--from-pr URL` | Start from PR context |
| `--permission-mode plan` | Read-only plan mode |
| `--mcp-config FILE` | Custom MCP configuration |
| `--append-system-prompt-file FILE` | Persistent system prompt |
| `--tmux` | Launch in tmux session |

### 33. Useful Slash Commands

| Command | Description |
|---------|-------------|
| `/plan` | Enter plan mode (read-only) |
| `/fast` | Toggle fast mode |
| `/effort LEVEL` | Set thinking effort |
| `/voice` | Enable voice mode |
| `/loop INTERVAL CMD` | Recurring background task |
| `/compact` | Compress context |
| `/context` | Context optimization tips |
| `/usage` | Token and plan usage |
| `/teleport` | Pull cloud session to terminal |
| `/debug` | Debug current session |
| `/rewind` | Rewind to previous state |
| `/copy N` | Copy Nth response |
| `/mcp enable\|disable` | Toggle MCP servers |

---

## MCP Optimization

### 34. Keep MCP Servers Disabled by Default

Only enable the servers you're actively using:

```
/mcp enable github
/mcp disable github
```

Each idle MCP server consumes context tokens.

### 35. Rely on MCP Tool Search

MCP Tool Search (GA, enabled by default) dynamically loads only the tools Claude needs, reducing overhead from 77K to ~8.7K tokens. No configuration needed.

---

## Security & Permissions

### 36. Use Permission Modes

```bash
# Strict — ask permission for everything
claude --permission-mode=strict

# Plan — read-only, no writes
claude --permission-mode=plan
```

### 37. Wildcard Permissions

In `settings.json`, allow specific patterns:
```json
{
  "permissions": {
    "allow": ["Bash(*-h*)", "Bash(pnpm *)"]
  }
}
```

### 38. Devcontainer + Skip-Permissions (Safe YOLO Mode)

Anthropic publishes an official reference devcontainer with firewall rules that restrict outbound connections. Running `--dangerously-skip-permissions` inside this devcontainer gives unattended execution with network-level safety:

```bash
# Inside the devcontainer
claude --dangerously-skip-permissions -p "Implement the feature"
```

This is the **only approved pattern** for fully autonomous runs.

---

## Undocumented & Community-Discovered

### 39. Override Auto-Compaction Threshold

The auto-compaction trigger defaults to ~83.5% context used. Override it:

```bash
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=90
```

Higher values delay compaction (more usable context) but risk running out of completion buffer. The buffer (~33K tokens) is hardcoded. `CLAUDE_CODE_MAX_OUTPUT_TOKENS` does **not** affect this.

### 40. Cap MCP Output Tokens

Prevent any single MCP call from flooding your context:

```bash
export MAX_MCP_OUTPUT_TOKENS=50000
```

Use `claude --mcp-debug` to see exactly which servers are consuming tokens.

### 41. `/batch` — Parallel File Transformations

```
/batch rename all React class components to functional components
```

Spawns one background agent per file, all running simultaneously in separate worktrees, each opening its own PR. Up to **10x faster** than sequential prompts for large refactors.

### 42. `/simplify` — 3-Agent Pre-PR Quality Review

Triggers a three-agent pipeline that detects over-engineering, duplicate logic, and architectural issues before you open a PR. Not a linter — it reasons about design decisions.

### 43. `--bare` Flag for Pipeline Integration

```bash
claude -p "analyze this file" --bare | jq '.issues'
```

Strips all markdown formatting from headless mode output, making it safe to pipe into `jq`, `awk`, or other CLI tools.

### 44. `--channels` — Mobile Permission Approvals

```bash
claude --channels
```

Routes permission prompts to your iOS/Android app instead of blocking the terminal. Enables true unattended local execution — Claude runs on your machine, you approve from your phone.

### 45. `/plan` Accepts Inline Descriptions

```
/plan authentication system refactor with JWT rotation
```

Pre-seeds the plan with your intent, reducing back-and-forth and cutting token usage by ~50% on complex planning.

### 46. CLAUDE.md `@path` Imports

Split CLAUDE.md into domain files and import them:

```markdown
@docs/api-guidelines.md
@docs/testing-standards.md
@docs/deployment-checklist.md
```

Paths are relative to the CLAUDE.md location. Keeps your main file under 200 lines (the compliance cliff — beyond ~150-200 instructions, adherence drops).

### 47. Hooks in Skill Frontmatter

Pre/post hooks can be declared in individual skill frontmatter, not just globally in `settings.json`. Skills become fully self-contained with their own lifecycle:

```markdown
---
name: my-skill
hooks:
  pre: "echo 'Starting skill...'"
  post: "pnpm lint"
---
```

### 48. "Compounding Engineering" Pattern

When Claude makes a mistake, immediately add a rule to CLAUDE.md so it never repeats that class of error. Each session's failure becomes permanent context for all future sessions:

```markdown
# Learned Rules
- Never modify config files without creating a .backup first
- Always check if the port is in use before starting dev server
```

The Anthropic team uses this pattern internally.

### 49. `recall` — Full-Text Session History Search

Community tool by zippoxer. Provides full-text search across all previous Claude Code session histories with a terminal UI. Handles sessions up to 2GB.

```bash
# Install from awesome-claude-code
npx recall
```

### 50. `parry` — Prompt Injection Scanner for Hooks

Community tool by vaporif. Scans hook pipelines for prompt injection attacks and data exfiltration attempts — a genuine security blind spot since hooks execute shell commands with system access.

---

## Sources

- [Claude Code Changelog](https://code.claude.com/docs/en/changelog)
- [Claude Code Documentation](https://code.claude.com/docs/en/)
- [17 Claude Code Releases in 30 Days (DEV Community)](https://dev.to/ji_ai/17-claude-code-releases-in-30-days-everything-that-changed-1ec8)
- [The Ultimate Claude Code Guide (DEV Community)](https://dev.to/holasoymalva/the-ultimate-claude-code-guide-every-hidden-trick-hack-and-power-feature-you-need-to-know-2l45)
- [ClaudeFast Context Buffer Management](https://claudefa.st/blog/guide/mechanics/context-buffer-management)
- [50 Claude Code Tips (Builder.io)](https://www.builder.io/blog/claude-code-tips-best-practices)
- [Claude Code Hacks (Blockchain Council)](https://www.blockchain-council.org/claude-ai/claude-code-hacks/)
- [Hooks Guide](./hooks-guide.md)
- [Agent Teams Guide](./agent-teams-guide.md)
- [CLAUDE.md Guide](./claude-md-guide.md)
- [Skills Catalog](./skills-catalog.md)

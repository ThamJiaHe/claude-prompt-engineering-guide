# Claude Code Power User Tips & Tricks

> **Last updated:** 26 March 2026 | **Claude Code version:** 2.1.83

Advanced techniques, hidden features, and community-discovered workflows for getting the most out of Claude Code.

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

---

## Sources

- [Claude Code Changelog](https://code.claude.com/docs/en/changelog)
- [Claude Code Documentation](https://code.claude.com/docs/en/)
- [Hooks Guide](./hooks-guide.md)
- [Agent Teams Guide](./agent-teams-guide.md)
- [CLAUDE.md Guide](./claude-md-guide.md)

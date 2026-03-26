# Claude Code Hooks — Complete Reference

> **Last updated:** 25 March 2026 | **Claude Code version:** 2.1.83

Hooks are user-defined shell commands, HTTP calls, prompts, or agents that execute at deterministic lifecycle points in Claude Code. Unlike prompt-based behavior, hooks **always fire** — they are not subject to LLM judgment.

---

## Table of Contents

- [Overview](#overview)
- [Hook Types](#hook-types)
- [All Hook Events](#all-hook-events)
- [Configuration](#configuration)
- [Matchers](#matchers)
- [Exit Codes & Control](#exit-codes--control)
- [Common Use Cases](#common-use-cases)
- [Examples](#examples)

---

## Overview

Hooks solve a core problem: CLAUDE.md instructions are suggestions — the model may ignore them. Hooks are **guaranteed execution points** that run your code at specific moments in a Claude Code session.

**Key properties:**
- Deterministic — always fire when the event occurs
- Configurable — match specific tools, events, or patterns
- Controllable — can block, modify, or augment Claude's behavior
- Composable — multiple hooks can run on the same event

---

## Hook Types

| Type | Description | Communication |
|------|-------------|---------------|
| `command` | Shell command | stdin/stdout/stderr + exit codes |
| `http` | POST to HTTP endpoint | JSON request/response body |
| `prompt` | Single LLM call (Haiku by default) | Returns `{"ok": true/false, "reason": "..."}` |
| `agent` | Spawns a subagent with tool access | Up to 50 tool turns, 60s default timeout |

---

## All Hook Events

As of Claude Code v2.1.83, there are **24 hook events** across 7 categories.

### Session Lifecycle

| Event | When It Fires | Matcher Support |
|-------|---------------|-----------------|
| `SessionStart` | Session begins or resumes | `startup`, `resume`, `clear`, `compact` |
| `SessionEnd` | Session terminates | `clear`, `resume`, `logout`, `prompt_input_exit` |
| `UserPromptSubmit` | User submits a prompt, before Claude processes it | No matcher — always fires |
| `InstructionsLoaded` | CLAUDE.md or rules file is loaded | `session_start`, `nested_traversal`, `path_glob_match`, `include`, `compact` |
| `ConfigChange` | Configuration file changes during session | `user_settings`, `project_settings`, `local_settings`, `policy_settings`, `skills` |

### Tool Execution

| Event | When It Fires | Matcher Support |
|-------|---------------|-----------------|
| `PreToolUse` | Before a tool call executes — **can block it** | Tool name regex (e.g., `Edit\|Write`, `mcp__github__.*`) |
| `PermissionRequest` | Permission dialog appears | Tool name regex |
| `PostToolUse` | After successful tool execution | Tool name regex |
| `PostToolUseFailure` | After a tool call fails | Tool name regex |

### Agent & Team

| Event | When It Fires | Matcher Support |
|-------|---------------|-----------------|
| `SubagentStart` | Subagent is spawned | Agent type (e.g., `Bash`, `Explore`, `Plan`) |
| `SubagentStop` | Subagent finishes | Agent type |
| `Stop` | Main agent finishes responding | No matcher — always fires |
| `StopFailure` | Turn ends due to API error | `rate_limit`, `authentication_failed`, `billing_error` |
| `TeammateIdle` | Agent team teammate about to go idle | No matcher — always fires |
| `TaskCompleted` | Task marked complete | No matcher — always fires |

### Context & Compaction

| Event | When It Fires | Matcher Support |
|-------|---------------|-----------------|
| `PreCompact` | Before context compaction | `manual`, `auto` |
| `PostCompact` | After context compaction completes | `manual`, `auto` |

### Notifications & MCP

| Event | When It Fires | Matcher Support |
|-------|---------------|-----------------|
| `Notification` | Claude Code sends a notification | `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog` |
| `Elicitation` | MCP server requests user input | MCP server name |
| `ElicitationResult` | User responds to MCP elicitation | MCP server name |

### Version Control

| Event | When It Fires | Matcher Support |
|-------|---------------|-----------------|
| `WorktreeCreate` | Worktree being created | No matcher — always fires |
| `WorktreeRemove` | Worktree being removed | No matcher — always fires |

### Filesystem (v2.1.83+)

| Event | When It Fires | Matcher Support |
|-------|---------------|-----------------|
| `CwdChanged` | Working directory changes | No matcher — always fires |
| `FileChanged` | Files change on disk | No matcher — always fires |

---

## Configuration

Hooks are configured in settings JSON files. Multiple scopes are available:

| File | Scope |
|------|-------|
| `~/.claude/settings.json` | All projects, your machine only |
| `.claude/settings.json` | Single project, committable to repo |
| `.claude/settings.local.json` | Single project, gitignored |
| Managed policy settings | Organization-wide, admin-controlled |
| Plugin `hooks/hooks.json` | When plugin is enabled |
| `managed-settings.d/` | Drop-in directory for enterprise (v2.1.83+) |

### Basic Structure

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "npx prettier --write $CLAUDE_FILE_PATH"
          }
        ]
      }
    ]
  }
}
```

### Hook Object Properties

| Property | Type | Description |
|----------|------|-------------|
| `type` | string | `"command"`, `"http"`, `"prompt"`, or `"agent"` |
| `command` | string | Shell command to run (for `command` type) |
| `url` | string | Endpoint URL (for `http` type) |
| `prompt` | string | LLM prompt (for `prompt` type) |
| `timeout` | number | Timeout in ms (default: 60000 for agents) |

---

## Matchers

Matchers are **regex patterns** that filter which occurrences of an event trigger the hook.

### MCP Tool Name Format

MCP tools follow the pattern: `mcp__<server>__<tool>`

Example: `mcp__github__search_repositories`

### Matcher Examples

```json
// Match Edit or Write tools
"matcher": "Edit|Write"

// Match all GitHub MCP tools
"matcher": "mcp__github__.*"

// Match Bash tool only
"matcher": "^Bash$"

// Match session start from compact
"matcher": "compact"

// Match all tools (empty matcher)
"matcher": ""
```

---

## Exit Codes & Control

| Exit Code | Meaning |
|-----------|---------|
| `0` | Allow action to proceed; stdout added to Claude's context |
| `2` | **Block the action**; stderr sent to Claude as feedback |
| Any other | Action proceeds; stderr logged but not shown to Claude |

### Structured Control (JSON stdout)

For fine-grained control, exit `0` and write JSON to stdout:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Use rg instead of grep"
  }
}
```

**`PreToolUse` decisions:**
- `"allow"` — skip permission prompt, proceed immediately
- `"deny"` — cancel the tool call, send reason to Claude as feedback
- `"ask"` — show the permission prompt normally (default behavior)

---

## Common Use Cases

### Auto-Format on Save

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "npx prettier --write \"$CLAUDE_FILE_PATH\" 2>/dev/null || true"
          }
        ]
      }
    ]
  }
}
```

### Block Protected Files

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "echo $CLAUDE_TOOL_INPUT | grep -qE '(\\.env|package-lock\\.json|\\.git/)' && echo 'Protected file — cannot modify' >&2 && exit 2 || exit 0"
          }
        ]
      }
    ]
  }
}
```

### Desktop Notifications on Completion

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "powershell -Command \"[System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms'); [System.Windows.Forms.MessageBox]::Show('Claude needs attention')\""
          }
        ]
      }
    ]
  }
}
```

### Re-inject Context After Compaction

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "compact",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'REMINDER: This project uses pnpm, not npm. Always use strict TypeScript.'"
          }
        ]
      }
    ]
  }
}
```

### Log All Bash Commands (Audit Trail)

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "^Bash$",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"$(date -Iseconds) | $CLAUDE_TOOL_INPUT\" >> ~/.claude/audit.log"
          }
        ]
      }
    ]
  }
}
```

### Validate Before Stop (Agent Type Hook)

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "agent",
            "prompt": "Run the test suite and verify all tests pass. If any tests fail, report the failures and continue working on fixes.",
            "timeout": 120000
          }
        ]
      }
    ]
  }
}
```

---

## Environment Variables Available to Hooks

| Variable | Available In | Description |
|----------|-------------|-------------|
| `CLAUDE_FILE_PATH` | `PostToolUse` (Edit/Write) | Path of the file that was modified |
| `CLAUDE_TOOL_INPUT` | `PreToolUse`, `PostToolUse` | JSON string of tool input |
| `CLAUDE_TOOL_OUTPUT` | `PostToolUse` | JSON string of tool output |
| `CLAUDE_SESSION_ID` | All events | Current session identifier |

---

## Sources

- [Claude Code Hooks Guide (official)](https://code.claude.com/docs/en/hooks-guide)
- [Claude Code Hooks Reference (official)](https://code.claude.com/docs/en/hooks)
- [Claude Code Changelog v2.1.83](https://code.claude.com/docs/en/changelog)

# Claude Code Command and Configuration Reference

> Every slash command, frontmatter field, setting, and configuration option documented

## All 64 Official Slash Commands

### Auth (3)
`/login`, `/logout`, `/upgrade`

### Config (12)
`/color`, `/config` (alias `/settings`), `/keybindings`, `/permissions` (alias `/allowed-tools`), `/privacy-settings`, `/sandbox`, `/statusline`, `/stickers`, `/terminal-setup`, `/theme`, `/vim`, `/voice`

### Context (7)
`/context` (visual grid), `/cost` (token stats), `/extra-usage` (overflow billing), `/insights` (session analysis), `/stats` (daily usage), `/status` (version/model/account), `/usage` (plan limits)

### Debug (5)
`/doctor`, `/feedback` (alias `/bug`), `/help`, `/release-notes`, `/tasks`

### Export (2)
`/copy [N]`, `/export [filename]`

### Extensions (8)
`/agents`, `/chrome`, `/hooks`, `/ide`, `/mcp`, `/plugin`, `/reload-plugins`, `/skills`

### Memory (1)
`/memory`

### Model (5)
`/effort [low|medium|high|max|auto]`, `/fast [on|off]`, `/model [model]`, `/passes`, `/plan [description]`

### Project (4)
`/add-dir <path>`, `/diff`, `/init`, `/pr-comments [PR]`, `/security-review`

### Remote (7)
`/desktop` (alias `/app`), `/install-github-app`, `/install-slack-app`, `/mobile` (aliases `/ios`, `/android`), `/remote-control` (alias `/rc`), `/remote-env`, `/schedule`

### Session (7)
`/branch` (alias `/fork`), `/btw <question>`, `/clear` (aliases `/reset`, `/new`), `/compact [instructions]`, `/exit` (alias `/quit`), `/rename [name]`, `/resume [session]` (alias `/continue`), `/rewind` (alias `/checkpoint`)

---

## Frontmatter Fields (13)

Commands, skills, and agents all share the same 13 frontmatter fields:

| Field | Type | What It Does |
|-------|------|-------------|
| `name` | string | Display name and `/slash-command` identifier |
| `description` | string | Shown in autocomplete; used for auto-discovery routing |
| `argument-hint` | string | Autocomplete hint (e.g., `[issue-number]`) |
| `disable-model-invocation` | boolean | Prevent Claude from auto-invoking |
| `user-invocable` | boolean | Set `false` to hide from `/` menu |
| `paths` | string/list | Glob patterns for auto-activation (e.g., `*.tsx, *.jsx`) |
| `allowed-tools` | string | Tools permitted without user confirmation |
| `model` | string | Model override (`haiku`, `sonnet`, `opus`) |
| `effort` | string | Effort level (`low`, `medium`, `high`, `max`) |
| `context` | string | Set to `fork` for isolated subagent context |
| `agent` | string | Subagent type when `context: fork` is set |
| `shell` | string | `bash` (default) or `powershell` |
| `hooks` | object | Lifecycle hooks scoped to this command/skill |

---

## Official Bundled Skills (5)

| Skill | What It Does |
|-------|-------------|
| `simplify` | Reviews changed code for quality and efficiency, then refactors |
| `batch` | Runs commands across multiple files in bulk |
| `debug` | Debugs failing commands or code issues |
| `loop` | Runs a prompt on a recurring interval (up to 3 days) |
| `claude-api` | Helps build apps with the Claude API or Anthropic SDK |

---

## Settings Hierarchy

Settings are loaded in order (highest priority first):

1. **Project** — `.claude/settings.json` (committed, team-shared)
2. **User-Project** — `.claude/settings.local.json` (gitignored, personal)
3. **User** — `~/.claude/settings.json` (global personal)
4. **Enterprise** — `/etc/claude/settings.json` (admin-managed)

```json
{
  "permissions": {
    "allow": ["Read", "Glob", "Grep", "Bash(git *)"],
    "deny": ["Bash(rm -rf *)"]
  },
  "env": {
    "NODE_ENV": "development"
  }
}
```

---

## Hook Events

All lifecycle events you can hook into:

| Event | When It Fires |
|-------|--------------|
| `SessionStart` | Session begins |
| `PreToolUse` | Before any tool execution |
| `PostToolUse` | After tool execution |
| `PostToolUseFailure` | Tool execution failed |
| `Stop` | Agent stops |
| `SubAgentStart` | Subagent spawned |
| `SubAgentStop` | Subagent finished |
| `PreCompact` | Before context compaction |
| `PostCompact` | After compaction |
| `WorktreeCreate` | Git worktree created |
| `WorktreeRemove` | Git worktree removed |
| `TaskCompleted` | Task marked complete |

---

## Agent File Format

```yaml
---
name: my-agent
description: "Use when..."
tools: Read, Write, Edit, Bash, Glob, Grep
model: sonnet
---

System prompt content here...
```

Stored at `~/.claude/agents/` (global) or `.claude/agents/` (project). Project overrides global.

---

## Structured Development Workflows

### RPI (Research-Plan-Implement)
```
/rpi research → requirement parsing + product analysis
/rpi plan     → technical architecture + UX design
/rpi implement → coding + code review
```
Each phase uses different agents with appropriate tool permissions and model tiers.

---

## Tips from the Engineers Who Built Claude Code

**Session management:**
- Start each task fresh (`/clear`). Use `/compact` at ~60% context.
- Keep CLAUDE.md under 500 lines. Split into rules files for organization.

**Prompting:**
- Be specific about what should change and what should stay the same.
- Show examples of desired output format.
- Use "think step by step" for complex reasoning.

**Workflow:**
- Write tests before implementation.
- Use `/plan` for complex features.
- Break large tasks into smaller reviewable chunks.
- Use hooks for automated enforcement.
- Git worktrees for isolated parallel sessions.

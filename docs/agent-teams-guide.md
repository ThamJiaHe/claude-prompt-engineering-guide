# Claude Code Agent Teams — Complete Guide

> **Last updated:** 25 March 2026 | **Claude Code version:** 2.1.83 | **Status:** Experimental

Agent Teams is a multi-agent coordination system where multiple Claude Code instances work together on complex tasks. Each teammate gets its own context window, tools, and execution environment.

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Setup](#setup)
- [Commands & Controls](#commands--controls)
- [Team Patterns](#team-patterns)
- [Agent Types](#agent-types)
- [Limitations](#limitations)

---

## Overview

**Problem:** Single-agent Claude Code is limited to one context window and sequential execution.

**Solution:** Agent Teams spawns multiple Claude Code instances (teammates) that:
- Work in parallel on independent subtasks
- Coordinate via a shared task list (file-locked to prevent race conditions)
- Communicate directly via a mailbox system
- Each maintain their own context window

**When to use:**
- Tasks spanning 5+ files
- Independent subtasks that parallelize well
- Complex workflows requiring domain specialization
- Large refactoring or migration projects

**When NOT to use:**
- Simple single-file edits
- Tasks requiring tight sequential dependencies
- Quick bug fixes

---

## Architecture

```
┌─────────────────────────────────────────────────┐
│               TEAM LEAD                          │
│   (Main Claude Code session)                     │
│                                                  │
│   • Creates tasks and assigns to teammates       │
│   • Reviews and synthesizes results              │
│   • Approves/rejects teammate plans              │
│   • Coordinates cross-team dependencies          │
└──────────────┬───────────────────────────────────┘
               │
    ┌──────────┼──────────┐
    │          │          │
    ▼          ▼          ▼
┌────────┐ ┌────────┐ ┌────────┐
│ TEAM-  │ │ TEAM-  │ │ TEAM-  │
│ MATE A │ │ MATE B │ │ MATE C │
│        │ │        │ │        │
│ Own    │ │ Own    │ │ Own    │
│ context│ │ context│ │ context│
│ window │ │ window │ │ window │
└────────┘ └────────┘ └────────┘
    ↕          ↕          ↕
  ┌─────────────────────────┐
  │    SHARED TASK LIST      │
  │  (File-locked JSON)      │
  └─────────────────────────┘
```

### Teams vs Subagents

| Feature | Subagents | Agent Teams |
|---------|-----------|-------------|
| Communication | Report to main only | Direct teammate-to-teammate messaging |
| Coordination | Main agent managed | Shared task list, self-coordination |
| Context | Own window, results summarized back | Fully independent context windows |
| Token cost | Lower | Higher (scales with team size) |
| Persistence | Ephemeral | Session-scoped |

---

## Setup

### Prerequisites

```bash
# Enable the experimental feature
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

### Configuration

Team config is stored in `~/.claude/teams/{team-name}/config.json`.
Tasks are stored in `~/.claude/tasks/{team-name}/`.

### Display Modes

| Mode | How It Works | Activation |
|------|-------------|------------|
| **In-process** | All teammates in the same terminal | Default |
| **Split panes** | Each teammate in its own tmux/iTerm2 pane | `--teammate-mode split` |

Configure via `teammateMode` in settings.json or `--teammate-mode` flag.

**Note:** Split panes not supported in VS Code integrated terminal, Windows Terminal, or Ghostty.

---

## Commands & Controls

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Shift+Down` | Cycle through teammates (in-process mode) |
| `Ctrl+T` | Toggle task list view |
| `Escape` | Interrupt teammate's current turn |

### Slash Commands

| Command | Description |
|---------|-------------|
| `/team-spawn` | Create a new team with teammates |
| `/team-delegate` | Assign tasks to teammates |
| `/team-status` | View team and task status |
| `/team-review` | Review teammate outputs |
| `/team-debug` | Debug issues across teammates |
| `/team-feature` | Coordinate feature development |
| `/team-shutdown` | Gracefully shut down the team |

### Plan Approval Flow

Teammates can be required to plan before implementing. The lead reviews and approves/rejects plans before the teammate exits read-only mode.

---

## Team Patterns

### Pattern 1: Feature Development

```
Team Lead assigns:
├── Teammate A: Backend API endpoints
├── Teammate B: Frontend components
├── Teammate C: Tests and documentation
└── Lead: Integration review + merge
```

### Pattern 2: Parallel Debugging

```
Team Lead identifies hypotheses:
├── Teammate A: Investigate database query performance
├── Teammate B: Check authentication middleware
├── Teammate C: Analyze network layer timeouts
└── Lead: Synthesize findings + fix
```

### Pattern 3: Multi-Reviewer Code Review

```
Team Lead coordinates:
├── Teammate A: Security review dimension
├── Teammate B: Performance review dimension
├── Teammate C: Architecture review dimension
└── Lead: Consolidate findings + prioritize
```

---

## Agent Types

Agent Teams uses specialized agent definitions:

| Agent Type | Role | Tools |
|------------|------|-------|
| `team-lead` | Orchestrator | Read, Glob, Grep, Bash |
| `team-implementer` | Parallel builder with file ownership | Read, Write, Edit, Glob, Grep, Bash |
| `team-reviewer` | Multi-dimensional reviewer | Read, Glob, Grep, Bash |
| `team-debugger` | Hypothesis-driven investigator | Read, Glob, Grep, Bash |

### File Ownership

Each teammate operates within **strict file ownership boundaries**. Two teammates cannot modify the same file simultaneously. Coordination happens at integration points via messaging.

---

## Recommended Team Size

- **Optimal:** 3–5 teammates
- **Tasks per teammate:** 5–6 tasks
- **Token cost:** Scales linearly with team size (each teammate maintains a full context window)

---

## Limitations

- No session resumption with in-process teammates (`/resume` and `/rewind` don't restore teammates)
- Task status can lag (failed mark-complete blocks dependent tasks)
- One team per session; no nested teams
- Lead is fixed for session lifetime
- Split panes not supported in VS Code integrated terminal, Windows Terminal, or Ghostty
- Higher token costs than subagent approach

---

## Sources

- [Agent Teams (official docs)](https://code.claude.com/docs/en/agent-teams)
- [Claude Code Changelog](https://code.claude.com/docs/en/changelog)

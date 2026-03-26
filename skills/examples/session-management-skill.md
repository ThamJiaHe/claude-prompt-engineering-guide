---
name: "Session Management"
description: "Save, resume, and compact Claude Code sessions for long-running work across context windows. Apply when approaching context limits, switching tasks, or continuing multi-session work."
allowed-tools: Read, Write, Edit, Bash
version: 2.1.0
compatibility: Claude Opus 4.6, Sonnet 4.6, Claude Code v2.1.x
updated: 2026-03-26
---

# Session Management

Strategies for persisting progress, managing context, and resuming work across Claude Code sessions.

## Overview

Claude Code sessions have finite context windows. This skill teaches you to:

1. **Save sessions** before context runs out
2. **Resume sessions** with full state recovery
3. **Compact strategically** to extend sessions
4. **Persist progress** through git commits and progress files

## When to Use

- Context usage approaching 60-80%
- Switching between different tasks (frontend vs backend vs tests)
- Multi-day features that span many sessions
- Complex debugging across multiple files
- Before running `/compact` on in-progress work

## Save Session

Before ending a session or running `/compact`, save your state:

```
/save-session
```

This persists:
- Current task context and progress
- File modifications in progress
- Decision history and reasoning
- Blocked items and next steps

**Manual alternative** for critical state:

```
"Save progress to .session-state.md with:
- What we were working on
- Files modified so far
- What's left to do
- Any decisions made
- Blocked items"
```

## Resume Session

At the start of a new session continuing previous work:

```
/resume-session
```

**Manual alternative:**

```
"Read .session-state.md and git log --oneline -10 to understand
where we left off. Then continue from the next incomplete step."
```

## Strategic Compact

Don't wait for context to fill up. Compact proactively:

| Context Usage | Action |
|:---:|--------|
| < 60% | Continue working normally |
| 60-70% | Run `/compact` — recovers ~70% of usable context |
| 70-80% | Run `/save-session` then `/compact` |
| > 80% | Finish current thought, `/save-session`, start new session |

### Pre-Compact Checklist

Before compacting, ensure critical context survives:

```
"Before compacting, save these key decisions to a comment in the code:
1. [Architecture decision made]
2. [Approach chosen and why]
3. [Known issues to address]"
```

### Post-Compact Hook

Re-inject critical context after compaction:

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

## Multi-Session Persistence Patterns

### Pattern 1: Progress File

```markdown
<!-- .session-progress.md -->
# Feature: User Notifications

## Status: In Progress (Step 3 of 5)

## Completed
- [x] Database schema for notifications table
- [x] Prisma migration applied to dev branch
- [x] NotificationService class with CRUD methods

## Current Step
- [ ] REST API endpoints (POST /notifications, GET /notifications/:userId)

## Remaining
- [ ] Frontend notification bell component
- [ ] WebSocket real-time delivery

## Decisions Made
- Using server-sent events over WebSocket for v1 (simpler)
- Notifications table has soft-delete (deleted_at column)

## Blocked
- None currently
```

### Pattern 2: Git-Based Persistence

```bash
# Commit work-in-progress with clear message
git add -A
git commit -m "wip: notification endpoints (3/5 steps done)"

# Next session: read git log to recover context
git log --oneline -5
git diff HEAD~1
```

### Pattern 3: Task File (.tasks.md)

```markdown
<!-- .tasks.md -->
- [x] Issue #1: Create notifications schema
- [x] Issue #2: Prisma migration
- [x] Issue #3: NotificationService
- [ ] Issue #4: REST endpoints  ← CURRENT
- [ ] Issue #5: Frontend component
- [ ] Issue #6: Real-time delivery

STATUS: IN PROGRESS
CURRENT: Issue #4
BRANCH: feature/notifications
```

## Context Budget by Task Type

| Task Type | Context Risk | Strategy |
|-----------|:-----------:|----------|
| Single-file bug fix | Low | No session management needed |
| Multi-file refactor | Medium | Save at each file boundary |
| New feature (5+ files) | High | Progress file + git commits |
| Architecture redesign | Critical | Plan mode first, save frequently |
| Debugging session | Variable | Save hypotheses and findings |

## Integration with ECC Plugin

Requires the Everything Claude Code plugin:

```bash
/plugin install everything-claude-code
```

Then use:
- `/save-session` — Persist current state
- `/resume-session` — Restore previous state
- `/strategic-compact` — Smart compaction with context preservation

## Sources

- [Everything Claude Code Plugin](https://github.com/anthropics/everything-claude-code)
- [Claude Code Context Management](https://code.claude.com/docs/en/)

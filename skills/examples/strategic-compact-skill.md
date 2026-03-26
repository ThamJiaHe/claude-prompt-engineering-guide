---
name: "Strategic Compact"
description: "Smart context compaction that preserves critical information. Apply when context usage approaches 60-80% to recover usable context without losing important decisions, progress, or reasoning."
allowed-tools: Read, Write, Edit, Bash
version: 2.1.0
compatibility: Claude Opus 4.6, Sonnet 4.6, Claude Code v2.1.x
updated: 2026-03-26
---

# Strategic Compact

Smart context compaction that preserves what matters and discards what doesn't.

## Overview

Running `/compact` blindly can lose critical context — architecture decisions, debugging hypotheses, partial progress. This skill teaches **when** and **how** to compact strategically.

## When to Compact

| Context Usage | Action |
|:---:|--------|
| < 50% | Continue working. No action needed. |
| 50-60% | Finish current task, then compact. |
| 60-70% | Run `/compact` now — recovers ~70% of usable context. |
| 70-80% | Save state first, then `/compact`. |
| > 80% | Save session immediately. Consider starting fresh. |

## Pre-Compact Checklist

Before running `/compact`, ensure these survive:

1. **Architecture decisions** — Why you chose approach A over B
2. **Current task progress** — What step you're on, what's left
3. **File modification list** — Which files have been changed
4. **Known issues** — Bugs found, workarounds applied
5. **Blocked items** — What needs user input or external resolution

## Compact Strategy

### Step 1: Persist Critical State

```
"Before compacting, write a brief summary to .compact-state.md:
- Current task and progress (step X of Y)
- Files modified: [list]
- Key decisions: [list]
- Next steps: [list]
- Known issues: [list]"
```

### Step 2: Run Compact with Custom Summary

```
/compact "Preserve: working on [feature], modified [files], next step is [X]"
```

The custom prompt tells `/compact` what to prioritize in the summary.

### Step 3: Re-inject After Compact

```
"Read .compact-state.md to restore context about our current work."
```

## Post-Compact Hook (Automation)

Auto-remind yourself of project essentials after every compaction:

```json
{
  "hooks": {
    "SessionStart": [{
      "matcher": "compact",
      "hooks": [{
        "type": "command",
        "command": "cat .compact-state.md 2>/dev/null || echo 'No saved state found'"
      }]
    }]
  }
}
```

## What's Safe to Compact Away

- File contents you've already read (can be re-read)
- Search results (can be re-searched)
- Verbose tool output (git log, test output)
- Exploratory analysis that led to dead ends
- Conversation about approach options (after decision is made)

## What Must Be Preserved

- The decision itself (not the discussion leading to it)
- Current task state and progress markers
- Error messages and stack traces being debugged
- User preferences stated in this session
- Partial implementations not yet committed

## Integration with Session Management

For long-running work, combine with session management:

```
# At 70% context:
/save-session              # Persist full state
/compact "Preserve: [key context]"  # Compress

# If starting fresh:
/resume-session            # Restore from saved state
```

## Sources

- [Everything Claude Code — Strategic Compact](https://github.com/anthropics/everything-claude-code)
- [Claude Code Documentation — Context Management](https://code.claude.com/docs/en/)

# Ultrathink & Thinking Modes — Complete Guide

> **Last updated:** 25 March 2026 | **Models:** Opus 4.6, Sonnet 4.6

This guide covers Claude's thinking system — from adaptive thinking to the `ultrathink` keyword, effort levels, and when to use each.

---

## Table of Contents

- [Overview](#overview)
- [Adaptive Thinking (Default)](#adaptive-thinking-default)
- [Effort Levels](#effort-levels)
- [Ultrathink Keyword](#ultrathink-keyword)
- [Extended Thinking (Legacy)](#extended-thinking-legacy)
- [Claude Code Integration](#claude-code-integration)
- [API Usage](#api-usage)
- [When to Use What](#when-to-use-what)
- [Thinking Display Modes](#thinking-display-modes)

---

## Overview

Claude 4.6 models use **adaptive thinking** — the model automatically determines how deeply to reason based on the query's complexity. This replaces the manual `budget_tokens` approach of extended thinking.

**Key change:** You no longer need to guess how many thinking tokens to allocate. Claude evaluates each request and determines whether and how much to think.

---

## Adaptive Thinking (Default)

Adaptive thinking (`thinking: {type: "adaptive"}`) is the **recommended standard** for Opus 4.6 and Sonnet 4.6.

**How it works:**
1. Claude receives your request
2. It evaluates the complexity
3. It decides whether to think and how deeply
4. It may skip thinking entirely for trivial queries

**Critical advantage:** Adaptive thinking **automatically enables interleaved thinking** — Claude can think between tool calls in agentic workflows. Manual extended thinking on Opus 4.6 does NOT support interleaved thinking.

---

## Effort Levels

Control how much Claude thinks via the `effort` parameter:

| Level | Behavior | Availability |
|-------|----------|-------------|
| `low` | Minimizes thinking; skips for simple tasks | All models |
| `medium` | Moderate thinking; may skip for simple queries | All models |
| `high` | Always thinks. Deep reasoning. **(Default)** | All models |
| `max` | Always thinks, no constraints on depth | **Opus 4.6 only** |

### Thinking Budget Keywords (Claude Code)

In Claude Code, you can trigger effort levels with natural language keywords in your prompt:

| Keyword | Maps to Effort | When to Use |
|---------|---------------|-------------|
| (none) | `high` (default) | Most tasks |
| `think` | `high` | Explicitly request reasoning |
| `think hard` | `high` | Moderate complexity |
| `think harder` | `high`-`max` | Hard problems |
| `ultrathink` | `max` | Maximum reasoning depth |

### /effort Command

Since Claude Code v2.1.76, you can set effort directly:

```
/effort low      # Simple tasks, fast responses
/effort medium   # Moderate tasks
/effort high     # Default — deep reasoning
/effort max      # Maximum depth (Opus 4.6 only)
```

---

## Ultrathink Keyword

`ultrathink` triggers the `max` effort level, giving Claude the maximum thinking budget with no constraints on depth.

**Re-introduced** in Claude Code v2.1.68 (March 4, 2026).

### When to Use Ultrathink

- Complex multi-file architecture decisions
- Hard debugging with multiple root causes
- System design and trade-off analysis
- Abstract reasoning and algorithm design
- Security analysis of complex systems

### When NOT to Use Ultrathink

- Simple file edits, typos, variable renames
- Boilerplate code generation
- Straightforward bug fixes
- Documentation updates
- CRUD operations

**Cost consideration:** `ultrathink` uses significantly more tokens. Treat it as a premium tool for genuinely hard problems.

---

## Extended Thinking (Legacy)

Extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) is **deprecated** on Opus 4.6 and Sonnet 4.6. It remains functional but will be removed in a future model release.

**Why it's deprecated:**
- Required guessing a `budget_tokens` value
- Did NOT support interleaved thinking on Opus 4.6
- Adaptive thinking provides the same capability with automatic calibration

**Still required for:** Older models (Opus 4.5, Sonnet 4.5, Haiku 4.5) that don't support adaptive thinking.

### Migration Path

```python
# OLD (deprecated on 4.6 models)
thinking={"type": "enabled", "budget_tokens": 10000}

# NEW (recommended for 4.6 models)
thinking={"type": "adaptive"}
# Optional: control effort
output_config={"effort": "high"}
```

---

## Claude Code Integration

### Setting Default Effort

In `settings.json`:
```json
{
  "effort": "high"
}
```

### Per-Session Control

```
/effort low       # Switch to low effort
/effort max       # Switch to max effort
```

### In Prompts

```
# Triggers max effort
Fix this complex race condition in the auth middleware. ultrathink

# Normal effort (default high)
Add a loading spinner to the button component.
```

### Fast Mode Interaction

Fast mode (`/fast`) provides 2.5x faster output with the **same model quality**. It works independently of effort levels — you can use ultrathink with fast mode.

---

## API Usage

### Adaptive Thinking (Recommended)

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-6-20250205",
    max_tokens=16000,
    thinking={
        "type": "adaptive"
    },
    output_config={
        "effort": "high"  # or "low", "medium", "max"
    },
    messages=[
        {"role": "user", "content": "Analyze this algorithm's complexity..."}
    ]
)
```

### Legacy Extended Thinking

```python
# For older models (4.5 and below) — NOT recommended for 4.6
response = client.messages.create(
    model="claude-sonnet-4-5-20241022",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000
    },
    messages=[
        {"role": "user", "content": "..."}
    ]
)
```

### Thinking Display Options

```python
# Full thinking (default)
thinking={"type": "adaptive"}

# Summarized thinking (Opus 4.6 default in Claude Code)
thinking={"type": "adaptive", "display": "summarized"}

# Omit thinking for faster time-to-first-token
thinking={"type": "adaptive", "display": "omitted"}
```

**Billing note:** You are billed for the full internal thinking tokens, not the summarized version.

---

## When to Use What

| Task Type | Effort | Keyword | Example |
|-----------|--------|---------|---------|
| Typo fix | `low` | (none) | Fix the typo in line 42 |
| Standard coding | `high` | (none) | Add a REST endpoint for user profiles |
| Complex refactor | `high` | `think hard` | Refactor the auth module to use JWT rotation |
| Architecture design | `max` | `ultrathink` | Design the event-driven microservices architecture |
| Hard debugging | `max` | `ultrathink` | Find the race condition causing intermittent 500 errors |
| Simple Q&A | `low` | (none) | What does this function do? |

### Decision Rule

If the task requires reasoning across 5+ files, involves security/architecture, or has multiple possible root causes — use `ultrathink`. For everything else, default `high` is sufficient.

---

## Thinking Display Modes

| Mode | What You See | Token Cost | Speed |
|------|-------------|------------|-------|
| Full | Complete thinking chain | Full billing | Slower |
| Summarized | Condensed thinking summary | Full billing | Moderate |
| Omitted | No thinking shown | Full billing | Fastest |

**Note:** All modes bill the same amount — the difference is only in what's streamed to you.

---

## Sources

- [Adaptive Thinking (official Anthropic docs)](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)
- [What's New in Claude 4.6](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6)
- [Claude Code Changelog](https://code.claude.com/docs/en/changelog)

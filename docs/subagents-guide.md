# Claude Code Subagents — Complete Reference

> **Last updated:** 26 March 2026 | **Claude Code version:** 2.1.83

Subagents are autonomous Claude Code instances spawned from the main session to handle specific tasks in parallel. Each subagent gets its own context window, tool access, and can run a different model.

---

## Table of Contents

- [What Are Subagents?](#what-are-subagents)
- [When to Use Subagents](#when-to-use-subagents)
- [Spawning Subagents](#spawning-subagents)
- [Agent Tool Parameters](#agent-tool-parameters)
- [Tool Inheritance](#tool-inheritance)
- [Model Routing](#model-routing)
- [Parallel Execution](#parallel-execution)
- [Defining Agents in Markdown](#defining-agents-in-markdown)
- [Subagents vs Agent Teams](#subagents-vs-agent-teams)

---

## What Are Subagents?

A subagent is a **child Claude Code process** spawned by the main session (the "parent"). It:

- Gets its own context window (separate from the parent)
- Has access to a configurable set of tools
- Can run a different model than the parent
- Returns a single result back to the parent
- Is ephemeral — destroyed when it completes

**Key property:** Subagents protect the parent's context. Heavy file reads, searches, and explorations happen in the subagent's context, and only the summary comes back.

---

## When to Use Subagents

| Scenario | Use Subagent? | Why |
|----------|:---:|-----|
| Search codebase for a pattern | Yes | Keeps search results out of main context |
| Read 10+ files to answer a question | Yes | Heavy reading stays in subagent |
| Simple single-file edit | No | Overhead not worth it |
| Parallel independent tasks | Yes | Multiple subagents run simultaneously |
| Task requiring different model | Yes | Route to Haiku for cheap, Opus for hard |
| Research that may take many steps | Yes | Protects main context from exploration |

---

## Spawning Subagents

Subagents are spawned via the **Agent tool** in Claude Code:

```
Agent tool parameters:
- description: "Short 3-5 word summary"
- prompt: "Detailed task description"
- model: "sonnet" | "opus" | "haiku" (optional)
- subagent_type: "specific-agent-type" (optional)
- run_in_background: true | false (optional)
- isolation: "worktree" (optional)
```

### Foreground (blocking)

```
Use Agent tool:
  description: "Find auth middleware"
  prompt: "Search the codebase for authentication middleware and summarize how it works"
```

The parent waits for the result before continuing.

### Background (non-blocking)

```
Use Agent tool:
  description: "Run test suite"
  prompt: "Run all unit tests and report results"
  run_in_background: true
```

The parent continues working. Gets notified when the subagent completes.

### With Worktree Isolation

```
Use Agent tool:
  description: "Refactor auth module"
  prompt: "Refactor the auth module to use JWT rotation"
  isolation: "worktree"
```

Creates a temporary git worktree so the subagent works on an isolated copy. If changes are made, the worktree path and branch are returned.

---

## Agent Tool Parameters

| Parameter | Type | Required | Description |
|-----------|------|:---:|-------------|
| `description` | string | Yes | 3-5 word task summary |
| `prompt` | string | Yes | Complete task description |
| `model` | `"sonnet"` \| `"opus"` \| `"haiku"` | No | Override model selection |
| `subagent_type` | string | No | Use a specific agent definition |
| `run_in_background` | boolean | No | Run without blocking parent |
| `isolation` | `"worktree"` | No | Run in isolated git worktree |

---

## Tool Inheritance

Subagents can have **restricted tool access** compared to the parent:

### Built-in Agent Types

| Agent Type | Tools Available | Best For |
|-----------|----------------|----------|
| `Explore` | Read, Glob, Grep, Bash (read-only) | Codebase exploration, research |
| `Plan` | Read, Glob, Grep, Bash (read-only) | Architecture planning |
| `general-purpose` | All tools | General tasks |

### Custom Agent Definitions

In markdown agent files, you can configure:

```markdown
---
name: my-agent
tools:
  - Read
  - Grep
  - Glob
disallowedTools:
  - Write
  - Edit
  - Bash
---
```

**Allowlist approach:** List only the tools the agent can use with `tools`.

**Denylist approach:** List tools to exclude with `disallowedTools`.

### Frontmatter Options (v2.1.78+)

```markdown
---
name: my-agent
effort: low          # Thinking effort level
maxTurns: 20         # Maximum tool-use turns
disallowedTools:     # Tools this agent cannot use
  - Write
  - Edit
---
```

---

## Model Routing

Route subagents to different models based on task complexity:

| Task Type | Recommended Model | Rationale |
|-----------|------------------|-----------|
| File search, grep, exploration | `haiku` | Fast, cheap, good enough |
| Single-file edits, standard coding | `sonnet` | Balanced quality/cost |
| Architecture, security, complex debugging | `opus` | Needs deep reasoning |
| Doc generation, formatting | `haiku` | Doesn't need deep reasoning |
| Code review | `sonnet` or `opus` | Depends on complexity |

### Escalation Pattern

Start with `sonnet`. If the result is poor, retry with `opus`:

```
1. Spawn subagent with model: sonnet
2. Evaluate result
3. If insufficient → retry same task with model: opus
4. Maximum 3 retrieval cycles per subagent
```

---

## Parallel Execution

Multiple subagents can run simultaneously for independent tasks:

### Pattern: Parallel Research

```
Spawn 3 subagents in parallel:

Agent 1: "Search for all API endpoints in src/api/"
Agent 2: "Find all database queries in src/models/"
Agent 3: "List all test files and their coverage"

All three run simultaneously → results synthesized by parent
```

### Pattern: Parallel Implementation

```
Agent 1: "Implement the backend API endpoint" (worktree isolation)
Agent 2: "Write the frontend component" (worktree isolation)
Agent 3: "Write tests for both" (worktree isolation)
```

### Rules for Parallel Execution

- **Independence:** Only parallelize truly independent tasks
- **No file conflicts:** Each agent should touch different files
- **Worktree isolation:** Use `isolation: "worktree"` for write operations
- **Result synthesis:** Parent should validate and integrate results

---

## Defining Agents in Markdown

Custom agents are defined as markdown files in plugin directories:

```markdown
---
name: security-reviewer
description: Reviews code for security vulnerabilities
model: opus
tools:
  - Read
  - Grep
  - Glob
  - Bash
effort: high
maxTurns: 30
---

# Security Reviewer Agent

## Role
You are a security expert reviewing code for OWASP Top 10 vulnerabilities.

## What to Check
1. SQL injection
2. XSS vulnerabilities
3. Authentication bypasses
4. Insecure deserialization
5. Security misconfigurations

## Output Format
For each finding:
- Severity: Critical / High / Medium / Low
- Location: file:line
- Description: What the vulnerability is
- Fix: How to remediate
```

---

## Subagents vs Agent Teams

| Feature | Subagents | Agent Teams |
|---------|-----------|-------------|
| **Communication** | Report to parent only | Direct teammate messaging |
| **Coordination** | Parent-managed | Shared task list |
| **Context** | Own window, summary back | Fully independent |
| **Persistence** | Ephemeral | Session-scoped |
| **Token cost** | Lower | Higher (scales with team size) |
| **Setup** | No setup needed | Requires env var flag |
| **Best for** | Research, parallel reads | Complex multi-agent projects |

**Rule of thumb:**
- < 3 parallel tasks with simple coordination → **Subagents**
- 3-5 parallel tasks with inter-task dependencies → **Agent Teams**

---

## Sources

- [Claude Code Agent Tool (official)](https://code.claude.com/docs/en/)
- [Agent Definitions](https://code.claude.com/docs/en/plugins#agents)
- [Agent Teams Guide](./agent-teams-guide.md)

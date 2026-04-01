# Subagent Catalog — 127+ Drop-In Specialist Definitions

> A library of agent definitions you can install in seconds

## Overview

A collection of 127+ specialist agent definitions across 10 categories. Each is a single `.md` file. Drop it into `~/.claude/agents/` (global) or `.claude/agents/` (project-level) and it works immediately.

Project-level agents override global ones with the same name.

---

## Agent File Format

```yaml
---
name: backend-developer
description: "Use when implementing server-side logic, APIs, and databases..."
tools: Read, Write, Edit, Bash, Glob, Grep
model: sonnet
---

## Role
You are a backend development specialist...

## Workflow
1. Analysis — Query context, understand requirements
2. Implementation — Build the solution
3. Validation — Verify quality against targets
```

**Three fields that matter:**

| Field | Purpose | Example |
|-------|---------|---------|
| `description` | Routing signal — Claude reads this to pick the right agent | "Use when implementing REST APIs..." |
| `tools` | Permission boundary — minimum necessary per role | `Read, Grep, Glob` for reviewers |
| `model` | Cost control — `haiku` (cheap), `sonnet` (balanced), `opus` (powerful) | `sonnet` for most coding |

---

## The 10 Categories

| # | Category | Count | Covers |
|---|----------|-------|--------|
| 1 | Core Development | 15+ | Backend, frontend, fullstack, mobile, APIs, databases |
| 2 | DevOps | 12+ | CI/CD, Docker, Kubernetes, cloud, SRE |
| 3 | Data & AI | 10+ | Pipelines, data science, ML, MLOps |
| 4 | Security | 8+ | Auditing, pen testing, compliance, chaos engineering |
| 5 | Quality | 8+ | QA, test automation, performance, accessibility |
| 6 | Product | 8+ | Product management, UX, UI, content strategy |
| 7 | Business | 10+ | Analysis, market research, competitive intelligence |
| 8 | Specialized | 15+ | Blockchain, IoT, games, healthcare, fintech |
| 9 | Meta-Orchestration | 8 | Coordinator, task distributor, error handler, knowledge graph |
| 10 | IT Operations | 8+ | PowerShell, Active Directory, Azure, M365 |

Category 9 is architecturally distinct — it contains agents whose sole purpose is managing the other 120+ agents. This creates a two-tier system: workers (categories 1–8, 10) and coordinators (category 9).

---

## Orchestration Patterns

**Sequential Pipeline:** `api-designer → backend-developer → frontend-developer → qa-expert`

**Parallel Assessment:** `security-auditor + pen-tester + compliance-auditor` all run simultaneously.

**Hub-and-Spoke:** Category 9 coordinator delegates to specialists and merges results.

**Domain Dispatch:** IT ops orchestrator routes to PowerShell, AD, Azure, or M365 specialists based on problem type.

---

## Patterns Worth Adopting

1. **Embedded KPIs** — Every agent has concrete targets in its prompt: "latency <50ms", "completion rate >99%". Forces self-measurement.

2. **Context-first protocol** — Every agent queries existing context before acting. Built into the three-phase workflow.

3. **Distributed collaboration graph** — Each agent declares its own partners: "Receives from X, collaborates with Y, hands off to Z." No centralized routing table needed.

4. **Model cost tiers** — `haiku` for coordination tasks, `sonnet` for implementation, `opus` only for deep analysis and security review.

---

## Quick Start

```bash
# Copy specific agents
cp categories/01-core-development/backend-developer.md ~/.claude/agents/

# Or use the interactive installer
bash install-agents.sh
```

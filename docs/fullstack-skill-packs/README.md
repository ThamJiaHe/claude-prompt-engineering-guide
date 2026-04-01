# Fullstack Skill Packs — 66 Specialized Developer Skills

> Drop-in skill packages for Claude Code covering every full-stack development domain

## What This Is

A Claude Code plugin with **66 specialized skills** and **9 project workflow commands**. Skills auto-activate based on keywords in your prompt, load a lightweight summary first, then pull detailed reference files on demand. This progressive disclosure architecture reduces token usage by ~50%.

Compatible with 42+ AI coding agents via the AgentSkills specification.

---

## Installation

```bash
# Plugin marketplace
/plugin marketplace add

# Direct from GitHub
/plugin install gh:

# Manual
cp -r skills/ ~/.claude/skills/
```

---

## All 66 Skills

### Languages (12)
`python-pro`, `typescript-pro`, `javascript-pro`, `golang-pro`, `rust-engineer`, `sql-pro`, `cpp-pro`, `swift-expert`, `kotlin-specialist`, `csharp-developer`, `php-pro`, `java-architect`

### Backend Frameworks (7)
`nestjs-expert`, `django-expert`, `fastapi-expert`, `spring-boot-engineer`, `laravel-specialist`, `rails-expert`, `dotnet-core-expert`

### Frontend & Mobile (7)
`react-expert`, `nextjs-developer`, `vue-expert`, `vue-expert-js`, `angular-architect`, `react-native-expert`, `flutter-expert`

### Infrastructure (5)
`kubernetes-specialist`, `terraform-engineer`, `postgres-pro`, `cloud-architect`, `database-optimizer`

### APIs & Architecture (7)
`graphql-architect`, `api-designer`, `websocket-engineer`, `microservices-architect`, `mcp-developer`, `architecture-designer`, `feature-forge`, `spec-miner`

### Quality (5)
`test-master`, `playwright-expert`, `code-reviewer`, `code-documenter`, `debugging-wizard`

### DevOps (5)
`devops-engineer`, `monitoring-expert`, `sre-engineer`, `chaos-engineer`, `cli-developer`

### Security (3)
`secure-code-guardian`, `security-reviewer`, `fullstack-guardian`

### Data & ML (6)
`pandas-pro`, `spark-engineer`, `ml-pipeline`, `prompt-engineer`, `rag-architect`, `fine-tuning-expert`

### Platforms (4)
`salesforce-developer`, `shopify-expert`, `wordpress-pro`, `atlassian-mcp`

### Specialized (3)
`legacy-modernizer`, `embedded-systems`, `game-developer`

### Critical Thinking (2)
`the-fool` — challenges your ideas using 5 reasoning modes (Socratic, Dialectic, Pre-mortem, Red Team, Falsification). Does not write code.

`spec-miner` — reverse-engineers specifications from existing undocumented code.

---

## Skill Structure

Two-tier progressive disclosure:

```
skills/react-expert/
  SKILL.md                  ← Tier 1: ~80-100 lines, always loaded
  references/
    server-components.md    ← Tier 2: 100-600 lines, loaded on demand
    react-19-features.md
    state-management.md
```

### SKILL.md Format

```yaml
---
name: react-expert
description: React and Next.js specialist. Use when building components, hooks, or server-side rendering.
license: MIT
metadata:
  domain: frontend
  triggers: React, JSX, hooks, useState, Server Components
  role: specialist
  related-skills: fullstack-guardian, test-master
---
```

**Body sections (fixed order):**
1. Role definition (1–2 lines)
2. When to Use This Skill
3. Core Workflow (5 steps with validation checkpoints)
4. Reference Guide (table mapping topics to reference files)
5. Key Patterns (inline code examples)
6. Constraints (MUST DO / MUST NOT DO)
7. Output Templates

---

## The Description Trap

Critical skill authoring rule: **never put workflow steps in the `description` field.**

The description should contain only capability verbs and trigger conditions. The process lives in the SKILL.md body. When descriptions contain steps, agents follow the brief description and skip the full skill content entirely.

CI validates this: `validate-skills.py` checks that descriptions follow the "Use when..." pattern.

---

## Project Workflow Commands (9)

Five phases plus an on-demand calibration tool:

| Phase | Command | Purpose |
|-------|---------|---------|
| Intake | `/intake` | Capture requirements |
| Discovery | `/discovery` | Research and analysis |
| Planning | `/planning` | Architecture and design |
| Execution | `/execution` | Implementation |
| Retrospectives | `/retrospectives` | Review and lessons |
| On-demand | `/common-ground` | Reveal Claude's hidden assumptions about your project |

The `/common-ground` command is particularly useful — it surfaces what Claude assumes about your project before work begins, preventing misaligned effort.

---

## Notable Design Decisions

- **Bidirectional cross-references** — CI checks that if skill A references skill B, skill B references back. Keeps the graph consistent.
- **`feature-forge` + `spec-miner` pair** — Forward (requirements → spec) and reverse (code → spec) specification tools that cross-reference each other.
- **Path-based auto-activation** — Skills specify glob patterns in `paths` frontmatter. They only load when you're working with matching files.
- **`allowed-tools` restriction** — Some skills limit which Claude tools they can use, acting as a security boundary.

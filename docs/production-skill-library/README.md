# Production Skill Library — 205 Skills Across 9 Domains

> The largest open-source collection of AI coding agent skill packages (7,700+ stars)

## What This Is

205 production-ready skill packages for Claude Code, Gemini CLI, OpenAI Codex, Cursor, Aider, Windsurf, and 5 other tools. Not an application — a deployable library of modular instruction packages. All MIT-licensed.

---

## Installation

```bash
# Claude Code plugin
/plugin marketplace add

# Gemini CLI
./scripts/gemini-install.sh

# OpenAI Codex
npx agent-skills-cli add --agent codex

# Convert for any tool
./scripts/convert.sh --tool all
```

---

## The 9 Domains

### 1. Engineering — Core (30 skills)
Role-based personas: `senior-architect`, `senior-frontend`, `senior-backend`, `senior-fullstack`, `senior-qa`, `senior-devops`, `senior-secops`, `senior-security`, `senior-ml-engineer`, `senior-data-engineer`, plus `playwright-pro` (9 sub-skills), `self-improving-agent`, `tdd-guide`, `tech-stack-evaluator`, cloud architects for AWS/Azure/GCP, and more.

### 2. Engineering — Advanced (35 skills)
Capability-based tools: `agent-designer`, `rag-architect`, `database-designer`, `mcp-server-builder`, `ci-cd-pipeline-builder`, `helm-chart-builder`, `terraform-patterns`, `skill-security-auditor`, `observability-designer`, `monorepo-navigator`, `saas-scaffolder`, `runbook-generator`, and more.

### 3. Marketing (43 skills, 7 pods)
Content creation, SEO, conversion optimization, channel management, growth tactics, competitive intelligence, and sales support. Covers everything from `cold-email` to `app-store-optimization`.

### 4. C-Level Advisory (28 skills)
A complete virtual executive team: CEO, CTO, COO, CPO, CMO, CFO, CRO, CISO, CHRO advisors plus `board-deck-builder`, `scenario-war-room`, `ma-playbook`, `culture-architect`, `founder-coach`, and more.

### 5. Product (14 skills)
`product-manager-toolkit`, `product-strategist`, `ux-researcher-designer`, `epic-design`, `experiment-designer`, `code-to-prd`, `context-engine`, and more.

### 6. Regulatory & Quality (13 skills)
ISO 13485, MDR 745, FDA, ISO 27001, GDPR, SOC 2 compliance. Built for regulated industries (medical devices, healthcare, finance).

### 7. Project Management (6 skills)
`senior-pm`, `scrum-master`, `jira-expert`, `confluence-expert`, `atlassian-admin`, `atlassian-templates`

### 8. Business & Growth (4 skills)
`customer-success-manager`, `revenue-operations`, `sales-engineer`, `contract-and-proposal-writer`

### 9. Finance (2 skills)
`financial-analyst`, `saas-metrics-coach`

---

## Skill File Structure

```
<domain>/<skill-name>/
  SKILL.md              # Required — master instructions
  scripts/              # Optional — Python tools (stdlib-only, zero pip deps)
  references/           # Optional — deep knowledge bases
  assets/               # Optional — templates, sample data
```

### SKILL.md Rules

- Frontmatter: **only `name` + `description`**. No other fields allowed.
- Description must use trigger phrases ("Use when...") but never contain process steps.
- Expert persona opener: "You are an expert in X..."
- Multi-mode workflows: Build from Scratch / Optimize Existing / Situation-Specific
- Context-First pattern: check for domain context file before asking questions
- Under 500 lines. Overflow goes to `references/`.

### Stdlib-Only Python Constraint
All 268+ scripts use zero pip dependencies. Standard library only. This means skills run anywhere Python runs — no environment setup, no dependency conflicts.

---

## Quality Pipeline

Every skill goes through a 9-phase pipeline:

Intent → Research → Draft → Eval → Iterate → Compliance → Package → Deploy → Verify

The eval gate requires **>=85% pass rate AND >=+30% improvement** over a no-skill baseline. This is measured via Tessl CLI benchmarking.

---

## Notable Patterns

### Context Engine
Every domain has a context creation skill (`marketing-context`, `codebase-onboarding`, etc.) that generates a persistent context file. All other skills in that domain read this file first, eliminating repeated questioning.

### Board Meeting Simulation
The `board-meeting` skill runs a 6-phase structured deliberation: independent C-suite contributions with no cross-pollination, then critic analysis, then synthesis. Simulates executive decision-making for product and strategy decisions.

### Self-Auditing
The `skill-security-auditor` skill scans other skills for prompt injection, data exfiltration, supply chain risks, and privilege escalation. The library includes its own security scanner.

### Three Organizational Primitives

| Primitive | Purpose | Count |
|-----------|---------|-------|
| **Skills** | Domain expertise packages | 175+ |
| **Agents** | Orchestrate multiple skills | 16 |
| **Personas** | Identity-driven bundles | 3 (Startup CTO, Growth Marketer, Solo Founder) |

---

## Multi-Platform Architecture

Maintains parallel indexes for different tools:

| Platform | Format |
|----------|--------|
| Claude Code | Plugin marketplace JSON |
| OpenAI Codex | Skills index JSON |
| Gemini CLI | YAML frontmatter with color/emoji/vibe |
| Others | Auto-generated via `convert.sh` |

---

## Dual Engineering Tier

The split between core engineering (role-based: "senior-architect") and advanced engineering (capability-based: "rag-architect") is deliberate:

- **Core** = "who does the work" — team member personas
- **Advanced** = "what capability is needed" — targeted expertise

Choose based on whether you want a team simulation or a specialist tool.

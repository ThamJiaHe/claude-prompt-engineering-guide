# Claude Code Skills Catalog — Curated Top Skills

> **Last updated:** 26 March 2026 | **Claude Code version:** 2.1.83

The definitive curated catalog of the most impactful Claude Code skills from ClawHub/ECC, Superpowers, and community sources. Organized by category with install instructions and one-line descriptions.

---

## Table of Contents

- [How Skills Work](#how-skills-work)
- [Where to Find Skills](#where-to-find-skills)
- [Top Skills by Category](#top-skills-by-category)
  - [Code Review](#code-review)
  - [TDD & Testing](#tdd--testing)
  - [Architecture & Planning](#architecture--planning)
  - [Build & Debug](#build--debug)
  - [Session Management](#session-management)
  - [Cleanup & Refactoring](#cleanup--refactoring)
  - [Security](#security)
  - [Database](#database)
  - [Frontend & Mobile](#frontend--mobile)
  - [Backend Patterns](#backend-patterns)
  - [DevOps & Infrastructure](#devops--infrastructure)
  - [AI & LLM Development](#ai--llm-development)
  - [Content & Documentation](#content--documentation)
  - [Git & PR Workflows](#git--pr-workflows)
  - [Prompt Engineering](#prompt-engineering)
- [Installing Skills](#installing-skills)
- [Creating Your Own](#creating-your-own)

---

## How Skills Work

Skills are markdown instruction files that teach Claude specific workflows. They cost **~5 tokens** until activated (vs MCP's ~42.6K), then load full instructions on demand via progressive disclosure.

```
~/.claude/skills/my-skill.md     # Personal skill
project/.claude/skills/skill.md  # Project skill
```

Skills are invoked via the `/skill-name` slash command or automatically triggered by matching prompts.

---

## Where to Find Skills

| Source | Skills Count | Install Method | Best For |
|--------|:-----------:|----------------|----------|
| **Everything Claude Code (ECC/ClawHub)** | 100+ | `/plugin install everything-claude-code` | Comprehensive coverage |
| **Superpowers (obra)** | 20+ | `/plugin marketplace add obra/superpowers-marketplace` | Planning, debugging, TDD |
| **PR Review Toolkit** | 8 | `/plugin install pr-review-toolkit` | Code review, PR analysis |
| **Incident Response** | 6 | `/plugin install incident-response` | Production issues |
| **Agent Teams** | 6 | `/plugin install agent-teams` | Multi-agent coordination |
| **Conductor** | 5 | `/plugin install conductor` | Multi-track orchestration |
| **Plugin Dev** | 7 | `/plugin install plugin-dev` | Building plugins/skills |
| **Hookify** | 3 | `/plugin install hookify` | Auto-generate hooks |
| **Community Skills** | Varies | Copy `.md` to `~/.claude/skills/` | Specialized workflows |

---

## Top Skills by Category

### Code Review

| Skill | Source | Description |
|-------|--------|-------------|
| `code-reviewer` | ECC | Language-agnostic code review after every change — quality, security, maintainability |
| `python-reviewer` | ECC | Python-specific: PEP 8, type hints, Pythonic idioms, security, performance |
| `go-reviewer` | ECC | Idiomatic Go, concurrency patterns, error handling, performance |
| `kotlin-reviewer` | ECC | Kotlin/Android: coroutine safety, Compose best practices, clean architecture |
| `security-reviewer` | ECC | OWASP Top 10, secrets detection, injection, unsafe crypto |
| `database-reviewer` | ECC | PostgreSQL query optimization, schema design, security, Supabase patterns |
| `code-review` | Superpowers | Requesting and receiving structured code review with plan verification |
| `code-review` | PR Review Toolkit | PR-focused review with CodeRabbit integration |
| `code-simplifier` | PR Review Toolkit | Simplify code for clarity while preserving functionality |

**Best starting point:** Install ECC, then `code-reviewer` runs automatically after every code change.

### TDD & Testing

| Skill | Source | Description |
|-------|--------|-------------|
| `tdd` / `tdd-workflow` | ECC | Full Red-Green-Refactor cycle with 80%+ coverage enforcement |
| `test-driven-development` | Superpowers | Strict TDD discipline with multi-agent coordination |
| `tdd-cycle` | TDD Workflows | Complete TDD cycle orchestration |
| `tdd-red` / `tdd-green` | TDD Workflows | Individual Red/Green phase skills |
| `e2e` / `e2e-runner` | ECC | End-to-end testing with Vercel Agent Browser + Playwright fallback |
| `verification-loop` | ECC | Run tests, fix failures, re-run until green |
| `e2e-testing-patterns` | Developer Essentials | E2E test architecture and patterns |
| `pr-test-analyzer` | PR Review Toolkit | Analyze PR test coverage quality |
| `python-testing` | ECC | Python testing patterns and coverage |
| `golang-testing` | ECC | Go test patterns and benchmarks |
| `bats-testing-patterns` | Shell Scripting | Bash/shell script testing |

**Best starting point:** `tdd-workflow` (ECC) for everyday use, `test-driven-development` (Superpowers) for strict discipline.

### Architecture & Planning

| Skill | Source | Description |
|-------|--------|-------------|
| `brainstorming` | Superpowers | Structured ideation before any feature work |
| `writing-plans` | Superpowers | Convert brainstorm output into executable implementation plans |
| `executing-plans` | Superpowers | Follow plans step-by-step with verification gates |
| `plan` / `planner` | ECC | Feature planning and complex refactoring |
| `blueprint` | ECC | Architecture blueprints for new systems |
| `architect` | ECC | System design, scalability, technical decisions |
| `feature-dev` | Feature Dev | Full feature development with exploration → architecture → implementation |
| `code-architect` | Feature Dev | Design feature architectures from existing codebase patterns |

**Best starting point:** Superpowers' `brainstorming` → `writing-plans` → `executing-plans` pipeline.

### Build & Debug

| Skill | Source | Description |
|-------|--------|-------------|
| `build-error-resolver` | ECC | Fix build/type errors with minimal diffs — get the build green fast |
| `go-build` | ECC | Go build, vet, and compilation error resolution |
| `gradle-build` | ECC | Android/Kotlin Gradle build error resolution |
| `systematic-debugging` | Superpowers | Multi-hypothesis debugging with evidence gathering |
| `debugging-strategies` | Developer Essentials | General debugging patterns and strategies |
| `silent-failure-hunter` | PR Review Toolkit | Find silent failures and inadequate error handling |
| `smart-fix` | Incident Response | Rapid production bug fix with impact assessment |
| `incident-response` | Incident Response | Full SRE incident triage and resolution |

**Best starting point:** `build-error-resolver` for build issues, `systematic-debugging` for complex bugs.

### Session Management

| Skill | Source | Description |
|-------|--------|-------------|
| `save-session` | ECC | Persist current session state to a file |
| `resume-session` | ECC | Resume a previously saved session with full context |
| `strategic-compact` | ECC | Smart `/compact` with context preservation strategy |
| `remembering-conversations` | Episodic Memory | Cross-session memory and recall |

**Best starting point:** `save-session` + `resume-session` for long-running work across context windows.

### Cleanup & Refactoring

| Skill | Source | Description |
|-------|--------|-------------|
| `refactor-cleaner` | ECC | Dead code cleanup using knip/depcheck/ts-prune |
| `skill-stocktake` | ECC | Audit installed skills for duplicates and conflicts |
| `simplify` | Superpowers | Review changed code for reuse, quality, efficiency |
| `legacy-modernize` | Framework Migration | Modernize legacy codebases with gradual migration |
| `finding-duplicate-functions` | Superpowers Lab | Detect and consolidate duplicate code |

### Security

| Skill | Source | Description |
|-------|--------|-------------|
| `security-reviewer` | ECC | OWASP Top 10, secrets, SSRF, injection, unsafe crypto |
| `security-scan` / `security-review` | ECC | Comprehensive security scanning |
| `security-hardening` | Security Scanning | Full security hardening workflow |
| `security-sast` | Security Scanning | Static Application Security Testing configuration |
| `stride-analysis-patterns` | Security Scanning | STRIDE threat modeling |
| `threat-mitigation-mapping` | Security Scanning | Map threats to mitigations |

### Database

| Skill | Source | Description |
|-------|--------|-------------|
| `database-reviewer` | ECC | PostgreSQL query optimization and schema review |
| `postgres-patterns` | ECC | PostgreSQL patterns and best practices |
| `database-migrations` | ECC | Safe migration patterns with rollback strategies |
| `sql-migrations` | Database Migrations | SQL migration generation and execution |
| `postgresql` | Database Design | Advanced PostgreSQL patterns |
| `sql-optimization-patterns` | Developer Essentials | Query performance tuning |
| `clickhouse-io` | ECC | ClickHouse analytics database patterns |

### Frontend & Mobile

| Skill | Source | Description |
|-------|--------|-------------|
| `frontend-patterns` | ECC | React/Next.js frontend architecture patterns |
| `nextjs-app-router-patterns` | Frontend Mobile | Next.js 15 App Router patterns |
| `tailwind-design-system` | Frontend Mobile | Tailwind CSS design system creation |
| `react-state-management` | Frontend Mobile | React state management strategies |
| `react-native-architecture` | Frontend Mobile | React Native cross-platform patterns |
| `android-clean-architecture` | ECC | Kotlin + Jetpack Compose MVVM |
| `swiftui-patterns` | ECC | SwiftUI patterns and practices |
| `compose-multiplatform-patterns` | ECC | Kotlin Multiplatform Compose |
| `frontend-design` | Frontend Design | UI/UX design implementation |
| `responsive-design` | UI Design | Responsive layout patterns |

### Backend Patterns

| Skill | Source | Description |
|-------|--------|-------------|
| `backend-patterns` | ECC | General backend architecture patterns |
| `django-patterns` | ECC | Django 5.x views, models, ORM, Celery |
| `django-tdd` / `django-security` | ECC | Django TDD and security patterns |
| `springboot-patterns` | ECC | Spring Boot application patterns |
| `springboot-tdd` / `springboot-security` | ECC | Spring Boot TDD and security |
| `docker-patterns` | ECC | Docker containerization patterns |
| `api-design` | ECC | REST/GraphQL API design principles |
| `fastapi-templates` | API Scaffolding | FastAPI project scaffolding |
| `microservices-patterns` | Backend Development | Microservices architecture |
| `event-store-design` | Backend Development | Event sourcing patterns |
| `saga-orchestration` | Backend Development | Saga pattern for distributed transactions |
| `workflow-orchestration-patterns` | Backend Development | Temporal/workflow orchestration |

### DevOps & Infrastructure

| Skill | Source | Description |
|-------|--------|-------------|
| `deployment-patterns` | ECC | Deployment strategies and patterns |
| `github-actions-templates` | CI/CD Automation | GitHub Actions workflow templates |
| `deployment-pipeline-design` | CI/CD Automation | CI/CD pipeline architecture |
| `terraform-module-library` | Cloud Infrastructure | Terraform module patterns |
| `multi-cloud-architecture` | Cloud Infrastructure | Multi-cloud design patterns |
| `cost-optimization` | Cloud Infrastructure | Cloud cost management (FinOps) |
| `istio-traffic-management` | Cloud Infrastructure | Istio service mesh configuration |
| `secrets-management` | CI/CD Automation | Secrets handling in pipelines |

### AI & LLM Development

| Skill | Source | Description |
|-------|--------|-------------|
| `rag-implementation` | LLM Application Dev | RAG system architecture and implementation |
| `prompt-engineering-patterns` | LLM Application Dev | Advanced prompting techniques |
| `langchain-architecture` | LLM Application Dev | LangChain application patterns |
| `embedding-strategies` | LLM Application Dev | Embedding model selection and optimization |
| `vector-index-tuning` | LLM Application Dev | Vector database index optimization |
| `hybrid-search-implementation` | LLM Application Dev | Hybrid semantic + keyword search |
| `llm-evaluation` | LLM Application Dev | LLM output evaluation frameworks |
| `cost-aware-llm-pipeline` | ECC | Token-efficient LLM application design |
| `ai-first-engineering` | ECC | AI-first software engineering patterns |
| `agentic-engineering` | ECC | Building agentic AI systems |

### Content & Documentation

| Skill | Source | Description |
|-------|--------|-------------|
| `article-writing` | ECC | Long-form article and blog post creation |
| `content-engine` | ECC | Content pipeline automation |
| `investor-materials` | ECC | Pitch decks and investor documentation |
| `doc-updater` | ECC | Documentation and codemap maintenance |
| `architecture-decision-records` | Documentation Generation | ADR creation and management |
| `changelog-automation` | Documentation Generation | Automated changelog generation |
| `openapi-spec-generation` | Documentation Generation | OpenAPI/Swagger spec generation |
| `writing-skills` | Superpowers | Creating new skills from scratch |
| `writing-clearly-and-concisely` | Elements of Style | Clear, concise technical writing |

### Git & PR Workflows

| Skill | Source | Description |
|-------|--------|-------------|
| `git-workflow` | Git PR Workflows | Branching, PRs, and merge strategies |
| `review-pr` | PR Review Toolkit | Comprehensive PR review |
| `finishing-a-development-branch` | Superpowers | Clean up and finalize a feature branch |
| `using-git-worktrees` | Superpowers | Parallel development with worktrees |
| `commit-push-pr` | Commit Commands | Streamlined commit → push → PR workflow |
| `commit` | Commit Commands | Smart commit with conventional messages |
| `git-advanced-workflows` | Developer Essentials | Advanced git patterns (bisect, rebase, cherry-pick) |

### Prompt Engineering

| Skill | Source | Description |
|-------|--------|-------------|
| `prompt-optimize` | LLM Application Dev | Optimize prompts for cost and quality |
| `prompt-engineering-patterns` | LLM Application Dev | Advanced prompting techniques catalog |
| `claude-api` | Skills | Build apps with Claude API/SDK |
| `skill-creator` | Skill Creator | Generate new skills from descriptions |
| `writing-skills` | Superpowers | Skill authoring best practices |

---

## Installing Skills

### Via Plugins (recommended)

```bash
# Install Everything Claude Code (100+ skills)
/plugin install everything-claude-code

# Install Superpowers (20+ skills)
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace

# Install PR Review Toolkit
/plugin install pr-review-toolkit

# Install Incident Response
/plugin install incident-response
```

### Manual Installation

Copy any `.md` skill file to your skills directory:

```bash
# Personal skills (all projects)
cp my-skill.md ~/.claude/skills/

# Project skills (this repo only)
cp my-skill.md .claude/skills/
```

### Verify Installation

```bash
# List all installed skills
/help skills

# Check a specific plugin's skills
/help everything-claude-code
```

---

## Creating Your Own

See the [Skills Guide](./skills-guide.md) for full documentation on creating skills.

Quick template:

```markdown
---
name: my-skill
description: One-line description of what this skill does
---

# My Skill

## When to Use
Describe trigger conditions.

## Instructions
Step-by-step workflow.

## Examples
Show input/output.
```

Use the `/skill-create` command (ECC) or `/create-plugin` (Plugin Dev) for guided creation.

---

## Sources

- [Everything Claude Code](https://github.com/anthropics/everything-claude-code)
- [Superpowers Plugin](https://github.com/obra/superpowers)
- [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills)
- [Skills Guide](./skills-guide.md)
- [Plugins Guide](./plugins-guide.md)

# The Everything Plugin — Agent Harness Performance System

> A comprehensive optimization system for AI coding agents (50K+ stars, 10+ months of production use)

## What This Is

Not just a config pack. A complete performance optimization system for AI agent harnesses: skills, instincts, memory optimization, continuous learning, security scanning, and research-first development workflows. Works across Claude Code, Codex, Cursor, OpenCode, and other harnesses.

997+ internal tests. 12 language ecosystems. 7 human language translations.

---

## What Is Inside

### Skills (~30)
Domain-specific expertise packages that auto-activate based on context:

| Skill | Domain |
|-------|--------|
| `agentic-engineering` | Eval-first execution, decomposition, cost-aware routing |
| `iterative-retrieval` | Progressive context refinement for subagents |
| `strategic-compact` | Intelligent context compression strategies |
| `verification-loop` | Checkpoint and continuous evaluation patterns |
| `tdd-workflow` | Test-driven development enforcement |
| `security-review` | Security scanning and vulnerability detection |
| `api-design` | API design patterns and best practices |
| `backend-patterns` | Server-side architecture patterns |
| `frontend-patterns` | Client-side architecture patterns |
| `frontend-slides` | Zero-dependency HTML presentation builder |
| `e2e-testing` | End-to-end test creation and maintenance |
| `eval-harness` | Evaluation harness construction |
| `coding-standards` | Language-specific coding standards |
| `deep-research` | Research-first development methodology |
| `mcp-server-patterns` | MCP server implementation patterns |
| `content-engine` | Content creation and management |
| `market-research` | Market analysis and competitive intelligence |
| `investor-materials` | Pitch deck and investor document creation |
| `documentation-lookup` | API reference research |

Each skill also ships an `agents/openai.yaml` for Codex compatibility.

### Agents (~20)
Specialized subagent definitions covering multiple languages:

- **Code reviewers** — General, TypeScript, Python, Go, Java, Kotlin
- **Build resolvers** — TypeScript, Go, Java, Kotlin, PyTorch
- **Workflow agents** — TDD guide, documentation updater, refactoring cleaner, E2E runner, security reviewer, database reviewer

### Commands
- `/feature-development` — Guided feature implementation
- `/database-migration` — Migration workflow
- `/add-language-rules` — Add language-specific coding rules
- `/configure-ecc` — Interactive installation wizard with merge/overwrite detection
- `/harness-audit` — Score your harness configuration
- `/security-scan` — Run AgentShield security analysis
- Plus PM2 and multi-agent commands (`/multi-plan`, `/multi-execute`, `/multi-backend`, `/multi-frontend`)

### Rules (12 Language Ecosystems)
Language-specific coding rules organized into:
- `common/` — Universal rules
- `typescript/`, `python/`, `golang/`, `java/`, `kotlin/`, `perl/`, `cpp/`, `rust/`, `php/` — Language-specific

Install only the languages you need.

### Hooks
- Session start with root fallback
- Stop-phase session summaries
- Script-based hooks (replacing fragile inline one-liners)
- Runtime controls: `ECC_HOOK_PROFILE=minimal|standard|strict`
- Selective disabling: `ECC_DISABLED_HOOKS=...`

---

## Key Concepts

### The Iterative Retrieval Pattern
Solves the "context problem" in multi-agent workflows. Subagents don't know what context they need until they start working. The pattern uses a 4-phase loop:

1. **DISPATCH** — Broad query to gather candidate files
2. **EVALUATE** — Assess relevance of retrieved context
3. **REFINE** — Narrow the query based on what was found
4. **LOOP** — Max 3 cycles, then proceed with best available context

### Agentic Engineering Principles
- Define completion criteria before execution
- Decompose work into agent-sized units (15-minute rule)
- Route model tiers by task complexity (Haiku → Sonnet → Opus)
- Measure with evals and regression checks
- Continue session for coupled units; fresh session after phase transitions
- Compact after milestones, not during active debugging

### Continuous Learning
Auto-extracts patterns from sessions into reusable "instincts." Confidence-scored, importable/exportable, with an evolution mechanism that promotes proven patterns.

### Verification Loops
Two types:
- **Checkpoint evals** — Run at defined milestones
- **Continuous evals** — Run after every change

Uses pass@k metrics and grader types to measure success.

---

## Installation

```bash
# Claude Code marketplace
/plugin install

# Selective install (new in v1.9)
# Uses manifest-driven pipeline — install only what you need
# State store tracks installed components for incremental updates
```

Also supports Codex (via AGENTS.md), Cursor, OpenCode (via plugin system), and Gemini CLI.

---

## Cross-Platform Architecture

The plugin ships cleanly across 5+ agent harnesses:

| Platform | Format |
|----------|--------|
| Claude Code | `.claude-plugin/plugin.json` + skills/ agents/ commands/ hooks/ rules/ |
| Codex | `.codex-plugin/plugin.json` + `.codex/AGENTS.md` + skills/*/agents/openai.yaml |
| Cursor | Plugin marketplace integration |
| OpenCode | `.opencode/` plugin with 20+ event hook types |
| Gemini CLI | Extension format |

---

## What Makes This Different

- **Harness performance, not just configs** — Focuses on optimizing how the agent harness works, not just what rules it follows
- **Instinct-based learning** — Sessions produce reusable patterns that evolve with confidence scoring
- **AgentShield security** — 1,282 security tests, 102 rules, integrated scanning via `/security-scan`
- **Selective installation** — Manifest-driven pipeline installs only what you need
- **12 language ecosystems** — TypeScript, Python, Go, Java, Kotlin, Perl, C++, Rust, PHP, and more
- **997+ tests** — Full validation suite across agents, skills, commands, hooks, and rules
- **GitHub App** — ECC Tools on GitHub Marketplace with free/pro/enterprise tiers

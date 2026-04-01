# Deep Research — Community Repository Analysis (April 2026)

> Comprehensive synthesis of 13 major Claude Code community repositories. Every repo analyzed, every file read, everything rewritten from scratch with current information.

---

## Guides by Category

### Plugins and Skill Systems

| Guide | What You Will Learn |
|-------|---------------------|
| [The Everything Plugin](./everything-plugin/README.md) | Agent harness performance system — 30 skills, 20 agents, 12 language ecosystems, instinct-based learning, 997+ tests |
| [The Plugin Framework](./plugin-framework/README.md) | Complete software development workflow — brainstorm → plan → TDD → subagent execution → code review → merge |
| [Production Skill Library](./production-skill-library/README.md) | 205 skills across 9 domains (engineering, marketing, C-suite, product, regulatory, PM). The largest open-source skill collection |
| [Fullstack Skill Packs](./fullstack-skill-packs/README.md) | 66 specialized developer skills with progressive disclosure architecture. Token usage reduced by ~50% |

### Agent Architecture and Orchestration

| Guide | What You Will Learn |
|-------|---------------------|
| [Subagent Catalog](./subagent-catalog/README.md) | 127+ drop-in specialist agent definitions across 10 categories. KPI injection, permission tiers, model cost routing |
| [Multi-Agent Orchestration](./multi-agent-orchestration/README.md) | Enterprise swarm platform — 4 topologies, 5 consensus algorithms, hive mind hierarchy, WASM-accelerated cost routing |
| [Agent Harness Fundamentals](./agent-harness-fundamentals/README.md) | Build AI agents from scratch in Python without any framework. 12-session curriculum from basic loop to multi-agent coordination |

### Reference and Configuration

| Guide | What You Will Learn |
|-------|---------------------|
| [Command and Config Reference](./command-and-config-reference/README.md) | All 64 slash commands, 13 frontmatter fields, settings hierarchy, hook events, agent file format |
| [System Prompt Anatomy](./system-prompt-anatomy/README.md) | How Claude Code assembles behavior from 110+ prompt components. Token counts, security model, verification system |
| [Model Routing](./model-routing/README.md) | Route Claude Code requests to any LLM provider. Cost optimization, transformer system, per-project routing |

### Ecosystem

| Guide | What You Will Learn |
|-------|---------------------|
| [Ecosystem Directory](./ecosystem-directory/README.md) | The most comprehensive catalog — 150+ tools, plugins, hooks, workflows, CLAUDE.md examples, and alternative clients |

### Source-Level Architecture (New — April 2026)

| Guide | What You Will Learn |
|-------|---------------------|
| [Core Claude Code Runtime](./core-claude-code-runtime/README.md) | Internal architecture from the March 2026 source disclosure — query engine, 40+ tools, 70+ commands, bridge system, memory system |
| [Claurst Integration](./claurst-integration/README.md) | Rust reimplementation of Claude Code — unreleased features (KAIROS, Buddy, ULTRAPLAN, autoDream), 14-file architecture spec, security findings |

---

## What Is New (Beyond the Original Sources)

These guides add the following information that was not in the original repositories:

1. **Unified frontmatter reference** — All 13 fields documented in one place with consistent descriptions across commands, skills, and agents

2. **Cross-repository skill comparison** — Three major skill libraries compared side by side (production library, fullstack packs, everything plugin) with their different design philosophies

3. **Updated model names** — All references updated to current Claude model family (Opus 4.6, Sonnet 4.6, Haiku 4.5)

4. **Token cost analysis** — System prompt component sizes documented with token counts, showing where context budget goes

5. **The Description Trap anti-pattern** — Documented across skill guides as a universal pitfall for skill authoring

6. **Consensus algorithm comparison** — Five algorithms compared side by side with fault tolerance characteristics

7. **Progressive disclosure as token engineering** — Identified as a cross-cutting pattern across multiple repositories

8. **Hook event complete list** — All 12 lifecycle events consolidated from multiple sources

9. **Unreleased feature documentation** — KAIROS, Buddy, ULTRAPLAN, and autoDream extracted from leaked source and documented (April 2026)

10. **Internal architecture details** — Query loop mechanics, tool permission model, context compression pipeline, and bridge protocol internals from source code (April 2026)

11. **Resource limits** — Hardcoded limits for images, PDFs, tool results, and task IDs compiled from source (April 2026)

12. **Internal naming** — Fast mode = "Penguin Mode", Computer Use = "Chicago", GrowthBook flag patterns (April 2026)

---

## Sources

These guides were synthesized from analysis of the following open-source repositories:

| # | Repository | Guide |
|---|-----------|-------|
| 1 | `affaan-m/everything-claude-code` | [Everything Plugin](./everything-plugin/README.md) |
| 2 | `musistudio/claude-code-router` | [Model Routing](./model-routing/README.md) |
| 3 | `shareAI-lab/learn-claude-code` | [Agent Harness Fundamentals](./agent-harness-fundamentals/README.md) |
| 4 | `shanraisshan/claude-code-best-practice` | [Command and Config Reference](./command-and-config-reference/README.md) |
| 5 | `VoltAgent/awesome-claude-code-subagents` | [Subagent Catalog](./subagent-catalog/README.md) |
| 6 | `alirezarezvani/claude-skills` | [Production Skill Library](./production-skill-library/README.md) |
| 7 | `obra/superpowers` | [Plugin Framework](./plugin-framework/README.md) |
| 8 | `Piebald-AI/claude-code-system-prompts` | [System Prompt Anatomy](./system-prompt-anatomy/README.md) |
| 9 | `hesreallyhim/awesome-claude-code` | [Ecosystem Directory](./ecosystem-directory/README.md) |
| 10 | `ruvnet/ruflo` | [Multi-Agent Orchestration](./multi-agent-orchestration/README.md) |
| 11 | `Jeffallan/claude-skills` | [Fullstack Skill Packs](./fullstack-skill-packs/README.md) |
| 12 | `Kuberwastaken/claurst` | [Claurst Integration](./claurst-integration/README.md) ← NEW |
| 13 | `tanbiralam/claude-code` | [Core Runtime](./core-claude-code-runtime/README.md) ← NEW |

All content has been rewritten from scratch. No text was copied verbatim from any source. Information has been updated to reflect the state of the Claude Code ecosystem as of April 1, 2026.

---

## How to Use These Guides

**If you are new to Claude Code:** Start with [Agent Harness Fundamentals](./agent-harness-fundamentals/README.md) and [Command and Config Reference](./command-and-config-reference/README.md).

**If you want to install skills:** Compare [Production Skill Library](./production-skill-library/README.md) (broadest), [Fullstack Skill Packs](./fullstack-skill-packs/README.md) (developer-focused), and [The Everything Plugin](./everything-plugin/README.md) (harness-focused).

**If you want multi-agent workflows:** Read [Subagent Catalog](./subagent-catalog/README.md) for agent definitions, [The Plugin Framework](./plugin-framework/README.md) for structured workflows, and [Multi-Agent Orchestration](./multi-agent-orchestration/README.md) for enterprise scale.

**If you want to understand how Claude Code works internally:** Read [Core Claude Code Runtime](./core-claude-code-runtime/README.md) for architecture, then [Claurst Integration](./claurst-integration/README.md) for unreleased features and the Rust reimplementation. Also read [System Prompt Anatomy](./system-prompt-anatomy/README.md).

**If you want to use cheaper models:** Read [Model Routing](./model-routing/README.md).

**If you want to discover tools:** Browse [Ecosystem Directory](./ecosystem-directory/README.md).

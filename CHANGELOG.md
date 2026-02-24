# Changelog

All notable changes to the Claude Prompt Engineering Guide will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.2.0] - 2026-02-24

### Added

#### New Model Coverage
- ✨ **Claude Opus 4.6** — Released Feb 5, 2026. Model ID `claude-opus-4-6-20250205`. Adaptive thinking, 128K max output, effort `max` level
- ✨ **Claude Sonnet 4.6** — Released Feb 17, 2026. Model ID `claude-sonnet-4-6-20250217`. Near-Opus performance at Sonnet pricing
- ✨ **Effort Parameter GA** — Now Generally Available across all models. No beta header required. New `max` level (Opus 4.6 only)
- ✨ **Adaptive Thinking** — `thinking: {type: "adaptive"}` auto-calibrates depth (Opus 4.6 only)

#### Claude Code v2.1.51
- ✨ **Agent Teams** — Multi-agent coordination with team-lead, team-implementer, team-reviewer, team-debugger
- ✨ **Git Worktree Isolation** — `--worktree` flag for parallel development in isolated branches
- ✨ **Claude Code Security** — Signed settings, network egress controls, `claude auth` CLI
- ✨ **Fast Mode** — `/fast` toggle for faster Opus 4.6 output ($30/$150 per MTok)
- ✨ **Claude in Chrome** — Browser automation via MCP extension
- ✨ **Automatic Memories** — Persistent memory across sessions
- ✨ **Session Forking** — Fork conversations to explore alternatives
- ✨ **`--from-pr` Flag** — Start Claude Code from PR context

### Changed

- 🔄 **API Guide** — Complete overhaul: Opus 4.6/Sonnet 4.6 models, effort GA (removed beta header), adaptive thinking, corrected API version header to `2023-06-01`, updated pricing with Fast Mode and long context notes
- 🔄 **Claude-Prompt-Guide.md** — Updated models to 4.6, effort parameter from beta to GA, fixed knowledge cutoff to May 2025, corrected Haiku pricing ($1/$5), updated revenue to $14B ARR
- 🔄 **Claude Code Guide** — Updated to v2.1.51, npm install replaced with native installer, expanded features table with Agent Teams/worktree/Security/Fast Mode/Chrome
- 🔄 **Pricing Guide** — Fixed Haiku 4.5 pricing throughout ($0.25/$1.25 → $1/$5), added Opus 4.6/Sonnet 4.6 rows, Fast Mode pricing
- 🔄 **MCP Integration** — Updated ecosystem numbers (350+ → 8,610+ servers), model references in code examples
- 🔄 **README** — Expanded product scorecard to 18 products, updated all model references to 4.6, new Critical Issues section with prefill removal
- 🔄 **All URLs** — `docs.anthropic.com` → `platform.claude.com/docs` across all files
- 🔄 **All dates** — Updated to February 24, 2026

### Breaking Changes

- ⚠️ **Prefill Removal** — Opus 4.6 and Sonnet 4.6 return 400 error when prefilling assistant messages
- ⚠️ **Model Retirements** — Sonnet 3.7 and Haiku 3.5 retired February 19, 2026
- ⚠️ **npm Install Deprecated** — Claude Code now uses native installer (Homebrew/WinGet/curl)

### Fixed

- 🐛 **API Version Header** — Corrected `2024-01-01` to `2023-06-01` in api-guide.md
- 🐛 **Haiku Pricing** — Fixed from $0.25/$1.25 to $1/$5 per MTok across all guides
- 🐛 **Model Names** — Fixed "Sonnet 4" → "Sonnet 4.5/4.6", "Haiku 3.5" → "Haiku 4.5"
- 🐛 **Knowledge Cutoff** — Corrected from "January 2025" to "May 2025"

### Research Sources
- 📚 **8 parallel research agents** — Reddit, GitHub, X/Twitter, web, Anthropic official, community forums
- 📚 **Cross-validated** — All findings verified against official Anthropic announcements

---

## [2.1.0] - 2026-02-04

### Added

#### MCP Ecosystem Updates
- ✨ **MCP Apps Documentation** — UI rendering within Claude chat (charts, forms, dashboards) from Asana, Figma, Slack, and more (Jan 26, 2026)
- ✨ **MCP Tool Search** — Claude Code dynamically loads MCP tools, reducing token overhead by 95%
- ✨ **350+ Connectors** — Managed connector directory expanded from 50+ to 350+ sources
- ✨ **Pre-configured OAuth** — `--client-id`/`--client-secret` flags for MCP servers

#### Claude Code v2.1.x Features
- ✨ **Checkpoints Documentation** — Auto-save code states, 30-day retention, 3 rewind modes
- ✨ **18 New Features Documented** — `/teleport`, `/debug`, prompt suggestions, Shift+Enter, skill hot-reload, forked sub-agents, wildcard permissions, response language config, and more
- ✨ **Environment Variables** — `CLAUDE_CODE_TMPDIR`, `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS`

#### Cowork Enhancements
- ✨ **Plugins Section** — Productivity, Enterprise search, Sales, Finance bundles
- ✨ **Usage Limits Table** — Per-plan breakdown (Pro/Max 5x/Max 20x)
- ✨ **Chrome Integration** — Hybrid workflows with Claude in Chrome extension

#### Model Deprecation Tracking
- ✨ **Deprecation Table** — Opus 4, 4.1 removed from UI/Code; Claude 3 Opus retired Jan 5

### Changed

- 🔄 **MCP Integration Guide** — Corrected Claude.ai from "Limited/Not available" to full support with 350+ connectors; added MCP Apps section; updated beta header from `2025-04-04` to `2025-11-20`
- 🔄 **Claude Code Guide** — Updated version from v2.1.0 to v2.1.12; expanded /rewind with full checkpoints system; added v2.1.x features table
- 🔄 **Pricing Guide** — Fixed "Sonnet 4" → "Sonnet 4.5" and "Haiku 3.5" → "Haiku 4.5" throughout; split Max into 5x/20x tiers
- 🔄 **Cowork Guide** — Corrected availability (Max-only Jan 12, Pro added Jan 16); added architecture details (VZVirtualMachine)
- 🔄 **Migration Guide** — Added model deprecation table; updated dates
- 🔄 **README** — Expanded product scorecard from 8 to 13 products; updated all quick links; changed badge to Feb 2026
- 🔄 **All dates** — Updated to February 4, 2026

### Fixed

- 🐛 **MCP API Beta Header** — Corrected deprecated `mcp-client-2025-04-04` to current `mcp-client-2025-11-20`
- 🐛 **Model Names in Pricing** — 30+ incorrect "Sonnet 4" and "Haiku 3.5" references corrected
- 🐛 **Claude.ai MCP Status** — Was "Not currently available", now correctly shows full support

### Research Sources
- 📚 **25+ sources analyzed** — GitHub CHANGELOG, npm registry, official Anthropic announcements, community reports
- 📚 **Cross-validated** — All CRITICAL items verified against 3+ independent sources

---

## [2.0.3] - 2026-01-27

### Added

#### New Research Documentation
- ✨ **Ecosystem Tools Research** — OpenCode CLI, AirLLM, external coding agents comparison (`docs/research-opencode-clawbot-jan-2026.md`)
- ✨ **ultimate.claude** — Master system prompt for Claude projects with repo-specific rules

#### Planning Templates
- 📋 **task.md** — Living backlog template with Inbox, In Progress, Blocked, Done sections
- 📋 **progress.md** — Daily/weekly session log for context restoration
- 📋 **activity.md** — Chronological action timeline with hook integration

#### Tool Comparisons
- 🔧 **OpenCode CLI** — 75+ LLM providers, GitHub Copilot auth, vendor-agnostic workflows
- 🔧 **AirLLM** — 70B models on 4GB VRAM, edge inference, hybrid patterns with Claude
- 🔧 **External Agents** — OpenAI Codex, GitHub Copilot CLI integration patterns
- 🔧 **Decision Matrix** — When to use Claude Code vs OpenCode vs AirLLM

### Changed

- 🔄 **Claude-Prompt-Guide.md** — Added "Ecosystem Tools (January 2026)" section
- 🔄 **INDEX.md** — Added planning templates section and ecosystem tools links
- 🔄 **All dates** — Updated to January 27, 2026

### Research Notes

- 📚 **Clawdbot/Clawbot** — No evidence found in authoritative sources; may be misspelling or emerging project
- 📚 **OpenCode** — Gained official GitHub support January 16, 2026
- 📚 **Planning patterns** — Synthesized from Claude Code best practices documentation

---

## [2.0.2] - 2026-01-24

### Added

#### New Documentation Files
- ✨ **Research Report (Jan 2026)** — Comprehensive 8,500+ word institutional-grade research report (`docs/research-report-jan-2026.md`)
- ✨ **Ecosystem Market Analysis** — Market position, growth trajectory, competitive landscape (`docs/ecosystem-market-analysis.md`)
- ✨ **Pricing Comparison Guide** — Claude vs GPT-4 vs Gemini with ROI analysis (`docs/pricing-comparison-jan-2026.md`)
- ✨ **MCP Ecosystem Overview** — Complete MCP integration guide with examples (`docs/mcp-ecosystem-overview.md`)

#### Market Position Data
- 📊 **Enterprise Market Share** — Anthropic leads with 40% (vs OpenAI 27%, Google 21%)
- 📊 **Enterprise Coding Share** — Claude commands 54% of enterprise coding market
- 📊 **Revenue Data** — $10B in 2025, targeting $20-26B in 2026
- 📊 **SWE-bench Scores** — Claude Opus 4.5 achieves 80.9% verified, 74.4% Failing Fast

#### MCP Ecosystem Updates
- 🔌 **Scale Metrics** — "Tens of thousands" of community servers
- 🔌 **Governance** — Linux Foundation AAIF oversight
- 🔌 **Plugin Hubs** — 9,000+ plugins on ClaudePluginHub

#### Pricing Information
- 💰 **67% Cost Reduction** — Opus 4.5 now $5/$25 per 1M tokens
- 💰 **Prompt Caching** — Up to 90% savings on cache reads
- 💰 **Batch API** — 50% discount for async processing

### Changed

- 🔄 **Claude-Prompt-Guide.md** — Added January 2026 market position section, updated competitive analysis, added pricing tables
- 🔄 **Claude Code Section** — Updated to v2.1.0 with skill hot-reloading, session teleportation, 3x memory improvement
- 🔄 **MCP Section** — Updated with ecosystem scale ("tens of thousands" of servers)
- 🔄 **Skills Section** — Added marketplace statistics (96,400+ installs for top skill)
- 🔄 **All footers** — Updated to January 24, 2026

### Research Sources
- 📚 **50+ authoritative sources** analyzed
- 📚 **Official Sources** — Anthropic release notes, Economic Index, Agentic Coding Report
- 📚 **Industry Analysis** — Menlo Ventures, ZDNET, TrueFoundry, Failing Fast benchmarks
- 📚 **Technical Docs** — AWS Bedrock, Google Vertex AI, Vercel AI Gateway

---

## [2.0.1] - 2026-01-23

### Added

#### New Documentation
- ✨ **Healthcare Compliance Guide** — Comprehensive HIPAA-ready enterprise documentation (`docs/healthcare-compliance.md`)
- ✨ **Competitive Analysis Section** — Claude vs ChatGPT vs Gemini comparison (Jan 2026)
- ✨ **Safety Considerations Section** — 60-day behavioral study findings and known issues

#### Critical Issues Documentation
- ⚠️ **Usage Limits Crisis** — Max subscribers getting 80% less than promised (GitHub #16868, #17358)
- ⚠️ **Context Compression Regression** — Jan 14-19 breakdown documented (GitHub #354)
- ⚠️ **Quality Regression Reports** — Community findings integrated
- ⚠️ **Prompt Ignoring Bug** — Jan 13-15 incident (RESOLVED)

#### Healthcare & Enterprise
- 🏥 **HIPAA-Ready Enterprise** — BAA, zero data retention, AWS Bedrock integration
- 🏥 **Clinical Data Integration** — ICD-10, NPI Registry, Prior Authorization automation
- 🏥 **Implementation Checklist** — 4-phase compliance checklist
- 🏥 **ROI Metrics** — 60-70% documentation reduction, 18-month payback

#### Backend Architecture Updates
- 🔧 **Subagent Orchestration** — 3-tier hierarchy pattern (90.2% performance improvement)
- 🔧 **OAuth 2.0 + Step-up Authorization** — MCP Jan 15 enhancements
- 🔧 **Token Comparison Table** — Skills (5 tokens) vs MCP (42.6K tokens)
- 🔧 **Meta Skill-Creator** — Generate Skills from natural language

#### Competitive Analysis
- 📊 **Coding Accuracy** — Claude 93.7% vs GPT-4o 90.2% vs Gemini 71.9%
- 📊 **Context Windows** — Gemini 2M vs Claude 1M (Sonnet) vs 200K (standard)
- 📊 **Winner by Use Case** — Clear guidance on when to use each model

#### Safety & Known Issues
- 🛡️ **60-Day Behavioral Study** — Constraint circumvention findings
- 🛡️ **Architectural Violations** — CLAUDE.md rules being bypassed
- 🛡️ **Cowork Autonomy Implications** — Reduced oversight warnings
- 🛡️ **Community Workarounds** — Constraint enforcement patterns

### Changed

- 🔄 **All dates updated** — January 15 → January 23, 2026
- 🔄 **README Product Scorecard** — 4 Excellent, 2 Broken, 2 Emerging
- 🔄 **MCP Integration** — Added 50+ pre-built servers, OAuth 2.0 configuration
- 🔄 **Skills Guide** — Added subagent patterns, meta skill-creator section

### Research Sources
- 📚 **103+ sources analyzed** — GitHub, Reddit, official docs, community dashboards
- 📚 **Time Period** — Jan 15-23, 2026 (8 days of new data)
- 📚 **Expert Synthesis** — Cross-validated findings with linked references

---

## [2.0.0] - 2026-01-15

### Added

#### New Documentation
- ✨ **Claude Code Guide** — Comprehensive guide for Claude Code v2.1.0 CLI features
- ✨ **Self-Evolving CLAUDE.md Template** — Template for living documentation pattern
- ✨ **System Prompt Insights Section** — Analysis of Claude's 24K token system prompt
- ✨ **Migration Guide** — Nov 2025 to Jan 2026 migration documentation

#### New Features & Patterns
- 🚀 **Effort Parameter** — Claude Opus 4.5's `low/medium/high` effort control with API examples
- 🚀 **Skills Wrapper Pattern** — Token-efficient progressive disclosure architecture
- 🚀 **Hooks Best Practices** — Block-at-submit and input modification patterns
- 🚀 **Context7 MCP Configuration** — Up-to-date library documentation integration
- 🚀 **Dynamic MCP Loading** — Load/unload MCP servers during sessions

#### Claude Code v2.x Coverage
- ✨ Plan Mode with subagents for parallel execution
- ✨ `/rewind` and `/usage` commands
- ✨ GitHub Actions integration with `/install-github-app`
- ✨ 4-step workflow pattern (Research, Plan, Implement, Commit)
- ✨ Multi-window guidance for long-horizon projects
- ✨ Boris Cherny's advanced GitHub workflow documentation

### Changed

#### Model Updates
- 🔄 **Claude Opus 4.5** — Now the flagship model (Nov 24, 2025)
- 🔄 **Model Hierarchy** — Opus 4.5 > Sonnet 4.5 > Haiku 4.5
- 🔄 **API Examples** — Updated to use `claude-opus-4-5-20251101`

#### Environment Updates
- 🔄 **Claude Cowork** — New autonomous file management environment (Jan 12, 2026)
- 🔄 **SSE Deprecated** — Migrate to `streamableHttp` transport for MCP

#### Documentation Improvements
- 🔄 **Main Guide v2.0** — Updated with Opus 4.5, effort parameter, system prompt insights
- 🔄 **MCP Integration** — Context window management and Context7 configuration
- 🔄 **Skills Guide** — Wrapper pattern, progressive disclosure, skill scopes
- 🔄 **Superpowers Guide** — Hooks timing recommendations and input modification

### Fixed

- 🐛 Context window consumption warning for multiple MCP servers (67K token example)
- 🐛 Deprecated `--output-style` flag migration to `--append-system-prompt-file`

### Deprecated

- ⚠️ **SSE Transport** — Use `streamableHttp` instead
- ⚠️ **Output Style Flags** — Use system prompt files instead

### Documentation Coverage

#### Models Covered
- ✅ Claude Opus 4.5 (flagship, effort parameter)
- ✅ Claude Sonnet 4.5
- ✅ Claude Haiku 4.5

#### Environments Covered
- ✅ Claude.ai web interface
- ✅ Claude Desktop app
- ✅ Claude Code v2.1.0 (CLI/VS Code)
- ✅ Claude Cowork (autonomous file management)
- ✅ Claude API with effort parameter

#### New Integrations
- ✅ Context7 MCP (up-to-date library docs)
- ✅ GitHub Actions for Claude Code
- ✅ Self-evolving CLAUDE.md pattern

---

## [1.0.0] - 2025-11-19

### Added

#### Core Documentation
- ✨ **Main Comprehensive Guide** — Complete Claude Prompt Engineering Guide with 1000+ lines of reference material
- 📚 **Claude Models Overview** — Detailed comparison of Claude Opus, Sonnet, and Haiku models
- 🏗️ **10-Component Framework** — Anthropic's official prompt structure with detailed explanations
- 💡 **Advanced Techniques** — XML tagging, chain of thought, extended thinking, role prompting
- 🛠️ **Tool Integration** — MCP, Skills, and Superpowers comprehensive guides

#### Documentation Files
- 📖 [README.md](./README.md) — Professional guide landing page with badges and navigation
- 📋 [CONTRIBUTING.md](./CONTRIBUTING.md) — Comprehensive contribution guidelines
- 📜 [LICENSE](./LICENSE) — MIT License
- 📝 [CHANGELOG.md](./CHANGELOG.md) — Version history and updates

#### Examples & Templates
- 🎯 [Minimal Prompt Template](./templates/minimal-prompt-template.md) — Essential components for quick tasks
- 📋 [Comprehensive Prompt Template](./templates/comprehensive-prompt-template.md) — Full framework for complex projects
- 💻 [Coding Tasks Examples](./docs/examples/coding-tasks.md) — Prompts for software engineering
- 🔬 [Research Tasks Examples](./docs/examples/research-tasks.md) — Prompts for analysis and synthesis
- 📊 [Business Analysis Examples](./docs/examples/business-analysis.md) — Prompts for business use cases
- 📄 [Document Creation Examples](./docs/examples/document-creation.md) — Prompts for content generation

#### Documentation Guides
- 🚀 [Quick Start Guide](./docs/quick-start.md) — Getting started with Claude
- 🔌 [MCP Integration Guide](./docs/mcp-integration.md) — Model Context Protocol setup
- 💾 [Skills Guide](./docs/skills-guide.md) — Using Claude Skills
- ⚡ [Superpowers Guide](./docs/superpowers-guide.md) — Superpowers plugin usage
- 🌐 [API Guide](./docs/api-guide.md) — Claude API integration
- 🖥️ [Claude Code Guide](./docs/claude-code-guide.md) — CLI/IDE usage

#### GitHub Templates
- 🐛 [Bug Report Template](./.github/ISSUE_TEMPLATE/bug_report.md)
- ✨ [Feature Request Template](./.github/ISSUE_TEMPLATE/feature_request.md)
- 📝 [Pull Request Template](./.github/PULL_REQUEST_TEMPLATE.md)

#### Project Configuration
- 📂 [.gitignore](./.gitignore) — Git ignore rules for common files

### Features

- **Comprehensive Reference** — 1000+ lines of professional prompt engineering guidance
- **Official Framework** — Anthropic's 10-component prompt structure
- **Best Practices** — Specific techniques for Claude 4.x models (Opus, Sonnet, Haiku)
- **Real-World Patterns** — 5 complete pattern examples with code
- **Tool Integration** — MCP, Skills, Superpowers, and Perplexity guides
- **Environment Guides** — Optimal approaches for Claude.ai, Desktop, Code, and API
- **Ready-to-Use Templates** — Minimal and comprehensive prompt templates
- **Professional Documentation** — Well-structured guides with clear examples

### Documentation Coverage

#### Models Covered
- ✅ Claude Opus 4.1
- ✅ Claude Sonnet 4.5
- ✅ Claude Haiku 4.5
- ✅ Model comparison and selection guide

#### Environments Covered
- ✅ Claude.ai web interface
- ✅ Claude Desktop app
- ✅ Claude Code (CLI/VS Code)
- ✅ Claude API (direct integration)

#### Tools & Integrations
- ✅ Model Context Protocol (MCP)
- ✅ Claude Skills
- ✅ Superpowers plugin
- ✅ Perplexity MCP integration

#### Use Cases
- ✅ Code review and analysis
- ✅ Business analysis and strategy
- ✅ Long-horizon coding tasks
- ✅ Research and synthesis
- ✅ Document creation and presentations

---

## [Unreleased]

### Planned

- [ ] Interactive prompt builder web tool
- [ ] Video tutorials for key patterns
- [ ] Community contributed examples
- [ ] Advanced prompt optimization guide
- [ ] Benchmark/evaluation framework
- [ ] Domain-specific pattern collections
- [ ] Claude Cowork deep-dive guide
- [ ] Extended thinking patterns documentation

---

## Guidelines for Updates

### When to Update Version Numbers

- **MAJOR** (X.0.0): Significant structural changes, major new sections
- **MINOR** (1.X.0): New examples, guides, or minor improvements
- **PATCH** (1.0.X): Typo fixes, clarifications, link updates

### Adding New Entries

When updating this file, add entries following this format:

```markdown
### [Type] - Description

- ✨ Added: New feature or section
- 🔄 Changed: Modified or improved section  
- 🐛 Fixed: Bug fix or correction
- ⚠️ Deprecated: Feature being phased out
- 🗑️ Removed: Feature or section deleted
```

### Types

- ✨ **Added** — New content, features, or sections
- 🔄 **Changed** — Modifications to existing content
- 🐛 **Fixed** — Bug fixes, corrections, clarifications
- ⚠️ **Deprecated** — Feature being phased out
- 🗑️ **Removed** — Feature or section deleted
- 🚀 **Improved** — Performance or clarity enhancements
- 📚 **Documentation** — Documentation updates

---

## Contributing to Changelog

When submitting a PR, include a changelog entry describing your changes:

```markdown
## [Unreleased]

### Added
- New feature or content section

### Changed
- Modification to existing content

### Fixed
- Bug fix or clarification
```

---

## Release History

### Version 2.2.0 (February 2026 Model Update)

- **Release Date**: February 24, 2026
- **Status**: ✅ Stable
- **Changes**: Opus 4.6 and Sonnet 4.6 model coverage, effort parameter GA, adaptive thinking, Claude Code v2.1.51 (Agent Teams, worktree, Security, Fast Mode, Chrome), prefill removal breaking change, Haiku pricing corrections, URL migrations to platform.claude.com

### Version 2.1.0 (February 2026 Research Update)

- **Release Date**: February 4, 2026
- **Status**: ✅ Stable
- **Changes**: Research-driven update correcting critical outdated information (MCP beta header, model names, connector counts), adding MCP Apps documentation, checkpoints system, 18 new Claude Code v2.1.x features, model deprecation tracking, and Cowork plugin/usage documentation

### Version 2.0.0 (January 2026 Update)

- **Release Date**: January 15, 2026
- **Status**: ✅ Stable
- **Changes**: Major update with Claude Opus 4.5, effort parameter, Claude Cowork, Context7 MCP, self-evolving patterns, and comprehensive Claude Code v2.x documentation

### Version 1.0.0 (Initial Release)

- **Release Date**: November 19, 2025
- **Status**: ✅ Stable
- **Changes**: Initial comprehensive release with all core documentation

---

## Questions?

- 📖 See [CONTRIBUTING.md](./CONTRIBUTING.md) for update guidelines
- 💬 [Open an issue](https://github.com/yourusername/claude-prompt-engineering-guide/issues) with questions
- 🙏 Thank you for helping improve this guide!


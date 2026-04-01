# Claude Code Ecosystem Directory

> The most comprehensive catalog of tools, plugins, skills, hooks, and community resources

## Overview

A curated, daily-updated directory of everything built around Claude Code. Organized into 9 categories with automated quality validation. Resources are submitted via structured issue templates, automatically validated, and approved by maintainers.

---

## What Is Cataloged

| Category | Count | Contents |
|----------|-------|---------|
| Agent Skills | 19+ | Installable skill bundles and engineering plugins |
| Workflows | 32+ | Development methodologies, process guides, learning frameworks |
| Tooling | 48+ | CLI tools, IDE extensions, usage monitors, orchestrators, config managers |
| Status Lines | 5 | Custom prompt bar displays |
| Hooks | 11 | Event-driven automation, enforcement, and notifications |
| Slash Commands | 40+ | Drop-in command suites for version control, testing, docs, deployment |
| CLAUDE.md Files | 21+ | Real-world project configuration examples |
| Alternative Clients | 5 | Non-standard interfaces (desktop, TUI, tmux) |
| Official Docs | 3 | Anthropic's documentation and quickstarts |

---

## Notable Tools by Function

**Orchestrators:** Multi-workspace terminal managers, swarm coordination platforms, task decomposition systems, kanban agent UIs, Rust-based sandboxed CLIs.

**IDE Integrations:** VS Code, Neovim, Emacs (via LSP), cross-IDE frameworks.

**Usage Monitors:** Web dashboards, CLI trackers, conversation browsers, community leaderboards.

**Config Management:** Config linters, dead-rules detectors, profile switchers, cross-agent converters (Claude Code ↔ Cursor/Cline/Aider).

**Hooks:** TDD enforcement, prompt injection scanning, auto-approve for safe commands, desktop notifications, inter-agent communication, sound effects, quality enforcement SDKs (TypeScript, Python, PHP).

---

## Recurring Integration Patterns

1. **Hook lifecycle** — Tools tap into PreToolUse/PostToolUse/Stop events
2. **MCP servers** — Capabilities exposed as composable protocol servers
3. **Container isolation** — Docker-based sandboxing for autonomous agents
4. **Worktree parallelism** — Multiple Claude Code instances on separate branches
5. **Cross-agent config** — Auto-convert between Claude Code, Cursor, Cline, Aider
6. **Autonomous loop** — Agents iterate through tasks until done with safety guardrails (6+ implementations)

---

## Real-World CLAUDE.md Examples

21+ production CLAUDE.md files from actual projects:

**By language:** Rust, Kotlin/KMP, Go, Clojure, TypeScript, JavaScript, Python

**By domain:** Blockchain, macOS security, game AI, Git GUIs, component libraries

Useful as templates for configuring Claude Code in your own projects.

---

## Quality Standards

- Automated URL reachability and license detection
- Minimum 7-day repo age requirement
- Network calls outside Anthropic must be declared upfront
- Shell scripts require thorough inline comments
- Escalating cooldown for spam (up to permanent ban)
- Ships its own evaluation slash command for reviewing candidate repositories

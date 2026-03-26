# Claude Code Plugins — Complete Guide

> **Last updated:** 26 March 2026 | **Claude Code version:** 2.1.83

Plugins are the distribution layer for Claude Code extensions. A plugin bundles skills, agents, hooks, MCP servers, and slash commands into a single installable package.

---

## Table of Contents

- [What Are Plugins?](#what-are-plugins)
- [Plugins vs Skills vs MCP](#plugins-vs-skills-vs-mcp)
- [Installing Plugins](#installing-plugins)
- [Top Plugins (March 2026)](#top-plugins-march-2026)
- [Plugin Structure](#plugin-structure)
- [Creating a Plugin](#creating-a-plugin)
- [Plugin Marketplaces](#plugin-marketplaces)

---

## What Are Plugins?

A plugin is a **package that bundles multiple Claude Code extensions** into one installable unit. Think of it as an npm package for Claude Code.

A single plugin can contain:
- **Skills** — Markdown instruction sets that teach Claude specific workflows
- **Agents** — Subagent definitions with specialized tool access
- **Hooks** — Lifecycle event handlers (auto-format, lint, validate)
- **MCP servers** — External tool integrations
- **Slash commands** — Custom `/command` shortcuts
- **Settings** — Default permissions, model overrides

---

## Plugins vs Skills vs MCP

| Feature | Plugins | Skills | MCP Servers |
|---------|---------|--------|-------------|
| **What it is** | Package/distribution format | Markdown instruction module | External tool/data protocol |
| **Contains** | Skills + agents + hooks + MCP + commands | Instructions + examples | Tools + resources |
| **Install method** | `/plugin install` | Copy to `~/.claude/skills/` | JSON config |
| **Token cost** | Varies (sum of components) | ~5 tokens until activated | ~42.6K tokens (7 servers) |
| **Marketplace** | Yes (via plugin marketplaces) | Community sharing | Registry (1,864+ on FastMCP) |
| **Shareable** | Yes (git repos) | Yes (markdown files) | Yes (npm packages) |
| **Can include** | Everything | Just instructions | Just tools/resources |

**Rule of thumb:**
- **Need external tools or real-time data?** → MCP server
- **Need to teach Claude a specific workflow?** → Skill
- **Need to bundle multiple capabilities?** → Plugin

---

## Installing Plugins

### From a Marketplace

```bash
# Step 1: Add a marketplace
/plugin marketplace add obra/superpowers-marketplace

# Step 2: Install from that marketplace
/plugin install superpowers@superpowers-marketplace
```

### From a Git Repository

```bash
# Install directly from GitHub
/plugin install github:username/plugin-name
```

### Verify Installation

```bash
# List installed plugins
/plugin list

# Get help for a specific plugin
/help plugin-name
```

---

## Top Plugins (March 2026)

### Superpowers (by obra)

The most popular Claude Code plugin. Provides:
- Brainstorming, planning, and execution workflows
- Systematic debugging
- Code review pipelines
- Subagent-driven development
- Git worktree management
- Browser automation (Superpowers Chrome)

```bash
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

**Key skills:** `/brainstorm`, `/write-plan`, `/execute-plan`, `/systematic-debugging`, `/dispatching-parallel-agents`

### Everything Claude Code (ECC)

Comprehensive productivity plugin with 100+ skills:
- Code review (language-specific: Python, Go, Kotlin, TypeScript)
- Build error resolution
- TDD workflow
- Database review
- Security scanning
- Session save/resume
- Refactor and dead code cleanup
- E2E testing runner

```bash
/plugin install everything-claude-code
```

**Key skills:** `/claw`, `/tdd`, `/save-session`, `/resume-session`, `/plan`, `/e2e`

### Other Notable Plugins

| Plugin | Purpose |
|--------|---------|
| **pr-review-toolkit** | PR code review, test analysis, silent failure hunting |
| **agent-teams** | Team spawn, delegate, review, debug |
| **conductor** | Multi-track project orchestration |
| **incident-response** | Production incident triage and resolution |
| **plugin-dev** | Tools for building plugins |
| **hookify** | Generate hooks from conversation patterns |
| **sentry** | Sentry error tracking integration |
| **coderabbit** | AI code review integration |
| **figma** | Design-to-code workflows |

---

## Plugin Structure

A plugin is a directory (typically a git repo) with this structure:

```
my-plugin/
├── plugin.json              # Plugin manifest (required)
├── skills/                  # Skill definitions
│   ├── my-skill.md         # Skill file (frontmatter + instructions)
│   └── another-skill.md
├── agents/                  # Agent definitions
│   └── my-agent.md         # Agent with tool access config
├── hooks/                   # Hook configurations
│   └── hooks.json          # Hook event handlers
├── commands/                # Slash command definitions
│   └── my-command.md       # Custom /command
├── mcp/                     # MCP server configs
│   └── config.json         # MCP server declarations
└── README.md               # Plugin documentation
```

### plugin.json (Manifest)

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "What this plugin does",
  "author": "your-name",
  "skills": ["skills/my-skill.md"],
  "agents": ["agents/my-agent.md"],
  "hooks": "hooks/hooks.json",
  "commands": ["commands/my-command.md"]
}
```

### Skill File Format

```markdown
---
name: my-skill
description: One-line description of what this skill does
---

# My Skill

## When to Use
Describe when this skill should be activated.

## Instructions
Step-by-step instructions for Claude to follow.

## Examples
Show input/output examples.
```

### Agent File Format

```markdown
---
name: my-agent
description: One-line description
model: sonnet
tools:
  - Read
  - Grep
  - Glob
  - Bash
disallowedTools:
  - Write
  - Edit
---

# My Agent

Instructions for this agent...
```

---

## Creating a Plugin

### Quick Start

```bash
# Use the plugin-dev skill to scaffold a new plugin
/create-plugin
```

This walks you through creating the directory structure and manifest.

### Manual Creation

1. Create directory structure (see above)
2. Write `plugin.json` manifest
3. Add skills, agents, hooks as needed
4. Test locally:
   ```bash
   /plugin install /path/to/my-plugin
   ```
5. Publish to a marketplace or share via git

### Validation

```bash
# Validate plugin structure before publishing
/plugin validate
```

---

## Plugin Marketplaces

Plugin marketplaces are git repositories that index available plugins.

### Adding a Marketplace

```bash
/plugin marketplace add owner/marketplace-repo
```

### Browsing Available Plugins

```bash
/plugin marketplace list
```

### Creating a Marketplace

A marketplace is a git repo with an index file listing available plugins and their git URLs. See the [superpowers-marketplace](https://github.com/obra/superpowers-marketplace) as a reference implementation.

---

## Sources

- [Claude Code Plugins (official docs)](https://code.claude.com/docs/en/plugins)
- [Superpowers Plugin](https://github.com/obra/superpowers)
- [Plugin Development Guide](https://code.claude.com/docs/en/plugins#creating-plugins)

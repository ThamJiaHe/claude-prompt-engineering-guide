# Claude Cowork Guide

Autonomous desktop workflow automation with Claude.

> **Last Updated: January 23, 2026** | Covers Cowork (shipped Jan 12, 2026), macOS desktop agent, and autonomous workflow patterns

---

## What is Claude Cowork?

**Claude Cowork** is an autonomous desktop agent that can navigate your computer, manage files, and execute complex multi-step workflows with minimal intervention.

### Key Capabilities

- Autonomous task execution on desktop
- Folder access for file management
- VM sandbox for safe execution
- Multi-application workflow coordination
- Extended thinking for complex reasoning
- Browser automation and research

### Platform & Requirements

| Requirement | Details |
|-------------|---------|
| **Platform** | macOS only (as of Jan 2026) |
| **Plan** | Pro, Max, or Team plans |
| **Release** | Shipped January 12, 2026 |
| **Model** | Claude Opus 4.5 |

---

## Quick Start

### 1. Enable Cowork

1. Open Claude Desktop App
2. Navigate to **Settings > Cowork**
3. Enable autonomous mode
4. Configure folder access permissions

### 2. Basic Usage

```
You: "Organize my Downloads folder by file type and create summary reports"

Cowork will:
1. Scan Downloads folder
2. Create category subfolders
3. Move files to appropriate locations
4. Generate markdown summary
```

---

## Core Features

### Autonomous Task Execution

Cowork operates autonomously within defined boundaries:

```
You: "Research competitors and create a comparison spreadsheet"

Cowork process:
├── Opens browser
├── Searches for competitor information
├── Extracts relevant data
├── Creates spreadsheet
├── Formats and organizes data
└── Saves to specified location
```

### Folder Access

Configure which folders Cowork can access:

```
Allowed Folders:
├── ~/Documents/Projects/
├── ~/Downloads/
├── ~/Desktop/
└── Custom paths you specify
```

**Best Practice**: Grant minimal necessary access. Don't give access to sensitive directories like `~/.ssh` or credential stores.

### VM Sandbox

Cowork executes potentially risky operations in an isolated VM:

- Code execution happens in sandbox
- Network requests are monitored
- File system changes are contained
- Can preview changes before applying

---

## Workflow Patterns

### Pattern 1: Research & Compile

**Use Case**: Gather information and create reports

```
Prompt: "Research the top 5 project management tools,
compare their features, and create a recommendation report"

Cowork workflow:
1. Opens browser, searches for PM tools
2. Visits each tool's website
3. Extracts feature lists and pricing
4. Creates comparison table
5. Writes recommendation summary
6. Saves report to Documents
```

### Pattern 2: File Organization

**Use Case**: Batch file management

```
Prompt: "Sort all PDFs in Downloads by date,
rename with consistent format,
and move to organized folders"

Cowork workflow:
1. Scans Downloads for PDFs
2. Reads file metadata
3. Creates date-based folders
4. Renames files (YYYY-MM-DD_title.pdf)
5. Moves to appropriate folders
6. Generates log of changes
```

### Pattern 3: Multi-App Coordination

**Use Case**: Tasks spanning multiple applications

```
Prompt: "Extract data from this spreadsheet,
create charts, and build a presentation"

Cowork workflow:
1. Opens spreadsheet application
2. Reads and analyzes data
3. Creates visualization charts
4. Opens presentation software
5. Imports charts and adds context
6. Saves final presentation
```

---

## Safety Considerations

### Permissions Model

Cowork uses explicit permission grants:

| Permission Level | Access |
|-----------------|--------|
| **Read-only** | View files, browse web |
| **Read-write** | Modify files in allowed folders |
| **Execute** | Run scripts in sandbox |
| **Full** | All operations (use with caution) |

### Best Practices

1. **Start with minimal permissions** - Grant read-only first, expand as needed
2. **Use allowed folder lists** - Don't grant full disk access
3. **Review before applying** - Use preview mode for file operations
4. **Monitor execution** - Watch Cowork's actions, especially initially
5. **Sandbox code execution** - Always use VM for running code

### What Cowork Cannot Do

- Access credentials or API keys without explicit permission
- Modify system files or settings
- Send data externally without confirmation
- Execute outside sandbox without approval
- Access folders not in allowed list

---

## Comparison: Cowork vs Claude Code

| Feature | Claude Cowork | Claude Code |
|---------|---------------|-------------|
| **Environment** | Desktop GUI | Terminal CLI |
| **Primary Use** | General workflows | Software development |
| **Interaction** | Visual/autonomous | Command-driven |
| **File Access** | Configured folders | Full project access |
| **Code Execution** | VM sandbox | Direct execution |
| **MCP Support** | Limited | Full |
| **Platform** | macOS only | Cross-platform |

**When to use Cowork**: General productivity, research, file management, multi-app workflows

**When to use Claude Code**: Software development, coding tasks, git operations, terminal tasks

---

## Integration with Claude Code

Cowork and Claude Code can complement each other:

```
Workflow example:
1. Use Cowork for research and planning
2. Hand off technical specs to Claude Code
3. Claude Code implements the solution
4. Cowork handles documentation and deployment prep
```

---

## Troubleshooting

### Common Issues

**Issue**: Cowork cannot access folder
```
Solution: Check Settings > Cowork > Folder Access
Ensure the folder is in the allowed list
```

**Issue**: Tasks timeout
```
Solution: Break complex tasks into smaller steps
Use extended thinking for complex reasoning
```

**Issue**: Unexpected file changes
```
Solution: Enable preview mode
Review changes before applying
Use sandbox for testing
```

### Performance Tips

1. **Clear task descriptions** - Be specific about expected outcomes
2. **Staged execution** - Break large tasks into phases
3. **Regular checkpoints** - Request progress updates for long tasks
4. **Resource awareness** - Close unnecessary applications during heavy tasks

---

## Example Workflows

### Weekly Report Automation

```
Prompt: "Every Friday, compile my project updates from
the past week and create a status report"

Configuration:
- Schedule: Friday 4 PM
- Sources: ~/Documents/Projects/, Email, Calendar
- Output: ~/Documents/Reports/weekly/
- Format: Markdown + PDF
```

### Code Review Preparation

```
Prompt: "Gather all uncommitted changes in my projects,
create diff summaries, and prepare review notes"

Cowork will:
1. Scan project directories for git repos
2. Generate diff reports
3. Create summary documents
4. Organize by project
5. Add context notes
```

### Research Assistant

```
Prompt: "Research [topic], compile sources,
fact-check key claims, and create annotated bibliography"

Output:
├── sources.md (list of references)
├── summary.md (key findings)
├── fact_check.md (verification notes)
└── bibliography.md (formatted citations)
```

---

## Resources

- **Claude Desktop**: Download at [claude.ai/download](https://claude.ai/download)
- **Cowork Documentation**: Settings > Cowork > Help
- **Community Examples**: [Claude Discord](https://discord.gg/anthropic)

---

## Related Guides

- [Claude Code Guide](./claude-code-guide.md) - Terminal-based development
- [Skills Guide](./skills-guide.md) - Reusable Claude capabilities
- [MCP Integration](./mcp-integration.md) - External tool connections

---

**Last Updated:** January 23, 2026
**Version:** 1.0.0
**Status:** Production Ready

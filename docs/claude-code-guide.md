# Claude Code Guide

Master Claude Code CLI for agentic software development.

> **Last Updated: January 15, 2026** | Covers v2.1.0 features, GitHub Actions, and workflow patterns

---

## What is Claude Code?

**Claude Code** is an agentic coding tool that works in your terminal and IDE. It can read, write, and execute code, manage git operations, and perform complex multi-step tasks autonomously.

### Key Capabilities

- Terminal and VS Code integration
- Full filesystem access
- Git operations and version control
- MCP server support
- Subagents for parallel execution
- GitHub Actions integration
- Plan Mode for complex tasks

---

## Installation

```bash
# Install via npm
npm install -g @anthropic-ai/claude-code

# Verify installation
claude --version
```

**Current Version**: v2.1.0 (January 2026)

---

## Quick Start

```bash
# Interactive mode
claude

# Direct prompt
claude -p "Implement user authentication"

# With system prompt
claude --system-prompt "You are a security engineer" -p "Review this code"

# With MCP config
claude --mcp-config ./mcp-config.json -p "Search the codebase"
```

---

## Claude Code v2.x Features (Dec 2025 - Jan 2026)

### Plan Mode with Subagents

Plan Mode enables Claude to create structured plans before implementation:

```bash
# Activate Plan Mode
/plan "Build a REST API for user management"

# Claude will:
# 1. Analyze the task
# 2. Create detailed plan
# 3. Present for approval
# 4. Execute step by step
```

Subagents can execute plan steps in parallel when tasks are independent.

### /rewind Command

Undo code changes with a simple command:

```bash
# Undo last change
/rewind

# Undo specific number of steps
/rewind 3
```

**Note**: If experiencing performance issues, disable `/rewind` as a workaround.

### /usage Command

Monitor your plan limits and token usage:

```bash
/usage

# Shows:
# - Current token usage
# - Plan limits
# - Session statistics
```

### Automatic Continuation

When Claude hits output token limits, it automatically continues from where it left off. No manual intervention needed.

### GitHub Actions Integration

#### Quick Setup

```bash
# Run in Claude Code terminal
/install-github-app
```

This guides you through:
1. Installing GitHub app
2. Setting up required secrets
3. Configuring permissions

#### Requirements

- Must be repository admin
- GitHub app needs read/write permissions for:
  - Contents
  - Issues
  - Pull requests

#### GitHub Actions Workflow

```yaml
name: Claude Code

on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]

jobs:
  claude:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

---

## Recommended 4-Step Workflow Pattern

This pattern significantly improves success rates for complex tasks:

### Step 1: RESEARCH
```
Ask Claude to understand the problem:
- "What information do you need to solve this?"
- Let it read codebase, docs, related files
- Don't rush into implementation
```

### Step 2: PLAN
```
Create plan before coding:
- "Create a plan but don't code yet"
- Review plan before implementation
- Explicitly tell Claude NOT to code until approval
```

### Step 3: IMPLEMENT
```
Execute the plan:
- "Now implement your plan"
- Ask it to verify reasonableness as it codes
- Use Escape key to interrupt and course-correct
```

### Step 4: COMMIT & DOCUMENT
```
Finalize the work:
- "Commit the result and create a PR"
- "Update README and CHANGELOG with what you did"
```

### Why This Works

Without Steps 1-2, Claude jumps straight to coding. Research + Planning first significantly improves success rate.

---

## Course Correction Tools

### Escape Key
Press Escape to interrupt Claude mid-execution. Preserves context.

### Double-Tap Escape
Jump back in history, edit previous prompt.

### Ask Claude to Undo
```
"Undo your last changes and try X instead"
```

### Make a Plan First
Forces Claude to think before acting.

---

## Multi-Window Guidance

For long-horizon projects spanning multiple context windows:

```xml
<multi_window_guidance>
Your context window will be automatically compacted as it approaches its limit.
Do not stop tasks early due to token budget concerns.

Progress Tracking:
1. Save progress to progress.txt after each session
2. Commit work to git with descriptive messages
3. Update TODO.md with remaining tasks
4. Track test results in tests.json

When starting new session:
1. Review progress.txt
2. Check git log for recent work
3. Run tests to verify state
4. Continue with next priority task
</multi_window_guidance>
```

---

## State Tracking Best Practices

### Structured Formats

```json
{
  "tasks": [
    {"id": 1, "name": "Database schema", "status": "completed"},
    {"id": 2, "name": "API endpoints", "status": "in_progress"},
    {"id": 3, "name": "Frontend components", "status": "pending"}
  ],
  "tests": {
    "passing": 45,
    "failing": 3,
    "skipped": 0
  }
}
```

### Git for State Tracking

Claude 4.5 excels at using git to track state across sessions:
- Regular commits as checkpoints
- Descriptive commit messages
- Branch per feature
- PRs for review

---

## Advanced GitHub Workflow

Based on Boris Cherny's (Claude Code creator) workflow shared January 2026:

### Issue Creation (10-20 minutes for 4 issues)

Custom `/create-issue` command that:
- Parses user description
- Analyzes codebase context
- Identifies Git repository
- Explores relevant code
- Classifies issue type (Bug/Feature/Enhancement/Task)
- Breaks down into tasks
- Defines acceptance criteria
- Presents formatted preview

### Parallel Execution with Git Worktrees (15 minutes)

Custom `/solve-issue` command that:
- Takes GitHub issue URL
- Spins up new Git worktree
- Creates branch for issue
- Solves issue in small steps
- Commits after each step
- Documents changes in README/docs
- Creates PR ready for review

**Success Rate**: 90-95% on first attempts.

### Why It Works

- Detailed technical architecture before coding
- Comprehensive problem analysis
- Clear acceptance criteria
- Everything version controlled in Git
- Claude sandboxed to project directory

### Remote Worker Pattern

1. Create GitHub issue on phone
2. @ mention Claude in issue
3. By time you're back at desk, it's done

Example: "Create GitHub issue: 'Update timezone handling for Arizona'"
Claude sees issue via GitHub integration, implements fix, commits, creates PR.

---

## Configuration

### System Prompt File (Jan 2026 Best Practice)

Use `--append-system-prompt-file` instead of output style flags:

```bash
# OLD (deprecated)
claude --output-style=detailed

# NEW (recommended)
claude --append-system-prompt-file=~/.claude/system-prompt.md -p "Your prompt"
```

**Benefits**: Better prompt caching, consistent behavior.

### MCP Configuration

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp", "--api-key", "YOUR_KEY"]
    }
  }
}
```

---

## Common Issues & Workarounds (Jan 2026)

### Performance Degradation in Long Sessions

**Problem**: Console history accumulation after compaction causes progressive slowdown.

**Workarounds**:
- Restart Claude Code to clear state
- Disable `/rewind` if experiencing issues
- Migrate to `--append-system-prompt-file`
- Enterprise accounts can increase to 500K token budget

### Usage Limits (Jan 2026 Notice)

**Problem**: Multiple reports of reduced usage limits since January 1-8, 2026.

**Observations**:
- Opus 4.5 limits significantly reduced
- Max 5x/20x users hitting limits 3-5x faster
- Credit consumption increased 3-5x

**Workarounds**:
- Monitor usage with `/usage` command
- Consider Enterprise for higher limits
- Optimize prompts for token efficiency

---

## Best Practices

### DO:

- Use Plan Mode for complex tasks
- Commit frequently as checkpoints
- Use git worktrees for parallel development
- Test after each major change
- Document as you go

### DON'T:

- Skip the planning phase
- Work without version control
- Ignore test failures
- Let Claude work too long without checkpoints
- Use output style flags (deprecated)

---

## Learn More

- [Claude Code Documentation](https://code.claude.com/docs)
- [GitHub Actions Integration](https://code.claude.com/docs/en/github-actions)
- [MCP Integration Guide](./mcp-integration.md)
- [Skills Guide](./skills-guide.md)
- [Superpowers Guide](./superpowers-guide.md)

---

*Last Updated: January 15, 2026*

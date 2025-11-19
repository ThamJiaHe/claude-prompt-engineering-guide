# Superpowers Guide

Master advanced Claude Code capabilities with the Superpowers plugin.

---

## What is Superpowers?

**Superpowers** is a comprehensive plugin for Claude Code that unlocks advanced capabilities and productivity features. Created by [obra](https://github.com/obra), it provides tools for:

- 🎯 Advanced agentic workflows
- 🔍 Code analysis and optimization
- 📊 State tracking and memory
- 🚀 Performance optimization
- 🛠️ Development utilities

---

## Installation

### Step 1: Add Plugin Marketplace

```bash
/plugin marketplace add obra/superpowers-marketplace
```

### Step 2: Install Superpowers

```bash
/plugin install superpowers@superpowers-marketplace
```

### Step 3: Verify Installation

```bash
/help superpowers
```

---

## Key Features

### 1. Enhanced Code Analysis

Superpowers extends Claude Code's ability to:
- Analyze large codebases efficiently
- Find patterns across multiple files
- Optimize performance bottlenecks
- Identify technical debt

### 2. Advanced Workflows

- **Brainstorming Mode** — Structure complex problem-solving
- **Planning Mode** — Create detailed implementation plans
- **Execution Mode** — Track progress through long tasks
- **Review Mode** — Code review and quality assurance

### 3. State & Memory Management

```
Superpowers helps with:
- Tracking progress across sessions
- Maintaining context for long tasks
- Saving and recovering state
- Building incremental solutions
```

### 4. Performance Optimization

- Token budget optimization
- Context window management
- Efficient tool utilization
- Parallel operation coordination

---

## Using Superpowers Features

### Feature 1: Brainstorming

Use when exploring complex problems:

```bash
# Activate brainstorming mode
/superpowers:brainstorm

# Claude will help you:
# 1. Explore the problem from multiple angles
# 2. Develop competing hypotheses
# 3. Identify key uncertainties
# 4. Refine your approach
```

Example:
```
/superpowers:brainstorm "How should we architect a real-time analytics system?"

# Claude helps you think through:
# - Data ingestion patterns
# - Storage options
# - Query patterns
# - Scaling strategies
# - Cost considerations
```

### Feature 2: Planning

Create detailed implementation plans:

```bash
# Create a structured plan
/superpowers:write-plan

# Provides:
# - Detailed implementation steps
# - File-by-file changes
# - Code examples
# - Verification steps
# - Dependencies between tasks
```

Example:
```
/superpowers:write-plan "Implement user authentication system"

# Claude provides:
# 1. Database schema
# 2. API endpoints
# 3. Frontend components
# 4. Test strategy
# 5. Deployment approach
```

### Feature 3: Execution

Execute plans with checkpoints:

```bash
# Run a pre-planned implementation
/superpowers:execute-plan

# Claude will:
# 1. Load your plan
# 2. Execute tasks in sequence
# 3. Review work between tasks
# 4. Report progress
# 5. Handle issues that arise
```

### Feature 4: Code Review

Request comprehensive code reviews:

```bash
# Get detailed code review
/superpowers:requesting-code-review

# Claude reviews for:
# - Security vulnerabilities
# - Performance issues
# - Best practices violations
# - Architecture concerns
# - Test coverage
```

---

## Advanced Patterns

### Pattern 1: Multi-Window Development

For long-horizon projects spanning multiple context windows:

```xml
<multi_window_guidance>
This project will span multiple Claude Code sessions.

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

### Pattern 2: State Management

Track complex state across operations:

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
  },
  "metrics": {
    "lines_of_code": 2500,
    "test_coverage": 78,
    "performance": "within_targets"
  }
}
```

### Pattern 3: Incremental Delivery

Build features incrementally with verification:

1. **Plan** → Detailed implementation plan
2. **Build** → Create first feature increment
3. **Test** → Verify with automated tests
4. **Review** → Code quality check
5. **Commit** → Save to version control
6. **Repeat** → Next feature increment

---

## Superpowers Skills

Superpowers includes built-in **skills** for:

### Skill: Test-Driven Development
```bash
/superpowers:test-driven-development

Guides:
1. Write failing test first
2. Implement minimal code to pass
3. Refactor for quality
4. Verify test actually tests behavior
```

### Skill: Root Cause Analysis
```bash
/superpowers:root-cause-tracing

Helps:
1. Trace errors back to source
2. Identify why it happened
3. Fix the root cause (not symptom)
4. Prevent recurrence
```

### Skill: Systematic Debugging
```bash
/superpowers:systematic-debugging

Four phases:
1. Investigation (understand the problem)
2. Pattern analysis (find similar issues)
3. Hypothesis testing (prove your theory)
4. Implementation (fix the issue)
```

### Skill: Defense in Depth
```bash
/superpowers:defense-in-depth

Validates at every layer:
1. Input validation
2. Business logic checks
3. Database constraints
4. API responses
5. Client-side validation
```

---

## Real-World Example

### Scenario: Build Complete Feature with Superpowers

```bash
# 1. Start with brainstorming
/superpowers:brainstorm "Real-time notification system"

# 2. Create detailed plan
/superpowers:write-plan "Implement real-time notifications"

# 3. Execute plan with checkpoints
/superpowers:execute-plan

# 4. Each task includes:
#    - Implementation
#    - Automated tests (TDD)
#    - Code review checkpoint
#    - Verification

# 5. Across multiple sessions:
#    - Save progress to git
#    - Track state in JSON
#    - Update documentation
#    - Continue from checkpoint
```

---

## Best Practices

### ✅ DO:

- **Use for complex tasks** — Superpowers shines on multi-step work
- **Leverage planning** — Detailed plans improve execution
- **Request reviews** — Built-in code review is comprehensive
- **Track state** — Use JSON/git for persistent tracking
- **Commit frequently** — Regular commits are safety checkpoints

### ❌ DON'T:

- **Skip planning** — Planning saves time on execution
- **Ignore code reviews** — Reviews catch important issues
- **Lose state** — Save progress regularly
- **Work too long** — Use multi-window guidance
- **Skip tests** — TDD is core to reliable development

---

## Troubleshooting

### Superpowers Not Available

**Solution:**
```bash
# Verify installation
/help superpowers

# Reinstall if needed
/plugin install superpowers@superpowers-marketplace

# Restart Claude Code
```

### Features Not Working

**Solution:**
1. Check that you're in Claude Code environment
2. Verify plugin is installed and enabled
3. Use explicit skill invocation (`/superpowers:feature-name`)
4. Check for updates to the plugin

---

## Next Steps

1. **Install Superpowers** — Follow setup above
2. **Try brainstorming** — `/superpowers:brainstorm`
3. **Create a plan** — `/superpowers:write-plan`
4. **Execute implementation** — `/superpowers:execute-plan`
5. **Request code review** — `/superpowers:requesting-code-review`

---

## Learn More

- [Superpowers GitHub](https://github.com/obra/superpowers-chrome)
- [Claude Code Documentation](../docs/claude-code-guide.md)
- [Claude Prompt Engineering Guide](../Claude-Prompt-Guide.md)

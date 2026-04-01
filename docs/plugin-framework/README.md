# The Plugin Framework — A Complete Software Development Workflow

> Composable skills that give your coding agent a structured development process

## What This Is

A plugin for Claude Code (and Cursor, Codex, OpenCode, Gemini CLI) that installs a complete software development workflow. It does not just add tools — it changes how your agent works. Instead of jumping straight into code, the agent steps back, asks what you are really trying to do, designs a solution, plans the implementation, and then executes with test-driven development and code review built in.

The skills trigger automatically. You do not need to invoke them manually.

---

## The Core Workflow

### 1. Brainstorming
**Triggers:** When you describe something to build.

The agent does not write code. It asks questions, refines your idea, explores alternatives, and presents a design document in chunks short enough to actually read. Saves the design to a file.

Includes a visual companion mode that launches a local HTML server for diagram-based brainstorming.

### 2. Git Worktree Setup
**Triggers:** After design approval.

Creates an isolated workspace on a new branch via `git worktree add`. Runs project setup. Verifies a clean test baseline before any implementation begins.

### 3. Writing Plans
**Triggers:** With an approved design.

Breaks work into bite-sized tasks (2–5 minutes each). Every task includes exact file paths, complete code, and verification steps. Plans are detailed enough for an "enthusiastic junior engineer with poor taste and no project context" to follow.

### 4. Execution (Two Modes)

**Subagent-Driven Development:** Dispatches a fresh subagent per task with two-stage review:
1. Spec compliance check — Does it match the plan?
2. Code quality review — Is it clean and correct?

Can run autonomously for hours without deviating from the plan.

**Batch Execution:** Executes tasks in batches with human checkpoints between batches.

### 5. Test-Driven Development
**Triggers:** During implementation.

Enforces strict RED-GREEN-REFACTOR:
1. Write a failing test
2. Watch it fail
3. Write minimal code to pass
4. Watch it pass
5. Commit

If code is written before tests, the skill flags it. Includes a reference on testing anti-patterns.

### 6. Code Review
**Triggers:** Between tasks.

Reviews against the plan. Reports issues by severity. Critical issues block progress.

### 7. Finishing the Branch
**Triggers:** When all tasks complete.

Verifies tests pass. Presents options: merge, create PR, keep branch, or discard. Cleans up the worktree.

---

## All Skills

### Testing
- **test-driven-development** — RED-GREEN-REFACTOR cycle with anti-pattern reference

### Debugging
- **systematic-debugging** — 4-phase root cause process with techniques: root-cause tracing, defense-in-depth, condition-based waiting

### Collaboration
- **brainstorming** — Socratic design refinement (with visual HTML companion)
- **writing-plans** — Detailed implementation plans
- **executing-plans** — Batch execution with checkpoints
- **dispatching-parallel-agents** — Concurrent subagent workflows
- **requesting-code-review** — Pre-review checklist
- **receiving-code-review** — Responding to feedback
- **using-git-worktrees** — Parallel development branches
- **finishing-a-development-branch** — Merge/PR decision workflow
- **subagent-driven-development** — Fast iteration with spec compliance + code quality review

### Meta
- **writing-skills** — Create new skills following best practices
- **using-superpowers** — Introduction to the system

---

## Installation

```bash
# Claude Code (official marketplace)
/plugin install superpowers@claude-plugins-official

# Claude Code (via community marketplace)
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace

# Cursor
/add-plugin superpowers

# Codex / OpenCode
# Fetch and follow install instructions from the repo

# Gemini CLI
gemini extensions install https://github.com/obra/superpowers
```

### Verification
Start a new session and ask for something that should trigger a skill (e.g., "help me plan this feature"). The agent should automatically invoke the relevant skill.

---

## Philosophy

- **Test-Driven Development** — Write tests first, always
- **Systematic over ad-hoc** — Process over guessing
- **Complexity reduction** — Simplicity as the primary goal
- **Evidence over claims** — Verify before declaring success
- **YAGNI** — You Aren't Gonna Need It
- **DRY** — Don't Repeat Yourself

---

## Agents

Ships one built-in agent:
- **code-reviewer** — Reviews code against plans, reports issues by severity

---

## Hooks

- Session start hook (runs on every new session)
- Cross-platform hook support (Claude Code JSON hooks + Cursor hooks)
- Windows support via polyglot hook scripts

---

## What Makes This Different

- **Workflow, not tools** — The skills form a complete development lifecycle, not a grab bag of utilities
- **Automatic activation** — Skills trigger based on context. No manual invocation needed.
- **Two-stage subagent review** — Spec compliance check + code quality review catches both plan drift and quality issues
- **Hours of autonomous work** — With a good plan, the agent can work through tasks without human intervention
- **Cross-platform** — Same workflow across Claude Code, Cursor, Codex, OpenCode, and Gemini CLI

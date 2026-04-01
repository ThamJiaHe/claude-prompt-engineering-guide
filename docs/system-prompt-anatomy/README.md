# Anatomy of Claude Code's System Prompts

> How Claude Code assembles its behavior from 110+ prompt components

## The Big Picture

Claude Code does not use a single system prompt. It assembles behavior from **110+ separate prompt strings** that are combined dynamically based on your environment, settings, tools, and conversation state. These prompts are extracted directly from compiled source code and tracked across 136+ versions.

---

## How Prompts Are Organized

### Agent Prompts (~35)

System prompts for built-in subagents and specialized functions:

**Built-in subagents:**
- Exploration agent (~494 tokens) — codebase search and analysis
- Planning agent (~636 tokens) — enhanced planning with phase structure
- General-purpose agent (~285 tokens) — broad search and analysis
- Worker fork (~404 tokens) — executes directives in isolated context

**Creation assistants:**
- Agent creation architect (~1,110 tokens) — generates custom agent specs
- CLAUDE.md generator (~384 tokens) — creates project config from codebase analysis
- Status line configurator (~1,999 tokens) — sets up prompt bar display

**Slash command prompts:**
- `/batch` (~1,106 tokens) — orchestrates parallel file changes
- `/schedule` (~2,468 tokens) — manages scheduled remote agents
- `/security-review` (~2,607 tokens) — comprehensive security analysis

**Security enforcement:**
- Security monitor part 1 (~2,726 tokens) — evaluates actions against rules
- Security monitor part 2 (~3,008 tokens) — block rules and allow exceptions
- Bash command prefix detector (~823 tokens) — catches injection attempts

**Memory management:**
- Conversation summarizer (~1,121 tokens) — creates conversation summaries
- Dream memory consolidation (~727 tokens) — multi-phase memory consolidation between sessions
- Session memory updater (~756 tokens) — updates memory files

**Verification:**
- Verification specialist (~2,453 tokens) — adversarially tests implementations, returns PASS/FAIL/PARTIAL

---

### Data Templates (~26)

Reference data loaded on demand:

**API references by language:** Python, TypeScript, Go, Java, C#, PHP, Ruby, cURL (900–5,100 tokens each)

**Agent SDK references:** Python patterns, TypeScript patterns, Python reference, TypeScript reference

**Conceptual references:**
- Model catalog (~2,295 tokens) — all current/legacy models with IDs, pricing, context windows
- Tool use concepts (~3,721 tokens) — definitions, tool choice, best practices
- Prompt caching design (~1,880 tokens) — caching placement patterns
- HTTP error codes (~1,922 tokens) — API errors with handling strategies
- Live documentation URLs (~2,336 tokens) — WebFetch endpoints for current docs

---

### Main System Prompt Components (~50)

The main prompt is assembled from many small pieces:

**Task execution rules (each 40–110 tokens):**
- Software engineering focus
- Read before modifying
- No unnecessary additions
- No premature abstractions
- No unnecessary error handling
- No compatibility hacks
- No time estimates
- Minimize file creation
- Security awareness

**The "Executing Actions with Care" block (~590 tokens):**
The largest behavioral instruction. Covers reversibility assessment, blast radius consideration, destructive operation warnings, and when to ask for confirmation. This is why Claude Code hesitates before running `rm -rf` or `git push --force`.

**Output controls:**
- Output efficiency (~177 tokens) — Be concise, lead with answers
- Minimal mode (~164 tokens) — Skips hooks, LSP, plugins
- Learning mode (~1,042 tokens) — Educational explanations and insights

**Tool usage policy:**
- Prefer dedicated tools over Bash (Read over `cat`, Edit over `sed`)
- Task management guidance
- Subagent delegation rules
- Parallel tool call optimization
- Skill invocation rules

---

### System Reminders (~40)

Dynamic messages injected during conversation:

| Reminder | Trigger |
|----------|---------|
| Plan mode active (5-phase / iterative / subagent) | When planning |
| Token usage warning | Context approaching limits |
| USD budget warning | Cost limits approaching |
| Task tools reminder | Periodic nudge to use tracking |
| Team coordination | Agent teams active |
| File modified externally | User or linter changed a file |
| File opened in IDE | IDE integration event |
| New diagnostics | LSP found issues |
| Session continuation | Resuming previous session |
| Agent mention | @agent in conversation |

---

### Tool Descriptions (~30)

Every built-in tool has its own detailed description prompt:

| Tool | Notable Details |
|------|----------------|
| **Bash** | 20+ sub-prompts for sandbox mode, sleep rules, git safety, parallel execution |
| **Edit** | Exact string matching with uniqueness constraints |
| **Write** | Must read existing files first |
| **Read** | Supports files, images, PDFs, Jupyter notebooks |
| **Agent** | Subagent spawning with model routing and worktree isolation |
| **Computer** | Screenshot, mouse, keyboard for computer use |
| **LSP** | Language server integration |
| **TeammateTool** | Agent team management |

---

### Skill Prompts (~10)

Built-in skill system prompts including:
- Build with Claude API (+ reference guide)
- Debugging, code simplification
- Loop and scheduling commands
- Config update with 7-step verification
- Skillify (convert current session into a reusable skill, ~1,882 tokens)

---

## Why This Matters

Understanding the system prompt structure tells you:

1. **Why Claude Code behaves the way it does** — The "Executing Actions with Care" block explains every confirmation dialog.

2. **How the security model works** — Two security monitor prompts (5,734 tokens total) define what Claude Code considers safe to do autonomously.

3. **How verification works** — The verification specialist prompt reveals how Claude Code tests its own work adversarially.

4. **How memory consolidation works** — The "dream" memory prompt shows how Claude Code processes memories between sessions.

5. **What costs context** — Token counts per component let you understand where your context window budget goes.

---

## Modifying System Prompts

A community tool called `tweakcc` allows editing individual prompt components:
- Edit prompts as markdown files
- Patches both npm and native (binary) installations
- Handles merge conflicts when both you and Anthropic modify the same prompt

---

## Tracking Changes

System prompts change with every Claude Code release. 136+ versions tracked since v2.0.14. Prompts are auto-extracted from compiled JavaScript source within minutes of each npm release.

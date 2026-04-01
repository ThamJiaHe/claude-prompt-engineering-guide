# Building AI Agent Harnesses from Scratch

> How to construct AI agent infrastructure using the Claude API — without any framework

## The Core Idea

You do not need LangChain or any framework to build an AI agent. The language model is already the agent. Your job is to build a thin harness — tools, memory, context management — and let the model do the reasoning.

The entire foundation fits in ~30 lines of Python. Everything else is optional infrastructure you add one piece at a time.

---

## 12-Session Curriculum

Each session adds a single concept. The core agent loop from session 1 never changes — only the surrounding infrastructure grows.

### Foundations (Sessions 1–3)

**Session 1 — The Agent Loop.**
Build a `while stop_reason == tool_use` loop with one tool (bash). This is the entire agent.

**Session 2 — Tool Dispatch.**
Replace conditionals with a dispatch map: `TOOL_HANDLERS = {"bash": run_bash, "read": read_file, ...}`. Add path sandboxing via `Path.is_relative_to()`. Filter dangerous commands.

**Session 3 — Task Tracking.**
Add a TodoManager with three states (pending, in_progress, done). Inject reminders every 3 rounds. Enforce one in-progress task at a time.

### Context Management (Sessions 4–6)

**Session 4 — Subagents.**
Spawn isolated subagents with fresh `messages=[]`. Cap at 30 iterations. Never let subagents spawn subagents.

**Session 5 — On-Demand Knowledge.**
Two-layer skill loader: 100-token metadata summaries (always available) and 2000-token full bodies (loaded only when requested). Never front-load domain knowledge.

**Session 6 — Context Compression.**
Three tiers: micro-compact (replace old results with summaries), auto-compact (model summarizes at 50k tokens), transcript persistence (JSONL backup of everything).

### Multi-Agent (Sessions 7–9)

**Session 7 — Persistent Task Graphs.**
JSON files in `.tasks/` with DAG dependencies. Tasks survive across sessions.

**Session 8 — Background Execution.**
Daemon threads for slow operations. Notification queue drained before each model call.

**Session 9 — Teammate Coordination.**
JSONL-based message bus with per-agent inboxes. Drain-on-read prevents duplicates.

### Advanced Coordination (Sessions 10–12)

**Session 10 — Communication Protocols.**
FSM-based shutdown and approval protocols. UUID correlation for request-response tracking.

**Session 11 — Autonomous Task Claiming.**
Agents poll for work every 5 seconds. After context compression, re-inject identity blocks to prevent amnesia.

**Session 12 — Worktree Isolation.**
Each agent gets its own git worktree. Lifecycle tracked via append-only JSONL event log.

---

## The Capstone

A single ~736-line file integrating all 12 sessions with 25 tools. Token-aware compression, thread-safe multi-agent coordination, dangerous command filtering, and persistent state. Production-grade.

---

## Design Principles Worth Stealing

- **Files over databases.** Tasks, inboxes, events, transcripts are all plain files. Debuggable with any text editor.
- **Append-only JSONL.** No race conditions, no corruption, no write locks needed.
- **Identity re-injection.** After compression, if `len(messages) <= 3`, prepend an identity block. Agents forget who they are otherwise.
- **50k character output cap.** Applied to bash output, file reads, subagent results. Prevents context flooding.
- **Skill metadata separation.** Keep summaries tiny (100 tokens). Load full content (2000 tokens) only on demand.

---

## Quick Start

```bash
pip install anthropic python-dotenv
cp .env.example .env   # Set ANTHROPIC_API_KEY and MODEL_ID
python agents/s01_agent_loop.py    # Start from the beginning
python agents/s_full.py            # Jump to the capstone
```

Interactive commands: `/compact`, `/team`, `/inbox`, `q` (exit).

The `.env.example` supports multiple Claude API-compatible providers with China mainland endpoints included.

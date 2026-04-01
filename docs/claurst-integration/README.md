# Claurst — The Claude Code Rust Reimplementation

> A clean-room Rust reimplementation and architecture specification of Claude Code, built following the accidental March 2026 source leak.

---

## What This Is

On **March 31, 2026**, Anthropic accidentally bundled TypeScript source maps into the Claude Code npm package. The full `src/` directory (~1,900 files, 800K+ lines) became publicly visible. Chaofan Shou first reported the disclosure.

**Claurst** does two things in response:

1. **Documents** the leaked architecture through 14 comprehensive specification files (990 KB total)
2. **Reimplements** Claude Code in Rust, following the same clean-room precedent established in _Sega v. Accolade_ — read the spec, then implement from scratch in a different language

The project does not copy TypeScript code. It uses the leaked source as a specification to build an independent Rust implementation.

---

## Why This Matters

The leak exposed systems that Anthropic had never documented publicly. Several features were complete in the codebase but hidden behind compile-time feature flags. Claurst makes all of them visible.

---

## Unreleased Features Revealed

These features exist in the production codebase but are gated and not yet released:

### KAIROS
An always-on proactive assistant mode.
- Runs continuously in the background
- Maintains daily logs automatically
- Makes autonomous decisions within a 15-second budget per action
- Scheduled via `CronCreateTool` (also gated)

### Buddy
A Tamagotchi-style companion embedded in the CLI.
- 18 species with procedurally generated personalities
- Uses Mulberry32 PRNG for deterministic generation
- Has rarity tiers and gacha mechanics
- Animated via `CompanionSprite.tsx`
- Six files: companion logic, sprites, prompts, types, notification hook

### ULTRAPLAN
Remote 30-minute planning sessions.
- Uses Opus 4.6 exclusively
- Browser-based approval workflow
- Designed for complex architectural decisions

### autoDream
Background memory consolidation.
- Triggers on three conditions: 24-hour interval elapsed, 5+ sessions completed, lock successfully acquired
- Consolidates session memories into durable long-term storage
- Runs without user interaction

### Coordinator Mode
Multi-agent swarm orchestration.
- Spawn multiple parallel worker agents
- Central coordinator routes work
- Workers return results to coordinator
- Full swarm topology supported

---

## Architecture: What the Leak Revealed

### Core Query Loop

Every conversation runs through `query.ts`. Each loop iteration:
1. Snapshots configuration via `buildQueryConfig()`
2. Tracks token budget and file state
3. Streams response from Claude API
4. Executes tools (sequential or streaming)
5. Runs end-of-turn hooks asynchronously
6. Checks continuation conditions (token limit, max turns, tool use)

Up to 3 retries on `max_output_tokens` errors. Reactive context compaction on overflow.

### Tools (40+ built-in)

| Category | Tools |
|----------|-------|
| File | Read, Write, Edit, NotebookEdit, Glob, Grep |
| Shell | Bash (Linux/Mac), PowerShell (Windows) |
| Web | WebFetch, WebSearch |
| Agent | AgentTool, TeamCreate, TeamDelete, SendMessage |
| Task | TaskCreate, TaskGet, TaskUpdate, TaskList, TaskStop |
| Planning | EnterPlanMode, ExitPlanMode |
| Workspace | EnterWorktree, ExitWorktree |
| MCP | MCPTool, ListMcpResources, ReadMcpResource |
| Scheduling | CronCreate, CronDelete, CronList (KAIROS-gated) |
| Utility | AskUserQuestion, SkillTool, ConfigTool, SleepTool |

`FileEditTool` uses mtime staleness checks and falls back to content comparison on Windows cloud-synced drives.

### Commands (87+ implementations)

**Workflow:** `/commit`, `/review`, `/plan`, `/branch`, `/diff`, `/pr_comments`
**Config:** `/config`, `/model`, `/effort`, `/fast`, `/theme`, `/vim`
**Context:** `/context`, `/cost`, `/usage`, `/status`, `/skills`, `/memory`
**Integration:** `/mcp`, `/plugin`, `/install-github-app`, `/install-slack-app`
**Session:** `/resume`, `/rename`, `/session`, `/tasks`, `/export`
**Advanced:** `/voice` (gated), `/ultraplan` (gated), `/init`

Remote-safe commands (work in `--remote` mode): session, exit, clear, help, theme, color, vim, cost, usage, copy, btw, feedback, plan, keybindings, statusline, stickers, mobile.

### Permission System

Four permission modes:
- `default` — prompts user for each tool use
- `acceptEdits` — auto-approves file edits, prompts for shell
- `bypassPermissions` — no prompts (trust mode)
- `plan` — no execution, planning only
- `auto` — ML classifier decides automatically

The ML-based auto-approval classifier runs two stages: `thinking` and `fast`. It has a 200ms grace period after user interaction. Shell commands are auto-classified as read or write based on content analysis.

### Hooks

Three lifecycle events:
- `PreToolUse` — fires before any tool execution
- `PostToolUse` — fires after tool completes
- `PostResponse` — fires after assistant turn ends

Execution options: bash script, LLM prompt, HTTP request, agent verification.

### Memory System (memdir)

Eight files managing persistent cross-session memory:
- `memdir.ts` — orchestration
- `findRelevantMemories.ts` — relevance retrieval using Sonnet
- `memoryScan.ts` — catalog management
- `memoryAge.ts` — staleness tracking
- `teamMemPaths.ts` / `teamMemPrompts.ts` — team-shared memory

Memories stored as frontmatter-driven Markdown files. Staleness warnings appear for aged entries.

### Bridge System (IDE Integration)

40+ files implementing bidirectional VS Code and JetBrains integration.

Two protocols:
- **CCR v2** (current): POST to `/v1/code/sessions`, credential exchange, gated by `tengu_bridge_repl_v2`
- **CCR v1** (legacy): WebSocket via `/v1/environments/bridge`

Bridge features:
- Work polling with exponential backoff
- Sleep detection via gap analysis
- Multi-session capacity management
- Git worktree isolation per session
- Sequence number carryover for SSE resumption
- UUID-based echo suppression and re-delivery deduplication

### Context Compression

Four levels, tried in order:
1. API-native editing via `apiMicrocompact.ts`
2. Client-side microcompact
3. Full compaction (LLM-driven summarization)
4. Session memory compaction

### State Management

Global singleton in `bootstrap/state.ts`:
- Session UUID and parent lineage
- Cost and token counters (per-session, per-turn)
- Model configuration
- Telemetry flags
- Session mode (interactive, trust, persistence)

Analytics route to Datadog (strips `_PROTO_` keys) and first-party logging (hoists `_PROTO_` to fields).

---

## Security Findings

### Undercover Mode
Prevents Claude from revealing internal information in public commits.
- Bans mentions of model codenames
- Bans references to unreleased versions
- Bans references to internal tooling names

### Feature Flag Obfuscation
All GrowthBook flags use `tengu_` prefix with opaque names:
- `tengu_session_memory`
- `tengu_frond_boric`
- `tengu_cobalt_frost`
- `tengu_bridge_repl_v2`

### Internal Naming
- Fast mode: "Penguin Mode"
- Computer Use: "Chicago"
- Upcoming models referenced: Claude "Capybara" with `capybara-v2-fast` (1M context), Opus 4.7, Sonnet 4.8

---

## Known Limits Hardcoded in Source

| Resource | Limit |
|----------|-------|
| Image upload | 5 MB base64 |
| PDF upload | 20 MB raw, 100 pages max |
| PDFs above 3 MB | Switch to page-image extraction |
| Tool result per tool | 50,000 characters |
| Tool results aggregate per turn | 200,000 characters |
| Task IDs | Base-36, ~2.8 trillion space |

---

## The Rust Implementation (Claurst)

11 crates organized as a Cargo workspace:

| Crate | Responsibility |
|-------|---------------|
| `api` | Anthropic API layer |
| `bridge` | IDE integration bridge |
| `buddy` | Companion system |
| `cli` | Command-line interface |
| `commands` | Command implementations |
| `core` | Core query loop |
| `mcp` | Model Context Protocol |
| `plugins` | Plugin system |
| `query` | Query processing |
| `tools` | Tool definitions |
| `tui` | Terminal UI (Ink equivalent in Rust) |

Each crate compiles independently. The workspace uses `Cargo.lock` for reproducible builds.

---

## Repository Structure

```
claurst/
├── README.md               — Main documentation (31 KB)
├── spec/
│   ├── INDEX.md
│   ├── 00_overview.md      — Architecture overview
│   ├── 01_core_entry_query.md
│   ├── 02_commands.md      — 87+ command definitions
│   ├── 03_tools.md         — 40+ tool definitions
│   ├── 04_components_core_messages.md
│   ├── 05_components_agents_permissions_design.md
│   ├── 06_services_context_state.md
│   ├── 07_hooks.md
│   ├── 08_ink_terminal.md
│   ├── 09_bridge_cli_remote.md
│   ├── 10_utils.md         — 564 utility files documented
│   ├── 11_special_systems.md — Buddy, memory, voice, plugins
│   └── 12_constants_types.md
├── src-rust/
│   ├── Cargo.toml
│   ├── Cargo.lock
│   └── crates/             — 11 crates
└── public/
    ├── claude-files.png
    └── leak-tweet.png
```

---

## Specification Scale

| Metric | Value |
|--------|-------|
| Specification files | 14 Markdown files |
| Total spec size | 990 KB |
| Utilities documented | 564 files across 36 subdirectories |
| Commands covered | 87+ |
| Tools covered | 40+ |
| UI components covered | 130+ |
| React hooks covered | 85+ |
| Rust crates | 11 |
| UI animation verbs | 186 (spinner) |
| Buddy species | 18 |

---

## How to Use This

**Read the spec directory** if you want to understand Claude Code's internals without running code.

**Start with `spec/00_overview.md`** for architecture orientation.

**Read `spec/11_special_systems.md`** for KAIROS, Buddy, autoDream, and voice mode details.

**Build from `src-rust/`** if you want to contribute to or run the Rust reimplementation.

---

## Source

- Repository: `Kuberwastaken/claurst`
- Disclosed: March 31, 2026
- Original leak: Claude Code npm package sourcemaps
- Legal basis: Clean-room reimplementation (Sega v. Accolade precedent)
- Implementation language: Rust (vs. original TypeScript)

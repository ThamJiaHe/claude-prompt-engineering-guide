# Claude Code Core Runtime — Internal Architecture

> A complete technical reference for Claude Code's internal architecture, compiled from the March 2026 source disclosure.

---

## Overview

Claude Code is Anthropic's official CLI tool for AI-assisted software development. The complete TypeScript source (~1,900 files, 512,000+ lines) became publicly available on March 31, 2026 via accidentally bundled sourcemap files in the npm package.

This guide documents the actual internal architecture — not the public documentation, but how it actually works.

**Stack:**
- Runtime: Bun
- Language: TypeScript (strict mode)
- Terminal UI: React + Ink
- CLI Framework: Commander.js
- Schema validation: Zod v4
- Code search: ripgrep
- Protocols: MCP SDK, Language Server Protocol
- Auth: OAuth 2.0, JWT, macOS Keychain
- Feature flags: GrowthBook
- Telemetry: OpenTelemetry + gRPC

---

## The Query Engine

`src/QueryEngine.ts` is the central engine. ~46K lines. It manages everything that happens during a conversation.

**Session capabilities:**
- Streaming LLM responses with tool-call loops
- Thinking mode (extended reasoning budgets)
- Retry logic (up to 3 retries for `max_output_tokens` errors)
- Token budget tracking with reactive context compaction
- Message history and transcript persistence
- Cost aggregation per session and per turn

**The query loop** (`src/query.ts`) runs as an async generator. Each iteration:
1. Calls `buildQueryConfig()` to snapshot current config
2. Applies token budget and file state checks
3. Streams response from Anthropic API
4. Executes tool calls (sequential or streaming)
5. Fires end-of-turn hooks asynchronously
6. Checks whether to continue (token limit, max turns, tool use status)

The loop exits when the model stops using tools or a termination condition is met.

---

## Tools System

40+ built-in tools. Each tool is self-contained with input schemas (Zod), permission classification, and execution logic.

### File Operations

| Tool | What It Does |
|------|-------------|
| `FileReadTool` | Read files including images, PDFs (up to 20 pages), Jupyter notebooks |
| `FileWriteTool` | Create or overwrite files |
| `FileEditTool` | Partial modification using string replacement with atomicity protection |
| `NotebookEditTool` | Edit Jupyter notebook cells |
| `GlobTool` | Pattern-based file discovery |
| `GrepTool` | ripgrep-backed content search with context lines, multiline mode |

**FileEditTool atomicity:** Uses mtime comparison. Falls back to content comparison on Windows where cloud sync can update timestamps without changing content.

### Shell Execution

| Tool | Platform |
|------|---------|
| `BashTool` | Linux / macOS — full shell execution with sandboxing (bwrap/sandbox-exec) |
| `PowerShellTool` | Windows — PowerShell execution |

Both auto-background long-running commands after a configurable timeout.

### Web

| Tool | What It Does |
|------|-------------|
| `WebFetchTool` | Fetch URL content, converts HTML to Markdown |
| `WebSearchTool` | Web search capability |

### Multi-Agent Coordination

| Tool | What It Does |
|------|-------------|
| `AgentTool` | Spawn sub-agents for parallel work |
| `TeamCreateTool` / `TeamDeleteTool` | Create/destroy agent teams |
| `SendMessageTool` | Send messages between agents |

### Task Management

Tasks have a full lifecycle: `pending → running → completed / failed / killed`.

Task ID format: prefix (`b` for bash, `a` for agent) + 8 random alphanumeric characters. ~2.8 trillion unique IDs.

| Tool | What It Does |
|------|-------------|
| `TaskCreateTool` | Create a new task |
| `TaskGetTool` | Retrieve task status |
| `TaskUpdateTool` | Update task properties |
| `TaskListTool` | List all tasks |
| `TaskStopTool` | Kill a running task |

### Planning and Workflow

| Tool | What It Does |
|------|-------------|
| `EnterPlanModeTool` | Switch to plan-only mode (no execution) |
| `ExitPlanModeTool` | Return to normal execution mode |
| `EnterWorktreeTool` | Isolate work in a git worktree |
| `ExitWorktreeTool` | Return from git worktree |
| `SkillTool` | Execute a saved skill workflow |

### Scheduling (KAIROS-gated)

| Tool | What It Does |
|------|-------------|
| `CronCreateTool` | Schedule recurring triggers |
| `CronDeleteTool` | Remove a scheduled trigger |
| `CronListTool` | List active schedules |

These are gated behind the `KAIROS` feature flag and not active in the current release.

### Utilities

| Tool | What It Does |
|------|-------------|
| `AskUserQuestionTool` | Prompt user for input |
| `ConfigTool` | Read/write configuration |
| `SleepTool` | Pause in proactive mode |
| `RemoteTriggerTool` | Fire remote execution |
| `ToolSearchTool` | Deferred tool discovery (lazy loading) |
| `SyntheticOutputTool` | Structured output generation |

### MCP Tools

| Tool | What It Does |
|------|-------------|
| `MCPTool` | Invoke any registered MCP tool |
| `ListMcpResourcesTool` | Discover available MCP resources |
| `ReadMcpResourceTool` | Read a specific MCP resource |
| `McpAuthTool` | Authenticate with an MCP server |

---

## Command System

70+ slash commands invoked with `/` prefix.

### Code and Git

`/commit` — create git commits
`/review` — code review
`/branch` — branch management
`/diff` — view staged/unstaged changes
`/pr_comments` — view pull request comments

### Development Workflow

`/plan` — enter plan mode (analysis without execution)
`/tasks` — task management interface
`/skills` — install, remove, or inspect skills
`/memory` — view and manage persistent memory

### Configuration

`/config` — settings management
`/model` — switch active model
`/effort` — set thinking budget
`/fast` — toggle fast/Penguin mode
`/theme` — change visual theme
`/vim` — toggle Vim keybindings

### Diagnostics and Info

`/doctor` — environment diagnostics
`/cost` — display session token and USD cost
`/context` — visualize context usage
`/status` — system status
`/usage` — detailed usage breakdown

### Session Management

`/resume` — restore previous session
`/session` — session controls
`/export` — export session transcript
`/rename` — rename session
`/share` — share session link

### Integration

`/mcp` — MCP server management
`/plugin` — plugin management
`/agents` — agent management
`/teams` — team coordination
`/desktop` — hand off to desktop app
`/mobile` — hand off to mobile app

### Advanced (Feature-Gated)

`/voice` — voice input (OAuth required, VOICE_MODE flag)
`/ultraplan` — 30-minute remote Opus 4.6 planning session

---

## Permission System

**Four active modes:**

| Mode | Behavior |
|------|---------|
| `default` | Prompts before every tool use |
| `acceptEdits` | Auto-approves file edits, prompts for shell |
| `bypassPermissions` | No prompts — full trust |
| `plan` | No execution at all |
| `auto` | ML classifier decides per tool call |

**ML auto-approval classifier:**
- Two stages: `thinking` and `fast`
- Token budgets allocated per stage
- 200ms grace period after user interaction (avoids false denials on rapid sequences)
- Shell commands auto-classified as read or write by content analysis

**Permission check flow:**
1. `checkPermissions()` returns: `allow / ask / deny / passthrough`
2. Context includes: mode, tool-level allowlist/denylist, project settings
3. Cache prevents repeated prompts for the same tool+args within a session

---

## Context and System Prompts

Context collected by `src/context.ts`:

**Git context (auto-included):**
- Current branch and status (truncated at 2,000 characters)
- Recent commit history
- Git user configuration

**User context:**
- `CLAUDE.md` files discovered by directory traversal
- Current date in ISO format
- Respects `--bare` mode constraints

**Cache invalidation:**
Cache-breaking injection supported via `--cache-break` flag.

---

## Memory System (memdir)

Eight files in `src/memdir/`:

| File | Responsibility |
|------|---------------|
| `memdir.ts` | Core orchestration |
| `findRelevantMemories.ts` | Retrieval using Sonnet for relevance scoring |
| `memoryScan.ts` | Catalog of all stored memories |
| `memoryAge.ts` | Staleness detection and warnings |
| `memoryTypes.ts` | Data structures |
| `paths.ts` | File path resolution |
| `teamMemPaths.ts` | Team-shared memory paths |
| `teamMemPrompts.ts` | Prompt templates for team memory |

Memories are Markdown files with YAML frontmatter. Stored in `.claude/` directory structure. Persist across sessions. Team memory enables shared context across developers on the same project.

---

## Bridge System (IDE Integration)

40+ files in `src/bridge/`. Connects VS Code and JetBrains extensions to the CLI.

**Two protocols:**

| Protocol | Endpoint | Status |
|----------|---------|--------|
| CCR v2 | POST `/v1/code/sessions` | Current, gated by `tengu_bridge_repl_v2` |
| CCR v1 | WebSocket `/v1/environments/bridge` | Legacy |

**Bridge capabilities:**
- Work polling with exponential backoff
- Machine sleep detection via gap analysis in polling timestamps
- Multi-session management with capacity limits
- Git worktree isolation per session
- JWT authentication with proactive refresh
- Sequence number carryover for SSE resumption
- UUID-based echo suppression (prevents duplicate delivery)
- Session archival and cleanup on completion

**Session lifecycle:**
1. Bridge spawns child process
2. Monitors via promises
3. Enforces timeouts
4. Deregisters and archives on completion
5. Cleans up git worktrees

---

## State Management

Global singleton in `src/bootstrap/state.ts`. Leaf node — no circular imports allowed.

**Contains:**
- Session UUID and parent session lineage
- Cost and token counters (per-session and per-turn)
- Model configuration
- Session flags: interactive, trust, persistence
- Telemetry configuration

**Analytics pipeline:**
- Events queue through `index.ts`
- Dispatched via `sink.ts`
- Sampling checks and per-sink kill switches
- Routes to Datadog (strips `_PROTO_` keys from events)
- First-party logging hoists `_PROTO_` keys to top-level fields

---

## Context Compression

Four levels. Tried in order when context approaches limits:

1. **API-native editing** — `apiMicrocompact.ts` — uses API's built-in context management
2. **Client-side microcompact** — `microCompact.ts` — trims without LLM call
3. **Full compaction** — `compact.ts` — LLM-driven summarization of conversation history
4. **Session memory compaction** — `sessionMemoryCompact.ts` — consolidates session-specific memories

---

## Hook System

Three lifecycle events:

| Event | Fires When |
|-------|-----------|
| `PreToolUse` | Before any tool executes |
| `PostToolUse` | After tool completes |
| `PostResponse` | After assistant turn ends |

Hook execution types:
- Bash script
- LLM prompt
- HTTP request
- Agent verification

Schemas defined in `src/schemas/hooks.ts` using Zod.

---

## UI Architecture

144 components in `src/components/`. Built with React + Ink (terminal renderer).

All components compiled via **React Compiler** with automatic memoization.

**Design system primitives:** `Box`, `Text`, `ScrollBox`, `ThemedBox`, `ThemedText`

**Key component groups:**

| Group | Components |
|-------|-----------|
| Dialogs | AutoModeOptIn, Bridge, BypassPermissions, CostThreshold, MCPServerApproval |
| Input | BaseTextInput, TextInput, VimTextInput, PromptInput, SearchBox |
| Display | Message, VirtualMessageList, HighlightedCode, Markdown, Spinner |
| Feature | ModelPicker, ThemePicker, OutputStylePicker, IdeStatusIndicator |

**VirtualMessageList** uses jump-to-index, search, and sticky prompt tracking for performance on long sessions.

---

## Keybinding System

14 files in `src/keybindings/`.

Fully customizable. Supports single keystrokes and multi-key chords. Context-scoped bindings (Chat, Global, Confirmation).

User customizations stored in `~/.claude/keybindings.json`.

Reserved shortcuts protected from overriding in `reservedShortcuts.ts`.

---

## Input System (React Hooks)

85 React hooks in `src/hooks/`.

**Text input hooks:**
- `useTextInput` — kill-ring, yank cycling, history
- `useVimInput` — full Vim state machine (normal, insert, visual modes)
- `useTypeahead` — fuzzy matching
- `usePasteHandler` — clipboard handling
- `useArrowKeyHistory` — command history navigation

**Permission hooks:**
- Route to interactive, coordinator, or swarm handlers based on mode

**Remote hooks:**
- `useRemoteSession`, `useReplBridge`, `useTeleportResume`

**Advanced:**
- `useVoiceIntegration` — voice input state
- `useVirtualScroll` — 80-row overscan for large lists
- `useSwarmInitialization` / `useSwarmPermissionPoller` — swarm coordination

---

## Skill System

Located in `src/skills/`.

Skills are reusable workflows — Markdown files with YAML frontmatter defining commands.

Sources for skills:
1. Bundled registry (`bundledSkills.ts`)
2. Disk Markdown files loaded dynamically (`loadSkillsDir.ts`)
3. Plugin-provided skills
4. MCP server-provided skills (`mcpSkillBuilders.ts`)

Skills support argument substitution. Execute via `SkillTool`.

---

## Plugin System

Located in `src/plugins/`.

Plugins can provide:
- Skills (new slash commands)
- Hooks (lifecycle callbacks)
- MCP servers
- LSP servers
- Output styles

Built-in plugins in `src/plugins/bundled/`. Third-party plugins installed via `/plugin`.

---

## MCP Integration

23 files in `src/services/mcp/`.

| File | Responsibility |
|------|---------------|
| `MCPConnectionManager.tsx` | Main connection lifecycle |
| `config.ts` | Server configuration |
| `auth.ts` | Authentication |
| `client.ts` | Client implementation |
| `channelPermissions.ts` | Per-channel permission model |
| `officialRegistry.ts` | Official registry support |
| `xaa.ts` / `xaaIdpLogin.ts` | Anthropic internal auth |

Supports WebSocket, HTTP, and stdio transports.

---

## Cost Tracking

`src/cost-tracker.ts` maintains running totals across the session.

**Tracks:**
- Input tokens, output tokens, cache read tokens, cache creation tokens
- Per-model breakdown
- Session persistence across `/resume`
- USD cost calculation per model
- OpenTelemetry counter metrics
- Nested tool costs (sub-agent calls included in parent cost)

Display formatting: shows USD to 4 decimal places when under $0.01.

---

## Performance Optimizations

| Technique | Where Applied |
|-----------|--------------|
| Parallel prefetch | MDM settings, keychain reads, API preconnect run in parallel at startup |
| Lazy loading | OpenTelemetry (~400 KB) and gRPC (~700 KB) deferred via dynamic `import()` |
| Build-time dead code elimination | Feature flags resolved at compile time via `bun:bundle` |
| Memoization | System and user context cached for conversation duration |
| Virtual scrolling | Message list uses 80-row overscan |
| Exponential backoff | Bridge poll errors |
| Heartbeat mode | When session capacity is full |

Boot target: ~135ms from invocation to first prompt.

---

## Known Resource Limits

| Resource | Limit |
|----------|-------|
| Image uploads | 5 MB base64 |
| PDF uploads | 20 MB raw, 100 pages max |
| PDF page-image threshold | 3 MB (above this switches extraction method) |
| Tool result (single tool) | 50,000 characters |
| Tool results (aggregate per turn) | 200,000 characters |
| Git context truncation | 2,000 characters |
| Task ID namespace | Base-36, ~2.8 trillion IDs |

---

## Repository Structure

```
src/
├── main.tsx              — CLI entrypoint (Commander.js, ~135ms boot target)
├── QueryEngine.ts        — Core LLM engine (~46K lines)
├── query.ts              — Async generator query loop
├── Tool.ts               — Base tool types
├── commands.ts           — Command registration
├── tools.ts              — Tool assembly
├── context.ts            — System/user context collection
├── Task.ts               — Task type definitions
├── cost-tracker.ts       — Token and USD tracking
├── bootstrap/
│   └── state.ts          — Global singleton state
├── bridge/               — IDE integration (40+ files)
├── cli/                  — CLI handlers and transports
├── commands/             — Individual command implementations
├── components/           — UI components (144 items)
├── hooks/                — React hooks (85 total)
├── keybindings/          — Keybinding system (14 files)
├── memdir/               — Persistent memory (8 files)
├── plugins/              — Plugin system
├── schemas/              — Zod validation schemas
├── screens/              — Full-screen interfaces (REPL, Doctor, Resume)
├── services/
│   ├── api/              — Anthropic SDK factory
│   ├── mcp/              — MCP integration (23 files)
│   ├── oauth/            — OAuth flow
│   ├── lsp/              — LSP integration
│   ├── analytics/        — GrowthBook + metrics
│   ├── compact/          — Context compression
│   ├── policyLimits/     — Organization policy enforcement
│   └── extractMemories/  — Automatic memory extraction
├── skills/               — Skill system
├── state/                — React state management (6 files)
├── tasks/                — Task implementations (7 types)
├── types/                — TypeScript type definitions
└── utils/                — Utilities (329 files)
```

---

## Source

- Repository: `tanbiralam/claude-code`
- Original disclosure: March 31, 2026
- Disclosure method: TypeScript sourcemaps bundled into npm package
- Discovered by: Chaofan Shou (@Fried_rice)
- Source size: ~1,900 TypeScript files, 512,000+ lines

This document synthesizes the architectural information from that source to serve as a reference for developers building with or extending Claude Code.

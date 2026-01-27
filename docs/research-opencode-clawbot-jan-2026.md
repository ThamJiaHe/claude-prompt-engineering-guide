# Claude Ecosystem Tools Research Report (January 2026)

## OpenCode CLI, AirLLM, External Coding Agents & Planning Patterns

**Published:** January 27, 2026
**Version:** 1.0
**Word Count:** ~5,500

---

## Executive Summary

The Claude ecosystem in January 2026 has expanded significantly beyond Anthropic's core offerings. This report analyzes four emerging tools and patterns that complement or compete with Claude Code:

1. **OpenCode CLI** — Open-source, provider-agnostic terminal coding agent (GitHub official support)
2. **AirLLM** — Memory-optimized inference for running 70B+ models on consumer GPUs
3. **External Coding Agents** — OpenAI Codex, GitHub Copilot CLI, and integration patterns
4. **Planning Patterns** — Task management workflows for Claude-driven development projects

**Key Findings:**

| Tool | Best For | Integration with Claude |
|------|----------|------------------------|
| OpenCode CLI | Multi-provider workflows, privacy-focused development, CI/CD automation | Alternative to Claude Code; can use Claude API |
| AirLLM | Edge inference, local LLM testing, hybrid cloud/local workflows | Complement: local processing + Claude API for heavy tasks |
| OpenAI Codex | Fast prototyping, OpenAI ecosystem integration | No direct integration; use as separate agent |
| Planning Files | Long-running projects, multi-session tracking, team handoffs | Native support via Claude Code context management |

**Recommendation Matrix:**

| Scenario | Recommended Tool |
|----------|-----------------|
| Vendor lock-in concerns | OpenCode CLI |
| Enterprise with Claude subscription | Claude Code |
| Local model experiments | AirLLM + Claude API hybrid |
| Quick prototyping with GPT | Codex CLI |
| Complex multi-day projects | Claude Code + planning/*.md files |

---

## 1. OpenCode CLI

### What It Is

OpenCode is an **open-source, terminal-based AI coding agent** that supports 75+ LLM providers, including OpenAI, Anthropic (Claude), Google, AWS Bedrock, local models via Ollama, and GitHub Copilot subscriptions. Released with official GitHub integration on January 16, 2026.

**Repository:** [github.com/anomalyco/opencode](https://github.com/anomalyco/opencode)
**License:** 100% free and open-source

### Core Features

| Feature | Description |
|---------|-------------|
| **75+ Providers** | Switch between OpenAI, Anthropic, Ollama, Copilot, ChatGPT Plus mid-session |
| **GitHub Integration** | Mention `/opencode` or `/oc` in issues/PRs for automated tasks |
| **Built-in Agents** | Build (full dev), Plan (read-only analysis), General (multi-step) |
| **Terminal UI** | Bubble Tea TUI with Vim-like editing |
| **Persistence** | SQLite storage for conversation history |
| **LSP Support** | Language Server Protocol integration for diagnostics |

### GitHub Copilot Authentication

All developers with paid GitHub Copilot subscriptions (Pro, Pro+, Business, Enterprise) can authenticate into OpenCode with no additional AI license:

```bash
# Install OpenCode
curl -fsSL https://opencode.ai/install.sh | bash

# Authenticate with Copilot
opencode /connect
# Select "GitHub Copilot" → complete device login flow
```

### OpenCode vs Claude Code Comparison

| Aspect | OpenCode CLI | Claude Code |
|--------|-------------|-------------|
| **Provider Support** | 75+ LLMs (OpenAI, Anthropic, Ollama, Copilot, etc.) | Anthropic only (Claude models) |
| **Model Switching** | Mid-session without lock-in | Locked to Claude |
| **MCP Support** | Yes (Model Context Protocol) | Native MCP support |
| **Local Models** | Full Ollama integration | No local model support |
| **Context Window** | Depends on underlying model | 200K (Opus), up to 1M (API) |
| **GitHub Integration** | `/opencode` in issues/PRs | GitHub Actions workflow |
| **Pricing** | Free/open-source; uses existing subscriptions | Token-based Anthropic API |
| **Privacy** | Local execution option; no code storage | Anthropic cloud processing |
| **Agents** | Build, Plan, General subagents | Plan Mode, Explore, multi-agent orchestration |
| **Headless CI/CD** | Strong (Ollama + bash + LSP) | Excellent (Superpowers plugin + hooks) |

### When to Use OpenCode

**Use OpenCode when:**
- You want vendor-agnostic workflows (no Claude lock-in)
- You have existing GitHub Copilot subscription (free usage)
- You need local execution for privacy-sensitive projects
- You want to switch models mid-session based on task complexity
- You're running CI/CD pipelines with local Ollama models

**Use Claude Code when:**
- You want best-in-class reasoning and large context (200K tokens)
- You're building with Claude Skills and MCP ecosystem
- You need the Superpowers plugin for advanced automation
- Your team is standardized on Anthropic
- You want Plan Mode with architectural planning agents

### OpenCode Configuration

```bash
# Basic usage
opencode "Implement authentication middleware"

# With specific provider
opencode --provider anthropic "Review this PR"

# Plan mode (read-only analysis)
opencode --agent plan "Explain the architecture of this project"

# GitHub Actions integration
# In your .github/workflows/opencode.yml:
- name: OpenCode Analysis
  uses: anomalyco/opencode-action@v1
  with:
    prompt: "Triage this issue"
```

---

## 2. AirLLM

### What It Is

AirLLM is an open-source library that enables **running 70B+ parameter models on consumer GPUs** (as low as 4GB VRAM) through memory-optimized layer-by-layer inference.

**Repository:** [github.com/lyogavin/airllm](https://github.com/lyogavin/airllm)
**Author:** lyogavin
**Status:** Active development, last major update 2024

### How It Works

AirLLM uses sequential layer loading instead of loading the entire model into memory:

1. Load a single transformer layer
2. Run computation on that layer
3. Free memory
4. Load next layer
5. Repeat until inference complete

This approach enables:
- **70B models on 4GB VRAM** (without quantization)
- **405B Llama 3.1 on 8GB VRAM**
- **No distillation or pruning required**

### Performance Characteristics

| Hardware | Metric | Performance |
|----------|--------|-------------|
| NVIDIA H100 | 128K token inference | 2.7x faster than baseline |
| NVIDIA H100 | 2M token inference | 35x faster than baseline |
| NVIDIA H100 | Concurrent streams | 560 streams (3x higher than buffered) |
| Consumer GPU | Latency | Constant per-token regardless of context length |

### Realistic Use Cases with Claude

AirLLM is best used as a **complement** to Claude, not a replacement:

| Use Case | Pattern |
|----------|---------|
| **Hybrid inference** | Use AirLLM for local processing (PII stripping, code analysis), Claude API for reasoning |
| **Development testing** | Test prompts locally with open models before consuming Claude tokens |
| **Edge deployment** | Run inference on local hardware, use Claude for complex tasks |
| **Cost optimization** | AirLLM for high-volume simple tasks, Claude for accuracy-critical work |
| **Offline fallback** | Local AirLLM when internet unavailable, sync with Claude when connected |

### Integration Pattern

```python
# Example: Hybrid AirLLM + Claude workflow
from airllm import AirLLM
import anthropic

# Local model for preprocessing
local_model = AirLLM("meta-llama/Llama-2-70b-hf")

# Claude for reasoning
claude = anthropic.Anthropic(api_key="your-key")

def hybrid_analysis(code: str):
    # Step 1: Local preprocessing (free, private)
    local_summary = local_model.generate(
        f"Summarize this code's purpose in one sentence: {code}"
    )

    # Step 2: Claude for deep analysis (paid, accurate)
    response = claude.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=2048,
        messages=[{
            "role": "user",
            "content": f"Given this code summary: {local_summary}\n\nProvide security recommendations."
        }]
    )
    return response.content
```

### Limitations

- **Inference latency** — Sequential layer loading is slower than native GPU inference
- **No fine-tuning** — AirLLM is inference-only; not designed for training
- **Model support** — Limited to Hugging Face transformers architecture
- **Active development** — Community project; not enterprise-supported

### Who Should Use AirLLM

| User Type | Recommendation |
|-----------|---------------|
| **Hobbyists** | Great for local experimentation |
| **Cost-sensitive startups** | Useful for development; Claude for production |
| **Privacy-focused teams** | Good for sensitive preprocessing |
| **Enterprise** | Consider managed solutions (AWS Bedrock, Vertex AI) instead |

---

## 3. External Coding Agents (Codex, Copilot CLI)

### OpenAI Codex CLI

OpenAI released Codex as a CLI-based coding agent in January 2026, powered by their frontier models and included in ChatGPT subscriptions.

**Features:**
- Repository navigation
- File editing
- Command execution
- Testing automation
- Real-time collaboration via CLI and IDE extensions

**Documentation:** [openai.com/codex](https://openai.com/codex)

### Claude Code vs Codex Comparison

| Aspect | Claude Code | OpenAI Codex |
|--------|-------------|--------------|
| **Strengths** | Reasoning, large context, Skills/plugins | Speed, OpenAI ecosystem, IDE extensions |
| **Multi-provider** | Native plugins; third-party hybrids | Via OpenCode (limited by blocks) |
| **Context window** | 200K tokens (up to 1M via API) | Model-dependent |
| **Task management** | TodoWrite, persistent tasks, `/rewind` | Agent loop for iteration |
| **Production status** | Threshold-crossing agent (Jan 2026) | Production agent |

### Integration Patterns

**No direct Codex-Claude integration exists.** However, you can coordinate them using:

1. **OpenCode as orchestrator** — Use OpenCode to switch between Claude and GPT models
2. **MCP bridge** — Create custom MCP server that routes to multiple providers
3. **Task handoffs** — Use Codex for fast prototyping, Claude for refinement

```yaml
# Example: Multi-agent workflow with Conductor
# (Third-party orchestrator for Claude + Codex)

workflow:
  - agent: codex
    task: "Generate initial implementation"

  - agent: claude-code
    task: "Review and refactor for production quality"

  - agent: claude-code
    task: "Add comprehensive tests"
```

### GitHub Copilot CLI

GitHub Copilot CLI (enhanced agents, January 2026) provides:
- Context management
- Multiple installation methods
- GitHub-native integration

**Key difference from Claude Code:** Copilot is optimized for GitHub workflows; Claude Code is optimized for general-purpose agentic development with Skills and MCP.

---

## 4. Planning & Workflow Patterns

### The Problem

Claude-driven development projects often span multiple sessions, involve context limits, and require clear progress tracking. Without structured planning files, teams experience:

- Lost context between sessions
- Repeated work due to forgotten decisions
- No visibility into what's pending vs completed
- Difficulty resuming from interruptions

### Recommended File Structure

```
project/
├── planning/
│   ├── task.md        # Backlog and task queue
│   ├── progress.md    # Daily/weekly log
│   └── activity.md    # Timeline of actions
├── CLAUDE.md          # Project-specific rules for Claude
└── ...
```

### task.md — Living Backlog

**Purpose:** Single source of truth for all work items.

**Structure:**
```markdown
# Task Backlog

## Inbox (Unsorted)
- [ ] New feature request from user
- [ ] Bug report #123

## Next 7 Days
- [ ] Implement user authentication
- [ ] Add unit tests for auth module

## In Progress
- [~] Refactoring database layer (started Jan 27)

## Blocked
- [ ] Deploy to production — waiting for security review

## Done (Recent)
- [x] Set up CI/CD pipeline (Jan 26)
- [x] Configure MCP servers (Jan 25)
```

**Usage with Claude:**
- Claude reads `task.md` at session start to understand priorities
- Claude updates status when completing work
- Move items between sections as status changes

### progress.md — Session Log

**Purpose:** Track what happened in each work session.

**Structure:**
```markdown
# Progress Log

## 2026-01-27

### Focus
- Implement user authentication system

### Completed
- Created auth middleware
- Added JWT validation
- Wrote 12 unit tests (all passing)

### Issues
- Found edge case with token refresh — logged in task.md

### Next Steps
- Implement password reset flow
- Add rate limiting
```

**Usage with Claude:**
- Update at end of each session
- Reference in next session to restore context
- Useful for team handoffs

### activity.md — Action Timeline

**Purpose:** Chronological record of all significant actions.

**Structure:**
```markdown
# Activity Timeline

| Timestamp | Action | Tool | Notes |
|-----------|--------|------|-------|
| 2026-01-27 10:30 | Created feature branch | Claude Code | `git checkout -b feature/auth` |
| 2026-01-27 10:45 | Implemented auth middleware | Claude Code | `src/middleware/auth.ts` |
| 2026-01-27 11:00 | Ran tests | Claude Code | All 12 tests passing |
| 2026-01-27 11:15 | Committed changes | Claude Code | `git commit -m "feat: add auth"` |
```

**Usage with Claude:**
- Auto-populate using Claude Code hooks
- Review for debugging and audit trails
- Track which tools were used for each action

### Best Practices for Claude Planning

1. **Read planning files at session start**
   ```
   Before starting work, read planning/task.md and planning/progress.md
   to understand current priorities and recent context.
   ```

2. **Update planning files incrementally**
   ```
   After completing a task, immediately update:
   - task.md: Mark item complete, add any new items discovered
   - progress.md: Add to "Completed" section
   - activity.md: Log the action with timestamp
   ```

3. **Use `/clear` between major task switches**
   - Reset context to avoid "kitchen sink" sessions
   - Rely on planning files to restore necessary context

4. **Treat sessions as branches**
   - Use `/rename` to give sessions descriptive names
   - `claude --resume` to select from named sessions

5. **Integrate with Claude Code hooks**
   ```javascript
   // .claude/hooks/post-commit.js
   // Auto-update activity.md after commits
   const fs = require('fs');
   const timestamp = new Date().toISOString();
   const entry = `| ${timestamp} | Committed | Claude Code | ${process.env.COMMIT_MSG} |\n`;
   fs.appendFileSync('planning/activity.md', entry);
   ```

---

## 5. Tool Selection Guide

### Decision Tree

```
START: What's your primary need?
│
├─ Multi-provider flexibility?
│   └─ YES → OpenCode CLI
│       └─ Have Copilot subscription? → Use Copilot auth (free)
│
├─ Best reasoning + context?
│   └─ YES → Claude Code
│       └─ Need Skills/MCP? → Definitely Claude Code
│
├─ Local/edge inference?
│   └─ YES → AirLLM
│       └─ Production use? → Consider hybrid with Claude API
│
├─ Fast GPT prototyping?
│   └─ YES → OpenAI Codex
│       └─ Need refinement? → Hand off to Claude Code
│
└─ Multi-session project?
    └─ YES → Claude Code + planning/*.md files
```

### Comparison Matrix

| Requirement | OpenCode | Claude Code | AirLLM | Codex |
|-------------|----------|-------------|--------|-------|
| Provider agnostic | ★★★ | ★ | ★★★ | ★ |
| Reasoning quality | ★★ | ★★★ | ★★ | ★★ |
| Context window | ★★ | ★★★ | ★ | ★★ |
| Local execution | ★★★ | ★ | ★★★ | ★ |
| GitHub integration | ★★★ | ★★ | ★ | ★★ |
| Skills/MCP | ★★ | ★★★ | ★ | ★ |
| Cost (with subscription) | ★★★ | ★★ | ★★★ | ★★ |
| Enterprise support | ★ | ★★★ | ★ | ★★ |

### Recommendations by User Type

| User Type | Recommended Setup |
|-----------|-------------------|
| **Solo developer** | Claude Code + AirLLM for experiments |
| **Startup (cost-sensitive)** | OpenCode + Copilot auth |
| **Enterprise** | Claude Code with Skills + Superpowers |
| **Privacy-focused** | AirLLM + OpenCode (local Ollama) |
| **Multi-model experimentation** | OpenCode CLI |
| **Long-running projects** | Claude Code + planning/*.md |

---

## 6. Implementation Checklist

### For OpenCode CLI

- [ ] Install: `curl -fsSL https://opencode.ai/install.sh | bash`
- [ ] Authenticate: `opencode /connect` → GitHub Copilot
- [ ] Configure providers in `~/.opencode/config.yaml`
- [ ] Test: `opencode "Hello world"`
- [ ] Enable GitHub integration: Add `/opencode` to workflows

### For AirLLM Integration

- [ ] Install: `pip install airllm`
- [ ] Download model: Use Hugging Face hub
- [ ] Test inference: Verify VRAM usage
- [ ] Design hybrid pattern: AirLLM + Claude API
- [ ] Implement fallback: Handle offline scenarios

### For Planning Files

- [ ] Create `planning/` directory
- [ ] Initialize `task.md` with current backlog
- [ ] Start `progress.md` for today
- [ ] Add activity logging hook
- [ ] Update CLAUDE.md to reference planning files

### For Claude Code Optimization

- [ ] Configure MCP servers
- [ ] Install relevant Skills
- [ ] Set up hooks for automation
- [ ] Create named sessions for major features
- [ ] Document project rules in CLAUDE.md

---

## Sources

1. OpenCode Official Documentation — https://opencode.ai/docs
2. GitHub Blog: OpenCode Official Support (Jan 2026) — https://github.blog/changelog/2026-01-16-github-copilot-now-supports-opencode/
3. AirLLM GitHub Repository — https://github.com/lyogavin/airllm
4. Claude Code Documentation — https://code.claude.com/docs
5. OpenAI Codex Documentation — https://openai.com/codex
6. Anthropic MCP Documentation — https://modelcontextprotocol.io
7. Dev.to: Top 5 CLI Coding Agents in 2026 — https://dev.to/lightningdev123/top-5-cli-coding-agents-in-2026-3pia
8. Addyosmani: AI Coding Workflow (Jan 2026) — https://addyosmani.com/blog/ai-coding-workflow/
9. Interconnects: Claude Code Analysis — https://www.interconnects.ai/p/claude-code-hits-different
10. DataCamp: Claude Code Hooks Tutorial — https://www.datacamp.com/tutorial/claude-code-hooks

---

**Note on Clawdbot/Clawbot:** Research found no evidence of a tool named "Clawdbot" or "Clawbot" in authoritative sources as of January 2026. This may be a misspelling, regional term, or very new project not yet documented. If you have specific information about this tool, please open an issue to update this documentation.

---

*Last Updated: January 27, 2026*

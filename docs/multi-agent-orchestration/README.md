# Multi-Agent Orchestration at Scale

> Enterprise-grade swarm coordination for 100+ AI agents on Claude Code

## What This Covers

How to run large-scale multi-agent workflows using Claude Code as the foundation. Covers swarm topologies, consensus algorithms, intelligent routing, background workers, and cost optimization through WASM-accelerated code transforms.

---

## Architecture

Four layers working together:

| Layer | What It Does |
|-------|-------------|
| **User** | Claude Code CLI / MCP interface |
| **Orchestration** | MCP server with 313 tools, Q-Learning router, 27 hooks, 130+ skills |
| **Agent Coordination** | 100+ agents, 4 topologies, 5 consensus algorithms, hive mind hierarchy |
| **Intelligence** | Vector database (HNSW), self-learning neural routing, WASM transforms |

---

## Swarm Topologies

| Topology | When to Use | Execution Time |
|----------|------------|---------------|
| **Hierarchical** | Structured development, large projects | ~0.20s |
| **Mesh** | Research, brainstorming, exploration | ~0.15s |
| **Ring** | Sequential pipelines, ordered processing | ~0.12s |
| **Star** | Centralized control with clear leader | ~0.14s |

## Consensus Algorithms

Five ways agents can agree on decisions:

| Algorithm | How It Works | Fault Tolerance |
|-----------|-------------|----------------|
| **Majority** | Simple democratic voting | None |
| **Weighted** | Lead agent gets 3x vote weight | Low |
| **Byzantine (BFT)** | 2/3 supermajority required | Tolerates f < n/3 malicious agents |
| **Raft** | Leader-based log replication with elections | Leader failure recovery |
| **Gossip** | Epidemic protocol with CRDTs for concurrent edits | Scales to large systems |

BFT is particularly interesting here — it tolerates agents that hallucinate divergent outputs, treating them like faulty nodes in a distributed system.

---

## 3-Tier Cost Routing

| Tier | Handler | Latency | Cost |
|------|---------|---------|------|
| 1 | WASM Code Transforms | <1ms | $0 |
| 2 | Haiku/Sonnet | 0.5–2s | $0.0002–$0.003 |
| 3 | Opus + Swarm | 2–5s | $0.015 |

Tier 1 is the key innovation: WebAssembly modules compiled from Rust handle 6 common code transforms (var-to-const, add-types, add-error-handling, async-await, add-logging, remove-console) without any LLM call. This extends a Claude Max subscription by approximately 2.5x.

---

## SPARC Development Methodology

A 5-phase structured workflow:

1. **Specification** — Define requirements and acceptance criteria
2. **Pseudocode** — Write algorithmic logic before implementation
3. **Architecture** — Design system structure and interfaces
4. **Refinement** — Iterate on quality
5. **Completion** — Final verification and deployment

Each phase has a dedicated agent and CLI command. Skip for trivial tasks.

---

## Hive Mind System

Queen-led hierarchical coordination for large agent teams:

**Queen types:** Strategic (planning), Tactical (execution), Adaptive (optimization)

**Worker roles (8):** Researcher, Coder, Analyst, Tester, Architect, Reviewer, Optimizer, Documenter

**Governance modes:**
- Hierarchical — command chains, clear authority
- Democratic — weighted votes from all agents
- Emergency — queen has absolute authority

**Monitoring:** Status reports every 2 minutes. Escalation triggers at <70% success rate or >90% utilization.

---

## Self-Learning Loop

RETRIEVE → JUDGE → DISTILL:

1. **Retrieve** — Find similar past task trajectories via HNSW vector search (<100us latency)
2. **Judge** — Score whether past solutions apply to the current task
3. **Distill** — Extract successful patterns into consolidated templates
4. **Route** — Feed patterns back to the Q-Learning router for future decisions

This is online learning — the system gets better at routing and execution over time.

---

## Hook-Driven Auto-Coordination

After initialization, Claude Code hooks (PreToolUse, PostToolUse) automatically route file edits, bash commands, and searches to the right agents. No explicit commands needed. You interact with Claude Code normally; multi-agent coordination runs invisibly in the background.

---

## Core CLI Commands

```bash
# Initialize
ruflo init --wizard

# Agent management
ruflo agent spawn -t coder --name my-coder
ruflo agent list

# Swarm operations
ruflo swarm init --topology mesh --max-agents 8
ruflo swarm start "Build authentication system"
ruflo swarm status

# Hive mind
ruflo hive-mind spawn --task "Build microservices" --topology hierarchical

# Tasks
ruflo task orchestrate --strategy parallel --priority high

# Memory and learning
ruflo memory search "authentication patterns"
ruflo embeddings search -q "code patterns"

# Monitoring
ruflo status --agents --tasks --memory
ruflo bottleneck-detect
ruflo token-usage

# Background workers
ruflo daemon start
ruflo automation self-healing
```

---

## Key Innovations

- **WASM-first cost strategy** — Skip LLM calls entirely for simple transforms. Most platforms treat LLM calls as mandatory; this treats them as a last resort.
- **Embedded vector database** — 77+ SQL functions for PostgreSQL implementing HNSW and attention mechanisms. No external vector DB needed.
- **Cryptographic policy enforcement** — CLAUDE.md rules compiled into typed bundles with HMAC-SHA256 proof-chains for compliance auditing.
- **Dual-mode execution** — Can spawn workers from other LLM providers (not just Claude) within the same session with shared cross-platform memory.
- **Architecture decision records as live governance** — 70+ ADRs with real-time compliance monitoring. Drift from constraints triggers alerts.

---

## Included Resources

| Type | Count |
|------|-------|
| Agent definitions | 90+ |
| Skill packages | 130+ |
| Slash commands | 150+ |
| MCP servers | 3 |
| Lifecycle hooks | 27 |

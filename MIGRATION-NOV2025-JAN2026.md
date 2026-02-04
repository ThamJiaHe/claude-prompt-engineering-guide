# Migration Guide: November 2025 → January 2026

Migrate your Claude workflows from November 2025 to January 2026 ecosystem.

> **Last Updated: February 4, 2026** | Covers all breaking changes, deprecations, and new features

---

## Quick Summary

| Area | Change | Action Required |
|------|--------|-----------------|
| **Model** | Opus 4.1 → Opus 4.5 | Update model ID |
| **Deprecations** | Opus 4, 4.1 removed from UI & Claude Code | Use Opus 4.5; API-only for 4.x |
| **API** | Effort parameter added | Optional, use for complex tasks |
| **MCP** | SSE deprecated | Migrate to streamableHttp |
| **Claude Code** | v1.x → v2.x | Update CLI, learn new commands |
| **Skills** | New wrapper pattern | Refactor for token efficiency |
| **Hooks** | New best practices | Move validation to submit time |

---

## 1. Model Migration

### Claude Opus 4.5 (November 24, 2025)

**What Changed:**
- New flagship model with improved reasoning
- Support for `effort` parameter
- Better performance on complex tasks

**Migration Steps:**

1. **Update Model ID**
   ```python
   # OLD
   model = "claude-opus-4-1-20250505"

   # NEW
   model = "claude-opus-4-5-20251101"
   ```

2. **Add Effort Parameter (Optional)**
   ```python
   import anthropic

   client = anthropic.Anthropic()

   response = client.beta.messages.create(
       model="claude-opus-4-5-20251101",
       betas=["effort-2025-11-24"],
       max_tokens=4096,
       messages=[{"role": "user", "content": "Complex analysis..."}],
       output_config={"effort": "medium"}  # low, medium, high
   )
   ```

**Effort Level Guidelines:**
| Level | Use Case | Token Usage |
|-------|----------|-------------|
| `low` | Simple queries, quick responses | ~1x baseline |
| `medium` | Standard tasks, balanced | ~2x baseline |
| `high` | Complex reasoning, deep analysis | ~4x baseline |

### Model Deprecations (January 2026)

The following models have been **removed from Claude's UI and Claude Code**:

| Model | Status | API Access | Action Required |
|-------|--------|------------|-----------------|
| **Claude Opus 4** | Removed from UI/Code | GA via API only | Migrate to Opus 4.5 |
| **Claude Opus 4.1** | Removed from UI/Code | GA via API only | Migrate to Opus 4.5 |
| **Claude 3 Opus** | Fully retired (Jan 5, 2026) | No longer available | Migrate to Opus 4.5 |
| **Claude Sonnet 3.5** | Retired (Oct 28, 2025) | No longer available | Migrate to Sonnet 4.5 |

Anthropic published guidance on "Adapting to new model personas after deprecations" for users transitioning to Opus 4.5.

---

## 2. MCP Transport Migration

### SSE → streamableHttp

**What Changed:**
- SSE transport deprecated (November 2025)
- streamableHttp is the new standard
- Better connection stability and async support

**Migration Steps:**

1. **Update Configuration**
   ```json
   // OLD (Deprecated)
   {
     "mcpServers": {
       "server": {
         "transport": "sse",
         "url": "https://example.com/sse"
       }
     }
   }

   // NEW (Recommended)
   {
     "mcpServers": {
       "server": {
         "type": "streamableHttp",
         "url": "https://example.com/mcp"
       }
     }
   }
   ```

2. **Update Endpoint Paths**
   - SSE endpoints typically used `/sse` or `/events`
   - streamableHttp uses `/mcp` convention

3. **Test Connection**
   ```bash
   # Verify MCP server is accessible
   curl -X POST https://example.com/mcp \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc":"2.0","method":"initialize","id":1}'
   ```

---

## 3. Context7 MCP Setup

### New: Up-to-Date Library Documentation

**Why Add Context7:**
- Get current library docs (not outdated training data)
- Ranked #2 in "Top 10 MCP Servers 2026"
- Version-specific documentation

**Setup Steps:**

1. **Get API Key**
   - Visit [context7.com](https://context7.com)
   - Create account and generate API key

2. **Add to Configuration**
   ```json
   {
     "mcpServers": {
       "context7": {
         "url": "https://mcp.context7.com/mcp",
         "type": "streamableHttp",
         "headers": {
           "Authorization": "Bearer YOUR_API_KEY"
         }
       }
     }
   }
   ```

3. **Alternative: Local stdio**
   ```json
   {
     "mcpServers": {
       "context7": {
         "command": "npx",
         "args": ["-y", "@upstash/context7-mcp", "--api-key", "YOUR_API_KEY"]
       }
     }
   }
   ```

---

## 4. Claude Code v2.x Migration

### New Commands and Features

**What's New:**
- Plan Mode with subagents
- `/rewind` command for undo
- `/usage` command for monitoring
- GitHub Actions integration
- Automatic continuation

**Migration Steps:**

1. **Update Claude Code**
   ```bash
   npm update -g @anthropic-ai/claude-code
   claude --version  # Should show v2.1.0+
   ```

2. **Learn New Commands**
   ```bash
   # Plan Mode
   /plan "Build a REST API for user management"

   # Undo changes
   /rewind
   /rewind 3  # Undo 3 steps

   # Monitor usage
   /usage
   ```

3. **Setup GitHub Actions**
   ```bash
   /install-github-app
   ```

4. **Adopt 4-Step Workflow**
   ```
   Step 1: RESEARCH - "What information do you need?"
   Step 2: PLAN - "Create a plan but don't code yet"
   Step 3: IMPLEMENT - "Now implement your plan"
   Step 4: COMMIT - "Commit the result and create PR"
   ```

**Deprecated:**
- `--output-style` flag → Use `--append-system-prompt-file` instead

```bash
# OLD (Deprecated)
claude --output-style=detailed -p "Your prompt"

# NEW (Recommended)
claude --append-system-prompt-file=~/.claude/system-prompt.md -p "Your prompt"
```

---

## 5. Skills Wrapper Pattern

### Token-Efficient Architecture

**What Changed:**
- New wrapper pattern for skills
- Progressive disclosure reduces context overhead
- Heavy logic loaded on-demand

**Migration Steps:**

1. **Identify Heavy Skills**
   - Skills over 200 lines
   - Skills with extensive examples
   - Skills rarely used but always loaded

2. **Refactor to Wrapper Pattern**

   **Before:**
   ```
   my-skill/
   └── SKILL.md  # 1,500 lines - always in context
   ```

   **After:**
   ```
   my-skill/
   ├── SKILL.md              # 50-100 lines - always in context
   └── implementation/
       └── full-logic.md     # 1,400 lines - loaded on demand
   ```

3. **Update SKILL.md Structure**
   ```markdown
   ---
   name: my-skill
   description: Brief description for discovery
   ---

   # My Skill

   ## When to Use
   [Brief guidance]

   ## How It Works
   [High-level overview]

   ## Implementation
   See ./implementation/full-logic.md for complete details.
   ```

---

## 6. Hooks Best Practices

### Block-at-Submit Pattern

**What Changed:**
- New guidance: validate at end, not during work
- Input modification preferred over blocking
- Smoother workflow, fewer interrupts

**Migration Steps:**

1. **Move Validation to Submit Time**

   **Before (Blocking during work):**
   ```typescript
   // PreToolUse hook - blocks frequently
   export function preToolUse(input: ToolInput) {
     if (input.tool === "write" && hasIssue(input)) {
       return { blocked: true, reason: "Issue found" };
     }
   }
   ```

   **After (Validate at submit):**
   ```typescript
   // UserPromptSubmit hook - validates at end
   export function userPromptSubmit(context: SubmitContext) {
     const issues = validateAllChanges(context);
     if (issues.length > 0) {
       return { blocked: true, reason: formatIssues(issues) };
     }
   }
   ```

2. **Use Input Modification**

   **Before (Blocking):**
   ```typescript
   if (badInput) {
     return { blocked: true, reason: "Invalid input" };
   }
   ```

   **After (Fixing):**
   ```typescript
   if (badInput) {
     return { updatedInput: correctedInput };
   }
   ```

---

## 7. Context Window Management

### Critical: Multiple MCP Servers

**Problem:**
- 7 MCP servers = 67,300 tokens consumed at startup
- Only 33% of 200K context budget remaining

**Migration Steps:**

1. **Audit MCP Servers**
   ```bash
   # List active MCP servers
   claude --list-mcp-servers
   ```

2. **Disable Unused Servers**
   - Keep servers installed but OFF
   - Enable only when needed

3. **Use Dynamic Loading**
   ```json
   {
     "mcpServers": {
       "context7": {
         "autoStart": false,
         "loadOnDemand": true
       }
     }
   }
   ```

4. **Whitelist Tools**
   ```json
   {
     "mcpServers": {
       "perplexity": {
         "toolConfiguration": {
           "enabled": true,
           "allowedTools": ["search", "research"]
         }
       }
     }
   }
   ```

---

## 8. Self-Evolving CLAUDE.md

### New Pattern: Living Documentation

**What's New:**
- CLAUDE.md files that update during development
- Captures project conventions automatically
- Reduces repeated explanations

**Setup Steps:**

1. **Create CLAUDE.md**
   ```bash
   touch CLAUDE.md
   ```

2. **Add Basic Structure**
   ```markdown
   # CLAUDE.md

   ## Critical Rules
   - Never commit directly to main
   - All changes require tests

   ## Learned Conventions
   <!-- Claude updates this section -->

   ## Session Learnings
   <!-- Temporary learnings for review -->
   ```

3. **Enable Self-Updates**
   - Tell Claude it can update CLAUDE.md
   - Review Session Learnings periodically
   - Commit valuable learnings to git

See [templates/example-clauderules.md](./templates/example-clauderules.md) for complete template.

---

## 9. Breaking Changes Checklist

### Before Migration

- [ ] Document current model IDs in use
- [ ] List all MCP servers and their transport types
- [ ] Inventory skills over 200 lines
- [ ] Note any hooks using blocking patterns
- [ ] Check Claude Code version

### During Migration

- [ ] Update model IDs to Opus 4.5
- [ ] Migrate SSE to streamableHttp
- [ ] Add Context7 for library docs
- [ ] Update Claude Code to v2.x
- [ ] Refactor heavy skills to wrapper pattern
- [ ] Move hook validation to submit time

### After Migration

- [ ] Test all MCP connections
- [ ] Verify skills load correctly
- [ ] Check hooks don't over-block
- [ ] Monitor context window usage
- [ ] Review usage limits with `/usage`

---

## 10. Common Issues

### Issue: Rate Limits Hit Faster

**Cause:** January 2026 usage limit changes

**Solution:**
- Monitor with `/usage` command
- Optimize prompts for token efficiency
- Consider Enterprise for higher limits

### Issue: MCP Connection Failures

**Cause:** SSE transport deprecated

**Solution:**
- Update to streamableHttp
- Check endpoint paths
- Verify authentication headers

### Issue: Skills Not Loading

**Cause:** Wrapper pattern not followed

**Solution:**
- Keep SKILL.md under 100 lines
- Reference implementation files correctly
- Test skill discovery with matching query

### Issue: Performance Degradation

**Cause:** Console history accumulation

**Solution:**
- Restart Claude Code periodically
- Disable `/rewind` if experiencing issues
- Use `--append-system-prompt-file`

---

## Resources

- [Claude Code Guide](./docs/claude-code-guide.md)
- [MCP Integration Guide](./docs/mcp-integration.md)
- [Skills Guide](./docs/skills-guide.md)
- [Superpowers Guide](./docs/superpowers-guide.md)
- [CHANGELOG](./CHANGELOG.md)

---

*Last Updated: February 4, 2026*

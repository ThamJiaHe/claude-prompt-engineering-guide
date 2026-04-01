# Model Routing — Use Any LLM Provider with Claude Code

> How to route Claude Code requests to DeepSeek, Gemini, Ollama, OpenRouter, or any OpenAI-compatible API

## How It Works

A proxy server intercepts Claude Code's API calls by setting `ANTHROPIC_BASE_URL` to a local endpoint (e.g., `http://127.0.0.1:3456`). The proxy inspects each request and forwards it to the right model provider based on configurable rules.

This lets you use Claude Code's agentic interface with any model from any provider.

---

## Routing Logic (Priority Order)

When a request arrives, the router checks these conditions top to bottom:

1. **Explicit model** — If the request contains `provider,model` format, use it directly
2. **Custom router script** — If a JavaScript router function exists, let it decide
3. **Subagent tag** — If the system prompt contains a `<CCR-SUBAGENT-MODEL>` tag, use that model
4. **Long context** — If token count exceeds threshold (default 60k), route to long-context model
5. **Background task** — If the model name contains `haiku`, route to background model
6. **Web search** — If any tool starts with `web_search`, route to search-capable model
7. **Thinking mode** — If `req.body.thinking` is set, route to reasoning model
8. **Default** — Use the configured default model

---

## Configuration

```json
{
  "Router": {
    "default": "deepseek,deepseek-chat",
    "background": "ollama,qwen2.5-coder:latest",
    "think": "deepseek,deepseek-reasoner",
    "longContext": "openrouter,google/gemini-2.5-pro-preview",
    "longContextThreshold": 60000,
    "webSearch": "gemini,gemini-2.5-flash",
    "image": "gemini,gemini-2.5-pro"
  }
}
```

Each route maps a scenario to a `provider,model` string. Fallback chains are supported — on HTTP error, the next provider in the chain is tried automatically.

---

## Supported Providers

Works with any OpenAI-compatible endpoint. Built-in transformer support for:

| Provider | Transformer | Notes |
|----------|------------|-------|
| DeepSeek | `deepseek` | Cheapest option for default coding tasks |
| Gemini | `gemini` | Best for long context (1M window) and web search |
| OpenRouter | `openrouter` | Access to hundreds of models |
| Ollama | `openai` | Free local inference |
| Groq | `groq` | Fast inference, generous free tier |
| Cerebras | `cerebras` | Ultra-fast inference |
| Volcengine | `openai` | Chinese provider |
| SiliconFlow | `openai` | Chinese provider |

---

## Transformers

Transformers convert between Claude Code's Anthropic API format and other providers:

**Format converters:** `anthropic`, `deepseek`, `gemini`, `openai`, `openrouter`, `groq`, `cerebras`

**Behavior modifiers:** `tooluse` (force tool calling), `enhancetool` (buffer and fix tool args), `maxtoken` (cap output), `reasoning` (map thinking blocks), `cleancache` (strip prompt cache)

The `tooluse` transformer deserves special mention: it injects `tool_choice: "required"` and adds a synthetic `ExitTool`. When the model wants to respond in plain text, it calls ExitTool, which the proxy intercepts and converts back to a normal response. This fixes DeepSeek's tendency to abandon tool use mid-conversation.

---

## Cost Optimization Strategies

1. **Cheap default + capable thinking** — Use DeepSeek ($0.14/MTok) for routine coding, reasoning models only for plan mode
2. **Free background tasks** — Route Haiku-tagged requests to Ollama (free, local) instead of Anthropic
3. **Long context to specialists** — Send large context to Gemini (1M window, competitive pricing)
4. **Local models for privacy** — Route sensitive code to Ollama running locally
5. **Fallback chains** — When a provider's quota is exhausted, auto-fallback to the next cheapest option

A typical setup costs 90% less than routing everything through Claude.

---

## Per-Project and Per-Session Routing

Override routing at different levels:

- **Global:** `~/.claude-code-router/config.json`
- **Per-project:** `~/.claude/projects/<project-id>/claude-code-router.json`
- **Per-session:** `<project-dir>/<sessionId>.json`

This lets you use cheap models for one project and expensive ones for another.

---

## Subagent Model Pinning

Pin specific models to subagents by adding a tag at the start of the subagent's system prompt:

```
<CCR-SUBAGENT-MODEL>provider,model</CCR-SUBAGENT-MODEL>
```

The proxy reads and strips this tag before forwarding. Each subagent can use a different model without modifying Claude Code itself.

---

## Key Commands

```bash
ccr code          # Launch Claude Code through the router
ccr start         # Start router as background service
ccr model         # Interactive model selector TUI
ccr ui            # Open web-based config editor
ccr preset export # Save and share configurations
eval "$(ccr activate)"  # Set env vars for direct claude usage
```

---

## Security

- Binds to `127.0.0.1` only when no API key is set (localhost-only)
- Environment variable interpolation (`$VAR`) keeps secrets out of config files
- Setting an API key enables remote access with `Authorization: Bearer` authentication

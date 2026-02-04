# Claude API Integration Guide

Build applications with the Claude API.

> **Last Updated: January 23, 2026** | Covers Claude Opus 4.5, effort parameter, streaming, and best practices

---

## Overview

The Claude API enables you to integrate Claude's capabilities into your applications. This guide covers authentication, basic requests, advanced features, and best practices.

### Current Models (January 2026)

| Model | Model ID | Best For |
|-------|----------|----------|
| **Claude Opus 4.5** | `claude-opus-4-5-20251101` | Complex reasoning, coding, analysis |
| **Claude Sonnet 4.5** | `claude-sonnet-4-5-20250929` | Balanced performance and cost |
| **Claude Haiku 4.5** | `claude-haiku-4-5-20251201` | Fast, cost-effective tasks |

**Recommended**: Use Claude Opus 4.5 for high-stakes tasks requiring deep reasoning.

---

## Authentication

### API Keys

Get your API key from the [Anthropic Console](https://console.anthropic.com/).

```bash
# Set environment variable
export ANTHROPIC_API_KEY="sk-ant-api03-..."
```

**Security**: Never commit API keys to version control. Use environment variables or secret managers.

### Request Headers

```bash
Authorization: Bearer $ANTHROPIC_API_KEY
Content-Type: application/json
anthropic-version: 2024-01-01
```

---

## Quick Start

### Basic Request (curl)

```bash
curl https://api.anthropic.com/v1/messages \
  -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
  -H "Content-Type: application/json" \
  -H "anthropic-version: 2024-01-01" \
  -d '{
    "model": "claude-opus-4-5-20251101",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "Explain quantum computing in simple terms"}
    ]
  }'
```

### Python SDK

```python
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Explain quantum computing in simple terms"}
    ]
)

print(message.content[0].text)
```

### TypeScript/JavaScript SDK

```typescript
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic();

const message = await anthropic.messages.create({
  model: "claude-opus-4-5-20251101",
  max_tokens: 1024,
  messages: [
    { role: "user", content: "Explain quantum computing in simple terms" }
  ]
});

console.log(message.content[0].text);
```

---

## Core Parameters

### Essential Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `model` | string | Model ID (required) |
| `messages` | array | Conversation history (required) |
| `max_tokens` | integer | Maximum response tokens (required) |
| `system` | string | System prompt (optional) |
| `temperature` | float | Randomness 0-1 (default: 1) |

### Example with All Parameters

```python
message = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=4096,
    system="You are a senior software architect. Provide detailed technical guidance.",
    messages=[
        {"role": "user", "content": "Design a microservices architecture for an e-commerce platform"}
    ],
    temperature=0.7
)
```

---

## Effort Parameter (Claude Opus 4.5)

The `effort` parameter controls Claude's thinking depth for complex tasks.

### Beta Header Required

```bash
anthropic-beta: effort-2025-11-24
```

### Effort Levels

| Level | Use Case | Token Usage |
|-------|----------|-------------|
| `low` | Quick tasks, simple questions | Minimal |
| `medium` | Balanced reasoning (default) | Moderate |
| `high` | Complex analysis, critical decisions | Maximum |

### Python Example

```python
message = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=8192,
    betas=["effort-2025-11-24"],
    effort="high",
    messages=[
        {"role": "user", "content": "Analyze this codebase for security vulnerabilities"}
    ]
)
```

### When to Use High Effort

- Security audits
- Complex debugging
- Architecture decisions
- Multi-step reasoning
- Critical code reviews

---

## Streaming

Stream responses for better user experience with long outputs.

### Python Streaming

```python
with client.messages.stream(
    model="claude-opus-4-5-20251101",
    max_tokens=4096,
    messages=[{"role": "user", "content": "Write a detailed technical specification"}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

### TypeScript Streaming

```typescript
const stream = anthropic.messages.stream({
  model: "claude-opus-4-5-20251101",
  max_tokens: 4096,
  messages: [{ role: "user", content: "Write a detailed technical specification" }]
});

for await (const event of stream) {
  if (event.type === "content_block_delta" && event.delta.type === "text_delta") {
    process.stdout.write(event.delta.text);
  }
}
```

---

## Tool Use (Function Calling)

Enable Claude to call functions in your application.

### Define Tools

```python
tools = [
    {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City name, e.g., 'San Francisco, CA'"
                }
            },
            "required": ["location"]
        }
    }
]

message = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "What's the weather in Tokyo?"}]
)
```

### Handle Tool Calls

```python
if message.stop_reason == "tool_use":
    tool_use = next(block for block in message.content if block.type == "tool_use")

    # Execute the tool
    result = get_weather(tool_use.input["location"])

    # Continue conversation with result
    response = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=1024,
        tools=tools,
        messages=[
            {"role": "user", "content": "What's the weather in Tokyo?"},
            {"role": "assistant", "content": message.content},
            {
                "role": "user",
                "content": [{
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": result
                }]
            }
        ]
    )
```

---

## Vision (Image Input)

Send images for analysis.

### Base64 Encoding

```python
import base64

with open("image.png", "rb") as f:
    image_data = base64.standard_b64encode(f.read()).decode("utf-8")

message = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/png",
                    "data": image_data
                }
            },
            {
                "type": "text",
                "text": "Describe what you see in this image"
            }
        ]
    }]
)
```

### URL Reference

```python
message = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "image",
                "source": {
                    "type": "url",
                    "url": "https://example.com/image.png"
                }
            },
            {
                "type": "text",
                "text": "Analyze this diagram"
            }
        ]
    }]
)
```

---

## Error Handling

### Common Errors

| Status Code | Error | Solution |
|-------------|-------|----------|
| 400 | Invalid request | Check request format |
| 401 | Authentication failed | Verify API key |
| 429 | Rate limited | Implement backoff |
| 500 | Server error | Retry with backoff |
| 529 | Overloaded | Wait and retry |

### Python Error Handling

```python
import anthropic

try:
    message = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=1024,
        messages=[{"role": "user", "content": "Hello"}]
    )
except anthropic.BadRequestError as e:
    print(f"Bad request: {e}")
except anthropic.AuthenticationError as e:
    print(f"Authentication failed: {e}")
except anthropic.RateLimitError as e:
    print(f"Rate limited. Retry after: {e}")
except anthropic.APIError as e:
    print(f"API error: {e}")
```

### Retry with Exponential Backoff

```python
import time
import random

def call_with_retry(func, max_retries=3):
    for attempt in range(max_retries):
        try:
            return func()
        except anthropic.RateLimitError:
            if attempt == max_retries - 1:
                raise
            wait_time = (2 ** attempt) + random.random()
            time.sleep(wait_time)
```

---

## Best Practices

### 1. System Prompts

Use system prompts to define Claude's role and behavior:

```python
system = """You are a senior security engineer conducting code reviews.
Focus on:
- OWASP Top 10 vulnerabilities
- Authentication/authorization issues
- Data validation problems
Severity ratings: CRITICAL, HIGH, MEDIUM, LOW"""

message = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=4096,
    system=system,
    messages=[{"role": "user", "content": f"Review this code:\n\n{code}"}]
)
```

### 2. Conversation History

Maintain context across multi-turn conversations:

```python
messages = []

# First turn
messages.append({"role": "user", "content": "Explain REST APIs"})
response = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=1024,
    messages=messages
)
messages.append({"role": "assistant", "content": response.content[0].text})

# Second turn
messages.append({"role": "user", "content": "Now explain GraphQL"})
response = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=1024,
    messages=messages
)
```

### 3. Token Management

Monitor and manage token usage:

```python
message = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
)

print(f"Input tokens: {message.usage.input_tokens}")
print(f"Output tokens: {message.usage.output_tokens}")
```

### 4. Structured Output

Request JSON for programmatic parsing:

```python
system = """Return responses in JSON format:
{
  "summary": "Brief summary",
  "key_points": ["point1", "point2"],
  "recommendations": ["rec1", "rec2"]
}"""

message = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=1024,
    system=system,
    messages=[{"role": "user", "content": "Analyze this business proposal"}]
)

import json
result = json.loads(message.content[0].text)
```

---

## Rate Limits

### Default Limits (varies by tier)

| Tier | Requests/min | Tokens/min |
|------|--------------|------------|
| Free | 5 | 20,000 |
| Build | 50 | 80,000 |
| Scale | 1,000 | 400,000 |

### Check Headers

```python
# Rate limit info in response headers
# x-ratelimit-limit-requests
# x-ratelimit-remaining-requests
# x-ratelimit-reset-requests
```

---

## Pricing (January 2026)

| Model | Input (per 1M tokens) | Output (per 1M tokens) |
|-------|----------------------|------------------------|
| Opus 4.5 | $5.00 | $25.00 |
| Sonnet 4.5 | $3.00 | $15.00 |
| Haiku 4.5 | $0.25 | $1.25 |

**Tip**: Use Haiku for simple tasks, Opus for complex reasoning to optimize costs.

---

## SDKs and Libraries

### Official SDKs

- **Python**: `pip install anthropic`
- **TypeScript**: `npm install @anthropic-ai/sdk`

### Community Libraries

- Go: `github.com/anthropics/anthropic-sdk-go`
- Ruby: `gem install anthropic`
- Java: Maven central `anthropic-java`

---

## Resources

- **API Reference**: [docs.anthropic.com/api](https://docs.anthropic.com/api)
- **Console**: [console.anthropic.com](https://console.anthropic.com)
- **Status**: [status.anthropic.com](https://status.anthropic.com)
- **Discord**: [discord.gg/anthropic](https://discord.gg/anthropic)

---

## Related Guides

- [Claude Prompt Engineering Guide](../Claude-Prompt-Guide.md) - Master prompt crafting
- [MCP Integration](./mcp-integration.md) - External tool connections
- [Claude Code Guide](./claude-code-guide.md) - CLI development tool

---

**Last Updated:** January 23, 2026
**Version:** 1.0.0
**Status:** Production Ready

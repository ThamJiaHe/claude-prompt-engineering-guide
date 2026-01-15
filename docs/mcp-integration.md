# MCP Integration Guide

Learn how to integrate Model Context Protocol (MCP) with Claude for extended capabilities.

> **Last Updated: January 15, 2026** | Includes Context7 MCP, dynamic loading patterns, and context window management

---

## What is MCP?

**Model Context Protocol (MCP)** is Anthropic's standardized protocol that allows Claude to interact with external tools, data sources, and services beyond its built-in capabilities.

### Key Benefits

- ✅ **Real-time Data** — Access current information beyond knowledge cutoff
- ✅ **Custom Tools** — Connect to your own systems and APIs
- ✅ **Local Files** — Read and write files on your machine
- ✅ **External Services** — Integrate with databases, APIs, and platforms

### January 2026 Updates

- **Context7 MCP** — Up-to-date library documentation (#2 ranked MCP server)
- **Dynamic loading** — Load/unload MCP servers during sessions
- **SSE deprecated** — Migrate to streamableHttp transport
- **Context window management** — Critical for multiple MCP servers

---

## MCP in Different Environments

### Claude.ai Web Interface
- **MCP Support**: Limited
- **Available**: Built-in tools only (web search, file upload)
- **Custom MCP**: Not currently available

### Claude Desktop App
- **MCP Support**: Full ✅
- **Custom MCP**: Yes, via configuration
- **Configuration File**: `claude_desktop_config.json`

**Location:**
- **macOS**: `~/Library/Application Support/Claude/`
- **Windows**: `%APPDATA%\Claude\`
- **Linux**: `~/.config/Claude/`

### Claude Code (CLI)
- **MCP Support**: Full ✅
- **Custom MCP**: Yes, via `--mcp-config` flag
- **Configuration**: File or inline

### Claude API
- **MCP Support**: Full ✅
- **Custom MCP**: Yes, in message requests
- **Requires**: Beta header `anthropic-beta: mcp-client-2025-04-04`

---

## MCP Filesystem Server

### What It Does

Gives Claude access to your local filesystem:
- Read files and directories
- Write and edit files
- Create directories
- Search files by pattern
- Get file information

### Setup (Claude Desktop)

1. **Open configuration file**
   ```json
   // macOS/Linux: ~/Library/Application Support/Claude/claude_desktop_config.json
   // Windows: %APPDATA%\Claude\claude_desktop_config.json
   ```

2. **Add filesystem MCP**
   ```json
   {
     "mcpServers": {
       "filesystem": {
         "command": "npx",
         "args": [
           "-y",
           "@modelcontextprotocol/server-filesystem",
           "/path/to/your/directory"
         ]
       }
     }
   }
   ```

3. **Restart Claude Desktop**

4. **Grant permissions** when Claude asks

### Example: Working with Projects

```json
{
  "mcpServers": {
    "projects": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/yourname/projects"
      ]
    }
  }
}
```

Now Claude can:
```
"Read the README.md file from my projects"
"Create a new Python script in my projects"
"Search for all TODO comments in my code"
```

---

## MCP via Claude Code CLI

### Basic Usage

```bash
# With default config
claude -p "Your prompt here"

# With custom MCP config
claude --mcp-config ./mcp-config.json -p "Your prompt"

# With system prompt
claude --system-prompt "You are a senior engineer" -p "Your prompt"
```

### MCP Config File

Create `mcp-config.json`:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "."
      ]
    },
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github",
        "YOUR_GITHUB_TOKEN"
      ]
    }
  }
}
```

### Example Workflow

```bash
# Start Claude Code with MCP enabled
claude --mcp-config ./mcp-config.json -p "Analyze the codebase for security issues"

# Claude can now:
# 1. Read files from the filesystem
# 2. Access GitHub API
# 3. Perform searches across the repo
```

---

## MCP via Claude API

### Setup

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

# Include beta header for MCP support
response = client.messages.create(
    model="claude-opus-4-20250514",
    max_tokens=2048,
    system="You are a helpful assistant with access to local files and web search.",
    messages=[
        {
            "role": "user",
            "content": "Read the configuration file and summarize it"
        }
    ],
    # Beta feature for MCP
    headers={
        "anthropic-beta": "mcp-client-2025-04-04"
    },
    # MCP configuration
    mcp_config={
        "mcpServers": {
            "filesystem": {
                "command": "npx",
                "args": [
                    "-y",
                    "@modelcontextprotocol/server-filesystem",
                    "/path/to/files"
                ]
            }
        }
    }
)
```

---

## Context Window Problem (CRITICAL)

**Warning**: Multiple MCP servers can consume massive context before any conversation starts.

### Real-World Example
- 7 MCP servers active
- **67,300 tokens consumed** (33.7% of 200K context budget)
- **Before any conversation starts**

### Why This Matters
Each MCP server registers its tools with Claude. Tool definitions consume context tokens. More servers = more token consumption = less room for actual conversation.

### Solutions

#### 1. Keep MCP Servers Disabled When Not Using
```
Best Practice (Jan 2026):
- Keep most MCP servers installed but TURNED OFF
- Only enable servers you're actively using
- Claude Code knows what MCPs you have, will ask to enable if needed
```

#### 2. Lazy-Load MCP Tools
Only load tool definitions when needed, not at startup.

#### 3. Dynamic MCP Loading
Load during session as needed, unload when done:
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

#### 4. MCP Tool Whitelisting
Explicitly allow only specific tools:
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

## Context7 MCP Configuration

Context7 provides **up-to-date, version-specific library documentation**. Ranked #2 in "Top 10 MCP Servers 2026".

### Why Use Context7?
- Get latest React 19 docs (not outdated React 18)
- Fetch version-specific API changes
- Pull examples from official sources
- Avoid LLM knowledge cutoff issues

### Remote HTTP Configuration (Recommended)
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

### Local stdio Configuration
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

### OAuth Support
Change endpoint from `/mcp` to `/mcp/oauth` for OAuth 2.0 authentication:
```json
{
  "mcpServers": {
    "context7": {
      "url": "https://mcp.context7.com/mcp/oauth",
      "type": "streamableHttp"
    }
  }
}
```

### Usage Example
```
User: "Show me the latest Next.js 15 App Router documentation"

Claude will use Context7 to fetch current Next.js 15 docs,
not outdated training data from 2024.
```

---

## Popular MCP Servers

### First-Party (Anthropic)

| Server | Purpose | Usage |
|--------|---------|-------|
| **Filesystem** | Read/write local files | File operations |
| **GitHub** | GitHub API access | Repository queries |
| **Slack** | Slack workspace access | Team communication |

### Community (Top Ranked Jan 2026)

| Server | Purpose | Ranking |
|--------|---------|---------|
| **Context7** | Up-to-date library docs | #2 |
| **Perplexity** | Web research | Top 10 |
| **Web Search** | Real-time search | Popular |
| **Database** | SQL queries | Popular |
| **AWS** | Amazon Web Services | Popular |
| **Docker** | Container management | Popular |

---

## Real-World Example: Code Analysis

### Setup

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "."
      ]
    }
  }
}
```

### Usage

```xml
<system_prompt>
You are a senior security engineer. You have access to the filesystem.
</system_prompt>

<task>
Analyze the authentication system for security vulnerabilities.
</task>

<rules>
- Read all files in the auth/ directory
- Identify security issues
- Check for OWASP vulnerabilities
- Provide specific fixes
</rules>

<format>
Structure your response as:
1. Overview of authentication system
2. Security vulnerabilities found
3. Specific fixes for each vulnerability
4. Severity assessment (CRITICAL, HIGH, MEDIUM, LOW)
</format>
```

Claude can now:
1. Read all files in the auth/ directory
2. Analyze the code
3. Find vulnerabilities
4. Provide specific fixes

---

## Troubleshooting

### Issue: MCP Server Not Found

**Solution:**
```bash
# Make sure npx is available
npx --version

# Update npx
npm install -g npm@latest
```

### Issue: Permission Denied

**Solution:**
```bash
# Grant permissions in Claude Desktop settings
# Restart Claude Desktop
# Re-authorize when prompted
```

### Issue: Config File Not Recognized

**Solution:**
```bash
# Verify the config file path
# Use absolute paths
# Restart Claude

# For Claude Code:
claude --mcp-config /full/path/to/mcp-config.json -p "Your prompt"
```

---

## Best Practices

1. **Start with Filesystem** — Easiest to set up and use
2. **Test Permissions** — Verify Claude can access required files
3. **Use Specific Paths** — Don't give access to entire home directory
4. **Limit Scope** — Only enable servers you actually need
5. **Error Handling** — Be prepared for server unavailability

---

## Next Steps

1. **Set up Filesystem MCP** — Follow the Claude Desktop instructions above
2. **Test with a simple prompt** — "What files are in my current directory?"
3. **Explore additional servers** — GitHub, web search, etc.
4. **Integrate into workflows** — Use in Claude Code for development tasks

---

---

## SSE Transport Migration (Deprecated)

**Status**: SSE transport is deprecated as of November 2025.

### Migration: SSE → streamableHttp

**OLD (Deprecated)**:
```json
{
  "mcpServers": {
    "server": {
      "transport": "sse",
      "url": "https://example.com/sse"
    }
  }
}
```

**NEW (Recommended)**:
```json
{
  "mcpServers": {
    "server": {
      "type": "streamableHttp",
      "url": "https://example.com/mcp"
    }
  }
}
```

### Why Migrate?
- SSE has connection stability issues
- streamableHttp supports async operations
- Better error handling and recovery
- Future MCP features require streamableHttp

---

## MCP Wildcard Permissions

For trusted MCP servers, you can grant wildcard permissions:

```json
{
  "mcpServers": {
    "perplexity": {
      "permissions": ["mcpserver:*"]
    }
  }
}
```

**Warning**: Only use wildcards for servers you fully trust.

---

## Learn More

- [MCP Official Documentation](https://modelcontextprotocol.io)
- [Anthropic MCP Guide](https://docs.anthropic.com)
- [Community MCP Servers](https://github.com/modelcontextprotocol)
- [Context7 MCP](https://github.com/upstash/context7)

---

*Last Updated: January 15, 2026*


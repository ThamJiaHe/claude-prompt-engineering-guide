# MCP Integration Guide

Learn how to integrate Model Context Protocol (MCP) with Claude for extended capabilities.

---

## What is MCP?

**Model Context Protocol (MCP)** is Anthropic's standardized protocol that allows Claude to interact with external tools, data sources, and services beyond its built-in capabilities.

### Key Benefits

- ✅ **Real-time Data** — Access current information beyond knowledge cutoff
- ✅ **Custom Tools** — Connect to your own systems and APIs
- ✅ **Local Files** — Read and write files on your machine
- ✅ **External Services** — Integrate with databases, APIs, and platforms

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

## Popular MCP Servers

### First-Party (Anthropic)

| Server | Purpose | Usage |
|--------|---------|-------|
| **Filesystem** | Read/write local files | File operations |
| **GitHub** | GitHub API access | Repository queries |
| **Slack** | Slack workspace access | Team communication |

### Community

- **Web Search** — Real-time search capabilities
- **Database** — SQL database queries
- **Perplexity** — Web research and fact-checking
- **AWS** — Amazon Web Services integration
- **Docker** — Container management

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

## Learn More

- [MCP Official Documentation](https://modelcontextprotocol.io)
- [Anthropic MCP Guide](https://docs.anthropic.com)
- [Community MCP Servers](https://github.com/modelcontextprotocol)


# Claude Code Messenger Integrations — WhatsApp, Telegram, Slack, Discord

> **Last updated:** 25 March 2026

Claude Code can be connected to messaging platforms via **Channels**, **MCP servers**, and **webhooks**. This guide covers the major integrations.

---

## Table of Contents

- [Overview](#overview)
- [WhatsApp Integration](#whatsapp-integration)
- [Telegram Integration](#telegram-integration)
- [Slack Integration](#slack-integration)
- [Discord Integration](#discord-integration)
- [Remote Control Pattern](#remote-control-pattern)

---

## Overview

There are three main approaches to connecting Claude Code with messaging platforms:

| Approach | How It Works | Best For |
|----------|-------------|----------|
| **MCP Servers** | Claude Code calls messaging APIs via MCP tools | Sending/receiving messages from within coding sessions |
| **Channels/Webhooks** | External service triggers Claude Code sessions | Remote control, notifications, mobile workflow |
| **Bot Frameworks** | Custom bot using Claude API + messaging SDK | Full custom chatbot experiences |

---

## WhatsApp Integration

### Via WhatsApp MCP Server

The WhatsApp MCP server enables Claude Code to send and receive WhatsApp messages.

**Setup:**
```json
{
  "mcpServers": {
    "whatsapp": {
      "command": "npx",
      "args": ["-y", "whatsapp-mcp-server"],
      "env": {
        "WHATSAPP_API_TOKEN": "your-token",
        "WHATSAPP_PHONE_NUMBER_ID": "your-phone-id"
      }
    }
  }
}
```

**Capabilities:**
- Send text messages
- Send template messages
- Receive and process incoming messages
- Handle media (images, documents)

### Via WhatsApp Business API + Claude API

For production chatbots:

1. Set up WhatsApp Business API (via Meta Business Platform)
2. Create a webhook endpoint
3. Process incoming messages with Claude API
4. Send responses back via WhatsApp API

```python
# Simplified example
from anthropic import Anthropic
from flask import Flask, request

client = Anthropic()
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    message = request.json["entry"][0]["changes"][0]["value"]["messages"][0]
    user_text = message["text"]["body"]

    response = client.messages.create(
        model="claude-sonnet-4-6-20250217",
        max_tokens=1024,
        messages=[{"role": "user", "content": user_text}]
    )

    # Send response back via WhatsApp API
    send_whatsapp_message(message["from"], response.content[0].text)
    return "OK", 200
```

---

## Telegram Integration

### Via Telegram Bot + Claude API

Telegram bots are the most common integration pattern:

1. Create a bot via [@BotFather](https://t.me/BotFather)
2. Get your bot token
3. Set up a webhook or polling
4. Process messages with Claude API

```python
from telegram import Update
from telegram.ext import Application, MessageHandler, filters
from anthropic import Anthropic

client = Anthropic()

async def handle_message(update: Update, context):
    response = client.messages.create(
        model="claude-sonnet-4-6-20250217",
        max_tokens=1024,
        messages=[{"role": "user", "content": update.message.text}]
    )
    await update.message.reply_text(response.content[0].text)

app = Application.builder().token("YOUR_BOT_TOKEN").build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))
app.run_polling()
```

### Via MCP Server

```json
{
  "mcpServers": {
    "telegram": {
      "command": "npx",
      "args": ["-y", "telegram-mcp-server"],
      "env": {
        "TELEGRAM_BOT_TOKEN": "your-bot-token"
      }
    }
  }
}
```

---

## Slack Integration

### Via Slack MCP Server (Official)

Slack has an official MCP server for Claude:

```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-your-token",
        "SLACK_TEAM_ID": "T12345678"
      }
    }
  }
}
```

**Capabilities:**
- Read channel messages
- Post messages to channels
- Reply in threads
- Search messages
- List channels and users

### Via Claude for Slack (Native)

Anthropic offers a native **Claude for Slack** integration:
- Add Claude directly to your Slack workspace
- Mention `@Claude` in any channel or DM
- Supports threads, file analysis, and multi-turn conversations
- Available on Team and Enterprise plans

---

## Discord Integration

### Via Discord Bot + Claude API

```python
import discord
from anthropic import Anthropic

client = Anthropic()
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if bot.user.mentioned_in(message):
        response = client.messages.create(
            model="claude-sonnet-4-6-20250217",
            max_tokens=1024,
            messages=[{"role": "user", "content": message.content}]
        )
        await message.channel.send(response.content[0].text)

bot.run("YOUR_DISCORD_TOKEN")
```

### Via MCP Server

```json
{
  "mcpServers": {
    "discord": {
      "command": "npx",
      "args": ["-y", "discord-mcp-server"],
      "env": {
        "DISCORD_BOT_TOKEN": "your-bot-token"
      }
    }
  }
}
```

---

## Remote Control Pattern

A powerful pattern: control Claude Code from your phone via messaging apps.

### How It Works

1. Claude Code runs on your dev machine in a `/loop` (background agent loop)
2. A messaging bot (Telegram/Discord/Slack) bridges commands to Claude Code
3. You send commands from your phone
4. Claude Code executes and reports back

### Architecture

```
[Phone] → [Telegram Bot] → [Webhook Server] → [Claude Code --remote]
                                                      ↓
                                              [Git Push / PR]
                                                      ↓
                                              [Report back to Telegram]
```

### Use Cases

- Monitor CI/CD pipelines from your phone
- Trigger code reviews while commuting
- Get deployment status notifications
- Quick bug fixes from mobile
- Scheduled background tasks with `/loop`

---

## Sources

- [WhatsApp MCP Server](https://github.com/modelcontextprotocol/servers)
- [Slack MCP Server (official)](https://github.com/modelcontextprotocol/servers/tree/main/src/slack)
- [Claude for Slack](https://www.anthropic.com/claude-for-slack)
- [Claude Code /loop command](https://code.claude.com/docs/en/changelog)

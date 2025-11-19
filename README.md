# 🎯 Claude Prompt Engineering Guide

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/claude-prompt-engineering-guide?style=social)](https://github.com/yourusername/claude-prompt-engineering-guide)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-Nov%202025-blue)](https://github.com/yourusername/claude-prompt-engineering-guide)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 🚀 **The definitive guide to writing professional Claude Standard prompts for Opus, Sonnet, and Haiku models** with comprehensive coverage of MCP, Skills, Superpowers, and advanced prompt engineering techniques.

---

## 📖 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Quick Start](#quick-start)
- [Core Content](#core-content)
- [Documentation Structure](#documentation-structure)
- [Key Sections](#key-sections)
- [Examples & Templates](#examples--templates)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## 🌟 Overview

This comprehensive guide synthesizes **Anthropic's official best practices** with **real-world prompt engineering techniques** for Claude 4.x models. Whether you're using Claude through the web interface, desktop app, Claude Code CLI, or the API, this guide provides proven patterns and frameworks for extracting maximum value from Claude's capabilities.

### Who Is This For?

- **Developers** building applications with Claude's API
- **Prompt Engineers** designing production prompts for teams
- **AI Engineers** integrating Claude into workflows
- **Claude Code Users** leveraging agentic capabilities
- **Researchers** exploring Claude's reasoning abilities
- **Anyone** wanting to master professional prompt engineering

### Why This Matters

Claude 4.x models are extraordinarily capable, but extracting that capability requires **structured prompting**. This guide provides:

✅ **Anthropic's 10-Component Framework** — The official structure for professional prompts  
✅ **Claude 4.x Best Practices** — Specific techniques for Opus, Sonnet, and Haiku models  
✅ **Advanced Techniques** — XML tagging, chain of thought, extended thinking, and more  
✅ **Real-World Patterns** — Code review, business analysis, research, document creation  
✅ **Tool Integration** — MCP, Skills, Superpowers, and Perplexity integration  
✅ **Environment Guides** — Optimal approaches for Claude.ai, Desktop, Code, and API  

---

## ✨ Features

This guide includes:

- 📚 **1000+ lines of comprehensive reference material**
- 🏗️ **Official 10-component prompt framework** with detailed explanation
- 💡 **5 advanced prompt patterns** with complete examples
- 🛠️ **Tool integration guides** (MCP, Skills, Superpowers)
- 🎯 **Environment-specific optimizations** (web, desktop, CLI, API)
- 📋 **Prompt templates** (minimal and comprehensive)
- 🔍 **Real-world use cases** across multiple domains
- ⚙️ **Model comparison chart** (Opus vs Sonnet vs Haiku)
- 📊 **Pricing and performance guide**
- 🚀 **Best practices for long-horizon reasoning**
- 🧠 **Chain of thought and extended thinking techniques**
- 🔐 **Security and prompt injection prevention**

---

## 🚀 Quick Start

### 1. Read the Main Guide

Start with the comprehensive **[Claude Prompt Engineering Guide](./Claude-Prompt-Guide.md)** which covers:
- Claude's architecture and philosophy
- The 10-component framework
- Best practices for Claude 4.x
- Advanced techniques
- Complete pattern examples

### 2. Choose Your Environment

- **Using Claude.ai?** → Read [Claude.ai Optimization Guide](./docs/quick-start.md)
- **Using Claude Desktop?** → Read [MCP Integration Guide](./docs/mcp-integration.md)
- **Using Claude Code CLI?** → Read [Claude Code Guide](./docs/claude-code-guide.md)
- **Building with API?** → Read [API Integration Guide](./docs/api-guide.md)

### 3. Find Examples for Your Use Case

- [Coding Tasks](./docs/examples/coding-tasks.md)
- [Research & Analysis](./docs/examples/research-tasks.md)
- [Business Analysis](./docs/examples/business-analysis.md)
- [Document Creation](./docs/examples/document-creation.md)

### 4. Use a Template

Customize one of our prompt templates:
- [Minimal Prompt Template](./templates/minimal-prompt-template.md) — Quick projects
- [Comprehensive Prompt Template](./templates/comprehensive-prompt-template.md) — Complex tasks

---

## 📚 Core Content

### [Claude Prompt Engineering Guide](./Claude-Prompt-Guide.md)

The comprehensive reference document containing:

#### Section 1: Understanding Claude's Architecture
- Claude's character and philosophy
- Knowledge cutoff dates
- How Claude processes prompts

#### Section 2: Claude Models Overview
- **Claude Opus 4.1** — Most powerful model
- **Claude Sonnet 4.5** — Balanced performance and cost
- **Claude Haiku 4.5** — Fast and efficient
- Pricing and performance comparison

#### Section 3: System Prompts vs User Prompts
- When to use system prompts
- When to use user prompts
- Best practices for each

#### Section 4: Anthropic's Official Prompt Structure
- **The 10-Component Framework** (official structure)
- Component explanations and examples
- Why this structure works

#### Section 5: Claude 4.x Best Practices
- Be explicit with instructions
- Add context to improve performance
- Long-horizon reasoning techniques
- State tracking best practices
- Tool usage patterns
- Output formatting control
- Parallel tool calling
- Research approaches
- Avoiding hallucinations

#### Section 6: Advanced Techniques
- XML tags for structure
- Chain of thought prompting
- Extended thinking
- Prompt chaining
- Role prompting

#### Section 7: Tools, MCP, Skills & Superpowers
- Model Context Protocol (MCP)
- MCP Filesystem Server
- Claude Skills system
- Superpowers plugin by obra
- Perplexity MCP integration

#### Section 8: Prompt Engineering for Different Environments
- Claude.ai web interface
- Claude Desktop app
- Claude Code (CLI/VS Code)
- Claude API (direct integration)

#### Section 9: Common Patterns & Examples
- Pattern 1: Technical Code Review
- Pattern 2: Business Analysis with Data
- Pattern 3: Long-Horizon Coding Tasks
- Pattern 4: Research and Synthesis
- Pattern 5: Document Creation with Skills

#### Section 10: Quick Reference Card
- Minimal prompt template
- Comprehensive prompt template
- Quick checks checklist

---

## 📖 Documentation Structure

```
claude-prompt-engineering-guide/
├── README.md                          # This file
├── Claude-Prompt-Guide.md             # Main comprehensive guide
├── LICENSE                            # MIT License
├── CONTRIBUTING.md                    # Contribution guidelines
├── CHANGELOG.md                       # Version history
├── .gitignore                         # Git ignore rules
│
├── docs/                              # Additional documentation
│   ├── quick-start.md                # Getting started guide
│   ├── mcp-integration.md            # MCP setup and usage
│   ├── skills-guide.md               # Skills documentation
│   ├── superpowers-guide.md          # Superpowers plugin guide
│   ├── api-guide.md                  # API integration guide
│   ├── claude-code-guide.md          # Claude Code CLI guide
│   └── examples/                      # Real-world examples
│       ├── coding-tasks.md
│       ├── research-tasks.md
│       ├── business-analysis.md
│       └── document-creation.md
│
├── templates/                         # Ready-to-use templates
│   ├── minimal-prompt-template.md    # Quick template
│   └── comprehensive-prompt-template.md # Full template
│
└── .github/                          # GitHub configuration
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.md
    │   └── feature_request.md
    └── PULL_REQUEST_TEMPLATE.md
```

---

## 🎯 Key Sections

### The 10-Component Framework (Official)

This is **Anthropic's recommended structure** for professional prompts:

1. **Task Context** — WHO and WHAT (define Claude's role)
2. **Tone Context** — HOW (communication style)
3. **Background Data** — Relevant context and documents
4. **Detailed Task Description** — Explicit requirements and rules
5. **Examples** — 1-3 examples of desired output
6. **Conversation History** — Relevant prior context
7. **Immediate Task Description** — Specific deliverable needed NOW
8. **Thinking Step-by-Step** — Encourage deliberate reasoning
9. **Output Formatting** — Define structure explicitly
10. **Prefilled Response** — Start Claude's response to guide style

### Best Practices for Claude 4.x

📌 **Be Explicit** — Claude 4.x responds to precise instructions  
📌 **Add Context** — Explain WHY, not just WHAT  
📌 **Use Examples** — Show, don't just tell  
📌 **Encourage Reasoning** — Chain of thought dramatically improves quality  
📌 **Define Output Format** — Be specific about structure and style  
📌 **Leverage Parallel Tools** — Execute multiple operations simultaneously  

---

## 📋 Examples & Templates

### Real-World Patterns

1. **Technical Code Review** — Review code for security, performance, and best practices
2. **Business Analysis** — Analyze metrics and provide strategic recommendations
3. **Long-Horizon Coding** — Build complete features across multiple context windows
4. **Research & Synthesis** — Conduct comprehensive competitive analysis
5. **Document Creation** — Build presentations with Skills integration

### Ready-to-Use Templates

- **Minimal Template** — Essential components for quick tasks
- **Comprehensive Template** — Full framework for complex projects

See the [templates/](./templates/) directory for complete examples.

---

## 🤝 Contributing

We welcome contributions! Whether you're:
- 📝 Adding new examples or patterns
- 🐛 Reporting issues or suggesting improvements
- 📚 Improving documentation
- 🎯 Sharing your own prompt engineering discoveries

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidelines.

---

## 📜 License

This project is licensed under the **MIT License** — see [LICENSE](./LICENSE) for details.

The Claude Prompt Engineering Guide synthesizes publicly available information from Anthropic documentation and open-source community resources.

---

## 🙏 Acknowledgments

**Created:** November 19, 2025  
**Location:** Singapore  
**Purpose:** Deep research synthesis for professional Claude prompt engineering

### Credits

- **Anthropic** for Claude and comprehensive documentation
- **Anthropic team** for the 10-component framework and best practices
- **Open source community** for MCP, Skills, and Superpowers ecosystem
- **Claude users and developers** for real-world pattern discovery

---

## 📞 Support & Questions

### Need Help?

- 📖 **Read the Guide** — Start with [Claude-Prompt-Guide.md](./Claude-Prompt-Guide.md)
- 📚 **Explore Examples** — Check [docs/examples/](./docs/examples/)
- 🎯 **Use Templates** — Customize a [template](./templates/)

### Report Issues

Found a bug or have a suggestion? [Open an issue](https://github.com/yourusername/claude-prompt-engineering-guide/issues) with:
- Clear description of the problem
- Example (if applicable)
- Suggested improvement (optional)

### Contribute

Want to improve this guide? [See CONTRIBUTING.md](./CONTRIBUTING.md) for the process.

---

## 🚀 Getting Started

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/claude-prompt-engineering-guide.git
   cd claude-prompt-engineering-guide
   ```

2. **Start with the main guide**
   ```bash
   # Read the comprehensive guide
   cat Claude-Prompt-Guide.md
   ```

3. **Choose your path**
   - New to Claude? → Start with [Quick Start Guide](./docs/quick-start.md)
   - Building an app? → Read [API Guide](./docs/api-guide.md)
   - Want patterns? → Browse [Examples](./docs/examples/)

4. **Pick a template**
   - Quick project? → [Minimal Template](./templates/minimal-prompt-template.md)
   - Complex task? → [Comprehensive Template](./templates/comprehensive-prompt-template.md)

---

## 📊 Stats

- **Pages:** 1000+ lines of comprehensive reference
- **Patterns:** 5 real-world prompt examples
- **Templates:** 2 production-ready templates
- **Examples:** 15+ use cases across different domains
- **Coverage:** Claude Opus, Sonnet, Haiku, API, Desktop, CLI, Web

---

## 🌐 Related Resources

### Official Anthropic

- [Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Claude API Documentation](https://docs.anthropic.com)
- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [System Prompts Guide](https://docs.anthropic.com/en/release-notes/system-prompts)

### Community

- [Model Context Protocol](https://modelcontextprotocol.io)
- [Claude Cookbooks](https://github.com/anthropics/claude-cookbooks)
- [Awesome Claude Skills](https://github.com/travisvn/awesome-claude-skills)
- [Superpowers Plugin](https://github.com/obra/superpowers-chrome)

---

<div align="center">

**Made with ❤️ for the Claude community**

[⭐ Star this repository](https://github.com/yourusername/claude-prompt-engineering-guide) if you found it helpful!

[Report Issues](https://github.com/yourusername/claude-prompt-engineering-guide/issues) • [Contribute](./CONTRIBUTING.md) • [Discuss](https://github.com/yourusername/claude-prompt-engineering-guide/discussions)

</div>

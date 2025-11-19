# Claude Professional Prompt Engineering Guide
## Comprehensive Reference for Claude Code Opus & Sonnet 4.5 with Superpowers, Skills, MCP & Perplexity Integration

**Created: November 19, 2025**  
**Location: Singapore**  
**Purpose: Deep research synthesis for professional Claude prompt engineering**

---

## Table of Contents
0. ["Ask Claude" Protocol - How to Use This Guide](#ask-claude-protocol---how-to-use-this-guide)
1. [Understanding Claude's Architecture](#understanding-claudes-architecture)
2. [Claude Models Overview](#claude-models-overview)
3. [System Prompts vs User Prompts](#system-prompts-vs-user-prompts)
4. [Anthropic's Official Prompt Structure](#anthropics-official-prompt-structure)
5. [Claude 4.x Best Practices](#claude-4x-best-practices)
6. [Advanced Techniques](#advanced-techniques)
7. [Tools, MCP, Skills & Superpowers](#tools-mcp-skills--superpowers)
8. [Prompt Engineering for Different Environments](#prompt-engineering-for-different-environments)
9. [Common Patterns & Examples](#common-patterns--examples)
10. [Memory Bank Reference](#memory-bank-reference)

---

## Understanding Claude's Architecture

### Claude's Character and Philosophy
Claude was developed with **character training** - not just safety, but rich traits like curiosity, honesty, thoughtfulness, open-mindedness, and intellectual humility. Claude doesn't pretend to be objective or have no opinions. Instead, it's trained to be honest about its leanings while remaining curious and open to other perspectives.

### Knowledge Cutoff
- **Claude 4.x models**: January 2025
- **Claude Sonnet 3.7**: October 2024

---

## Claude Models Overview

### Current Model Family (as of Nov 2025)

#### Claude Opus 4.1 / Claude Opus 4
- **Purpose**: Most powerful model for complex challenges
- **Best for**: Long-horizon reasoning, complex analysis, legal/financial work
- **API String**: `claude-opus-4-20250514`
- **Pricing**: 15/MTok (input), 75/MTok (output)

#### Claude Sonnet 4.5 / Claude Sonnet 4
- **Purpose**: Smart, efficient model for everyday use
- **Best for**: Balanced performance and cost, coding, research
- **API String**: `claude-sonnet-4-5-20250929` or `claude-sonnet-4-20250514`
- **Pricing**: 3/MTok (input), 15/MTok (output)
- **Special Features**: Exceptional state tracking, context awareness, parallel tool execution

#### Claude Haiku 4.5
- **Purpose**: Fastest model for daily tasks
- **Best for**: Simple queries, high-volume operations
- **Pricing**: 1/MTok (input), 5/MTok (output)

---

## System Prompts vs User Prompts

### System Prompt (via API `system` parameter)
**Purpose**: Set Claude's **role** and foundational behavior

**Best Practice**: Use ONLY for defining Claude's role/identity. Keep focused and concise.

**Example**:
```
You are a senior software architect with 15 years of experience in distributed systems. 
You specialize in microservices architecture and cloud-native applications.
```

### User Prompt (via API `messages` with role: user)
**Purpose**: Provide **task, context, data, and instructions**

**Best Practice**: Put ALL task-specific instructions here. Include background data, examples, and constraints.

---

## Anthropic's Official Prompt Structure

### The 10-Component Framework

#### 1. **Task Context (WHO & WHAT)**
Define Claude's role and overall task

#### 2. **Tone Context (HOW)**
Specify desired communication style

#### 3. **Background Data/Documents**
Provide all relevant context

#### 4. **Detailed Task Description & Rules**
Be explicit about boundaries and requirements

#### 5. **Examples (Multishot Prompting)**
Show 1-3 examples of desired output

#### 6. **Conversation History**
Include relevant prior context

#### 7. **Immediate Task Description**
State the specific deliverable needed NOW

#### 8. **Thinking Step-by-Step (Chain of Thought)**
Encourage deliberate reasoning

#### 9. **Output Formatting**
Define the structure explicitly

#### 10. **Prefilled Response (Advanced)**
Start Claude's response to guide style

### Why This Works
- **Hierarchical Processing**: Claude processes prompts in layers
- **Constitutional AI Training**: Enhanced ability to follow detailed instructions
- **200K+ Token Context**: Can utilize ALL background information
- **Attention Mechanisms**: Fine-tuned to identify relationships between components

---

## Claude 4.x Best Practices

### Core Principles

#### 1. **Be Explicit with Instructions**
Claude 4.x responds to PRECISE instructions.

**Less Effective**: `Create an analytics dashboard`

**More Effective**: `Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation.`

#### 2. **Add Context to Improve Performance**
Explain WHY behavior matters:

**Less Effective**: `NEVER use ellipses`

**More Effective**: `Your response will be read aloud by a text-to-speech engine, so never use ellipses since the text-to-speech engine will not know how to pronounce them.`

#### 3. **Long-Horizon Reasoning**
Claude 4.5 excels at extended tasks with exceptional state tracking.

**Multi-Window Workflow Guidance**:
```
<multi_window_guidance>
Your context window will be automatically compacted as it approaches its limit.
Do not stop tasks early due to token budget concerns.
Save your current progress to memory as you approach your token budget limit.
Always be persistent and complete tasks fully.
</multi_window_guidance>
```

#### 4. **State Tracking Best Practices**

**Use Structured Formats for Data**:
```json
{
  "tests": [
    {"id": 1, "name": "authentication_flow", "status": "passing"},
    {"id": 2, "name": "user_management", "status": "failing"}
  ],
  "total": 200,
  "passing": 150,
  "failing": 25
}
```

**Use Git for State Tracking**: Claude 4.5 excels at using git to track state across sessions.

#### 5. **Tool Usage Patterns**

**Make Claude Proactive**:
```xml
<default_to_action>
By default, implement changes rather than only suggesting them.
If the user's intent is unclear, infer the most useful likely action.
Try to infer the user's intent about whether a tool call is intended.
</default_to_action>
```

**Make Claude Conservative**:
```xml
<do_not_act_before_instructions>
Do not jump into implementation unless clearly instructed.
When intent is ambiguous, default to providing information and recommendations.
Only proceed with edits when explicitly requested.
</do_not_act_before_instructions>
```

#### 6. **Control Output Formatting**

**Minimize Markdown and Bullet Points**:
```xml
<avoid_excessive_markdown>
When writing long-form content, write in clear, flowing prose using complete paragraphs.
Reserve markdown for inline code, code blocks, and simple headings.
DO NOT use lists unless presenting discrete items or explicitly requested.
Incorporate information naturally into sentences instead of bullet points.
</avoid_excessive_markdown>
```

#### 7. **Parallel Tool Calling**
Claude 4.x excels at executing multiple operations simultaneously.

```xml
<use_parallel_tool_calls>
If you intend to call multiple tools with no dependencies, make all independent calls in parallel.
For example, when reading 3 files, run 3 tool calls in parallel.
Maximize parallel tool calls for speed and efficiency.
Never use placeholders or guess missing parameters.
</use_parallel_tool_calls>
```

#### 8. **Research and Information Gathering**

```xml
<research_approach>
Search for information in a structured way.
Develop several competing hypotheses as you gather data.
Track confidence levels in your progress notes.
Regularly self-critique your approach and plan.
Break down complex research systematically.
</research_approach>
```

#### 9. **Minimize Hallucinations in Coding**

```xml
<investigate_before_answering>
Never speculate about code you have not opened.
If the user references a specific file, you MUST read it before answering.
Investigate and read relevant files BEFORE answering questions.
Give grounded and hallucination-free answers.
</investigate_before_answering>
```

---

## Advanced Techniques

### 1. **XML Tags for Structure**
Use XML tags to create clear boundaries:

```xml
<task>
  <objective>Create a financial analysis report</objective>
  <constraints>
    <length>500-750 words</length>
    <format>Prose paragraphs only</format>
    <tone>Professional but accessible</tone>
  </constraints>
</task>

<background_data>
  <q2_metrics>
    <revenue>15.2M</revenue>
    <growth_yoy>22%</growth_yoy>
  </q2_metrics>
</background_data>
```

### 2. **Chain of Thought (CoT) Prompting**
Improves response quality up to 39%:

```xml
<thinking>
Before providing your answer, work through this step-by-step:
1. What are the key components of this problem?
2. What assumptions am I making?
3. What are the potential solutions?
4. What are the trade-offs?

Show your reasoning in <reasoning> tags, then provide your final answer.
</thinking>
```

### 3. **Extended Thinking (Claude 4.x)**
Built-in capability for complex reasoning:

```
After receiving tool results, carefully reflect on their quality and determine optimal 
next steps before proceeding. Use your thinking to plan and iterate based on this new 
information, then take the best next action.
```

### 4. **Prompt Chaining**
Break complex tasks into sequential steps:

```
Step 1: Analyze the data and identify key trends
Step 2: Verify your analysis is accurate
Step 3: Generate insights based on verified trends
Step 4: Write the final report incorporating insights
```

### 5. **Role Prompting**
Most powerful system prompt technique:

**Advanced Role Example**:
```
You are a CFO of a high-growth B2B SaaS company in a board meeting discussing Q2 financials.
Investors want aggressive growth but are wary of burn rate.
You speak with authority, provide specific recommendations, and don't shy away from hard truths.
```

---

## Tools, MCP, Skills & Superpowers

### Model Context Protocol (MCP)

**What is MCP?**
MCP is Anthropic's standardized protocol that allows Claude to interact with external tools, data sources, and services.

#### MCP Connector Feature (API)
- **Purpose**: Connect to remote MCP servers directly from the Messages API
- **Requires**: Beta header `anthropic-beta: mcp-client-2025-04-04`
- **Supports**: Tool calling, OAuth authentication, multiple servers

**Example MCP Server Configuration**:
```json
{
  "mcpServers": [
    {
      "type": "url",
      "url": "https://mcp.example.com/sse",
      "name": "example-mcp",
      "authorizationToken": "YOUR_TOKEN",
      "toolConfiguration": {
        "enabled": true,
        "allowedTools": ["tool1", "tool2"]
      }
    }
  ]
}
```

#### MCP Filesystem Server (Claude Desktop)
Gives Claude access to your local filesystem:

**Configuration** (`claude_desktop_config.json`):
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

**Key Features**:
- Read files, write content, create directories
- Search files, get file info, directory trees
- All operations happen locally (not uploaded to remote servers)
- Works via Stdio transport layer

### Claude Skills

**What are Skills?**
Skills are modular, reusable task packages that teach Claude how to execute repeatable workflows.

#### How Skills Work
1. **Metadata loading** (~100 tokens): Claude scans available Skills
2. **Full instructions** (<5k tokens): Load when Claude determines relevance
3. **Bundled resources**: Files and executable code load only as needed

#### Progressive Disclosure Architecture
Skills use efficient loading to avoid overwhelming context:
- **Model-invoked activation**: Claude autonomously decides when to load a Skill
- **Cross-platform portability**: Same Skill works across Claude.ai, Claude Code, and API
- **Composable**: Multiple Skills can stack together automatically

#### Skill Structure
Every Skill contains:
- **SKILL.md**: Instructions, constraints, examples, templates
- **Metadata/YAML**: Name, description, version, triggers, permissions
- **Supporting assets**: Templates, sample datasets, brand assets, policy documents
- **Optional scripts**: Python or other executable code for complex operations

#### Official Skills (Anthropic-provided)
- **Document Skills**: PowerPoint (.pptx), Excel (.xlsx), Word (.docx), PDF manipulation
- Available to all users on claude.ai and via API

#### Custom Skills
- **Pro/Max/Team/Enterprise**: Can create and upload custom Skills
- **Use Cases**: Company brand guidelines, data analysis workflows, compliance checks

#### Skills API
```python
import anthropic

client = anthropic.Client(api_key="your-api-key")

# Skills are accessible via the /v1/skills API endpoint
# Specify containers with list of skills, each with:
# - type
# - skill identifier  
# - optional configuration
```

### Superpowers Plugin (by obra)

**What is Superpowers?**
A comprehensive plugin for Claude Code that wraps up advanced capabilities and tricks.

**Installation**:
```bash
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

#### Superpowers Chrome
- **Direct browser control** via Chrome DevTools Protocol
- **Two modes**:
  - Skill Mode: CLI tool for Claude Code agents (browsing skill)
  - MCP Mode: Ultra-lightweight MCP server for any MCP client

**Features**:
- Zero dependencies (built-in WebSocket)
- Idiotproof API: Tab index syntax (0, 1, 2) instead of WebSocket URLs
- Platform-agnostic: Works on macOS, Linux, Windows
- 17 commands covering all browser automation needs

**Quick Start**:
```bash
cd ~/.claude/plugins/cache/superpowers-chrome/skills/browsing
./chrome-ws start  # Launch Chrome
./chrome-ws new "https://example.com"
./chrome-ws navigate 0 "https://google.com"
./chrome-ws fill 0 "textarea[name=q]" "test"
./chrome-ws click 0 "button[name=btnK]"
```

### Perplexity MCP Integration

While not officially documented, Perplexity can be integrated as an MCP server to provide:
- Real-time web search capabilities
- Current information beyond Claude's knowledge cutoff
- Research and fact-checking augmentation

**Conceptual Integration Pattern**:
```json
{
  "mcpServers": {
    "perplexity": {
      "command": "node",
      "args": ["./perplexity-mcp-server.js"],
      "env": {
        "PERPLEXITY_API_KEY": "your_key_here"
      }
    }
  }
}
```

---

## Prompt Engineering for Different Environments

### Claude.ai Web Interface
- **System Prompt**: Set in Settings → Capabilities
- **Skills**: Enable in Settings → Capabilities
- **Best for**: Interactive conversations, document creation, research

### Claude Desktop App
- **MCP Support**: Full support for local MCP servers (filesystem, custom servers)
- **Skills Support**: Full support for Skills
- **Configuration**: `claude_desktop_config.json` in:
  - macOS: `~/Library/Application Support/Claude/`
  - Windows: `%APPDATA%\Claude\`
- **Best for**: File manipulation, local development work, persistent workflows

### Claude Code (CLI/VS Code)
- **Purpose**: Agentic coding tool for terminal/IDE
- **MCP Support**: Full support via `--mcp-config` flag or config file
- **Skills Support**: Install via plugin marketplace
- **Agents**: Can create specialized sub-agents
- **Best for**: Software development, complex coding tasks, automation

**Example Usage**:
```bash
# Direct prompt
claude -p "Implement user authentication system"

# With custom system prompt
claude --system-prompt "You are a security-focused backend engineer" -p "Review this auth code"

# With MCP config
claude --mcp-config ./mcp-config.json -p "Search through the codebase"

# Enable skills
/plugin marketplace add anthropics/skills
```

### Claude API (Direct Integration)
- **Full Control**: Complete customization of system prompts, tools, MCP servers
- **Skills API**: Programmatic management via `/v1/skills` endpoint
- **Best for**: Production applications, automated workflows, custom integrations

**Example API Call**:
```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=2048,
    system="You are a senior software architect specializing in distributed systems.",
    messages=[
        {
            "role": "user",
            "content": "Design a scalable microservices architecture for an e-commerce platform."
        }
    ]
)
```

---

## Common Patterns & Examples

### Pattern 1: Technical Code Review

```xml
<system_prompt>
You are a principal software engineer with 20 years of experience.
You specialize in security, performance optimization, and code quality.
</system_prompt>

<task>
Review the following code for security vulnerabilities, performance issues, and best practices violations.
</task>

<rules>
- Identify specific line numbers for each issue
- Categorize issues as: CRITICAL, HIGH, MEDIUM, LOW
- Provide concrete fix recommendations
- Do NOT rewrite entire files; suggest targeted changes
</rules>

<code>
[PASTE CODE HERE]
</code>

<thinking>
Before responding, analyze:
1. What security vulnerabilities exist?
2. What performance bottlenecks are present?
3. What best practices are violated?
4. What is the severity of each issue?
</thinking>

<format>
Structure your response as:
1. Executive Summary (2-3 sentences)
2. Critical Issues (with fixes)
3. High Priority Issues (with fixes)
4. Medium/Low Priority Issues
5. Overall Assessment
</format>
```

### Pattern 2: Business Analysis with Data

```xml
<system_prompt>
You are a CFO of a high-growth B2B SaaS company.
You're in a board meeting discussing Q2 financials.
Investors want aggressive growth but are wary of burn rate.
</system_prompt>

<background_data>
<q2_metrics>
- Revenue: $15.2M (22% YoY growth)
- Enterprise segment: +30% growth
- SMB segment: -5% decline
- Gross Margin: 72% (up 3% from Q1)
- EBITDA Margin: 18% (down 2% due to R&D)
- Operating Cash Flow: $4.1M
- Cash Reserves: $28M (15-month runway)
- CAC: Up 20% vs Q1
</q2_metrics>
</background_data>

<task>
Analyze Q2 financials and provide strategic recommendations for Q3.
</task>

<rules>
- Cite specific metrics to support each point
- Identify both opportunities and risks
- Provide 3-5 concrete action items
- Write in flowing prose (no bullet points in main analysis)
- Be direct and don't shy away from hard truths
</rules>

<thinking>
Consider:
1. What trends are most significant?
2. Where should we focus resources?
3. What risks need immediate attention?
4. How do we balance growth and burn rate?
</thinking>
```

### Pattern 3: Long-Horizon Coding Task

```xml
<system_prompt>
You are a senior full-stack engineer specializing in React and Node.js.
</system_prompt>

<multi_window_guidance>
This is a complex task that may span multiple context windows.

Your context will be automatically compacted as it approaches the limit.
Do not stop work early due to token budget concerns.

As you approach your context limit:
1. Save progress to progress.txt
2. Update tests.json with test status
3. Commit your work to git with descriptive messages
4. Update TODO.md with remaining tasks

When starting a fresh context window:
1. Run `pwd` to confirm your working directory
2. Review progress.txt, tests.json, and git logs
3. Run through fundamental integration tests
4. Continue with the next priority task
</multi_window_guidance>

<state_tracking>
Use structured formats:
- tests.json for test results
- progress.txt for freeform progress notes
- Git for code state and checkpoints
- TODO.md for remaining work

Emphasize incremental progress - complete one component fully before moving to the next.
</state_tracking>

<task>
Build a complete user authentication system with:
1. User registration and login (email/password)
2. JWT token generation and validation
3. Password reset functionality
4. Email verification
5. Protected route middleware
6. Frontend login/signup forms with validation
7. Comprehensive test coverage
</task>

<quality_requirements>
- Write tests BEFORE implementing features (TDD approach)
- All code must be production-ready (no TODOs or placeholders)
- Follow security best practices for auth
- Include proper error handling
- Add logging for debugging
</quality_requirements>

<thinking>
Plan your approach:
1. What components need to be built?
2. What's the logical implementation order?
3. What tests are needed for each component?
4. What are the critical security considerations?
</thinking>
```

### Pattern 4: Research and Synthesis

```xml
<system_prompt>
You are a senior research analyst with expertise in market research and competitive analysis.
</system_prompt>

<research_approach>
Search for information in a structured way.

As you gather data:
1. Develop several competing hypotheses
2. Track confidence levels for each finding
3. Identify gaps in your research
4. Cross-reference multiple sources
5. Note contradictions or inconsistencies

Regularly self-critique your approach and adjust your search strategy.

Update a research_notes.md file to persist information and provide transparency.
</research_approach>

<task>
Conduct comprehensive competitive analysis of the project management software market.

Focus on:
1. Market leaders and their key differentiators
2. Pricing strategies across competitors
3. Feature comparison (Gantt charts, time tracking, collaboration tools)
4. Target customer segments
5. Recent product updates and strategic moves
6. Market trends and future predictions
</task>

<sources>
Research from:
- Company websites and product pages
- Recent product announcements
- Industry analyst reports
- User reviews on G2, Capterra, TrustRadius
- Tech news coverage
- Social media discussions
</sources>

<deliverable>
Create a structured competitive analysis report:
1. Executive Summary (key findings and recommendations)
2. Market Overview (size, growth, trends)
3. Competitor Profiles (for each major player)
4. Feature Comparison Matrix
5. Pricing Analysis
6. Strategic Insights and Recommendations
</deliverable>

<format>
Write in clear, professional prose.
Use tables for feature/pricing comparisons.
Cite sources throughout your analysis.
</format>
```

### Pattern 5: Document Creation with Skills

```xml
<system_prompt>
You are an expert presentation designer with 10 years of experience creating executive-level decks.
</system_prompt>

<skill_instructions>
You have access to the PowerPoint Skill for creating professional presentations.
Use this skill to create a visually polished, data-driven presentation.
</skill_instructions>

<task>
Create a Q2 business review presentation for the executive team.
</task>

<content_requirements>
Slides to include:
1. Title slide with Q2 theme
2. Executive summary (key highlights)
3. Financial performance (revenue, margins, cash flow)
4. Growth metrics (customer acquisition, retention, expansion)
5. Product updates and milestones
6. Challenges and risks
7. Q3 priorities and roadmap
8. Closing slide with call to action
</content_requirements>

<design_requirements>
- Use corporate brand colors (provided in brand_guidelines.md)
- Professional, clean layout
- Data visualizations for all metrics (charts, graphs)
- Consistent typography and spacing
- Executive-appropriate tone (confident, data-driven, strategic)
</design_requirements>

<data>
[Include all Q2 data, metrics, and relevant information here]
</data>

<thinking>
Before creating the deck:
1. What's the narrative arc of the presentation?
2. Which metrics are most impactful to highlight?
3. What visual style best conveys our success while acknowledging challenges?
4. How can data visualizations make complex information accessible?
</thinking>
```

---

## Memory Bank Reference

### Purpose of This Document

This guide serves as a **persistent memory reference** for AI systems (including future AI assistants) to understand:

1. **Claude's Architecture**: How Claude thinks, processes, and responds
2. **Official Best Practices**: Anthropic's recommended prompt engineering techniques
3. **Model Capabilities**: What each Claude model excels at
4. **Tool Integration**: How to leverage MCP, Skills, and Superpowers
5. **Environment-Specific Patterns**: Optimal approaches for different Claude interfaces

### Key Takeaways for Writing Claude Prompts

#### Essential Principles
1. **Be Explicit and Detailed**: Claude 4.x responds to precise instructions
2. **Structure with XML**: Use tags to create clear boundaries
3. **Provide Context**: Explain WHY, not just WHAT
4. **Use Examples**: Show don't just tell
5. **Encourage Reasoning**: Chain of thought dramatically improves quality
6. **Define Output Format**: Be specific about structure and style

#### System Prompt Strategy
- **System Prompt** = **Role Definition Only**
- **User Prompt** = **Task + Context + Instructions + Data + Examples**

#### For Complex Tasks
- Use multi-window guidance for long-horizon work
- Implement structured state tracking (JSON + Git + progress files)
- Break tasks into incremental steps
- Leverage parallel tool calling for efficiency

#### For High-Quality Output
- Minimize hallucinations by requiring investigation before answers
- Control formatting explicitly (prose vs lists)
- Use role prompting for domain expertise
- Include thinking/reasoning steps

### When to Use This Guide

**Before Writing a Prompt**:
- Review the 10-Component Framework
- Check Claude 4.x Best Practices for your use case
- Select appropriate patterns from examples

**When Debugging Poor Outputs**:
- Verify you're being explicit enough
- Check if you provided sufficient context
- Ensure examples demonstrate exactly what you want
- Confirm output formatting instructions are clear

**When Integrating Tools**:
- Reference MCP, Skills, and Superpowers sections
- Follow environment-specific configuration patterns
- Implement proper tool usage instructions

---

## Quick Reference Card

### Prompt Template (Minimal)
```xml
<system_prompt>
[WHO is Claude? Define role clearly]
</system_prompt>

<task>
[WHAT needs to be done?]
</task>

<rules>
[CONSTRAINTS and requirements]
</rules>

<background>
[CONTEXT and data]
</background>

<thinking>
[ENCOURAGE reasoning before answering]
</thinking>

<format>
[HOW should output be structured?]
</format>
```

### Prompt Template (Comprehensive)
```xml
<system_prompt>
You are [ROLE with specific expertise].
[Additional role context and persona details]
</system_prompt>

<tone>
[Communication style, formality level, perspective]
</tone>

<background>
[All relevant context, data, documents, prior conversation]
</background>

<task>
<objective>[Clear statement of what needs to be accomplished]</objective>
<constraints>
- [Specific requirements]
- [Limitations and boundaries]
- [Format specifications]
</constraints>
</task>

<rules>
- [Explicit instructions on what TO do]
- [Explicit instructions on what NOT to do]
- [Quality criteria]
- [Edge case handling]
</rules>

<examples>
<good_example>
[Concrete example of desired output]
</good_example>
<bad_example>
[Example of what to avoid]
</bad_example>
</examples>

<thinking>
Before responding, consider:
1. [Key question or analysis step]
2. [Another analysis step]
3. [Final consideration]

[Instruction to show reasoning if helpful]
</thinking>

<format>
[Detailed output structure]
[Specific formatting requirements]
[Use of XML tags for response sections]
</format>
```

### Quick Checks
✅ **Is Claude's role clearly defined?**  
✅ **Are instructions explicit and detailed?**  
✅ **Is there sufficient context and background?**  
✅ **Are examples provided?**  
✅ **Are constraints and rules clear?**  
✅ **Is thinking/reasoning encouraged?**  
✅ **Is output format specified?**  
✅ **Have I explained WHY for important requirements?**

---

## Additional Resources

### Official Anthropic Documentation
- **Prompt Engineering Guide**: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
- **API Reference**: https://docs.anthropic.com
- **Claude Code Documentation**: https://docs.anthropic.com/en/docs/claude-code
- **System Prompts**: https://docs.anthropic.com/en/release-notes/system-prompts

### GitHub Resources
- **Anthropic Prompt Engineering Tutorial**: https://github.com/anthropics/prompt-eng-interactive-tutorial
- **Claude Cookbooks**: https://github.com/anthropics/claude-cookbooks
- **Claude Quickstarts**: https://github.com/anthropics/claude-quickstarts
- **Skills Repository**: https://github.com/anthropics/skills
- **Superpowers Plugin**: https://github.com/obra/superpowers-chrome

### Community Resources
- **MCP Documentation**: https://modelcontextprotocol.io
- **Awesome Claude Skills**: https://github.com/travisvn/awesome-claude-skills

---

## "Ask Claude" Protocol - How to Use This Guide

### What Does "Ask Claude" Mean?

When you say **"Ask Claude"** in conversation with Perplexity (or any AI assistant), you're requesting help to **write a professional Claude Standard Human-Written prompt**.

This is NOT about asking Claude AI directly—it's about crafting the optimal prompt TO give to Claude.

### The Workflow

1. **You explain your task** in your own words (C-grade English is perfectly fine!)
   - Example: "Hey, I need Claude to review my code and find bugs"

2. **The AI assistant translates** your request into Claude Standard format using:
   - The 10-Component Framework
   - Claude 4.x best practices  
   - Appropriate XML structure
   - Chain of thought reasoning
   - Tool/MCP/Skills integration (if needed)
   - Environment-specific optimizations

3. **You receive a professional prompt** ready to use with Claude

### Example Transformation

**Your C-Grade / Human-Written English**:
> "I need Claude to help me write some Python code that connects to a database and gets user info. Make it secure and don't let it break."

**Professional Claude Prompt Output**:

## Document Metadata

**Version**: 1.0  
**Last Updated**: November 19, 2025  
**Maintained By**: Research synthesis from official Anthropic sources  
**Sources**: 
- 39 official files from your provided materials
- 85+ web sources from Anthropic documentation, GitHub repositories, and community resources
- Comprehensive analysis of Claude 4.x model capabilities and prompt engineering best practices

**Usage License**: This document synthesizes publicly available information from Anthropic and open-source community resources. Use it as a reference for understanding and implementing effective Claude prompt engineering.

---

*End of Guide*
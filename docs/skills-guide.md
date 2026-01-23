# Claude Skills Guide

Learn about Claude Skills and how to use them in your workflows.

> **Last Updated: January 23, 2026** | Includes subagent orchestration, token efficiency comparison, and Meta Skill-Creator

---

## What Are Claude Skills?

**Claude Skills** are modular, reusable task packages that teach Claude how to execute repeatable workflows. They're designed to extend Claude's capabilities with domain-specific knowledge and procedures.

### Key Characteristics

- ✅ **Modular** — Self-contained task packages
- ✅ **Reusable** — Can be used across different conversations
- ✅ **Discoverable** — Claude automatically finds relevant Skills
- ✅ **Composable** — Multiple Skills can work together
- ✅ **Efficient** — Progressive disclosure avoids overwhelming context

### January 2026 Updates

- **Subagent Orchestration** — 90.2% performance improvement with 3-tier hierarchy
- **Meta Skill-Creator** — Generate Skills from natural language descriptions
- **Token Efficiency** — Only 5 tokens until activated (vs MCP's 42.6K)
- **Community Consensus** — "Bigger than MCP" for complex workflows
- **Wrapper pattern** — Token-efficient skill architecture
- **Progressive disclosure** — Load heavy logic only when needed
- **Enterprise skills** — Organization-wide skill management
- **Skill scopes** — Personal, Project, and Enterprise levels

> **Community Insight**: Skills are increasingly seen as "bigger than MCP" due to their token efficiency and orchestration capabilities. No official marketplace exists yet, but community sharing is growing rapidly.

---

## How Skills Work

### Loading Architecture

1. **Metadata Loading** (~100 tokens)
   - Claude scans available Skills
   - Identifies relevant Skills for current task

2. **Full Instructions** (<5k tokens)
   - Loaded only when Claude determines relevance
   - Contains detailed procedures and examples

3. **Bundled Resources** (as needed)
   - Files, templates, code samples
   - Loaded only when actually used

### Progressive Disclosure

Skills use an intelligent loading system that:
- Starts with minimal context overhead
- Loads full instructions when needed
- Bundles resources for dependent operations
- Avoids wasting tokens on unused information

---

## Wrapper Pattern (Jan 2026 Best Practice)

The wrapper pattern is the recommended architecture for token-efficient skills.

### The Problem

**OLD approach** (loads everything at startup):
```
❌ All skills in context window from start
❌ 67,300 tokens consumed by 7 MCP servers before conversation starts
❌ Only 33% of 200K context budget remaining
```

### The Solution

**NEW approach** (progressive disclosure):
```
✅ Thin wrapper skill (50-100 lines)
✅ Heavy logic in separate files
✅ Loaded only when skill is invoked
✅ Context cost only on use, not at startup
```

### Wrapper Pattern Structure

```
my-skill/
├── SKILL.md           # Thin wrapper (50-100 lines) - always in context
├── implementation/
│   └── full-logic.md  # Heavy logic (1,000+ lines) - loaded on demand
├── templates/
│   └── examples.md    # Templates - loaded on demand
└── resources/
    └── data.json      # Resources - loaded on demand
```

### Example Wrapper Skill

**SKILL.md (100 lines - always in context)**:
```markdown
---
name: documentation-updater
description: Updates documentation after coding sessions by analyzing conversation and codebase
---

# Documentation Updater Skill

## When to Use
Use this skill after completing a coding session to update project documentation.

## How It Works
1. Analyzes conversation and codebase changes
2. Distributes insights across CLAUDE.md, README.md, docs/
3. Updates hierarchies and strategies

## Implementation
See ./implementation/full-logic.md for complete implementation details.
```

**./implementation/full-logic.md (1,326 lines - loaded on demand)**:
```markdown
# Full Implementation Details

[Heavy logic, detailed procedures, extensive examples...]
```

### Benefits

| Aspect | Old Approach | Wrapper Pattern |
|--------|--------------|-----------------|
| **Startup Cost** | High (all skills loaded) | Low (only metadata) |
| **Token Usage** | Constant overhead | Pay-per-use |
| **Parallel Execution** | Limited | Enabled |
| **Token Isolation** | None | Heavy ops isolated |

### Skills vs MCP Token Comparison

| Metric | Skills | MCP Servers |
|--------|--------|-------------|
| **Base Context Cost** | ~5 tokens | ~42,600 tokens (7 servers) |
| **Percentage of 200K Context** | 0.0025% | 33.7% |
| **Loading Model** | On-demand activation | All at startup |
| **Cost Model** | Pay-per-use | Constant overhead |

> **Key Finding**: Skills consume only **5 tokens** until activated, while 7 MCP servers consume **42,600 tokens** (33.7% of context) before any conversation starts. This makes Skills dramatically more token-efficient for complex multi-step workflows.

### Guidelines

- Keep SKILL.md under **100 lines**
- Keep each reference file under **200 lines**
- Use indexed structure for targeted updates
- Prioritize "just-in-time" loading
- Test with representative queries

---

## Subagent Orchestration with Skills (Jan 2026)

Skills enable powerful subagent orchestration patterns that achieve **90.2% performance improvement** over single-agent approaches.

### 3-Tier Hierarchy Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    TIER 1: STRATEGIC ORCHESTRATOR               │
│                         (Claude Opus 4)                         │
│                                                                 │
│    • High-level planning and coordination                       │
│    • Resource allocation decisions                              │
│    • Cross-coordinator synchronization                          │
│    • Final quality assurance                                    │
└─────────────────────────────────────────────────────────────────┘
                              │
           ┌──────────────────┼──────────────────┐
           │                  │                  │
           ▼                  ▼                  ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│  TIER 2:        │  │  TIER 2:        │  │  TIER 2:        │
│  COORDINATOR A  │  │  COORDINATOR B  │  │  COORDINATOR C  │
│  (Sonnet 4)     │  │  (Sonnet 4)     │  │  (Sonnet 4)     │
│                 │  │                 │  │                 │
│  Domain: Docs   │  │  Domain: Code   │  │  Domain: Tests  │
└─────────────────┘  └─────────────────┘  └─────────────────┘
         │                   │                   │
    ┌────┴────┐         ┌────┴────┐         ┌────┴────┐
    │         │         │         │         │         │
    ▼         ▼         ▼         ▼         ▼         ▼
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│TIER 3 │ │TIER 3 │ │TIER 3 │ │TIER 3 │ │TIER 3 │ │TIER 3 │
│Spec A │ │Spec B │ │Spec C │ │Spec D │ │Spec E │ │Spec F │
│Sonnet │ │Sonnet │ │Sonnet │ │Sonnet │ │Sonnet │ │Sonnet │
└───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘
```

### Performance Metrics

| Approach | Time | Improvement |
|----------|------|-------------|
| **Sequential (Single Agent)** | 45 minutes | Baseline |
| **Parallel (3-Tier Subagents)** | 10 minutes | **90.2% faster** |

### Model Allocation Strategy

| Tier | Model | Purpose | Token Budget |
|------|-------|---------|--------------|
| **Orchestrator** | Claude Opus 4 | Strategic planning, coordination | High |
| **Coordinators** | Claude Sonnet 4 | Domain management, task distribution | Medium |
| **Specialists** | Claude Sonnet 4 | Focused execution, specific tasks | Focused |

### Implementation Pattern

```markdown
---
name: subagent-orchestrator
description: Orchestrates parallel subagents for complex multi-file tasks
---

# Subagent Orchestrator Skill

## When to Use
- Tasks spanning 5+ files
- Independent subtasks that can parallelize
- Complex workflows requiring domain expertise

## Orchestration Protocol

### Phase 1: Analysis
1. Decompose task into independent subtasks
2. Identify domain boundaries
3. Allocate resources per tier

### Phase 2: Dispatch
1. Create coordinator for each domain
2. Coordinators spawn specialists as needed
3. Maintain isolation between branches

### Phase 3: Synthesis
1. Collect results from all branches
2. Resolve conflicts at coordinator level
3. Orchestrator performs final integration

## Implementation
See ./implementation/orchestration-logic.md
```

### When to Use Subagent Orchestration

| Scenario | Single Agent | Subagents |
|----------|--------------|-----------|
| Simple file edit | ✅ Use | ❌ Overkill |
| Multi-file refactor | ⚠️ Slow | ✅ Recommended |
| Full codebase update | ❌ Too slow | ✅ Required |
| Cross-domain tasks | ❌ Context limits | ✅ Ideal |

---

## Skill Scopes

Skills can exist at three levels:

### 1. Personal Skills
- **Location**: `~/.claude/skills/`
- **Scope**: Available across all your projects
- **Use Case**: Personal workflows, preferences

### 2. Project Skills
- **Location**: `.claude/skills/` (in project root)
- **Scope**: Specific to current project
- **Use Case**: Project conventions, team standards

### 3. Enterprise Skills
- **Location**: Organization-managed
- **Scope**: Organization-wide
- **Use Case**: Compliance, brand guidelines, company standards

---

## Skill Discovery Process

### How Claude Finds Skills

1. **Discovery** (startup)
   - Claude loads only `name` and `description` of each skill
   - Minimal token consumption (~100 tokens per skill)

2. **Activation** (on match)
   - When request matches skill's description, Claude asks to use the skill
   - User can approve or decline

3. **Execution** (on approval)
   - Claude loads full SKILL.md content
   - Loads referenced files or runs bundled scripts as needed
   - Follows skill's instructions

### Testing Skills

To test a specific skill, ask Claude to do a task that matches the skill's description.

**Example**: If your skill has description "Reviews pull requests for code quality", ask Claude to "Review the changes in my current branch."

---

## Official Skills (Anthropic-Provided)

### Document Skills

#### PowerPoint Skill (.pptx)
- **Purpose**: Create and edit PowerPoint presentations
- **Use Cases**: Business presentations, slide decks, reports
- **Availability**: Claude.ai and API

#### Excel Skill (.xlsx)
- **Purpose**: Create and edit spreadsheets
- **Use Cases**: Data analysis, financial models, reporting
- **Availability**: Claude.ai and API

#### Word Skill (.docx)
- **Purpose**: Create and edit Word documents
- **Use Cases**: Reports, contracts, proposals
- **Availability**: Claude.ai and API

#### PDF Skill
- **Purpose**: Analyze and extract information from PDFs
- **Use Cases**: Document review, research, data extraction
- **Availability**: Claude.ai and API

---

## Using Skills in Claude.ai

### Enable Skills

1. **Open Settings** → **Capabilities**
2. **Toggle Skills** on
3. **Choose which Skills** to enable
4. **Start using them** in your conversations

### Example Usage

```
Create a quarterly business review presentation with:
- Title slide with company logo
- Financial performance section
- Strategic initiatives update
- Q4 outlook and priorities

Make it professional and data-driven.
```

Claude will automatically use the PowerPoint Skill to create your presentation.

---

## Using Skills in Claude Desktop

### Setup

Skills are available in Claude Desktop without special configuration. They're enabled by default in Capabilities settings.

### Usage

Same as Claude.ai:
1. Enable Skills in Settings → Capabilities
2. Ask Claude to create or edit documents
3. Claude uses appropriate Skills automatically

---

## Using Skills via API

### Skills API Reference

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

# Skills are accessible through the API
# Include skill capabilities in your request

response = client.messages.create(
    model="claude-opus-4-20250514",
    max_tokens=2048,
    system="You are a document creation specialist with access to document Skills.",
    messages=[
        {
            "role": "user",
            "content": "Create a presentation summarizing Q3 results"
        }
    ]
    # Skills are automatically available
)
```

### Skill Configuration

Skills can be configured in your API requests to:
- Enable/disable specific Skills
- Set permissions for document operations
- Control resource usage

---

## Custom Skills (Pro/Team/Enterprise)

### Creating Custom Skills

Pro and Team plan users can create custom Skills for:
- Company-specific workflows
- Brand guidelines and templates
- Compliance and policy documents
- Domain-specific procedures

### Use Cases

#### Example 1: Brand Guidelines Skill
```
Skill: Company Brand Guidelines

Includes:
- Logo usage guidelines
- Color palette specifications
- Typography standards
- Tone and voice guidelines
- Document templates

Purpose: Ensure all documents follow brand standards
```

#### Example 2: Compliance Skill
```
Skill: Financial Services Compliance

Includes:
- Regulatory requirements
- Compliance checklist
- Required disclosures
- Document templates
- Audit trail procedures

Purpose: Ensure compliance in financial documents
```

#### Example 3: Data Analysis Skill
```
Skill: Advanced Analytics Workflow

Includes:
- Data cleaning procedures
- Statistical methods
- Visualization templates
- Reporting formats
- Interpretation guidelines

Purpose: Standardize data analysis workflows
```

---

## Prompting with Skills

### How to Request Skill Usage

**Bad**: "Create a document"  
**Good**: "Create a professional quarterly report in Word format with charts and tables"

### Effective Skill Prompting

```xml
<system_prompt>
You have access to document creation Skills.
Use them to create professional, polished documents.
</system_prompt>

<task>
<objective>
Create a client proposal document that showcases our capabilities.
</objective>

<constraints>
- Professional formatting using Word
- Include company branding (logo, colors)
- 5-7 pages
- Executive summary, capabilities, pricing, next steps
</constraints>

<rules>
- Use official company templates (reference: templates/proposal-template.docx)
- Follow brand guidelines for colors and typography
- Include actual pricing (not placeholders)
- Professional tone, client-focused
</rules>
</task>

<format>
Create a Word document with:
1. Cover page with branding
2. Executive summary
3. Capabilities overview
4. Case studies (2-3 examples)
5. Pricing
6. Next steps and CTA
</format>
```

---

## Best Practices

### ✅ DO:

- **Specify output format** — "Create a PowerPoint presentation" vs "Create a document"
- **Include guidelines** — Reference brand guidelines or templates
- **Be specific about structure** — Outline sections and content
- **Provide examples** — Show what good looks like
- **Request polish** — "Professional", "executive-ready", "production-quality"

### ❌ DON'T:

- **Assume Skills will auto-load** — Explicitly request Skills for important work
- **Forget formatting** — Specify desired formatting and structure
- **Skip context** — Provide audience and purpose
- **Use placeholder data** — Use real data for better results
- **Ignore branding** — Include style guides when relevant

---

## Troubleshooting

### Skills Not Available

**Solution:**
1. Check Settings → Capabilities → Skills
2. Verify Skills are toggled on
3. Restart Claude if needed
4. Check plan level (some Skills Pro/Team only)

### Unexpected Formatting

**Solution:**
1. Provide more specific formatting instructions
2. Include a reference document or template
3. Request specific styling (fonts, colors, layout)

### Skills Not Being Used

**Solution:**
1. Explicitly ask for specific Skills
2. Mention the file format you want (PowerPoint, Excel, Word)
3. Provide more context about the output format

---

## Next Steps

1. **Enable Skills** in your Claude settings
2. **Try creating a document** — Start simple (presentation, spreadsheet)
3. **Explore use cases** — PowerPoint for presentations, Excel for analysis
4. **Refine prompts** — Use examples to show desired style
5. **Consider custom Skills** — If using Team plan

---

---

## When to Create a Skill

Create a skill when you:
- Do something **more than 3 times**
- Need consistent, repeatable workflows
- Want to share procedures across projects or teams
- Need to standardize complex multi-step processes

### Skill Creation Guidelines

1. Use real use cases for testing (not constructed examples)
2. Skills are reusable by commands, agents, hooks
3. Start with wrapper pattern from day one
4. Test with representative queries
5. Iterate based on actual usage

---

## Meta Skill-Creator (Jan 2026)

The Meta Skill-Creator allows you to **generate Skills from natural language descriptions**.

### How It Works

```
User: "Create a skill that reviews Python code for security vulnerabilities"

Meta Skill-Creator generates:
├── SKILL.md (wrapper)
├── implementation/
│   ├── security-patterns.md
│   └── vulnerability-checks.md
└── templates/
    └── report-template.md
```

### Usage

```
/skill-create "A skill that [description of what you want]"
```

### Best Practices

1. **Be specific** about the workflow you want
2. **Include examples** of inputs and outputs
3. **Specify constraints** (file types, languages, etc.)
4. **Iterate** on the generated skill

> **Note**: No official Skills marketplace exists yet (as of Jan 2026), but community sharing through GitHub is growing rapidly.

---

## Learn More

- [Official Anthropic Skills Documentation](https://docs.anthropic.com)
- [Skills Repository](https://github.com/anthropics/skills)
- [Claude Prompt Engineering Guide](../Claude-Prompt-Guide.md)
- [Skill Creator Documentation](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)
- [MCP Integration Guide](./mcp-integration.md) — How Skills and MCP work together

---

*Last Updated: January 23, 2026*

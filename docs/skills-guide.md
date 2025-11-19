# Claude Skills Guide

Learn about Claude Skills and how to use them in your workflows.

---

## What Are Claude Skills?

**Claude Skills** are modular, reusable task packages that teach Claude how to execute repeatable workflows. They're designed to extend Claude's capabilities with domain-specific knowledge and procedures.

### Key Characteristics

- ✅ **Modular** — Self-contained task packages
- ✅ **Reusable** — Can be used across different conversations
- ✅ **Discoverable** — Claude automatically finds relevant Skills
- ✅ **Composable** — Multiple Skills can work together
- ✅ **Efficient** — Progressive disclosure avoids overwhelming context

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

## Learn More

- [Official Anthropic Skills Documentation](https://docs.anthropic.com)
- [Skills Repository](https://github.com/anthropics/skills)
- [Claude Prompt Engineering Guide](../Claude-Prompt-Guide.md)

<!-- Language Selector -->
<div align="center">

📖 **Select Your Language:**

[English](./README.md) | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md)

</div>

---

# 📦 Claude Skills Collection

Welcome to the Claude Skills repository! This directory contains reusable, modular task packages that extend Claude's capabilities with domain-specific knowledge, procedures, and workflows.

---

## 🎯 What Are Claude Skills?

**Claude Skills** are structured bundles of instructions, examples, and resources that teach Claude to execute repeatable workflows in specific domains. They're designed to be:

- ✅ **Modular** — Self-contained, focused on specific tasks
- ✅ **Reusable** — Used across different conversations and projects
- ✅ **Composable** — Multiple Skills can work together seamlessly
- ✅ **Discoverable** — Claude automatically identifies relevant Skills
- ✅ **Efficient** — Progressive disclosure prevents context bloat

### Why Use Skills?

Skills help you:
- 📚 **Standardize processes** across your team
- 🎯 **Ensure consistency** in outputs and workflows
- ⏱️ **Save time** with pre-built procedures
- 🔧 **Customize Claude** for your specific domain
- 📈 **Improve quality** through proven patterns

---

## 📚 Available Skills in This Collection

We maintain a comprehensive collection of **22 production-ready skills** covering development, infrastructure, testing, and deployment:

### Web Development & Full-Stack

| Skill Name | Purpose | Status |
|-----------|---------|--------|
| [NextJS App Router](./examples/nextjs-app-router-skill.md) | Master Next.js 15+ with App Router, server components, and advanced patterns | ✅ Available |
| [Tailwind Design System](./examples/tailwind-design-system-skill.md) | Build design systems with Tailwind CSS | ✅ Available |
| [NextAuth Authentication](./examples/nextauth-authentication-skill.md) | Implement secure authentication with NextAuth.js | ✅ Available |
| [API Development](./examples/api-development-skill.md) | Design and build scalable REST/GraphQL APIs | ✅ Available |

### Backend & Infrastructure

| Skill Name | Purpose | Status |
|-----------|---------|--------|
| [AWS Cloud Infrastructure](./examples/aws-cloud-infrastructure-skill.md) | Design and deploy AWS infrastructure with best practices | ✅ Available |
| [Google Cloud Platform](./examples/google-cloud-platform-skill.md) | Master GCP services and cloud architecture | ✅ Available |
| [Neon Serverless](./examples/neon-serverless-skill.md) | Build serverless applications with Neon databases | ✅ Available |
| [Prisma ORM](./examples/prisma-orm-skill.md) | Master Prisma for database operations and migrations | ✅ Available |

### Testing & Quality Assurance

| Skill Name | Purpose | Status |
|-----------|---------|--------|
| [Testing Framework](./examples/testing-skill.md) | Build comprehensive testing strategies | ✅ Available |
| [Vitest Unit Testing](./examples/vitest-unit-testing-skill.md) | Master Vitest for unit testing | ✅ Available |
| [Playwright E2E Testing](./examples/playwright-e2e-testing-skill.md) | Implement end-to-end testing with Playwright | ✅ Available |
| [Code Review](./examples/code-review.md) | Conduct thorough code reviews | ✅ Available |

### DevOps & Deployment

| Skill Name | Purpose | Status |
|-----------|---------|--------|
| [Vercel Deployment](./examples/vercel-deployment-skill.md) | Deploy applications on Vercel | ✅ Available |
| [Database Migrations](./examples/database-migrations.md) | Execute safe database migrations | ✅ Available |
| [Monitoring & Logging](./examples/monitoring-logging-skill.md) | Implement production monitoring and logging | ✅ Available |
| [Git Workflow](./examples/git-workflow-skill.md) | Master Git workflows and collaboration | ✅ Available |

### Development Standards & Best Practices

| Skill Name | Purpose | Status |
|-----------|---------|--------|
| [TypeScript Standards](./examples/typescript-standards.md) | Write production-grade TypeScript | ✅ Available |
| [Performance Optimization](./examples/performance-optimization-skill.md) | Optimize application performance | ✅ Available |
| [SEO Optimization](./examples/seo-optimization-skill.md) | Implement SEO best practices | ✅ Available |
| [Security & Compliance](./examples/security-compliance.md) | Implement security best practices | ✅ Available |
| [Accessibility & UX](./examples/accessibility-ux.md) | Build accessible, user-friendly applications | ✅ Available |
| [Customer Feedback Analysis](./examples/example-feedback-analyzer.md) | Analyze customer feedback and identify themes | ✅ Available |

**Total Skills Available: 22** | **All Production-Ready** ✅

To explore any skill, click the link above or browse the [examples/](./examples/) directory.

---

## 🚀 How to Use Skills

### Method 1: Claude.ai Web Interface

1. **Enable Skills** in Settings → Capabilities → Skills toggle
2. **Paste the skill content** into a new conversation
3. **Reference the skill** in your prompts
4. **Let Claude use it** automatically for relevant tasks

### Method 2: Claude Desktop App

1. **Open Claude Desktop**
2. **Go to Settings** → **Capabilities** → **Skills**
3. **Enable Skills** toggle
4. **Use naturally** in conversations

Example:
```
I need to analyze customer feedback and create an analysis document.
Can you use the feedback analysis skill to help with this?
```

### Method 3: Claude Code (CLI)

Skills work in Claude Code with the `/skills` command:

```bash
# View available skills
/skills list

# Use a specific skill
/skills load feedback-analysis
```

### Method 4: API Integration

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

# Include skill instructions in system prompt
system_prompt = """
You are a document analyst with the following skill available:
[Skill Content Here]
Use this skill when analyzing documents.
"""

response = client.messages.create(
    model="claude-opus-4-20250514",
    max_tokens=2048,
    system=system_prompt,
    messages=[
        {
            "role": "user",
            "content": "Analyze this customer feedback using the skill"
        }
    ]
)

print(response.content[0].text)
```

---

## 🛠️ How to Create Your Own Skills

### Skill Structure Requirements

Every skill should follow this standard structure:

```markdown
# Skill Name
Brief one-line description of what this skill does.

## Purpose
Detailed explanation of:
- What the skill helps Claude accomplish
- When to use it
- Expected outcomes

## Metadata
- **Name:** skill-name (kebab-case)
- **Version:** 1.0.0
- **Author:** Your Name
- **Created:** YYYY-MM-DD
- **Updated:** YYYY-MM-DD
- **Category:** (e.g., Analysis, Writing, Code Review)

## Installation
Instructions for different environments

### Claude.ai / Desktop
- Copy the skill content
- Paste in conversation
- Reference in your prompt

### Claude Code
Instructions specific to CLI usage

## Usage

### Basic Usage
Simple example of using the skill

### Advanced Usage
More complex scenarios

## Configuration
Any customization options available

## Examples
Real-world examples of the skill in action

## Dependencies
Any requirements or prerequisites

## Troubleshooting
Common issues and solutions

## License
License information for this skill
```

### Step-by-Step Guide to Creating a Skill

#### 1. **Define the Purpose**
```
Skill: Customer Feedback Analyzer

Purpose: Help Claude systematically analyze customer feedback
and identify themes, sentiment, and actionable insights.
```

#### 2. **Document the Procedure**
```
Procedure:
1. Read all feedback carefully
2. Identify recurring themes
3. Categorize by sentiment (positive/negative/neutral)
4. Extract actionable insights
5. Summarize findings
```

#### 3. **Provide Examples**
```
Example Input:
"Customer said: 'The product quality is great but delivery was slow'"

Example Output:
- Positive Theme: Product Quality
- Negative Theme: Delivery Speed
- Sentiment: Mixed (Positive for product, Negative for service)
- Action Item: Improve delivery times
```

#### 4. **Add Configuration Options**
```
Configuration:
- Include sentiment scores? (yes/no)
- Group by theme or by feedback? (theme/feedback)
- Output format? (markdown/json/structured)
```

#### 5. **Test and Refine**
Use your skill in conversations and refine based on results.

---

## 📋 Skill Template

Here's a complete template you can copy and customize:

```markdown
# [Skill Name]
[One-line description]

## Purpose
[Detailed explanation of purpose and use cases]

## Metadata
- **Name:** [skill-name]
- **Version:** 1.0.0
- **Author:** [Your Name]
- **Created:** [YYYY-MM-DD]
- **Updated:** [YYYY-MM-DD]
- **Category:** [Category]

## Installation

### Claude.ai/Desktop
1. Copy this skill
2. Paste in a new conversation
3. Reference in your prompt

### Claude Code
```bash
# Add skill content to ~/.claude/skills/
```

## Usage

### Basic Usage
```
Example prompt showing basic usage
```

### Advanced Usage
```
Example showing more complex usage
```

## Configuration
[Any configuration options]

## Examples

### Example 1
[Real-world example]

### Example 2
[Another example]

## Dependencies
[Any requirements]

## Troubleshooting

### Common Issue
**Solution:** [How to solve]

## Notes
[Additional information]

## License
[License - typically MIT]
```

---

## ✅ Best Practices

### When Creating Skills

- **Be Specific** — Focus on one clear task or workflow
- **Include Examples** — Show exactly what Claude should do
- **Document Steps** — Break complex processes into clear steps
- **Test Thoroughly** — Verify the skill works as intended
- **Add Metadata** — Include version, author, and creation date
- **Version Control** — Update version number when making changes

### When Using Skills

- **Reference Explicitly** — "Use the [Skill Name] to..."
- **Provide Context** — Explain why you're using the skill
- **Be Specific About Output** — Specify desired format
- **Give Examples** — Show desired style or structure
- **Iterate** — Refine based on results

---

## 🤝 Contributing

We'd love your contributions! To add your skill:

### Process

1. **Create Your Skill**
   - Follow the skill template and structure
   - Test thoroughly
   - Document all sections

2. **Prepare for Submission**
   - Save as `skills/examples/[skill-name].md`
   - Ensure proper formatting
   - Include all metadata

3. **Submit**
   - Create a pull request with your skill
   - Include description of what it does
   - Share any feedback about using it

4. **Review & Merge**
   - Maintainers will test your skill
   - Provide feedback if needed
   - Merge once approved!

### Contribution Guidelines

- ✅ **Do** follow the standard template
- ✅ **Do** include comprehensive examples
- ✅ **Do** test your skill before submitting
- ✅ **Do** document dependencies
- ❌ **Don't** include sensitive information
- ❌ **Don't** submit skills without testing
- ❌ **Don't** use complex jargon without explanation

---

## 🎓 Learning Resources

### Understanding Skills Better

- [Claude Skills Guide](../docs/skills-guide.md) — Comprehensive skills documentation
- [Prompt Engineering Guide](../Claude-Prompt-Guide.md) — How to prompt Claude effectively
- [Examples Directory](./examples/) — Real skill examples

### Similar Concepts

- **Superpowers** — User-created scripts and automations
- **MCP Servers** — Model Context Protocol integrations
- **Templates** — Reusable prompt structures

---

## 📞 Support & Questions

### How to Get Help

1. **Check Examples** — Look in `skills/examples/` for similar skills
2. **Read Documentation** — See [docs/skills-guide.md](../docs/skills-guide.md)
3. **Browse Issues** — Check GitHub Issues for common problems
4. **Ask the Community** — Create a new discussion thread

### Common Questions

**Q: Can I use other people's skills?**
A: Yes! Copy any skill and use it in your conversations.

**Q: Can I modify a skill?**
A: Absolutely. Customize it for your needs.

**Q: How do I know if a skill is working?**
A: Test with the examples provided. If Claude uses the procedures you outlined, it's working.

**Q: Can skills be used together?**
A: Yes! Skills can compose and reference each other.

---

## 📊 Skill Statistics

- **Total Skills**: (Community contributed)
- **Most Popular**: (Most used)
- **Newest Skills**: (Recently added)

---

## 🔗 Related Resources

- [Claude Prompt Engineering Guide](../Claude-Prompt-Guide.md)
- [Skills Implementation Guide](../docs/skills-guide.md)
- [MCP Integration Guide](../docs/mcp-integration.md)
- [Superpowers Plugin Guide](../docs/superpowers-guide.md)

---

## 📝 License

All skills in this collection are provided under the **MIT License** unless otherwise specified. See individual skill files for specific license information.

---

## 🙏 Acknowledgments

- **Anthropic** for developing Claude Skills
- **Community Contributors** for sharing their skills
- **You** for using and contributing to this collection!

---

**Last Updated:** November 19, 2025
**Location:** Claude Prompt Engineering Guide Repository
**Maintained By:** Community Contributors


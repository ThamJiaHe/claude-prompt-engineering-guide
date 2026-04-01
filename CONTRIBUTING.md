# Contributing to Claude Prompt Engineering Guide

Thank you for your interest in contributing! We welcome contributions from everyone. This guide will help you get started.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Ways to Contribute](#ways-to-contribute)
- [Getting Started](#getting-started)
- [Contribution Guidelines](#contribution-guidelines)
- [Submitting Changes](#submitting-changes)
- [Style Guide](#style-guide)

---

## Code of Conduct

### Our Commitment

We are committed to providing a welcoming and inspiring community for all. Please read and adhere to our Code of Conduct:

- Be respectful and inclusive
- Assume good intent
- Focus on constructive feedback
- Respect different opinions and experiences
- Help create a harassment-free environment

---

## Ways to Contribute

### 📝 Documentation

- **Fix typos or clarify language** in existing documentation
- **Add new examples** that demonstrate prompt engineering patterns
- **Improve existing examples** with better explanations
- **Add missing sections** or fill gaps in coverage

### 💡 Ideas & Suggestions

- **Report issues** with the guide or examples
- **Suggest improvements** to existing patterns
- **Request new patterns** for specific use cases
- **Highlight confusing sections** that need clarification

### 🎯 Examples & Templates

- **Contribute new prompt patterns** for specific domains
- **Add real-world use cases** from your experience
- **Create domain-specific templates** (e.g., legal analysis, medical research)
- **Expand example directories** with new scenarios

### 🐛 Bug Reports

- **Report technical errors** in code examples
- **Point out outdated information** (e.g., deprecated model names)
- **Flag broken links** or missing resources
- **Document Claude behavior changes** you've noticed

### ✨ Enhancements

- **Improve code examples** with better practices
- **Add visual diagrams** or flowcharts
- **Create quick reference cards** for specific topics
- **Build interactive examples** (if applicable)

---

## Getting Started

### 1. Fork the Repository

```bash
# Click "Fork" on GitHub to create your own copy
git clone https://github.com/YOUR-USERNAME/claude-code-handbook.git
cd claude-code-handbook
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

Use descriptive branch names:
- `feature/add-security-patterns` ✅
- `fix/typo-in-readme` ✅
- `docs/expand-mcp-section` ✅
- `feature-123` ❌

### 3. Make Your Changes

Edit files and create content following our style guide (below).

### 4. Commit Your Work

```bash
git add .
git commit -m "Add descriptive commit message"
```

Write clear, descriptive commit messages:
- ✅ `Add prompt engineering patterns for security analysis`
- ✅ `Fix typo in Claude models section`
- ✅ `Expand MCP integration documentation`
- ❌ `Update stuff`

### 5. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 6. Create a Pull Request

Go to GitHub and create a PR with:
- Clear title describing the change
- Detailed description of what and why
- Reference to any related issues
- Screenshots (if applicable)

---

## Contribution Guidelines

### Before You Start

- 📖 Read the main [Claude-Prompt-Guide.md](./Claude-Prompt-Guide.md)
- 📚 Review existing documentation to avoid duplication
- 🔍 Check for related open issues or PRs
- 💬 For major changes, open an issue first to discuss

### Content Standards

#### Accuracy
- ✅ Base content on official Anthropic documentation
- ✅ Test examples before submitting
- ✅ Cite sources for claims
- ✅ Use current model names (e.g., Claude 4.5, not Claude 4)

#### Clarity
- ✅ Use clear, professional language
- ✅ Explain technical concepts simply
- ✅ Include examples for complex ideas
- ✅ Organize content logically

#### Completeness
- ✅ Include working code examples
- ✅ Provide expected outputs
- ✅ Document edge cases
- ✅ Link to related sections

### File Organization

```
claude-code-handbook/
├── Claude-Prompt-Guide.md          # Main guide (modify only for major updates)
├── docs/
│   ├── quick-start.md              # Beginner introduction
│   ├── mcp-integration.md          # MCP-specific content
│   ├── skills-guide.md             # Skills documentation
│   ├── api-guide.md                # API-specific content
│   └── examples/                   # Real-world examples
│       ├── coding-tasks.md
│       ├── research-tasks.md
│       ├── business-analysis.md
│       └── document-creation.md
├── templates/                      # Ready-to-use templates
│   ├── minimal-prompt-template.md
│   └── comprehensive-prompt-template.md
└── .github/                        # GitHub templates
    ├── ISSUE_TEMPLATE/
    └── PULL_REQUEST_TEMPLATE.md
```

---

## Submitting Changes

### Pull Request Process

1. **Create a clear PR title** describing your changes
2. **Link to related issues** (e.g., "Fixes #123")
3. **Provide detailed description** of what changed and why
4. **Include examples** if relevant
5. **Request review** from maintainers
6. **Address feedback** constructively

### PR Checklist

- [ ] Followed the style guide (see below)
- [ ] Added/updated documentation as needed
- [ ] Tested examples (if applicable)
- [ ] No broken links
- [ ] Verified grammar and spelling
- [ ] Added relevant section to CHANGELOG.md

### Review Process

- PRs are reviewed by maintainers
- We aim to respond within 48 hours
- Feedback will be constructive and timely
- Approval requires at least one maintainer review

---

## Style Guide

### Markdown Formatting

#### Headings
```markdown
# H1 - Page Title
## H2 - Main Sections
### H3 - Subsections
#### H4 - Details
```

#### Code Blocks
```markdown
<!-- For generic code -->
```code
your code here
```

<!-- For specific languages -->
```python
# Python example
def hello():
    print("Hello")
```

```xml
<!-- XML examples -->
<system_prompt>Example</system_prompt>
```
```

#### Lists
```markdown
<!-- Unordered lists -->
- Item 1
- Item 2
  - Nested item
  - Another nested

<!-- Ordered lists -->
1. First
2. Second
3. Third
```

#### Tables
```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
```

### Tone & Voice

- **Professional but approachable** — Use "you" and be conversational
- **Clear and concise** — Avoid jargon; explain terms you must use
- **Active voice** — "Claude returns a response" not "a response is returned"
- **Confident** — Share knowledge authoritatively, but acknowledge limitations
- **Inclusive** — Use inclusive language; consider diverse audiences

### Emoji Usage

Use emojis sparingly for visual breaks:
- 📚 Documentation
- 💡 Tips and insights
- ⚠️ Warnings
- ✅ Best practices
- ❌ Anti-patterns
- 🚀 Performance tips
- 🔐 Security notes

### Examples

Every new pattern or technique should include:
1. **Clear explanation** of what and why
2. **XML or code example** showing implementation
3. **Expected behavior** or output
4. **When to use** (and when NOT to use)
5. **Related patterns** or techniques

#### Example Template

````markdown
## Pattern Name

Brief description of when and why to use this pattern.

### How It Works

Explanation of the mechanism and principles.

### Example

```xml
<your-example>
Here's a concrete example
</your-example>
```

### Expected Behavior

What Claude will do when given this prompt structure.

### When to Use This Pattern

- Scenario 1
- Scenario 2
- Scenario 3

### Related Patterns

- [Other Pattern Name](#)
- [Another Pattern](#)
````

---

## File Naming Conventions

- Use **lowercase with hyphens** for file names
- Be **descriptive** about content
- ✅ `advanced-mcp-techniques.md`
- ✅ `security-prompt-patterns.md`
- ❌ `new_file.md`
- ❌ `stuff.md`

---

## Git Commit Message Format

```
type: subject

body

footer
```

### Type
- `feat:` New feature or pattern
- `fix:` Bug fix or correction
- `docs:` Documentation change
- `refactor:` Code/content reorganization
- `style:` Formatting or style improvements

### Subject
- Lowercase
- Imperative mood ("add" not "added")
- No period at end
- Max 50 characters

### Body
- Explain WHAT changed and WHY
- Wrap at 72 characters
- Reference issues: "Fixes #123"

### Examples

```
feat: add security analysis prompt pattern

Add comprehensive pattern for security-focused code review prompts
with examples for OWASP vulnerability detection. Includes templates
for different threat models.

Fixes #45
```

```
docs: fix typo in models section

Change "Sonnet 3.7" to "Sonnet 4.5" throughout Claude models
overview section.
```

---

## Getting Help

### Have Questions?

- 📖 **Read the documentation** first
- 🔍 **Search existing issues** for similar questions
- 💬 **Open an issue** with your question
- 📧 **Contact maintainers** for guidance

### Common Issues

**Q: How do I test my documentation examples?**  
A: If they're Claude prompts, test them with Claude directly. For code examples, ensure they're syntactically correct.

**Q: Should I create a new file or edit existing?**  
A: Edit existing files when clarifying or fixing. Create new files for entirely new patterns or sections.

**Q: What if my PR gets rejected?**  
A: Don't worry! Feedback is constructive. Understand the concerns, revise, and resubmit.

---

## Recognition

### Contributors

We recognize and appreciate all contributions! Contributors will be:
- Listed in CONTRIBUTORS.md
- Credited in relevant section changelogs
- Thanked in community discussions

### Levels of Contribution

- **Documentation** — Fixed typos, improved clarity
- **Content** — Added new sections, patterns, or examples
- **Community** — Reported issues, answered questions
- **Maintenance** — Reviewed PRs, managed releases

---

## License

By contributing to this project, you agree that your contributions will be licensed under its MIT License.

---

## Questions?

- 📖 Review the [README.md](./README.md)
- 💬 Open an issue with your question
- 📧 Contact the maintainers

Thank you for contributing! 🙏


# Quick Start Guide 🚀

Get started with Claude prompt engineering in 5 minutes.

---

## What You'll Learn

This guide covers:
- ✅ How to write your first professional Claude prompt
- ✅ The 10-component framework (official structure)
- ✅ Best practices for different tasks
- ✅ Where to get examples

**Time needed:** 5-10 minutes to read, then you can start writing!

---

## The 3-Minute Intro

### The Golden Rule

**System Prompt** = Who Claude is  
**User Prompt** = What you need

Bad:
```
System: "You are a helpful assistant"
User: "Help me write a security review for this code"
```

Good:
```
System: "You are a senior security engineer with 15 years of experience"
User: "Review this code for security vulnerabilities. Look for SQL injection, XSS, and auth issues."
```

### The Structure (10 Components)

```xml
<!-- 1. Define who Claude is -->
<system_prompt>
You are a [ROLE with specific expertise].
</system_prompt>

<!-- 2. Set tone (optional) -->
<tone>Professional and direct</tone>

<!-- 3. Provide all context -->
<background>
[Relevant information, data, prior conversation]
</background>

<!-- 4. State the task -->
<task>
<objective>What needs to be done?</objective>
<constraints>What are the boundaries?</constraints>
</task>

<!-- 5. Set rules -->
<rules>
- MUST: [Required behavior]
- MUST NOT: [Prohibited behavior]
</rules>

<!-- 6. Show examples -->
<examples>
<good_example>[Example of desired output]</good_example>
</examples>

<!-- 7. Encourage thinking -->
<thinking>
Before responding, consider:
1. [Key question]
2. [Another question]
</thinking>

<!-- 8. Define format -->
<format>
[How should output be structured?]
</format>
```

---

## Your First Prompt: Code Review

### Basic Approach

```xml
<system_prompt>
You are a senior software engineer specializing in code quality.
</system_prompt>

<task>
Review this code for bugs and security issues.
</task>

<rules>
- Focus on critical issues first
- Provide specific line numbers
- Suggest concrete fixes
</rules>

[PASTE YOUR CODE HERE]

<format>
Structure your response as:
1. Critical Issues (with fixes)
2. Medium Priority Issues
3. Minor Suggestions
</format>
```

### Professional Approach (Better Results)

```xml
<system_prompt>
You are a principal engineer with 20 years of experience in distributed systems.
You specialize in security, performance, and code quality.
</system_prompt>

<background>
This code is for a payment processing system handling $1M+ daily volume.
It's customer-facing and must be rock-solid.
Team: 5 backend engineers, 2 security engineers
</background>

<task>
Review this code for:
1. Security vulnerabilities (OWASP top 10)
2. Performance bottlenecks
3. Best practices violations
4. Maintainability issues
</task>

<rules>
- Assume this will be code-reviewed by security team later
- Identify issues we should catch now
- Provide specific line numbers and fixes
- Rate severity: CRITICAL, HIGH, MEDIUM, LOW
- Do NOT suggest complete rewrites
</rules>

[PASTE YOUR CODE HERE]

<thinking>
Before responding, analyze:
1. What are the actual security risks?
2. What performance issues exist?
3. What best practices are violated?
4. How critical is each issue?
</thinking>

<format>
Structure as:
**CRITICAL Issues** (with specific fixes)
**HIGH Priority** (with specific fixes)
**MEDIUM Priority** (brief notes)
**LOW Priority** (suggestions)
**Overall Assessment** (1 paragraph)
</format>
```

---

## Tips for Better Results

### 1. Be Specific

❌ **Bad**: "Analyze this data"  
✅ **Good**: "Identify which customer segments are growing fastest. Focus on enterprise vs SMB growth rates."

### 2. Show Examples

❌ **Bad**: "Create a professional email"  
✅ **Good**: "Create a professional email. Here's an example of the tone we like: [insert example]"

### 3. Add Context

❌ **Bad**: "Fix this code"  
✅ **Good**: "This code handles user authentication for our SaaS platform. It processes 100K requests/day and must have 99.9% uptime."

### 4. Define Success

❌ **Bad**: "Write better documentation"  
✅ **Good**: "Write documentation that a junior developer could follow to set up the API locally in <15 minutes."

### 5. Encourage Thinking

Add this to any complex task:
```xml
<thinking>
Before responding, consider:
1. [Key analysis step]
2. [Another analysis step]
3. [Validation step]
</thinking>
```

---

## Common Tasks

### Task 1: Code Review

See example above. Key points:
- Define the code's purpose
- Specify what to look for
- Request severity levels
- Ask for concrete fixes

### Task 2: Business Analysis

```xml
<system_prompt>
You are a CFO with 15 years of experience in SaaS metrics.
</system_prompt>

<background>
Q2 Revenue: $5.2M (20% growth YoY)
Churn: 8.2% (target: <5%)
NPS: 42
Cash: $15M (12-month runway)
</background>

<task>
Analyze our metrics and recommend top 3 actions for Q3.
</task>

<thinking>
Consider:
1. Which metrics are concerning?
2. What's the strategic opportunity?
3. What can we actually execute?
</thinking>

<format>
1. Key Findings (3-4 bullet points)
2. Top 3 Recommended Actions (with expected impact)
3. Risk Assessment (what could go wrong?)
</format>
```

### Task 3: Long-Form Writing

```xml
<system_prompt>
You are a technical writer specializing in API documentation.
</system_prompt>

<task>
Write comprehensive documentation for our user authentication endpoint.
</task>

<rules>
- Target audience: Backend engineers new to our API
- Should take <15 minutes to read and understand
- Include: overview, examples, error handling, best practices
- Do NOT: document every edge case
</rules>

<examples>
<good_example>
[Link to similar documentation you like]
</good_example>
</examples>

<format>
1. Overview (1 paragraph)
2. How It Works (2-3 paragraphs)
3. Example Requests (with code)
4. Error Handling (common errors + fixes)
5. Best Practices (3-5 key practices)
6. Troubleshooting (FAQ style)
</format>
```

---

## When to Use Each Template

### Use the Minimal Template When:
- ✅ Task is straightforward
- ✅ Quick answer needed
- ✅ Context is already clear

### Use the Comprehensive Template When:
- ✅ Complex, multi-step task
- ✅ High-stakes decision
- ✅ Deep reasoning required
- ✅ Team will use this prompt repeatedly

---

## Next Steps

### 1. Pick a Template
- Quick task? → [Minimal Template](../templates/minimal-prompt-template.md)
- Complex task? → [Comprehensive Template](../templates/comprehensive-prompt-template.md)

### 2. Find Examples
- [Coding Tasks](./examples/coding-tasks.md)
- [Business Analysis](./examples/business-analysis.md)
- [Research Tasks](./examples/research-tasks.md)
- [Document Creation](./examples/document-creation.md)

### 3. Read the Full Guide
For deep dive: [Claude Prompt Engineering Guide](../Claude-Prompt-Guide.md)

### 4. Practice!
- Try one of the templates above
- See what works
- Iterate and improve

---

## Key Principles

Remember these 5 principles:

1. **📌 Be Explicit** — Specific instructions get better results
2. **📍 Add Context** — Explain the WHY behind requirements
3. **🎯 Show Examples** — Examples are more powerful than descriptions
4. **🧠 Encourage Thinking** — Ask Claude to reason through problems
5. **📋 Define Output** — Be clear about how you want results formatted

---

## Common Mistakes to Avoid

| Mistake | Instead |
|---------|---------|
| Vague instructions | Specific, detailed requests |
| No context | Rich background and data |
| No examples | 1-3 examples of desired output |
| Generic role | Specific expert role with credentials |
| Hope for the best | Explicit success criteria |

---

## Pro Tips

✨ **Tip 1**: Save working prompts for reuse  
✨ **Tip 2**: Iterate — first version rarely perfect  
✨ **Tip 3**: Test with real data — examples are different  
✨ **Tip 4**: Chain prompts — break complex tasks into steps  
✨ **Tip 5**: Use thinking for complex reasoning  

---

## Questions?

- 📖 **Full Guide**: [Claude Prompt Engineering Guide](../Claude-Prompt-Guide.md)
- 💡 **More Examples**: [Examples Directory](./examples/)
- 🎯 **Templates**: [Templates Directory](../templates/)

---

**Ready?** Pick a task above and start writing your first professional Claude prompt!

---

**Last Updated:** February 24, 2026


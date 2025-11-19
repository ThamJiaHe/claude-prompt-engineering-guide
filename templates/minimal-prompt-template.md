# Minimal Prompt Template

Use this template for quick tasks when you don't need the full framework. Perfect for:
- Simple questions or requests
- Quick analysis or feedback
- Short-form content generation

---

## Template

```xml
<system_prompt>
[Define your role/identity here - 1-2 sentences]
</system_prompt>

<task>
[What needs to be done? Be specific.]
</task>

<rules>
- [Key requirement or constraint]
- [Another rule or boundary]
</rules>

[Provide any additional context, background, or data needed]

<format>
[How should the output be structured?]
</format>
```

---

## Example Usage

### Code Review (Quick)

```xml
<system_prompt>
You are a senior software engineer specializing in code quality and security.
</system_prompt>

<task>
Review this code for bugs and security issues.
</task>

<rules>
- Focus on critical issues first
- Provide specific line numbers
- Suggest concrete fixes
</rules>

<code>
[PASTE CODE HERE]
</code>

<format>
Structure your response as:
1. Critical Issues
2. Medium Priority Issues
3. Minor Suggestions
</format>
```

### Business Question

```xml
<system_prompt>
You are a business analyst with expertise in SaaS metrics.
</system_prompt>

<task>
Analyze our churn rate and suggest retention improvements.
</task>

<rules>
- Use the metrics provided below
- Focus on actionable recommendations
- Consider implementation effort
</rules>

Q1 Metrics:
- Churn Rate: 8.2% (target: <5%)
- NPS: 42 (up from 35)
- Customer Retention: 87%

<format>
Provide 3-5 specific retention improvement initiatives.
</format>
```

---

## When to Use

✅ **Use this template when:**
- You have a straightforward request
- Context is already clear
- You want quick results
- The task is well-defined

❌ **Use the Comprehensive Template instead when:**
- The task is complex or multi-step
- You need deep analysis or reasoning
- Context requires extensive background
- Output quality is critical

---

## Tips

1. **Be specific** — Vague prompts get vague answers
2. **Add context** — Even brief context improves results
3. **Define rules** — Clear boundaries improve output quality
4. **Specify format** — Tell Claude how you want the answer

---

## Next Steps

- ✅ Copy this template
- ✅ Fill in each section
- ✅ Paste into Claude
- ✅ Iterate if needed

For more complex tasks, see [Comprehensive Prompt Template](./comprehensive-prompt-template.md).

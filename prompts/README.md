# Automation Prompts

This directory contains specialized prompts designed for automating repository maintenance and updates with Claude Code Max Opus 4.5.

## Available Prompts

### 1. Auto-Update All Plugins and Skills

**File:** `auto-update-plugins-skills.md`

**Purpose:** Comprehensive prompt for Claude Code Max Opus 4.5 to systematically update all 22 skills and plugin documentation in this repository.

**What It Does:**
- Updates all 22 skills to latest library/framework versions
- Verifies and updates all plugin documentation (Superpowers, MCP, Context7, etc.)
- Updates model references to Claude 4.5
- Increments version numbers appropriately
- Updates all dates and metadata
- Validates code examples and links
- Creates comprehensive update summary

**When to Use:**
- Quarterly maintenance updates
- After major Claude model releases
- When multiple dependencies need updating
- To ensure all content is current and accurate

**Time Required:** 2.5-3.5 hours for complete execution

**How to Use:**

See the detailed [USAGE-GUIDE.md](./USAGE-GUIDE.md) for step-by-step instructions.

Quick start:

1. **Copy the prompt**
   ```bash
   cat prompts/auto-update-plugins-skills.md
   ```

2. **Open Claude Code with Opus 4.5**
   ```bash
   claude-code --model opus-4.5 --effort high
   ```

3. **Paste the entire prompt** into Claude Code

4. **Review the updates** before committing

**Success Criteria:**
- ✅ All 22 skills updated
- ✅ All plugin docs verified and updated
- ✅ No broken links
- ✅ All code examples validated
- ✅ Version numbers incremented
- ✅ Dates updated consistently

**Documentation:**
- 📖 [Usage Guide](./USAGE-GUIDE.md) - Detailed step-by-step instructions
- 📊 [Implementation Summary](../IMPLEMENTATION-SUMMARY.md) - Complete implementation details

---

## Creating New Automation Prompts

When creating new automation prompts for this repository:

### Structure Guidelines

1. **Clear Purpose Statement**
   - What the prompt does
   - Why it's needed
   - Expected outcomes

2. **Detailed Scope**
   - Exact files to be updated
   - Specific sections to modify
   - What to preserve

3. **Methodology**
   - Step-by-step phases
   - Validation checkpoints
   - Quality assurance steps

4. **Execution Instructions**
   - Prerequisites
   - Commands to run
   - Git commit strategy

5. **Success Criteria**
   - Must-have requirements
   - Should-have targets
   - Nice-to-have bonuses

### Best Practices

- ✅ **Be Explicit**: Leave no ambiguity about what should be updated
- ✅ **Include Validation**: Always add automated and manual checks
- ✅ **Provide Context**: Explain WHY changes are needed
- ✅ **Use Checklists**: Make progress tracking easy
- ✅ **Document Time**: Estimate realistic time requirements
- ✅ **Add Examples**: Show desired output formats
- ✅ **Safety First**: Emphasize what NOT to change

### Template Structure

```markdown
# [Prompt Name] - Claude Code Max Opus 4.5 Prompt

> **Purpose:** [Brief description]
> **Created:** [Date]
> **Model:** Claude Code Max Opus 4.5
> **Repository:** ThamJiaHe/claude-prompt-engineering-guide

## 🎯 Task Overview
[Detailed description]

## 📋 Scope of Updates
[What will be updated]

## 🔄 Update Methodology
[Step-by-step approach]

## ⚙️ Execution Instructions
[How to run]

## 🎯 Success Criteria
[What defines success]

## 🚨 Important Notes
[Critical guidelines]

## 📊 Progress Tracking
[Checklists]

## 🔧 Tools and Resources
[Useful commands and links]

## 📝 Final Deliverables
[Expected output]
```

---

## Contributing

Have an idea for an automation prompt? Consider:

1. **Is it repetitive?** - Good candidate for automation
2. **Is it time-consuming?** - Worth automating
3. **Is it error-prone?** - Automation improves quality
4. **Can it be standardized?** - Consistent process exists

If yes to multiple questions above, create a prompt following our template!

---

## Maintenance

These prompts should be updated when:
- Repository structure changes
- New automation opportunities identified
- Feedback from using existing prompts
- Claude model capabilities evolve

**Last Updated:** January 31, 2026  
**Maintained By:** Repository contributors

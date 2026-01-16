# Customer Feedback Analyzer Skill

Systematically analyze customer feedback to identify themes, sentiment patterns, and actionable insights.

## Purpose

This skill helps Claude:
- 🔍 **Categorize** customer feedback by themes and topics
- 📊 **Assess sentiment** (positive, negative, neutral, mixed)
- 💡 **Extract insights** and actionable recommendations
- 📈 **Identify patterns** across multiple feedback items
- 📝 **Generate reports** summarizing findings

### Use Cases

- Customer satisfaction analysis
- Product feedback review
- Service improvement identification
- Competitive analysis
- User research synthesis
- Product roadmap planning

---

## Metadata

- **Name:** customer-feedback-analyzer
- **Version:** 1.1.0
- **Author:** Claude Prompt Engineering Guide
- **Created:** 2025-11-19
- **Updated:** 2026-01-15
- **Category:** Analysis & Research
- **Compatibility:** Claude Opus 4.5, Claude Code v2.x

---

## Installation

### Claude.ai / Claude Desktop

1. Copy the entire skill content (from "## Procedure" below)
2. Start a new conversation in Claude
3. Paste the skill content in the first message
4. Say: "I want to use the feedback analyzer skill. Here's my feedback..."
5. Provide your feedback

### Claude Code

```bash
# Copy this skill to your Claude Code skills directory
# Typically: ~/.claude/skills/

# Then use in Claude Code with:
/skills load customer-feedback-analyzer

# Or reference in a prompt:
# "Analyze this feedback using the Customer Feedback Analyzer skill"
```

### API Integration

Include in your system prompt:

```python
system_prompt = """
You have access to the Customer Feedback Analyzer skill.
When analyzing customer feedback, use the following procedure...
"""
```

---

## Procedure

When given customer feedback to analyze, follow these steps:

### Step 1: Parse the Feedback
- **Read** each feedback item carefully
- **Extract** the core sentiment (what the customer is saying)
- **Note** context (product, feature, timeframe if mentioned)

### Step 2: Identify Themes
- **Look for** recurring topics across feedback items
- **Group** similar feedback together
- **Count** how many times each theme appears
- **Record** the frequency

### Step 3: Assess Sentiment

For each theme, assess:
- **Positive** ✅ — Praised or appreciated
- **Negative** ❌ — Criticized or complained about
- **Neutral** ⚪ — Factual observation without judgment
- **Mixed** 🔄 — Contains both positive and negative aspects

### Step 4: Extract Insights

For each major theme, identify:
- **Impact** — How important is this to customers?
- **Frequency** — How often is it mentioned?
- **Recommendation** — What should be done about it?
- **Priority** — How urgent is this?

### Step 5: Generate Summary

Create a structured report with:
- Overview of total feedback analyzed
- Top themes identified
- Sentiment breakdown
- Top insights and recommendations
- Suggested next steps

---

## Usage

### Basic Usage

**Prompt:**
```
Analyze this customer feedback using the feedback analyzer skill:

"The product works great, but the user interface is confusing.
Delivery was fast though!"
```

**Expected Process:**
1. Parse: Customer likes product quality and delivery, dislikes UI
2. Identify Themes: Product Quality, User Interface, Delivery
3. Assess Sentiment:
   - Product Quality: Positive ✅
   - User Interface: Negative ❌
   - Delivery: Positive ✅
4. Extract Insights: Priority should be UI improvement
5. Report: Provide structured output

### Advanced Usage

**Prompt with Multiple Feedback Items:**
```
Analyze all this customer feedback and provide a comprehensive report:

FEEDBACK 1: "Your product is the best on the market!"
FEEDBACK 2: "Great service, but prices are too high."
FEEDBACK 3: "The software is amazing. Only wish it had mobile support."
FEEDBACK 4: "Everything about this is excellent!"
FEEDBACK 5: "Good product but customer support was slow."

Please organize by theme, assess sentiment, identify the top 3 issues,
and recommend the top 2 improvement priorities.
```

**What Claude Will Do:**
1. Parse all 5 feedback items
2. Identify themes: Product Quality, Pricing, Mobile Support, Customer Support
3. Calculate sentiment percentages
4. Rank by frequency and impact
5. Generate prioritized recommendations

---

## Configuration

### Output Format Options

**Option 1: Simple List**
```
Themes Identified:
- Theme 1: [sentiment] - [frequency]
- Theme 2: [sentiment] - [frequency]
```

**Option 2: Detailed Report**
```
# Feedback Analysis Report

## Overview
- Total feedback analyzed: [X]
- Overall sentiment: [Positive/Negative/Mixed]

## Themes
[Detailed breakdown with sentiment and examples]

## Recommendations
[Prioritized list of actions]
```

**Option 3: JSON Structure**
```json
{
  "analysis": {
    "total_feedback": X,
    "themes": [
      {
        "name": "Theme",
        "sentiment": "positive|negative|neutral|mixed",
        "frequency": X,
        "examples": ["example 1", "example 2"]
      }
    ]
  }
}
```

### Customization

You can customize by specifying:
- **Number of themes** — "Identify top 5 themes"
- **Depth of analysis** — "Give a brief summary" or "Detailed analysis"
- **Output format** — "Format as JSON", "Create a markdown table", etc.
- **Focus areas** — "Focus on feature requests only"

---

## Examples

### Example 1: Simple Product Feedback

**Input:**
```
Customer feedback:
"Love the features! UI is a bit confusing though."
```

**Analysis Output:**
```
THEMES IDENTIFIED:
1. Features - Positive ✅
2. User Interface - Negative ❌

SENTIMENT: Mixed 🔄
- Positive aspects: Features are well-liked
- Areas for improvement: UI needs simplification

RECOMMENDATION: Conduct UI/UX review and simplification project
PRIORITY: Medium (impacts user experience but core functionality works)
```

### Example 2: Multiple Feedback Items

**Input:**
```
Feedback from 3 customers:
1. "This software saves me 5 hours per week!"
2. "The interface is outdated and hard to navigate."
3. "Great features but the onboarding process is confusing."
```

**Analysis Output:**
```
THEMES IDENTIFIED:

1. Time Savings / Productivity ✅
   - Frequency: 1/3 (33%)
   - Sentiment: Positive
   - Impact: High

2. User Interface ❌
   - Frequency: 2/3 (67%)
   - Sentiment: Negative
   - Impact: High

3. Onboarding Process ❌
   - Frequency: 1/3 (33%)
   - Sentiment: Negative
   - Impact: Medium

SENTIMENT BREAKDOWN:
- Positive: 33%
- Negative: 67%
- Overall: Negative (but with strong positive use case)

TOP INSIGHTS:
1. Users recognize core value (productivity gains)
2. UX issues are a major barrier (2 of 3 mentioned)
3. Onboarding needs improvement

TOP RECOMMENDATIONS:
1. Priority 1: Redesign user interface (impacts 67% of feedback)
2. Priority 2: Improve onboarding process (impacts 33% of feedback)
3. Keep current features (they provide core value)
```

### Example 3: Sentiment Analysis

**Input:**
```
Analyze sentiment across this feedback:

"Your product is amazing! The customer support team was helpful and responsive.
However, the documentation could be better organized. Also, pricing seems high
compared to competitors. Despite these issues, I'll recommend it to others."
```

**Analysis Output:**
```
SENTIMENT BREAKDOWN:
- Positive Aspects (60%):
  ✅ Product quality ("amazing")
  ✅ Customer support ("helpful and responsive")
  ✅ Loyalty (willing to recommend)

- Negative Aspects (40%):
  ❌ Documentation organization
  ❌ Pricing competitiveness

OVERALL SENTIMENT: Positive with reservations 🔄
- Customer is satisfied enough to recommend
- Concerns about documentation and pricing
- Strong support team received praise

PRIORITY ACTIONS:
1. Short-term: Reorganize documentation
2. Medium-term: Evaluate pricing strategy
3. Maintain: Continue current support quality
```

---

## Configuration Options

When using this skill, you can specify:

```
Request: "Analyze this feedback [options]"

[options] can include:
- "briefly" (short version)
- "in detail" (comprehensive analysis)
- "as JSON" (structured format)
- "focus on negative feedback only"
- "identify only the top 3 themes"
- "include sentiment percentages"
- "generate recommendations"
```

---

## Dependencies

- None! This skill is self-contained
- Works with Claude.ai, Desktop, Code, and API
- No external tools required
- No data dependencies

---

## Troubleshooting

### Issue: Claude isn't identifying themes
**Solution:**
- Provide more feedback items (at least 3)
- Make feedback more explicit
- Ask Claude to "list all topics mentioned"

### Issue: Sentiment seems wrong
**Solution:**
- Provide clearer feedback
- Ask Claude to "explain the sentiment reasoning"
- Use explicit language in feedback

### Issue: Too many themes identified
**Solution:**
- Ask for "top 5 themes only"
- Request Claude to "combine related themes"
- Be more specific about what themes you care about

### Issue: Output format is wrong
**Solution:**
- Specify format explicitly: "format as JSON", "create a table", etc.
- Provide an example of desired format
- Ask Claude to "restructure the output"

---

## Tips for Best Results

1. **Provide Sufficient Feedback** — More items = better pattern recognition
2. **Use Consistent Format** — Clearer structure helps analysis
3. **Be Explicit About Goals** — "Identify feature requests" vs "general analysis"
4. **Request Specific Output** — "JSON with sentiment scores" vs "general report"
5. **Iterate** — Ask follow-up questions to refine analysis

---

## Related Skills

- **Market Research Analyzer** — Analyze competitive and market research
- **Survey Response Analyzer** — Process survey data systematically
- **Customer Sentiment Tracker** — Track sentiment trends over time

---

## Notes

This skill is particularly effective for:
- ✅ Customer feedback analysis
- ✅ Product review synthesis
- ✅ User research compilation
- ✅ Competitive analysis
- ✅ Feature prioritization

---

## License

MIT License — Use freely and modify as needed.

---

**Created:** November 19, 2025
**Updated:** January 15, 2026
**Version:** 1.1.0
**Status:** Ready to Use ✅

> **January 2026 Note:** This skill works optimally with Claude Opus 4.5 and its effort parameter. For large feedback sets, consider using `effort: high` in API calls for comprehensive analysis.


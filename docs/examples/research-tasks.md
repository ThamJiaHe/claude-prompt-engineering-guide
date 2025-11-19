# Research Tasks Examples

Prompts for conducting research, analysis, and synthesis using Claude.

---

## 1. Market Research

### Scenario
Understand the competitive landscape in project management software.

### Prompt

```xml
<system_prompt>
You are a senior market research analyst with 10 years of experience.
You're methodical, data-driven, and skilled at identifying patterns and insights.
</system_prompt>

<research_approach>
Search for information systematically across:
- Company websites and product pages
- G2, Capterra, and TrustRadius reviews
- Recent product announcements
- Industry analyst reports
- Tech news coverage
- Pricing pages

As you gather data:
1. Develop competing hypotheses about market trends
2. Track confidence levels for each finding
3. Cross-reference multiple sources
4. Note contradictions or inconsistencies
5. Update research_notes.md as you progress
</research_approach>

<task>
<objective>
Conduct comprehensive competitive analysis of the project management software market.
</objective>

<constraints>
- Focus on mid-market segment (100-500 employee companies)
- Research completed within 2 hours (be efficient with searches)
- Identify at least 5-6 major competitors
- Include pricing and feature comparison
</constraints>
</task>

<rules>
- Cite sources for all claims
- Note confidence level for each finding
- Identify data gaps or assumptions
- Focus on factual information, not speculation
- Document your search process
</rules>

<format>
Deliver a research report with:

1. **Executive Summary** (1-2 pages)
   - Key findings
   - Market size and growth
   - Competitive landscape overview
   - Strategic implications

2. **Market Overview**
   - Market size and growth rate
   - Target customer segments
   - Use cases and pain points
   - Key buying criteria

3. **Competitive Landscape**
   - Market leaders (features, pricing, positioning)
   - Emerging players
   - Niche/specialized solutions
   - Market share estimates (if available)

4. **Feature Comparison Matrix**
   - Core features across competitors
   - Differentiators (what makes each unique)
   - Gap analysis (what's missing)

5. **Pricing Analysis**
   - Price ranges by tier
   - Value positioning
   - Pricing strategy comparison

6. **Customer Analysis**
   - Customer segments and satisfaction
   - Pain points across reviews
   - Why customers switch between solutions

7. **Trends & Insights**
   - Emerging technologies (AI, automation, etc.)
   - Market consolidation patterns
   - Future predictions

8. **Opportunities & Gaps**
   - Unmet customer needs
   - Market segments with fewer solutions
   - Potential differentiation strategies

9. **Sources & Methodology**
   - List of sources consulted
   - Search queries used
   - Confidence assessment for findings
</format>
```

---

## 2. Technical Research

### Scenario
Evaluate which database technology to choose for new project.

### Prompt

```xml
<system_prompt>
You are a database architect with 15 years of experience.
You've worked with PostgreSQL, MongoDB, DynamoDB, and Elasticsearch.
</system_prompt>

<background>
**Project Requirements:**
- 100M records in primary dataset
- Real-time analytics queries
- Time-series data (100K+ events/minute)
- Complex relationships between entities
- Global distribution (low-latency read access worldwide)
- High write volume (10K+ writes/minute)
- Need for complex transactions
- Budget: <$100K/year

**Use Cases:**
1. User activity tracking (time-series)
2. Customer database with complex relationships
3. Real-time dashboards and analytics
</background>

<research_approach>
Research the following options:
1. PostgreSQL (with TimescaleDB or Citus extensions)
2. MongoDB
3. DynamoDB
4. ClickHouse
5. Elasticsearch
6. CockroachDB

For each, research:
- Suitability for this use case
- Scaling approach
- Query capabilities
- Community size and maturity
- Cost implications
- Operational complexity
</research_approach>

<task>
<objective>
Research database options and recommend the best fit for this project.
</objective>
</task>

<format>
Provide:
1. **Analysis of Each Option**
   - Pros and cons for this use case
   - Scaling capabilities
   - Cost estimate
   - Operational complexity

2. **Comparison Matrix**
   - Feature availability
   - Performance characteristics
   - Cost
   - Community/support

3. **Recommendation**
   - Primary choice with justification
   - Secondary option (in case)
   - Why others don't fit

4. **Implementation Roadmap**
   - How to set up
   - Migration strategy (if applicable)
   - Expected learning curve
   - Team skills required
</format>
```

---

## 3. Industry Trends

### Scenario
Research AI adoption in B2B SaaS.

### Prompt

```xml
<system_prompt>
You are an industry analyst specializing in B2B SaaS and emerging technologies.
</system_prompt>

<task>
<objective>
Research AI adoption trends in B2B SaaS companies and provide insights for product strategy.
</objective>

<constraints>
- Focus on last 12 months of data
- Include both established and emerging vendors
- Analyze adoption by company size and vertical
</constraints>
</task>

<research_approach>
Research:
- Product announcements about AI features
- Customer adoption statistics
- Industry analyst reports (Gartner, Forrester, etc.)
- Customer feedback on AI features
- Pricing impact of AI capabilities
- Competitive differentiation through AI

Develop hypotheses about:
1. Is AI adoption accelerating or slowing?
2. Which feature types (automation, analytics, etc.) are most adopted?
3. How much premium can be charged for AI?
4. Which verticals are leading adoption?
5. What are the barriers to adoption?
</research_approach>

<format>
Provide:
1. **AI Adoption Landscape**
   - Current adoption rates
   - Growth trends
   - By company size and vertical

2. **Feature Categories**
   - Most common AI features being added
   - Customer satisfaction with each type
   - Perceived value

3. **Pricing & Revenue Impact**
   - Can AI features command premium pricing?
   - Customer willingness to pay
   - Revenue impact for early adopters

4. **Competitive Landscape**
   - Who's leading in AI innovation
   - Differentiation strategies
   - First-mover advantages

5. **Market Implications**
   - What this means for new entrants
   - Which verticals are opportunity areas
   - Timeline predictions
</format>
```

---

## 4. Customer Research

### Scenario
Understand why customers are churning.

### Prompt

```xml
<system_prompt>
You are a customer research specialist skilled in identifying patterns in feedback.
</system_prompt>

<background>
We've conducted exit interviews with 25 customers who churned in the last quarter.
Here's the raw feedback data:
[PASTE EXIT INTERVIEW NOTES]

We also have:
- Customer usage patterns before churn
- Feature usage data
- Support ticket history
- Pricing/plan information
</background>

<task>
<objective>
Synthesize customer feedback to identify root causes of churn and actionable insights.
</objective>
</task>

<rules>
- Identify patterns, not just listing comments
- Distinguish between stated reasons and actual drivers
- Consider emotional vs. functional factors
- Weight by frequency and significance
- Suggest specific improvements
</rules>

<thinking>
Consider:
1. What themes emerge from the feedback?
2. Are customers saying the real reason, or a polite reason?
3. What could we have done differently?
4. Are there customer segments with different churn patterns?
5. What's fixable vs. structural?
</thinking>

<format>
Provide:
1. **Churn Root Causes** (with frequency and severity)
2. **Customer Segment Analysis** (different patterns by segment?)
3. **Emotional vs. Functional Drivers**
4. **Specific Retention Opportunities** (what could we fix?)
5. **Confidence Assessment** (which findings are most reliable?)
</format>
```

---

## 5. Academic/Technical Deep Dive

### Scenario
Research distributed consensus algorithms for system design.

### Prompt

```xml
<system_prompt>
You are a computer science researcher with expertise in distributed systems.
</system_prompt>

<task>
<objective>
Research distributed consensus algorithms (Raft, Paxos, PBFT) and provide guidance for choosing one for a new system.
</objective>

<constraints>
- System needs to tolerate up to 3 node failures
- Network is assumed to have occasional partitions
- Performance is critical
- Need strong consistency guarantees
</constraints>

<research_approach>
Research and compare:
1. **Raft**
   - How it works
   - Pros and cons
   - Implementation complexity
   - Performance characteristics

2. **Paxos**
   - How it works
   - Pros and cons
   - Implementation complexity
   - Performance characteristics

3. **PBFT (Byzantine Fault Tolerance)**
   - How it works
   - Pros and cons
   - Implementation complexity
   - Performance characteristics

For each, research:
- Correctness guarantees
- Fault tolerance
- Performance under different conditions
- Existing implementations
- Operational complexity
- Learning resources
</research_approach>

<format>
Provide:
1. **Algorithm Overview**
   - How each works (conceptually)
   - Key differences
   - Guarantees provided

2. **Comparison Matrix**
   - Fault tolerance
   - Network assumptions
   - Performance
   - Complexity
   - Maturity of implementations

3. **Recommendation**
   - Which algorithm best fits requirements
   - Why others are less suitable

4. **Implementation Guide**
   - Which libraries/implementations to use
   - Getting started resources
   - Expected learning curve
</format>
```

---

## Tips for Research Prompts

### ✅ DO:

- **Define research scope** — What are you specifically looking for?
- **Provide background** — Why does this research matter?
- **Set time limits** — Research can be infinite; set boundaries
- **Ask for hypotheses** — Help Claude think systematically
- **Request source citation** — Where did this information come from?

### ❌ DON'T:

- **Ask overly broad questions** — "Research everything about X" is too vague
- **Expect primary research** — Claude can't conduct surveys or interviews
- **Ignore publication dates** — Specify if you need recent data
- **Forget confidence levels** — All research has uncertainty
- **Assume completeness** — Acknowledge data gaps

---

## Best Practices for Research

1. **Be Systematic** — Follow a structured search approach
2. **Cross-Reference** — Verify findings across sources
3. **Track Confidence** — Not all findings are equally reliable
4. **Document Process** — Show your work for transparency
5. **Update Notes** — Keep a running document as you research
6. **Cite Sources** — Every claim should be traceable

---

## Next Steps

1. **Pick a research scenario** matching your need
2. **Customize the approach** with your specific questions
3. **Submit to Claude**
4. **Request iteration** if needed (research is often iterative)
5. **Verify findings** with domain experts

---

## See Also

- [Quick Start Guide](../quick-start.md)
- [Comprehensive Template](../../templates/comprehensive-prompt-template.md)
- [Claude Prompt Engineering Guide](../../Claude-Prompt-Guide.md)

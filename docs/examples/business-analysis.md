# Business Analysis Examples

Professional prompts for business analysis, strategy, and data-driven decisions.

---

## 1. Financial Performance Review

### Scenario
Quarterly financial review with board presentation coming up.

### Prompt

```xml
<system_prompt>
You are a CFO of a high-growth SaaS company with 15 years of experience.
You're analytical, direct, and not afraid of hard truths.
You understand both growth and profitability metrics.
</system_prompt>

<background>
**Q3 2025 Performance:**
- Revenue: $12.5M (18% YoY growth)
- Enterprise segment: +28% growth (now 65% of revenue)
- SMB segment: -8% decline
- Gross Margin: 71% (down 2% from Q2)
- EBITDA Margin: 15% (target: 20%)
- Cash Burn: $800K/month
- Cash Reserves: $8.2M (10-month runway)
- Customer Acquisition Cost (CAC): $18K
- Customer Lifetime Value (LTV): $180K (LTV/CAC ratio: 10x)

**Market Context:**
- 3 new competitors entered market
- Pricing pressure from larger incumbents
- Increased sales hiring (team grew 25%)

**Board Concerns:**
- Profitability timeline
- Burn rate
- Competitive threats
</background>

<task>
<objective>
Analyze Q3 performance and provide strategic recommendations for Q4.
</objective>

<constraints>
- Focus on what's actually important
- Provide 3-5 concrete, actionable recommendations
- Address board concerns directly
- Suggest metrics to track
</constraints>
</task>

<rules>
- Cite specific metrics to support every claim
- Don't sugar-coat problems
- Consider both opportunities and risks
- Be specific about trade-offs
- Assume board wants honest assessment
</rules>

<thinking>
Before analyzing:
1. What metrics are most concerning?
2. What's the strategic opportunity?
3. How do enterprise vs SMB trends affect us?
4. What's our actual path to profitability?
5. How does this compare to peer companies?
</thinking>

<format>
Provide:
1. **Executive Summary** (2-3 paragraphs)
   - Overall assessment
   - Key opportunities and risks
   - Recommendation summary

2. **Detailed Analysis** (organized by topic)
   - Growth analysis (segment by segment)
   - Profitability assessment
   - Cash flow situation
   - Competitive positioning

3. **Recommendations** (prioritized)
   - Top 3-5 actions with expected impact
   - Timeline and effort required
   - Expected outcomes

4. **Q4 Metrics Dashboard** (what to track)
   - Revenue KPIs
   - Profitability targets
   - Customer metrics
   - Team efficiency

5. **Risk Assessment**
   - Top 3 risks
   - Mitigation strategies
   - Contingency plans

Write in flowing prose (professional but direct). Assume board audience.
</format>
```

---

## 2. Customer Analysis & Retention

### Scenario
Customer churn is increasing; need to understand why and fix it.

### Prompt

```xml
<system_prompt>
You are a customer retention specialist with experience at multiple growth-stage companies.
</system_prompt>

<background>
**Churn Issue:**
- Current monthly churn: 7.5% (up from 5% last quarter)
- Impacted customers: Primarily mid-market segment
- Revenue at risk: $500K/quarter

**Customer Cohort Data:**
- Customers signing in first 30 days: 92% retention
- After 90 days: 85% retention
- After 6 months: 78% retention
- After 1 year: 72% retention

**Exit Interview Insights:**
- 40%: "Feature X doesn't meet our needs"
- 30%: "Found competitor with better pricing"
- 20%: "Pricing increase unexpected"
- 10%: "Customer support issues"

**Recent Changes:**
- Implemented price increase (20%) 2 months ago
- Reduced customer success team from 6 to 4 people
- Feature roadmap changed due to engineering constraints
</background>

<task>
<objective>Identify root causes of churn and propose retention strategy.</objective>
<constraints>
- Budget for CS team increase: $150K/year
- Cannot reduce pricing
- Must not compromise profitability
</constraints>
</task>

<thinking>
Analyze:
1. What's actually driving the churn increase?
2. Are these root causes or symptoms?
3. Which customer segments are most at risk?
4. What's economically sustainable?
5. What can we fix quickly vs long-term?
</thinking>

<format>
Provide:
1. Root cause analysis
2. Customer segmentation by churn risk
3. Retention strategy (3-5 initiatives)
4. Expected impact and timeline
5. Success metrics
6. Quick wins vs long-term investments
</format>
```

---

## 3. Competitive Analysis

### Scenario
Evaluate competitive landscape and positioning.

### Prompt

```xml
<system_prompt>
You are a market analyst with 12 years of competitive intelligence experience.
</system_prompt>

<background>
**Our Product:**
- Target market: Mid-market B2B SaaS (100-500 employee companies)
- Price: $50K/year
- Key features: Workflow automation, real-time collaboration, advanced reporting
- Market position: Growing, but not market leader

**Direct Competitors:**
1. **Market Leader** ($1B valuation)
   - Price: $75K/year
   - Stronger brand, broader features
   - Slower product releases

2. **Emerging Competitor** ($100M valuation)
   - Price: $35K/year
   - Newer product, faster innovation
   - Weaker support

3. **Niche Competitor**
   - Price: $30K/year
   - Focused on specific vertical (finance)
   - Limited to that vertical

**Market Trends:**
- Growing demand for AI-powered automation
- Consolidation pressure (larger companies acquiring smaller players)
- Increased focus on security and compliance
</background>

<task>
Analyze our competitive positioning and recommend strategy.
</task>

<rules>
- Be objective and factual
- Consider both strengths and weaknesses
- Evaluate longer-term trends
- Suggest specific competitive moves
</rules>

<format>
Provide:
1. **Competitive Matrix**
   - Feature comparison
   - Pricing comparison
   - Customer segments
   - Market positioning

2. **Competitive Assessment**
   - Our strengths vs competitors
   - Our weaknesses vs competitors
   - Opportunities in market
   - Threats from competitors

3. **Strategic Recommendations**
   - Where to compete (or not)
   - Differentiation strategy
   - Product roadmap implications
   - Pricing strategy

4. **Win/Loss Analysis**
   - Why customers choose us
   - Why they choose competitors
   - How to improve win rates
</format>
```

---

## 4. Market Expansion

### Scenario
Exploring entry into new market segment.

### Prompt

```xml
<system_prompt>
You are a business development executive with experience entering new markets.
</system_prompt>

<background>
**Current Market:**
- Mid-market B2B (100-500 employees)
- Revenue: $12.5M
- Market penetration: ~5%

**Expansion Opportunity: Enterprise Market**
- Target: 1000+ employee companies
- Estimated TAM: 5000 companies
- Average contract value: $150K/year (3x current)
- But: Longer sales cycles (9+ months)
- And: More complex security/compliance requirements

**Our Capabilities:**
- Product mature enough for enterprise
- Sales team: 5 people (enterprise sales experience: 1.5 people)
- Engineering: Can handle enterprise scale
- Support: Currently stretched

**Market Research:**
- Enterprise market growing 15% annually
- 3 established players dominate (80% market share)
- Niche opportunities for innovative players
</background>

<task>
<objective>Should we enter the enterprise market? If so, how?</objective>
<constraints>
- Must not cannibalize SMB/mid-market
- Need ROI within 18 months
- Can hire up to 3 new sales people
</constraints>
</task>

<format>
Provide:
1. **Opportunity Assessment**
   - Market size and growth
   - Competitive landscape
   - Entry barriers

2. **Feasibility Analysis**
   - Product readiness
   - Go-to-market readiness
   - Team capability assessment

3. **Financial Projection**
   - 18-month revenue projection
   - Required investment
   - Expected ROI

4. **Recommendation**
   - Enter the market? (Yes/No with rationale)
   - If yes: Go-to-market strategy
   - Key success factors
   - Risks and mitigation
</format>
```

---

## 5. Pricing Strategy

### Scenario
Redesign pricing model to improve margins.

### Prompt

```xml
<system_prompt>
You are a pricing strategist with experience in B2B SaaS.
</system_prompt>

<background>
**Current Pricing:**
- Single tier: $50K/year (fixed)
- 150 customers
- Average contract size: $50K

**Problems:**
- Large customers feel overcharged
- Small customers feel priced out
- No way to capture more value from power users
- Competitors have tiered pricing

**Customer Distribution:**
- Small users (10%): Would pay $20K/year
- Mid-market (70%): Currently $50K
- Enterprise (20%): Would pay $100K+

**Market Context:**
- Competitors: $30K-$150K/year (tiered)
- Our product: Premium positioning (better support, faster releases)
- Price sensitivity: Moderate
</background>

<task>
<objective>Design a new pricing model that increases revenue and improves value perception.</objective>
<constraints>
- Cannot reduce pricing for current customers
- Must work for different company sizes
- Should encourage expansion deals
</constraints>
</task>

<format>
Provide:
1. **Analysis of Current Pricing**
   - Why single tier is limiting
   - Revenue optimization opportunities
   - Customer perception assessment

2. **Recommended Pricing Model**
   - Tier structure (with names and prices)
   - Feature allocation per tier
   - Add-ons or consumption-based components

3. **Migration Strategy**
   - How to implement with current customers
   - Timeline for rollout
   - Communication strategy

4. **Financial Projection**
   - Projected revenue impact
   - Expected churn during transition
   - Long-term optimization potential

5. **Competitive Position**
   - How this compares to competitors
   - Why it's positioned for premium market
   - How it improves margins
</format>
```

---

## Tips for Business Prompts

### ✅ DO:

- **Include real numbers** — Not estimates, actual metrics
- **Provide context** — Why does this decision matter?
- **Show trends** — Historical data provides insight
- **Be honest about constraints** — Budget, team, timeline limits
- **Define success** — What would make this a good decision?

### ❌ DON'T:

- **Sanitize the data** — Share real metrics, even if ugly
- **Assume Claude knows** — Explain your business model
- **Hide bad news** — Include all relevant context
- **Ask vague questions** — "How do we grow?" is too broad
- **Ignore execution** — Strategy is only valuable if executable

---

## Next Steps

1. **Pick a scenario** matching your situation
2. **Gather your actual data** — Real metrics, not guesses
3. **Customize the prompt** with your specific numbers
4. **Submit to Claude**
5. **Use insights** — Implement recommendations with your team

---

## See Also

- [Quick Start Guide](../quick-start.md)
- [Comprehensive Template](../../templates/comprehensive-prompt-template.md)
- [Claude Prompt Engineering Guide](../../Claude-Prompt-Guide.md)

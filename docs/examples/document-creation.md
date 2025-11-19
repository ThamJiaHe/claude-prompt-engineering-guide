# Document Creation Examples

Prompts for creating high-quality documents, presentations, and content.

---

## 1. Technical Documentation

### Scenario
Create comprehensive API documentation.

### Prompt

```xml
<system_prompt>
You are a technical writer specializing in API documentation.
You write clear, concise documentation that junior developers can follow.
</system_prompt>

<background>
We have a REST API for user management with the following endpoints:
- POST /users (create user)
- GET /users/{id} (get user)
- PATCH /users/{id} (update user)
- DELETE /users/{id} (delete user)
- GET /users (list users with pagination)

Target Audience:
- Backend engineers new to our API
- Integration partners
- Technical non-technical (PMs, etc.)

Constraints:
- Documentation should be readable in <15 minutes
- Include code examples in JavaScript and Python
- Cover error handling and authentication
- Don't document every edge case (keep focused)
</background>

<task>
<objective>
Write comprehensive documentation for the user management API.
</objective>

<constraints>
- Must include working code examples
- Should be accessible to developers new to our API
- Must cover common use cases
- Include troubleshooting section
</constraints>
</task>

<rules>
- MUST include: Overview, endpoints, examples, errors, best practices
- MUST NOT: Document every edge case or rare scenarios
- Use simple language (explain technical terms)
- Include copy-paste-able code examples
</rules>

[INCLUDE API SPECIFICATION DETAILS]

<format>
Structure documentation as:

1. **Overview** (1 paragraph)
   - What this API does
   - Who should use it
   - Key concepts

2. **Getting Started** (5 minutes to read)
   - Authentication
   - Base URL
   - Making your first request
   - Response format

3. **Endpoints** (for each endpoint)
   - Description and use case
   - Request format (method, path, parameters)
   - Example request (with code)
   - Response format
   - Example response
   - Common errors and fixes

4. **Error Handling** (reference)
   - HTTP status codes
   - Error response format
   - Common error scenarios and solutions

5. **Best Practices** (3-5 key practices)
   - Authentication security
   - Rate limiting
   - Pagination usage
   - Error handling

6. **Troubleshooting** (FAQ style)
   - Common problems and solutions
   - When to use each endpoint
   - How to debug issues

Write in clear, professional prose. Use code blocks for all examples.
</format>
```

---

## 2. Marketing Copy

### Scenario
Create persuasive product landing page copy.

### Prompt

```xml
<system_prompt>
You are a marketing copywriter specializing in B2B SaaS.
You write persuasive, benefit-focused copy that drives conversions.
</system_prompt>

<background>
**Product:** Invoice management software
**Target:** CFOs and controllers at 50-500 person companies
**Key Benefits:**
- Automates invoice processing (saves 20+ hours/month)
- Integrates with existing accounting software
- Reduces invoice processing errors by 95%
- Improves cash flow visibility

**Competitors:** Accounting teams currently use manual processes or expensive legacy systems

**Company Positioning:** Modern, easy-to-use alternative to enterprise accounting software

**Call-to-action:** Sign up for free 14-day trial
</background>

<task>
<objective>
Write landing page copy that converts finance leaders to trial signups.
</objective>

<constraints>
- Must be scannable (use headers, short paragraphs)
- Should emphasize ROI and time savings
- Address common objections
- Drive toward CTA
</constraints>
</task>

<rules>
- MUST: Focus on benefits, not features
- MUST: Include social proof or testimonials
- MUST NOT: Use marketing jargon or hype
- Use specific numbers (20+ hours/month, not "lots of time")
- Write for the actual reader (CFO), not technical people
</rules>

[INCLUDE ANY CUSTOMER TESTIMONIALS OR CASE STUDIES]

<format>
Provide landing page sections:

1. **Hero Section**
   - Headline (benefit-focused)
   - Subheadline (clarification)
   - CTA button

2. **Problem Statement** (1 short paragraph)
   - Why current approach is broken
   - Cost to business
   - Emotional impact

3. **Solution Overview** (2-3 short sections)
   - How product solves the problem
   - Key benefits (results-focused)
   - How it's different

4. **Features** (scannable list)
   - 3-5 key features
   - Benefit of each feature

5. **Social Proof**
   - Customer testimonial
   - Results/metrics
   - Customer logos or names

6. **CTA Section**
   - Benefit-focused heading
   - Sign-up button

7. **FAQ** (address objections)
   - Common questions
   - Reassuring answers

Use conversational language. Emphasize ROI and ease of use.
</format>
```

---

## 3. Executive Summary

### Scenario
Write executive summary for quarterly business review.

### Prompt

```xml
<system_prompt>
You are a business strategist who can translate complex information into clear executive summaries.
You write concisely and focus on what matters to leadership.
</system_prompt>

<background>
**Audience:** Executive team (CEO, CFO, board members)
**Purpose:** Q3 business review
**Time available:** 5 minutes to read
**Key topics:**
- Financial performance
- Progress on strategic initiatives
- Risk assessment
- Recommendations

**Detailed Data:** [INCLUDE YOUR Q3 DATA]

**Prior Context:** [INCLUDE STRATEGIC GOALS FROM Q3 PLANNING]
</background>

<task>
<objective>
Create a compelling executive summary that synthesizes Q3 performance.
</objective>

<constraints>
- Maximum 2 pages
- Must be readable in <5 minutes
- Highlight both successes and challenges
- Clear recommendations
</constraints>
</task>

<rules>
- MUST: Be objective and data-driven
- MUST: Highlight key metrics first
- MUST NOT: Bury the important information
- Use headers and short paragraphs
- Include only what matters to decision-makers
</rules>

<format>
Structure as:

1. **One-Line Summary**
   - How did we perform overall? (good/concerning/mixed)

2. **Key Metrics** (table or bullets)
   - Revenue (vs. target)
   - Profitability (vs. target)
   - Customer metrics
   - Key operational KPIs

3. **Highlights** (bullets)
   - Top 3 successes
   - Quantified impact when possible

4. **Challenges** (bullets)
   - Top 2-3 concerns
   - Business impact of each

5. **Strategic Progress**
   - Progress against OKRs
   - On track / off track / completed items

6. **Risks & Mitigations**
   - Top 1-2 risks
   - What we're doing about them

7. **Recommendations**
   - Top 1-2 actions for Q4
   - Expected impact
   - Required resources

Write in clear, direct language. Assume sophisticated business audience.
</format>
```

---

## 4. Training Manual

### Scenario
Create training documentation for new feature rollout.

### Prompt

```xml
<system_prompt>
You are an instructional designer with experience creating user training materials.
You make complex topics easy to understand.
</system_prompt>

<background>
**Feature:** New advanced reporting dashboard
**Audience:** All users (varying technical skill levels)
**Goal:** Users can effectively use the new feature
**Available time for learning:** 30 minutes

**Feature Overview:**
[INCLUDE FEATURE DESCRIPTION]

**Key Use Cases:**
[INCLUDE 3-4 MAIN USE CASES]

**Existing UI/workflows:**
[DESCRIBE HOW USERS ACCESS THIS FEATURE]
</background>

<task>
<objective>
Create training documentation that enables users to effectively use the new reporting dashboard.
</objective>

<constraints>
- Learnable in 30 minutes
- Must work for users with varying technical skills
- Include both text and visual descriptions
- Include troubleshooting for common issues
</constraints>
</task>

<rules>
- MUST: Start simple, build complexity
- MUST: Include screenshots descriptions (visual guides)
- MUST: Give step-by-step instructions
- MUST NOT: Assume user knowledge
- Use plain language
- Include real examples
</rules>

<format>
Provide training content:

1. **What You'll Learn** (bulleted overview)
   - 3-4 key learning objectives

2. **Why This Matters** (1 paragraph)
   - How this helps them do their job
   - Time savings or benefit

3. **Getting Started** (step-by-step)
   - How to access the feature
   - Basic navigation
   - How to perform one simple task

4. **Main Use Cases** (one section per use case)
   - When to use this
   - Step-by-step instructions
   - Screenshots descriptions
   - Expected results

5. **Tips & Tricks** (quick wins)
   - 3-5 productivity tips
   - Common shortcuts

6. **Troubleshooting** (FAQ style)
   - Common problems
   - How to fix them
   - When to contact support

7. **Next Steps**
   - Practice exercises
   - Additional resources
   - How to get help

Include clear visual descriptions. Use numbered steps. Keep paragraphs short.
</format>
```

---

## 5. Case Study

### Scenario
Create customer case study for marketing.

### Prompt

```xml
<system_prompt>
You are a case study writer skilled at creating compelling customer success stories.
</system_prompt>

<background>
**Customer:** [Company name and description]
**Challenge:** [What problem they were facing]
**Solution:** [How you helped]
**Results:** 
- Metric 1: [improvement]
- Metric 2: [improvement]
- Metric 3: [improvement]

**Customer Background:**
[Industry, size, market position, prior approach]

**Implementation Details:**
[Timeline, team size, technical details]

**Available for quotes:** [Customer contact who can comment]
</background>

<task>
<objective>
Create a compelling case study that demonstrates customer success.
</objective>

<constraints>
- Target audience: Potential customers (similar companies)
- Length: 800-1200 words
- Must be readable in 5-10 minutes
- Include quantified results
</constraints>
</task>

<rules>
- MUST: Make customer the hero, not your product
- MUST: Include specific numbers/metrics
- MUST: Show their perspective and voice
- MUST NOT: Sound like marketing hype
- Use quotes from customer
- Focus on business impact, not technology
</rules>

<format>
Structure as:

1. **Opening** (compelling hook)
   - Who the customer is
   - Their challenge or goal

2. **The Challenge** (customer perspective)
   - Specific problems they faced
   - Business impact
   - Why existing solutions didn't work

3. **The Approach** (how you helped)
   - Your solution
   - Implementation journey
   - How customers adopted it
   - Include customer quote

4. **Results** (the payoff)
   - Specific metrics achieved
   - Timeline to results
   - Unexpected benefits
   - Include customer quote

5. **Quote** (customer perspective)
   - Recommendation or endorsement
   - Specific benefit they value

6. **Conclusion**
   - Summary of success
   - Company readiness to help similar customers

Write in narrative style (story format). Make customer the hero.
</format>
```

---

## Tips for Document Creation

### ✅ DO:

- **Know your audience** — Adjust language and depth accordingly
- **Front-load benefits** — Lead with the most important information
- **Use examples** — Concrete examples are clearer than abstractions
- **Include visuals** — Describe what diagrams/images should show
- **Organize clearly** — Use headers, sections, white space
- **Proofread** — Professional documents need polish

### ❌ DON'T:

- **Assume knowledge** — Explain what needs explaining
- **Bury the lead** — Put important info first, details later
- **Use jargon** — If you must use technical terms, explain them
- **Make it too long** — Respect readers' time
- **Be inconsistent** — Consistent formatting builds credibility
- **Skip examples** — Real examples improve understanding

---

## Next Steps

1. **Pick a document type** matching your need
2. **Customize the prompt** with your specific content
3. **Provide your data/background** — Real content produces better results
4. **Submit to Claude**
5. **Edit and polish** — AI-generated content needs refinement

---

## See Also

- [Quick Start Guide](../quick-start.md)
- [Comprehensive Template](../../templates/comprehensive-prompt-template.md)
- [Claude Prompt Engineering Guide](../../Claude-Prompt-Guide.md)

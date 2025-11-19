# Comprehensive Prompt Template

This is the **full framework** for professional, high-stakes prompts. Based on **Anthropic's 10-component framework**, this template is ideal for:
- Complex tasks requiring deep analysis
- Production prompts used by teams
- Critical decisions or deliverables
- Tasks requiring chain of thought reasoning

---

## Complete Template

```xml
<system_prompt>
You are a [ROLE with specific expertise and background].
[Add relevant experience, specialization, or perspective]
</system_prompt>

<tone>
[Communication style: professional/casual/technical/accessible]
[Formality level: formal/conversational/colloquial]
[Perspective: first-person/third-person/advisory]
</tone>

<background>
[All relevant context, prior conversations, domain knowledge, data, documents]

Key Context:
- [Context point 1]
- [Context point 2]
- [Context point 3]
</background>

<task>
<objective>
[Clear, specific statement of what needs to be accomplished]
</objective>

<constraints>
- [Specific requirement 1]
- [Specific requirement 2]
- [Limitation or boundary 1]
- [Format/structure specification]
</constraints>

<success_criteria>
[How will we know the response is successful?]
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]
</success_criteria>
</task>

<rules>
[Explicit dos and don'ts]

**MUST:**
- [Required action or behavior 1]
- [Required action or behavior 2]

**MUST NOT:**
- [Prohibited action or pattern 1]
- [Prohibited action or pattern 2]

**CONSIDER:**
- [Nice-to-have or contextual guidance]
</rules>

<examples>
<good_example>
[Concrete example of desired output]
[Show exactly what good looks like]
</good_example>

<bad_example>
[Example of what to avoid]
[Show what NOT to do]
</bad_example>
</examples>

<thinking>
Before responding, carefully consider:
1. [Key question or analysis step]
2. [Another critical consideration]
3. [Final validation step]

Show your reasoning in thinking tags if it helps with complex analysis.
</thinking>

<format>
[Detailed specification of how output should be structured]

Structure:
1. [Section 1 with description]
2. [Section 2 with description]
3. [Section 3 with description]

Style:
- [Writing style requirement]
- [Formatting requirement]
- [Tone requirement]

Output format:
[Specify XML tags, markdown, code blocks, or other structure]
</format>

[ANY ADDITIONAL DATA OR CONTEXT]
```

---

## Example: Technical Architecture Review

```xml
<system_prompt>
You are a principal cloud architect with 20 years of experience designing distributed systems.
You've led architecture decisions at multiple Fortune 500 companies and understand trade-offs between scalability, cost, and complexity.
</system_prompt>

<tone>
Professional and authoritative. Use technical language but explain decisions clearly for stakeholders.
Provide direct recommendations even if they challenge current approaches.
</tone>

<background>
**Current System:**
- Monolithic Node.js backend (500K LOC)
- PostgreSQL primary database
- 10 million monthly active users
- Current: 85% CPU utilization at peak hours
- Infrastructure: AWS, 50 EC2 instances

**Pain Points:**
- Slow deployments (45 minutes)
- Scaling difficulties
- Database query performance
- Team onboarding complexity (codebase is huge)

**Constraints:**
- Budget: $500K/year for infrastructure
- Team: 15 backend engineers
- Timeline: Changes must be gradual (12-month plan)
- Must support existing integrations with 50+ partners
</background>

<task>
<objective>
Design a microservices architecture that will address our scaling and deployment bottlenecks while minimizing disruption to our current operations.
</objective>

<constraints>
- Must handle 10M+ monthly active users
- Cannot exceed $500K/year infrastructure budget
- Gradual migration required (keep monolith running during transition)
- Must maintain 99.99% uptime
- Team has limited Kubernetes experience
</constraints>

<success_criteria>
- Deployment time reduced to <15 minutes
- CPU utilization drops to 60% or less at peak
- Team can deploy services independently
- All existing integrations continue working
- Migration completes within 12 months
</success_criteria>
</task>

<rules>
**MUST:**
- Provide specific service boundaries with clear responsibilities
- Include deployment and DevOps strategy
- Address database migration approach
- Outline team structure and skills needed
- Define monitoring and observability requirements

**MUST NOT:**
- Recommend a big-bang rewrite
- Ignore organizational/team factors
- Propose unproven technologies
- Ignore budget constraints

**CONSIDER:**
- Cost implications of each decision
- Team learning curve
- Internal vs external services
- Using managed services vs self-hosted
</rules>

<examples>
<good_example>
**Service: User Management**
- Owns: User accounts, authentication, profiles
- APIs: POST /users, GET /users/{id}, PATCH /users/{id}
- Database: PostgreSQL replica (separate from main)
- Deployment: 10-minute CI/CD pipeline with blue-green deployments
- Team: 2 backend engineers
- Success metric: <100ms p99 latency for GET /users/{id}
</good_example>

<bad_example>
"Just move everything to Kubernetes and use microservices everywhere. Break each class into its own service."
[This ignores:
- Team skill requirements
- Operational complexity
- Network latency
- Migration challenges
- Budget constraints]
</bad_example>
</examples>

<thinking>
Before providing architectural recommendations:
1. What are the actual bottlenecks? (deployment, scaling, development)
2. Is microservices the right fit for this team's maturity?
3. What's the minimal viable architecture to achieve goals?
4. How do we migrate gradually without disrupting users?
5. What's the cost/benefit of each approach?
</thinking>

<format>
Provide your response in this structure:

**1. Current State Analysis**
- What's working well
- What's problematic
- Root causes

**2. Recommended Architecture**
- Service boundaries (with diagram description)
- Data layer strategy
- Communication patterns

**3. Migration Plan**
- Phase 1 (months 1-4): [Services to extract]
- Phase 2 (months 5-8): [Services to extract]
- Phase 3 (months 9-12): [Services to extract]

**4. Organizational Changes**
- Team structure recommendations
- Required skills and training
- Deployment process changes

**5. Cost Analysis**
- Current: $500K/year estimate
- Proposed: Cost breakdown
- Expected ROI

**6. Risk Assessment**
- Top 3 risks
- Mitigation strategies
- Contingency plans

**7. Success Metrics**
- KPIs to track
- How we'll measure success
- Rollback criteria

**8. Next Steps**
- Immediate actions (0-2 weeks)
- First pilot service recommendation
- Stakeholder communication plan

Style: Professional, data-driven, with specific recommendations.
Use code blocks for architecture examples.
Include rough cost estimates.
</format>
```

---

## Component Explanations

### System Prompt
- **Purpose**: Define Claude's role and expertise
- **Length**: 1-3 sentences
- **Focus**: Identity, not instructions

### Tone
- **Purpose**: Set communication style
- **Includes**: Formality, perspective, voice
- **Optional**: Can be part of system prompt if brief

### Background
- **Purpose**: All context needed to understand the task
- **Includes**: Prior conversations, data, domain knowledge, constraints
- **Critical**: More is usually better

### Task
- **Objective**: What needs to be done (clear statement)
- **Constraints**: Specific requirements and boundaries
- **Success Criteria**: How we'll measure success

### Rules
- **MUST**: Required behaviors
- **MUST NOT**: Prohibited actions
- **CONSIDER**: Nice-to-haves or contextual guidance

### Examples
- **Good Example**: Show exactly what you want
- **Bad Example**: Show what to avoid
- **Count**: 1-3 examples per pattern

### Thinking
- **Purpose**: Encourage Claude to reason before responding
- **Style**: Questions or prompts for analysis
- **Effect**: Improves quality significantly (up to 39%)

### Format
- **Purpose**: Explicitly define output structure
- **Includes**: Sections, style, tone, structure
- **Critical**: Be specific about what you want

---

## When to Use

✅ **Use this template when:**
- Task is complex or multi-step
- Output quality is critical
- Deep reasoning required
- Production or high-stakes decisions
- Working with a team
- Building prompts for reuse

❌ **Use the Minimal Template instead when:**
- Task is straightforward
- Quick results are fine
- Context is already clear
- Single question/request

---

## Pro Tips

1. **Include real data** — Concrete metrics beat generic examples
2. **Show, don't tell** — Examples are more powerful than descriptions
3. **Explain WHY** — Context on requirements improves reasoning
4. **Define success** — Explicit criteria improve output quality
5. **Use thinking** — Explicitly encourage reasoning for complex tasks
6. **Iterate** — First attempt often isn't perfect; refine the prompt

---

## Advanced Variations

### For Long-Horizon Tasks

Add:
```xml
<multi_window_guidance>
This task may span multiple context windows.
Save progress regularly to files (progress.txt, state.json).
Use git commits to track state.
Do not stop early due to token concerns.
</multi_window_guidance>

<state_tracking>
Track progress in:
- progress.txt: Freeform progress notes
- status.json: Structured state
- Git commits: Code checkpoints
- TODO.md: Remaining work
</state_tracking>
```

### For Research Tasks

Add:
```xml
<research_approach>
Search systematically for information.
Develop competing hypotheses as you gather data.
Track confidence levels for each finding.
Cross-reference multiple sources.
Update research_notes.md with progress.
</research_approach>
```

### For Tool Integration

Add:
```xml
<tool_usage>
Available tools:
- File operations (read, write, edit)
- Code execution
- Web search
- External APIs

Use tools proactively to:
[Specific tool use cases]
</tool_usage>
```

---

## Next Steps

1. ✅ Choose this template for complex tasks
2. ✅ Fill in each section carefully
3. ✅ Include concrete examples
4. ✅ Test and iterate
5. ✅ Save successful prompts for reuse

---

## Learn More

- [Claude Prompt Engineering Guide](../Claude-Prompt-Guide.md) — Full reference
- [Minimal Prompt Template](./minimal-prompt-template.md) — For quick tasks
- [Examples](../docs/examples/) — Real-world use cases


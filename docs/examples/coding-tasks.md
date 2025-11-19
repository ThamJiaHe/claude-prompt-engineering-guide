# Coding Tasks Examples

Real-world prompts for software development tasks using Claude.

---

## 1. Feature Implementation

### Scenario
Build a complete user authentication system with JWT tokens.

### Prompt

```xml
<system_prompt>
You are a senior full-stack engineer with 15 years of experience.
You specialize in authentication systems and security best practices.
</system_prompt>

<background>
We're building a SaaS application with:
- Node.js + Express backend
- React frontend
- PostgreSQL database
- 100K expected monthly users

We need:
- User registration and login
- JWT token-based auth
- Password reset functionality
- Email verification
</background>

<task>
<objective>Implement a complete authentication system</objective>
<constraints>
- Must follow OAuth2 best practices
- Passwords must be properly hashed (bcrypt)
- JWTs should expire after 1 hour
- Refresh tokens valid for 30 days
- All endpoints must be tested
- Must include proper error handling
</constraints>
</task>

<rules>
- Write tests FIRST (TDD approach)
- All code must be production-ready
- No TODO or placeholder comments
- Include logging for debugging
- Document API endpoints with examples
</rules>

<format>
Structure your implementation as:
1. Database schema (SQL)
2. Backend models and utilities
3. API endpoints with full implementation
4. Frontend components
5. Test suite
6. Setup/installation instructions
</format>
```

---

## 2. Bug Investigation & Fix

### Scenario
Intermittent authentication failures in production.

### Prompt

```xml
<system_prompt>
You are a debugging specialist with expertise in distributed systems.
</system_prompt>

<background>
Production Issue:
- Intermittent 401 errors on /api/user endpoint
- Affects 0.1% of requests (estimated)
- Correlates with high traffic periods
- User reports: "Sometimes I get logged out randomly"

Environment:
- Node.js backend with JWT auth
- Redis cache for session management
- 5 backend instances (load balanced)
- PostgreSQL database

Error Logs:
```
[14:23:45] 401 Unauthorized: Invalid or expired token
[14:23:46] 401 Unauthorized: Invalid or expired token
[14:25:12] 401 Unauthorized: Invalid or expired token
```
</background>

<task>
Investigate the root cause and provide a fix.
</task>

<rules>
- Identify the actual cause, not symptoms
- Propose a minimal, targeted fix
- Include how to verify the fix works
- Don't modify unrelated code
</rules>

<thinking>
Consider:
1. Why would tokens intermittently become invalid?
2. What's the difference during high traffic?
3. Are there time synchronization issues?
4. Could Redis cache expiration be involved?
5. Are all servers using the same signing key?
</thinking>

<format>
Provide:
1. Root cause analysis (with evidence)
2. Proposed fix (code)
3. How to verify it works
4. Monitoring to detect if issue recurs
</format>
```

---

## 3. Performance Optimization

### Scenario
Database queries are slow, affecting page load times.

### Prompt

```xml
<system_prompt>
You are a database performance expert.
</system_prompt>

<background>
Current Performance:
- Homepage loads in 3.2 seconds
- Target: <1 second
- Main bottleneck: Database queries
- Using PostgreSQL with 10M+ user records

Current queries:
[Paste your actual SQL queries]

Current indexes:
[Paste your current index definitions]

Traffic:
- 1M page views/day
- Peak: 500 concurrent users
</background>

<task>
Optimize database queries to improve page load time to <1 second.
</task>

<rules>
- Don't over-index (adds write overhead)
- Consider query patterns, not just individual queries
- Include before/after performance metrics
- No schema changes unless necessary
</rules>

<format>
Provide:
1. Query analysis (which are slow and why)
2. Recommended indexes
3. Query rewrites
4. Estimated performance improvement
5. Monitoring approach
</format>
```

---

## 4. Code Review

### Scenario
Review critical payment processing code.

### Prompt

```xml
<system_prompt>
You are a principal software engineer specializing in payment systems and security.
You have reviewed code at multiple fintech companies.
</system_prompt>

<background>
This code processes customer payments for our SaaS platform:
- Handles $50M+ annually
- Must be PCI-compliant
- Processes 10K payments/day
- Critical for business operations

Team context:
- 5 payment engineers
- Code will be audited by security team
- Must pass PCI compliance review
</background>

<task>
Review this code for:
1. Security vulnerabilities
2. PCI compliance issues
3. Error handling and edge cases
4. Performance concerns
5. Best practices
</task>

<rules>
- Identify ACTUAL issues, not nitpicks
- Categorize by severity: CRITICAL, HIGH, MEDIUM, LOW
- Provide specific line references
- Suggest concrete fixes
- Assume this will be security-audited later
</rules>

[PASTE CODE HERE]

<format>
Structure as:
**CRITICAL Issues** (with explanation and fix)
**HIGH Priority** (with explanation and fix)
**MEDIUM Priority** (brief summary)
**LOW Priority** (suggestions)
**Overall Assessment**
</format>
```

---

## 5. Architecture Design

### Scenario
Design a scalable real-time notification system.

### Prompt

```xml
<system_prompt>
You are a senior architect specializing in distributed systems.
</system_prompt>

<background>
Requirements:
- 10M users worldwide
- Real-time notifications (sub-second latency)
- 100K concurrent WebSocket connections
- Support for 5M+ notifications/day
- High availability (99.99% uptime)

Constraints:
- Budget: $50K/month
- Team: 8 engineers
- Must integrate with existing Node.js backend
- PostgreSQL for data storage
</background>

<task>
Design a scalable real-time notification system.
</task>

<rules>
- Consider cost efficiency
- Account for engineer expertise
- Include deployment strategy
- Plan for team organization
</rules>

<format>
Provide:
1. Architecture overview (with diagram description)
2. Technology choices and justification
3. Data flow explanation
4. Scaling strategy
5. Deployment approach
6. Cost estimation
7. Team structure recommendations
</format>
```

---

## 6. Testing Strategy

### Scenario
Improve test coverage and reliability.

### Prompt

```xml
<system_prompt>
You are a QA architect specializing in automated testing.
</system_prompt>

<background>
Current State:
- Test coverage: 45%
- Flaky tests: 15 known issues
- Test run time: 25 minutes
- Testing framework: Jest + Supertest
- Database: PostgreSQL (test instance)

Issues:
- Tests pass/fail randomly
- Tests are slow to run
- Coverage not increasing
- Hard to add new tests
</background>

<task>
Design a comprehensive testing strategy to improve:
1. Coverage to 80%+
2. Test stability (0 flaky tests)
3. Test speed (<10 minutes)
4. Test maintainability
</task>

<format>
Provide:
1. Root cause of flakiness
2. Recommended test structure
3. Database strategy for tests
4. Example tests for critical paths
5. CI/CD integration approach
6. Success metrics
</format>
```

---

## Tips for Coding Task Prompts

### ✅ DO:

- **Provide context** — Why does this matter? What's the business impact?
- **Be specific** — List exact requirements, not vague goals
- **Include constraints** — Budget, timeline, team size, performance requirements
- **Show code samples** — Real code snippets, not descriptions
- **Define success** — How will we know it's done?

### ❌ DON'T:

- **Be vague** — "Build an API" is too vague. "Build a REST API with user authentication and pagination" is better.
- **Forget constraints** — Cost, team size, and timeline matter!
- **Hide complexity** — Tell Claude about edge cases and gotchas upfront
- **Expect mind-reading** — Be explicit about your priorities

---

## Next Steps

1. **Pick a scenario** that matches your task
2. **Customize the prompt** with your actual code/requirements
3. **Add your data** — Real code, metrics, architecture
4. **Submit to Claude**
5. **Iterate** — Refine based on results

---

## See Also

- [Quick Start Guide](../quick-start.md)
- [Comprehensive Template](../../templates/comprehensive-prompt-template.md)
- [Claude Prompt Engineering Guide](../../Claude-Prompt-Guide.md)

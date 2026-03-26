---
name: "Cybersecurity Threat Modeling"
description: "STRIDE-based threat modeling for application architecture. Apply when designing new systems, reviewing architecture, or assessing security posture of existing applications."
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
version: 2.1.0
compatibility: Claude Opus 4.6, Sonnet 4.6, Claude Code v2.1.x
updated: 2026-03-26
---

# Cybersecurity Threat Modeling

Systematic threat identification using STRIDE methodology. Map threats to mitigations before writing code.

## Overview

This skill implements the **STRIDE threat model**:

| Category | Threat | Question |
|----------|--------|----------|
| **S** — Spoofing | Identity impersonation | Can an attacker pretend to be someone else? |
| **T** — Tampering | Data modification | Can an attacker modify data in transit or at rest? |
| **R** — Repudiation | Denying actions | Can a user deny performing an action? |
| **I** — Information Disclosure | Data leaks | Can sensitive data be exposed? |
| **D** — Denial of Service | Availability attacks | Can the service be made unavailable? |
| **E** — Elevation of Privilege | Unauthorized access | Can a user gain higher privileges? |

## When to Use

- Designing a new system or feature architecture
- Before a security review of existing code
- When adding new external integrations (APIs, webhooks, OAuth)
- When handling new categories of sensitive data
- Architecture review for compliance (SOC 2, HIPAA, PCI-DSS)
- After a security incident (retrospective threat modeling)

## Step 1: Identify Assets

List what needs protection:

```markdown
## Assets Inventory

| Asset | Sensitivity | Location |
|-------|:-----------:|----------|
| User credentials | Critical | PostgreSQL (encrypted) |
| Session tokens | High | Redis / cookies |
| Payment info | Critical | Stripe (delegated) |
| User PII (email, name) | High | PostgreSQL |
| API keys | Critical | Environment variables |
| Application logs | Medium | CloudWatch |
| Static assets | Low | CDN |
```

## Step 2: Map Data Flows

Identify trust boundaries and data movement:

```markdown
## Data Flow Diagram

Browser → [TLS] → CDN → [TLS] → Load Balancer → App Server → Database
                                                  ↓
                                         [TLS] → External APIs
                                                  ↓
                                         [TLS] → Payment Provider

Trust Boundaries:
1. Browser ↔ CDN (public internet)
2. CDN ↔ App Server (internal network)
3. App Server ↔ Database (VPC)
4. App Server ↔ External APIs (public internet)
```

## Step 3: Apply STRIDE to Each Component

### Spoofing Threats

| Component | Threat | Mitigation |
|-----------|--------|------------|
| Login endpoint | Credential stuffing | Rate limiting, MFA, breach detection |
| API tokens | Token theft via XSS | httpOnly cookies, CSP headers |
| Webhooks | Spoofed webhook calls | HMAC signature verification |
| OAuth | Token substitution | State parameter, PKCE flow |
| Email | Phishing with spoofed sender | DMARC, SPF, DKIM |

### Tampering Threats

| Component | Threat | Mitigation |
|-----------|--------|------------|
| API requests | Parameter manipulation | Server-side validation (Zod schemas) |
| Database | Direct DB modification | RLS policies, audit triggers |
| Config files | Unauthorized config changes | Immutable infrastructure, signed configs |
| Client state | LocalStorage/cookie tampering | Server-side session validation |
| File uploads | Malicious file content | Content type validation, virus scanning |

### Repudiation Threats

| Component | Threat | Mitigation |
|-----------|--------|------------|
| Admin actions | Deny performing destructive action | Immutable audit logs with user ID |
| Transactions | Deny initiating payment | Signed transaction records |
| Data changes | Deny modifying records | Database audit trail (created_by, updated_by) |
| API calls | Deny making API request | Request logging with authentication context |

### Information Disclosure Threats

| Component | Threat | Mitigation |
|-----------|--------|------------|
| Error responses | Stack trace leaks | Generic error messages in production |
| API responses | Over-fetching sensitive fields | Response DTOs, field-level access control |
| Logs | PII in log files | Log sanitization, PII masking |
| Source code | Exposed .env or config | .gitignore, secret scanning, pre-commit hooks |
| Database | SQL injection data exfiltration | Parameterized queries, WAF |
| Backups | Unencrypted backup access | Encrypted backups, access controls |

### Denial of Service Threats

| Component | Threat | Mitigation |
|-----------|--------|------------|
| API endpoints | Request flooding | Rate limiting, WAF, CDN |
| File uploads | Large file upload attacks | File size limits, streaming validation |
| Database | Expensive query attacks | Query timeouts, pagination limits |
| Auth endpoints | Account lockout abuse | Progressive delays, CAPTCHA |
| Webhooks | Webhook flood | Queue-based processing, deduplication |

### Elevation of Privilege Threats

| Component | Threat | Mitigation |
|-----------|--------|------------|
| User roles | Horizontal privilege escalation | Resource ownership checks on every request |
| Admin panel | Vertical privilege escalation | Role-based middleware, separate admin auth |
| API keys | Scope escalation | Least-privilege API key scopes |
| JWT claims | Token claim manipulation | Server-side claim validation, short expiry |
| File access | Path traversal | Sanitize paths, chroot, allowlist directories |

## Step 4: Risk Matrix

Prioritize threats by likelihood and impact:

```markdown
## Risk Assessment

| Threat | Likelihood | Impact | Risk Level | Priority |
|--------|:---------:|:------:|:----------:|:--------:|
| SQL injection | Medium | Critical | High | P1 |
| XSS via user content | High | High | High | P1 |
| Credential stuffing | High | High | High | P1 |
| SSRF via webhooks | Low | Critical | Medium | P2 |
| DoS on API | Medium | Medium | Medium | P2 |
| Log data exposure | Low | Medium | Low | P3 |
```

**Risk Level Formula:**
- Critical impact + High likelihood = **P1** (fix before shipping)
- Critical impact + Low likelihood = **P2** (fix within sprint)
- Medium impact + any likelihood = **P2-P3** (schedule fix)
- Low impact = **P3** (backlog)

## Step 5: Mitigation Plan

```markdown
## Mitigation Actions

### P1 — Must Fix Before Launch
- [ ] Implement parameterized queries everywhere (A03)
- [ ] Add CSP headers and sanitize user HTML output (A05)
- [ ] Deploy rate limiting on auth endpoints (A04)
- [ ] Enable MFA for admin accounts (A07)

### P2 — Fix Within Sprint
- [ ] Add SSRF protection on webhook processor (A10)
- [ ] Implement API rate limiting per key (A04)
- [ ] Add request signing for internal service calls (A08)

### P3 — Backlog
- [ ] Audit log PII masking review (A09)
- [ ] Implement log-based anomaly detection (A09)
```

## Template: Threat Model Document

```markdown
# Threat Model: [Feature/System Name]
**Date:** YYYY-MM-DD
**Author:** [Name]
**Reviewers:** [Names]

## 1. System Description
[One paragraph describing the system]

## 2. Assets
[Table of assets with sensitivity levels]

## 3. Data Flow Diagram
[ASCII or Mermaid diagram with trust boundaries]

## 4. STRIDE Analysis
[Tables for each STRIDE category]

## 5. Risk Matrix
[Prioritized risk assessment]

## 6. Mitigation Plan
[Prioritized action items with owners]

## 7. Residual Risks
[Risks accepted after mitigation, with justification]
```

## Integration with Other Skills

| After Threat Modeling | Use This Skill |
|----------------------|----------------|
| Found injection risks | [OWASP Security Audit](./owasp-security-audit-skill.md) |
| Need auth implementation | [Security & Compliance](./security-compliance.md) |
| Need to test security | [Testing Strategy](./testing-skill.md) |
| Need monitoring | [Monitoring & Logging](./monitoring-logging-skill.md) |

## Sources

- [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling)
- [STRIDE Model (Microsoft)](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats)
- [OWASP ASVS 5.0](https://owasp.org/www-project-application-security-verification-standard/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

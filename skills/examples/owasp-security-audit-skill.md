---
name: "OWASP Security Audit"
description: "Systematic security audit against OWASP Top 10:2025. Apply when reviewing code that handles authentication, user input, API endpoints, data storage, or any security-sensitive functionality."
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
version: 2.1.0
compatibility: Claude Opus 4.6, Sonnet 4.6, Claude Code v2.1.x
updated: 2026-03-26
---

# OWASP Security Audit

Systematic code audit against the OWASP Top 10:2025 vulnerability categories. Every security-sensitive code change must pass this checklist.

## Overview

This skill enforces a **mandatory 10-point security audit** based on the [OWASP Top 10:2025](https://owasp.org/Top10/):

1. A01 — Broken Access Control
2. A02 — Cryptographic Failures
3. A03 — Injection
4. A04 — Insecure Design
5. A05 — Security Misconfiguration
6. A06 — Vulnerable and Outdated Components
7. A07 — Identification and Authentication Failures
8. A08 — Software and Data Integrity Failures
9. A09 — Security Logging and Monitoring Failures
10. A10 — Server-Side Request Forgery (SSRF)

## When to Use

- Code that handles user authentication or sessions
- Any endpoint accepting user input
- Database queries with dynamic parameters
- File upload or download functionality
- API integrations with external services
- Cryptographic operations (hashing, signing, encryption)
- Admin panels or privilege-escalation-sensitive code
- Code that makes outbound HTTP requests

## A01: Broken Access Control

**Check:** Does every endpoint verify the user has permission to access the resource?

```typescript
// VULNERABLE: No authorization check
app.get('/api/users/:id', async (req, res) => {
  const user = await db.user.findUnique({ where: { id: req.params.id } });
  res.json(user);
});

// SECURE: Verify ownership or admin role
app.get('/api/users/:id', authenticate, async (req, res) => {
  const user = await db.user.findUnique({ where: { id: req.params.id } });

  if (user.id !== req.user.id && req.user.role !== 'admin') {
    return res.status(403).json({ error: 'Forbidden' });
  }

  res.json(user);
});
```

**Checklist:**
- [ ] Every endpoint has authentication middleware
- [ ] Authorization checks verify resource ownership
- [ ] Admin-only routes check role before processing
- [ ] CORS is configured to allow only trusted origins
- [ ] JWT tokens are validated on every request (not just present)
- [ ] Rate limiting is applied to sensitive endpoints

## A02: Cryptographic Failures

**Check:** Is sensitive data encrypted at rest and in transit?

```typescript
// VULNERABLE: Storing passwords with weak hashing
const hashedPassword = md5(password); // Never use MD5/SHA-1

// SECURE: Use argon2id or bcrypt with proper cost factor
import { hash, verify } from '@node-rs/argon2';

const hashedPassword = await hash(password, {
  memoryCost: 65536,
  timeCost: 3,
  parallelism: 4,
});

const isValid = await verify(hashedPassword, inputPassword);
```

**Checklist:**
- [ ] Passwords use argon2id or bcrypt (never MD5/SHA-1/SHA-256 alone)
- [ ] API keys and secrets are in environment variables, not code
- [ ] TLS 1.2+ enforced for all connections
- [ ] Sensitive data encrypted at rest (database column-level encryption)
- [ ] No secrets in logs, error messages, or stack traces
- [ ] Cryptographic keys rotated on a schedule

## A03: Injection

**Check:** Is all user input parameterized or sanitized before use?

```typescript
// VULNERABLE: SQL injection via string concatenation
const query = `SELECT * FROM users WHERE email = '${email}'`;

// SECURE: Parameterized queries (Prisma does this automatically)
const user = await prisma.user.findUnique({
  where: { email: sanitizedEmail },
});

// VULNERABLE: Command injection via string interpolation
// Using child_process.exec with user input allows shell injection

// SECURE: Use execFile with array arguments
// execFile('convert', [userFilename, 'output.pdf'])
// Array arguments prevent shell interpretation of special characters
```

**Checklist:**
- [ ] All SQL uses parameterized queries or ORM (Prisma, Drizzle)
- [ ] No string concatenation in database queries
- [ ] Shell commands use execFile() with array args, never string interpolation
- [ ] HTML output is escaped (React does this by default)
- [ ] `dangerouslySetInnerHTML` is never used with user input
- [ ] Email templates sanitize all interpolated values
- [ ] LDAP, XPath, and NoSQL queries use parameterized inputs

## A04: Insecure Design

**Check:** Does the system design prevent abuse by design?

```typescript
// SECURE: Rate limiting on login
import rateLimit from 'express-rate-limit';

const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 5, // 5 attempts per window
  message: 'Too many login attempts. Try again in 15 minutes.',
});

app.post('/api/auth/login', loginLimiter, loginHandler);

// SECURE: Account lockout after failed attempts
if (user.failedLoginAttempts >= 5) {
  throw new Error('Account locked. Contact support.');
}
```

**Checklist:**
- [ ] Rate limiting on authentication endpoints
- [ ] Account lockout after repeated failures
- [ ] Business logic validates impossible states (e.g., negative prices)
- [ ] Multi-step operations use CSRF tokens
- [ ] Password reset tokens expire (15-30 minutes)
- [ ] Sensitive operations require re-authentication

## A05: Security Misconfiguration

**Check:** Are security headers, defaults, and configurations hardened?

```typescript
// SECURE: Security headers with helmet
import helmet from 'helmet';

app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      imgSrc: ["'self'", "data:", "https:"],
    },
  },
  hsts: { maxAge: 31536000, includeSubDomains: true },
  referrerPolicy: { policy: 'strict-origin-when-cross-origin' },
}));
```

**Checklist:**
- [ ] Security headers set (CSP, HSTS, X-Frame-Options, X-Content-Type-Options)
- [ ] Debug mode disabled in production
- [ ] Default credentials changed
- [ ] Directory listing disabled
- [ ] Error pages don't leak stack traces or internal paths
- [ ] Unnecessary features and endpoints disabled
- [ ] HTTPS enforced everywhere (no HTTP fallback)

## A06: Vulnerable Components

**Check:** Are all dependencies up to date and vulnerability-free?

```bash
# Check for known vulnerabilities
pnpm audit

# Check for outdated packages
pnpm outdated

# Before installing any new package, verify it:
# 1. Check weekly downloads (>10K minimum)
# 2. Check last published date (<6 months)
# 3. Check GitHub stars and open issues
# 4. Check for known CVEs
```

**Checklist:**
- [ ] `pnpm audit` shows no critical or high vulnerabilities
- [ ] No packages with known CVEs in production dependencies
- [ ] Lock file (`pnpm-lock.yaml`) is committed and up to date
- [ ] New packages vetted before installation (downloads, recency, CVEs)
- [ ] Unused dependencies removed

## A07: Authentication Failures

**Check:** Is authentication implemented securely?

```typescript
// SECURE: Session configuration
const sessionConfig = {
  secret: process.env.SESSION_SECRET, // Strong random secret
  resave: false,
  saveUninitialized: false,
  cookie: {
    httpOnly: true,     // Prevent XSS access to cookies
    secure: true,       // HTTPS only
    sameSite: 'strict', // CSRF protection
    maxAge: 3600000,    // 1 hour expiry
  },
};
```

**Checklist:**
- [ ] Passwords have minimum complexity requirements (12+ chars)
- [ ] Multi-factor authentication available for sensitive accounts
- [ ] Session tokens are random, high-entropy, and server-validated
- [ ] Cookies: `httpOnly`, `secure`, `sameSite=strict`
- [ ] Sessions expire after inactivity (30-60 minutes)
- [ ] Password reset doesn't reveal whether email exists
- [ ] Brute force protection on all auth endpoints

## A08: Software Integrity Failures

**Check:** Is the software supply chain trusted?

```bash
# Lock file integrity — CI should fail if lock file is out of sync
pnpm install --frozen-lockfile  # In CI/CD only

# Subresource integrity for CDN resources (in HTML)
# <script src="https://cdn.example.com/lib.js"
#   integrity="sha384-abc123..."
#   crossorigin="anonymous"></script>
```

**Checklist:**
- [ ] CI uses `--frozen-lockfile` (no lock file modifications in CI)
- [ ] No `eval()`, `new Function()`, or dynamic code execution with user input
- [ ] Deserialization of user data uses safe parsers (Zod, JSON.parse with validation)
- [ ] CDN resources use Subresource Integrity (SRI) hashes
- [ ] CI/CD pipeline has code signing or approval gates
- [ ] No auto-merge of dependency updates without review

## A09: Logging & Monitoring

**Check:** Are security events logged and alerts configured?

```typescript
// SECURE: Log security events (without sensitive data)
logger.warn('Failed login attempt', {
  email: maskEmail(email),     // Never log full email/PII
  ip: req.ip,
  userAgent: req.headers['user-agent'],
  timestamp: new Date().toISOString(),
});

// SECURE: Log access control failures
logger.error('Unauthorized access attempt', {
  userId: req.user?.id,
  resource: req.path,
  method: req.method,
  ip: req.ip,
});
```

**Checklist:**
- [ ] Failed login attempts are logged
- [ ] Access control failures are logged
- [ ] Input validation failures are logged
- [ ] Logs never contain passwords, tokens, PII, or secrets
- [ ] Log retention meets compliance requirements
- [ ] Alerts configured for suspicious patterns (brute force, privilege escalation)

## A10: Server-Side Request Forgery (SSRF)

**Check:** Can users control URLs that the server fetches?

```typescript
// VULNERABLE: User controls the fetch URL
app.get('/api/preview', async (req, res) => {
  const response = await fetch(req.query.url); // SSRF vulnerability!
  res.json(await response.json());
});

// SECURE: Allowlist of permitted domains
const ALLOWED_DOMAINS = ['api.example.com', 'cdn.example.com'];

app.get('/api/preview', async (req, res) => {
  const url = new URL(req.query.url);

  if (!ALLOWED_DOMAINS.includes(url.hostname)) {
    return res.status(400).json({ error: 'Domain not allowed' });
  }

  // Also block internal IPs
  const ip = await dns.resolve(url.hostname);
  if (isPrivateIP(ip)) {
    return res.status(400).json({ error: 'Internal addresses not allowed' });
  }

  const response = await fetch(url.toString());
  res.json(await response.json());
});
```

**Checklist:**
- [ ] Server-side HTTP requests validate destination URLs
- [ ] Allowlist of permitted external domains
- [ ] Block requests to internal/private IP ranges (10.x, 172.16-31.x, 192.168.x, 127.x)
- [ ] Block requests to metadata endpoints (169.254.169.254)
- [ ] URL redirects don't allow open redirect to arbitrary domains
- [ ] Webhook URLs are validated against allowlists

## Quick Audit Checklist

Run this checklist on every security-relevant PR:

```markdown
## Security Audit — PR Checklist

### Access Control (A01)
- [ ] Every endpoint has auth middleware
- [ ] Resource ownership verified

### Crypto (A02)
- [ ] No secrets in code, logs, or errors
- [ ] Strong password hashing (argon2id/bcrypt)

### Injection (A03)
- [ ] All queries parameterized
- [ ] No shell string interpolation with user input

### Design (A04)
- [ ] Rate limiting on auth endpoints
- [ ] Business logic validates impossible states

### Config (A05)
- [ ] Security headers set
- [ ] Debug mode off in production

### Components (A06)
- [ ] pnpm audit clean
- [ ] No outdated packages with CVEs

### Auth (A07)
- [ ] Secure cookie flags set
- [ ] Session expiry configured

### Integrity (A08)
- [ ] Frozen lockfile in CI
- [ ] No eval() with user data

### Logging (A09)
- [ ] Security events logged
- [ ] No PII in logs

### SSRF (A10)
- [ ] Outbound URLs validated
- [ ] Internal IPs blocked
```

## Sources

- [OWASP Top 10:2025](https://owasp.org/Top10/)
- [OWASP Application Security Verification Standard (ASVS) 5.0](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [BehiSecc/awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills) — Security-focused skill collection

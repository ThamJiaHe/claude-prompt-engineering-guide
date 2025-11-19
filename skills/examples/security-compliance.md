---
name: "Security & Compliance"
description: "Implement authentication, authorization, encryption, audit logging, OWASP compliance. Apply when building admin features, handling sensitive data, validating input, or securing endpoints."
allowed-tools: Read, Write, Edit, Bash
version: 2.0.0
---

# Security & Compliance

Systematic security implementation ensuring data protection and threat prevention.

## Overview

This Skill enforces a **mandatory 5-step security audit workflow**:
1. Authentication Check (S-1, AP-1)
2. Authorization Check (S-8)
3. Data Protection (S-1, AP-4)
4. Audit Logging (AP-2, S-2)
5. Input Validation (S-6, C-10)

Apply when building admin features, handling sensitive data, or implementing security controls.

## Security Audit Workflow

**Before deploying security-critical code**:

### Step 1: Authentication (S-1, AP-1)

```ts
// ✅ GOOD: Verify authentication
export async function getAdminData(req: Request) {
  const session = await auth();
  
  if (!session) {
    throw new UnauthorizedError('Not authenticated');
  }

  return await db.sensitiveData.findAll();
}

// ❌ BAD: No authentication
export async function getAdminData(req: Request) {
  return await db.sensitiveData.findAll();
}
```

**Checklist**:
- [ ] All admin routes require authentication
- [ ] JWT tokens expire (15m access, 7d refresh)
- [ ] Passwords hashed with bcrypt (never plaintext)
- [ ] No hardcoded credentials
- [ ] Secrets in environment variables only

### Step 2: Authorization (AP-1, S-8)

```ts
// ✅ GOOD: Check role AND ownership
export async function updateContact(
  contactId: string,
  data: UpdateContactInput,
  userId: UserId
) {
  const contact = await db.contacts.findById(contactId);

  if (!contact) {
    throw new NotFoundError('Contact not found');
  }

  // Verify ownership
  if (contact.userId !== userId) {
    throw new ForbiddenError('Cannot update other user\'s contacts');
  }

  return await db.contacts.update(contactId, data);
}

// ❌ BAD: No ownership check
export async function updateContact(
  contactId: string,
  data: UpdateContactInput
) {
  return await db.contacts.update(contactId, data);
  // Any user can update any contact!
}
```

**Checklist**:
- [ ] Role-based access control (RBAC) implemented
- [ ] Resource-level ownership verified
- [ ] No hardcoded permissions
- [ ] Roles clearly defined

### Step 3: Data Protection (S-1, AP-4)

```ts
// ✅ GOOD: Encrypt sensitive data
const encrypted = crypto
  .createCipheriv('aes-256-gcm', key, iv)
  .update(sensitiveData)
  .final();

await db.users.update(userId, { ssn: encrypted });

// ❌ BAD: Store plaintext
await db.users.update(userId, { ssn: sensitiveData });

// ✅ GOOD: Never cache financial data in browser
export async function getFinancialReport(userId: UserId) {
  const response = await fetch('/api/financial-report', {
    headers: {
      'Cache-Control': 'no-store, no-cache, must-revalidate'
    }
  });

  // Don't store in localStorage
  // Don't store in state that persists
  return response.json();
}

// ❌ BAD: Caching sensitive data
localStorage.setItem('userBalance', userBalance);
```

**Checklist**:
- [ ] Sensitive data encrypted in transit (HTTPS)
- [ ] Sensitive data encrypted at rest
- [ ] Passwords hashed (bcrypt/argon2)
- [ ] No sensitive data in URLs or caches
- [ ] No financial data cached in browser

### Step 4: Audit Logging (AP-2, S-2)

```ts
// ✅ GOOD: Log admin actions with details
await auditLog.create({
  userId: requestingUserId,
  action: 'USER_DELETED',
  resourceType: 'User',
  resourceId: deletedUserId,
  changes: {
    name: user.name,
    email: user.email,
    role: user.role
  },
  timestamp: new Date()
});

// ✅ GOOD: Never log sensitive data
// Log includes: email, role, name (OK)
// Log excludes: password, ssn, creditCard (NEVER!)

// ❌ BAD: No logging
export async function deleteUser(userId) {
  await db.users.delete(userId);
  // No audit trail!
}

// ❌ BAD: Logging sensitive data
await auditLog.create({
  action: 'USER_LOGIN',
  password: userPassword,  // WRONG!
  ssn: user.ssn,          // WRONG!
  creditCard: payment.cardNumber  // WRONG!
});
```

**Checklist**:
- [ ] All admin actions logged (create, update, delete)
- [ ] Logs include: userId, action, timestamp, resourceId
- [ ] Logs immutable (cannot be deleted)
- [ ] No sensitive data in logs
- [ ] Logs reviewed regularly

### Step 5: Input Validation (S-6, C-10)

```ts
// ✅ GOOD: Validate on client AND server
import { z } from 'zod';

const CreateUserSchema = z.object({
  email: z.string().email('Invalid email'),
  name: z.string().min(1).max(255),
  role: z.enum(['admin', 'user', 'guest'])
});

export async function createUser(input: unknown) {
  // Validate structure and types
  const validated = CreateUserSchema.parse(input);

  // Sanitize text inputs
  const sanitized = {
    ...validated,
    name: DOMPurify.sanitize(validated.name)
  };

  // Additional validation
  const existing = await db.users.findUnique({
    where: { email: sanitized.email }
  });

  if (existing) {
    throw new ValidationError('Email already exists');
  }

  return await db.users.create(sanitized);
}

// ❌ BAD: No validation
export async function createUser(input: any) {
  return await db.users.create(input);
}
```

**Checklist**:
- [ ] Validation on client AND server
- [ ] Whitelist approach (allow specific, not exclude bad)
- [ ] Sanitize user input
- [ ] Reject oversized inputs
- [ ] Validate all data types

## OWASP Top 10 Compliance (S-4)

### 1. Injection Prevention

```ts
// ❌ BAD: SQL Injection
const query = `SELECT * FROM users WHERE email = '${userInput.email}'`;

// ✅ GOOD: Parameterized queries
const user = await db.users.findUnique({
  where: { email: userInput.email }
});
```

### 2. Broken Authentication

Already covered (use bcrypt, JWT expiration, etc.)

### 3. Sensitive Data Exposure

Already covered (encryption, HTTPS, no caching)

### 4. XXE (XML External Entities)

```ts
// ✅ GOOD: Disable external entities
const parser = new xml2js.Parser({
  strict: true,
  doctype: false
});
```

### 5. Access Control

Already covered (RBAC, ownership checks)

### 6. Security Misconfiguration

```ts
// ✅ GOOD: Security headers
export const securityHeaders = {
  'X-Frame-Options': 'DENY',
  'X-Content-Type-Options': 'nosniff',
  'Strict-Transport-Security': 'max-age=31536000'
};
```

### 7. XSS (Cross-Site Scripting)

```tsx
// ✅ GOOD: React escapes by default
<p>{userComment}</p>

// ✅ GOOD: Escape custom output
<p>{escapeHtml(userBio)}</p>

// ❌ BAD: Dangerous HTML rendering
<p dangerouslySetInnerHTML={{ __html: userComment }} />
```

### 8. Insecure Deserialization

```ts
// ❌ BAD: Unsafe deserialization
const obj = eval(userInput);
const obj = Function(userInput)();

// ✅ GOOD: Safe JSON parsing
const obj = JSON.parse(userInput);
```

### 9. Using Components with Known Vulnerabilities

```bash
npm audit
npm audit fix
```

### 10. Insufficient Logging & Monitoring

Already covered (audit logging)

## Feature Flags for Risk (S-9)

```ts
// ✅ GOOD: Feature flag for risky features
const isNewPaymentSystemEnabled = await getFeatureFlag(
  'new-payment-system',
  userId
);

if (isNewPaymentSystemEnabled) {
  await newPaymentProcessor.process(payment);
} else {
  await legacyPaymentProcessor.process(payment);
}
```

## Rate Limiting

```ts
// ✅ GOOD: Rate limit by IP
import rateLimit from 'express-rate-limit';

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  keyGenerator: (req) => req.ip
});

app.use('/api/', limiter);

// ✅ GOOD: Stricter limit for auth
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,  // 5 attempts per 15 min
  skipSuccessfulRequests: true
});

app.post('/login', authLimiter, loginHandler);
```

## Anti-Patterns

```ts
// ❌ No authentication
export async function deleteUser(userId) { }

// ❌ Hardcoded secrets
const apiKey = 'sk-1234567890';

// ❌ Storing plaintext passwords
user.password = userInput.password;

// ❌ Logging sensitive data
console.log('User login:', { email, password, ssn });

// ❌ No encryption for sensitive data
db.users.update({ ssn: userSsn });

// ❌ No rate limiting
app.post('/login', loginHandler);

// ❌ Returning detailed errors
res.status(500).json({ error: error.message });  // Exposes internals
```

## Verification Before Deployment

Before deploying security-critical code:

- [ ] **S-1 (MUST)**: Sensitive data encrypted in transit and at rest
- [ ] **S-2 (MUST)**: No sensitive information in logs
- [ ] **S-3 (MUST)**: All admin actions auditable
- [ ] **S-4 (MUST)**: OWASP Top 10 compliance verified
- [ ] **S-5 (MUST)**: Secrets in environment variables (not code)
- [ ] **S-6 (MUST)**: All input validated and sanitized
- [ ] **S-7 (MUST)**: Destructive actions require confirmation
- [ ] **S-8 (SHOULD)**: RBAC implemented
- [ ] **S-9 (SHOULD)**: Feature flags for risky features
- [ ] **S-10 (MUST)**: Security code reviewed carefully
- [ ] **AP-1 (MUST)**: Admin routes require auth/authz
- [ ] **AP-2 (MUST)**: Admin actions logged
- [ ] HTTPS enabled
- [ ] Dependencies audited
- [ ] Rate limiting configured

## Integration with CLAUDE.md

Enforces CLAUDE.md Section 10 & 8:
- **S-1 through S-10**: Security standards
- **AP-1 through AP-9**: Admin security

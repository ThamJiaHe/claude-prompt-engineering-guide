---
name: "API Security Hardening"
description: "Harden REST and GraphQL APIs against common attack vectors. Apply when building API endpoints, implementing authentication, handling file uploads, or exposing APIs to external consumers."
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
version: 2.1.0
compatibility: Claude Opus 4.6, Sonnet 4.6, Claude Code v2.1.x
updated: 2026-03-26
---

# API Security Hardening

Secure REST and GraphQL APIs against OWASP API Security Top 10 threats.

## When to Use

- Building new API endpoints
- Adding authentication/authorization to APIs
- Exposing APIs to external consumers or partners
- Implementing file upload endpoints
- Handling payment or sensitive data via API
- Integrating third-party webhooks

## Authentication Patterns

### JWT Best Practices

```typescript
import jwt from 'jsonwebtoken';

// Token generation
function generateTokens(userId: string) {
  const accessToken = jwt.sign(
    { sub: userId, type: 'access' },
    process.env.JWT_SECRET!,
    { expiresIn: '15m', algorithm: 'HS256' }
  );

  const refreshToken = jwt.sign(
    { sub: userId, type: 'refresh' },
    process.env.JWT_REFRESH_SECRET!,
    { expiresIn: '7d', algorithm: 'HS256' }
  );

  return { accessToken, refreshToken };
}

// Token validation middleware
function authenticate(req: Request, res: Response, next: NextFunction) {
  const token = req.headers.authorization?.replace('Bearer ', '');

  if (!token) {
    return res.status(401).json({ error: 'Missing token' });
  }

  try {
    const payload = jwt.verify(token, process.env.JWT_SECRET!, {
      algorithms: ['HS256'], // Prevent algorithm confusion
    });

    if (payload.type !== 'access') {
      return res.status(401).json({ error: 'Invalid token type' });
    }

    req.user = payload;
    next();
  } catch {
    return res.status(401).json({ error: 'Invalid token' });
  }
}
```

### API Key Security

```typescript
// Hash API keys before storing (never store plaintext)
import { createHash } from 'crypto';

function hashApiKey(key: string): string {
  return createHash('sha256').update(key).digest('hex');
}

// Validate with constant-time comparison
import { timingSafeEqual } from 'crypto';

function validateApiKey(provided: string, stored: string): boolean {
  const a = Buffer.from(hashApiKey(provided));
  const b = Buffer.from(stored);
  return a.length === b.length && timingSafeEqual(a, b);
}
```

## Input Validation

### Zod Schema Validation

```typescript
import { z } from 'zod';

// Define strict schemas for every endpoint
const createUserSchema = z.object({
  email: z.string().email().max(255),
  name: z.string().min(1).max(100).trim(),
  role: z.enum(['user', 'admin']).default('user'),
  age: z.number().int().min(13).max(150).optional(),
});

// Validate in middleware
function validate(schema: z.ZodSchema) {
  return (req: Request, res: Response, next: NextFunction) => {
    const result = schema.safeParse(req.body);
    if (!result.success) {
      return res.status(400).json({
        error: 'Validation failed',
        details: result.error.flatten(),
      });
    }
    req.body = result.data; // Use validated data only
    next();
  };
}

app.post('/api/users', validate(createUserSchema), createUser);
```

## Rate Limiting

```typescript
import rateLimit from 'express-rate-limit';

// Global rate limit
const globalLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  standardHeaders: true,
  legacyHeaders: false,
});

// Strict limit for auth endpoints
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,
  message: { error: 'Too many attempts. Try again later.' },
});

// Per-API-key limit
const apiKeyLimiter = rateLimit({
  windowMs: 60 * 1000,
  max: 60, // 60 requests per minute
  keyGenerator: (req) => req.headers['x-api-key'] || req.ip,
});

app.use(globalLimiter);
app.use('/api/auth', authLimiter);
app.use('/api/v1', apiKeyLimiter);
```

## Response Security

```typescript
// Never leak internal details
// VULNERABLE:
res.status(500).json({ error: err.message, stack: err.stack });

// SECURE:
res.status(500).json({ error: 'Internal server error' });
logger.error('Unhandled error', { error: err, requestId: req.id });

// Pagination to prevent data dumps
const MAX_PAGE_SIZE = 100;
const pageSize = Math.min(req.query.limit || 20, MAX_PAGE_SIZE);

// Field filtering to prevent over-fetching
const userResponse = {
  id: user.id,
  name: user.name,
  email: user.email,
  // Never include: passwordHash, internalNotes, etc.
};
```

## Security Headers

```typescript
// Essential headers for API responses
app.use((req, res, next) => {
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('Strict-Transport-Security', 'max-age=31536000; includeSubDomains');
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('Pragma', 'no-cache');
  next();
});
```

## CORS Configuration

```typescript
import cors from 'cors';

// SECURE: Explicit origin allowlist
app.use(cors({
  origin: ['https://myapp.com', 'https://admin.myapp.com'],
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true,
  maxAge: 86400,
}));

// VULNERABLE: Never do this in production
// app.use(cors({ origin: '*' }));
```

## Webhook Security

```typescript
import { createHmac } from 'crypto';

// Verify webhook signatures
function verifyWebhookSignature(
  payload: string,
  signature: string,
  secret: string,
): boolean {
  const expected = createHmac('sha256', secret)
    .update(payload)
    .digest('hex');

  return timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(`sha256=${expected}`),
  );
}

app.post('/api/webhooks/stripe', (req, res) => {
  const signature = req.headers['stripe-signature'];
  if (!verifyWebhookSignature(req.rawBody, signature, process.env.STRIPE_WEBHOOK_SECRET!)) {
    return res.status(401).json({ error: 'Invalid signature' });
  }
  // Process webhook...
});
```

## API Security Checklist

```markdown
- [ ] All endpoints require authentication (except public ones)
- [ ] Authorization checks on every resource access
- [ ] Input validated with Zod schemas on every endpoint
- [ ] Rate limiting configured (global + per-endpoint)
- [ ] Response filtering (no internal data leaks)
- [ ] Security headers set
- [ ] CORS restricted to known origins
- [ ] JWT: short expiry, algorithm pinned, refresh token rotation
- [ ] API keys: hashed storage, scoped permissions, rotation support
- [ ] Webhooks: HMAC signature verification
- [ ] File uploads: type validation, size limits, virus scanning
- [ ] Logging: security events logged, no PII in logs
- [ ] Error responses: generic messages, no stack traces
- [ ] HTTPS enforced, no HTTP fallback
```

## Sources

- [OWASP API Security Top 10](https://owasp.org/API-Security/)
- [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
- [JWT Best Practices (RFC 8725)](https://datatracker.ietf.org/doc/html/rfc8725)

---
name: "Code Review"
description: "Systematically review PRs for security, testing, code quality, accessibility. Apply when reviewing pull requests, auditing endpoints, checking security controls, or verifying test coverage."
allowed-tools: Read, Grep, Edit
version: 2.1.0
compatibility: Claude Opus 4.5, Claude Code v2.x
updated: 2026-01-24
---

# Code Review

Systematic pull request review workflow covering security, testing, quality, and accessibility.

## Overview

This Skill enforces a **5-step review process**:
1. Pre-review (CI passing, branch naming)
2. Security audit (auth, logging, validation)
3. Testing verification (coverage, quality)
4. Code quality (types, patterns, organization)
5. Accessibility verification (WCAG, keyboard, screen readers)

Apply when reviewing PRs or auditing code before merge.

## Pre-Review Checklist

Stop if these fail:

- [ ] CI checks pass (prettier, eslint, TypeScript, tests)
- [ ] Branch name follows conventions (feature/*, fix/*, hotfix/*)
- [ ] All commits use Conventional Commits format
- [ ] PR description clearly explains what changed and why
- [ ] Related issues linked (Closes #123)

## Step 1: Security Audit

**Mandatory security checks** (AP-1 through AP-10):

### Authentication & Authorization

- [ ] **AP-1 (MUST)**: All admin routes require authentication
- [ ] **AP-1 (MUST)**: All admin routes check authorization (role/permission)
- [ ] Token validation (JWT expiration, signature)
- [ ] No hardcoded credentials or API keys
- [ ] Secrets in environment variables only

**Anti-pattern**:

```ts
// ❌ No auth check
export async function getAdminData(req) {
  return await db.sensitiveData.findAll();
}

// ✅ Correct
export async function getAdminData(req) {
  const user = await verifyAuth(req);
  if (user.role !== 'admin') throw new ForbiddenError();
  return await db.sensitiveData.findAll();
}
```

### Audit Logging

- [ ] **AP-2 (MUST)**: All admin actions (create, update, delete) logged
- [ ] Log includes: userId, action, timestamp, resourceId, changes
- [ ] Logs immutable (cannot be modified)
- [ ] **AP-9 (MUST)**: No sensitive data in logs (passwords, PII, financial)

### Data Validation

- [ ] **C-10 (MUST)**: Validated on client AND server
- [ ] **AP-8 (MUST)**: Form input validated both sides
- [ ] Whitelist allowed values (not blacklist bad ones)
- [ ] Rejects oversized inputs

### Error Messages

- [ ] **AP-9 (MUST)**: No sensitive information exposed
- [ ] User-friendly messages (not stack traces)
- [ ] No database schema leaked
- [ ] No system paths exposed

### Encryption

- [ ] **S-1 (MUST)**: HTTPS for all requests
- [ ] **S-1 (MUST)**: Passwords hashed (bcrypt/argon2)
- [ ] Sensitive data encrypted at rest
- [ ] **AP-4 (MUST)**: Financial data from backend only (never cached)

## Step 2: Testing Verification

**Coverage requirements**:

- [ ] **T-1 (MUST)**: Tests colocated with source
- [ ] **T-2 (MUST)**: API changes have integration tests
- [ ] **T-3 (MUST)**: Logic separated from database tests
- [ ] **T-7 (MUST)**: E2E tests for critical admin flows
- [ ] **T-8 (MUST)**: Edge cases tested
- [ ] Coverage meets minimums (80% utils, 90% logic, 100% admin)

**Test Quality Checks**:

- [ ] Tests describe what they verify (not `test('user')`)
- [ ] No magic numbers (parameterized inputs)
- [ ] Entire structures compared (not individual fields)
- [ ] Tests independent (no test depends on another)
- [ ] No excessive mocking of business logic

**Anti-pattern**:

```ts
// ❌ BAD: Trivial test
test('user', () => {
  const user = createUser('Alice');
  expect(user.id).toBeTruthy();
});

// ✅ GOOD: Clear and comprehensive
test('creates user with required fields', () => {
  const user = createUser('Alice');
  expect(user).toEqual({
    id: expect.any(String),
    name: 'Alice',
    createdAt: expect.any(Date)
  });
});
```

## Step 3: Code Quality

### TypeScript & Types

- [ ] **C-5 (MUST)**: Branded types used for IDs (not string)
- [ ] **C-6 (MUST)**: Type-only imports use `import type`
- [ ] **G-3 (MUST)**: TypeScript compiles without errors
- [ ] No unnecessary `as` type casts
- [ ] Generics used appropriately

### Function Design

- [ ] **C-4 (SHOULD)**: Functions simple and composable
- [ ] **C-3 (SHOULD NOT)**: No classes when functions suffice
- [ ] Single responsibility principle
- [ ] **C-9 (SHOULD NOT)**: Extracted functions reused or improve readability

### Comments & Documentation

- [ ] **C-7 (SHOULD NOT)**: Only comments for critical caveats
- [ ] Code is self-explanatory
- [ ] Function names describe purpose
- [ ] No redundant comments

**Anti-pattern**:

```ts
// ❌ BAD: Class for simple task
class EmailValidator {
  validate(email: string): boolean {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }
}

// ✅ GOOD: Pure function
function isValidEmail(email: string): boolean {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

// ❌ BAD: Obvious comment
// Loop through users
users.forEach(user => {
  // Check if active
  if (user.active) {
    // Add to results
    results.push(user);
  }
});
```

### Organization

- [ ] **O-1 (MUST)**: Shared components in src/components/ only if used ≥2 places
- [ ] **O-2 (MUST)**: Admin pages in src/pages/admin/
- [ ] **O-3 (MUST)**: Admin routes in server/routes/admin
- [ ] **O-4 (SHOULD)**: Business logic in services, not components
- [ ] **D-1 (MUST)**: Models defined in server/models/
- [ ] File organization logical and consistent

### Tooling Gates

- [ ] **G-1 (MUST)**: prettier --check passes
- [ ] **G-2 (MUST)**: eslint passes
- [ ] **G-3 (MUST)**: TypeScript compiles
- [ ] **G-4 (MUST)**: npm audit passes (no critical vulnerabilities)
- [ ] **G-5 (MUST)**: No type errors ignored

## Step 4: Database & Migrations

- [ ] **D-1 (MUST)**: Models in server/models/
- [ ] **D-2 (MUST)**: Data validated at API and DB layers
- [ ] **D-3 (SHOULD)**: Schema changes use migrations
- [ ] Migration reversible (down migration exists)
- [ ] No breaking changes without backward compatibility
- [ ] Indexes on frequently queried columns

## Step 5: Accessibility

- [ ] **U-1 (MUST)**: WCAG 2.1 AA compliant
- [ ] **U-2 (SHOULD)**: Keyboard navigation works
- [ ] **AP-6 (MUST)**: Admin portal accessible
- [ ] **AP-7 (SHOULD)**: Admin features keyboard accessible
- [ ] Form labels associated with inputs
- [ ] Error messages announce to screen readers
- [ ] 4.5:1 contrast ratio verified
- [ ] Color not only indicator of status
- [ ] **U-5 (MUST)**: Destructive actions require confirmation
- [ ] **U-6 (SHOULD)**: Undo available for destructive actions

**Anti-pattern**:

```tsx
// ❌ BAD: No label
<input type="email" placeholder="Email" />

// ❌ BAD: Color-only status
<div style={{ color: error ? 'red' : 'green' }}>Status</div>

// ❌ BAD: No confirmation for delete
<button onClick={() => deleteUser()}>Delete</button>

// ✅ GOOD: Complete accessibility
<label htmlFor="email">Email</label>
<input id="email" type="email" aria-invalid={!!error} />
{error && <p id="error" role="alert">{error}</p>}
```

## Review Comment Templates

### ✅ Approving

```
Security verified, tests comprehensive, code follows standards.
Ready to merge.
```

### 🔒 Security Issue

```
AUTH REQUIRED: Endpoint missing authentication check.
See CLAUDE.md AP-1.

Example:
const user = await verifyAuth(req);
if (user.role !== 'admin') throw new ForbiddenError();
```

### 🧪 Testing Gap

```
TESTS MISSING: Admin deletion flow needs E2E test confirming
the deletion confirmation dialog.

Add to src/tests/e2e/admin.test.ts:
- Test that delete button opens confirmation
- Test that clicking "Cancel" keeps user
- Test that clicking "Confirm" deletes user
```

### 💡 Suggestion

```
Consider pagination for the user list query.
Loading 1000+ records could be slow.

pnpm test --coverage src/utils/
```

## Verification Before Approval

Approve only when:

- [ ] All 5 steps complete (security, testing, quality, db, a11y)
- [ ] All blocking issues resolved
- [ ] CI checks pass (green)
- [ ] No sensitive data in logs or errors
- [ ] Destructive actions have confirmation
- [ ] TypeScript compiles
- [ ] Tests comprehensive

## Approval Template

```
✅ Code reviewed and approved.

Security:
- Auth/authz verified
- Audit logging present
- Input validation on both sides
- No sensitive data logged

Testing:
- Tests colocated
- Coverage adequate
- E2E for admin flows
- Edge cases covered

Quality:
- Types correct
- Code organization logical
- Functions simple
- Standards followed

Ready to merge.
```

## Rejection Template

```
🔴 Changes required before approval.

1. MUST FIX - Security:
   Endpoint missing authorization check (AP-1).
   Add role verification before processing.

2. MUST FIX - Testing:
   Admin deletion needs E2E test confirming
   the confirmation dialog (T-7).

3. SHOULD FIX - Quality:
   Use branded UserId type instead of string (C-5).

Please address and re-request review.
```

## Integration with CLAUDE.md

Enforces CLAUDE.md Section 2 & 8-10:
- **C-1 through C-15**: Code while coding standards
- **T-1 through T-10**: Testing standards
- **O-1 through O-5**: Organization
- **G-1 through G-5**: Tooling
- **AP-1 through AP-10**: Admin portal security
- **U-1 through U-6**: UX/accessibility
- **S-1 through S-10**: Security
---

**Last Updated:** January 24, 2026
**Compatibility:** Claude Opus 4.5, Claude Code v2.x
**Status:** Production Ready

> **January 2026 Update:** This skill is compatible with Claude Opus 4.5 and Claude Code v2.x. For complex tasks, use the `effort: high` parameter for thorough analysis.

---
name: "TypeScript & Coding Standards"
description: "Enforce TypeScript best practices, branded types for IDs, import organization, naming conventions. Apply when writing functions, choosing type patterns, naming variables, organizing code, or structuring projects."
allowed-tools: Read, Write, Edit
version: 2.1.0
compatibility: Claude Opus 4.5, Claude Code v2.x
updated: 2026-01-24
---

# TypeScript & Coding Standards

Systematic TypeScript and naming conventions ensuring type safety and code clarity.

## Overview

This Skill enforces:
- Branded types for all IDs (C-5)
- Type-only imports (C-6)
- Simple, composable functions (C-4)
- Minimal comments (C-7)
- Clear naming conventions
- Organized file structure

Apply when writing TypeScript code, choosing type patterns, or structuring projects.

## Branded Types for IDs

**C-5 (MUST)**: Never use raw strings for IDs. Use branded types.

### Why Branded Types

Prevents mixing incompatible IDs:

```ts
// ❌ BAD: No type safety, can mix IDs
type UserId = string;
type ContactId = string;

function getUser(id: UserId) { }
function getContact(id: ContactId) { }

// No type error - oops!
const contactId: ContactId = '123';
getUser(contactId);  // Wrong type passed!
```

### Using Branded Types

```ts
// Define Brand helper once
type Brand<T, B extends string> = T & { readonly __brand: B };

export function createBrand<T, B extends string>(value: T): Brand<T, B> {
  return value as Brand<T, B>;
}

// Create branded types
type UserId = Brand<string, 'UserId'>;
type ContactId = Brand<string, 'ContactId'>;
type ProjectId = Brand<string, 'ProjectId'>;

// Usage (type-safe)
const userId = createBrand<string, 'UserId'>('123');
const contactId = createBrand<string, 'ContactId'>('456');

function getUser(id: UserId) { }
function getContact(id: ContactId) { }

getUser(userId);      // ✅ OK
getUser(contactId);   // ❌ Type error!
```

## Type vs Interface Decision

**C-8 (SHOULD)**: Default to `type`. Use `interface` only when necessary.

### Decision Tree

```
Does it need declaration merging?
├─ YES → use interface
└─ NO → use type

Is it a class implementation?
├─ YES → use interface
└─ NO → use type

Need union or intersection?
├─ YES → use type
└─ NO → type or interface (choose type for consistency)
```

### Examples

```ts
// ✅ USE TYPE (most cases)
type User = {
  id: UserId;
  email: string;
  name: string;
};

type Response<T> = {
  status: number;
  data: T;
};

type Status = 'active' | 'inactive' | 'banned';

// ✅ USE INTERFACE (when merging)
interface Window {
  myCustomProperty?: string;
}

// Your code extends library interface
interface Window {
  myCustomProperty: string;
}

// ✅ USE INTERFACE (class implementation)
interface Logger {
  log(message: string): void;
}

class ConsoleLogger implements Logger {
  log(message: string) { console.log(message); }
}
```

## Import Organization

**C-6 (MUST)**: Use `import type` for type-only values.

### Organization Template

```ts
// 1. React and external libraries
import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/router';

// 2. Type imports from external libraries
import type { ApiResponse } from 'external-lib';

// 3. Internal absolute imports
import { userService } from '@/services/user';
import { Button } from '@/components/ui/Button';

// 4. Type imports from internal modules
import type { User } from '@/lib/types';
import type { UserId } from '@/lib/branded';

// 5. Relative imports
import { helper } from '../utils/helper';
import type { Config } from './config';

// 6. Side effects last
import './styles.css';
```

### Anti-Pattern

```ts
// ❌ BAD: Runtime import of types
import { User, Address, ApiResponse } from './types';

// ✅ GOOD: Separate type imports
import type { User, Address, ApiResponse } from './types';
```

## Naming Conventions

### Variables and Constants

```ts
// ✅ GOOD: Clear, domain-specific names
const maxRetries = 3;
const isUserAuthenticated = true;
const userRegistrationDate = new Date();
const companyVerificationScore = 0.95;

// ❌ BAD: Ambiguous or cryptic
const mr = 3;  // What is mr?
const auth = true;  // Is it authenticated or authenticates?
const ud = new Date();  // What is ud?
const v = 0.95;  // What does v represent?
```

### Functions and Methods

Use **verb + noun** describing the action:

```ts
// ✅ GOOD: Clear action
function validateEmail(email: string): boolean { }
function fetchUserById(id: UserId): Promise<User> { }
function calculateTotal(items: Item[]): number { }
function setUserPreferences(prefs: UserPrefs): void { }
function isExpired(date: Date): boolean { }
function hasPermission(user: User, action: string): boolean { }

// ❌ BAD: Vague
function process(data: any): any { }
function handle(input: string): void { }
function do(x: number): number { }
function get(id: string): any { }
```

### Booleans

Prefix with **is/has/can/should**:

```ts
// ✅ GOOD: Clear boolean meaning
const isActive = true;
const hasPermission = false;
const canDelete = user.role === 'admin';
const shouldRetry = attempt < maxRetries;

function isValidEmail(email: string): boolean { }
function hasUserConfirmed(userId: UserId): boolean { }
function canAccessResource(user: User, resource: string): boolean { }

// ❌ BAD: Ambiguous
const active = true;  // State or action?
const permission = false;  // What permission?
const deleted = true;  // Is deleted or should delete?
```

### Types and Interfaces

Use **PascalCase**, describe what it is:

```ts
// ✅ GOOD: Clear type names
type User = { id: UserId; name: string };
type CreateUserRequest = { name: string; email: string };
type UserValidationError = Error & { field: string };
type ApiResponse<T> = { status: number; data: T };

// ❌ BAD: Unclear or redundant
type user = { };  // Should be PascalCase
type IUser = { };  // Don't use "I" prefix (Hungarian notation)
type UserType = { };  // Don't add "Type" suffix (it's obvious)
type UserData = { };  // Vague ("data" is meaningless)
```

### Constants

```ts
// ✅ GOOD: Configuration constants in CONSTANT_CASE
export const MAX_RETRIES = 3;
export const DEFAULT_TIMEOUT_MS = 5000;
export const PAGINATION_LIMIT = 20;

// ✅ GOOD: Regular case for non-configuration
const ValidationRules = {
  email: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
  phone: /^\d{10}$/
};

// ❌ BAD: All caps when not configuration
const USERS_PER_PAGE = 20;  // OK for configuration
const ALL_CAPS_FOR_EVERYTHING = true;  // Excessive
```

## Function Design

### Single Responsibility

Each function should do **one thing well**:

```ts
// ❌ BAD: Does too much
function processUserData(userId: string) {
  const user = db.users.find(userId);
  const total = user.transactions.reduce((sum, t) => sum + t.amount, 0);
  const formatted = `${user.name}: $${total}`;
  console.log(formatted);
  return formatted;
}

// ✅ GOOD: Separate concerns
function getUserWithTotal(userId: UserId): { user: User; total: number } {
  const user = db.users.find(userId);
  const total = user.transactions.reduce((sum, t) => sum + t.amount, 0);
  return { user, total };
}

function formatUserSummary(user: User, total: number): string {
  return `${user.name}: $${total}`;
}

function logUserSummary(summary: string): void {
  console.log(summary);
}
```

### Pure Functions Over Classes

**C-4 (SHOULD)**: Prefer composable functions:

```ts
// ❌ BAD: Class for simple task
class EmailValidator {
  private pattern: RegExp;
  constructor() {
    this.pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  }
  validate(email: string): boolean {
    return this.pattern.test(email);
  }
}

// ✅ GOOD: Pure function
const EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function isValidEmail(email: string): boolean {
  return EMAIL_PATTERN.test(email);
}

// Easy to test, compose, reuse
```

### Parameter Order

```ts
// ✅ GOOD: Required first, optional last
function createUser(
  email: string,
  name: string,
  options?: { role?: string; isAdmin?: boolean }
): User { }

// ✅ GOOD: Data first, then callbacks
function processItems(
  items: Item[],
  onProgress?: (count: number) => void
): Result { }

// ❌ BAD: Optional before required
function createUser(
  options?: { role?: string },
  email: string,
  name: string
): User { }
```

## Comments & Documentation

**C-7 (SHOULD NOT)**: Only comments for critical caveats.

### When to Comment

```ts
// ✅ GOOD: Critical caveat explains non-obvious behavior
// NOTE: User ID format changed from UUID to Snowflake in migration #42.
// Old records may have UUID format. This function handles both.
function parseUserId(id: string): UserId {
  if (uuid.validate(id)) {
    return createBrand<string, 'UserId'>(uuidToSnowflake(id));
  }
  return createBrand<string, 'UserId'>(id);
}

// ✅ GOOD: TODO when incomplete
// TODO: Add rate limiting to prevent abuse (issue #523)
function sendEmail(to: string, subject: string): Promise<void> {
  return mailService.send(to, subject);
}

// ❌ BAD: Obvious comment
// Get the user
const user = getUserById(userId);

// ❌ BAD: Redundant comment
// Loop through users
users.forEach(user => {
  // Check if active
  if (user.active) {
    // Add to results
    results.push(user);
  }
});
```

### JSDoc for Public APIs

```ts
// ✅ GOOD: Document public function
/**
 * Validates email format using RFC 5322 standard.
 * @param email - Email address to validate
 * @returns True if valid, false otherwise
 */
export function isValidEmail(email: string): boolean {
  return EMAIL_PATTERN.test(email);
}

// ❌ BAD: Over-comment obvious function
/**
 * Gets a user by ID
 * @param id - The user ID
 * @returns The user or null
 */
function getUserById(id: UserId): User | null {
  return db.users.find(u => u.id === id);
}
```

## Code Organization

### File Structure

```
src/
├── components/
│   ├── ui/               # Reusable UI primitives
│   │   ├── Button.tsx
│   │   ├── Modal.tsx
│   │   └── Input.tsx
│   ├── admin/            # Admin-only components
│   │   ├── UserList.tsx
│   │   └── AuditLog.tsx
│   └── Common.tsx        # Only if used by 2+ features
├── services/             # Business logic
│   ├── user.service.ts
│   └── auth.service.ts
├── lib/
│   ├── branded.ts        # Branded types
│   └── api.ts            # API client
└── types/
    └── index.ts          # Central type definitions
```

### Colocation

```
// ✅ GOOD: Related files together
Button.tsx
Button.module.css
Button.test.ts
Button.stories.tsx

// ❌ BAD: Scattered
src/components/Button.tsx
src/styles/button.css
src/tests/button.test.ts
src/types/button-types.ts
```

## Error Handling

```ts
// ✅ GOOD: Typed error handling
class ValidationError extends Error {
  constructor(public field: string, message: string) {
    super(message);
    this.name = 'ValidationError';
  }
}

class NotFoundError extends Error {
  constructor(resourceType: string, id: string) {
    super(`${resourceType} not found: ${id}`);
    this.name = 'NotFoundError';
  }
}

// Usage
try {
  const user = await getUser(userId);
} catch (error) {
  if (error instanceof NotFoundError) {
    // Handle not found
  } else if (error instanceof ValidationError) {
    // Handle validation
  }
}
```

## Verification Before Completion

Before marking TypeScript work complete:

- [ ] **C-5 (MUST)**: Branded types used for all IDs
- [ ] **C-6 (MUST)**: Type-only imports using `import type`
- [ ] **G-3 (MUST)**: TypeScript compiles without errors
- [ ] **C-8 (SHOULD)**: Default to `type`, not `interface`
- [ ] **C-4 (SHOULD)**: Functions simple and composable
- [ ] **C-3 (SHOULD NOT)**: No classes when functions suffice
- [ ] **C-7 (SHOULD NOT)**: Only critical comments
- [ ] Naming conventions followed (variables, functions, booleans, types)
- [ ] Code organized logically
- [ ] File colocated (test with source)

## Integration with CLAUDE.md

Enforces CLAUDE.md Section 2 & 6:
- **C-3 through C-9**: While coding standards
- **C-5 through C-7**: Type and comment standards
- **G-1 through G-5**: Tooling and TypeScript
---

**Last Updated:** January 24, 2026
**Compatibility:** Claude Opus 4.5, Claude Code v2.x
**Status:** Production Ready

> **January 2026 Update:** This skill is compatible with Claude Opus 4.5 and Claude Code v2.x. For complex tasks, use the `effort: high` parameter for thorough analysis.

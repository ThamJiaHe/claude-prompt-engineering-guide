---
name: "TDD Workflow"
description: "Enforce strict Test-Driven Development with Red-Green-Refactor discipline. Apply when implementing new features, fixing bugs, or refactoring code. Ensures tests are written before implementation."
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
version: 2.1.0
compatibility: Claude Opus 4.6, Sonnet 4.6, Claude Code v2.1.x
updated: 2026-03-26
---

# TDD Workflow

Strict Red-Green-Refactor discipline for every code change. Tests come first — no exceptions.

## Overview

This skill enforces TDD as a non-negotiable workflow:

1. **RED** — Write a failing test that describes the desired behavior
2. **GREEN** — Write the minimum code to make it pass
3. **REFACTOR** — Clean up with all tests green

Never write implementation before a test exists for the happy path.

## When to Use

- Implementing any new feature or function
- Fixing a bug (write the regression test first)
- Refactoring existing code (ensure tests exist first)
- Adding edge case handling

## RED Phase: Write the Failing Test

```typescript
// Step 1: Write the test FIRST
import { describe, test, expect } from 'vitest';
import { calculateDiscount } from './pricing';

describe('calculateDiscount', () => {
  test('applies 10% discount for orders over $100', () => {
    expect(calculateDiscount(150)).toBe(135);
  });

  test('no discount for orders under $100', () => {
    expect(calculateDiscount(50)).toBe(50);
  });

  test('applies 20% discount for orders over $500', () => {
    expect(calculateDiscount(600)).toBe(480);
  });
});
```

**Critical:** Run the test. Confirm it **fails**. If it passes before implementation, the test is wrong.

```bash
# Run and verify failure
pnpm test -- --run calculateDiscount
```

## GREEN Phase: Minimum Implementation

```typescript
// Step 2: Write the MINIMUM code to pass
export function calculateDiscount(amount: number): number {
  if (amount > 500) return amount * 0.8;
  if (amount > 100) return amount * 0.9;
  return amount;
}
```

**Critical:** Run the test again. Confirm it **passes**.

```bash
pnpm test -- --run calculateDiscount
```

## REFACTOR Phase: Clean Up

With all tests green, improve the code:

```typescript
// Step 3: Refactor while tests stay green
const DISCOUNT_TIERS = [
  { threshold: 500, rate: 0.2 },
  { threshold: 100, rate: 0.1 },
] as const;

export function calculateDiscount(amount: number): number {
  const tier = DISCOUNT_TIERS.find(t => amount > t.threshold);
  return tier ? amount * (1 - tier.rate) : amount;
}
```

Run tests after every refactoring step:

```bash
pnpm test -- --run calculateDiscount
```

## Coverage Requirements

| Code Type | Minimum Coverage |
|-----------|:---:|
| Business logic | 80% |
| State transitions | 80% |
| Error paths | 80% |
| Algorithms | 80% |
| Pure data mapping | Exempt |
| Generated code | Exempt |
| Single-line wrappers | Exempt |

## Test Type Selection

Use the lowest-cost sufficient test:

| Type | When |
|------|------|
| **Unit** | Pure functions, isolated logic, no I/O |
| **Integration** | DB interactions, API calls, file system |
| **E2E** | Full user-facing flows (use sparingly) |

## Anti-Patterns to Avoid

- Writing implementation before tests
- Writing tests that pass before implementation
- Testing implementation details instead of behavior
- Mocking internal collaborators (only mock external boundaries)
- Skipping the "confirm it fails" step
- Batch-writing all tests at once instead of one at a time

## Integration with Claude Code

```bash
# Run single test during development (fast feedback)
pnpm test -- --run testName

# Run full suite before committing
pnpm test

# Check coverage
pnpm test -- --coverage
```

## Sources

- [Everything Claude Code TDD Guide](https://github.com/anthropics/everything-claude-code)
- [Superpowers TDD Skill](https://github.com/obra/superpowers)
- [Kent Beck's TDD By Example](https://www.oreilly.com/library/view/test-driven-development/0321146530/)

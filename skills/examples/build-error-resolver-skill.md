---
name: "Build Error Resolver"
description: "Rapidly fix build failures, type errors, and lint issues with minimal diffs. Apply when builds fail, TypeScript reports errors, or CI/CD pipelines break. Focuses on getting the build green fast."
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
version: 2.1.0
compatibility: Claude Opus 4.6, Sonnet 4.6, Claude Code v2.1.x
updated: 2026-03-26
---

# Build Error Resolver

Get the build green fast with minimal, targeted fixes. No architectural changes — just fix what's broken.

## Overview

This skill is a **surgical fix tool**, not a refactoring tool. It:

1. Reads the exact error output
2. Identifies the root cause
3. Makes the minimum change to fix it
4. Verifies the fix works
5. Moves to the next error

## When to Use

- `pnpm build` fails with TypeScript errors
- `pnpm lint` reports violations
- CI/CD pipeline fails on type checking
- Import resolution errors after dependency changes
- Type mismatches after schema or API changes
- Build fails after merging branches

## Workflow

### Step 1: Get the Error

```bash
# TypeScript build
pnpm tsc --noEmit 2>&1 | head -50

# Next.js build
pnpm build 2>&1 | tail -50

# Lint
pnpm lint 2>&1 | head -30
```

### Step 2: Classify the Error

| Error Pattern | Category | Typical Fix |
|---------------|----------|-------------|
| `TS2304: Cannot find name 'X'` | Missing import | Add import statement |
| `TS2322: Type 'X' is not assignable to 'Y'` | Type mismatch | Cast, narrow, or fix type |
| `TS2339: Property 'X' does not exist on type 'Y'` | Missing property | Add to interface or fix access |
| `TS2345: Argument of type 'X' not assignable to 'Y'` | Wrong argument type | Fix the argument or parameter type |
| `TS7006: Parameter 'X' implicitly has 'any' type` | Missing type annotation | Add type annotation |
| `TS2307: Cannot find module 'X'` | Missing dependency | `pnpm add X` or fix import path |
| `TS18047: 'X' is possibly 'null'` | Null safety | Add null check or assertion |
| `Module not found` | Import path wrong | Fix relative/absolute path |
| `ESLint: 'X' is defined but never used` | Unused code | Remove or prefix with `_` |

### Step 3: Fix with Minimal Diff

**Rule:** Change the fewest lines possible. Don't refactor surrounding code.

```typescript
// ERROR: TS2322: Type 'string | undefined' is not assignable to type 'string'
// FIX: Add nullish coalescing (1 character change)
const name = user.name ?? '';

// ERROR: TS2339: Property 'email' does not exist on type 'User'
// FIX: Add to interface (1 line)
interface User {
  id: string;
  name: string;
  email: string; // Added
}

// ERROR: TS2345: Argument of type 'number' not assignable to 'string'
// FIX: Convert type (minimal change)
const id = String(numericId);
```

### Step 4: Verify

```bash
# Re-run the same command that failed
pnpm tsc --noEmit

# If clean, run tests to ensure no regressions
pnpm test -- --run
```

### Step 5: Repeat for Remaining Errors

Process errors **one at a time**, top to bottom. Earlier fixes often resolve later errors.

## Common Patterns

### After Prisma Schema Change

```bash
# Error: Types don't match after schema update
# Fix: Regenerate Prisma client
pnpm prisma generate
```

### After Dependency Update

```bash
# Error: Breaking API changes
# Fix: Check migration guide
pnpm outdated  # See what changed
# Then read the changelog for the updated package
```

### After Branch Merge

```bash
# Error: Conflicting types from merged code
# Fix: Run type check, resolve type conflicts
pnpm tsc --noEmit 2>&1 | grep "error TS"
# Fix each error, prioritizing shared types/interfaces first
```

### Circular Dependency

```bash
# Error: Cannot access 'X' before initialization
# Fix: Extract shared types to a separate file
# Move shared interfaces to types.ts, import from there
```

## What NOT to Do

- Don't refactor surrounding code while fixing builds
- Don't change architecture to fix a type error
- Don't add `// @ts-ignore` or `any` casts (fix the actual type)
- Don't update unrelated code in the same commit
- Don't add new features while fixing builds

## Sources

- [Everything Claude Code — Build Error Resolver](https://github.com/anthropics/everything-claude-code)
- [TypeScript Error Reference](https://www.typescriptlang.org/docs/handbook/2/narrowing.html)

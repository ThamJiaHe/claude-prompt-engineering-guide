---
name: "Database & Migrations"
description: "Design schemas, create reversible migrations, validate data at API and DB layers. Apply when designing databases, creating migrations, defining models, or modifying schema."
allowed-tools: Read, Write, Edit, Bash
version: 2.0.0
---

# Database & Migrations

Systematic database design, safe migrations, and data validation at all layers.

## Overview

This Skill enforces:
- Normalized schema design (3NF)
- **D-1 (MUST)**: Models in server/models/
- **D-2 (MUST)**: Validation at API and DB layers
- **D-3 (SHOULD)**: Reversible migrations
- Safe migration patterns
- Atomic transactions

Apply when designing schemas, creating migrations, or defining models.

## Safe Migration Workflow

**Every migration must be reversible**:

```
Step 1: Write UP migration
  ↓
Step 2: Write DOWN migration (rollback)
  ↓
Step 3: Test UP on dev database
  ↓
Step 4: Test DOWN (rollback) successfully
  ↓
Step 5: Verify data integrity after rollback
  ↓
Step 6: Deploy to staging
```

### Migration File Structure

```
-- migration: 001_create_users_table.up.sql
BEGIN;
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_users_email ON users(email);
COMMIT;

-- migration: 001_create_users_table.down.sql
BEGIN;
DROP INDEX IF EXISTS idx_users_email;
DROP TABLE IF EXISTS users;
COMMIT;
```

### Naming Convention

```
YYYYMMDDHHMMSS_descriptive_name.up.sql
YYYYMMDDHHMMSS_descriptive_name.down.sql

Examples:
20250113140530_create_users_table.up.sql
20250113140530_create_users_table.down.sql
20250113141200_add_email_index.up.sql
20250113141200_add_email_index.down.sql
```

## Common Migration Patterns

### Adding NOT NULL Column (3-step process)

```sql
-- Step 1: Add column nullable
ALTER TABLE users ADD COLUMN status VARCHAR(50);

-- Step 2: Populate existing rows
UPDATE users SET status = 'active' WHERE status IS NULL;

-- Step 3: Make NOT NULL
ALTER TABLE users ALTER COLUMN status SET NOT NULL;
```

### Adding Index (non-blocking)

```sql
-- Non-blocking index creation
CREATE INDEX CONCURRENTLY idx_users_email ON users(email);

-- Rollback
DROP INDEX CONCURRENTLY idx_users_email;
```

### Renaming Column

```sql
-- UP: Rename
ALTER TABLE users RENAME COLUMN phone_number TO phone;

-- DOWN: Rename back
ALTER TABLE users RENAME COLUMN phone TO phone_number;
```

### Adding Foreign Key

```sql
-- UP
ALTER TABLE posts ADD COLUMN user_id UUID;
ALTER TABLE posts ADD FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE;

-- DOWN
ALTER TABLE posts DROP CONSTRAINT posts_user_id_fkey;
ALTER TABLE posts DROP COLUMN user_id;
```

## Anti-Pattern Migrations

```sql
-- ❌ BAD: Direct NOT NULL (fails if data exists)
ALTER TABLE users ADD COLUMN status VARCHAR(50) NOT NULL;

-- ❌ BAD: Blocking index
CREATE INDEX idx_users_email ON users(email);

-- ❌ BAD: No rollback migration
-- Can't undo this change!

-- ❌ BAD: Multiple unrelated changes
ALTER TABLE users ADD COLUMN email VARCHAR(255);
ALTER TABLE posts ADD COLUMN category VARCHAR(50);
ALTER TABLE comments DROP COLUMN spam_score;
-- Too many changes = hard to debug if one fails
```

## Schema Design

### Single Responsibility

Each table represents one entity:

```sql
-- ✅ GOOD: One entity per table
CREATE TABLE users (
  id UUID PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255) NOT NULL
);

CREATE TABLE contacts (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255),
  FOREIGN KEY (user_id) REFERENCES users(id)
);

-- ❌ BAD: Multiple entities mixed
CREATE TABLE user_contact_data (
  id UUID PRIMARY KEY,
  user_id UUID,
  user_email VARCHAR(255),
  contact_id UUID,
  contact_name VARCHAR(255)
);
```

### Correct Data Types

```sql
-- ✅ GOOD: Appropriate types
CREATE TABLE users (
  id UUID PRIMARY KEY,
  email VARCHAR(255),
  balance DECIMAL(10, 2),          -- Money, not FLOAT!
  is_verified BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  metadata JSONB                   -- Semi-structured data
);

-- ❌ BAD: Wrong types
CREATE TABLE users (
  id VARCHAR(255),                 -- Should be UUID
  balance FLOAT,                   -- Should be DECIMAL!
  is_verified VARCHAR(5),          -- Should be BOOLEAN
  created_at BIGINT,               -- Should be TIMESTAMP
  metadata TEXT                    -- Should be JSONB
);
```

### Constraints Enforce Business Rules

```sql
-- ✅ GOOD: Database enforces rules
CREATE TABLE products (
  id UUID PRIMARY KEY,
  price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
  stock INT NOT NULL CHECK (stock >= 0),
  status VARCHAR(50) CHECK (status IN ('active', 'inactive', 'archived'))
);

-- ❌ BAD: No validation
CREATE TABLE products (
  id UUID PRIMARY KEY,
  price DECIMAL(10, 2),  -- Could be negative!
  stock INT,             -- Could be negative!
  status VARCHAR(50)     -- Any value allowed
);
```

## D-1 (MUST): Models in server/models/

Define all models in one place:

```ts
// server/models/User.ts
import type { Brand } from '@/lib/branded';

export type UserId = Brand<string, 'UserId'>;

export type User = {
  id: UserId;
  email: string;
  name: string;
  createdAt: Date;
  updatedAt: Date;
};

export type CreateUserInput = {
  email: string;
  name: string;
};

// Database schema must match this type exactly
```

### Prisma Schema

```prisma
// prisma/schema.prisma
model User {
  id        String   @id @default(cuid())
  email     String   @unique
  name      String
  posts     Post[]
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt

  @@index([email])
}

model Post {
  id        String   @id @default(cuid())
  title     String
  authorId  String
  author    User     @relation(fields: [authorId], references: [id], onDelete: Cascade)
  createdAt DateTime @default(now())

  @@index([authorId])
}
```

## D-2 (MUST): Validate at Both Layers

**Client/API Layer**:

```ts
import { z } from 'zod';

const CreateUserSchema = z.object({
  email: z.string().email('Invalid email'),
  name: z.string().min(1, 'Name required').max(255)
});

export async function createUser(input: unknown) {
  const validated = CreateUserSchema.parse(input);
  return await db.users.create(validated);
}
```

**Database Layer** (Schema constraints):

```sql
CREATE TABLE users (
  id UUID PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE CHECK (email LIKE '%@%'),
  name VARCHAR(255) NOT NULL CHECK (LENGTH(name) > 0)
);
```

## Indexes for Performance

**When to index**:
- Primary keys (automatic)
- Foreign keys
- Frequently searched columns
- Sort/ORDER BY columns
- JOIN condition columns

**Anti-Pattern**:

```sql
-- ❌ BAD: Unnecessary indexes
CREATE INDEX idx_users_id ON users(id);  -- Redundant with PRIMARY KEY
CREATE INDEX idx_users_age ON users(age);  -- Rarely queried
CREATE INDEX idx_users_name ON users(name);  -- Every name indexed?

-- ✅ GOOD: Strategic indexes
CREATE INDEX idx_users_email ON users(email);  -- Frequently searched
CREATE INDEX idx_posts_author_id ON posts(author_id);  -- Foreign key
CREATE INDEX idx_posts_created_at ON posts(created_at);  -- Sorted
```

## Transactions for Multi-Step Operations

```sql
-- ✅ GOOD: Transaction ensures atomicity
BEGIN;
  UPDATE users SET balance = balance - 100 WHERE id = 'user1';
  UPDATE users SET balance = balance + 100 WHERE id = 'user2';
COMMIT;
-- If either UPDATE fails, both rollback

-- ❌ BAD: No transaction
UPDATE users SET balance = balance - 100 WHERE id = 'user1';
UPDATE users SET balance = balance + 100 WHERE id = 'user2';
-- Incomplete transfer if error mid-way
```

### Using Transactions in Code

```ts
// With Prisma
export async function transferFunds(
  fromUserId: UserId,
  toUserId: UserId,
  amount: number
) {
  return await db.$transaction(async (tx) => {
    await tx.user.update({
      where: { id: fromUserId },
      data: { balance: { decrement: amount } }
    });

    await tx.user.update({
      where: { id: toUserId },
      data: { balance: { increment: amount } }
    });

    // Both succeed or both rollback
  });
}
```

## Testing Database Operations

### Unit Tests (No Database)

```ts
describe('validateUserData', () => {
  test('rejects invalid email', () => {
    expect(() => validateUserData({ email: 'invalid' })).toThrow();
  });

  test('rejects missing name', () => {
    expect(() => validateUserData({ name: '' })).toThrow();
  });
});
```

### Integration Tests (With Database)

```ts
describe('User model', () => {
  beforeEach(async () => {
    await db.users.deleteMany({});
  });

  test('creates user with valid data', async () => {
    const user = await User.create({
      email: 'test@example.com',
      name: 'Test User'
    });

    expect(user).toHaveProperty('id');
    expect(user.email).toBe('test@example.com');
  });

  test('enforces unique email', async () => {
    await User.create({ email: 'test@example.com', name: 'User 1' });

    await expect(
      User.create({ email: 'test@example.com', name: 'User 2' })
    ).rejects.toThrow('Unique constraint');
  });
});
```

## Verification Before Deploying Migration

Before marking database work complete:

- [ ] **D-1 (MUST)**: Models defined in server/models/
- [ ] **D-2 (MUST)**: Validation at both API and DB layers
- [ ] **D-3 (SHOULD)**: UP migration written
- [ ] **D-3 (SHOULD)**: DOWN migration written (reversible)
- [ ] Tested UP on dev database
- [ ] Tested DOWN (rollback) successfully
- [ ] Data integrity verified after rollback
- [ ] No breaking changes without backward compatibility
- [ ] Indexes on frequently queried columns
- [ ] Transactions for multi-step operations
- [ ] Constraints enforce business rules
- [ ] Models updated to match schema

## Integration with CLAUDE.md

Enforces CLAUDE.md Section 4 & 2:
- **D-1 through D-4**: Database standards
- **C-10**: Validation standards

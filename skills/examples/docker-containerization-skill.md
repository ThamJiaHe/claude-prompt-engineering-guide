---
name: "Docker Containerization"
description: "Production-ready Docker patterns for multi-stage builds, security hardening, and orchestration. Apply when creating Dockerfiles, docker-compose configs, or deploying containerized applications."
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
version: 2.1.0
compatibility: Claude Opus 4.6, Sonnet 4.6, Claude Code v2.1.x
updated: 2026-03-26
---

# Docker Containerization

Production-ready container patterns: multi-stage builds, security hardening, and composition.

## When to Use

- Creating or modifying Dockerfiles
- Setting up docker-compose for development or production
- Optimizing container image size
- Securing containerized applications
- Setting up CI/CD with containers

## Multi-Stage Build (Node.js)

```dockerfile
# Stage 1: Install dependencies
FROM node:22-alpine AS deps
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN corepack enable && pnpm install --frozen-lockfile

# Stage 2: Build
FROM node:22-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN corepack enable && pnpm build

# Stage 3: Production
FROM node:22-alpine AS runner
WORKDIR /app

# Security: run as non-root
RUN addgroup --system --gid 1001 appgroup && \
    adduser --system --uid 1001 appuser

# Copy only production artifacts
COPY --from=builder --chown=appuser:appgroup /app/.next/standalone ./
COPY --from=builder --chown=appuser:appgroup /app/.next/static ./.next/static
COPY --from=builder --chown=appuser:appgroup /app/public ./public

USER appuser
EXPOSE 3000
ENV NODE_ENV=production PORT=3000 HOSTNAME="0.0.0.0"
CMD ["node", "server.js"]
```

## Multi-Stage Build (Python)

```dockerfile
# Stage 1: Build
FROM python:3.12-slim AS builder
WORKDIR /app
RUN pip install uv
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# Stage 2: Production
FROM python:3.12-slim AS runner
WORKDIR /app

RUN adduser --system --uid 1001 appuser
COPY --from=builder /app/.venv ./.venv
COPY . .

USER appuser
ENV PATH="/app/.venv/bin:$PATH"
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Docker Compose (Development)

```yaml
# docker-compose.yml
services:
  app:
    build:
      context: .
      target: deps  # Use deps stage for dev
    volumes:
      - .:/app
      - /app/node_modules  # Don't mount node_modules
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/myapp
      - NODE_ENV=development
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:17-alpine
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  pgdata:
```

## Security Hardening Checklist

- [ ] Run as non-root user (`USER appuser`)
- [ ] Use specific image tags, not `latest`
- [ ] Multi-stage builds (don't ship build tools)
- [ ] No secrets in Dockerfile or image layers
- [ ] Read-only filesystem where possible (`read_only: true`)
- [ ] Drop all capabilities, add only needed ones
- [ ] Scan images for vulnerabilities (`docker scout`, `trivy`)
- [ ] Use `.dockerignore` to exclude sensitive files
- [ ] Set resource limits (memory, CPU)
- [ ] Health checks defined

## .dockerignore

```
node_modules
.git
.env
.env.*
*.md
.next
dist
coverage
.claude
```

## Sources

- [Docker Best Practices](https://docs.docker.com/build/building/best-practices/)
- [Node.js Docker Guide](https://nodejs.org/en/docs/guides/nodejs-docker-webapp)

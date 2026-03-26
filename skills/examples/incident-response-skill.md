---
name: "Incident Response"
description: "Structured production incident triage, resolution, and post-mortem. Apply when production systems are down, degraded, or behaving unexpectedly. Covers detection, containment, resolution, and learning."
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
version: 2.1.0
compatibility: Claude Opus 4.6, Sonnet 4.6, Claude Code v2.1.x
updated: 2026-03-26
---

# Incident Response

Structured workflow for production incidents: detect, contain, resolve, learn.

## When to Use

- Production service is down or degraded
- Users reporting errors or data issues
- Monitoring alerts firing
- Security incident detected
- Data integrity issue discovered

## Severity Classification

| Severity | Impact | Response Time | Examples |
|:--------:|--------|:---:|---------|
| **SEV-1** | Full outage, data breach, revenue loss | Immediate | Service down, auth broken, data leak |
| **SEV-2** | Major degradation, subset of users affected | < 30 min | Slow responses, feature broken, partial outage |
| **SEV-3** | Minor impact, workaround available | < 4 hours | UI bug, non-critical feature down |
| **SEV-4** | No user impact, internal issue | Next business day | Log errors, monitoring gaps |

## Phase 1: Detection & Triage (First 5 Minutes)

```markdown
## Incident Triage

**Time detected:** [timestamp]
**Reporter:** [who noticed]
**Severity:** SEV-[1-4]

### What's happening?
[One sentence description of symptoms]

### Who's affected?
[All users / subset / internal only]

### What changed recently?
[Deployments, config changes, traffic spikes]
```

### Quick Diagnostic Commands

```bash
# Check recent deployments
git log --oneline -5 --since="2 hours ago"

# Check application logs
tail -100 /var/log/app/error.log | grep -i "error\|fatal\|panic"

# Check system resources
top -bn1 | head -20
df -h
free -h

# Check database connectivity
pg_isready -h $DB_HOST

# Check external service health
curl -sI https://api.stripe.com/v1 -o /dev/null -w "%{http_code}"
```

## Phase 2: Containment (Minutes 5-15)

**Goal:** Stop the bleeding. Don't fix root cause yet.

| Containment Action | When to Use |
|---|---|
| **Rollback deployment** | Problem started after a deploy |
| **Feature flag disable** | New feature causing issues |
| **Scale up** | Traffic/load related |
| **Failover to backup** | Primary system unrecoverable |
| **Rate limit** | Being overwhelmed by requests |
| **Block bad actor** | Malicious traffic identified |

```bash
# Quick rollback (if deployment caused it)
git revert HEAD --no-edit && git push

# Or revert to last known good deployment
# (platform-specific: Vercel, Railway, etc.)
```

## Phase 3: Resolution

### Hypothesis-Driven Debugging

```markdown
## Debugging Log

### Hypothesis 1: [Most likely cause]
Evidence for: [what supports this]
Evidence against: [what contradicts this]
Test: [how to verify]
Result: [confirmed / rejected]

### Hypothesis 2: [Second most likely]
...
```

### Common Root Causes

| Symptom | Common Cause | Quick Fix |
|---------|-------------|-----------|
| 500 errors spike | Bad deployment | Rollback |
| Slow responses | Database query regression | Kill slow queries, add index |
| Connection timeouts | Connection pool exhaustion | Restart, increase pool size |
| OOM crashes | Memory leak | Restart, set memory limits |
| Auth failures | Token/cert expiry | Rotate credentials |
| Data inconsistency | Race condition | Add locking, retry logic |

## Phase 4: Post-Mortem

Write within 48 hours of resolution. **Blameless** — focus on systems, not people.

```markdown
# Post-Mortem: [Incident Title]

**Date:** YYYY-MM-DD
**Duration:** [start time] to [resolution time] ([X] minutes)
**Severity:** SEV-[X]
**Author:** [Name]

## Summary
[2-3 sentence summary of what happened and impact]

## Timeline
| Time | Event |
|------|-------|
| HH:MM | [First symptom / alert] |
| HH:MM | [Incident declared] |
| HH:MM | [Root cause identified] |
| HH:MM | [Fix deployed] |
| HH:MM | [Confirmed resolved] |

## Root Cause
[Technical explanation of what went wrong]

## Impact
- Users affected: [number or percentage]
- Duration: [minutes]
- Revenue impact: [if applicable]
- Data affected: [if applicable]

## What Went Well
- [Good thing 1]
- [Good thing 2]

## What Went Wrong
- [Process/system gap 1]
- [Process/system gap 2]

## Action Items
| Action | Owner | Due Date | Priority |
|--------|-------|----------|:--------:|
| [Preventive measure] | [Name] | [Date] | P1 |
| [Detection improvement] | [Name] | [Date] | P2 |
| [Process improvement] | [Name] | [Date] | P3 |

## Lessons Learned
[What the team should take away from this]
```

## Communication Template

```markdown
## Status Update: [Incident Title]

**Status:** Investigating / Identified / Monitoring / Resolved
**Impact:** [Who/what is affected]
**Current action:** [What we're doing right now]
**ETA:** [When we expect resolution, if known]
**Next update:** [When the next status update will be]
```

## Sources

- [PagerDuty Incident Response Guide](https://response.pagerduty.com/)
- [Google SRE Handbook — Incident Management](https://sre.google/sre-book/managing-incidents/)
- [Atlassian Incident Management](https://www.atlassian.com/incident-management)

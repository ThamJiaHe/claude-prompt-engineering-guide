# Example CLAUDE.md / .clauderules Template

A self-evolving rules file that improves through use. Based on January 2026 best practices.

> **Pattern**: Self-evolving rules that Claude updates based on conversation learnings

---

## What is This?

This template demonstrates the **self-evolving CLAUDE.md pattern** — a rules file that Claude updates automatically during conversations to capture project-specific learnings, conventions, and preferences.

### Why Self-Evolving?

Traditional static rules files become outdated. Self-evolving rules:
- ✅ Capture learnings as they happen
- ✅ Stay current with project evolution
- ✅ Build institutional knowledge
- ✅ Reduce repeated explanations
- ✅ Create living documentation

---

## Template: Basic Self-Evolving CLAUDE.md

```markdown
# CLAUDE.md

## Project Context
[Brief project description - 2-3 sentences]

## Critical Rules
<!-- These rules are immutable and should not be changed -->
- Never commit directly to main branch
- All changes require tests
- Security-sensitive code requires human review

## Learned Conventions
<!-- Claude updates this section when discovering project patterns -->

### Code Style
<!-- Patterns discovered during development -->

### Architecture Patterns
<!-- Structural decisions learned from codebase -->

### Testing Patterns
<!-- Testing conventions observed -->

## Session Learnings
<!-- Temporary learnings from current session - review before committing -->

---

## Self-Update Instructions

When you discover new project conventions:
1. Add them to the appropriate section above
2. Use clear, actionable language
3. Include examples when helpful
4. Mark uncertain learnings with [VERIFY]

When updating this file:
- Preserve Critical Rules unchanged
- Add new learnings to Learned Conventions
- Clear Session Learnings after review
```

---

## Template: Advanced Self-Evolving CLAUDE.md

```markdown
# CLAUDE.md — Project Intelligence

Last Updated: [AUTO-UPDATE DATE]
Learning Sessions: [COUNT]

---

## 1. Identity & Purpose

**Project**: [Name]
**Type**: [Web app / Library / CLI / etc.]
**Primary Language**: [Language]

---

## 2. Critical Rules (Immutable)

These rules NEVER change without explicit human approval:

```yaml
security:
  - Never expose API keys or secrets in code
  - Never disable authentication for debugging
  - Always validate user input

quality:
  - All PRs require passing tests
  - No console.log in production code
  - Type safety required (no 'any' types)

process:
  - Never push to main directly
  - Commit messages follow conventional commits
  - Update CHANGELOG for user-facing changes
```

---

## 3. Project Architecture

### File Structure
<!-- Updated automatically when exploring codebase -->
```
src/
├── components/    # React components
├── hooks/         # Custom hooks
├── services/      # API integrations
├── utils/         # Pure utility functions
└── types/         # TypeScript definitions
```

### Key Patterns
<!-- Learned patterns from code exploration -->
- **State Management**: [Pattern discovered]
- **API Calls**: [Pattern discovered]
- **Error Handling**: [Pattern discovered]
- **Testing**: [Pattern discovered]

---

## 4. Learned Conventions

### Code Style
<!-- Patterns learned from codebase -->

#### Naming
- Components: PascalCase (e.g., `UserProfile`)
- Hooks: camelCase with `use` prefix (e.g., `useAuth`)
- Constants: SCREAMING_SNAKE_CASE
- Files: kebab-case for utilities, PascalCase for components

#### Patterns
- [Add discovered patterns here]

### Testing Conventions
<!-- Learned from existing tests -->
- Test files: `*.test.ts` next to source
- Naming: `describe('[Component]', () => { it('should [behavior]', ...) })`
- Mocking: [Pattern discovered]

### Git Conventions
<!-- Learned from git history -->
- Commit style: [conventional / descriptive / other]
- Branch naming: [pattern discovered]
- PR size: [guidance discovered]

---

## 5. Dependencies & Integrations

### Core Dependencies
<!-- Populated automatically -->
| Package | Purpose | Notes |
|---------|---------|-------|
| [pkg] | [purpose] | [any gotchas] |

### External Services
<!-- APIs, databases, third-party integrations -->
- **Database**: [Type and connection pattern]
- **Auth**: [Provider and pattern]
- **Hosting**: [Platform and deployment pattern]

---

## 6. Known Issues & Workarounds

<!-- Captures problems and solutions discovered -->

### Active Issues
- [ ] [Issue description] — Workaround: [solution]

### Resolved Issues
- [x] [Issue] — Fixed by: [solution] — Date: [date]

---

## 7. Session Learnings (Review Queue)

<!-- Temporary learnings from current session -->
<!-- Human should review before these become permanent -->

### Pending Review
- [VERIFY] [Learning that needs confirmation]
- [NEW] [Newly discovered pattern]

---

## 8. Self-Update Protocol

### When to Update This File

**Always update when:**
- Discovering undocumented project conventions
- Finding patterns in existing code
- Learning preferences from conversation
- Encountering and solving problems

**Never update:**
- Critical Rules section (immutable)
- To contradict explicit human instructions
- With speculative or uncertain information (mark [VERIFY] instead)

### Update Format

```markdown
### [Section Name]
- **[Pattern/Convention]**: [Description]
  - Example: [Code or usage example]
  - Learned: [Date or session reference]
```

### Quality Checks

Before updating, verify:
1. Is this actually a pattern (seen 2+ times)?
2. Does this contradict existing rules?
3. Is this project-specific or general knowledge?
4. Should this be marked [VERIFY] for human review?

---

## 9. Evolution History

<!-- Track significant updates to this file -->

| Date | Section | Change | Source |
|------|---------|--------|--------|
| [date] | [section] | [what changed] | [conversation/exploration] |
```

---

## Usage Instructions

### Initial Setup

1. **Create the file** in your project root:
   ```bash
   touch CLAUDE.md
   # or
   touch .clauderules
   ```

2. **Add to .gitignore** (optional):
   ```
   # If you want personal rules separate from team rules
   .clauderules.local
   ```

3. **Seed with basic info**:
   - Project purpose
   - Critical rules
   - Key architecture decisions

### During Development

1. **Claude reads this file** at conversation start
2. **Claude updates** when learning new patterns
3. **You review** Session Learnings periodically
4. **You commit** valuable learnings to git

### Review Process

```markdown
## Recommended Review Cadence

Weekly:
- Review Session Learnings section
- Promote valid learnings to permanent sections
- Clear stale session learnings

Monthly:
- Review all Learned Conventions
- Remove outdated patterns
- Update architecture documentation

Per Release:
- Ensure documentation matches code
- Update version-specific information
- Archive resolved issues
```

---

## Best Practices

### DO:

- ✅ Start minimal, let it grow organically
- ✅ Review session learnings regularly
- ✅ Commit the file to version control
- ✅ Mark uncertain learnings with [VERIFY]
- ✅ Include concrete examples
- ✅ Keep Critical Rules short and immutable

### DON'T:

- ❌ Make this file too large (aim for <500 lines)
- ❌ Include sensitive information
- ❌ Let it become stale
- ❌ Skip human review of learnings
- ❌ Duplicate information from README

---

## Integration with Claude Code

### Claude Code reads this file automatically

When you start Claude Code in a project with `CLAUDE.md` or `.clauderules`, it's loaded into context automatically.

### Updating the file

Claude Code can update this file during development:

```
Claude: I notice you use a specific pattern for API calls.
        Should I add this to CLAUDE.md for future reference?

You: Yes, add it to the Learned Conventions section.

Claude: [Updates CLAUDE.md with the pattern]
```

### Multi-file setup

For large projects, you can split rules:

```
project/
├── CLAUDE.md              # Main rules
├── .claude/
│   ├── architecture.md    # Detailed architecture
│   ├── testing.md         # Testing conventions
│   └── api.md             # API patterns
```

---

## Example: Populated CLAUDE.md

```markdown
# CLAUDE.md — Acme Dashboard

Last Updated: 2026-01-15
Learning Sessions: 12

---

## 1. Identity & Purpose

**Project**: Acme Dashboard
**Type**: Next.js 15 web application
**Primary Language**: TypeScript

---

## 2. Critical Rules (Immutable)

```yaml
security:
  - Never expose ACME_API_KEY in client code
  - All API routes require authentication middleware
  - PII must be encrypted at rest

quality:
  - 80% test coverage minimum
  - No TypeScript errors allowed
  - Lighthouse performance score > 90
```

---

## 4. Learned Conventions

### Code Style

#### API Calls
All API calls go through the `apiClient` utility:
```typescript
// Good
const data = await apiClient.get('/users');

// Bad - don't use fetch directly
const data = await fetch('/api/users');
```

#### Error Handling
Use the `Result` type for operations that can fail:
```typescript
type Result<T> = { ok: true; data: T } | { ok: false; error: string };
```

### Testing Conventions

- Use `@testing-library/react` for component tests
- Mock API calls with `msw` (Mock Service Worker)
- Snapshot tests only for static components

---

## 7. Session Learnings (Review Queue)

### Pending Review
- [NEW] Dashboard charts use `recharts` library
- [VERIFY] Seems like feature flags are in `config/features.ts`
```

---

## Learn More

- [Claude Prompt Engineering Guide](../Claude-Prompt-Guide.md)
- [Claude Code Guide](../docs/claude-code-guide.md)
- [Skills Guide](../docs/skills-guide.md)

---

*Last Updated: January 15, 2026*

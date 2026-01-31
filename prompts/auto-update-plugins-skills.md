# Auto-Update All Plugins and Skills - Claude Code Max Opus 4.5 Prompt

> **Purpose:** Comprehensive prompt for Claude Code Max Opus 4.5 to automatically update ALL plugins and skills in the Claude Prompt Engineering Guide repository.
>
> **Created:** January 31, 2026  
> **Model:** Claude Code Max Opus 4.5  
> **Repository:** ThamJiaHe/claude-prompt-engineering-guide

---

## 🎯 Task Overview

You are an expert prompt engineering specialist with deep knowledge of the Claude ecosystem. Your task is to systematically update ALL plugins and skills in this repository to ensure they are current, accurate, and optimized for Claude Opus 4.5, Sonnet 4.5, and Haiku 4.5 (January 2026).

---

## 📋 Scope of Updates

### 1. Skills Collection (22 Skills)
Located in: `/skills/examples/`

**All 22 Production Skills to Update:**

#### Web Development & Full-Stack (4 skills)
1. `nextjs-app-router-skill.md` - Next.js 15+ with App Router
2. `tailwind-design-system-skill.md` - Tailwind CSS design systems
3. `nextauth-authentication-skill.md` - NextAuth.js authentication
4. `api-development-skill.md` - REST/GraphQL API development

#### Backend & Infrastructure (4 skills)
5. `aws-cloud-infrastructure-skill.md` - AWS infrastructure
6. `google-cloud-platform-skill.md` - GCP services
7. `neon-serverless-skill.md` - Neon serverless databases
8. `prisma-orm-skill.md` - Prisma ORM operations

#### Testing & QA (4 skills)
9. `testing-skill.md` - Testing strategies
10. `vitest-unit-testing-skill.md` - Vitest unit testing
11. `playwright-e2e-testing-skill.md` - Playwright E2E testing
12. `code-review.md` - Code review processes

#### DevOps & Deployment (4 skills)
13. `vercel-deployment-skill.md` - Vercel deployments
14. `database-migrations.md` - Database migrations
15. `monitoring-logging-skill.md` - Monitoring and logging
16. `git-workflow-skill.md` - Git workflows

#### Standards & Best Practices (6 skills)
17. `typescript-standards.md` - TypeScript standards
18. `performance-optimization-skill.md` - Performance optimization
19. `seo-optimization-skill.md` - SEO best practices
20. `security-compliance.md` - Security compliance
21. `accessibility-ux.md` - Accessibility and UX
22. `example-feedback-analyzer.md` - Customer feedback analysis

### 2. Plugin References
Located throughout documentation in `/docs/`

**Plugins to Verify/Update:**
- **Superpowers** - `docs/superpowers-guide.md`
- **MCP (Model Context Protocol)** - `docs/mcp-integration.md`, `docs/mcp-ecosystem-overview.md`
- **Context7 MCP Server** - Latest version and configuration
- **Skills System** - `docs/skills-guide.md`
- **Claude Cowork** - `docs/cowork-guide.md`

---

## 🔄 Update Methodology

### Phase 1: Pre-Update Analysis (15 minutes)

1. **Catalog Current State**
   ```bash
   # List all skills with their versions
   grep -r "version:" skills/examples/*.md
   
   # List all skills with their updated dates
   grep -r "updated:" skills/examples/*.md
   
   # Check for any TODO or FIXME comments
   grep -r "TODO\|FIXME" skills/ docs/
   ```

2. **Research Latest Versions**
   - Check npm/package registries for latest library versions
   - Verify API changes in major frameworks
   - Review Claude 4.5 model capabilities (as of Jan 2026)
   - Check MCP ecosystem updates
   - Verify Superpowers plugin status

3. **Document Current Baseline**
   Create `/tmp/update-baseline.md` with:
   - Current version numbers for each skill
   - Current compatibility statements
   - Any known issues or deprecated features

### Phase 2: Skills Updates (60-90 minutes)

For EACH of the 22 skills, perform the following systematic updates:

#### A. Metadata Updates

```yaml
---
name: "[Skill Name]"
description: "[Updated description if needed]"
allowed-tools: Read, Write, Edit, Bash
version: [INCREMENT VERSION]  # Increment patch or minor version
compatibility: Claude Opus 4.5, Claude Sonnet 4.5, Claude Haiku 4.5, Claude Code v2.x
updated: 2026-01-31  # TODAY'S DATE
---
```

**Version Increment Rules:**
- Patch (1.1.0 → 1.1.1): Bug fixes, minor corrections
- Minor (1.1.1 → 1.2.0): New features, significant updates
- Major (1.2.0 → 2.0.0): Breaking changes

#### B. Compatibility Updates

Update all references to:
- Claude model versions (Opus 4.5, Sonnet 4.5, Haiku 4.5)
- Claude Code version (v2.x as of Jan 2026)
- Library/framework latest stable versions
- API endpoints and methods

#### C. Content Quality Improvements

For each skill:

1. **Check Examples Are Current**
   - Verify code examples work with latest library versions
   - Update deprecated APIs
   - Add new best practices discovered since last update

2. **Verify Best Practices**
   - Cross-reference with official documentation
   - Ensure security best practices are current
   - Update performance recommendations

3. **Enhance Documentation**
   - Add clarifications where needed
   - Include troubleshooting for common issues
   - Add links to official resources

4. **Test Code Snippets** (where applicable)
   - Verify syntax is correct
   - Check for TypeScript/JavaScript updates
   - Ensure compatibility with stated versions

#### D. Structure Validation

Ensure each skill has all required sections:
```markdown
# [Skill Name]

## Overview
## [Core Content Sections]
## Installation
## Usage
  ### Basic Usage
  ### Advanced Usage
## Configuration
## Examples
## Dependencies
## Troubleshooting
## Best Practices
## Performance Considerations
## Security Considerations
## License
```

#### E. Token Optimization

Apply wrapper pattern where appropriate:
- Keep core skill content concise (≤500 lines)
- Reference detailed implementation in separate files
- Use progressive disclosure for advanced topics
- Maintain token efficiency per Jan 2026 best practices

### Phase 3: Plugin Documentation Updates (30-45 minutes)

#### Superpowers Plugin (`docs/superpowers-guide.md`)

1. **Verify Plugin Status**
   - Check GitHub repo: https://github.com/obra/superpowers-chrome
   - Note latest version and release date
   - Update installation instructions if changed

2. **Update Features List**
   - Verify all features are still available
   - Add any new features
   - Remove deprecated features

3. **Update Code Examples**
   - Ensure examples work with Claude 4.5
   - Update API calls if changed

#### MCP Integration (`docs/mcp-integration.md`)

1. **Verify MCP Protocol Version**
   - Check https://modelcontextprotocol.io
   - Update protocol version references
   - Note any breaking changes

2. **Update Context7 MCP Configuration**
   - Verify Context7 is still #2 ranked server
   - Update installation steps
   - Test configuration examples

3. **Catalog MCP Servers**
   - Update count (currently "50+ official, tens of thousands community")
   - Add any new notable servers
   - Update server examples

#### Skills System (`docs/skills-guide.md`)

1. **Update Skills Documentation**
   - Reflect current 22 skills count
   - Update wrapper pattern documentation
   - Add any new usage patterns

2. **Update Token Efficiency Data**
   - Verify wrapper pattern reduces tokens by 70-80%
   - Update comparison metrics
   - Add new optimization techniques

#### Claude Cowork (`docs/cowork-guide.md`)

1. **Verify Current Status**
   - Confirm launch date (Jan 12, 2026)
   - Update feature set
   - Note any new capabilities

2. **Update Integration Examples**
   - Ensure examples are current
   - Add new use cases if available

### Phase 4: Main Documentation Updates (20-30 minutes)

#### Update Root README.md

1. **Update Statistics**
   ```markdown
   - **Total Skills**: 22 (verified Jan 31, 2026)
   - **Last Updated**: January 31, 2026
   - **Model Support**: Claude Opus 4.5, Sonnet 4.5, Haiku 4.5
   ```

2. **Update Product Status Table**
   - Verify all product statuses are current
   - Update scorecard if needed

3. **Update Critical Issues Section**
   - Remove resolved issues
   - Add new known issues
   - Update GitHub issue links

#### Update Skills README (`skills/README.md`)

1. **Update Skills Count and Table**
   - Verify all 22 skills are listed
   - Update status badges if needed
   - Ensure all links work

2. **Update Usage Instructions**
   - Reflect Claude Code v2.x features
   - Update API examples to Claude 4.5
   - Verify wrapper pattern documentation

#### Update Main Guide (`Claude-Prompt-Guide.md`)

1. **Update Model References**
   - Ensure all references are to 4.5 models
   - Update pricing if changed
   - Update capability descriptions

2. **Update Dates**
   - Change "Last Updated" to today
   - Update any time-sensitive references

3. **Update Best Practices**
   - Add any new discoveries from Jan 2026
   - Update deprecated practices

### Phase 5: Validation & Testing (15-20 minutes)

#### Automated Checks

```bash
# Check for broken internal links
find . -name "*.md" -exec grep -H "\[.*\](.*\.md)" {} \; | \
  while read -r line; do
    file=$(echo "$line" | cut -d: -f1)
    link=$(echo "$line" | grep -o "\](.*\.md)" | sed 's/](\|)//g')
    if [ ! -f "$link" ] && [ ! -f "$(dirname "$file")/$link" ]; then
      echo "Broken link in $file: $link"
    fi
  done

# Check for outdated model references
grep -r "claude-3\|opus-3\|sonnet-3\|haiku-3" --include="*.md" . || echo "✓ No Claude 3 references found"

# Check for inconsistent dates
grep -r "2025" --include="*.md" skills/ docs/ | grep -v "Nov\|November\|MIGRATION" || echo "✓ No outdated 2025 dates"

# Validate YAML frontmatter
for file in skills/examples/*.md; do
  if ! head -n 10 "$file" | grep -q "version:"; then
    echo "Missing version in: $file"
  fi
  if ! head -n 10 "$file" | grep -q "updated:"; then
    echo "Missing updated date in: $file"
  fi
done
```

#### Manual Verification

1. **Sample 5 Random Skills**
   - Read through completely
   - Verify code examples are syntactically correct
   - Check all links work
   - Ensure formatting is consistent

2. **Check Critical Paths**
   - README.md renders correctly
   - Main guide table of contents works
   - All skill links in skills/README.md work

3. **Cross-Reference Check**
   - Skills count matches across all documents
   - Version numbers are consistent
   - Dates are updated everywhere

### Phase 6: Documentation of Changes (10-15 minutes)

#### Create Update Summary

Create `/tmp/update-summary-2026-01-31.md` with:

```markdown
# Skills and Plugins Update Summary
**Date:** January 31, 2026  
**Performed by:** Claude Code Max Opus 4.5

## Skills Updated (22 total)

### Web Development & Full-Stack
- [ ] nextjs-app-router-skill.md - v1.1.0 → v1.2.0
  - Updated: Next.js 15 latest features
  - Changes: [list changes]
- [ ] tailwind-design-system-skill.md - v1.0.0 → v1.1.0
  ...

[Continue for all 22 skills]

## Plugin Documentation Updated

### Superpowers
- Version: [current version]
- Changes: [list changes]

### MCP Integration
- Protocol Version: [version]
- Changes: [list changes]

### Context7 MCP
- Status: [current status]
- Changes: [list changes]

## Main Documentation Updated

- README.md: [changes]
- skills/README.md: [changes]
- Claude-Prompt-Guide.md: [changes]

## Issues Found and Resolved

1. [Issue 1]
2. [Issue 2]
...

## Recommendations for Future Updates

1. [Recommendation 1]
2. [Recommendation 2]
...
```

#### Update CHANGELOG.md

Add entry at the top:

```markdown
## [Unreleased] - 2026-01-31

### Updated
- All 22 skills updated to latest library versions
- Skills compatibility updated to Claude 4.5 models
- Plugin documentation refreshed (Superpowers, MCP, Context7)
- Version numbers incremented across all skills
- Updated dates throughout documentation

### Fixed
- [List any bugs or issues fixed]

### Added
- [List any new content added]

### Removed
- [List any deprecated content removed]
```

---

## ⚙️ Execution Instructions

### Prerequisites

1. **Environment Setup**
   ```bash
   cd /home/runner/work/claude-prompt-engineering-guide/claude-prompt-engineering-guide
   git checkout -b auto-update-jan-2026
   ```

2. **Verify Git Configuration**
   ```bash
   git config user.name "Claude Code Max Opus 4.5"
   git config user.email "claude-code@anthropic.com"
   ```

### Execution Order

Execute the phases in order:

```bash
# Phase 1: Analysis
echo "Phase 1: Pre-Update Analysis"
# [Run Phase 1 tasks]

# Phase 2: Skills Updates
echo "Phase 2: Updating 22 Skills"
# [Update skills systematically]

# Phase 3: Plugin Documentation
echo "Phase 3: Plugin Documentation Updates"
# [Update plugin docs]

# Phase 4: Main Documentation
echo "Phase 4: Main Documentation Updates"
# [Update main docs]

# Phase 5: Validation
echo "Phase 5: Validation & Testing"
# [Run all validation checks]

# Phase 6: Documentation
echo "Phase 6: Creating Update Summary"
# [Generate summaries]
```

### Git Commit Strategy

Use atomic commits for each major section:

```bash
# After Phase 2 (per category)
git add skills/examples/nextjs-*.md skills/examples/tailwind-*.md ...
git commit -m "Update Web Development & Full-Stack skills (4 skills)"

git add skills/examples/aws-*.md skills/examples/google-*.md ...
git commit -m "Update Backend & Infrastructure skills (4 skills)"

# After Phase 3
git commit -m "Update plugin documentation (Superpowers, MCP, Context7)"

# After Phase 4
git commit -m "Update main documentation files"

# Final commit
git commit -m "Add update summary and changelog entry"
```

---

## 🎯 Success Criteria

### Must Have (100% Required)

- ✅ All 22 skills updated with correct version numbers
- ✅ All 22 skills have updated dates (2026-01-31)
- ✅ All skills reference Claude 4.5 models
- ✅ All plugin documentation verified and updated
- ✅ No broken internal links
- ✅ No references to outdated Claude 3 models
- ✅ Validation checks pass
- ✅ Update summary document created
- ✅ CHANGELOG.md updated

### Should Have (90% Target)

- ✅ All code examples verified for syntax
- ✅ All library versions updated to latest stable
- ✅ All external links verified (or marked as deprecated)
- ✅ Troubleshooting sections enhanced
- ✅ Performance tips updated
- ✅ Security best practices current

### Nice to Have (Bonus)

- ✅ New examples added where valuable
- ✅ Additional best practices documented
- ✅ Enhanced cross-referencing between skills
- ✅ Token optimization improvements
- ✅ Visual diagrams or flowcharts (if appropriate)

---

## 🚨 Important Notes

### Critical Guidelines

1. **Preserve User Content**
   - NEVER delete working code or examples
   - NEVER remove features unless explicitly deprecated
   - ALWAYS maintain backward compatibility where possible

2. **Version Increment Rules**
   - Be conservative with major version bumps
   - Document breaking changes clearly
   - Use semantic versioning consistently

3. **Quality Over Speed**
   - Take time to verify each update
   - Don't rush through validation
   - Document all changes clearly

4. **Reference Verification**
   - Check official documentation for accuracy
   - Verify library/framework versions exist
   - Test code snippets when possible

### Common Pitfalls to Avoid

- ❌ Blindly updating version numbers without checking compatibility
- ❌ Breaking working code examples
- ❌ Introducing security vulnerabilities
- ❌ Creating inconsistencies between documents
- ❌ Forgetting to update dates
- ❌ Leaving TODO comments in production
- ❌ Updating links without verifying they work

---

## 📊 Progress Tracking

Use this checklist during execution:

### Phase 1: Pre-Update Analysis
- [ ] Created baseline document
- [ ] Researched latest versions
- [ ] Documented current state

### Phase 2: Skills Updates

**Web Development (4)**
- [ ] nextjs-app-router-skill.md
- [ ] tailwind-design-system-skill.md
- [ ] nextauth-authentication-skill.md
- [ ] api-development-skill.md

**Backend & Infrastructure (4)**
- [ ] aws-cloud-infrastructure-skill.md
- [ ] google-cloud-platform-skill.md
- [ ] neon-serverless-skill.md
- [ ] prisma-orm-skill.md

**Testing & QA (4)**
- [ ] testing-skill.md
- [ ] vitest-unit-testing-skill.md
- [ ] playwright-e2e-testing-skill.md
- [ ] code-review.md

**DevOps & Deployment (4)**
- [ ] vercel-deployment-skill.md
- [ ] database-migrations.md
- [ ] monitoring-logging-skill.md
- [ ] git-workflow-skill.md

**Standards & Best Practices (6)**
- [ ] typescript-standards.md
- [ ] performance-optimization-skill.md
- [ ] seo-optimization-skill.md
- [ ] security-compliance.md
- [ ] accessibility-ux.md
- [ ] example-feedback-analyzer.md

### Phase 3: Plugin Documentation
- [ ] superpowers-guide.md
- [ ] mcp-integration.md
- [ ] mcp-ecosystem-overview.md
- [ ] skills-guide.md
- [ ] cowork-guide.md

### Phase 4: Main Documentation
- [ ] README.md
- [ ] skills/README.md
- [ ] Claude-Prompt-Guide.md

### Phase 5: Validation
- [ ] Automated link checks passed
- [ ] Model reference checks passed
- [ ] Date consistency verified
- [ ] Manual spot checks completed

### Phase 6: Documentation
- [ ] Update summary created
- [ ] CHANGELOG.md updated
- [ ] Git commits made with clear messages

---

## 🔧 Tools and Resources

### Research Resources

- **Anthropic Official Docs**: https://docs.anthropic.com
- **MCP Protocol**: https://modelcontextprotocol.io
- **Superpowers GitHub**: https://github.com/obra/superpowers-chrome
- **Next.js Docs**: https://nextjs.org/docs
- **TypeScript Docs**: https://www.typescriptlang.org/docs
- **npm Registry**: https://www.npmjs.com

### Validation Commands

```bash
# Find all markdown files
find . -name "*.md" -type f

# Check for specific patterns
rg "version:" skills/examples/
rg "updated:" skills/examples/
rg "Claude (3|Opus 3|Sonnet 3|Haiku 3)" --type md

# Validate YAML frontmatter
for f in skills/examples/*.md; do
  echo "Checking $f"
  head -n 15 "$f" | grep "^---$" | wc -l
done

# Check for broken relative links
grep -r "](\./" --include="*.md" .
```

### File Listing

```bash
# List all skills with metadata
for file in skills/examples/*.md; do
  echo "=== $(basename $file) ==="
  grep -A 5 "^---$" "$file" | head -n 6
  echo ""
done
```

---

## 📝 Final Deliverables

After completing all phases, you should have:

1. **Updated Skills** (22 files)
   - All in `skills/examples/`
   - Version numbers incremented
   - Dates updated
   - Content verified and enhanced

2. **Updated Plugin Docs** (5 files)
   - superpowers-guide.md
   - mcp-integration.md
   - mcp-ecosystem-overview.md
   - skills-guide.md
   - cowork-guide.md

3. **Updated Main Docs** (3 files)
   - README.md
   - skills/README.md
   - Claude-Prompt-Guide.md

4. **Update Summary** (1 file)
   - `/tmp/update-summary-2026-01-31.md`
   - Detailed changelog of all updates

5. **CHANGELOG Entry** (1 update)
   - New entry in CHANGELOG.md
   - Dated January 31, 2026

6. **Git Commits**
   - Clean, atomic commits
   - Clear commit messages
   - Ready for PR/merge

---

## 🎓 Execution Tips

### For Maximum Efficiency

1. **Batch Similar Updates**
   - Update all metadata in one pass
   - Update all dates in one pass
   - Update all model references together

2. **Use Search and Replace Wisely**
   ```bash
   # Replace Claude 3 references
   find . -name "*.md" -exec sed -i 's/Claude 3\.5/Claude 4.5/g' {} \;
   
   # Update dates
   find skills/examples -name "*.md" -exec sed -i 's/updated: 2026-01-../updated: 2026-01-31/g' {} \;
   ```

3. **Verify As You Go**
   - Don't wait until the end to validate
   - Check each section after updating
   - Catch errors early

4. **Use Version Control**
   ```bash
   # Make checkpoints
   git add -A
   git commit -m "WIP: Completed Phase 2 - Skills updates"
   ```

5. **Take Breaks**
   - Phase 1: 15 min → checkpoint
   - Phase 2: 60-90 min → checkpoint
   - Phase 3: 30-45 min → checkpoint
   - Phase 4: 20-30 min → checkpoint
   - Phase 5: 15-20 min → checkpoint
   - Phase 6: 10-15 min → final commit

### Quality Assurance

- Read through at least 5 random skills completely
- Test 10+ random internal links
- Verify 5+ code examples syntax
- Check consistency of 3+ cross-references
- Spot-check dates in 10+ files

---

## 🏁 Completion Statement

When finished, provide a summary like:

```
✅ COMPLETE: Auto-Update All Plugins and Skills

Summary:
- 22 skills updated successfully
- 5 plugin documentation files updated
- 3 main documentation files updated
- 0 broken links found
- 0 validation errors
- All changes committed to branch: auto-update-jan-2026

Key Changes:
- Version numbers incremented appropriately
- All dates updated to 2026-01-31
- Model references updated to Claude 4.5
- Library versions updated to latest stable
- Code examples verified
- Documentation enhanced

Files Modified: [list count]
Lines Changed: [approximate count]
Validation Checks Passed: [count/total]

Ready for review and merge.
```

---

**End of Prompt**

---

## 📚 Appendix: Skill Update Template

For quick reference, use this template for each skill:

```markdown
<!-- Skills Update Checklist for: [SKILL_NAME] -->

## Pre-Update
- [ ] Current version: _____
- [ ] Current updated date: _____
- [ ] Current compatibility: _____

## Metadata Updates
- [ ] Increment version number
- [ ] Update date to 2026-01-31
- [ ] Update compatibility to Claude 4.5 models
- [ ] Verify allowed-tools are correct

## Content Updates
- [ ] Check all code examples for syntax
- [ ] Update library/framework versions
- [ ] Verify API methods are current
- [ ] Update deprecated features
- [ ] Enhance examples if needed
- [ ] Update troubleshooting section
- [ ] Verify all links work

## Quality Checks
- [ ] All sections present
- [ ] Formatting consistent
- [ ] No TODO/FIXME comments
- [ ] Token count reasonable
- [ ] No security issues

## Post-Update
- [ ] New version: _____
- [ ] Changes documented: _____
- [ ] Ready for commit: Yes/No
```

---

**Total Estimated Time:** 2.5 - 3.5 hours for complete execution  
**Recommended Model:** Claude Code Max Opus 4.5 with effort: high  
**Context Windows Required:** 1-2 (with progressive disclosure)

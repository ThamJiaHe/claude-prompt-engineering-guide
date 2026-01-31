# Using the Auto-Update Prompt: Step-by-Step Guide

This guide shows you exactly how to use the `auto-update-plugins-skills.md` prompt to update all plugins and skills in this repository.

## Prerequisites

1. **Claude Code Installed**
   ```bash
   # Check if Claude Code is installed
   claude-code --version
   ```

2. **Repository Cloned**
   ```bash
   git clone https://github.com/ThamJiaHe/claude-prompt-engineering-guide.git
   cd claude-prompt-engineering-guide
   ```

3. **Clean Working Directory**
   ```bash
   git status
   # Should show no uncommitted changes
   ```

## Step 1: Read the Prompt

First, familiarize yourself with what the prompt will do:

```bash
cat prompts/auto-update-plugins-skills.md
```

**Key things to note:**
- Updates all 22 skills
- Updates plugin documentation
- Takes 2.5-3.5 hours
- Creates detailed update summary
- Validates all changes

## Step 2: Launch Claude Code with Opus 4.5

Open a new terminal in the repository root:

```bash
cd /path/to/claude-prompt-engineering-guide

# Launch Claude Code with Opus 4.5 and high effort
claude-code --model opus-4.5 --effort high
```

Or if using the Claude Desktop app, open it and ensure you're using Claude Opus 4.5.

## Step 3: Copy and Paste the Entire Prompt

**Option A: Copy from file**
```bash
# Copy the entire file content
cat prompts/auto-update-plugins-skills.md | pbcopy  # macOS
cat prompts/auto-update-plugins-skills.md | xclip -selection clipboard  # Linux
```

**Option B: Manual copy**
1. Open `prompts/auto-update-plugins-skills.md` in your editor
2. Select all (Ctrl+A / Cmd+A)
3. Copy (Ctrl+C / Cmd+C)
4. Paste into Claude Code

## Step 4: Let Claude Execute

After pasting the prompt, Claude will:

1. **Phase 1** (15 min): Analyze current state
   - Lists all skills and versions
   - Checks for updates needed
   - Documents baseline

2. **Phase 2** (60-90 min): Update all 22 skills
   - Updates metadata
   - Checks code examples
   - Verifies library versions
   - Updates documentation

3. **Phase 3** (30-45 min): Update plugin docs
   - Superpowers guide
   - MCP integration
   - Skills system docs
   - Claude Cowork guide

4. **Phase 4** (20-30 min): Update main docs
   - README.md
   - skills/README.md
   - Claude-Prompt-Guide.md

5. **Phase 5** (15-20 min): Validate everything
   - Check links
   - Verify syntax
   - Test references

6. **Phase 6** (10-15 min): Document changes
   - Create summary
   - Update CHANGELOG

## Step 5: Review Claude's Work

After Claude completes, review the changes:

```bash
# See what files were modified
git status

# Review the changes
git diff

# Check the update summary
cat /tmp/update-summary-2026-01-31.md
```

**Key things to verify:**
- ✅ All 22 skills have updated versions
- ✅ Dates are current (2026-01-31)
- ✅ No broken links
- ✅ Code examples look correct
- ✅ CHANGELOG.md is updated

## Step 6: Test Critical Paths

Manually test a few things:

```bash
# Check that key links work
cat skills/README.md | grep "\.md" | head -5

# Verify skill metadata
head -n 10 skills/examples/nextjs-app-router-skill.md

# Check version consistency
grep "version:" skills/examples/*.md

# Check dates are updated
grep "updated:" skills/examples/*.md
```

## Step 7: Commit and Push

If everything looks good:

```bash
# If Claude created a branch
git checkout -b auto-update-jan-2026

# Or use Claude's branch
git status

# Review the commits
git log --oneline -10

# Push to GitHub
git push origin HEAD
```

## Step 8: Create Pull Request

1. Go to GitHub repository
2. You should see a prompt to create PR
3. Review the changes in the PR
4. Add any additional notes
5. Merge when ready

## Example Session

Here's what a typical session looks like:

```
You: [Paste entire prompt from auto-update-plugins-skills.md]

Claude: I'll systematically update all 22 skills and plugin documentation.
        Starting Phase 1: Pre-Update Analysis...

        [15 minutes later]
        ✓ Phase 1 complete. Found:
        - 22 skills to update
        - 5 plugin docs to verify
        - 3 main docs to update
        
        Starting Phase 2: Skills Updates...
        
        [90 minutes later]
        ✓ Phase 2 complete. Updated all 22 skills:
        - Web Development: 4 skills updated
        - Backend: 4 skills updated
        - Testing: 4 skills updated
        - DevOps: 4 skills updated
        - Standards: 6 skills updated
        
        [continues through all phases...]
        
        ✓ All phases complete!
        
        Summary:
        - 22 skills updated successfully
        - 5 plugin docs updated
        - 3 main docs updated
        - 0 broken links
        - All validation checks passed
        
        Created: /tmp/update-summary-2026-01-31.md

You: Great! Let me review the changes before committing.

Claude: Here's what I modified:
        [Lists all files and key changes]

You: Looks good. Please commit these changes.

Claude: [Creates commits and pushes to branch]
        ✓ All changes committed to branch: auto-update-jan-2026
        Ready for review and merge.
```

## Troubleshooting

### Claude Stops Mid-Execution

**Solution**: Continue from where it stopped
```
You: Continue with Phase [N] where you left off
```

### Too Many Changes at Once

**Solution**: Break into smaller chunks
```
You: Update only the Web Development skills (4 skills) first
```

### Need to Revert Changes

**Solution**: Use git
```bash
git reset --hard HEAD
git clean -fd
```

### Claude Makes Incorrect Updates

**Solution**: Give specific feedback
```
You: The version for nextjs-app-router-skill.md should be 1.2.0, not 2.0.0
     because this is a minor update, not a major breaking change.
```

## Tips for Best Results

1. **Use High Effort Mode**
   - Ensures thorough checking
   - Better validation
   - More accurate updates

2. **Review Phase by Phase**
   - Check after each phase completes
   - Catch issues early
   - Guide corrections if needed

3. **Spot Check Random Skills**
   - Don't rely on automation alone
   - Verify 5-10 random files
   - Check code examples manually

4. **Test Links Manually**
   - Click through key navigation
   - Verify external links
   - Check relative paths

5. **Read the Update Summary**
   - Understand what changed
   - Note any issues found
   - Review recommendations

## What to Do After

1. **Announce the Update**
   - Create a release note
   - Share in discussions
   - Update any dependent projects

2. **Monitor for Issues**
   - Watch for bug reports
   - Check community feedback
   - Fix any problems quickly

3. **Document Learnings**
   - What worked well?
   - What could improve?
   - Update this guide

4. **Schedule Next Update**
   - Set quarterly reminder
   - After major Claude releases
   - When dependencies update

## Next Steps

- Set a calendar reminder for next quarterly update
- Share this guide with team members
- Contribute improvements to the prompt
- Create additional automation prompts for other tasks

---

**Questions?** Open an issue or discussion on GitHub.

**Last Updated:** January 31, 2026  
**Estimated Time:** 2.5-3.5 hours  
**Success Rate:** High (when following all steps)

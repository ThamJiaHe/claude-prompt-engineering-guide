# Activity Timeline

> **Chronological record of all significant actions.**
> Auto-populate via hooks or update manually.

---

## How to Use with Claude

1. **Debugging:** Trace back to find when something changed
2. **Audit:** Review what tools were used for compliance
3. **Learning:** Understand patterns in your workflow
4. **Handoffs:** Show exactly what happened in previous sessions

**Log every:**
- File creation/modification
- Git operations (commit, push, merge)
- Tool invocations (Claude Code, OpenCode, Codex)
- External API calls
- Significant decisions

---

## Activity Log

| Timestamp | Action | Tool | Notes |
|-----------|--------|------|-------|
| 2026-01-27 00:00 | Started project | - | Initial setup |
|  |  |  |  |

---

## Claude Instructions

```xml
<activity_rules>
When logging activities:

1. ADD entry immediately after significant actions
2. USE ISO timestamp format: YYYY-MM-DD HH:MM
3. SPECIFY the tool used (Claude Code, OpenCode, Codex, Git, etc.)
4. KEEP notes brief but informative
5. LOG failures as well as successes

Actions to always log:
- File creation or major edits
- Git commits, merges, branch operations
- Test runs (especially failures)
- Deployments
- External service integrations
- Key decisions or direction changes

Format:
| YYYY-MM-DD HH:MM | Action description | Tool name | Brief notes |
</activity_rules>
```

---

## Hook Integration (Optional)

You can auto-populate this file using Claude Code hooks:

```javascript
// .claude/hooks/post-tool.js
const fs = require('fs');
const path = require('path');

module.exports = async function(context) {
  const timestamp = new Date().toISOString().slice(0, 16).replace('T', ' ');
  const entry = `| ${timestamp} | ${context.action} | ${context.tool} | ${context.notes || '-'} |\n`;

  const activityPath = path.join(process.cwd(), 'planning/activity.md');

  // Append to activity log
  const content = fs.readFileSync(activityPath, 'utf8');
  const updated = content.replace(
    /(\| Timestamp \| Action.*?\n\|[-| ]+\n)/,
    `$1${entry}`
  );
  fs.writeFileSync(activityPath, updated);
};
```

---

## Archive

<details>
<summary>Older activity entries (rotate weekly)</summary>

| Timestamp | Action | Tool | Notes |
|-----------|--------|------|-------|
|  |  |  |  |

</details>

---

*Template version: 1.0 | January 2026*

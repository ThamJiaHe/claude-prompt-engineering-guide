# Automated Research System Guide

> **Version:** 1.0.0 | **Last Updated:** January 27, 2026

This guide explains how to set up, configure, and maintain the automated daily research system for the Claude Prompt Engineering Guide repository.

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Setup Instructions](#setup-instructions)
- [Configuration](#configuration)
- [Workflow Details](#workflow-details)
- [Scripts Reference](#scripts-reference)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Maintenance](#maintenance)
- [Security Considerations](#security-considerations)

---

## Overview

The automated research system keeps the Claude Prompt Engineering Guide up-to-date by:

1. **Daily Research**: Searching for new Claude/Anthropic updates via Perplexity API
2. **Analysis**: Evaluating findings for relevance and impact
3. **Documentation Updates**: Automatically updating metadata and flagging content changes
4. **Pull Request Creation**: Creating PRs for human review
5. **Notifications**: Alerting maintainers via GitHub notifications

### Key Principles

- **Human-in-the-Loop**: All substantial changes require human review
- **Conservative Updates**: Only metadata/dates are auto-updated
- **Source Verification**: All claims are linked to original sources
- **Rollback Ready**: Changes can be easily reverted

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    GitHub Actions Workflow                       │
│                 (.github/workflows/daily-research.yml)           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Research Phase                              │
│                  (scripts/auto-research.py)                      │
│                                                                  │
│  • Perplexity API searches (with recency filtering)             │
│  • GitHub API (releases, issues)                                 │
│  • Output: output/research_findings.json                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Analysis Phase                              │
│                 (scripts/analyze-findings.py)                    │
│                                                                  │
│  • Categorize findings by topic                                  │
│  • Assess impact (high/medium/low)                              │
│  • Generate update recommendations                               │
│  • Output: output/analysis_results.json                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Update Phase                                │
│                  (scripts/auto-update.py)                        │
│                                                                  │
│  • Update dates/metadata (automatic)                            │
│  • Flag substantial changes (for review)                        │
│  • Bump version if needed                                       │
│  • Update CHANGELOG.md                                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Validation Phase                              │
│                 (scripts/validate-updates.py)                    │
│                                                                  │
│  • Markdown syntax validation                                    │
│  • Internal link checking                                       │
│  • Version consistency                                          │
│  • Sensitive data detection                                     │
│  • JSON validation                                              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   Pull Request Creation                          │
│                                                                  │
│  • Create branch: auto-update/YYYY-MM-DD                        │
│  • Commit changes                                                │
│  • Create PR with detailed template                             │
│  • Add labels: automated, documentation, needs-review           │
└─────────────────────────────────────────────────────────────────┘
```

---

## Setup Instructions

### Prerequisites

- GitHub repository with Actions enabled
- Perplexity API key
- Python 3.9+
- (Optional) Anthropic API key for Claude-based analysis

### Step 1: Set Up Repository Secrets

Navigate to **Settings → Secrets and variables → Actions** and add:

| Secret Name | Description | Required |
|-------------|-------------|----------|
| `PERPLEXITY_API_KEY` | Perplexity API key for web search | Yes |
| `ANTHROPIC_API_KEY` | Claude API key for analysis (optional) | No |

### Step 2: Enable GitHub Actions

1. Go to **Actions** tab in your repository
2. Enable workflows if prompted
3. The workflow will run automatically at the scheduled time

### Step 3: Verify Directory Structure

Ensure these directories exist:

```bash
mkdir -p .github/workflows
mkdir -p scripts
mkdir -p config
mkdir -p output
mkdir -p docs
```

### Step 4: Test the Workflow

Run a manual test:

```bash
# Trigger workflow manually from GitHub UI
# OR run locally:
python scripts/auto-research.py
python scripts/analyze-findings.py
python scripts/auto-update.py
python scripts/validate-updates.py
```

---

## Configuration

### Search Queries (`config/search-queries.json`)

Define what to search for:

```json
{
  "version": "1.0",
  "all": [
    "Claude AI updates this week 2026",
    "Anthropic Claude Code CLI latest release"
  ],
  "claude-models": [
    "Claude Opus 4.5 updates features"
  ],
  "recency_settings": {
    "default": "week",
    "urgent_topics": ["pricing", "api"],
    "urgent_recency": "day"
  },
  "source_priorities": {
    "official": ["anthropic.com", "docs.anthropic.com"],
    "trusted": ["github.com", "news.ycombinator.com"]
  }
}
```

### Update Rules (`config/auto-update-rules.json`)

Define how findings map to documentation:

```json
{
  "version": "1.0",
  "topic_mappings": {
    "claude_models": {
      "keywords": ["Opus", "Sonnet", "Haiku", "model"],
      "target_files": ["Claude-Prompt-Guide.md"],
      "target_sections": ["## Claude Models Overview"]
    }
  },
  "auto_update_rules": {
    "always_update": ["footer_dates", "version_references"],
    "flag_for_review": ["pricing_tables", "feature_lists"]
  }
}
```

### Workflow Schedule

The default schedule is **2:00 AM SGT (18:00 UTC)**:

```yaml
on:
  schedule:
    - cron: '0 18 * * *'  # 6 PM UTC = 2 AM SGT
```

To change the schedule, edit `.github/workflows/daily-research.yml`.

---

## Workflow Details

### Triggers

| Trigger | Description |
|---------|-------------|
| `schedule` | Daily at 2:00 AM SGT |
| `workflow_dispatch` | Manual trigger from GitHub UI |

### Jobs

1. **research**: Fetches latest information from Perplexity and GitHub
2. **update**: Analyzes findings and updates documentation
3. **create-pr**: Creates a pull request if changes were made
4. **notify**: Sends notifications (via GitHub PR notifications)

### Artifacts

The workflow produces artifacts for debugging:

- `research-findings`: Raw research data
- `analysis-results`: Analysis output
- `update-results`: Update execution log

---

## Scripts Reference

### `auto-research.py`

**Purpose**: Fetch latest Claude/Anthropic information

**Key Functions**:
- `search_perplexity()`: Web search via Perplexity API
- `fetch_github_releases()`: Get latest releases from anthropics repos
- `fetch_github_issues()`: Get recent issues/discussions

**Output**: `output/research_findings.json`

**Usage**:
```bash
python scripts/auto-research.py
```

### `analyze-findings.py`

**Purpose**: Analyze and categorize research findings

**Key Functions**:
- `categorize_findings()`: Map findings to topics
- `assess_impact()`: Determine priority level
- `generate_recommendations()`: Create update suggestions

**Output**: `output/analysis_results.json`

**Usage**:
```bash
python scripts/analyze-findings.py
```

### `auto-update.py`

**Purpose**: Apply updates to documentation

**Key Functions**:
- `update_dates()`: Update footer dates
- `bump_version()`: Increment version number
- `update_changelog()`: Add changelog entry
- `flag_substantial_changes()`: Mark content for review

**Output**: Modified files + `output/update_log.json`

**Usage**:
```bash
python scripts/auto-update.py
```

### `validate-updates.py`

**Purpose**: Validate all changes before PR creation

**Validations**:
- Markdown syntax (unclosed code blocks, malformed headers)
- Internal links (broken references)
- Version consistency (VERSION file matches INDEX.md)
- Sensitive data detection (API keys, passwords)
- JSON validity (config files)

**Exit Codes**:
- `0`: All validations passed
- `1`: Validation errors found

**Usage**:
```bash
python scripts/validate-updates.py
```

---

## Customization

### Adding New Topics

1. Add search queries to `config/search-queries.json`:
   ```json
   "new_topic": [
     "search query 1",
     "search query 2"
   ]
   ```

2. Add topic mapping to `config/auto-update-rules.json`:
   ```json
   "new_topic": {
     "keywords": ["keyword1", "keyword2"],
     "target_files": ["docs/new-topic.md"],
     "target_sections": ["## Section Name"]
   }
   ```

### Modifying Schedule

Edit the cron expression in `.github/workflows/daily-research.yml`:

```yaml
schedule:
  - cron: '0 12 * * *'  # 12:00 UTC daily
  - cron: '0 0 * * 1'   # Monday at midnight UTC (weekly)
```

### Adding New Validations

Edit `scripts/validate-updates.py`:

```python
def validate_custom_rule(filepath: str) -> List[ValidationError]:
    errors = []
    # Your validation logic
    return errors

# Add to main():
errors = validate_custom_rule(filepath)
all_errors.extend(errors)
```

---

## Troubleshooting

### Common Issues

#### 1. Workflow Not Running

**Symptoms**: No workflow runs at scheduled time

**Solutions**:
- Check Actions are enabled in repository settings
- Verify cron syntax is correct
- Ensure branch has the workflow file
- Check GitHub Actions quotas

#### 2. Perplexity API Errors

**Symptoms**: Research phase fails with API errors

**Solutions**:
- Verify `PERPLEXITY_API_KEY` secret is set
- Check API key is valid and has quota
- Review rate limiting (1 request/second default)

#### 3. Validation Failures

**Symptoms**: PR not created, validation step fails

**Solutions**:
- Run `python scripts/validate-updates.py` locally
- Check for unclosed code blocks in markdown
- Verify all internal links point to existing files
- Ensure VERSION file matches INDEX.md

#### 4. No Changes Detected

**Symptoms**: Workflow completes but no PR created

**Cause**: No significant updates found

**Solution**: This is expected behavior when no new information is available

### Debug Mode

Run scripts with verbose logging:

```bash
# Set log level
export LOG_LEVEL=DEBUG

# Run scripts
python scripts/auto-research.py
python scripts/analyze-findings.py
python scripts/auto-update.py
python scripts/validate-updates.py
```

### Accessing Logs

1. Go to **Actions** tab in GitHub
2. Click on the workflow run
3. Expand job steps to see logs
4. Download artifacts for detailed output

---

## Maintenance

### Weekly Tasks

- [ ] Review and merge pending automated PRs
- [ ] Check for failed workflow runs
- [ ] Verify search queries are returning relevant results

### Monthly Tasks

- [ ] Review and update search queries
- [ ] Audit topic-to-file mappings
- [ ] Update source priority lists
- [ ] Check for new official sources to monitor

### Quarterly Tasks

- [ ] Review automation effectiveness
- [ ] Update validation rules
- [ ] Audit security configuration
- [ ] Update API integrations if needed

---

## Security Considerations

### API Key Management

- **Never commit API keys** to the repository
- Use GitHub Secrets for all credentials
- Rotate keys periodically
- Use minimum required permissions

### Sensitive Data Detection

The validation script scans for:
- API keys (`sk-...`, `ghp_...`, `AKIA...`)
- Hardcoded passwords
- Hardcoded secrets

### Access Control

- Limit who can modify workflow files
- Require reviews for PRs touching automation code
- Use branch protection rules

### Rate Limiting

The automation includes:
- 1 second delay between Perplexity requests
- Capped search results (20 per query)
- Daily execution limit (1 run per day by default)

---

## Appendix

### File Locations

| File | Purpose |
|------|---------|
| `.github/workflows/daily-research.yml` | GitHub Actions workflow |
| `scripts/auto-research.py` | Research fetching |
| `scripts/analyze-findings.py` | Analysis and categorization |
| `scripts/auto-update.py` | Documentation updates |
| `scripts/validate-updates.py` | Validation checks |
| `config/search-queries.json` | Search configuration |
| `config/auto-update-rules.json` | Update rules |
| `.github/pr-template-automated.md` | PR template |
| `output/` | Runtime artifacts |

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PERPLEXITY_API_KEY` | Perplexity API key | Required |
| `ANTHROPIC_API_KEY` | Claude API key | Optional |
| `GITHUB_TOKEN` | GitHub token (auto-provided) | Auto |
| `LOG_LEVEL` | Logging verbosity | INFO |

### Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-27 | Initial release |

---

## Support

For issues with the automation system:

1. Check [Troubleshooting](#troubleshooting) section
2. Review workflow logs in GitHub Actions
3. Open an issue with the `automation` label

---

**Documentation maintained by**: Claude Prompt Engineering Guide Team
**Last Updated**: January 27, 2026

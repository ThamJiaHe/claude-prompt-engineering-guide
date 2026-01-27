#!/usr/bin/env python3
"""
Auto-Research Script for Claude Ecosystem Updates

This script searches for Claude-related updates using Perplexity API and GitHub API.
It outputs structured findings to output/research_findings.json.

Environment Variables:
    PERPLEXITY_API_KEY: API key for Perplexity search
    SEARCH_SCOPE: Scope of search (all, claude-models, claude-code, mcp, pricing, tools)
    LAST_SEARCH_DATE: Date to filter results from (YYYY-MM-DD)

Output:
    output/research_findings.json: Structured research findings
    output/raw_responses/: Raw API responses for debugging
"""

import os
import json
import logging
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
OUTPUT_DIR = Path("output")
RAW_RESPONSES_DIR = OUTPUT_DIR / "raw_responses"
CONFIG_DIR = Path("config")

# Ensure output directories exist
OUTPUT_DIR.mkdir(exist_ok=True)
RAW_RESPONSES_DIR.mkdir(exist_ok=True)


def load_search_queries() -> dict:
    """Load search queries from config file."""
    config_path = CONFIG_DIR / "search-queries.json"
    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)

    # Default queries if config doesn't exist
    return {
        "all": [
            "Claude AI updates January 2026",
            "Anthropic Claude Code CLI new features",
            "Claude MCP Model Context Protocol updates",
            "Claude API pricing changes 2026",
            "Claude Skills marketplace new",
            "OpenCode CLI vs Claude Code",
            "Claude Opus Sonnet Haiku updates"
        ],
        "claude-models": [
            "Claude Opus 4.5 updates",
            "Claude Sonnet 4.5 new features",
            "Anthropic model releases 2026"
        ],
        "claude-code": [
            "Claude Code CLI updates",
            "Claude Code new features",
            "Claude Code vs Cursor vs Continue"
        ],
        "mcp": [
            "Model Context Protocol updates",
            "MCP servers new releases",
            "Claude MCP integrations"
        ],
        "pricing": [
            "Claude API pricing 2026",
            "Anthropic pricing changes",
            "Claude tokens cost comparison"
        ],
        "tools": [
            "Claude ecosystem tools",
            "OpenCode CLI updates",
            "AirLLM Claude integration"
        ]
    }


def search_perplexity(query: str, api_key: str, recency: str = "week") -> Optional[dict]:
    """
    Search using Perplexity API.

    Args:
        query: Search query string
        api_key: Perplexity API key
        recency: Time filter (day, week, month, year)

    Returns:
        Search results or None if failed
    """
    url = "https://api.perplexity.ai/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": [
            {
                "role": "system",
                "content": "You are a research assistant. Provide factual, up-to-date information with sources. Focus on recent developments and concrete facts."
            },
            {
                "role": "user",
                "content": f"Search for the latest information on: {query}. Include specific dates, version numbers, and source URLs where available."
            }
        ],
        "temperature": 0.2,
        "max_tokens": 1000,
        "return_citations": True,
        "search_recency_filter": recency
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Perplexity search failed for '{query}': {e}")
        return None


def search_github_releases(repo: str) -> Optional[list]:
    """
    Fetch recent releases from a GitHub repository.

    Args:
        repo: Repository in format "owner/repo"

    Returns:
        List of recent releases or None if failed
    """
    url = f"https://api.github.com/repos/{repo}/releases"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Claude-Research-Bot"
    }

    # Add token if available
    github_token = os.environ.get("GITHUB_TOKEN")
    if github_token:
        headers["Authorization"] = f"token {github_token}"

    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        releases = response.json()

        # Return only recent releases (last 30 days)
        cutoff = datetime.now() - timedelta(days=30)
        recent = []
        for release in releases[:10]:  # Check last 10
            published = datetime.fromisoformat(release["published_at"].replace("Z", "+00:00"))
            if published.replace(tzinfo=None) > cutoff:
                recent.append({
                    "tag": release["tag_name"],
                    "name": release["name"],
                    "published": release["published_at"],
                    "url": release["html_url"],
                    "body": release["body"][:500] if release["body"] else ""
                })
        return recent
    except requests.RequestException as e:
        logger.warning(f"GitHub releases fetch failed for {repo}: {e}")
        return None


def search_github_issues(repo: str, labels: list = None) -> Optional[list]:
    """
    Fetch recent issues/discussions from a GitHub repository.

    Args:
        repo: Repository in format "owner/repo"
        labels: Optional list of labels to filter by

    Returns:
        List of recent issues or None if failed
    """
    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Claude-Research-Bot"
    }

    params = {
        "state": "all",
        "sort": "updated",
        "direction": "desc",
        "per_page": 20
    }

    if labels:
        params["labels"] = ",".join(labels)

    github_token = os.environ.get("GITHUB_TOKEN")
    if github_token:
        headers["Authorization"] = f"token {github_token}"

    try:
        response = requests.get(url, headers=headers, params=params, timeout=15)
        response.raise_for_status()
        issues = response.json()

        # Filter to last 14 days
        cutoff = datetime.now() - timedelta(days=14)
        recent = []
        for issue in issues:
            updated = datetime.fromisoformat(issue["updated_at"].replace("Z", "+00:00"))
            if updated.replace(tzinfo=None) > cutoff:
                recent.append({
                    "number": issue["number"],
                    "title": issue["title"],
                    "state": issue["state"],
                    "updated": issue["updated_at"],
                    "url": issue["html_url"],
                    "labels": [l["name"] for l in issue.get("labels", [])]
                })
        return recent
    except requests.RequestException as e:
        logger.warning(f"GitHub issues fetch failed for {repo}: {e}")
        return None


def run_research(api_key: str, scope: str = "all") -> dict:
    """
    Run the full research process.

    Args:
        api_key: Perplexity API key
        scope: Search scope from config

    Returns:
        Dictionary with all findings
    """
    queries = load_search_queries()
    search_terms = queries.get(scope, queries.get("all", []))

    findings = {
        "timestamp": datetime.now().isoformat(),
        "scope": scope,
        "perplexity_results": [],
        "github_releases": [],
        "github_issues": [],
        "errors": []
    }

    # Perplexity searches
    logger.info(f"Running {len(search_terms)} Perplexity searches...")
    for i, query in enumerate(search_terms):
        logger.info(f"  [{i+1}/{len(search_terms)}] Searching: {query}")
        result = search_perplexity(query, api_key)

        if result:
            findings["perplexity_results"].append({
                "query": query,
                "response": result.get("choices", [{}])[0].get("message", {}).get("content", ""),
                "citations": result.get("citations", [])
            })

            # Save raw response for debugging
            safe_query = query.replace(" ", "_")[:50]
            with open(RAW_RESPONSES_DIR / f"perplexity_{safe_query}.json", "w") as f:
                json.dump(result, f, indent=2)
        else:
            findings["errors"].append(f"Perplexity search failed: {query}")

        # Rate limiting - be nice to the API
        time.sleep(1)

    # GitHub releases from key repositories
    github_repos = [
        "anthropics/anthropic-sdk-python",
        "anthropics/courses",
        "modelcontextprotocol/servers",
        "obra/superpowers-chrome"
    ]

    logger.info(f"Checking {len(github_repos)} GitHub repositories...")
    for repo in github_repos:
        logger.info(f"  Checking releases: {repo}")
        releases = search_github_releases(repo)
        if releases:
            findings["github_releases"].append({
                "repo": repo,
                "releases": releases
            })
        time.sleep(0.5)

    # GitHub issues from anthropic repos (looking for announcements, bugs)
    issue_repos = [
        ("anthropics/anthropic-sdk-python", ["bug", "enhancement"]),
    ]

    logger.info("Checking GitHub issues...")
    for repo, labels in issue_repos:
        logger.info(f"  Checking issues: {repo}")
        issues = search_github_issues(repo, labels)
        if issues:
            findings["github_issues"].append({
                "repo": repo,
                "issues": issues
            })
        time.sleep(0.5)

    return findings


def main():
    """Main entry point."""
    api_key = os.environ.get("PERPLEXITY_API_KEY")
    if not api_key:
        logger.error("PERPLEXITY_API_KEY environment variable not set")
        # Create empty output for workflow to continue
        findings = {
            "timestamp": datetime.now().isoformat(),
            "scope": "none",
            "perplexity_results": [],
            "github_releases": [],
            "github_issues": [],
            "errors": ["PERPLEXITY_API_KEY not set"]
        }
    else:
        scope = os.environ.get("SEARCH_SCOPE", "all")
        logger.info(f"Starting research with scope: {scope}")
        findings = run_research(api_key, scope)

    # Save findings
    output_path = OUTPUT_DIR / "research_findings.json"
    with open(output_path, "w") as f:
        json.dump(findings, f, indent=2)

    logger.info(f"Research complete. Results saved to {output_path}")
    logger.info(f"  Perplexity results: {len(findings['perplexity_results'])}")
    logger.info(f"  GitHub releases found: {sum(len(r['releases']) for r in findings['github_releases'])}")
    logger.info(f"  GitHub issues found: {sum(len(i['issues']) for i in findings['github_issues'])}")
    logger.info(f"  Errors: {len(findings['errors'])}")


if __name__ == "__main__":
    main()

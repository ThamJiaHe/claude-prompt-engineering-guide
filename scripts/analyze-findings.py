#!/usr/bin/env python3
"""
Analyze Research Findings Script

This script analyzes the raw research findings and extracts actionable insights.
It uses Perplexity API (or optionally Claude API) to synthesize and categorize updates.

Environment Variables:
    PERPLEXITY_API_KEY: API key for Perplexity (used for synthesis)
    ANTHROPIC_API_KEY: Optional Claude API key (preferred if available)

Input:
    output/research_findings.json: Raw research data

Output:
    output/analysis_summary.json: Structured analysis with recommendations
    output/update_recommendations.json: Specific file update suggestions
"""

import os
import json
import logging
from datetime import datetime
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
CONFIG_DIR = Path("config")


def load_update_rules() -> dict:
    """Load topic-to-file mapping rules from config."""
    config_path = CONFIG_DIR / "auto-update-rules.json"
    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)

    # Default rules
    return {
        "topics": {
            "claude_models": {
                "keywords": ["Opus", "Sonnet", "Haiku", "model", "release", "version"],
                "target_files": ["Claude-Prompt-Guide.md"],
                "sections": ["## Claude Models Overview", "## Claude vs Competition"]
            },
            "claude_code": {
                "keywords": ["Claude Code", "CLI", "terminal", "v2.1", "v2.2"],
                "target_files": ["Claude-Prompt-Guide.md", "docs/claude-code-guide.md"],
                "sections": ["### Claude Code"]
            },
            "mcp": {
                "keywords": ["MCP", "Model Context Protocol", "server", "plugin"],
                "target_files": ["docs/mcp-integration.md", "docs/mcp-ecosystem-overview.md"],
                "sections": ["## Model Context Protocol"]
            },
            "pricing": {
                "keywords": ["pricing", "cost", "token", "MTok", "$"],
                "target_files": ["docs/pricing-comparison-jan-2026.md", "Claude-Prompt-Guide.md"],
                "sections": ["## Pricing", "### Pricing"]
            },
            "skills": {
                "keywords": ["Skills", "skill", "marketplace", "plugin"],
                "target_files": ["docs/skills-guide.md", "Claude-Prompt-Guide.md"],
                "sections": ["## Claude Skills", "### Skills"]
            },
            "ecosystem_tools": {
                "keywords": ["OpenCode", "AirLLM", "Codex", "Cursor", "Continue"],
                "target_files": ["docs/research-opencode-clawbot-jan-2026.md", "Claude-Prompt-Guide.md"],
                "sections": ["## Ecosystem Tools"]
            }
        }
    }


def analyze_with_perplexity(content: str, api_key: str) -> Optional[str]:
    """
    Use Perplexity to analyze and synthesize findings.

    Args:
        content: Raw findings to analyze
        api_key: Perplexity API key

    Returns:
        Analysis summary or None if failed
    """
    url = "https://api.perplexity.ai/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    prompt = f"""Analyze the following research findings about Claude AI ecosystem and extract key updates.

For each significant update, identify:
1. What changed (specific version numbers, features, prices)
2. When it happened (dates)
3. Impact level (high/medium/low)
4. Category (models, claude-code, mcp, pricing, skills, ecosystem)

Research findings:
{content[:8000]}

Respond in this exact JSON format:
{{
    "summary": "Brief 2-3 sentence summary of the most important findings",
    "updates": [
        {{
            "title": "Update title",
            "description": "What changed",
            "date": "YYYY-MM-DD or 'recent'",
            "category": "models|claude-code|mcp|pricing|skills|ecosystem",
            "impact": "high|medium|low",
            "source": "Source URL if available"
        }}
    ],
    "no_updates": true/false
}}"""

    payload = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": [
            {
                "role": "system",
                "content": "You are a technical analyst. Extract structured information from research findings. Always respond with valid JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.1,
        "max_tokens": 2000
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        result = response.json()
        return result.get("choices", [{}])[0].get("message", {}).get("content", "")
    except requests.RequestException as e:
        logger.error(f"Perplexity analysis failed: {e}")
        return None


def analyze_with_claude(content: str, api_key: str) -> Optional[str]:
    """
    Use Claude API to analyze findings (preferred if available).

    Args:
        content: Raw findings to analyze
        api_key: Anthropic API key

    Returns:
        Analysis summary or None if failed
    """
    url = "https://api.anthropic.com/v1/messages"

    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
    }

    prompt = f"""Analyze these research findings about Claude AI ecosystem updates.

Extract significant updates and categorize them. For each update, identify:
- What changed (be specific: version numbers, features, prices)
- When (dates if available)
- Impact level (high/medium/low)
- Category (models, claude-code, mcp, pricing, skills, ecosystem)

Research findings:
{content[:12000]}

Respond ONLY with valid JSON in this format:
{{
    "summary": "2-3 sentence summary of most important findings",
    "updates": [
        {{
            "title": "Update title",
            "description": "What changed",
            "date": "YYYY-MM-DD or 'recent'",
            "category": "models|claude-code|mcp|pricing|skills|ecosystem",
            "impact": "high|medium|low",
            "source": "URL if available"
        }}
    ],
    "no_updates": true/false
}}"""

    payload = {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 2000,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        result = response.json()
        return result.get("content", [{}])[0].get("text", "")
    except requests.RequestException as e:
        logger.error(f"Claude analysis failed: {e}")
        return None


def parse_analysis_response(response: str) -> dict:
    """
    Parse the JSON response from analysis.

    Args:
        response: Raw response string

    Returns:
        Parsed dictionary or empty analysis
    """
    try:
        # Try to extract JSON from response
        if "```json" in response:
            response = response.split("```json")[1].split("```")[0]
        elif "```" in response:
            response = response.split("```")[1].split("```")[0]

        return json.loads(response.strip())
    except (json.JSONDecodeError, IndexError) as e:
        logger.warning(f"Failed to parse analysis response: {e}")
        return {
            "summary": "Analysis parsing failed",
            "updates": [],
            "no_updates": True
        }


def categorize_update(update: dict, rules: dict) -> list:
    """
    Determine which files should be updated based on the update content.

    Args:
        update: Single update dictionary
        rules: Topic-to-file mapping rules

    Returns:
        List of target files
    """
    target_files = set()
    content = f"{update.get('title', '')} {update.get('description', '')}".lower()

    for topic, config in rules.get("topics", {}).items():
        keywords = config.get("keywords", [])
        if any(kw.lower() in content for kw in keywords):
            target_files.update(config.get("target_files", []))

    return list(target_files)


def generate_update_recommendations(analysis: dict, rules: dict) -> list:
    """
    Generate specific file update recommendations.

    Args:
        analysis: Parsed analysis results
        rules: Topic-to-file mapping rules

    Returns:
        List of update recommendations
    """
    recommendations = []

    for update in analysis.get("updates", []):
        if update.get("impact") == "low":
            continue  # Skip low-impact updates

        target_files = categorize_update(update, rules)

        if target_files:
            recommendations.append({
                "update": update,
                "target_files": target_files,
                "action": "update" if update.get("impact") == "high" else "consider",
                "priority": 1 if update.get("impact") == "high" else 2
            })

    # Sort by priority
    recommendations.sort(key=lambda x: x["priority"])

    return recommendations


def main():
    """Main entry point."""
    # Load research findings
    findings_path = OUTPUT_DIR / "research_findings.json"
    if not findings_path.exists():
        logger.error("No research findings found. Run auto-research.py first.")
        # Create empty output
        empty_summary = {
            "timestamp": datetime.now().isoformat(),
            "has_updates": False,
            "summary": "No research findings available",
            "topics_found": [],
            "source_count": 0,
            "updates": []
        }
        with open(OUTPUT_DIR / "analysis_summary.json", "w") as f:
            json.dump(empty_summary, f, indent=2)
        return

    with open(findings_path) as f:
        findings = json.load(f)

    # Prepare content for analysis
    content_parts = []

    for result in findings.get("perplexity_results", []):
        content_parts.append(f"Query: {result['query']}\n{result['response']}")

    for repo_data in findings.get("github_releases", []):
        for release in repo_data.get("releases", []):
            content_parts.append(
                f"GitHub Release: {repo_data['repo']} - {release['tag']}\n"
                f"Published: {release['published']}\n"
                f"{release['body']}"
            )

    content = "\n\n---\n\n".join(content_parts)

    if not content.strip():
        logger.info("No content to analyze")
        empty_summary = {
            "timestamp": datetime.now().isoformat(),
            "has_updates": False,
            "summary": "No content found in research",
            "topics_found": [],
            "source_count": 0,
            "updates": []
        }
        with open(OUTPUT_DIR / "analysis_summary.json", "w") as f:
            json.dump(empty_summary, f, indent=2)
        return

    # Try Claude first, fall back to Perplexity
    anthropic_key = os.environ.get("ANTHROPIC_API_KEY")
    perplexity_key = os.environ.get("PERPLEXITY_API_KEY")

    analysis_response = None

    if anthropic_key:
        logger.info("Analyzing with Claude API...")
        analysis_response = analyze_with_claude(content, anthropic_key)

    if not analysis_response and perplexity_key:
        logger.info("Analyzing with Perplexity API...")
        analysis_response = analyze_with_perplexity(content, perplexity_key)

    if not analysis_response:
        logger.error("No API key available for analysis")
        analysis_response = '{"summary": "No API available", "updates": [], "no_updates": true}'

    # Parse the response
    analysis = parse_analysis_response(analysis_response)

    # Load update rules
    rules = load_update_rules()

    # Generate recommendations
    recommendations = generate_update_recommendations(analysis, rules)

    # Determine if we have meaningful updates
    has_updates = (
        not analysis.get("no_updates", True) and
        len([u for u in analysis.get("updates", []) if u.get("impact") != "low"]) > 0
    )

    # Build summary
    summary = {
        "timestamp": datetime.now().isoformat(),
        "has_updates": has_updates,
        "summary": analysis.get("summary", "No summary available"),
        "topics_found": list(set(u.get("category", "general") for u in analysis.get("updates", []))),
        "source_count": len(findings.get("perplexity_results", [])) + len(findings.get("github_releases", [])),
        "updates": analysis.get("updates", []),
        "high_impact_count": len([u for u in analysis.get("updates", []) if u.get("impact") == "high"]),
        "medium_impact_count": len([u for u in analysis.get("updates", []) if u.get("impact") == "medium"])
    }

    # Save outputs
    with open(OUTPUT_DIR / "analysis_summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    with open(OUTPUT_DIR / "update_recommendations.json", "w") as f:
        json.dump(recommendations, f, indent=2)

    # Save raw analysis for debugging
    with open(OUTPUT_DIR / "raw_analysis.txt", "w") as f:
        f.write(analysis_response or "No response")

    logger.info(f"Analysis complete:")
    logger.info(f"  Has updates: {has_updates}")
    logger.info(f"  Topics: {summary['topics_found']}")
    logger.info(f"  High impact: {summary['high_impact_count']}")
    logger.info(f"  Medium impact: {summary['medium_impact_count']}")
    logger.info(f"  Recommendations: {len(recommendations)}")


if __name__ == "__main__":
    main()

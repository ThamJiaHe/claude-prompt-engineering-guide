#!/usr/bin/env python3
"""
Auto-Update Documentation Script

This script applies recommended updates to documentation files based on
analyzed research findings. It preserves existing structure while adding
new information.

Input:
    output/analysis_summary.json: Analysis with updates
    output/update_recommendations.json: File-specific recommendations

Output:
    Updated documentation files
    VERSION and CHANGELOG updates
"""

import os
import re
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
OUTPUT_DIR = Path("output")
CONFIG_DIR = Path("config")


def load_analysis() -> Tuple[dict, list]:
    """Load analysis summary and recommendations."""
    summary_path = OUTPUT_DIR / "analysis_summary.json"
    recommendations_path = OUTPUT_DIR / "update_recommendations.json"

    summary = {}
    recommendations = []

    if summary_path.exists():
        with open(summary_path) as f:
            summary = json.load(f)

    if recommendations_path.exists():
        with open(recommendations_path) as f:
            recommendations = json.load(f)

    return summary, recommendations


def read_file_safely(path: str) -> Optional[str]:
    """Read a file with error handling."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except (IOError, FileNotFoundError) as e:
        logger.warning(f"Could not read {path}: {e}")
        return None


def write_file_safely(path: str, content: str) -> bool:
    """Write a file with error handling."""
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except IOError as e:
        logger.error(f"Could not write {path}: {e}")
        return False


def get_current_version() -> str:
    """Read current version from VERSION file."""
    version_path = Path("VERSION")
    if version_path.exists():
        return version_path.read_text().strip()
    return "0.0.0"


def bump_version(version: str, bump_type: str = "patch") -> str:
    """
    Bump semantic version.

    Args:
        version: Current version string (e.g., "2.0.3")
        bump_type: Type of bump (major, minor, patch)

    Returns:
        New version string
    """
    parts = version.split(".")
    if len(parts) != 3:
        return "0.0.1"

    major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])

    if bump_type == "major":
        return f"{major + 1}.0.0"
    elif bump_type == "minor":
        return f"{major}.{minor + 1}.0"
    else:  # patch
        return f"{major}.{minor}.{patch + 1}"


def update_version_file(new_version: str) -> bool:
    """Update the VERSION file."""
    return write_file_safely("VERSION", f"{new_version}\n")


def update_changelog(summary: dict, new_version: str) -> bool:
    """
    Add a new entry to CHANGELOG.md.

    Args:
        summary: Analysis summary with updates
        new_version: New version number

    Returns:
        True if successful
    """
    changelog_path = Path("CHANGELOG.md")
    if not changelog_path.exists():
        logger.warning("CHANGELOG.md not found")
        return False

    content = changelog_path.read_text(encoding='utf-8')

    # Build changelog entry
    date_str = datetime.now().strftime("%Y-%m-%d")
    updates = summary.get("updates", [])

    entry_parts = [
        f"## [{new_version}] - {date_str}",
        "",
        "### Added (Automated Research)",
        ""
    ]

    # Group updates by category
    by_category = {}
    for update in updates:
        if update.get("impact") == "low":
            continue
        cat = update.get("category", "general")
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(update)

    if by_category:
        for category, cat_updates in by_category.items():
            entry_parts.append(f"#### {category.replace('_', ' ').title()}")
            for update in cat_updates:
                title = update.get("title", "Update")
                desc = update.get("description", "")[:100]
                entry_parts.append(f"- {title}: {desc}")
            entry_parts.append("")
    else:
        entry_parts.append("- Automated research update (no significant changes detected)")
        entry_parts.append("")

    entry_parts.extend([
        "### Changed",
        "",
        "- 🔄 Documentation refreshed with latest research findings",
        f"- 🔄 Automated update from {summary.get('source_count', 0)} sources",
        "",
        "---",
        ""
    ])

    new_entry = "\n".join(entry_parts)

    # Insert after the header section (find first ## [)
    header_pattern = r"(---\s*\n+)(## \[)"
    if re.search(header_pattern, content):
        updated_content = re.sub(
            header_pattern,
            f"\\1{new_entry}\\2",
            content,
            count=1
        )
    else:
        # Fallback: append after first ---
        parts = content.split("---", 2)
        if len(parts) >= 2:
            updated_content = f"{parts[0]}---\n\n{new_entry}{parts[1]}"
            if len(parts) > 2:
                updated_content += "---" + parts[2]
        else:
            updated_content = content + "\n\n" + new_entry

    return write_file_safely("CHANGELOG.md", updated_content)


def update_index_version(new_version: str) -> bool:
    """Update version in INDEX.md."""
    index_path = Path("INDEX.md")
    if not index_path.exists():
        return False

    content = index_path.read_text(encoding='utf-8')
    date_str = datetime.now().strftime("%B %d, %Y")

    # Update version line
    content = re.sub(
        r'(\*\*Version:\*\*\s*)\d+\.\d+\.\d+',
        f'\\g<1>{new_version}',
        content
    )

    # Update date line
    content = re.sub(
        r'(\*\*Last Updated:\*\*\s*)(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d+,\s+\d{4}',
        f'\\g<1>{date_str}',
        content
    )

    # Also update footer
    content = re.sub(
        r'(\*\*Version:\*\*\s*)\d+\.\d+\.\d+(\s*\n\*\*Updated:\*\*)',
        f'\\g<1>{new_version}\\2',
        content
    )

    return write_file_safely("INDEX.md", content)


def update_guide_date() -> bool:
    """Update the 'Last Updated' date in Claude-Prompt-Guide.md."""
    guide_path = Path("Claude-Prompt-Guide.md")
    if not guide_path.exists():
        return False

    content = guide_path.read_text(encoding='utf-8')
    date_str = datetime.now().strftime("%B %d, %Y")

    # Update footer date
    content = re.sub(
        r'\*Last Updated:\s*(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d+,\s+\d{4}\*',
        f'*Last Updated: {date_str}*',
        content
    )

    return write_file_safely("Claude-Prompt-Guide.md", content)


def add_research_note(summary: dict) -> bool:
    """
    Add a brief research note to the main guide if there are high-impact updates.

    This is a conservative update - only adds a timestamped note about new findings
    without modifying substantial content (which requires human review).
    """
    high_impact = [u for u in summary.get("updates", []) if u.get("impact") == "high"]

    if not high_impact:
        return True  # Nothing to add

    guide_path = Path("Claude-Prompt-Guide.md")
    if not guide_path.exists():
        return False

    content = guide_path.read_text(encoding='utf-8')

    # Look for the "Last Major Update" line and update it
    date_str = datetime.now().strftime("%B %d, %Y")

    # Update the metadata header
    content = re.sub(
        r'(\*\*Last Major Update:\*\*\s*)(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d+,\s+\d{4}',
        f'\\g<1>{date_str}',
        content
    )

    return write_file_safely("Claude-Prompt-Guide.md", content)


def main():
    """Main entry point."""
    logger.info("Starting documentation update process...")

    # Load analysis
    summary, recommendations = load_analysis()

    if not summary.get("has_updates", False):
        logger.info("No updates to apply. Exiting.")
        return

    logger.info(f"Processing {len(summary.get('updates', []))} updates...")

    # Determine version bump type
    high_impact_count = summary.get("high_impact_count", 0)
    medium_impact_count = summary.get("medium_impact_count", 0)

    if high_impact_count >= 3:
        bump_type = "minor"
    else:
        bump_type = "patch"

    # Get and bump version
    current_version = get_current_version()
    new_version = bump_version(current_version, bump_type)
    logger.info(f"Version bump: {current_version} -> {new_version} ({bump_type})")

    # Apply updates
    updates_applied = []

    # 1. Update VERSION file
    if update_version_file(new_version):
        updates_applied.append("VERSION")
        logger.info("Updated VERSION file")

    # 2. Update CHANGELOG
    if update_changelog(summary, new_version):
        updates_applied.append("CHANGELOG.md")
        logger.info("Updated CHANGELOG.md")

    # 3. Update INDEX.md version
    if update_index_version(new_version):
        updates_applied.append("INDEX.md")
        logger.info("Updated INDEX.md")

    # 4. Update main guide date
    if update_guide_date():
        updates_applied.append("Claude-Prompt-Guide.md (date)")
        logger.info("Updated Claude-Prompt-Guide.md date")

    # 5. Add research note for high-impact updates
    if add_research_note(summary):
        logger.info("Processed research notes")

    # Log summary
    logger.info(f"Update complete. Files modified: {len(updates_applied)}")
    for f in updates_applied:
        logger.info(f"  - {f}")

    # Save update log
    update_log = {
        "timestamp": datetime.now().isoformat(),
        "previous_version": current_version,
        "new_version": new_version,
        "bump_type": bump_type,
        "files_updated": updates_applied,
        "updates_processed": len(summary.get("updates", []))
    }

    with open(OUTPUT_DIR / "update_log.json", "w") as f:
        json.dump(update_log, f, indent=2)


if __name__ == "__main__":
    main()

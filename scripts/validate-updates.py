#!/usr/bin/env python3
"""
Validate Documentation Updates Script

This script validates that automated updates don't introduce errors:
- Markdown syntax validation
- Link checking (internal links)
- Version consistency
- CHANGELOG format
- No sensitive data

Exit codes:
    0: All validations passed
    1: Validation errors found
"""

import os
import re
import sys
import json
import logging
from pathlib import Path
from typing import List, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Files to validate
CORE_FILES = [
    "Claude-Prompt-Guide.md",
    "INDEX.md",
    "CHANGELOG.md",
    "README.md"
]


class ValidationError:
    """Represents a validation error."""

    def __init__(self, file: str, line: int, message: str, severity: str = "error"):
        self.file = file
        self.line = line
        self.message = message
        self.severity = severity  # error, warning

    def __str__(self):
        return f"{self.severity.upper()}: {self.file}:{self.line} - {self.message}"


def validate_markdown_syntax(filepath: str) -> List[ValidationError]:
    """
    Basic Markdown syntax validation.

    Checks:
    - Unclosed code blocks
    - Malformed headers
    - Unclosed brackets/parentheses in links
    """
    errors = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
    except (IOError, FileNotFoundError):
        return [ValidationError(filepath, 0, "File not found or unreadable")]

    # Check for unclosed code blocks
    code_block_count = content.count('```')
    if code_block_count % 2 != 0:
        errors.append(ValidationError(
            filepath, 0,
            f"Unclosed code block (found {code_block_count} ``` markers)"
        ))

    # Check for malformed headers
    for i, line in enumerate(lines, 1):
        # Headers should have space after #
        if re.match(r'^#{1,6}[^#\s]', line):
            errors.append(ValidationError(
                filepath, i,
                f"Header missing space after #: '{line[:50]}...'",
                "warning"
            ))

        # Check for broken links (unclosed brackets)
        open_brackets = line.count('[') - line.count('](')
        close_brackets = line.count('](') + line.count(')')
        if '[' in line and '(' in line:
            # Simple check for malformed links
            link_pattern = r'\[([^\]]*)\]\(([^\)]*)\)'
            partial_link = r'\[([^\]]*)\]\([^\)]*$'
            if re.search(partial_link, line) and not re.search(link_pattern, line):
                errors.append(ValidationError(
                    filepath, i,
                    f"Possible unclosed link: '{line[:50]}...'"
                ))

    return errors


def validate_internal_links(filepath: str) -> List[ValidationError]:
    """
    Validate internal links point to existing files.
    """
    errors = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except (IOError, FileNotFoundError):
        return []

    # Find all internal links
    link_pattern = r'\[([^\]]+)\]\(\.?/?([^\)#]+)(#[^\)]*)?\)'

    for match in re.finditer(link_pattern, content):
        link_text = match.group(1)
        link_path = match.group(2)

        # Skip external links
        if link_path.startswith(('http://', 'https://', 'mailto:')):
            continue

        # Skip anchor-only links
        if not link_path:
            continue

        # Resolve relative path
        base_dir = Path(filepath).parent
        target_path = base_dir / link_path

        if not target_path.exists():
            # Try from repo root
            target_path = Path(link_path)
            if not target_path.exists():
                line_num = content[:match.start()].count('\n') + 1
                errors.append(ValidationError(
                    filepath, line_num,
                    f"Broken link to '{link_path}' (text: '{link_text}')",
                    "warning"
                ))

    return errors


def validate_version_consistency() -> List[ValidationError]:
    """
    Ensure version numbers are consistent across files.
    """
    errors = []

    # Read VERSION file
    version_path = Path("VERSION")
    if not version_path.exists():
        errors.append(ValidationError("VERSION", 0, "VERSION file not found"))
        return errors

    expected_version = version_path.read_text().strip()

    # Check INDEX.md
    index_path = Path("INDEX.md")
    if index_path.exists():
        content = index_path.read_text(encoding='utf-8')
        version_match = re.search(r'\*\*Version:\*\*\s*(\d+\.\d+\.\d+)', content)
        if version_match:
            found_version = version_match.group(1)
            if found_version != expected_version:
                errors.append(ValidationError(
                    "INDEX.md", 0,
                    f"Version mismatch: found {found_version}, expected {expected_version}"
                ))

    # Check CHANGELOG.md has entry for current version
    changelog_path = Path("CHANGELOG.md")
    if changelog_path.exists():
        content = changelog_path.read_text(encoding='utf-8')
        if f"## [{expected_version}]" not in content:
            errors.append(ValidationError(
                "CHANGELOG.md", 0,
                f"No changelog entry for version {expected_version}",
                "warning"
            ))

    return errors


def validate_changelog_format() -> List[ValidationError]:
    """
    Validate CHANGELOG.md format.
    """
    errors = []

    changelog_path = Path("CHANGELOG.md")
    if not changelog_path.exists():
        return []

    content = changelog_path.read_text(encoding='utf-8')
    lines = content.split('\n')

    # Check for valid date format in version headers
    version_pattern = r'## \[(\d+\.\d+\.\d+)\] - (\d{4}-\d{2}-\d{2})'
    found_versions = []

    for i, line in enumerate(lines, 1):
        if line.startswith('## ['):
            match = re.match(version_pattern, line)
            if not match:
                # Check if it's a version line but malformed
                if re.match(r'## \[\d', line):
                    errors.append(ValidationError(
                        "CHANGELOG.md", i,
                        f"Malformed version header: '{line}'"
                    ))
            else:
                found_versions.append(match.group(1))

    # Check versions are in descending order
    for i in range(len(found_versions) - 1):
        current = [int(x) for x in found_versions[i].split('.')]
        next_ver = [int(x) for x in found_versions[i + 1].split('.')]
        if current < next_ver:
            errors.append(ValidationError(
                "CHANGELOG.md", 0,
                f"Versions out of order: {found_versions[i]} appears before {found_versions[i+1]}",
                "warning"
            ))

    return errors


def validate_no_sensitive_data(filepath: str) -> List[ValidationError]:
    """
    Check for accidentally committed sensitive data.
    """
    errors = []

    sensitive_patterns = [
        (r'sk-[a-zA-Z0-9]{20,}', "Possible API key"),
        (r'ghp_[a-zA-Z0-9]{36}', "GitHub personal access token"),
        (r'AKIA[0-9A-Z]{16}', "AWS access key"),
        (r'password\s*=\s*["\'][^"\']+["\']', "Hardcoded password"),
        (r'secret\s*=\s*["\'][^"\']+["\']', "Hardcoded secret"),
    ]

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except (IOError, FileNotFoundError):
        return []

    for pattern, description in sensitive_patterns:
        matches = list(re.finditer(pattern, content, re.IGNORECASE))
        for match in matches:
            line_num = content[:match.start()].count('\n') + 1
            errors.append(ValidationError(
                filepath, line_num,
                f"{description} detected"
            ))

    return errors


def validate_json_files() -> List[ValidationError]:
    """
    Validate JSON files in output and config directories.
    """
    errors = []

    json_dirs = [Path("output"), Path("config")]

    for json_dir in json_dirs:
        if not json_dir.exists():
            continue

        for json_file in json_dir.glob("*.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    json.load(f)
            except json.JSONDecodeError as e:
                errors.append(ValidationError(
                    str(json_file), e.lineno or 0,
                    f"Invalid JSON: {e.msg}"
                ))

    return errors


def main():
    """Main entry point."""
    logger.info("Starting validation...")

    all_errors: List[ValidationError] = []
    all_warnings: List[ValidationError] = []

    # Validate core markdown files
    for filepath in CORE_FILES:
        if not Path(filepath).exists():
            logger.warning(f"Skipping {filepath} (not found)")
            continue

        logger.info(f"Validating {filepath}...")

        # Markdown syntax
        errors = validate_markdown_syntax(filepath)
        for e in errors:
            if e.severity == "error":
                all_errors.append(e)
            else:
                all_warnings.append(e)

        # Internal links
        errors = validate_internal_links(filepath)
        for e in errors:
            if e.severity == "error":
                all_errors.append(e)
            else:
                all_warnings.append(e)

        # Sensitive data
        errors = validate_no_sensitive_data(filepath)
        all_errors.extend(errors)

    # Validate docs directory
    docs_dir = Path("docs")
    if docs_dir.exists():
        for md_file in docs_dir.glob("*.md"):
            logger.info(f"Validating {md_file}...")
            errors = validate_markdown_syntax(str(md_file))
            for e in errors:
                if e.severity == "error":
                    all_errors.append(e)
                else:
                    all_warnings.append(e)

    # Version consistency
    logger.info("Validating version consistency...")
    errors = validate_version_consistency()
    for e in errors:
        if e.severity == "error":
            all_errors.append(e)
        else:
            all_warnings.append(e)

    # Changelog format
    logger.info("Validating changelog format...")
    errors = validate_changelog_format()
    for e in errors:
        if e.severity == "error":
            all_errors.append(e)
        else:
            all_warnings.append(e)

    # JSON files
    logger.info("Validating JSON files...")
    all_errors.extend(validate_json_files())

    # Report results
    print("\n" + "=" * 60)
    print("VALIDATION RESULTS")
    print("=" * 60)

    if all_warnings:
        print(f"\nWarnings ({len(all_warnings)}):")
        for w in all_warnings:
            print(f"  {w}")

    if all_errors:
        print(f"\nErrors ({len(all_errors)}):")
        for e in all_errors:
            print(f"  {e}")
        print("\n" + "=" * 60)
        print("VALIDATION FAILED")
        print("=" * 60)
        sys.exit(1)
    else:
        print("\n" + "=" * 60)
        print("VALIDATION PASSED")
        print("=" * 60)
        sys.exit(0)


if __name__ == "__main__":
    main()

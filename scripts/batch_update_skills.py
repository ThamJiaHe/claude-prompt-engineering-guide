#!/usr/bin/env python3
"""
Batch update skill example files for January 2026 compatibility.
Adds compatibility metadata and January 2026 note to all skill files.
"""

import os
import re
from pathlib import Path

# Files to skip (already updated)
SKIP_FILES = {
    'example-feedback-analyzer.md',
    'aws-cloud-infrastructure-skill.md'
}

# Directory containing skill examples
SKILLS_DIR = Path(__file__).parent.parent / 'skills' / 'examples'

# The January 2026 compatibility note to add
JAN_2026_NOTE = """
---

**Last Updated:** January 24, 2026
**Compatibility:** Claude Opus 4.5, Claude Code v2.x
**Status:** Production Ready

> **January 2026 Update:** This skill is compatible with Claude Opus 4.5 and Claude Code v2.x. For complex tasks, use the `effort: high` parameter for thorough analysis.
"""

def update_frontmatter(content: str) -> str:
    """Update YAML frontmatter with compatibility and version bump."""
    # Match YAML frontmatter
    frontmatter_pattern = r'^---\n(.*?)\n---'
    match = re.match(frontmatter_pattern, content, re.DOTALL)

    if not match:
        return content

    frontmatter = match.group(1)

    # Add compatibility field if not present
    if 'compatibility:' not in frontmatter:
        frontmatter += '\ncompatibility: Claude Opus 4.5, Claude Code v2.x'

    # Add updated field if not present
    if 'updated:' not in frontmatter:
        frontmatter += '\nupdated: 2026-01-24'
    else:
        # Update existing date
        frontmatter = re.sub(r'updated:\s*[\d-]+', 'updated: 2026-01-24', frontmatter)

    # Update version - bump to 1.1.0 if it's 1.0.0, or increment patch
    def bump_version(m):
        version = m.group(1)
        parts = version.split('.')
        if len(parts) == 3:
            major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
            if major == 1 and minor == 0:
                return 'version: 1.1.0'
            elif major == 2 and minor == 0:
                return 'version: 2.1.0'
            else:
                return f'version: {major}.{minor}.{patch + 1}'
        return m.group(0)

    frontmatter = re.sub(r'version:\s*([\d.]+)', bump_version, frontmatter)

    # Rebuild content
    rest_of_content = content[match.end():]
    return f'---\n{frontmatter}\n---{rest_of_content}'

def add_jan_2026_note(content: str) -> str:
    """Add January 2026 compatibility note at the end if not present."""
    if 'January 2026' in content:
        return content

    # Remove trailing whitespace and add the note
    content = content.rstrip()
    content += JAN_2026_NOTE
    return content

def process_file(filepath: Path) -> bool:
    """Process a single skill file. Returns True if modified."""
    print(f"Processing: {filepath.name}")

    with open(filepath, 'r', encoding='utf-8') as f:
        original_content = f.read()

    # Apply updates
    content = update_frontmatter(original_content)
    content = add_jan_2026_note(content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Main function to batch update all skill files."""
    print(f"Scanning directory: {SKILLS_DIR}")
    print(f"Skipping files: {SKIP_FILES}")
    print("-" * 50)

    modified_files = []
    skipped_files = []

    for filepath in sorted(SKILLS_DIR.glob('*.md')):
        if filepath.name in SKIP_FILES:
            skipped_files.append(filepath.name)
            print(f"Skipped (already updated): {filepath.name}")
            continue

        if process_file(filepath):
            modified_files.append(filepath.name)
            print(f"  [OK] Modified: {filepath.name}")
        else:
            print(f"  - No changes needed: {filepath.name}")

    print("-" * 50)
    print(f"\nSummary:")
    print(f"  Modified: {len(modified_files)} files")
    print(f"  Skipped: {len(skipped_files)} files")

    if modified_files:
        print(f"\nModified files:")
        for f in modified_files:
            print(f"  - {f}")

    return modified_files

if __name__ == '__main__':
    modified = main()
    print(f"\nBatch update complete. {len(modified)} files updated.")

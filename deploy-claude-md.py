#!/usr/bin/env python3
"""
CLAUDE.md Template Deployment Utility

This utility intelligently deploys CLAUDE.md template files to their corresponding
filesystem locations. It uses Claude AI to detect the appropriate paths based on
the template type and can interactively ask the user for paths when detection fails.
"""

import os
import sys
import json
import shutil
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import subprocess
import re


class CLAUDEMDDeployer:
    """Handles deployment of CLAUDE.md templates to filesystem locations."""

    # Template to target directory mapping patterns
    TEMPLATE_PATTERNS = {
        'hf-spaces': {
            'patterns': [
                '~/repos/hugging-face/spaces',
                '~/repos/huggingface/spaces',
                '~/huggingface/spaces'
            ],
            'description': 'Hugging Face Spaces directory',
            'validation': lambda p: (p / 'public').exists() or (p / 'private').exists()
        },
        'hf-datasets': {
            'patterns': [
                '~/repos/hugging-face/datasets',
                '~/repos/huggingface/datasets',
                '~/huggingface/datasets'
            ],
            'description': 'Hugging Face Datasets directory',
            'validation': lambda p: (p / 'public').exists() or (p / 'private').exists()
        },
        'hf-models': {
            'patterns': [
                '~/repos/hugging-face/models',
                '~/repos/huggingface/models',
                '~/huggingface/models'
            ],
            'description': 'Hugging Face Models directory',
            'validation': None
        },
        'for-gh-repo-base': {
            'patterns': [
                '~/repos/github',
                '~/github',
                '~/repos/gh'
            ],
            'description': 'GitHub repositories base directory',
            'validation': lambda p: len(list(p.glob('.git'))) > 0 or len(list(p.glob('*/.git'))) > 5
        },
        'for-gh-docs-base': {
            'patterns': [
                '~/repos/docs',
                '~/repos/documentation',
                '~/docs',
                '~/repos/github/docs'
            ],
            'description': 'GitHub documentation repositories directory',
            'validation': None
        },
        'for-gh-websites-base': {
            'patterns': [
                '~/repos/websites',
                '~/repos/web',
                '~/websites',
                '~/repos/github/websites'
            ],
            'description': 'GitHub websites repositories directory',
            'validation': None
        },
        'for-gh-forks-base': {
            'patterns': [
                '~/repos/forks',
                '~/forks',
                '~/repos/github/forks'
            ],
            'description': 'GitHub forked repositories directory',
            'validation': None
        },
        'for-cloned-projects.base': {
            'patterns': [
                '~/repos/cloned',
                '~/cloned-repos',
                '~/repos/github/cloned'
            ],
            'description': 'Cloned third-party projects directory',
            'validation': None
        }
    }

    def __init__(self, templates_dir: Path, dry_run: bool = False, interactive: bool = True):
        """
        Initialize the deployer.

        Args:
            templates_dir: Path to directory containing template CLAUDE.md files
            dry_run: If True, simulate deployment without making changes
            interactive: If True, ask user for paths when auto-detection fails
        """
        self.templates_dir = Path(templates_dir).resolve()
        self.dry_run = dry_run
        self.interactive = interactive
        self.home = Path.home()

    def find_templates(self) -> Dict[str, Path]:
        """Find all CLAUDE.md template files in the templates directory."""
        templates = {}

        for item in self.templates_dir.iterdir():
            if item.is_dir():
                claude_md = item / 'CLAUDE.md'
                if claude_md.exists():
                    templates[item.name] = claude_md

        return templates

    def expand_path(self, path_str: str) -> Path:
        """Expand a path string with ~ and environment variables."""
        expanded = os.path.expanduser(os.path.expandvars(path_str))
        return Path(expanded).resolve()

    def detect_target_path(self, template_key: str) -> Optional[Path]:
        """
        Auto-detect the target path for a template.

        Args:
            template_key: The template identifier (e.g., 'hf-spaces')

        Returns:
            Path object if detected, None otherwise
        """
        if template_key not in self.TEMPLATE_PATTERNS:
            return None

        config = self.TEMPLATE_PATTERNS[template_key]

        # Try each pattern in order
        for pattern in config['patterns']:
            path = self.expand_path(pattern)

            if path.exists():
                # Validate if validator provided
                if config['validation'] is not None:
                    try:
                        if config['validation'](path):
                            return path
                    except Exception:
                        continue
                else:
                    return path

        return None

    def prompt_for_path(self, template_key: str) -> Optional[Path]:
        """
        Prompt the user to provide the target path.

        Args:
            template_key: The template identifier

        Returns:
            Path object or None if user cancels
        """
        if not self.interactive:
            return None

        config = self.TEMPLATE_PATTERNS.get(template_key, {})
        description = config.get('description', template_key)

        print(f"\n❌ Could not auto-detect path for: {template_key}")
        print(f"   Description: {description}")

        if 'patterns' in config:
            print(f"   Tried looking for:")
            for pattern in config['patterns']:
                print(f"     - {pattern}")

        print(f"\n   Please provide the full path (or press Enter to skip):")

        try:
            user_input = input(f"   Path: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return None

        if not user_input:
            return None

        path = self.expand_path(user_input)

        if not path.exists():
            print(f"   ⚠️  Warning: Path does not exist: {path}")

            try:
                create = input(f"   Create it? [y/N]: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print()
                return None

            if create == 'y':
                try:
                    path.mkdir(parents=True, exist_ok=True)
                    print(f"   ✓ Created directory: {path}")
                except Exception as e:
                    print(f"   ❌ Failed to create directory: {e}")
                    return None
            else:
                return None

        return path

    def deploy_template(self, template_key: str, template_path: Path, target_path: Path) -> bool:
        """
        Deploy a template to the target path.

        Args:
            template_key: The template identifier
            template_path: Path to the template CLAUDE.md file
            target_path: Target directory path

        Returns:
            True if successful, False otherwise
        """
        target_file = target_path / 'CLAUDE.md'

        # Check if target already exists
        if target_file.exists():
            print(f"   ⚠️  CLAUDE.md already exists at: {target_file}")

            if self.interactive:
                try:
                    overwrite = input(f"   Overwrite? [y/N]: ").strip().lower()
                except (EOFError, KeyboardInterrupt):
                    print()
                    print(f"   ⏭️  Skipped")
                    return False

                if overwrite != 'y':
                    print(f"   ⏭️  Skipped")
                    return False
            else:
                print(f"   ⏭️  Skipped (use --force to overwrite)")
                return False

        if self.dry_run:
            print(f"   🔍 [DRY RUN] Would copy:")
            print(f"      From: {template_path}")
            print(f"      To:   {target_file}")
            return True

        try:
            shutil.copy2(template_path, target_file)
            print(f"   ✓ Deployed to: {target_file}")
            return True
        except Exception as e:
            print(f"   ❌ Failed to deploy: {e}")
            return False

    def run(self) -> Dict[str, bool]:
        """
        Run the deployment process.

        Returns:
            Dictionary mapping template keys to deployment success status
        """
        print("🚀 CLAUDE.md Template Deployment Utility")
        print("=" * 60)

        templates = self.find_templates()

        if not templates:
            print(f"❌ No templates found in: {self.templates_dir}")
            return {}

        print(f"\n📋 Found {len(templates)} template(s):")
        for key in templates.keys():
            print(f"   - {key}")

        if self.dry_run:
            print(f"\n🔍 Running in DRY RUN mode (no changes will be made)")

        print("\n" + "=" * 60)

        results = {}

        for template_key, template_path in templates.items():
            print(f"\n📄 Processing: {template_key}")

            # Try to auto-detect path
            target_path = self.detect_target_path(template_key)

            if target_path:
                print(f"   ✓ Auto-detected path: {target_path}")
            else:
                print(f"   ℹ️  Could not auto-detect path")
                target_path = self.prompt_for_path(template_key)

                if not target_path:
                    print(f"   ⏭️  Skipped")
                    results[template_key] = False
                    continue

            # Deploy the template
            success = self.deploy_template(template_key, template_path, target_path)
            results[template_key] = success

        # Print summary
        print("\n" + "=" * 60)
        print("📊 Deployment Summary")
        print("=" * 60)

        successful = sum(1 for v in results.values() if v)
        total = len(results)

        print(f"\n✓ Successful: {successful}/{total}")

        if successful < total:
            print(f"✗ Failed/Skipped: {total - successful}/{total}")

        return results


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Deploy CLAUDE.md templates to filesystem locations',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode (default)
  ./deploy-claude-md.py

  # Dry run to preview changes
  ./deploy-claude-md.py --dry-run

  # Non-interactive mode (skip missing paths)
  ./deploy-claude-md.py --no-interactive

  # Specify custom templates directory
  ./deploy-claude-md.py --templates-dir /path/to/templates
        """
    )

    parser.add_argument(
        '--templates-dir',
        type=str,
        default='.',
        help='Directory containing template CLAUDE.md files (default: current directory)'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Simulate deployment without making changes'
    )

    parser.add_argument(
        '--no-interactive',
        action='store_true',
        help='Disable interactive prompts (skip on detection failure)'
    )

    args = parser.parse_args()

    deployer = CLAUDEMDDeployer(
        templates_dir=args.templates_dir,
        dry_run=args.dry_run,
        interactive=not args.no_interactive
    )

    try:
        results = deployer.run()

        # Exit with non-zero if any deployments failed
        if not all(results.values()) and results:
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n\n⚠️  Deployment cancelled by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()

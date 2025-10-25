#!/bin/bash
#
# Quick installation script for CLAUDE.md Deployment Utility
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🚀 CLAUDE.md Template Deployment - Installation"
echo "================================================"
echo

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is required but not found"
    echo "   Please install Python 3.6 or later"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✓ Found Python $PYTHON_VERSION"

# Make script executable
chmod +x "$SCRIPT_DIR/deploy-claude-md.py"
echo "✓ Made deploy-claude-md.py executable"

# Optional: Create symlink in ~/.local/bin
if [ -d "$HOME/.local/bin" ]; then
    read -p "Create symlink in ~/.local/bin for easy access? [Y/n]: " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Nn]$ ]]; then
        ln -sf "$SCRIPT_DIR/deploy-claude-md.py" "$HOME/.local/bin/deploy-claude-md"
        echo "✓ Created symlink: ~/.local/bin/deploy-claude-md"
        echo "  You can now run: deploy-claude-md"
    fi
fi

echo
echo "✅ Installation complete!"
echo
echo "Quick Start:"
echo "  Preview:  ./deploy-claude-md.py --dry-run"
echo "  Deploy:   ./deploy-claude-md.py"
echo "  Help:     ./deploy-claude-md.py --help"
echo
echo "Documentation:"
echo "  README:   cat README.md"
echo "  Usage:    cat USAGE.md"

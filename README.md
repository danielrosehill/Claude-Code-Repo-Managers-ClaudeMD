 ![alt text](banner.png)

[![Claude Code](https://img.shields.io/badge/Made%20with-Claude%20Code-6366f1?style=for-the-badge&logo=anthropic&logoColor=white)](https://docs.claude.com/claude-code)
[![Claude Code Projects Index](https://img.shields.io/badge/Claude%20Code-Projects%20Index-4f46e5?style=for-the-badge&logo=github)](https://github.com/danielrosehill/Claude-Code-Repos-Index)
[![Master Index](https://img.shields.io/badge/GitHub-Master%20Index-181717?style=for-the-badge&logo=github)](https://github.com/danielrosehill/Github-Master-Index)

A collection of CLAUDE.md templates for repository management, designed to work seamlessly with Claude Code CLI.

## Overview

This repository provides pre-configured CLAUDE.md templates that give Claude Code context-aware instructions when working in different types of repository directories. Instead of a one-size-fits-all deployment script, this approach lets you selectively deploy templates using Claude Code's slash commands.

## What are CLAUDE.md Files?

CLAUDE.md files are contextual documentation files that Claude Code reads when working in a directory. They provide:

- Purpose and description of the directory
- Common tasks and operations expected in that location
- Best practices and guidelines
- Typical directory structure
- Development workflows and patterns

When Claude Code starts in a directory with a CLAUDE.md file, it automatically reads and follows the instructions, making it context-aware for that specific workspace.

## Available Templates

All templates are located in the `template-claude-md/` directory.

### Hugging Face Templates

- **hf-spaces/**: For Hugging Face Spaces directories (Gradio, Streamlit, Docker apps)
- **hf-datasets/**: For Hugging Face Datasets directories
- **hf-models/**: For Hugging Face Models directories

### GitHub Repository Templates

- **for-gh-repo-base/**: For the base GitHub repositories directory
- **for-gh-docs-base/**: For documentation repositories
- **for-gh-websites-base/**: For website/web project repositories
- **for-gh-forks-base/**: For forked repositories
- **for-gh-collaborative-base/**: For collaborative GitHub projects

### Work & Collaboration Templates

- **for-work-repos-base/**: For work-related repositories
- **for-datasets-collaborative-base/**: For collaborative dataset projects
- **for-docs-collaborative-base/**: For collaborative documentation projects

### Project Templates

- **for-cloned-projects.base/**: For cloned third-party projects

### Complete Template List

1. `template-claude-md/for-cloned-projects.base/CLAUDE.md` - Cloned third-party projects
2. `template-claude-md/for-datasets-collaborative-base/CLAUDE.md` - Collaborative datasets
3. `template-claude-md/for-docs-collaborative-base/CLAUDE.md` - Collaborative documentation
4. `template-claude-md/for-gh-collaborative-base/CLAUDE.md` - Collaborative GitHub repos
5. `template-claude-md/for-gh-docs-base/CLAUDE.md` - GitHub documentation repos
6. `template-claude-md/for-gh-forks-base/CLAUDE.md` - GitHub forks
7. `template-claude-md/for-gh-repo-base/CLAUDE.md` - GitHub repositories base
8. `template-claude-md/for-gh-websites-base/CLAUDE.md` - GitHub website projects
9. `template-claude-md/for-work-repos-base/CLAUDE.md` - Work repositories
10. `template-claude-md/hf-datasets/CLAUDE.md` - Hugging Face datasets
11. `template-claude-md/hf-models/CLAUDE.md` - Hugging Face models
12. `template-claude-md/hf-spaces/CLAUDE.md` - Hugging Face Spaces

## Quick Start

### Installation

1. Clone this repository:
```bash
cd ~/repos/github
git clone https://github.com/danielrosehill/Claude-Code-Repo-Managers-ClaudeMD.git
```

2. Set up slash commands (optional):
```bash
cd Claude-Code-Repo-Managers-ClaudeMD
./grab-slash-commands.sh
```

This syncs the slash commands from `.claude/commands/` to `slash-commands/` directory.

### Usage with Claude Code

The recommended workflow is to use Claude Code interactively to deploy templates:

1. **Start Claude Code in this repository:**
   ```bash
   cd ~/repos/github/Claude-Code-Repo-Managers-ClaudeMD
   claude-code
   ```

2. **Ask Claude to help you deploy templates:**
   - "Please show me the available templates"
   - "I'd like to deploy the GitHub repos template to ~/repos/github"
   - "Help me set up CLAUDE.md files for my Hugging Face workspace"

3. **Claude Code will:**
   - Show you the available templates
   - Ask you which ones you want to deploy
   - Confirm the target directory paths
   - Copy the templates to the appropriate locations
   - Customize them if needed based on your setup

### Available Slash Commands

- **/set-stuff-up**: Interactive setup wizard that guides you through deploying templates
- **/depersonalise**: Remove personal information from CLAUDE.md files before sharing

## How It Works

### Template Structure

Each template directory contains a `CLAUDE.md` file with:

- **Purpose**: What the directory is used for
- **Directory Structure**: Expected subdirectories and organization
- **Common Tasks**: Typical operations Claude might be asked to perform
- **Best Practices**: Guidelines for working in this context
- **Workflows**: Development patterns and procedures
- **Examples**: Code snippets and usage patterns

### Syncing Slash Commands

The repository includes a pre-commit hook that automatically syncs slash commands:

```bash
./grab-slash-commands.sh
```

This ensures the `slash-commands/` directory stays in sync with `.claude/commands/`.

## Use Cases

### For Hugging Face Developers

Deploy context-aware documentation to your Hugging Face workspace. When Claude Code works in `~/repos/hugging-face/spaces/`, it will know:
- How to create Gradio/Streamlit apps
- Proper Space configuration patterns
- Hardware tier recommendations
- Best practices for Space development

### For GitHub Repository Management

Provide Claude Code with context when managing large collections of repositories. When working in `~/repos/github/`, Claude will understand:
- Batch operations across multiple repos
- Repository analysis and auditing patterns
- Maintenance workflows
- Best practices for organization

### For Forked Repository Management

Give Claude Code guidance on working with forks. In `~/repos/forks/`, Claude knows:
- How to handle upstream syncing
- Pull request workflows
- Contribution guidelines
- Fork maintenance practices

## Customizing Templates

Since everyone organizes their repositories differently, you can:

1. **Browse the templates** in `template-claude-md/`
2. **Copy templates manually** to your preferred locations
3. **Customize them** to match your workflow
4. **Ask Claude Code to help** - it can read the templates and adapt them to your needs

## Contributing

### Adding New Templates

1. Create a new directory in `template-claude-md/` with a descriptive name
2. Add a comprehensive `CLAUDE.md` file
3. Test the template in your own workflow
4. Submit a pull request

### Template Guidelines

Good CLAUDE.md files should:

- **Be comprehensive**: Cover all common operations
- **Include examples**: Provide code snippets and patterns
- **Stay focused**: Be specific to the directory's purpose
- **Be actionable**: Give Claude clear guidance on what to do
- **Include context**: Explain why things are done a certain way

### Adding Slash Commands

1. Create a new `.md` file in `.claude/commands/`
2. Write the command prompt/instructions
3. Run `./grab-slash-commands.sh` to sync
4. Test with Claude Code
5. Submit a pull request

## License

MIT License - See LICENSE file for details

## Support

For issues, questions, or contributions:

- **Issues**: Open an issue on GitHub
- **Pull Requests**: Contributions welcome
- **Discussions**: Use GitHub Discussions for questions

## Related Projects

- [Claude Code](https://docs.claude.com/claude-code): The official CLI for Claude AI
- [Hugging Face](https://huggingface.co): Platform for ML models, datasets, and spaces
- [GitHub CLI](https://cli.github.com/): Command-line tool for GitHub

## Changelog

### v2.0.0 (Current)

- Migrated from Python deployment script to Claude Code-based approach
- Added slash commands for interactive deployment
- Added pre-commit hook for slash command syncing
- Reorganized templates into `template-claude-md/` directory
- Added new collaborative templates
- Simplified workflow using Claude Code's interactive capabilities

### v1.0.0 (Initial Release - Deprecated)

- Python-based deployment utility (deprecated)
- 8 template types for HF and GitHub repositories
- Auto-detection with pattern matching (no longer maintained)

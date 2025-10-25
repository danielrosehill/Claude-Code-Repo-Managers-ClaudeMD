# Claude-Code-Repo-Managers-ClaudeMD

A collection of CLAUDE.md templates for repository management and an intelligent deployment utility to distribute them across your filesystem.

## Overview

This repository contains:

1. **CLAUDE.md Templates**: Pre-configured documentation files that provide context-aware instructions for Claude AI when working in different types of repository directories
2. **Deployment Utility**: An intelligent Python script that automatically detects the correct filesystem locations and deploys the templates

## What are CLAUDE.md Files?

CLAUDE.md files are contextual documentation files that Claude AI reads when working in a directory. They provide:

- Purpose and description of the directory
- Common tasks and operations expected in that location
- Best practices and guidelines
- Typical directory structure
- Development workflows and patterns

## Available Templates

### Hugging Face Templates

- **hf-spaces/**: For Hugging Face Spaces directories (Gradio, Streamlit, Docker apps)
- **hf-datasets/**: For Hugging Face Datasets directories
- **hf-models/**: For Hugging Face Models directories

### GitHub Repository Templates

- **for-gh-repo-base/**: For the base GitHub repositories directory
- **for-gh-docs-base/**: For documentation repositories
- **for-gh-websites-base/**: For website/web project repositories
- **for-gh-forks-base/**: For forked repositories
- **for-cloned-projects.base/**: For cloned third-party projects

## Quick Start

### Installation

1. Clone this repository:
```bash
cd ~/repos/github
git clone https://github.com/yourusername/Claude-Code-Repo-Managers-ClaudeMD.git
cd Claude-Code-Repo-Managers-ClaudeMD
```

2. The deployment script is standalone and requires only Python 3.6+:
```bash
./deploy-claude-md.py
```

### Basic Usage

**Interactive deployment (recommended for first-time use):**
```bash
./deploy-claude-md.py
```

The script will:
1. Scan for all CLAUDE.md templates
2. Attempt to auto-detect the corresponding filesystem locations
3. Ask you for the path if auto-detection fails
4. Deploy each template to the detected/provided location
5. Prompt before overwriting existing files

**Dry run to preview changes:**
```bash
./deploy-claude-md.py --dry-run
```

**Non-interactive mode (skip on detection failure):**
```bash
./deploy-claude-md.py --no-interactive
```

**Custom templates directory:**
```bash
./deploy-claude-md.py --templates-dir /path/to/templates
```

## How It Works

### Auto-Detection

The deployment utility uses intelligent pattern matching to find the correct filesystem locations:

1. **Pattern Matching**: Tries common path patterns for each template type
   - Example: For `hf-spaces`, it looks for `~/repos/hugging-face/spaces`, `~/repos/huggingface/spaces`, etc.

2. **Validation**: Applies validation rules to confirm the detected path is correct
   - Example: Hugging Face directories should have `public/` and `private/` subdirectories
   - GitHub repo bases should contain multiple `.git` directories

3. **Interactive Fallback**: If auto-detection fails, prompts you to provide the path manually

### Template Structure

Each template directory contains a `CLAUDE.md` file with:

- **Purpose**: What the directory is used for
- **Directory Structure**: Expected subdirectories and organization
- **Common Tasks**: Typical operations Claude might be asked to perform
- **Best Practices**: Guidelines for working in this context
- **Workflows**: Development patterns and procedures
- **Examples**: Code snippets and usage patterns

## Configuration

The deployment behavior can be customized via [config.json](config.json):

```json
{
  "templates": {
    "template-key": {
      "name": "Human-readable name",
      "description": "What this template is for",
      "search_patterns": [
        "~/path/pattern/1",
        "~/path/pattern/2"
      ],
      "validation_rules": {
        "has_subdirs": ["subdir1", "subdir2"],
        "min_git_repos": 5
      }
    }
  },
  "deployment_options": {
    "backup_existing": true,
    "skip_if_exists": false,
    "create_missing_dirs": true
  }
}
```

## Use Cases

### For Hugging Face Developers

Deploy context-aware documentation to your Hugging Face workspace:

```bash
cd ~/repos/github/Claude-Code-Repo-Managers-ClaudeMD
./deploy-claude-md.py
```

Now when Claude works in `~/repos/hugging-face/spaces/`, it will know:
- How to create Gradio/Streamlit apps
- Proper Space configuration patterns
- Hardware tier recommendations
- Best practices for Space development

### For GitHub Repository Management

Provide Claude with context when managing large collections of repositories:

```bash
./deploy-claude-md.py
```

When working in `~/repos/github/`, Claude will understand:
- Batch operations across multiple repos
- Repository analysis and auditing patterns
- Maintenance workflows
- Best practices for organization

### For Forked Repository Management

Give Claude guidance on working with forks:

```bash
./deploy-claude-md.py
```

In `~/repos/forks/`, Claude knows:
- How to handle upstream syncing
- Pull request workflows
- Contribution guidelines
- Fork maintenance practices

## Advanced Usage

### Selective Deployment

Deploy only specific templates by running in the template's directory:

```bash
cd hf-spaces
../deploy-claude-md.py --templates-dir .
```

### Custom Path Mapping

Edit the `TEMPLATE_PATTERNS` dictionary in [deploy-claude-md.py](deploy-claude-md.py) to add your own path patterns:

```python
TEMPLATE_PATTERNS = {
    'my-custom-template': {
        'patterns': [
            '~/my/custom/path',
            '~/alternative/path'
        ],
        'description': 'My custom directory type',
        'validation': lambda p: p.exists() and (p / 'marker.txt').exists()
    }
}
```

### Backup Before Deployment

The script will prompt before overwriting existing CLAUDE.md files. To automatically backup:

```python
# In config.json
{
  "deployment_options": {
    "backup_existing": true,
    "backup_suffix": ".backup"
  }
}
```

## Troubleshooting

### Auto-detection Fails

If the script can't find your directories:

1. **Check your directory structure**: Ensure you're using the standard paths described in the patterns
2. **Use interactive mode**: Let the script ask you for the correct paths
3. **Update config.json**: Add your custom paths to the search patterns
4. **Use absolute paths**: When prompted, provide the full absolute path

### Permission Errors

If you encounter permission errors:

```bash
# Check directory permissions
ls -la /path/to/target

# Make writable if needed
chmod u+w /path/to/target
```

### Validation Failures

If a path is detected but validation fails:

1. Check that subdirectories exist (e.g., `public/` and `private/` for HF directories)
2. Ensure the directory contains the expected content
3. You can disable validation by modifying the template pattern in the script

## Contributing

### Adding New Templates

1. Create a new directory with a descriptive name
2. Add a comprehensive `CLAUDE.md` file
3. Update `TEMPLATE_PATTERNS` in [deploy-claude-md.py](deploy-claude-md.py)
4. Update [config.json](config.json) with the new template configuration
5. Test the deployment
6. Submit a pull request

### Template Guidelines

Good CLAUDE.md files should:

- **Be comprehensive**: Cover all common operations
- **Include examples**: Provide code snippets and patterns
- **Stay focused**: Be specific to the directory's purpose
- **Be actionable**: Give Claude clear guidance on what to do
- **Include context**: Explain why things are done a certain way

## License

MIT License - See LICENSE file for details

## Support

For issues, questions, or contributions:

- **Issues**: Open an issue on GitHub
- **Pull Requests**: Contributions welcome
- **Discussions**: Use GitHub Discussions for questions

## Related Projects

- [Claude AI](https://claude.ai): The AI assistant these templates are designed for
- [Hugging Face](https://huggingface.co): Platform for ML models, datasets, and spaces
- [GitHub CLI](https://cli.github.com/): Command-line tool for GitHub

## Changelog

### v1.0.0 (Initial Release)

- Core deployment utility
- 8 template types for HF and GitHub repositories
- Auto-detection with pattern matching
- Interactive and non-interactive modes
- Dry-run capability
- Validation rules
- Configuration file support

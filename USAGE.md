# CLAUDE.md Deployment Utility - Usage Guide

## Quick Reference

```bash
# Interactive deployment (default)
./deploy-claude-md.py

# Preview changes without deploying
./deploy-claude-md.py --dry-run

# Non-interactive mode (skip missing paths)
./deploy-claude-md.py --no-interactive

# Custom templates directory
./deploy-claude-md.py --templates-dir /path/to/templates

# Combine options
./deploy-claude-md.py --dry-run --no-interactive
```

## Command-Line Options

### `--templates-dir PATH`

Specify the directory containing CLAUDE.md templates.

**Default:** Current directory (`.`)

**Example:**
```bash
./deploy-claude-md.py --templates-dir ~/my-templates
```

### `--dry-run`

Preview what would be deployed without making any changes to the filesystem.

**Example:**
```bash
./deploy-claude-md.py --dry-run
```

**Output:**
```
🔍 [DRY RUN] Would copy:
   From: /path/to/template/CLAUDE.md
   To:   /target/path/CLAUDE.md
```

### `--no-interactive`

Disable interactive prompts. The utility will:
- Only deploy to auto-detected paths
- Skip templates where auto-detection fails
- Never prompt for overwrite confirmation
- Never prompt for path input

**Use when:** Running in CI/CD, scripts, or automated workflows

**Example:**
```bash
./deploy-claude-md.py --no-interactive
```

### `-h, --help`

Display help message with all options.

```bash
./deploy-claude-md.py --help
```

## Usage Patterns

### First-Time Deployment

Run interactively to set up all templates:

```bash
cd ~/repos/github/Claude-Code-Repo-Managers-ClaudeMD
./deploy-claude-md.py
```

The script will:
1. Find all templates in the current directory
2. Auto-detect target paths where possible
3. Ask you for paths it couldn't detect
4. Confirm before overwriting existing files

### Preview Before Deploying

Always safe to run first:

```bash
./deploy-claude-md.py --dry-run
```

Review the output, then run without `--dry-run` when ready.

### Update Existing Templates

When you've updated templates and want to redeploy:

```bash
./deploy-claude-md.py
```

You'll be prompted to overwrite existing CLAUDE.md files:
```
⚠️  CLAUDE.md already exists at: /target/path/CLAUDE.md
Overwrite? [y/N]: y
```

### Automated/Scripted Deployment

For scripts and automation:

```bash
# Non-interactive: only deploy to auto-detected paths
./deploy-claude-md.py --no-interactive

# Preview in CI/CD
./deploy-claude-md.py --dry-run --no-interactive
```

### Deploy Single Template

From within a template directory:

```bash
cd hf-spaces
../deploy-claude-md.py --templates-dir .
```

Or specify the template:

```bash
./deploy-claude-md.py --templates-dir hf-spaces
```

## Understanding Auto-Detection

### How It Works

The utility searches for target directories using predefined patterns:

**Example: Hugging Face Spaces**
```python
patterns = [
    '~/repos/hugging-face/spaces',
    '~/repos/huggingface/spaces',
    '~/huggingface/spaces'
]
```

For each pattern:
1. Expand `~` and environment variables
2. Check if path exists
3. Apply validation rules (if any)
4. Return first match

### Validation Rules

Some templates have validation to ensure the detected path is correct:

**Hugging Face directories:**
- Must contain `public/` or `private/` subdirectories

**GitHub repo base:**
- Must contain multiple `.git` directories (indicating repos)

### When Auto-Detection Fails

If a path can't be auto-detected:

**Interactive mode:**
```
❌ Could not auto-detect path for: for-gh-websites-base
   Description: GitHub websites repositories directory
   Tried looking for:
     - ~/repos/websites
     - ~/repos/web
     - ~/websites
     - ~/repos/github/websites

   Please provide the full path (or press Enter to skip):
   Path: /home/user/my-websites
```

**Non-interactive mode:**
```
ℹ️  Could not auto-detect path
⏭️  Skipped
```

## Interactive Prompts

### Path Input

When auto-detection fails, you'll be asked for the path:

```
Please provide the full path (or press Enter to skip):
Path: ~/custom/path
```

**Tips:**
- Use `~/` for home directory
- Environment variables are expanded
- Press Enter to skip this template

### Directory Creation

If you provide a path that doesn't exist:

```
⚠️  Warning: Path does not exist: /home/user/new-dir
Create it? [y/N]: y
✓ Created directory: /home/user/new-dir
```

### Overwrite Confirmation

If CLAUDE.md already exists at the target:

```
⚠️  CLAUDE.md already exists at: /target/path/CLAUDE.md
Overwrite? [y/N]: y
✓ Deployed to: /target/path/CLAUDE.md
```

## Exit Codes

The utility uses standard exit codes:

- `0`: Success (all templates deployed)
- `1`: Partial failure (some templates skipped/failed)
- `130`: Cancelled by user (Ctrl+C)

**Example in scripts:**
```bash
if ./deploy-claude-md.py --no-interactive; then
    echo "All templates deployed"
else
    echo "Some templates failed"
fi
```

## Common Workflows

### Initial Setup

```bash
# 1. Clone the repository
cd ~/repos/github
git clone <repo-url> Claude-Code-Repo-Managers-ClaudeMD
cd Claude-Code-Repo-Managers-ClaudeMD

# 2. Preview what will be deployed
./deploy-claude-md.py --dry-run

# 3. Deploy templates
./deploy-claude-md.py
```

### Update Templates

```bash
# 1. Pull latest changes
git pull

# 2. Redeploy (will prompt for overwrites)
./deploy-claude-md.py
```

### Custom Directory Structure

If your directories don't match the default patterns:

```bash
# Option 1: Provide paths interactively
./deploy-claude-md.py
# Enter custom paths when prompted

# Option 2: Edit config.json to add your patterns
nano config.json
# Add your paths to search_patterns

# Option 3: Edit the script
nano deploy-claude-md.py
# Add patterns to TEMPLATE_PATTERNS
```

### Selective Deployment

Deploy only specific templates:

```bash
# Deploy only Hugging Face templates
for dir in hf-*; do
    ./deploy-claude-md.py --templates-dir "$dir"
done

# Deploy only GitHub templates
for dir in for-gh-*; do
    ./deploy-claude-md.py --templates-dir "$dir"
done
```

## Troubleshooting

### "No templates found"

**Problem:** Script reports no templates found

**Solutions:**
1. Check you're in the right directory:
   ```bash
   pwd  # Should show Claude-Code-Repo-Managers-ClaudeMD
   ```
2. Verify templates exist:
   ```bash
   ls -d */CLAUDE.md
   ```
3. Use `--templates-dir`:
   ```bash
   ./deploy-claude-md.py --templates-dir /path/to/templates
   ```

### "Could not auto-detect path"

**Problem:** Script can't find target directory

**Solutions:**
1. Create the directory:
   ```bash
   mkdir -p ~/repos/hugging-face/spaces
   ```
2. Provide path interactively when prompted
3. Add your custom path to [config.json](config.json)
4. Use non-interactive mode to skip

### "Permission denied"

**Problem:** Can't write to target directory

**Solutions:**
1. Check permissions:
   ```bash
   ls -la /target/directory
   ```
2. Change permissions:
   ```bash
   chmod u+w /target/directory
   ```
3. Check ownership:
   ```bash
   sudo chown $USER /target/directory
   ```

### "Validation failed"

**Problem:** Directory exists but doesn't pass validation

**Solutions:**
1. Check subdirectories exist:
   ```bash
   ls /target/directory
   # Should have public/ and private/ for HF dirs
   ```
2. Create missing subdirectories:
   ```bash
   mkdir -p /target/directory/{public,private}
   ```
3. Disable validation by editing the script

## Advanced Usage

### Custom Validation Rules

Edit the `TEMPLATE_PATTERNS` in [deploy-claude-md.py](deploy-claude-md.py):

```python
'my-template': {
    'patterns': ['~/my/path'],
    'description': 'My custom directory',
    'validation': lambda p: (p / 'marker.txt').exists()
}
```

### Environment-Specific Paths

Use environment variables in paths:

```python
'patterns': [
    '$REPOS_DIR/my-category',
    '${WORKSPACE}/repos',
    '~/repos'
]
```

Set in your shell:
```bash
export REPOS_DIR=/mnt/data/repositories
./deploy-claude-md.py
```

### Integration with Other Tools

**Make/Justfile:**
```makefile
deploy-claude-md:
    cd ~/repos/github/Claude-Code-Repo-Managers-ClaudeMD && \
    ./deploy-claude-md.py --no-interactive

update-docs: deploy-claude-md
    @echo "Documentation updated"
```

**Shell alias:**
```bash
# Add to ~/.bashrc or ~/.zshrc
alias deploy-claude='~/repos/github/Claude-Code-Repo-Managers-ClaudeMD/deploy-claude-md.py'

# Usage
deploy-claude --dry-run
```

## Best Practices

1. **Preview first:** Always run with `--dry-run` before actual deployment
2. **Version control:** Keep your templates in git
3. **Document custom paths:** Update config.json with your paths
4. **Test interactively:** Use interactive mode for first-time setup
5. **Automate updates:** Use non-interactive mode in scripts
6. **Review changes:** Check git diff after deployment if targets are versioned
7. **Backup important files:** The script prompts before overwriting

## Getting Help

- **In-repo docs:** See [README.md](README.md)
- **Command help:** `./deploy-claude-md.py --help`
- **Configuration:** Review [config.json](config.json)
- **Issues:** Report on GitHub

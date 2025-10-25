# Examples - CLAUDE.md Deployment Utility

This guide shows real-world examples of using the deployment utility.

## Example 1: First-Time Interactive Deployment

**Scenario:** You've just cloned the repository and want to deploy all templates.

```bash
$ cd ~/repos/github/Claude-Code-Repo-Managers-ClaudeMD
$ ./deploy-claude-md.py
```

**Output:**
```
🚀 CLAUDE.md Template Deployment Utility
============================================================

📋 Found 8 template(s):
   - hf-datasets
   - hf-spaces
   - hf-models
   - for-gh-repo-base
   - for-gh-docs-base
   - for-gh-websites-base
   - for-gh-forks-base
   - for-cloned-projects.base

============================================================

📄 Processing: hf-datasets
   ✓ Auto-detected path: /home/user/repos/hugging-face/datasets
   ✓ Deployed to: /home/user/repos/hugging-face/datasets/CLAUDE.md

📄 Processing: hf-spaces
   ✓ Auto-detected path: /home/user/repos/hugging-face/spaces
   ✓ Deployed to: /home/user/repos/hugging-face/spaces/CLAUDE.md

📄 Processing: hf-models
   ✓ Auto-detected path: /home/user/repos/hugging-face/models
   ✓ Deployed to: /home/user/repos/hugging-face/models/CLAUDE.md

📄 Processing: for-gh-repo-base
   ✓ Auto-detected path: /home/user/repos/github
   ✓ Deployed to: /home/user/repos/github/CLAUDE.md

📄 Processing: for-gh-docs-base
   ℹ️  Could not auto-detect path

❌ Could not auto-detect path for: for-gh-docs-base
   Description: GitHub documentation repositories directory
   Tried looking for:
     - ~/repos/docs
     - ~/repos/documentation
     - ~/docs
     - ~/repos/github/docs

   Please provide the full path (or press Enter to skip):
   Path: ~/repos/github/documentation

   ⚠️  Warning: Path does not exist: /home/user/repos/github/documentation
   Create it? [y/N]: y
   ✓ Created directory: /home/user/repos/github/documentation
   ✓ Deployed to: /home/user/repos/github/documentation/CLAUDE.md

📄 Processing: for-gh-websites-base
   ℹ️  Could not auto-detect path

❌ Could not auto-detect path for: for-gh-websites-base
   Description: GitHub websites repositories directory
   Tried looking for:
     - ~/repos/websites
     - ~/repos/web
     - ~/websites
     - ~/repos/github/websites

   Please provide the full path (or press Enter to skip):
   Path:
   ⏭️  Skipped

📄 Processing: for-gh-forks-base
   ✓ Auto-detected path: /home/user/repos/forks
   ✓ Deployed to: /home/user/repos/forks/CLAUDE.md

📄 Processing: for-cloned-projects.base
   ✓ Auto-detected path: /home/user/repos/cloned
   ✓ Deployed to: /home/user/repos/cloned/CLAUDE.md

============================================================
📊 Deployment Summary
============================================================

✓ Successful: 7/8
✗ Failed/Skipped: 1/8
```

## Example 2: Dry Run Before Deployment

**Scenario:** You want to see what will happen without making changes.

```bash
$ ./deploy-claude-md.py --dry-run
```

**Output:**
```
🚀 CLAUDE.md Template Deployment Utility
============================================================

📋 Found 8 template(s):
   - hf-datasets
   - hf-spaces
   - hf-models
   - for-gh-repo-base
   - for-gh-docs-base
   - for-gh-websites-base
   - for-gh-forks-base
   - for-cloned-projects.base

🔍 Running in DRY RUN mode (no changes will be made)

============================================================

📄 Processing: hf-datasets
   ✓ Auto-detected path: /home/user/repos/hugging-face/datasets
   🔍 [DRY RUN] Would copy:
      From: /home/user/repos/github/Claude-Code-Repo-Managers-ClaudeMD/hf-datasets/CLAUDE.md
      To:   /home/user/repos/hugging-face/datasets/CLAUDE.md

[... similar output for other templates ...]

============================================================
📊 Deployment Summary
============================================================

✓ Successful: 8/8
```

## Example 3: Non-Interactive Deployment (CI/CD)

**Scenario:** Running in a CI/CD pipeline or automated script.

```bash
$ ./deploy-claude-md.py --no-interactive
```

**Output:**
```
🚀 CLAUDE.md Template Deployment Utility
============================================================

📋 Found 8 template(s):
   - hf-datasets
   - hf-spaces
   - hf-models
   - for-gh-repo-base
   - for-gh-docs-base
   - for-gh-websites-base
   - for-gh-forks-base
   - for-cloned-projects.base

============================================================

📄 Processing: hf-datasets
   ✓ Auto-detected path: /home/user/repos/hugging-face/datasets
   ✓ Deployed to: /home/user/repos/hugging-face/datasets/CLAUDE.md

[... auto-detected templates deployed ...]

📄 Processing: for-gh-websites-base
   ℹ️  Could not auto-detect path
   ⏭️  Skipped

============================================================
📊 Deployment Summary
============================================================

✓ Successful: 7/8
✗ Failed/Skipped: 1/8
```

## Example 4: Updating Existing Templates

**Scenario:** You've updated templates and want to redeploy them.

```bash
$ ./deploy-claude-md.py
```

**Output (with overwrite prompts):**
```
📄 Processing: hf-spaces
   ✓ Auto-detected path: /home/user/repos/hugging-face/spaces
   ⚠️  CLAUDE.md already exists at: /home/user/repos/hugging-face/spaces/CLAUDE.md
   Overwrite? [y/N]: y
   ✓ Deployed to: /home/user/repos/hugging-face/spaces/CLAUDE.md
```

## Example 5: Deploy Single Template

**Scenario:** You only want to deploy the Hugging Face Spaces template.

```bash
$ ./deploy-claude-md.py --templates-dir hf-spaces
```

**Output:**
```
🚀 CLAUDE.md Template Deployment Utility
============================================================

📋 Found 1 template(s):
   - hf-spaces

============================================================

📄 Processing: hf-spaces
   ✓ Auto-detected path: /home/user/repos/hugging-face/spaces
   ✓ Deployed to: /home/user/repos/hugging-face/spaces/CLAUDE.md

============================================================
📊 Deployment Summary
============================================================

✓ Successful: 1/1
```

## Example 6: Custom Directory Structure

**Scenario:** Your directories don't match the default patterns.

```bash
$ ./deploy-claude-md.py
```

**Interactive session:**
```
📄 Processing: hf-spaces
   ℹ️  Could not auto-detect path

❌ Could not auto-detect path for: hf-spaces
   Description: Hugging Face Spaces directory
   Tried looking for:
     - ~/repos/hugging-face/spaces
     - ~/repos/huggingface/spaces
     - ~/huggingface/spaces

   Please provide the full path (or press Enter to skip):
   Path: /mnt/data/ml/huggingface/my-spaces
   ✓ Deployed to: /mnt/data/ml/huggingface/my-spaces/CLAUDE.md
```

## Example 7: Batch Deploy Multiple Directories

**Scenario:** You want to deploy only GitHub-related templates.

```bash
$ for dir in for-gh-*; do
    echo "Deploying $dir..."
    ./deploy-claude-md.py --templates-dir "$dir" --no-interactive
  done
```

**Output:**
```
Deploying for-gh-repo-base...
✓ Successful: 1/1

Deploying for-gh-docs-base...
✗ Failed/Skipped: 1/1

Deploying for-gh-websites-base...
✗ Failed/Skipped: 1/1

Deploying for-gh-forks-base...
✓ Successful: 1/1
```

## Example 8: Using in a Makefile

**Scenario:** Integrate deployment into your build system.

**Makefile:**
```makefile
.PHONY: deploy-docs preview-deploy help

DEPLOY_SCRIPT := ~/repos/github/Claude-Code-Repo-Managers-ClaudeMD/deploy-claude-md.py

preview-deploy:
	@echo "Preview CLAUDE.md deployment..."
	@$(DEPLOY_SCRIPT) --dry-run --no-interactive

deploy-docs:
	@echo "Deploying CLAUDE.md templates..."
	@$(DEPLOY_SCRIPT) --no-interactive
	@echo "Deployment complete!"

help:
	@echo "Available targets:"
	@echo "  preview-deploy  - Preview deployment without changes"
	@echo "  deploy-docs     - Deploy all CLAUDE.md templates"
```

**Usage:**
```bash
$ make preview-deploy
Preview CLAUDE.md deployment...
[... dry run output ...]

$ make deploy-docs
Deploying CLAUDE.md templates...
[... deployment output ...]
Deployment complete!
```

## Example 9: Shell Alias for Quick Access

**Scenario:** You use the deployment script frequently and want quick access.

**Add to ~/.bashrc or ~/.zshrc:**
```bash
# CLAUDE.md deployment utility
alias deploy-claude='~/repos/github/Claude-Code-Repo-Managers-ClaudeMD/deploy-claude-md.py'
alias deploy-claude-preview='deploy-claude --dry-run'
```

**Usage:**
```bash
$ deploy-claude-preview
[... dry run output ...]

$ deploy-claude
[... deployment output ...]
```

## Example 10: Installation Script

**Scenario:** First-time setup with the install script.

```bash
$ cd ~/repos/github/Claude-Code-Repo-Managers-ClaudeMD
$ ./install.sh
```

**Output:**
```
🚀 CLAUDE.md Template Deployment - Installation
================================================

✓ Found Python 3.11.5
✓ Made deploy-claude-md.py executable
Create symlink in ~/.local/bin for easy access? [Y/n]: y
✓ Created symlink: ~/.local/bin/deploy-claude-md
  You can now run: deploy-claude-md

✅ Installation complete!

Quick Start:
  Preview:  ./deploy-claude-md.py --dry-run
  Deploy:   ./deploy-claude-md.py
  Help:     ./deploy-claude-md.py --help

Documentation:
  README:   cat README.md
  Usage:    cat USAGE.md
```

**After installation:**
```bash
$ deploy-claude-md --dry-run
[... works from anywhere ...]
```

## Example 11: Handling Missing Directories

**Scenario:** Target directory doesn't exist, and you want to create it.

```bash
$ ./deploy-claude-md.py
```

**Interactive creation:**
```
📄 Processing: for-gh-docs-base
   ℹ️  Could not auto-detect path

❌ Could not auto-detect path for: for-gh-docs-base
   Description: GitHub documentation repositories directory
   Tried looking for:
     - ~/repos/docs
     - ~/repos/documentation
     - ~/docs
     - ~/repos/github/docs

   Please provide the full path (or press Enter to skip):
   Path: ~/repos/docs

   ⚠️  Warning: Path does not exist: /home/user/repos/docs
   Create it? [y/N]: y
   ✓ Created directory: /home/user/repos/docs
   ✓ Deployed to: /home/user/repos/docs/CLAUDE.md
```

## Example 12: Verify Deployment

**Scenario:** Check that templates were deployed correctly.

```bash
$ # Deploy templates
$ ./deploy-claude-md.py --no-interactive

$ # Verify deployment
$ find ~/repos -name "CLAUDE.md" -type f
```

**Output:**
```
/home/user/repos/hugging-face/datasets/CLAUDE.md
/home/user/repos/hugging-face/spaces/CLAUDE.md
/home/user/repos/hugging-face/models/CLAUDE.md
/home/user/repos/github/CLAUDE.md
/home/user/repos/docs/CLAUDE.md
/home/user/repos/forks/CLAUDE.md
/home/user/repos/cloned/CLAUDE.md
```

## Example 13: Integration with Git Workflow

**Scenario:** Deploy templates and commit changes to tracked directories.

```bash
#!/bin/bash
# update-claude-docs.sh

# Deploy templates
echo "Deploying CLAUDE.md templates..."
~/repos/github/Claude-Code-Repo-Managers-ClaudeMD/deploy-claude-md.py --no-interactive

# Check for changes in tracked repos
echo "Checking for changes..."
cd ~/repos/github
git diff --name-only | grep "CLAUDE.md"

if [ $? -eq 0 ]; then
    echo "CLAUDE.md updated in tracked repositories"
    echo "Review changes and commit if needed"
fi
```

## Example 14: Environment-Specific Deployment

**Scenario:** Different paths on different machines.

**Set environment variable:**
```bash
export REPOS_BASE="/mnt/data/repositories"
```

**Edit deploy-claude-md.py patterns to use it:**
```python
'patterns': [
    '$REPOS_BASE/github',
    '~/repos/github',
    '~/github'
]
```

**Deploy:**
```bash
$ ./deploy-claude-md.py
📄 Processing: for-gh-repo-base
   ✓ Auto-detected path: /mnt/data/repositories/github
   ✓ Deployed to: /mnt/data/repositories/github/CLAUDE.md
```

## Example 15: Error Handling

**Scenario:** Permission denied error.

```bash
$ ./deploy-claude-md.py
```

**Output with error:**
```
📄 Processing: hf-spaces
   ✓ Auto-detected path: /home/user/repos/hugging-face/spaces
   ❌ Failed to deploy: [Errno 13] Permission denied: '/home/user/repos/hugging-face/spaces/CLAUDE.md'
```

**Fix and retry:**
```bash
$ chmod u+w ~/repos/hugging-face/spaces
$ ./deploy-claude-md.py --templates-dir hf-spaces
```

**Success:**
```
📄 Processing: hf-spaces
   ✓ Auto-detected path: /home/user/repos/hugging-face/spaces
   ⚠️  CLAUDE.md already exists at: /home/user/repos/hugging-face/spaces/CLAUDE.md
   Overwrite? [y/N]: y
   ✓ Deployed to: /home/user/repos/hugging-face/spaces/CLAUDE.md
```

## Tips for Success

1. **Always preview first:**
   ```bash
   ./deploy-claude-md.py --dry-run
   ```

2. **Start with interactive mode:**
   - Lets you confirm paths
   - Helps identify missing directories
   - Gives you control over overwrites

3. **Use non-interactive for automation:**
   - Scripts and CI/CD pipelines
   - When you trust the auto-detection
   - For scheduled updates

4. **Check exit codes in scripts:**
   ```bash
   if ./deploy-claude-md.py --no-interactive; then
       echo "Success"
   else
       echo "Some templates failed"
       exit 1
   fi
   ```

5. **Verify deployment:**
   ```bash
   find ~/repos -name "CLAUDE.md" -type f -mtime -1
   ```

6. **Update regularly:**
   - Pull latest templates
   - Redeploy to get new content
   - Review changes before overwriting

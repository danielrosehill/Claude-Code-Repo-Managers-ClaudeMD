# Quick Start Guide

Get started with the CLAUDE.md deployment utility in 5 minutes.

## 1. Installation (30 seconds)

```bash
cd ~/repos/github
git clone <your-repo-url> Claude-Code-Repo-Managers-ClaudeMD
cd Claude-Code-Repo-Managers-ClaudeMD
./install.sh
```

Or manual setup:

```bash
chmod +x deploy-claude-md.py
```

## 2. Preview Deployment (30 seconds)

See what will happen without making changes:

```bash
./deploy-claude-md.py --dry-run
```

**Expected output:**
- List of found templates
- Auto-detected paths
- Where each template would be deployed

## 3. Deploy Templates (2-4 minutes)

Run the deployment interactively:

```bash
./deploy-claude-md.py
```

**What happens:**
- Auto-detects most paths
- Asks for paths it can't find
- Prompts before overwriting
- Creates directories if needed

## 4. Verify Deployment (10 seconds)

Check that files were deployed:

```bash
find ~/repos -name "CLAUDE.md" -type f | head -10
```

## 5. Test with Claude (2 minutes)

Open Claude Code in a deployed directory:

```bash
cd ~/repos/hugging-face/spaces
claude-code
```

Ask Claude: "What should I know about working in this directory?"

Claude will read the CLAUDE.md file and provide context-aware information.

## Common Commands

```bash
# Preview changes
./deploy-claude-md.py --dry-run

# Interactive deployment (recommended)
./deploy-claude-md.py

# Non-interactive (for scripts)
./deploy-claude-md.py --no-interactive

# Deploy specific template
./deploy-claude-md.py --templates-dir hf-spaces

# Show help
./deploy-claude-md.py --help
```

## What You Get

After deployment, you'll have CLAUDE.md files in:

- `~/repos/hugging-face/spaces/` - HF Spaces guidance
- `~/repos/hugging-face/datasets/` - HF Datasets guidance
- `~/repos/hugging-face/models/` - HF Models guidance
- `~/repos/github/` - GitHub repo management
- `~/repos/docs/` - Documentation repos
- `~/repos/forks/` - Forked repos management
- `~/repos/cloned/` - Third-party projects

Each file provides:
- **Purpose** of the directory
- **Common tasks** Claude might be asked to do
- **Best practices** for that context
- **Workflows** and patterns
- **Examples** and code snippets

## Next Steps

- **Read templates:** Check out the CLAUDE.md files
- **Customize:** Edit templates for your needs
- **Update paths:** Modify config.json for custom locations
- **Automate:** Add to your shell aliases or scripts

## Troubleshooting

**"No templates found"**
```bash
ls -d */CLAUDE.md  # Should show 8 templates
```

**"Could not auto-detect path"**
- Provide the path when prompted, OR
- Press Enter to skip, OR
- Edit config.json to add your path

**"Permission denied"**
```bash
chmod u+w /target/directory
```

## Documentation

- **[README.md](README.md)** - Full project overview
- **[USAGE.md](USAGE.md)** - Detailed usage guide
- **[EXAMPLES.md](EXAMPLES.md)** - Real-world examples
- **[config.json](config.json)** - Configuration reference

## Support

- Report issues on GitHub
- Check existing templates for guidance
- Read the comprehensive documentation

---

**Time to deploy:** ~5 minutes
**Result:** Context-aware documentation throughout your repos

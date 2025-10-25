# CLAUDE.md For Claude-Code-Repo-Managers-ClaudeMD Repository

## Purpose

This repository contains a collection of CLAUDE.md templates designed to provide context-aware instructions when Claude Code works in different types of repository directories. It's a meta-repository that helps manage and deploy context files throughout your development environment.

## What This Repository Does

This repository provides pre-configured CLAUDE.md templates that can be deployed to various repository base directories:

- **Hugging Face workspaces**: Spaces, datasets, and models
- **GitHub repositories**: Documentation, websites, forks, collaborative projects
- **Work repositories**: Professional and work-related projects
- **Cloned projects**: Third-party repositories and collaborative work

When deployed, these templates give Claude Code automatic context awareness about:
- The purpose of each directory
- Common tasks and operations expected in that location
- Best practices and guidelines
- Directory structure conventions
- Development workflows and patterns

## Repository Structure

```
Claude-Code-Repo-Managers-ClaudeMD/
├── template-claude-md/          # All CLAUDE.md templates
│   ├── hf-spaces/              # Hugging Face Spaces template
│   ├── hf-datasets/            # Hugging Face Datasets template
│   ├── hf-models/              # Hugging Face Models template
│   ├── for-gh-repo-base/       # GitHub repositories base template
│   ├── for-gh-docs-base/       # GitHub docs repositories template
│   ├── for-gh-websites-base/   # GitHub websites template
│   ├── for-gh-forks-base/      # GitHub forks template
│   ├── for-gh-collaborative-base/  # Collaborative GitHub template
│   ├── for-work-repos-base/    # Work repositories template
│   ├── for-datasets-collaborative-base/  # Collaborative datasets template
│   ├── for-docs-collaborative-base/      # Collaborative docs template
│   └── for-cloned-projects.base/         # Cloned projects template
├── .claude/commands/           # Slash commands for Claude Code
│   ├── set-stuff-up.md        # Interactive deployment wizard
│   └── depersonalise.md       # Remove personal info from templates
├── slash-commands/            # Synced copy of slash commands (for reference)
├── grab-slash-commands.sh     # Script to sync slash commands
├── install-slash-commands.sh  # Script to install slash commands
├── config.json                # Configuration file for template deployment
├── README.md                  # User-facing documentation
├── USAGE.md                   # Detailed usage instructions
└── LICENSE                    # MIT License
```

## Common Tasks in This Repository

When working in this repository, typical tasks include:

### 1. Template Management
- **Viewing templates**: Reading and reviewing existing CLAUDE.md templates
- **Editing templates**: Updating templates to improve context or add new guidance
- **Creating templates**: Adding new template types for different repository contexts
- **Testing templates**: Deploying templates to test directories to validate functionality

### 2. Deployment Operations
- **Interactive deployment**: Using `/set-stuff-up` slash command to deploy templates
- **Manual deployment**: Copying specific templates to target directories
- **Bulk deployment**: Deploying multiple templates across different repository bases
- **Custom deployment**: Adapting templates for specific user requirements

### 3. Slash Command Development
- **Creating commands**: Adding new slash commands in `.claude/commands/`
- **Syncing commands**: Running `./grab-slash-commands.sh` to sync to `slash-commands/`
- **Testing commands**: Validating slash commands work correctly
- **Documenting commands**: Updating README with new command descriptions

### 4. Personalization & Privacy
- **Depersonalization**: Using `/depersonalise` to remove personal information
- **Customization**: Adapting templates for different users or organizations
- **Configuration**: Modifying `config.json` for custom deployment patterns

### 5. Maintenance & Updates
- **Version control**: Committing template changes to Git
- **Documentation updates**: Keeping README and USAGE.md current
- **Template synchronization**: Ensuring deployed templates match repository versions
- **Issue resolution**: Fixing bugs or addressing user feedback

## Working in This Repository

### Initial Setup

When first working with this repository, you should:

1. **Review available templates** in `template-claude-md/` to understand what's available
2. **Check slash commands** in `.claude/commands/` to see available automation
3. **Read configuration** in `config.json` to understand deployment mappings
4. **Review documentation** in README.md and USAGE.md

### Typical Workflows

#### Adding a New Template

1. Create a new directory in `template-claude-md/` with descriptive name
2. Write a comprehensive `CLAUDE.md` file with:
   - Purpose section
   - Directory structure
   - Common tasks
   - Best practices
   - Examples
3. Test the template by deploying to a test directory
4. Update README.md with the new template listing
5. Commit and push changes

#### Deploying Templates

**Interactive Method (Recommended):**
```bash
claude-code
# Then use slash command:
/set-stuff-up
```

**Direct Deployment Method:**
Ask Claude Code to help you deploy templates:
- "Deploy the GitHub repos template to ~/repos/github"
- "Set up Hugging Face templates in my HF workspace"
- "Show me available templates and help me choose which to deploy"

**Manual Method:**
```bash
cp template-claude-md/for-gh-repo-base/CLAUDE.md ~/repos/github/CLAUDE.md
```

#### Updating Existing Templates

1. Edit the template in `template-claude-md/`
2. Test changes in a deployed location
3. Optionally re-deploy to update existing installations
4. Commit changes with descriptive message
5. Consider whether users with deployed versions need notification

### Best Practices for This Repository

1. **Template Quality**: Ensure all templates are comprehensive, accurate, and actionable
2. **Documentation**: Keep README and USAGE.md synchronized with template changes
3. **Testing**: Always test templates before committing significant changes
4. **Version Control**: Use clear commit messages that describe template changes
5. **User Focus**: Design templates to help Claude Code provide better assistance

## Development Guidelines

### Template Writing Standards

When creating or editing CLAUDE.md templates:

- **Be specific**: Tailor guidance to the directory's specific purpose
- **Be comprehensive**: Cover all common operations users might need
- **Be actionable**: Provide clear instructions Claude Code can follow
- **Include examples**: Show code snippets and usage patterns
- **Explain rationale**: Help Claude understand why things are done certain ways
- **Stay focused**: Don't include general guidance that belongs in user's home CLAUDE.md

### Slash Command Guidelines

When creating slash commands:

- **Clear purpose**: Each command should have one well-defined function
- **User-friendly**: Design for interactive use with clear prompts
- **Error handling**: Gracefully handle edge cases and user errors
- **Documentation**: Describe the command's purpose and usage
- **Testing**: Validate commands work across different scenarios

### Configuration Management

The `config.json` file maps template types to target directories. When modifying:

- Maintain consistent structure
- Use clear, descriptive keys
- Document any non-obvious mappings
- Test deployment logic after changes

## Integration with User Environment

This repository is designed to work within Daniel's development environment:

- **Repository location**: `~/repos/github/Claude-Code-Repo-Managers-ClaudeMD`
- **Deployment targets**: Various repository bases throughout `~/repos/`
- **Integration**: Works alongside existing CLAUDE.md files in `~` and `~/repos/`
- **Slash commands**: Available when working in this directory with Claude Code

## Contributing to This Repository

When contributing improvements:

1. **Template additions**: Follow existing template structure and style
2. **Bug fixes**: Test thoroughly before committing
3. **Documentation**: Update README.md and USAGE.md as needed
4. **Slash commands**: Sync using `./grab-slash-commands.sh` after changes
5. **Testing**: Validate changes don't break existing deployments

## Common Questions

**Q: Should I deploy all templates?**
A: No, only deploy templates for directories you actually use. Use the interactive setup wizard (`/set-stuff-up`) to choose relevant templates.

**Q: Can I customize templates before deploying?**
A: Yes! Templates are meant to be starting points. Customize them for your specific needs.

**Q: How do I update deployed templates?**
A: Pull the latest changes from this repo, then re-deploy templates to update existing installations.

**Q: What if I have personal information in templates?**
A: Use the `/depersonalise` slash command to remove personal information before sharing or committing.

## Related Files

- **User's home CLAUDE.md**: `/home/daniel/CLAUDE.md` (general system context)
- **Repos directory CLAUDE.md**: `/home/daniel/repos/CLAUDE.md` (repos-level context)
- **Deployed templates**: Various CLAUDE.md files throughout `~/repos/` subdirectories

## License

MIT License - This repository and all templates are open source.

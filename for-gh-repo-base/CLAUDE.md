# CLAUDE.md For GitHub Repositories Base

## Purpose

This directory serves as the base level for cloning and managing Daniel's GitHub repositories. When operating at this level, you'll primarily be conducting batch operations across multiple repositories.

## Typical Contents

- Daniel's personal GitHub repositories
- Active development projects
- Code libraries and tools
- Utilities and scripts
- Experimental projects
- Archived or legacy repositories

## Common Tasks

When operating at this level of the filesystem, you may be asked to:

### Repository Management
- Clone multiple repositories in batch operations
- Organize repositories into logical folder structures
- Prune the collection by identifying and removing old/unused repos
- Sort repositories by visibility (private vs public)
- Archive inactive or completed projects
- Update repository metadata and descriptions

### Analysis and Auditing
- Gather requirements.txt files to identify Python package usage
- Analyze dependencies across multiple projects
- Identify security vulnerabilities or outdated dependencies
- Generate reports on repository statistics (size, activity, languages)
- Find duplicate code or common patterns across repos
- Audit licenses across projects

### Batch Operations
- Update dependencies across multiple repositories
- Apply consistent .gitignore patterns
- Add or update README files
- Standardize CI/CD configurations
- Update license files
- Apply code formatting standards
- Bulk update GitHub repo settings (topics, descriptions, etc.)

### Maintenance
- Pull latest changes across all repositories
- Check for uncommitted changes
- Identify repos that need attention
- Clean up old branches
- Update documentation

## Best Practices

1. **Organization**: Use consistent folder structure and naming conventions
2. **Documentation**: Ensure each repo has proper README and documentation
3. **Version Control**: Keep repositories in sync with remotes
4. **Security**: Regularly audit for exposed secrets or credentials
5. **Cleanup**: Periodically review and archive inactive projects
6. **Standards**: Apply consistent coding standards and tooling
7. **Backups**: Ensure important repositories are backed up

## Batch Operation Guidelines

When performing batch operations:
- Test operations on a single repository first
- Use git status to verify state before making changes
- Create backups before destructive operations
- Log operations for audit trail
- Handle errors gracefully and report failures
- Respect rate limits when using GitHub API
- Use gh CLI or GitHub API for repository metadata operations

## Working in This Directory

- Use `gh repo list` to see all GitHub repositories
- Consider using GNU Parallel for batch operations
- Script repetitive tasks for consistency
- Keep track of which repos have been processed
- Document any bulk changes in commit messages or changelogs

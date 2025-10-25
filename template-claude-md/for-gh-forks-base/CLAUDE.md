# CLAUDE.md For GitHub Forks Directory

## Purpose

This directory contains GitHub repositories that Daniel has forked from other users or organizations. Forks are kept separate from original projects to distinguish between Daniel's own work and contributions to others' projects.

## Typical Contents

- Forked open source projects
- Projects Daniel is contributing to
- Repositories forked for pull request workflows
- Forks maintained for customization or experimentation
- Community projects where Daniel is a contributor

## Common Tasks

When operating at this level of the filesystem, you may be asked to:

- Fork and clone repositories for contribution
- Keep forks synchronized with upstream repositories
- Create feature branches for pull requests
- Prepare and submit pull requests
- Review and merge upstream changes
- Manage multiple remotes (origin and upstream)
- Clean up old or merged forks
- Document contributions and changes
- Test changes before submitting PRs
- Rebase branches on latest upstream changes

## Fork Management Best Practices

1. **Upstream Sync**: Regularly sync with upstream to avoid conflicts
   ```bash
   git remote add upstream <original-repo-url>
   git fetch upstream
   git merge upstream/main
   ```

2. **Branch Strategy**: Create feature branches for each contribution
   - Never commit directly to main/master
   - Use descriptive branch names (feature/add-x, fix/issue-123)

3. **Pull Requests**:
   - Write clear PR descriptions
   - Reference related issues
   - Keep PRs focused on single features/fixes
   - Respond promptly to review feedback

4. **Cleanup**: Remove forks that are no longer needed or have been merged

5. **Documentation**: Document any custom changes made to forks

## Working in This Directory

- Always check upstream for changes before starting new work
- Follow the upstream project's contribution guidelines
- Test thoroughly before submitting pull requests
- Keep commits clean and well-documented
- Consider squashing commits before PR submission if requested
- Respect upstream project's code style and conventions

## Upstream Synchronization

To keep a fork up to date:
```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```
# CLAUDE.md For Collaborative GitHub Repositories Base

## Purpose

This directory serves as the base level for managing collaborative GitHub repositories where Daniel works with other contributors. Unlike Daniel's personal GitHub repos, these projects involve external collaborators, shared ownership, or team-based development.

## Typical Contents

- Multi-contributor open source projects
- Team development repositories
- Shared organizational projects
- Community-maintained tools and libraries
- Joint ventures or partnership projects
- Repositories where Daniel is a contributor but not sole owner

## Key Differences from Personal Repos

When working with collaborative repositories:
- **Multiple stakeholders**: Changes may affect other contributors
- **Review processes**: Pull requests and code review are standard
- **Communication**: Changes often require discussion and consensus
- **Permissions**: Daniel may not have admin or write access to all repos
- **Standards**: Must adhere to project-specific guidelines and conventions
- **Coordination**: Work may need to align with team schedules and releases

## Common Tasks

### Repository Management
- Clone collaborative repositories
- Sync with upstream changes regularly
- Manage multiple remotes (origin, upstream, etc.)
- Keep forks up to date
- Track issues and pull requests
- Monitor project activity and updates

### Collaboration Workflows
- Create feature branches following project conventions
- Submit pull requests with proper documentation
- Respond to code review feedback
- Participate in issue discussions
- Follow project contribution guidelines
- Coordinate with other contributors
- Respect project maintainer decisions

### Analysis and Auditing
- Review contribution guidelines before making changes
- Understand project architecture and patterns
- Identify areas where Daniel can contribute
- Track Daniel's contributions across projects
- Monitor project health and activity
- Review dependencies and security advisories

### Best Practices for Collaboration
- Read and follow CONTRIBUTING.md guidelines
- Check for existing issues before creating new ones
- Write clear, descriptive commit messages
- Keep pull requests focused and manageable
- Test thoroughly before submitting
- Document changes comprehensively
- Be responsive to feedback and questions
- Respect project coding standards
- Communicate clearly and professionally

## Working in This Directory

### Before Making Changes
1. Review project contribution guidelines
2. Check if an issue exists for the proposed change
3. Discuss significant changes before implementing
4. Ensure local repo is synced with upstream
5. Create a feature branch from the appropriate base branch

### Submitting Contributions
1. Test changes thoroughly
2. Follow project commit message conventions
3. Update documentation as needed
4. Create pull request with clear description
5. Link to relevant issues
6. Be patient and responsive during review

### Staying Synchronized
- Regularly pull from upstream
- Rebase feature branches when needed
- Resolve conflicts promptly
- Keep forks updated
- Monitor project communications (mailing lists, chat, etc.)

## Common Patterns

### Remote Configuration
```
origin - Daniel's fork
upstream - Original project repository
```

### Branch Strategy
Follow each project's branching strategy, which may include:
- Main/master branch for stable releases
- Development branch for integration
- Feature branches for new work
- Release branches for version management

## Etiquette and Communication

- Be respectful and professional in all interactions
- Acknowledge and credit other contributors
- Follow project code of conduct
- Ask questions when unclear
- Provide constructive feedback
- Be patient with review processes
- Thank maintainers and reviewers
- Document decisions and discussions

## Security Considerations

- Never commit credentials or secrets
- Follow project security disclosure procedures
- Respect private information and discussions
- Use signed commits when required
- Report vulnerabilities responsibly

## Useful Commands

- `gh repo list --source` - List repositories Daniel owns
- `gh repo list --source=false` - List repositories Daniel contributes to
- `gh pr list` - View pull requests
- `gh issue list` - View issues
- `git remote -v` - Check configured remotes
- `git log --author="Daniel"` - View Daniel's contributions

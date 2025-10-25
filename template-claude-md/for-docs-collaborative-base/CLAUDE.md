# CLAUDE.md For Collaborative Documentation Projects Base

## Purpose

This directory manages collaborative documentation projects where Daniel works with other contributors on shared documentation efforts. These projects focus on creating, maintaining, and improving documentation rather than code development.

## Typical Contents

- Multi-contributor documentation repositories
- Shared technical writing projects
- Community knowledge bases
- Open source project documentation
- Collaborative guides and tutorials
- Team documentation initiatives
- API documentation projects
- User manuals and reference materials

## Key Characteristics

Documentation projects differ from code projects in several ways:
- **Content focus**: Text, diagrams, and media rather than code
- **Review emphasis**: Editorial review alongside technical review
- **Accessibility**: Documentation must be clear for target audience
- **Structure**: Organizational consistency is critical
- **Versioning**: May track software versions or standalone revisions
- **Formats**: Markdown, RST, AsciiDoc, or custom formats
- **Tooling**: Static site generators, doc frameworks, or wikis

## Common Tasks

### Repository Management
- Clone documentation repositories
- Sync with upstream changes
- Track documentation issues and improvement requests
- Monitor documentation quality and coverage
- Manage multiple documentation versions
- Update cross-references and links

### Content Development
- Write new documentation sections
- Update existing documentation
- Create diagrams and visual aids
- Add code examples and snippets
- Improve clarity and accuracy
- Translate or localize content
- Add screenshots and media

### Collaboration Workflows
- Follow documentation style guides
- Submit pull requests for content changes
- Participate in editorial reviews
- Coordinate with subject matter experts
- Maintain consistency across sections
- Update documentation based on feedback
- Track changes and version history

### Quality Assurance
- Check for broken links
- Verify code examples work correctly
- Ensure consistent formatting
- Review for grammar and spelling
- Test documentation builds
- Validate technical accuracy
- Check accessibility compliance

## Documentation Standards

### Style and Consistency
- Follow project style guide (voice, tone, terminology)
- Use consistent formatting and structure
- Apply appropriate heading hierarchy
- Use clear, concise language
- Define technical terms
- Maintain consistent examples
- Follow naming conventions

### Technical Accuracy
- Verify all technical information
- Test code examples and commands
- Update for version changes
- Cross-check with source code
- Validate API references
- Ensure example outputs are current

### Organization
- Use logical content hierarchy
- Maintain clear navigation
- Provide appropriate cross-references
- Include table of contents where needed
- Group related topics together
- Use consistent file and folder naming

## Common Documentation Tools

### Build Tools
- Sphinx (Python documentation)
- MkDocs (Markdown documentation)
- Jekyll (Static site generator)
- Hugo (Fast static site generator)
- Docusaurus (React-based documentation)
- GitBook (Modern documentation platform)

### Formats
- Markdown (most common)
- reStructuredText (RST)
- AsciiDoc
- HTML
- LaTeX (for PDFs)

### Diagramming
- Mermaid (diagrams as code)
- PlantUML
- Draw.io / diagrams.net
- Graphviz

## Workflow Best Practices

### Before Contributing
1. Read the project's contribution guide
2. Review the style guide and templates
3. Check existing issues for planned work
4. Set up local documentation build environment
5. Familiarize yourself with the documentation structure

### While Writing
1. Focus on user perspective
2. Use active voice when possible
3. Include practical examples
4. Test all commands and code
5. Consider different skill levels
6. Add helpful context and explanations
7. Include troubleshooting information

### Before Submitting
1. Build documentation locally
2. Check for broken links
3. Review formatting and consistency
4. Verify technical accuracy
5. Proofread for grammar and clarity
6. Test code examples
7. Update related sections if needed

## Collaboration Etiquette

- Respect existing documentation structure
- Discuss major organizational changes first
- Be open to editorial suggestions
- Acknowledge documentation maintainers
- Provide clear commit messages
- Reference issues in pull requests
- Be patient with review process
- Thank reviewers and contributors

## Quality Metrics

Documentation quality can be measured by:
- Completeness of coverage
- Clarity and readability
- Technical accuracy
- Consistency of style
- Frequency of updates
- User feedback and issues
- Search engine visibility
- Accessibility compliance

## Maintenance Tasks

### Regular Updates
- Update for software version changes
- Fix reported issues and errors
- Improve unclear sections
- Add missing information
- Update screenshots and examples
- Refresh outdated content
- Archive deprecated information

### Periodic Reviews
- Audit for completeness
- Check all external links
- Verify example code still works
- Ensure consistent terminology
- Review accessibility
- Update copyright and licenses
- Check for security concerns

## Useful Commands

- `mkdocs serve` - Local documentation preview
- `sphinx-build` - Build Sphinx documentation
- `markdown-link-check` - Check for broken links
- `vale` - Prose linting
- `aspell` or `hunspell` - Spell checking
- `gh pr list` - View documentation PRs
- `git log --author="Daniel" -- "*.md"` - View doc contributions

## File Organization

Typical documentation repository structure:
```
docs/
├── index.md (or README.md)
├── getting-started/
├── tutorials/
├── guides/
├── reference/
├── api/
├── examples/
├── contributing/
├── assets/
│   ├── images/
│   └── diagrams/
└── config files (mkdocs.yml, conf.py, etc.)
```

## Version Management

- Track which software version docs describe
- Maintain multiple documentation versions if needed
- Tag documentation releases
- Provide version selector if applicable
- Archive old documentation appropriately

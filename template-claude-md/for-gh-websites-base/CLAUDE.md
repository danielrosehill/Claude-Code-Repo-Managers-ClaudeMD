# CLAUDE.md For GitHub-Deployed Websites

## Purpose

This directory contains websites that Daniel manages and deploys through GitHub, typically using GitHub Pages or similar deployment workflows.

## Typical Contents

- Static websites (HTML/CSS/JavaScript)
- Jekyll sites
- Hugo sites
- Next.js static exports
- Portfolio websites
- Landing pages
- Project showcase sites
- Personal or business websites

## Common Tasks

When operating at this level of the filesystem, you may be asked to:

- Create and configure new website repositories
- Update website content and styling
- Implement responsive design improvements
- Optimize website performance
- Configure GitHub Pages deployment
- Set up custom domains
- Update site metadata and SEO
- Implement analytics and tracking
- Test site builds locally before deployment
- Update dependencies and frameworks

## Deployment Considerations

- Most sites deploy via GitHub Pages (gh-pages branch or docs/ folder)
- Check for build scripts in package.json or configuration files
- Verify CNAME files for custom domains
- Test responsive design across device sizes
- Validate HTML/CSS before deployment
- Optimize images and assets for web

## Best Practices

1. **Version Control**: Commit changes with clear messages describing updates
2. **Testing**: Build and test locally before pushing to production
3. **Performance**: Optimize assets, minimize CSS/JS, compress images
4. **Accessibility**: Ensure sites meet accessibility standards (WCAG)
5. **SEO**: Include proper meta tags, structured data, sitemaps
6. **Security**: Keep dependencies updated, use HTTPS
7. **Mobile-First**: Design and test with mobile users in mind

## Working in This Directory

- Check for build tools (webpack, vite, parcel, etc.)
- Look for deployment workflows in `.github/workflows/`
- Respect existing design systems and style guides
- Consider using Daniel's preferred static site generator if starting fresh
- Test across browsers and devices before deployment
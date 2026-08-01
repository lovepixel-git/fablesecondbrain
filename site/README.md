# Fable 5 Brain Site

`site/` is a Quartz v4.5.2 static site that renders the sanitized wiki for GitHub Pages. Content comes from the mirrored `content/` directory.

The published output is the built `site/public/` directory, produced by `npm ci && npx quartz build` and deployed by `.github/workflows/pages.yml` through manual `workflow_dispatch`.

`ignorePatterns` in `quartz.config.ts` excludes volatile files: `.obsidian`, `hot.md`, and `log.md`. The accounts section is intentionally published from `site/content/accounts` and contains only public-safe tier information.

The site must never expose `.raw/` captures, full prompt text, ledgers, credentials, tokens, or local machine paths. Confirm GitHub Pages visibility before running the workflow.

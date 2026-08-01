# Publishing Notice

This repository is public research infrastructure. It is not affiliated with,
endorsed by, sponsored by, or authorized by Anthropic.

## Rights Boundary

Public availability of a source does not automatically create permission to
redistribute it. Treat copied prompt text, system-prompt captures, screenshots,
account exports, source excerpts, and third-party documentation as restricted
source evidence unless a clear license says otherwise.

## What Can Be Public

The following are designed to be safe for a public or semi-public landing page:

- High-level descriptions of the brain.
- Original summaries and operating doctrine.
- Counts, maturity status, and audit status.
- Links to official public sources.
- Short, compliant quotations within the vault's quote policy.
- Sanitized visuals that do not expose raw prompt text or private account data.

## What Must Stay Private

Do not publish through GitHub Pages, releases, public ZIPs, social posts, or
marketing pages:

- `.raw/` source captures. They are omitted from this public release.
- Full leaked prompt text or large prompt excerpts.
- Account-specific injected blocks.
- API keys, tokens, cookies, OAuth material, or credentials.
- Private user data, local paths, or machine-specific state.
- Unreviewed generated archives in `dist/`.

## GitHub Pages

GitHub Pages publishes the Quartz build of the sanitized `wiki/`, rendered via
`site/`. The full wiki is published subject to the same review checklist and
the `ignorePatterns` exclusions. The site excludes `.obsidian`, `hot.md`, and
`log.md`; the accounts section contains only public-safe tier information.
GitHub Pages visibility is controlled separately from repository visibility.
Confirm the Pages visibility before deploying.

## Review Checklist

Before publishing or pushing a release:

1. Run `python scripts/lint_vault.py --vault .`.
2. Run `python scripts/audit_brain.py --require market-ready`.
3. Run a secret scan across tracked and untracked files.
4. Confirm `.raw/` is not included in any public artifact.
5. Confirm the Pages source is the Quartz build of `site/`, built from the
   mirrored `site/content/` directory, and that `ignorePatterns` still excludes
   `.obsidian`, `hot.md`, and `log.md`. The accounts section must contain only
   public-safe tier information.
6. Confirm repository visibility and Pages visibility separately.

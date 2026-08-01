---
type: meta
title: "lint-report-2026-07-07"
status: evergreen
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/best-practices
  - note/meta
domain: best-practices
confidence: evidence-based
related:
  - "[[index]]"
  - "[[overview]]"
  - "[[hot]]"
  - "[[log]]"
  - "[[CONVENTIONS]]"
  - "[[dashboard]]"
---

# Lint Report 2026-07-07

Initial build lint, run after hub synthesis and reconciliation. Verdict: **clean**.

## Summary

- Pages: 90 (78 non-hub notes + 12 `_index.md` hubs)
- Orphan pages: 0 (every page has at least one inbound link)
- Dead wikilinks: 0 (`python3 scripts/lint_vault.py --vault .` passes)
- Frontmatter gaps: 0 (every page carries type, title, status, created, updated, tags, domain, confidence)
- Empty sections: 0
- Em or en dashes: 0
- Average note length: 94.8 lines; average wikilinks per note: 21.4
- Duplicate stems: 0 (filenames unique vault-wide)

## Issues found and fixed during this pass

- `CLAUDE.md Project Memory` filename contained `.md` mid-name, breaking link resolution; renamed to `Claude Code Project Memory` and all links retargeted.
- Hub `_index.md` files had zero inbound links; the master [[index]] now links all 12 hubs with full vault paths.
- Two hub blurbs truncated mid-wikilink by the generator; blurbs are now de-linked plain text.
- Root `shipping-rules.md`, `CODEX.md`, and lowercase `wiki/meta/dashboard.md` were required by the vault linter; added.

## Gate results at report time

- `python3 scripts/lint_vault.py --vault .` : Vault lint passed
- `python3 -m brainstein audit-brain . --json` : score 100, grade SSS+, maturity market-ready, zero critical failures

Next scheduled check: on every commit (see [[CONVENTIONS]] gates) and at the 2026-08-06 source refresh ([[Brain Refresh Flow]]).

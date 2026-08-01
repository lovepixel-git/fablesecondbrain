---
type: meta
title: "Dashboard"
status: evergreen
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/best-practices
  - note/meta
domain: best-practices
confidence: evidence-based
related:
  - "[[Start Here]]"
  - "[[CONVENTIONS]]"
  - "[[Tag Taxonomy]]"
  - "[[index]]"
  - "[[overview]]"
  - "[[hot]]"
  - "[[log]]"
---

# Dashboard

Dataview views over the vault (requires the Dataview community plugin; degrades to plain text without it).

## Notes by status

```dataview
TABLE status, domain, updated
FROM "wiki"
WHERE type != "meta"
SORT status ASC, updated DESC
```

## Seeds needing substance

```dataview
LIST
FROM "wiki"
WHERE status = "seed"
```

## Contested claims to resolve

```dataview
LIST
FROM "wiki"
WHERE confidence = "contested"
```

## Recently updated

```dataview
TABLE updated, domain
FROM "wiki"
SORT updated DESC
LIMIT 15
```

## Stale watch

Sources past `refresh_due` live in `references/source-ledger.json`; run the [[Brain Refresh Flow]] when `python3 scripts/audit_brain.py --json` flags staleness or any note carries a `> [!stale]` callout.

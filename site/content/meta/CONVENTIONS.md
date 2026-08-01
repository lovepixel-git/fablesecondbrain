---
type: meta
title: "CONVENTIONS"
status: evergreen
created: 2026-07-07
updated: 2026-07-09
tags:
  - fable5/best-practices
  - note/meta
domain: best-practices
confidence: evidence-based
related:
  - "[[Start Here]]"
  - "[[Tag Taxonomy]]"
  - "[[index]]"
  - "[[overview]]"
  - "[[hot]]"
  - "[[log]]"
---

# Conventions

This is the master copy of the vault operating contract. CLAUDE.md carries a summary;
if a `brainstein upgrade` ever clobbers CLAUDE.md, restore the contract from here.

## Three layers

- `.raw/` holds immutable source material with sha256 provenance in `.raw/.manifest.json`. Never edit files there.
- `wiki/` is the knowledge layer. Atomic notes in type folders, hubs as `_index.md`, canonical files `index.md`, `overview.md`, `hot.md`, `log.md` at the wiki root.
- `CLAUDE.md` is the contract layer for agents.

## Frontmatter contract (every wiki page)

```yaml
---
type: concept        # source|entity|concept|flow|platform|account|decision|deliverable|question|gap|experiment|comparison|meta
title: "Exact Title Case Name"
status: developing   # seed|developing|mature|evergreen
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/best-practices
  - note/concept
domain: best-practices
confidence: evidence-based
related:
  - "[[Claude Fable 5]]"
source_urls:
  - "https://docs.claude.com/... (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---
```

Rules: flat YAML only; ISO dates; lists as `- item`; wikilinks in YAML quoted; `related` has at least 6 entries; bump `updated` on every edit. `domain` is one of: model-and-family, claude-ai-harness, claude-code-harness, tools-and-skills, memory-and-context, communication-rules, safety-and-permissions, best-practices. `confidence` follows `references/CONFIDENCE_TAGS.md`. `approval_status`, `risk_level`, and `rollback_note` are added only on decision and flow notes that recommend mutations.

## Body contract (atomic notes)

Answer-first opening line, then: `## What it is`, `## How it works`, `## Best practice` (per-claim confidence tags), `## Pitfalls`, `## Sources` (dated entries), `## Related` (at least 8 wikilinks, each with a one-line why), `## Next actions`. Floor of 90 body-inclusive lines per note. Quotes from the export are verbatim, at most 15 words, attributed as `System Prompt Export 2026-07, L<start>-<end>`.

## Naming and links

Filenames Title Case and unique vault-wide; folders lowercase; wikilinks are path-less, like `[[Start Here]]`, except hubs, which may be linked with a full path like `[[meta/CONVENTIONS|CONVENTIONS]]` when a cross-folder link is ambiguous. Tags lowercase hierarchical per [[Tag Taxonomy]]. No em dashes anywhere.

### Sanctioned exceptions

- Hub files are named `_index.md` in every folder and share that basename by design; the uniqueness rule applies to note titles, not hub scaffolding.
- Entity notes named after domains keep the literal lowercase domain name, such as `docs.claude.com.md`; `claude.ai Platform.md` keeps its product spelling.
- Generated artifacts keep tool-generated names, such as `dashboard.md`, `lint-report-YYYY-MM-DD.md`, and `research-pack-YYYY-MM-DD.md`.
- Frontmatter: hub (`_index.md`), root, and meta pages use a lighter schema without `source_urls` and `sources`; content notes must carry `source_urls`, and the `sources` key is optional when `source_urls` is present and the body has a dated Sources section.

## Maintenance law

`wiki/log.md` is append-only, newest on top, entry format `## [YYYY-MM-DD] operation | Title`. `wiki/hot.md` is overwritten entirely, 500 words maximum. `wiki/index.md` is the master catalog and is updated on every save or ingest. Callouts: `> [!contradiction]`, `> [!gap]`, `> [!key-insight]`, `> [!stale]`.

## Gates

Run `python3 scripts/lint_vault.py` and `python3 scripts/audit_brain.py --json` before every commit. Do not call this brain market-ready unless the audit gate passes. The global `/save` rule routes conversation saves to the Second Brain, not this vault; write here only when explicitly operating the Fable 5 Brain.

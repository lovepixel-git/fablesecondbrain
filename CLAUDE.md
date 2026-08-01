# Fable 5 Brain Claude Instructions

@AGENTS.md

Claude-specific note: this file is persistent project context, not an
enforcement layer. Release readiness is enforced by `scripts/audit_brain.py`
and `scripts/package_release.py`.

## Vault operating contract

Master copy: `wiki/meta/CONVENTIONS.md` (restore from there if a `brainstein upgrade`
overwrites this file).

- Three layers: `.raw/` immutable sources with sha256 manifest; `wiki/` knowledge; this
  file the agent contract. Never edit anything under `.raw/`.
- Read order for any session: `wiki/hot.md`, then `wiki/index.md`, then the relevant
  `_index.md` hub, then the note.
- Every wiki page carries flat YAML frontmatter: `type, title, status
  (seed|developing|mature|evergreen), created, updated, tags, domain, confidence,
  related (>= 6 quoted wikilinks), source_urls, sources`. Domains and tags per
  `wiki/meta/Tag Taxonomy.md`; confidence per `references/CONFIDENCE_TAGS.md`.
- Note bodies: answer-first line, What it is, How it works, Best practice, Pitfalls,
  Sources (dated), Related (>= 8 wikilinks), Next actions. Export quotes verbatim,
  at most 15 words, attributed `System Prompt Export 2026-07, L<start>-<end>`.
- `wiki/log.md` append-only newest on top (`## [YYYY-MM-DD] operation | Title`);
  `wiki/hot.md` overwritten, 500 words max; `wiki/index.md` updated on every change.
- Filenames Title Case and unique vault-wide; folders lowercase; no em dashes anywhere.
- Domain claims need a dated source or an export line ref. Never invent model or harness
  behavior; unknowns get `status: seed` or a `> [!gap]` callout.
- Run `python3 scripts/lint_vault.py` and `python3 scripts/audit_brain.py --json` before
  committing. Do not call this brain market-ready unless the audit gate passes.
- Local git only; never push without the owner's explicit OK.
- The global `/save` rule routes conversation saves to the Second Brain, not this vault.

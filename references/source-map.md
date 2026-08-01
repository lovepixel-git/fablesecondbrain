# Source Map

## Raw Sources

- System prompt export metadata captured from a live claude.ai Fable 5 session, with raw capture omitted from this public release
- Claude Code changelog and release notes snapshots
- Anthropic model documentation snapshots for Fable 5

## Enrichment Sources

- Anthropic official docs at docs.anthropic.com and docs.claude.com
- Anthropic news and announcements at anthropic.com/news
- Anthropic engineering blog at anthropic.com/engineering
- Claude Code release notes and changelog on GitHub
- Anthropic model cards and system card PDFs

## Import Strategy

- Copy raw source files into `.raw/sources/`.
- Record path, hash, retrieval date, owner, and source type.
- Record external research sources in `references/source-ledger.json`.
- Record implemented schemas and adapters in `references/adapter-manifest.json`.
- Create a source note under `wiki/sources/`.
- Link affected entities, workflows, and deliverables.

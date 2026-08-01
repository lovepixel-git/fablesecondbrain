# Product Boundaries

Fable 5 Brain is an advisory, read-only Obsidian brain for Claude Fable 5 model and Claude Code harness ai operations and source-cited best practices.

## It Does

- Preserve raw sources under `.raw/`.
- Synthesize source-cited notes and deliverables.
- Maintain action queues, reports, and next actions.
- Keep decisions auditable through source links and rollback notes.
- Gate maturity through `references/source-ledger.json`,
  `references/adapter-manifest.json`, and `scripts/audit_brain.py`.

## It Does Not

- No claim about Fable 5 behavior without a dated source or a verbatim quote from the export
- Never present folklore or contested guidance as evidence-based
- No irreversible recommendation without owner, confidence, source, and rollback note
- Do not call this brain market-ready unless the audit gate passes

## Safety Risks

- Stale guidance about a fast-moving ai model presented as current
- System prompt export quoted out of context or misattributed
- Secrets or local absolute paths leaking into packaged artifacts
- Mutation of raw sources instead of append-only capture

## Maturity Boundary

This repo started as `scaffolded`. Market-ready quality requires current
research, domain adapters, deterministic demo verification, source citations,
Obsidian graph hygiene, and release scans. Current maturity is determined by
`scripts/audit_brain.py`; release packaging additionally requires a clean,
reproducible working tree.

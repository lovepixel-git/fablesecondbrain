---
type: meta
title: "Start Here"
status: evergreen
created: 2026-07-07
updated: 2026-07-09
tags:
  - fable5/best-practices
  - note/meta
domain: best-practices
confidence: evidence-based
related:
  - "[[CONVENTIONS]]"
  - "[[Tag Taxonomy]]"
  - "[[dashboard]]"
  - "[[index]]"
  - "[[overview]]"
  - "[[hot]]"
  - "[[Claude Fable 5]]"
source_urls:
  - "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f (retrieved 2026-07-07)"
---

# Start Here

This is the Fable 5 Brain: a source-cited Obsidian knowledge brain about the Claude Fable 5 model, the harnesses it runs in (claude.ai and Claude Code), and current operating best practices.

## Read order

1. [[overview]] for the big picture.
2. [[CONVENTIONS]] for the contract every note follows.
3. [[index]] for the master catalog.
4. The domain hub `_index.md` in each folder, then the atomic note.

## Ground rules

- Read before write. Cite dated sources. No em dashes.
- Every claim carries a confidence tag per `references/CONFIDENCE_TAGS.md`; folklore is never asserted.
- `.raw/` is immutable; quotes from the export are verbatim, at most 15 words, with line refs.
- Anything past its `refresh_due` in `references/source-ledger.json` is stale until re-verified.

## The eight domains

model-and-family, claude-ai-harness, claude-code-harness, tools-and-skills, memory-and-context, communication-rules, safety-and-permissions, best-practices. Each note carries one domain and one `fable5/*` tag; the graph colors by those tags per [[Tag Taxonomy]].

## Operating the brain

- Ask questions through the fable-secretary agent; it reads AGENTS.md, then this vault, and cites both the note and the official URL.
- New system prompt exports go to `.raw/sources/` with a dated name, then `scripts/import_system_prompt_export.py` parses and diffs them.
- Gates before any commit: `python3 scripts/lint_vault.py` and `python3 scripts/audit_brain.py --json`.

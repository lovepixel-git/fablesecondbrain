---
type: meta
title: "log"
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
  - "[[Start Here]]"
  - "[[CONVENTIONS]]"
  - "[[research-pack-2026-07-07|Research Pack 2026-07-07]]"
---

# Log

Append-only. New entries go at the TOP. Never edit past entries. Entry format: `## [YYYY-MM-DD] operation | Title`.

## [2026-07-07] research | GitHub Fable and Mythos leak sweep

- Operation: checked GitHub repository search, gists, prompt mirrors, and obvious Mythos false positives. Updated [[Public System Prompt Copies]], references/source-ledger.json, and references/claim-ledger.md.
- Key findings: Fable 5 has many public prompt mirrors and derivative Claude Code or Opus workflows; no verified Mythos 5 system-prompt leak was found. The visible "Mythos system prompt" gist is a mislabeled Fable prompt copy.
- Ledgers: references/source-ledger.json now records 96 sources; references/claim-ledger.md now records 187 claim rows.

## [2026-07-07] research | Mythos and Glasswing deep research wave

- Operation: ran parallel official-source research on Fable/Mythos docs, Project Glasswing history, and system-card safety evidence. Added [[Project Glasswing]], [[Fable Mythos 5 System Card]], and [[Fable Mythos Operating Doctrine]].
- Key findings: Mythos 5 is trusted-access, not a premium tier; Fable 5 and Mythos 5 share the underlying model; the system card supplies public evaluation evidence; Glasswing's bottleneck is verification, disclosure, and patching throughput after AI-assisted discovery scales.
- Ledgers: references/source-ledger.json now records 88 sources; references/claim-ledger.md now records 180 claim rows.

## [2026-07-07] review | Embodiment readiness review

- Operation: reviewed agent entrypoints, vault entrypoints, source and adapter ledgers, key embodiment notes, and release gates. Reconciled human-facing maturity and count prose to the machine-readable state: 78 sources and 160 claim rows.
- Verification: compileall passed, root vault lint passed, import/export tests passed, audit gate passed at market-ready score 100. Pipeline and package release are blocked in the current worktree by pre-existing `.obsidian/graph.json` drift.

## [2026-07-07] save | Claude Character and Constitution

- Operation: added the philosophy anchor note: constitution priority order, character training method, Fable 5 character audit metrics, and how the export instantiates the mentality. Closes the scattered-philosophy gap.

## [2026-07-07] build | Wave 3: procedural logic, design synthesis, corroboration

- Operation: coverage audit of decision logic plus a public prompt-copy hunt. Created [[System Prompt Design Logic]] (seven design patterns), [[Image Search Decision Rules]], [[Public System Prompt Copies]]; extended [[Claude Memory System]] (NEVER/CAN/SELECTIVELY tiers plus six example groups) and [[Core Search Behaviors]] (critical reminders L1594-1610).
- Key finding: Anthropic officially publishes the Fable 5 claude.ai behavioral core; eight behavioral notes now cite the official URL. Ledger 72 to 78 sources.

## [2026-07-07] build | Wave 2 reintegration and v1.1.0

- Operation: regenerated 12 hubs and the master index (85 notes), updated overview and hot, behavioral layer registered.

## [2026-07-07] fix | Integrity remediation

- Operation: adaptive-thinking contradiction resolved with fetched platform docs; knightli claims retagged PRACTITIONER; claim ledger honesty-revised with 35 SINGLE-SOURCE markers; [[Tone and Formatting Rules]] rewritten from L80-104; digest line-ref nits fixed.

## [2026-07-07] build | Wave 2 behavioral notes authored

- Operation: 3 parallel workers wrote 10 atomic notes for the export's behavioral and cognition layer, enriched with system-card and official behavioral sources.
- Pages created: [[User Wellbeing Rules]], [[Evenhandedness Rules]], [[Responding to Mistakes and Criticism]], [[Harness Refusal Handling]], [[Child Safety Rules]], [[Anthropic Runtime Reminders]], [[Adaptive Thinking and Thinking Mode]], [[Knowledge Cutoff and Search Triggers]], [[Core Search Behaviors]], [[User Preferences System]].

## [2026-07-07] research | Behavioral and thinking sources added

- Operation: two research agents verified the adaptive-thinking docs (contradiction settled: VERIFIED) and 11 official behavioral sources including the Fable 5 system card; ledger 61 to 72 sources.

## [2026-07-07] build | Hub synthesis and reconciliation

- Operation: generated 12 folder hubs, master index, overview, hot cache; reconciled wikilinks (0 dead after canonical files created).
- Pages created: all `_index.md` hubs, [[index]], [[overview]], [[hot]], this log.

## [2026-07-07] build | 69 atomic notes authored

- Operation: 9 parallel workers, disjoint folder ownership, verified claim packs as the only fact source.
- Average note length 96 lines; every note carries the frontmatter contract and at least 8 related links.

## [2026-07-07] ingest | System Prompt Export 2026-07

- Source: System Prompt Export 2026-07 (sha256 48358a42, 3826 lines, immutable).
- Summary: [[System Prompt Export 2026-07]]; chapter digests in wiki/sources.
- Key insight: the export is the claude.ai consumer harness prompt, not Claude Code (see [[Corpus Scope Decision]]).

## [2026-07-07] research | Source ledger assembled

- Operation: 7 parallel research questions plus corpus miner; adversarial verification (128 claims kept, 5 contested, 0 dropped).
- Pages created: [[research-pack-2026-07-07|Research Pack 2026-07-07]] (69 dated citations); references/source-ledger.json (61 sources); references/claim-ledger.md.

## [2026-07-07] scaffold | Brain scaffolded from Brainstein spec v2

- Operation: `brainstein new` in place with date pin 2026-07-07; corpus moved to .raw/ with manifest hash entry.

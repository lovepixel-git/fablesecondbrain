---
type: flow
title: "Corpus Ingestion Flow"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/best-practices
  - note/flow
domain: best-practices
confidence: practitioner
approval_status: approved
risk_level: low
rollback_note: "Ingestion only adds files: a new dated .raw capture, a manifest entry, and new or edited wiki notes under git; revert the ingest commit and delete the capture to undo."
related:
  - "[[System Prompt Export 2026-07]]"
  - "[[Corpus Scope Decision]]"
  - "[[Claim Verification Flow]]"
  - "[[Brain Refresh Flow]]"
  - "[[Citation Discipline]]"
  - "[[Export Chapter Product and Behavior]]"
  - "[[Export Chapter Tool Schemas]]"
  - "[[Which Export Rules Bind Claude Code]]"
  - "[[Export Omits Claude Code Harness]]"
  - "[[CONVENTIONS]]"
source_urls:
  - "https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)"
---

# Corpus Ingestion Flow

A new system prompt export enters this vault only through .raw: save it under a dated name, record its sha256 in .raw/.manifest.json, parse and diff it with scripts/import_system_prompt_export.py, then file findings as wiki notes with line-referenced citations.

## What it is

The intake pipeline for the brain's primary corpus, the captured claude.ai system prompt. Per [[CONVENTIONS]], .raw holds immutable source material with sha256 provenance in .raw/.manifest.json and is never edited. Per the [[Confidence Tag Policy]] assignment rules embedded in this vault, a claim sourced only from the export is evidence of that capture on the claude.ai harness, cited with a mandatory line reference in the form L123-145. The design mirrors Anthropic's long-running agent guidance: durable work needs persistent artifacts such as a JSON state file and descriptive history, because in-context memory alone is not sufficient.

## How it works

1. **Land the capture.** Save the new export under .raw with a dated name (pattern: a name carrying YYYY-MM, matching the existing System Prompt Export 2026-07 capture). Never overwrite a previous capture; each is a distinct snapshot.
2. **Record provenance.** Compute the file's sha256 and append it to .raw/.manifest.json alongside the filename and ingest date. The manifest is the tamper-evidence layer.
3. **Parse and diff.** Run scripts/import_system_prompt_export.py to parse the capture and diff it against the previous export. The diff, added, changed, and removed passages, is the actual finding set; unchanged text needs no new work.
4. **File findings.** Route each diff hunk to its owning chapter note (product behavior, memory, computer use, tool schemas, artifacts and citations) and update affected atomic notes. Every corpus-derived claim gets a verbatim quote of at most 15 words and an exact line attribution.
5. **Reconcile.** Where the new capture contradicts a live claim, apply the contested rule: `> [!contradiction]` callout in the owning note until a newer official source resolves it.
6. **Close the gate.** Update the source ledger, append the log entry, and run the lint and audit scripts before committing.

> [!key-insight]
> The capture is a primary source about one harness at one moment. Its value is the diff series: consecutive dated captures turn claude.ai behavior changes into observable, line-referenced evidence instead of anecdote.

## Best practice

- Keep .raw immutable; corrections happen in wiki notes, never in the capture. PRACTITIONER
- Hash at ingest time, not later; a manifest entry written after edits proves nothing. PRACTITIONER
- Diff against the previous capture before reading linearly; the delta is smaller and higher signal than the full text. PRACTITIONER
- Persist ingest state as artifacts (manifest, ledger, log) rather than relying on session memory, matching the harness principle that agents should leave durable, clean state between windows. EVIDENCE-BASED
- Give the ingest a runnable check, the vault's lint and audit scripts, in line with the Claude Code principle of verifiable checks. EVIDENCE-BASED
- Scope claims honestly: an export claim describes the claude.ai harness at capture time, not Claude Code and not the API. PRACTITIONER
- Quote at most 15 words per corpus citation with an exact L-ref, so every claim is spot-checkable against the capture. PRACTITIONER

## Pitfalls

- Editing a .raw file to fix a typo or normalize formatting; that silently invalidates the manifest hash and the line references of every citing note.
- Ingesting without dating: two undated captures cannot be diffed or cited unambiguously.
- Generalizing export claims to other harnesses; the export omits the Claude Code harness entirely, which is why [[Export Omits Claude Code Harness]] exists.
- Filing the whole capture as one giant note instead of routing diff hunks to owning chapter notes.
- Skipping the ledger update, which breaks the next [[Brain Refresh Flow]] scan.

> [!gap]
> The exact CLI flags and diff output format of scripts/import_system_prompt_export.py are not documented in any claim pack; verify against the script itself before the next ingest and record the invocation here.

## Sources

- Effective harnesses for long-running agents (persistent artifacts rationale), Anthropic Engineering: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents (published 2025-11-26, retrieved 2026-07-07)
- Best practices for Claude Code (verifiable checks principle), official docs: https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)
- Effective context engineering for AI agents (high-signal curation rationale), Anthropic Engineering: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (published 2025-09-29, retrieved 2026-07-07)

## Related

- [[System Prompt Export 2026-07]] because it is the current capture this flow ingested.
- [[Corpus Scope Decision]] because that decision fixes what counts as corpus at all.
- [[Claim Verification Flow]] because every filed finding then passes adversarial verification.
- [[Brain Refresh Flow]] because ingest updates feed the same ledger the refresh scan reads.
- [[Citation Discipline]] because L-refs and 15-word quotes are enforced at filing time.
- [[Export Chapter Product and Behavior]] because product-behavior diff hunks route there.
- [[Export Chapter Tool Schemas]] because tool-schema diff hunks route there.
- [[Which Export Rules Bind Claude Code]] because scope reconciliation depends on that analysis.
- [[Export Omits Claude Code Harness]] because it documents the flow's main scoping trap.
- [[CONVENTIONS]] because the three-layer architecture and gates come from the vault contract.

## Next actions

- Document the import script's flags and diff format inside this note after the next dry run.
- Add a manifest validation step to the lint gate so hash drift fails loudly.
- Rehearse the flow on the existing 2026-07 capture to produce a baseline diff of zero.

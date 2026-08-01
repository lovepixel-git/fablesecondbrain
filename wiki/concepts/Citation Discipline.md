---
type: concept
title: "Citation Discipline"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/communication
  - note/concept
domain: communication-rules
confidence: evidence-based
related:
  - "[[Copyright Compliance Rules]]"
  - "[[Tone and Formatting Rules]]"
  - "[[Export Chapter Artifacts API and Citations]]"
  - "[[Confidence Tag Policy]]"
  - "[[Claim Verification Flow]]"
  - "[[Corpus Ingestion Flow]]"
  - "[[docs.claude.com]]"
  - "[[Claude Fable 5]]"
  - "[[System Prompt Export 2026-07]]"
source_urls:
  - "https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Citation Discipline

Two citation regimes govern this brain: on claude.ai, Fable 5 must wrap every search-derived claim in cite tags and paraphrase it, and inside this vault, every sourced statement must carry a URL or corpus line reference plus a date.

## What it is

- The claude.ai regime: the export's citation_instructions require that "EVERY specific claim in the answer that follows from the search results" be wrapped in cite tags (System Prompt Export 2026-07, L3715-3727).
- The vault regime: this brain's own law that a Sources entry without a date is invalid, corpus claims carry line references in the L123-145 format, and claims sourced only from the export are marked as evidence of that capture, not universal truth (references/CONFIDENCE_TAGS.md, dated 2026-07-07).
- Both regimes exist to make claims auditable: the harness ties answers to retrieved documents, the vault ties notes to dated, re-checkable evidence.

## How it works

- Cite tag mechanics: each tag's index attribute encodes document and sentence spans in DOC_INDEX-START:END form, using the minimum sentences needed to support the claim (System Prompt Export 2026-07, L3715-3727).
- Scope exclusion: content from document_context is never cited; cite tags apply to search results only (System Prompt Export 2026-07, L3715-3727).
- Paraphrase mandate: "Claims must be in your own words, never exact quoted text" (System Prompt Export 2026-07, L3729-3735); citation grants attribution, not permission to reproduce source wording, even short phrases.
- Vault mechanics: every note's Sources section lists dated entries; a docs citation looks like https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07), and a corpus citation looks like System Prompt Export 2026-07, L3715-3727.
- Confidence coupling: a claim backed only by the export is EVIDENCE-BASED as primary capture evidence with a mandatory line reference; a claim corroborated by a dated public Anthropic URL is EVIDENCE-BASED outright; export-versus-docs conflicts are CONTESTED with a contradiction callout (references/CONFIDENCE_TAGS.md, dated 2026-07-07).
- Quote ceiling: verbatim quotes in vault notes stay under 15 words whether the source is the corpus or the web, and web quotes always travel with their URL (wiki/meta/CONVENTIONS.md, dated 2026-07-07).
- Corroboration habit: this brain's verified claim packs record a second source per claim where one exists, so notes can cite the strongest locator and keep a fallback.
- Staleness: anything past its refresh_due date in references/source-ledger.json must be re-verified before being cited as current.

> [!key-insight]
> The two regimes converge on one principle: a claim without a locator and a date is not knowledge, it is rumor. The harness enforces this with cite tags at answer time; the vault enforces it with lint gates at commit time.

## Best practice

- In this vault, never write a Sources entry without both a locator (URL or line reference) and a date; undated citations fail the lint gate. EVIDENCE-BASED
- Attribute corpus quotes exactly as System Prompt Export 2026-07, L<start>-<end>, and keep them at 15 words or fewer. EVIDENCE-BASED
- Say which harness a corpus claim describes (claude.ai) whenever citing the export, because the capture binds one surface only. EVIDENCE-BASED
- When claude.ai answers from search, expect paraphrased cited claims; do not prompt it to quote sources verbatim, the instructions forbid that. EVIDENCE-BASED
- Prefer a dated docs.claude.com or anthropic.com URL over any secondary blog when both support the same claim. PRACTITIONER
- On an export-versus-docs conflict, cite both, tag the claim CONTESTED, and add a contradiction callout in the owning note. EVIDENCE-BASED
- Date vault-internal laws the same way: cite CONVENTIONS and CONFIDENCE_TAGS with their updated dates so policy claims stay re-checkable. PRACTITIONER

## Pitfalls

- Trusting an undated retrieval: Anthropic docs pages change, and a URL without a retrieval date cannot be re-verified honestly.
- Citing the export for current behavior without noting it is a 2026-06-09 claude.ai snapshot; the lineup it lists is already stale.
- Expecting cite tags in API or Claude Code output; the citation_instructions are claude.ai harness rules from the capture.
- Quoting a source inside a cited claim on claude.ai; the paraphrase mandate makes quoted cited text a rule violation.
- Letting a source pass its refresh_due date and continuing to cite it as current; staleness silently downgrades the whole note.
- Citing an intermediate research pack instead of the underlying source; notes must carry the original URL or line reference so the chain stays auditable.

## Sources

- System Prompt Export 2026-07, L3715-3727, L3729-3735 (claims extracted 2026-07-07)
- Vault law: references/CONFIDENCE_TAGS.md, assignment policy (dated 2026-07-07)
- Vault law: wiki/meta/CONVENTIONS.md, body contract and maintenance law (dated 2026-07-07)
- Claude Platform Docs, Models overview, https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07), worked example of a dated citation

## Related

- [[Copyright Compliance Rules]] sets the quotation ceiling that citation must respect.
- [[Tone and Formatting Rules]] shapes the prose the citations decorate.
- [[Export Chapter Artifacts API and Citations]] holds the corpus extract of the citation_instructions.
- [[Confidence Tag Policy]] converts source quality into the tag each cited claim carries.
- [[Claim Verification Flow]] is the process that produces dated, double-sourced claims.
- [[Corpus Ingestion Flow]] is where line-referenced corpus citations are minted.
- [[docs.claude.com]] is the preferred primary target for dated public citations.
- [[Claude Fable 5]] is the model whose claude.ai answers the cite-tag regime governs.
- [[System Prompt Export 2026-07]] is the capture defining the harness-side rules quoted here.

## Next actions

- Confirm references/source-ledger.json has refresh_due entries for every URL cited in this note's cluster.
- Extract the full citation_instructions block into the owning export chapter with complete line coverage.
- Spot-check three vault notes for undated Sources entries and fix any found.
- Probe a live claude.ai search answer and record whether cite-tag behavior matches the L3715-3727 capture.

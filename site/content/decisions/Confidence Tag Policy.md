---
type: decision
title: "Confidence Tag Policy"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/best-practices
  - note/decision
domain: best-practices
confidence: practitioner
approval_status: approved
risk_level: low
rollback_note: "Tags are per-claim strings; retag affected notes with a mechanical sweep if the rules change, using references/CONFIDENCE_TAGS.md history as the baseline."
related:
  - "[[Frontmatter Dialect Decision]]"
  - "[[Corpus Scope Decision]]"
  - "[[CONVENTIONS]]"
  - "[[Tag Taxonomy]]"
  - "[[System Prompt Export 2026-07]]"
  - "[[Claim Verification Flow]]"
  - "[[No Public Fable 5 Benchmark Data]]"
  - "[[docs.claude.com]]"
  - "[[Anthropic]]"
source_urls:
  - "https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/claude-fable-5-mythos-5 (retrieved 2026-07-07)"
---

# Confidence Tag Policy

Every domain claim in this vault carries exactly one confidence tag assigned under five fixed rules from references/CONFIDENCE_TAGS.md, which privilege the corpus and dated Anthropic URLs and demote folklore.

## What it is

- A decision record adopting references/CONFIDENCE_TAGS.md as the binding assignment policy for this brain.
- Four tags exist: EVIDENCE-BASED (controlled research or authoritative primary data), PRACTITIONER (operationally useful applied judgment, not proven by studies), CONTESTED (mixed, disputed, or failed-replication evidence, always with a caveat), and FOLKLORE (popular claim without credible support, demoted and never presented as fact).
- The usage rule is strict: every domain claim carries exactly one tag, and a bestseller or popularity is not evidence.
- Fable 5 is new and public coverage is thin, so the policy adds five domain-specific assignment rules.

## How it works

The five assignment rules, verbatim in intent:

1. A claim sourced only from the system prompt export is EVIDENCE-BASED with `source_type: primary` and a mandatory line reference in the L123-145 format; it is evidence of that capture, not a universal guarantee, and the note must say which harness (claude.ai) it describes.
2. A claim corroborated by a dated public Anthropic URL (docs, news, engineering) is EVIDENCE-BASED.
3. Plausible operational advice without official confirmation is PRACTITIONER.
4. An export-versus-docs conflict is CONTESTED until resolved by a newer official source, with a `> [!contradiction]` callout in the owning note.
5. Anything past its `refresh_due` date in references/source-ledger.json is stale and must be re-verified before being cited as current.

Rule 1 works jointly with [[Corpus Scope Decision]]: the corpus is a claude.ai capture, so rule 1 evidence never generalizes to Claude Code.

FOLKLORE has no assignment rule because it never qualifies as support; it appears only inside explicit demotion sentences.

## Best practice

- Tag claims, not notes: the frontmatter `confidence` summarizes, but each guidance bullet ends with its own tag. PRACTITIONER
- Use dated Anthropic pages such as the models overview (https://platform.claude.com/docs/en/about-claude/models/overview) or the launch announcement (https://www.anthropic.com/news/claude-fable-5-mythos-5) as rule 2 anchors. EVIDENCE-BASED
- When a claim sits between rules 2 and 3, downgrade to PRACTITIONER rather than inflating to EVIDENCE-BASED. PRACTITIONER
- Pair every rule 4 CONTESTED tag with a `> [!contradiction]` callout in the owning note so the conflict is visible in graph queries. PRACTITIONER
- Never let FOLKLORE claims surface as assertions; quote them only to demote them explicitly. PRACTITIONER
- Re-verify anything past its ledger `refresh_due` date before citing it as current, per rule 5. PRACTITIONER
- Record `source_type: primary` on rule 1 claims so queries can separate capture evidence from documentation evidence. PRACTITIONER

## Pitfalls

- Tagging a whole note once and skipping per-claim tags, which hides mixed-confidence content.
- Treating popularity, virality, or bestseller status as evidence; the policy explicitly rejects this.
- Citing the corpus without a line reference; rule 1 makes the L-format reference mandatory.
- Forgetting the harness statement on rule 1 claims, which silently overgeneralizes claude.ai evidence.
- Resolving a rule 4 conflict by preference instead of waiting for a newer official source.
- Citing a stale ledger entry as current because the note text still reads plausibly.

## Sources

- Models overview, https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07); example of a rule 2 qualifying anchor.
- Claude Fable 5 and Claude Mythos 5, https://www.anthropic.com/news/claude-fable-5-mythos-5 (retrieved 2026-07-07, published 2026-06-09); example of a dated Anthropic news anchor.

## Related

- [[Frontmatter Dialect Decision]] defines the `confidence` key this policy fills.
- [[Corpus Scope Decision]] scopes rule 1 evidence to the claude.ai harness.
- [[CONVENTIONS]] points every author at this policy via the frontmatter contract.
- [[Tag Taxonomy]] holds the vault tag vocabulary this policy plugs into.
- [[System Prompt Export 2026-07]] is the primary source class rule 1 governs.
- [[Claim Verification Flow]] operationalizes rules 2 through 5 during ingestion.
- [[No Public Fable 5 Benchmark Data]] shows the policy handling absent evidence honestly and then upgrading the state once evidence lands.
- [[docs.claude.com]] is the canonical rule 2 documentation anchor.
- [[Anthropic]] publishes the news and engineering pages rule 2 accepts.

## Next actions

- Add a lint check that flags corpus citations missing an L-format line reference.
- Audit existing notes for CONTESTED tags lacking a contradiction callout.
- Review references/source-ledger.json refresh_due dates at the next brain refresh.

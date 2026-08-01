---
type: decision
title: "Corpus Scope Decision"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/harness/claude-ai
  - note/decision
domain: claude-ai-harness
confidence: evidence-based
approval_status: approved
risk_level: low
rollback_note: "Reverse by retagging corpus-backed notes; every corpus claim carries a line reference, so a scope change is a mechanical sweep."
related:
  - "[[System Prompt Export 2026-07]]"
  - "[[Export Omits Claude Code Harness]]"
  - "[[Which Export Rules Bind Claude Code]]"
  - "[[Confidence Tag Policy]]"
  - "[[Frontmatter Dialect Decision]]"
  - "[[claude.ai Platform]]"
  - "[[Claude Code Platform]]"
  - "[[Claude Code]]"
  - "[[Export Chapter Product and Behavior]]"
source_urls:
  - "https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/overview (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Corpus Scope Decision

The System Prompt Export 2026-07 is a June 9, 2026 capture of the claude.ai consumer system prompt, not Claude Code, so every corpus-only claim in this vault is tagged as evidence about the claude.ai harness alone.

## What it is

- A decision record fixing what the corpus is, what it is not, and what that means for confidence tagging vault-wide.
- What it is: a launch-day snapshot of the claude.ai consumer prompt, pinned to June 9, 2026; the post-schema identity block restates the June 09, 2026 date (System Prompt Export 2026-07, L3395-3405).
- The content inventory is consumer-shaped throughout: a budget block declaring a 190000 token budget (L1-7), a 24-tool inline harness inventory of consumer widgets (L1711-3392), consumer memory mechanics (L195-276), artifact runtime storage rules (L692-703), the claude.ai container layout with /mnt/user-data paths (L1074-1089), and a skills surface under /mnt/skills (L3740-3791).
- The capture also carries deferred-tool plumbing behind tool_search (L2940-3283) and userPreferences application rules (L846-873), both consumer-surface features.
- What it is not: a Claude Code capture. Nothing in the corpus describes the Claude Code harness, whose behavior is documented separately at code.claude.com; see [[Export Omits Claude Code Harness]].

## How it works

- Rule 1 of [[Confidence Tag Policy]] applies: a corpus-only claim is EVIDENCE-BASED with a mandatory line reference, and the owning note must state that it describes the claude.ai harness.
- A corpus claim is evidence of that capture, not a universal guarantee, and the capture is stale by design: it lists claude-sonnet-4-6 and omits claude-mythos-5 (L21-23), while current docs list claude-sonnet-5 and claude-mythos-5. The corpus lineup is stale, not wrong for its date.
- Export-versus-docs conflicts become CONTESTED under rule 4 with a contradiction callout, for example the web_fetch Zero Data Retention flag (L3083-3089) versus the documented Covered Model no-ZDR status, and the artifact-internal pin to claude-sonnet-4-20250514 (L3419-3432) versus a documented lineup containing no Sonnet 4 model.
- Claude Code claims can never rest on the corpus alone; they need code.claude.com pages or other dated public URLs under rule 2.
- Corpus-only product topics, such as Claude Cowork and the beta agents Claude in Chrome, Excel, and PowerPoint usable as Cowork tools (L25-27), stay rule 1 evidence until a public page corroborates them.

## Best practice

- State the harness explicitly in every corpus-backed note, for example "in the claude.ai harness". PRACTITIONER
- Pin corpus claims to the June 9, 2026 snapshot and re-verify against docs before treating them as current. PRACTITIONER
- Treat the documented lineup, claude-fable-5, claude-mythos-5, claude-opus-4-8, claude-sonnet-5, and claude-haiku-4-5, as current over the corpus lineup (https://platform.claude.com/docs/en/about-claude/models/overview). EVIDENCE-BASED
- Route claude.ai-versus-API discrepancies, such as the injected token budget versus the documented 1M-token default context window, into contradiction callouts instead of silently picking a winner. PRACTITIONER
- Keep a `sources` frontmatter entry on every note that uses corpus claims so corpus provenance stays queryable. PRACTITIONER
- Prefer corpus claims with tight line ranges over broad ones; narrow ranges are cheaper to re-verify at refresh. PRACTITIONER

## Pitfalls

- Reading the corpus model lineup as current; Sonnet 5 evidently shipped after the capture, and Mythos 5 is excluded from the consumer prompt because it is restricted to Project Glasswing partners.
- Assuming the claude.ai token budget bounds the API; docs give Fable 5 a 1M-token context window by default, and public docs do not list Fable 5 as a context-awareness model, so the injected budget is an unresolved harness-level detail.
- Treating the web_fetch Zero Data Retention flag as a live capability; docs designate Fable 5 a Covered Model that is not available under zero data retention.
- Citing corpus line references in support of Claude Code behavior claims; that crosses the scope boundary this decision draws.
- Repeating the corpus's framing of Fable 5 as the first Claude 5 family model (L13-19); Fable 5 and Mythos 5 were announced simultaneously on June 9, 2026 and share the same underlying model, so the wording is launch marketing, not lineage.

## Sources

- System Prompt Export 2026-07, L1-7, L21-23, L1711-3392, L3395-3405 (snapshot dated 2026-06-09, cited 2026-07-07).
- System Prompt Export 2026-07, L13-19, L25-27, L846-873, L2940-3283 (snapshot dated 2026-06-09, cited 2026-07-07).
- Models overview, https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07).
- Introducing Claude Fable 5 and Claude Mythos 5, https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07).
- Claude Code Overview, https://code.claude.com/docs/en/overview (retrieved 2026-07-07).

## Related

- [[System Prompt Export 2026-07]] is the corpus whose scope this decision fixes.
- [[Export Omits Claude Code Harness]] is the gap register entry this decision creates.
- [[Which Export Rules Bind Claude Code]] is the open question this scope boundary leaves behind.
- [[Confidence Tag Policy]] supplies the tagging rules this decision instantiates.
- [[Frontmatter Dialect Decision]] defines the `sources` key this decision governs.
- [[claude.ai Platform]] is the surface the corpus actually describes.
- [[Claude Code Platform]] is the surface the corpus does not describe.
- [[Claude Code]] documentation is the required source class for harness claims outside the corpus.
- [[Export Chapter Product and Behavior]] catalogs the consumer-shaped content that anchors this scoping.

## Next actions

- Sweep existing corpus-backed notes for a missing "claude.ai harness" scope statement.
- Open contradiction callouts for the ZDR flag and the artifact-internal Sonnet 4 pin in their owning notes.
- Watch docs for any Fable 5 context-awareness listing that would resolve the token budget question.
- Re-run this scope check whenever a newer export capture is ingested.

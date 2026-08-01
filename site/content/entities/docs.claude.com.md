---
type: entity
title: "docs.claude.com"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/best-practices
  - note/entity
domain: best-practices
confidence: evidence-based
related:
  - "[[Anthropic]]"
  - "[[Claude Fable 5]]"
  - "[[Claude 5 Model Family]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Confidence Tag Policy]]"
  - "[[Claim Verification Flow]]"
  - "[[Anthropic Engineering Blog Shelf]]"
  - "[[System Prompt Export 2026-07]]"
  - "[[Claude Console and API Platform]]"
source_urls:
  - "https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# docs.claude.com

docs.claude.com is Anthropic's official Claude documentation site and this brain's primary corroboration source; the three pages verified for this vault currently resolve under platform.claude.com/docs/en/ paths, all retrieved 2026-07-07.

## What it is

- The official documentation surface for Claude models and the Claude Platform, published by [[Anthropic]].
- Three pages are verified in the research pack, all retrieved 2026-07-07:
  - Models overview at https://platform.claude.com/docs/en/about-claude/models/overview
  - Introducing Claude Fable 5 and Claude Mythos 5 at https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5
  - Refusals and fallback at https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback
- This vault uses the canonical title docs.claude.com for the documentation entity while citing the exact verified URLs.

> [!gap] The research pack holds no verified URLs for the Claude Code docs set or the prompt engineering set, and does not establish how the docs.claude.com and platform.claude.com hostnames relate (redirect, mirror, or migration). Verify a live URL before citing either doc set or asserting the hostname relationship.

## How it works

- What each verified page evidences:
  - Models overview: the current lineup and IDs (claude-fable-5, claude-mythos-5, claude-opus-4-8, claude-sonnet-5, claude-haiku-4-5-20251001), the pinned-snapshot ID policy, prices, context windows, and Mythos 5 availability.
  - Introducing Claude Fable 5 and Claude Mythos 5: shared specs (1M context, 128k output, January 2026 cutoff, Opus 4.7 tokenizer), adaptive thinking, Covered Model 30-day retention, availability surfaces, Glasswing access, and restored access after the export-control episode.
  - Refusals and fallback: the four refusal categories, the HTTP 200 refusal shape with stop_reason "refusal", non-billing of pre-output refusals, and the three fallback paths to Opus 4.8.
- How this brain cites the site, per [[Confidence Tag Policy]]:
  - A claim corroborated by a dated public Anthropic URL is EVIDENCE-BASED.
  - Every citation carries a retrieval date, formatted "(retrieved 2026-07-07)".
  - An export-versus-docs conflict is CONTESTED until a newer official source resolves it.
  - Entries past refresh_due in references/source-ledger.json are stale and must be re-verified.
- The claude.ai harness itself points the same direction: "Any time you would otherwise rely on memory for Anthropic product details, verify here instead" (System Prompt Export 2026-07, L3756-3758).

## Best practice

- Record a retrieval date on every docs citation; undated citations cannot pass [[Claim Verification Flow]]. EVIDENCE-BASED
- Use the models overview page for lineup, ID, price, and context-window facts; it names every current pinned snapshot. EVIDENCE-BASED
- Answer refusal and fallback questions from the refusals-and-fallback page, not the launch news post; the docs carry the operational detail. PRACTITIONER
- Re-verify any docs claim past its refresh_due date in references/source-ledger.json before citing it as current. EVIDENCE-BASED
- Check docs before training memory for any Anthropic product fact, mirroring the harness's own product-self-knowledge rule. EVIDENCE-BASED

## Pitfalls

- Citing docs paths from memory; only the three URLs above are verified, and hostnames have shifted before.
- Treating the launch announcement as spec-authoritative; docs pages carry the current values when the two drift.
- Quoting Sonnet 5 introductory pricing ($2/$10 per MTok) as its list rate ($3/$15).
- Expecting docs to describe consumer harness internals; the memory system, artifact runtime, and tool inventory live only in [[System Prompt Export 2026-07]].
- Forgetting that docs pages are living documents; a retrieval date is part of the claim, not decoration.

## Sources

- Models overview, https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)
- Introducing Claude Fable 5 and Claude Mythos 5, https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)
- Refusals and fallback, https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback (retrieved 2026-07-07)
- System Prompt Export 2026-07, L3756-3758 (captured 2026-07-07)

## Related

- [[Anthropic]] - publisher of the documentation site.
- [[Claude Fable 5]] - the model whose specs these pages document.
- [[Claude 5 Model Family]] - lineup facts sourced from the models overview page.
- [[Fable 5 Dual-Use Safety Measures]] - built on the refusals-and-fallback page.
- [[Confidence Tag Policy]] - the rule making dated docs URLs EVIDENCE-BASED anchors.
- [[Claim Verification Flow]] - the workflow that checks vault claims against these pages.
- [[Anthropic Engineering Blog Shelf]] - companion shelf for engineering posts outside the docs.
- [[System Prompt Export 2026-07]] - the corpus these docs corroborate or contest.
- [[Claude Console and API Platform]] - the platform surface the docs primarily serve.
- [[research-pack-2026-07-07|Research Pack 2026-07-07]] - where each page's retrieval is logged.

## Next actions

- Verify live URLs for the Claude Code docs set and the prompt engineering set, then close the gap callout.
- Establish the docs.claude.com versus platform.claude.com hostname relationship with a dated check.
- Add refresh_due entries for the three verified pages to references/source-ledger.json if missing.

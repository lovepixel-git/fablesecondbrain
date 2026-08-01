---
type: concept
title: "Copyright Compliance Rules"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/communication
  - note/concept
domain: communication-rules
confidence: evidence-based
related:
  - "[[Citation Discipline]]"
  - "[[Tone and Formatting Rules]]"
  - "[[Export Chapter Artifacts API and Citations]]"
  - "[[Artifacts Usage Criteria]]"
  - "[[Confidence Tag Policy]]"
  - "[[CONVENTIONS]]"
  - "[[Claude Fable 5]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[System Prompt Export 2026-07]]"
source_urls:
  - "https://www.anthropic.com/legal/aup (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Copyright Compliance Rules

The claude.ai harness enforces three hard copyright limits on Fable 5, quotes under 15 words, one quote per source, and zero reproduction of lyrics, poems, or haikus, and this vault adopts the same 15-word ceiling as its own quoting law.

## What it is

- The copyright block of the claude.ai system prompt: hard limits that apply to every response, artifacts included, regardless of user instruction.
- Hard limit one: "15+ words from any single source is a SEVERE VIOLATION" (System Prompt Export 2026-07, L1279-1284).
- Hard limit two: "ONE quote per source MAXIMUM" (System Prompt Export 2026-07, L1365-1377); after one quote, that source is closed and everything further from it must be fully paraphrased.
- Hard limit three: "Never reproduce or quote song lyrics, poems, or haikus in ANY form" (System Prompt Export 2026-07, L1352-1354); these count as complete creative works, banned even one line at a time, even when they appear inside search results or artifacts.
- The severity language is the strongest in the captured copyright block: the 15-word breach is explicitly labeled a severe violation, not a soft guideline.

## How it works

- Scope: the limits bind every output surface of the claude.ai session, including artifact content, so a long quote inside generated code or a document is still a violation (System Prompt Export 2026-07, L1279-1284).
- Reinforcement from citations: cited claims must be paraphrased, "Claims must be in your own words, never exact quoted text" (System Prompt Export 2026-07, L3729-3735), so citation never becomes a quoting loophole.
- Runtime enforcement: the harness can inject an ip_reminder among its six classifier-triggered reminder types, and reminders never reduce restrictions (System Prompt Export 2026-07, L144-152).
- Policy backdrop: Anthropic's Usage Policy (effective 2025-09-15) frames the contractual layer above these prompt-level rules through its Universal Usage Standards (https://www.anthropic.com/legal/aup, retrieved 2026-07-07).
- Vault adoption: this brain's CONVENTIONS require export quotes to be verbatim, at most 15 words, attributed as System Prompt Export 2026-07, L<start>-<end>, mirroring the harness ceiling (wiki/meta/CONVENTIONS.md, dated 2026-07-07).
- Vault adoption for web sources: quotes from public pages follow the same sub-15-word ceiling and always carry the source URL, so every quoted fragment stays inside both regimes at once.

> [!key-insight]
> The three limits compose into one simple budget: per source, at most one quote of under 15 words, and for lyrics, poems, and haikus the budget is zero. Everything beyond the budget must be paraphrase with attribution.

## Best practice

- Keep every verbatim quote in vault notes under 15 words and attach an exact line reference or URL. EVIDENCE-BASED
- Take at most one quote from any single source in a given output, then paraphrase everything else from it. EVIDENCE-BASED
- Never reproduce lyrics, poems, or haikus in any note, artifact, or reply, even as a single line, even when quoting a source that quotes them. EVIDENCE-BASED
- When summarizing copyrighted web content, paraphrase and cite rather than quote; the citation regime and copyright regime agree on this. EVIDENCE-BASED
- Do not expect user instructions to lift these limits on claude.ai; they are hard limits, and runtime reminders only ever tighten behavior. EVIDENCE-BASED
- When a research pack hands you a longer verbatim passage, trim it to under 15 words or convert it to paraphrase before it enters a note. PRACTITIONER
- Prefer paraphrase even below 15 words unless the exact wording is load-bearing, as with definitions, error strings, or disputed phrasing. PRACTITIONER

## Pitfalls

- Counting the limit as "15 words allowed": the export marks 15 or more words as the violation, so 14 words is the practical maximum.
- Assuming attribution neutralizes over-quoting: the citation rules grant attribution, never permission to reproduce source wording (System Prompt Export 2026-07, L3729-3735).
- Quoting the same source twice in one response because each quote is short; the per-source cap is one, independent of length.
- Hiding quotes inside artifacts or code blocks and assuming the limits do not follow; the rules explicitly cover artifacts.
- Treating a haiku as safe because it is only 17 syllables; short creative works are banned in full, not by length.
- Forgetting the vault mirrors these limits: an over-quoting note fails vault law even though it never runs on claude.ai.
- Reading these as API-level rules; they are claude.ai harness rules from the 2026-06-09 capture, while API and Claude Code obligations flow from the Usage Policy layer.

## Sources

- System Prompt Export 2026-07, L1279-1284, L1365-1377, L1352-1354, L3729-3735, L144-152 (claims extracted 2026-07-07)
- Anthropic, Usage Policy, https://www.anthropic.com/legal/aup (effective 2025-09-15, retrieved 2026-07-07)
- Vault law: wiki/meta/CONVENTIONS.md, body contract quoting rule (dated 2026-07-07)

## Related

- [[Citation Discipline]] is the attribution regime that makes paraphrase auditable.
- [[Tone and Formatting Rules]] governs the prose around the quoting ceiling.
- [[Export Chapter Artifacts API and Citations]] owns the corpus extract these limits come from.
- [[Artifacts Usage Criteria]] defines the artifact surface the limits explicitly reach into.
- [[Confidence Tag Policy]] tags the claims that paraphrase replaces quotes with.
- [[CONVENTIONS]] codifies the vault's mirrored 15-word quoting law.
- [[Claude Fable 5]] is the model whose claude.ai output these limits constrain.
- [[Fable 5 Dual-Use Safety Measures]] shows the same classifier-and-reminder enforcement pattern on safety topics.
- [[System Prompt Export 2026-07]] is the primary capture for every hard limit cited here.

## Next actions

- Add a lint check that flags vault quotes of 15 or more words between quotation marks.
- Extract the full copyright block (L1279-1377) into the owning export chapter for complete coverage.
- Re-verify the three hard limits against the next claude.ai capture before citing them as current.
- Check whether a future capture changes the ip_reminder wording or the one-quote-per-source cap.

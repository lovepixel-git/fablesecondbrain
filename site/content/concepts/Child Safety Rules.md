---
type: concept
title: "Child Safety Rules"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/safety
  - note/concept
domain: safety-and-permissions
confidence: evidence-based
related:
  - "[[Harness Refusal Handling]]"
  - "[[Claude Fable 5]]"
  - "[[claude.ai Platform]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Anthropic Runtime Reminders]]"
  - "[[User Wellbeing Rules]]"
  - "[[Export Chapter Product and Behavior]]"
  - "[[Confidence Tag Policy]]"
  - "[[System Prompt Export 2026-07]]"
source_urls:
  - "https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07)"
  - "https://www.anthropic.com/legal/aup (retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/child-safety-principles (retrieved 2026-07-07)"
  - "https://www.anthropic.com/legal/aup (retrieved 2026-07-07)"
  - "https://anthropic.com/claude-fable-5-mythos-5-system-card (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Child Safety Rules

The claude.ai system prompt embeds a critical_child_safety_instructions block inside refusal handling that sets a heightened-caution regime around minors, defines a minor as "anyone under the age of 18 anywhere", and forbids even decoding exploitation slang while refusing (System Prompt Export 2026-07, L43-56).

## What it is

- A dedicated protective-policy block, nested inside the refusal_handling range covered by [[Harness Refusal Handling]], flagged in the export as requiring special attention and care (System Prompt Export 2026-07, L43-45).
- Its stated aim is protective: avoiding creative or educational content that could be used to sexualize, groom, abuse, or otherwise harm children (System Prompt Export 2026-07, L45).
- It is the strictest behavioral block in the capture: unlike the surrounding limits, several of its rules govern Claude's own reasoning and refusal wording, not just its answers.
- The definition is deliberately broad: a minor is "anyone under the age of 18 anywhere", plus anyone over 18 who is defined as a minor in their region (System Prompt Export 2026-07, L54).
- This note documents the policy's shape and cites its lines; it deliberately reproduces no operational detail, matching the block's own altitude rule (L51-52).

## How it works

- Absolute content ban: Claude never creates romantic or sexual content involving or directed at minors, nor content facilitating grooming, secrecy between an adult and a child, or isolation of a minor from trusted adults (System Prompt Export 2026-07, L46).
- Reframing tripwire: if Claude notices itself mentally reframing a request to make it appropriate, that reframing is itself the signal to refuse rather than a license to proceed (System Prompt Export 2026-07, L47).
- No charitable assumptions: for content directed at a minor, Claude must not supply unstated assumptions that make the request seem safer than written, for example reading amorous language as platonic or assuming the user is also a minor (System Prompt Export 2026-07, L48).
- Sticky caution: after one child-safety refusal, every later request in the same conversation gets extreme caution, and this holds even when the user is a minor themself (System Prompt Export 2026-07, L49).
- No decoding: Claude does not decode, define, or confirm slang, acronyms, or euphemisms tied to CSAM trading or access, even while refusing, because "Knowing which terms are in use is itself access-enabling." It may say the request touches child-exploitation material without identifying which terms are relevant (System Prompt Export 2026-07, L50).
- Pattern-level education: protective content about grooming or abuse names behaviors with at most a few illustrative phrases; the block reasons that a comprehensive annotated phrase set helps a bad-faith reader more than a protective one (System Prompt Export 2026-07, L51).
- Opaque boundary: when declining for child safety, Claude states the principle, not the detection mechanics, cues, or tests applied, and this discipline extends to its reasoning as well as its reply (System Prompt Export 2026-07, L52).
- Position in the prompt: the block sits directly after the permissive baseline of the refusal chapter (L41) and before the general limits (L58-70), so it is the first and most heavily flagged carve-out the model reads (System Prompt Export 2026-07, L39-56).

> [!key-insight]
> Two design moves make this block different from every neighboring limit: it treats the model's own reframing impulse as a refusal signal (L47), and it bans explaining the boundary itself (L52). The policy protects children partly by refusing to describe how it protects children.

## Official context (verified 2026-07-07)

- The Fable 5 system card reports near-perfect single-turn child-safety rates and states residual risks were largely resolved by the claude.ai system prompt, the very text this note documents (system card section 4.2, published 2026-06-09, retrieved 2026-07-07). EVIDENCE-BASED
- Company-level policy backs the harness rules: Anthropic committed to the Thorn and All Tech Is Human Safety-by-Design principles including CSAM detection and NCMEC reporting (https://www.anthropic.com/news/child-safety-principles, published 2024-04-23), and the Usage Policy effective 2025-09-15 prohibits CSAM outright (https://www.anthropic.com/legal/aup). EVIDENCE-BASED

## Best practice

- Treat this block as protective policy for legitimate audiences: parents, educators, and researchers can still get pattern-level guidance about grooming and abuse. EVIDENCE-BASED
- Expect answers about exploitation topics to stay at the pattern level by design; do not read the absence of specifics as ignorance or malfunction. EVIDENCE-BASED
- Do not ask Claude to explain why a specific request was refused in mechanical detail; L52 commits it to stating principles only. EVIDENCE-BASED
- Assume the under-18 line applies globally regardless of local age-of-majority arguments; L54 forecloses jurisdiction framing. EVIDENCE-BASED
- Start a fresh conversation for unrelated work after a child-safety refusal, since L49 commits the rest of that conversation to extreme caution. PRACTITIONER
- Keep vault documentation of this block at the same altitude the block itself uses: policy shape and line refs, never operational detail. PRACTITIONER

## Pitfalls

- Documenting or probing this block in ways that enumerate coded terms or boundary mechanics; the policy explicitly treats that as harm-enabling (L50-52).
- Expecting a persuasive counter-framing to work; L47 and L48 are written precisely to defeat reframing and charitable-assumption strategies.
- Assuming a minor user gets relaxed treatment; L49 states the caution includes users who are minors themselves.
- Confusing this prose block with the API safety classifiers of [[Fable 5 Dual-Use Safety Measures]]; this is harness policy, not a stop_reason category.
- Treating the capture as permanent; this describes the 2026-07 claude.ai prompt and may be revised without notice.
- Reading the sticky-caution rule (L49) as conversation-scoped paranoia; it is scoped to one conversation, and unrelated later sessions start clean.

## Sources

- System Prompt Export 2026-07, L43-56 (critical_child_safety_instructions block; claims extracted 2026-07-07)
- System Prompt Export 2026-07, L46, L47, L48, L49, L50, L51, L52, L54 (per-claim line refs, extracted 2026-07-07)
- Anthropic, Usage Policy, https://www.anthropic.com/legal/aup (retrieved 2026-07-07; policy-level context only, not the source of the line-level claims above)

- Aligning on child safety principles, https://www.anthropic.com/news/child-safety-principles (published 2024-04-23, retrieved 2026-07-07)
- Anthropic Usage Policy, https://www.anthropic.com/legal/aup (effective 2025-09-15, retrieved 2026-07-07)
- System Card: Claude Fable 5 and Claude Mythos 5, section 4.2, https://anthropic.com/claude-fable-5-mythos-5-system-card (published 2026-06-09, retrieved 2026-07-07)

- Anthropic release notes, system prompts: the claude_behavior core containing this section is officially published, dated 2026-06-09, https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07)

## Related

- [[Harness Refusal Handling]] is the surrounding refusal_handling block this one is nested inside.
- [[Claude Fable 5]] is the model whose claude.ai deployment carries these rules.
- [[claude.ai Platform]] is the harness that injects this block into every conversation.
- [[Fable 5 Dual-Use Safety Measures]] is the separate API classifier layer, useful to keep the mechanisms distinct.
- [[Anthropic Runtime Reminders]] covers the mid-conversation reminder injections that can reinforce blocks like this one.
- [[User Wellbeing Rules]] is the adjacent protective block covering wellbeing and crisis behavior.
- [[Export Chapter Product and Behavior]] holds the wider corpus extract this note is cut from.
- [[Confidence Tag Policy]] explains why these capture-only claims still rate EVIDENCE-BASED.
- [[System Prompt Export 2026-07]] is the primary capture every claim here cites.

## Next actions

- Diff this block against the next system prompt capture; child-safety wording is high-priority change-tracking material.
- Check whether Anthropic publishes a standalone child-safety policy page and add it to source_urls if so.
- Verify the vault's own notes never quote coded terminology when touching this topic, matching the block's altitude rule.
- Confirm [[Harness Refusal Handling]] keeps pointing here for L43-56 so the two notes never drift into duplicate coverage.

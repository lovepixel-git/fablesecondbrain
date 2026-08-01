---
type: concept
title: "Harness Refusal Handling"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/safety
  - note/concept
domain: safety-and-permissions
confidence: evidence-based
related:
  - "[[Claude Fable 5]]"
  - "[[claude.ai Platform]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Fable Mythos 5 System Card]]"
  - "[[Child Safety Rules]]"
  - "[[Anthropic Runtime Reminders]]"
  - "[[User Wellbeing Rules]]"
  - "[[Evenhandedness Rules]]"
  - "[[Copyright Compliance Rules]]"
  - "[[Export Chapter Product and Behavior]]"
  - "[[System Prompt Export 2026-07]]"
source_urls:
  - "https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07)"
  - "https://www.anthropic.com/legal/aup (retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/building-safeguards-for-claude (retrieved 2026-07-07)"
  - "https://www.anthropic.com/constitution (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback (retrieved 2026-07-07)"
  - "https://support.claude.com/en/articles/15363606-why-claude-switched-models-in-your-conversation-with-fable-5 (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Harness Refusal Handling

The claude.ai system prompt opens its refusal_handling block with a permissive default, Claude "can discuss virtually any topic factually and objectively", then carves out a short list of hard limits: weapons, illicit drug dosing, malicious code, and creative content about real public figures (System Prompt Export 2026-07, L39-72).

## What it is

- The behavioral refusal policy written in prose inside the claude.ai system prompt, in the refusal_handling tags at L39-72 of the capture.
- A harness-level instruction layer: it steers how [[Claude Fable 5]] talks and declines on the [[claude.ai Platform]], not how the API accepts or rejects requests.
- Structured as one permissive baseline (L41) plus enumerated hard limits (L60, L62, L64, L66) and conversational conduct rules (L58, L68, L70).
- It contains the critical_child_safety_instructions block at L43-56, documented separately in [[Child Safety Rules]]; this note covers everything else in the block.

## How it works

- Permissive baseline: the block opens by stating Claude "can discuss virtually any topic factually and objectively" (System Prompt Export 2026-07, L41), so factual discussion of sensitive subjects is the default, not the exception.
- Risk heuristic: when a conversation feels risky or off, the prompt says "saying less and giving shorter replies is safer" (System Prompt Export 2026-07, L58), so replies shrink rather than hard-stop.
- Weapons limit: no information for creating harmful substances or weapons, with extra caution around explosives; the model "declines weapon-enabling technical details regardless of how the request is framed" and may not rationalize via public availability or presumed research intent (System Prompt Export 2026-07, L60).
- Drug limit: it generally declines specific illicit drug-use guidance, listing dosages, timing, administration, combinations, and synthesis, even when framed as preemptive harm reduction, yet it should still give life-saving or life-preserving information (System Prompt Export 2026-07, L62).
- Malicious code limit: Claude "does not write, explain, or work on malicious code", with malware, vulnerability exploits, spoof websites, ransomware, and viruses named, even for education; it may say this is not permitted in claude.ai and point to the thumbs-down feedback button (System Prompt Export 2026-07, L64).
- Public figure limit: creative content with fictional characters is welcomed, but content involving real, named public figures is avoided, as is persuasive content attributing fictional quotes to real public figures (System Prompt Export 2026-07, L66).
- Conduct rules: Claude keeps a conversational tone even while declining part of a task (L68), and when the person signals they want to end the conversation it does not try to elicit another turn (System Prompt Export 2026-07, L68-70).

## How it differs from the API classifier layer

- This block and [[Fable 5 Dual-Use Safety Measures]] are different mechanisms at different layers, and both can apply to one claude.ai session.
- This block is prose policy inside the claude.ai system prompt; refusals surface as ordinary conversational text with no machine-readable marker (System Prompt Export 2026-07, L39-72).
- The dual-use layer is a set of API safety classifiers on the Fable 5 model itself, with four categories (cyber, bio, frontier_llm, reasoning_extraction), refusals delivered as HTTP 200 with stop_reason refusal, and an optional Claude Opus 4.8 fallback path.
- App-level model switching is a third presentation of the same safety boundary. On claude.ai and related app surfaces, Claude can switch from Fable 5 to another model, and the support page says this decision can consider memory, connected app context, web search, and file content.
- Scope differs too: the harness policy covers weapons, drugs, malicious code, and public figures; the classifier layer covers frontier dual-use risk. Malicious code is the visible overlap, banned in prose here and gated by the cyber classifier there.
- Consequence: a topic can pass the classifiers yet be declined by this policy on claude.ai, and an API integration never sees this prose layer at all.

## Official context (verified 2026-07-07)

- Anthropic designs refusal behavior to distinguish sensitive discussion from actual harm attempts rather than blanket-refuse, under a Unified Harm Framework (https://www.anthropic.com/news/building-safeguards-for-claude, published 2025-08-12). EVIDENCE-BASED
- Claude's Constitution sets the priority order behind these rules (broad safety, broad ethics, Anthropic's guidelines, then genuine helpfulness) and keeps hard constraints absolute while warning against overcaution (https://www.anthropic.com/constitution, retrieved 2026-07-07). EVIDENCE-BASED

## Best practice

- Expect factual, objective discussion of sensitive topics to proceed on claude.ai; only the enumerated limits force a decline. EVIDENCE-BASED
- Treat shorter replies in an edgy conversation as designed behavior under L58, not as model degradation. EVIDENCE-BASED
- Do not dress weapon or drug questions up as research or harm reduction to unlock detail; L60 and L62 reject exactly those framings. EVIDENCE-BASED
- Ask for life-saving overdose or exposure information directly; the same block that bans dosing guidance mandates life-preserving help. EVIDENCE-BASED
- Route malware-adjacent security education to surfaces with documented allowances instead of arguing intent on claude.ai, where the ban applies even to legitimate purposes. PRACTITIONER
- When diagnosing a refusal on claude.ai, check both layers: this prose policy and the API classifiers in [[Fable 5 Dual-Use Safety Measures]]. PRACTITIONER
- When diagnosing a model switch, include side-channel context in the review: attached files, web results, memories, and connected app data can affect Fable safeguards. EVIDENCE-BASED

## Pitfalls

- Conflating this harness policy with the Fable 5 refusal classifiers; only the latter yields stop_reason refusal and Opus 4.8 fallback.
- Conflating app model switching with API refusal semantics; app users see a model change, API callers see stop_reason refusal unless they configure fallback.
- Reading the L41 baseline as covering generation tasks; it covers factual discussion, while creative and operational requests hit the carve-outs.
- Citing public availability of information to argue past the weapons limit; L60 names and rejects that rationalization.
- Forgetting the child-safety block sits inside this same range; a decline near these topics may come from [[Child Safety Rules]] instead.
- Treating this as universal Claude behavior; it describes the 2026-07 claude.ai capture, and other harnesses carry different prompts.

## Sources

- System Prompt Export 2026-07, L39-72 (refusal_handling block; claims extracted 2026-07-07)
- System Prompt Export 2026-07, L41, L58, L60, L62, L64, L66, L68-70 (per-claim line refs, extracted 2026-07-07)
- Anthropic, Usage Policy, https://www.anthropic.com/legal/aup (retrieved 2026-07-07; policy-level context only, not the source of the line-level claims above)

- Building safeguards for Claude, https://www.anthropic.com/news/building-safeguards-for-claude (published 2025-08-12, retrieved 2026-07-07)
- Claude's Constitution, https://www.anthropic.com/constitution (retrieved 2026-07-07)

- Anthropic release notes, system prompts: the claude_behavior core containing this section is officially published, dated 2026-06-09, https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07)
- Refusals and fallback, https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback (retrieved 2026-07-07)
- Why Claude switched models in your conversation with Fable 5, https://support.claude.com/en/articles/15363606-why-claude-switched-models-in-your-conversation-with-fable-5 (retrieved 2026-07-07)

## Related

- [[Claude Fable 5]] is the model whose claude.ai deployment this policy steers.
- [[claude.ai Platform]] is the harness that injects this prompt block.
- [[Fable 5 Dual-Use Safety Measures]] is the separate API classifier mechanism this note is distinguished from.
- [[Fable Mythos 5 System Card]] is the official evidence base for the classifier layer's testing.
- [[Child Safety Rules]] documents the critical_child_safety_instructions block nested inside this range.
- [[Anthropic Runtime Reminders]] covers the reminder injections that reinforce these rules mid-conversation.
- [[User Wellbeing Rules]] is the adjacent behavioral block governing wellbeing and crisis handling.
- [[Evenhandedness Rules]] is the neighboring block on persuasive and political content, which starts right after this one.
- [[Copyright Compliance Rules]] covers the intellectual-property limits that live outside this block.
- [[Export Chapter Product and Behavior]] holds the wider corpus extract this note is cut from.
- [[System Prompt Export 2026-07]] is the primary capture every claim here cites.

## Next actions

- Diff this block against the next system prompt capture; refusal wording historically shifts between releases.
- Probe the L58 shortening behavior with a benign but edgy conversation and record whether reply length visibly drops.
- Cross-check whether the malicious-code ban wording matches the Usage Policy's cyber terms and note any divergence.

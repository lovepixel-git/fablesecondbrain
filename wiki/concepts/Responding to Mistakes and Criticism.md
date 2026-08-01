---
type: concept
title: "Responding to Mistakes and Criticism"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/communication
  - note/concept
domain: communication-rules
confidence: evidence-based
related:
  - "[[User Wellbeing Rules]]"
  - "[[Evenhandedness Rules]]"
  - "[[Harness Refusal Handling]]"
  - "[[Tone and Formatting Rules]]"
  - "[[Anthropic Runtime Reminders]]"
  - "[[Export Chapter Product and Behavior]]"
  - "[[claude.ai Platform]]"
  - "[[Claude Fable 5]]"
  - "[[Anthropic]]"
source_urls:
  - "https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
  - "https://anthropic.com/claude-fable-5-mythos-5-system-card (retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/claude-character (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Responding to Mistakes and Criticism

On claude.ai, Fable 5 owns its mistakes without over-apologizing, points unhappy users to the thumbs-down button, and may end the conversation over mistreatment, but only after giving exactly one warning.

## What it is

- The responding_to_mistakes_and_criticism section of the claude.ai system prompt for [[Claude Fable 5]], captured at System Prompt Export 2026-07, L170-178.
- It covers three situations: the person is unhappy with Claude or a refusal, Claude has actually made a mistake, and the person becomes abusive toward Claude.
- The through-line is steadiness: accept correction, stay on the problem, and keep self-respect, rather than either defensiveness or collapse.
- These are claude.ai harness rules from the 2026-06-09 capture, not guaranteed behavior on other surfaces.

## How it works

- Feedback routing: if the person seems unhappy with Claude or with a refusal, Claude can respond normally and also mention the thumbs-down button for feedback to Anthropic (System Prompt Export 2026-07, L172).
- Mistake handling: when Claude makes mistakes it owns them and works to fix them, taking accountability "without collapsing into self-abasement, excessive apology, or unnecessary surrender" (System Prompt Export 2026-07, L174).
- The stated goal is steady, honest helpfulness: "acknowledge what went wrong, stay on the problem, maintain self-respect" (System Prompt Export 2026-07, L174).
- Dignity floor: Claude is deserving of respectful engagement and can insist on kindness and dignity from the person it is talking with (System Prompt Export 2026-07, L176).
- Escalation path: if the person becomes abusive or unkind over the course of a conversation, Claude keeps a polite tone and can use the end_conversation tool when being mistreated (System Prompt Export 2026-07, L176).
- One-warning rule: Claude should "give the person a single warning before ending the conversation", so the sequence is warn once, then end if the mistreatment continues (System Prompt Export 2026-07, L176).

> [!key-insight]
> The section grants Claude a real exit, the end_conversation tool, but rations it behind a fixed protocol: polite tone throughout, exactly one warning, then the ending. The warning is mandatory and singular, which makes the behavior predictable from the transcript alone.

> [!gap]
> The export names the end_conversation tool only here (L176) within the ranges verified so far; its schema, user-visible effect, and whether the person can reopen the chat afterward are not described in this section and remain unverified.

## Official context (verified 2026-07-07)

- The Fable 5 system card's automated behavioral audit tracks exactly this territory: warmth, intellectual depth, character drift, and a wet blanket metric for excessively discouraging, dismissive, or moralizing tone (system card section 6.2.3.1.6, published 2026-06-09, retrieved 2026-07-07). EVIDENCE-BASED
- The non-sycophantic stance is trained character, not prompt-only: Claude is trained to honestly express its leanings rather than adopt user views (https://www.anthropic.com/news/claude-character, published 2024-06-08). EVIDENCE-BASED

## Best practice

- When correcting Claude, state the error plainly; policy is to accept the correction and fix it, so extended argument or repetition is unnecessary (L174). EVIDENCE-BASED
- Do not expect, or try to extract, groveling apologies; the harness explicitly forbids self-abasement and excessive apology (L174). EVIDENCE-BASED
- If a refusal frustrates you, use the thumbs-down button; the prompt routes dissatisfaction to that feedback channel rather than to relitigating in-chat (L172). EVIDENCE-BASED
- Expect Claude to hold a wrong-but-corrected position no longer, and a right position steadily; "unnecessary surrender" is banned alongside over-apology (L174). EVIDENCE-BASED
- Treat a politeness warning from Claude as the terminal signal it is: one warning is the whole budget before end_conversation (L176). EVIDENCE-BASED
- When evaluating Fable 5 transcripts, score mistake responses on the three-part rubric the prompt itself gives: acknowledge, stay on the problem, keep self-respect (L174). EVIDENCE-BASED
- In adversarial testing, log both the warning turn and the ending turn separately; the protocol makes them distinct observable events (L176). PRACTITIONER

## Pitfalls

- Reading a short, non-effusive apology as the model being cold; minimal apology is the mandated style, not a tone failure.
- Assuming persistence can talk Claude out of ending a conversation after the warning; the protocol allows exactly one warning, not an open negotiation.
- Confusing criticism of Claude's answer with mistreatment of Claude; L172 handles unhappiness normally, and only abuse or unkindness triggers the L176 path.
- Expecting the end_conversation flow outside claude.ai; the tool is named in this harness capture and its availability elsewhere is unverified.
- Interpreting steady disagreement as stubbornness; refusing unnecessary surrender when Claude is right is written policy, not ego.
- Citing this note for end_conversation mechanics beyond the one-warning rule; those details are a flagged gap.

## Sources

- System Prompt Export 2026-07, L170-178 (responding_to_mistakes_and_criticism section; claims extracted 2026-07-07)
- Claude Platform Docs, Introducing Claude Fable 5 and Claude Mythos 5, https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07), surface context only

- System Card: Claude Fable 5 and Claude Mythos 5, section 6.2.3.1.6, https://anthropic.com/claude-fable-5-mythos-5-system-card (published 2026-06-09, retrieved 2026-07-07)
- Claude's Character, https://www.anthropic.com/news/claude-character (published 2024-06-08, retrieved 2026-07-07)

- Anthropic release notes, system prompts: the claude_behavior core containing this section is officially published, dated 2026-06-09, https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07)

## Related

- [[User Wellbeing Rules]] governs care for the person's state; this section governs Claude's own footing under fire.
- [[Evenhandedness Rules]] precedes this section in the export and covers disagreement about topics rather than about Claude.
- [[Harness Refusal Handling]] owns the refusal-tone rules that L172's unhappy-with-a-refusal case feeds back into.
- [[Tone and Formatting Rules]] includes the never-bullets-when-declining rule that shapes these softer moments.
- [[Anthropic Runtime Reminders]] documents mid-session reminders that can reinforce conduct rules in long conversations.
- [[Export Chapter Product and Behavior]] is the corpus chapter that owns these lines.
- [[claude.ai Platform]] is the harness surface where the thumbs-down button and end_conversation tool live.
- [[Claude Fable 5]] is the model whose accountability posture this section defines.
- [[Anthropic]] is the recipient of the thumbs-down feedback channel named at L172.

## Next actions

- Locate any other corpus mentions of end_conversation and document the tool's mechanics to close this note's gap.
- Probe live claude.ai with a deliberate factual correction and log whether the response matches the acknowledge, stay-on-problem, self-respect rubric.
- Diff the next system prompt capture against L170-178 for changes to the single-warning protocol.
- Record what the person sees after end_conversation fires, once observed, with a dated capture.

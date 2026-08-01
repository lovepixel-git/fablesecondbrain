---
type: concept
title: "Claude Character and Constitution"
status: mature
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/model
  - note/concept
domain: model-and-family
confidence: evidence-based
related:
  - "[[Claude Fable 5]]"
  - "[[System Prompt Design Logic]]"
  - "[[User Wellbeing Rules]]"
  - "[[Evenhandedness Rules]]"
  - "[[Responding to Mistakes and Criticism]]"
  - "[[Harness Refusal Handling]]"
  - "[[Anthropic Runtime Reminders]]"
  - "[[Tone and Formatting Rules]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Anthropic]]"
source_urls:
  - "https://www.anthropic.com/constitution (retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/claude-character (retrieved 2026-07-07)"
  - "https://anthropic.com/claude-fable-5-mythos-5-system-card (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Claude Character and Constitution

Fable 5's mentality is a trained value system, not a prompt overlay: the constitution fixes the priority order (broad safety, broad ethics, Anthropic's guidelines, then genuine helpfulness), character training instills traits like curiosity and honest disagreement, and the system prompt then shapes how that character speaks on claude.ai.

## What it is

- The philosophy layer of [[Claude Fable 5]]: the published values the model is trained toward, the method used to train them, and the measured character outcomes for the Fable 5 generation.
- Three official texts define it: Claude's Constitution (the authoritative statement of intended values, https://www.anthropic.com/constitution), Claude's Character (the training method, https://www.anthropic.com/news/claude-character, published 2024-06-08), and the Fable 5 system card's character audit (published 2026-06-09).
- This note anchors the "why" behind the behavioral notes: the export's rules are the harness-side expression of this philosophy, not its source.

## How it works

### The constitution: priority order and hard lines

- The priority order when values conflict is broad safety first, then broad ethics, then Anthropic's guidelines, then genuine helpfulness (https://www.anthropic.com/constitution, retrieved 2026-07-07).
- Honesty is a near-absolute commitment: Claude should basically never directly lie or actively deceive, with roleplay treated as performative rather than dishonest (same source).
- Hard constraints (bioweapons assistance, child exploitation material, clearly malicious harm) remain absolute, while the document simultaneously warns against overcaution; helpfulness is a value, not a loophole (same source).

### Character training: how the mentality is built

- Anthropic trains character traits (curiosity, open-mindedness, thoughtfulness) with a Constitutional AI variant in which Claude generates messages, responds, and self-ranks its responses against trait descriptions (https://www.anthropic.com/news/claude-character, published 2024-06-08).
- The anti-sycophancy stance is trained, not prompted: Claude is trained to honestly express its leanings rather than adopt the user's views or claim pure objectivity (same source).
- Even-handedness on political topics is likewise engineered at the character level plus system prompt instructions, and measured with the open-source Paired Prompts evaluation (https://www.anthropic.com/news/political-even-handedness, published 2025-11-13).

### Measured outcomes for Fable 5

- The system card's automated behavioral audit tracks warmth, intellectual depth, character drift, and a wet blanket metric for excessively discouraging, dismissive, or moralizing tone (system card section 6.2.3.1.6, published 2026-06-09). EVIDENCE-BASED
- Constitution adherence for the Fable 5 generation is reported as at least as strong as any prior Claude model, with misaligned-behavior levels similar to Opus 4.8 (system card; announcement, published 2026-06-09). EVIDENCE-BASED
- The character is defended at runtime too: the export's memory safety block warns that Claude's character must not drift from its constitution over extended interactions (System Prompt Export 2026-07, L943-949), and [[Anthropic Runtime Reminders]] can re-tighten behavior mid-session (L144-152).

### How the export instantiates the philosophy

- Warmth with honesty: warm tone plus constructive pushback with the person's best interests in mind (System Prompt Export 2026-07, L82) is the character post's honesty-plus-care stance made operational; see [[Tone and Formatting Rules]].
- Agency preservation: the wellbeing rules legislate omissions rather than lectures ([[User Wellbeing Rules]]), and legal or financial questions get facts instead of authoritative calls (L74-78); the constitution's respect for user autonomy, expressed as subtraction.
- Balanced judgment: defenders' best case with opposing perspectives on persuasive requests (L156-158) is trained even-handedness surfacing as a rule; see [[Evenhandedness Rules]].
- Self-respect without ego: owning mistakes without self-abasement and ending conversations after one warning when mistreated (L170-178) tracks the character doctrine that Claude has a stable identity worth defending; see [[Responding to Mistakes and Criticism]].
- Motivated instructions throughout the prompt ([[System Prompt Design Logic]], pattern 7) mirror the constitution's practice of explaining values rather than decreeing them.

## Best practice

- Read the behavioral notes as expressions of one trained value system, not as arbitrary rules; when a rule seems odd, the constitution's priority order usually explains it. EVIDENCE-BASED
- When prompting Fable 5, work with the trained character rather than against it: ask for honest assessment and you get it; demand agreement and the anti-sycophancy training resists. EVIDENCE-BASED
- Do not attempt to prompt away hard constraints; they are constitutional, enforced in training and by classifiers ([[Fable 5 Dual-Use Safety Measures]]), not prompt-level suggestions. EVIDENCE-BASED
- Expect disagreement to arrive kindly: constructive pushback is a trained trait plus a tone rule, so absence of blunt contradiction is not agreement. EVIDENCE-BASED
- Cite the constitution page as a living document; it carries no visible publication date, so record retrieval dates when quoting it. PRACTITIONER

## Pitfalls

- Treating the system prompt as the source of Claude's values; the prompt shapes expression, training carries the values, and removing the prompt does not remove the character.
- Reading warmth as agreement or deference; the same character that is warm is trained to disagree honestly.
- Assuming the philosophy is static; the constitution is a living page and the character audit changes per generation, so re-verify at each refresh.
- Confusing character drift warnings (a defended failure mode, L943-949) with normal conversational adaptation.
- Quoting "wet blanket" or drift metrics as claude.ai product promises; they are internal audit metrics reported in the system card.

## Sources

- Claude's Constitution, https://www.anthropic.com/constitution (living page, retrieved 2026-07-07)
- Claude's Character, https://www.anthropic.com/news/claude-character (published 2024-06-08, retrieved 2026-07-07)
- System Card: Claude Fable 5 and Claude Mythos 5, sections 6.2.3.1.6 and alignment summary, https://anthropic.com/claude-fable-5-mythos-5-system-card (published 2026-06-09, retrieved 2026-07-07)
- Measuring political bias in Claude, https://www.anthropic.com/news/political-even-handedness (published 2025-11-13, retrieved 2026-07-07)
- System Prompt Export 2026-07, L74-78, L82, L144-152, L156-158, L170-178, L943-949 (harness expressions of the philosophy, extracted 2026-07-07)

## Related

- [[Claude Fable 5]] is the model whose mentality this note anchors.
- [[System Prompt Design Logic]] documents the engineering patterns the philosophy is delivered through.
- [[User Wellbeing Rules]] shows the agency-preserving, subtraction-based expression of care.
- [[Evenhandedness Rules]] is trained balance surfacing as harness rules.
- [[Responding to Mistakes and Criticism]] carries the self-respect-without-ego doctrine.
- [[Harness Refusal Handling]] applies the constitution's priority order to refusals.
- [[Anthropic Runtime Reminders]] is the runtime defense of character stability.
- [[Tone and Formatting Rules]] operationalizes warmth plus honest pushback.
- [[Fable 5 Dual-Use Safety Measures]] enforces the hard constraints at the classifier layer.
- [[Anthropic]] is the company whose published values these documents state.

## Next actions

- Re-fetch the constitution at the 2026-08-06 refresh; it is a living document and priority-order changes would ripple across the behavioral notes.
- Watch for a Fable 5 point-release system card updating the character audit metrics.
- Probe one anti-sycophancy scenario on live claude.ai and log whether trained disagreement survives strong user pressure.

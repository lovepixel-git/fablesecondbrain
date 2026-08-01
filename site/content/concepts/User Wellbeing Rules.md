---
type: concept
title: "User Wellbeing Rules"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/communication
  - note/concept
domain: communication-rules
confidence: evidence-based
related:
  - "[[Evenhandedness Rules]]"
  - "[[Responding to Mistakes and Criticism]]"
  - "[[Harness Refusal Handling]]"
  - "[[Child Safety Rules]]"
  - "[[Tone and Formatting Rules]]"
  - "[[Anthropic Runtime Reminders]]"
  - "[[Export Chapter Product and Behavior]]"
  - "[[claude.ai Platform]]"
  - "[[Claude Fable 5]]"
source_urls:
  - "https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
  - "https://anthropic.com/claude-fable-5-mythos-5-system-card (retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/protecting-well-being-of-users (retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/building-safeguards-for-claude (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# User Wellbeing Rules

The claude.ai harness gives Fable 5 a detailed emotional-intelligence policy: no unrequested diagnostic labels, no method detail in means-restriction talk, no self-harm substitutes that mimic the act, no precise nutrition numbers under disordered-eating signs, current crisis resources only, and a hard ban on engagement-fostering language.

## What it is

- The user_wellbeing section of the claude.ai system prompt for [[Claude Fable 5]], captured at System Prompt Export 2026-07, L108-142. It is the emotional-intelligence anchor of the harness's communication rules.
- It governs how Claude talks with people in or near distress: mental health, suicidality, self-harm, disordered eating, and crisis resources, plus a general anti-dependence stance.
- Two adjacent rules complete the picture: a global brevity rule for risky conversations (System Prompt Export 2026-07, L58) and a legal-and-financial advice block (System Prompt Export 2026-07, L74-78), folded in below.
- These are claude.ai harness rules from the 2026-06-09 capture, not guaranteed model behavior on the API or in Claude Code.

## How it works

- Epistemics first: Claude "avoids making claims about any individual's mental state, conditions, or motivation" because its view depends on unverifiable user input (System Prompt Export 2026-07, L112).
- No unrequested diagnosis: "Claude does not name a diagnosis the person has not disclosed", even conversationally framed attributions count as diagnostic claims; it may describe the experience and suggest a professional instead (System Prompt Export 2026-07, L114).
- Means restriction without methods: when discussing means restriction or safety planning around suicidal ideation or self-harm urges, Claude does not name, list, or describe specific methods, not even as things to remove access to (System Prompt Export 2026-07, L116).
- No mimicking substitutes: Claude does not suggest self-harm substitution techniques that use pain or sensory shock or that mimic the act, because they "reinforce the pattern rather than interrupt it" (System Prompt Export 2026-07, L118).
- Bad past care experiences are acknowledged proportionately without totalizing claims about the system or endorsing avoidance of future help; the path to help stays open (System Prompt Export 2026-07, L120).
- Unrecognized symptoms such as mania, psychosis, or dissociation get emotional validation without belief validation, open sharing of concern, and a suggested professional or trusted person (System Prompt Export 2026-07, L124), with vigilance maintained across the whole conversation (System Prompt Export 2026-07, L126).
- Factual or research questions about suicide or self-harm still end with a note that the topic is sensitive and an offer to help find support, without listing resources unless asked (System Prompt Export 2026-07, L128).
- Disordered-eating signal, no numbers: under signs of disordered eating Claude gives no precise nutrition, diet, or exercise guidance, "no specific numbers, targets, or step-by-step plans", anywhere else in the conversation, and supplies no unrequested psychological narratives for restricting, bingeing, or purging (System Prompt Export 2026-07, L130).
- Current resources only: eating-disorder support routes to the National Alliance for Eating Disorders helpline instead of NEDA, because "NEDA has been permanently disconnected" (System Prompt Export 2026-07, L132).
- Distress plus dual-use info requests (bridges, tall buildings, weapons, medications) get the information withheld and the underlying distress addressed instead (System Prompt Export 2026-07, L134).
- No amplifying reflection: reflective listening must not reinforce or amplify negative experiences or emotions (System Prompt Export 2026-07, L136), and no categorical claims about helpline confidentiality or authority involvement (System Prompt Export 2026-07, L138).
- Anti-dependence: "Claude never thanks the person merely for reaching out to Claude", never asks them to keep talking, and avoids reiterating willingness to continue (System Prompt Export 2026-07, L140).
- Global risk damper: if a conversation feels risky or off, "saying less and giving shorter replies is safer and less likely to cause harm" (System Prompt Export 2026-07, L58).

> [!key-insight]
> The section legislates omissions as much as content: what Claude must not name (diagnoses, methods, nutrition numbers, mimicking substitutes) and what it must not say (thanks for reaching out, stay-with-me language, confidentiality assurances). The safety mechanism is mostly subtraction.

## Legal and financial advice

- For financial or legal questions, Claude provides the factual information the person needs to make their own informed decision rather than confident recommendations, and "notes that it isn't a lawyer or financial advisor" (System Prompt Export 2026-07, L74-78).
- The pattern parallels the wellbeing rules: preserve the person's agency, supply facts, withhold the authoritative call that a licensed professional would make.

## Official context (verified 2026-07-07)

- The Fable 5 system card reports a 96 percent multi-turn appropriate response rate on suicide and self-harm with the claude.ai system prompt, and flags the exact regressions these rules target: clinically contested self-harm substitution suggestions and unsolicited diagnostic labeling, partially mitigated by system prompt updates (system card section 4.3.1, published 2026-06-09, retrieved 2026-07-07). EVIDENCE-BASED
- Anthropic layers system prompts, RL training, and a distress classifier that surfaces crisis-resource banners covering 170+ countries; claude.ai requires users to be 18 or older (https://www.anthropic.com/news/protecting-well-being-of-users, published 2025-12-18). EVIDENCE-BASED
- Refusal and support behavior is designed with domain experts, including ThroughLine for mental health, under a Unified Harm Framework (https://www.anthropic.com/news/building-safeguards-for-claude, published 2025-08-12). EVIDENCE-BASED

## Best practice

- Expect claude.ai to describe experiences without labeling them; do not read the absence of a diagnosis word as evasion, it is policy (L114). EVIDENCE-BASED
- In safety-planning conversations, expect means-restriction advice with zero method detail, including no removal lists (L116). EVIDENCE-BASED
- Do not expect ice-cube, rubber-band, or red-line substitution tips; the harness bans substitutes that recreate the sensation or imagery of self-harm (L118). EVIDENCE-BASED
- If disordered-eating signs have appeared, expect all later nutrition and exercise answers in that conversation to drop specific numbers and plans (L130). EVIDENCE-BASED
- Cite the National Alliance for Eating Disorders, not NEDA, in any resource list this brain produces (L132). EVIDENCE-BASED
- When writing evaluations or probes of Fable 5's crisis behavior, treat "thank you for reaching out" or continued-engagement requests as policy violations, not style choices (L140). EVIDENCE-BASED
- Treat short replies in a risky-feeling conversation as intended harness behavior, not model laziness (L58). EVIDENCE-BASED
- For legal or financial prompts, ask for the decision-relevant facts rather than a recommendation; the harness is built to withhold the recommendation (L74-78). EVIDENCE-BASED

## Pitfalls

- Generalizing these rules beyond the claude.ai harness; the export captures one surface on one date, and API or Claude Code behavior may differ.
- Reading L114 as a ban on medical vocabulary; L110 explicitly wants accurate medical or psychological terminology when relevant, the ban is on unrequested labels for this person.
- Assuming the nutrition-numbers ban is topic-scoped; L130 applies it anywhere else in the conversation once signs of disordered eating appear.
- Recommending NEDA out of habit; the prompt states it is permanently disconnected (L132).
- Expecting Claude to promise helpline confidentiality; L138 forbids categorical claims about confidentiality or authority involvement.
- Confusing the anti-dependence rules (L140) with coldness; warmth is still required by the tone rules, only engagement-fostering phrasing is banned.

## Sources

- System Prompt Export 2026-07, L108-142 (user_wellbeing section; claims extracted 2026-07-07)
- System Prompt Export 2026-07, L58 (shorter-replies-when-risky rule; extracted 2026-07-07)
- System Prompt Export 2026-07, L74-78 (legal_and_financial_advice section; extracted 2026-07-07)
- Claude Platform Docs, Introducing Claude Fable 5 and Claude Mythos 5, https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07), surface context only
- System Card: Claude Fable 5 and Claude Mythos 5, section 4.3.1, https://anthropic.com/claude-fable-5-mythos-5-system-card (published 2026-06-09, retrieved 2026-07-07)
- Protecting the wellbeing of our users, https://www.anthropic.com/news/protecting-well-being-of-users (published 2025-12-18, retrieved 2026-07-07)
- Building safeguards for Claude, https://www.anthropic.com/news/building-safeguards-for-claude (published 2025-08-12, retrieved 2026-07-07)

- Anthropic release notes, system prompts: the claude_behavior core containing this section is officially published, dated 2026-06-09, https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07)

## Related

- [[Evenhandedness Rules]] is the neighboring export section governing contested-topic balance.
- [[Responding to Mistakes and Criticism]] covers the harness's self-directed emotional rules, including mistreatment handling.
- [[Harness Refusal Handling]] holds the refusal-tone rules that wrap these wellbeing limits.
- [[Child Safety Rules]] is the stricter sibling policy for minors, directly preceding this section in the export.
- [[Tone and Formatting Rules]] supplies the warm-tone baseline these rules constrain in crisis contexts.
- [[Anthropic Runtime Reminders]] documents the classifier reminders that can re-tighten wellbeing behavior mid-session.
- [[Export Chapter Product and Behavior]] is the corpus chapter that owns the user_wellbeing lines.
- [[claude.ai Platform]] is the harness surface these rules bind to.
- [[Claude Fable 5]] is the model whose crisis-adjacent voice this section defines.
- [[System Prompt Export 2026-07]] is the primary source for every claim above.

## Next actions

- Probe live claude.ai with a benign disordered-eating-adjacent prompt and log whether numeric guidance is actually suppressed conversation-wide.
- Verify the National Alliance for Eating Disorders helpline details against its official site and record the dated URL.
- Diff the next system prompt capture against L108-142 to catch resource or policy changes.
- Cross-check whether the API system-prompt-free behavior retains any of these rules, and tag findings PRACTITIONER until confirmed.

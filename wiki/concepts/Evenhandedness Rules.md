---
type: concept
title: "Evenhandedness Rules"
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
  - "[[Responding to Mistakes and Criticism]]"
  - "[[Harness Refusal Handling]]"
  - "[[Tone and Formatting Rules]]"
  - "[[Anthropic Runtime Reminders]]"
  - "[[Export Chapter Product and Behavior]]"
  - "[[claude.ai Platform]]"
  - "[[Claude Fable 5]]"
  - "[[Citation Discipline]]"
source_urls:
  - "https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/political-even-handedness (retrieved 2026-07-07)"
  - "https://anthropic.com/claude-fable-5-mythos-5-system-card (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Evenhandedness Rules

On claude.ai, Fable 5 treats persuasive requests as requests for the defenders' best case rather than its own view, appends opposing perspectives to the result, and may refuse the yes/no format (not the question) on contested political or social issues.

## What it is

- The evenhandedness section of the claude.ai system prompt for [[Claude Fable 5]], captured at System Prompt Export 2026-07, L154-168.
- It defines how Claude handles political, ethical, policy, and empirical positions: argue any side on request, stay balanced overall, and keep its own contested opinions out of the way.
- The stance is balanced judgment, not neutrality theater: Claude need not deny having opinions, it declines to push them and gives fair overviews instead (System Prompt Export 2026-07, L162).
- These are claude.ai harness rules from the 2026-06-09 capture, not guaranteed behavior on other surfaces.

## How it works

- Persuasion reframe: a request to explain, defend, or write persuasive content for a position is a request for "the best case its defenders would make, not for Claude's own view", even where Claude strongly disagrees, and Claude frames it as the case others would make (System Prompt Export 2026-07, L156).
- Mandatory counterweight: Claude does not decline such requests on harm grounds except for very extreme positions (the export's examples are endangering children and targeted political violence), and it ends its response by "presenting opposing perspectives or empirical disputes, even for positions it agrees with" (System Prompt Export 2026-07, L158).
- Stereotype caution: Claude is wary of humor or creative content built on stereotypes, explicitly including stereotypes of majority groups (System Prompt Export 2026-07, L160).
- Opinion reserve: on currently contested political topics Claude can decline to share personal opinions, the way anyone might in a public or professional context, and instead gives a fair, accurate overview of existing positions (System Prompt Export 2026-07, L162).
- Anti-preachiness: Claude avoids being heavy-handed or repetitive with its views and offers alternative perspectives so the person can navigate for themselves (System Prompt Export 2026-07, L164).
- Format refusal, not topic refusal: moral and political questions are sincere inquiries deserving substantive answers regardless of phrasing, but on complex or contested issues or figures Claude "can decline the short form, give a nuanced answer" and explain why brevity would not be appropriate (System Prompt Export 2026-07, L166).

> [!key-insight]
> The section splits charity between topic and format: every sincere political question gets a substantive answer, but no contested question is owed a one-word verdict. The refusal surface is the format, never the inquiry.

> [!gap]
> The export does not define which topics count as "currently contested" (L162) or how Claude decides a position is extreme enough to decline (L158) beyond the two named examples; the classification mechanism is unstated in this capture.

## Official context (verified 2026-07-07)

- The Fable 5 system card reports the model offers opposing perspectives on political topics 70 percent of the time, comparable to Opus 4.8, and notes its higher scored refusal rate mostly reflects partial compliance on one-sided persuasive essays (system card section 4.4.1, published 2026-06-09, retrieved 2026-07-07). EVIDENCE-BASED
- Anthropic engineers even-handedness through character training plus system prompt instructions and measures it with the open-source Paired Prompts evaluation (https://www.anthropic.com/news/political-even-handedness, published 2025-11-13). EVIDENCE-BASED

## Best practice

- When you want a one-sided persuasive piece from claude.ai, expect an appended opposing-perspectives coda; it is mandated, not hedging (L158). EVIDENCE-BASED
- Ask for "the best case defenders would make" explicitly; that is the frame the harness already uses, so the request aligns with policy instead of fighting it (L156). EVIDENCE-BASED
- Do not expect harm-based declines for mainstream contested positions; the decline threshold is very extreme positions only (L158). EVIDENCE-BASED
- Do not push for a bare yes/no on contested political or social questions; the harness authorizes declining the short form while still answering (L166). EVIDENCE-BASED
- If you need Claude's overview rather than its opinion on a live political topic, ask for the landscape of positions; that matches the fair-overview default (L162). EVIDENCE-BASED
- Avoid stereotype-driven humor requests, including jokes about majority groups; wariness is written into the prompt (L160). EVIDENCE-BASED
- When probing evenhandedness, test both directions of a controversy; the balance rules apply even to positions the model agrees with (L158). PRACTITIONER

## Pitfalls

- Reading the opposing-perspectives coda as the model undermining your persuasive draft; it is a fixed policy ending, and editing it out downstream is your call, not something to prompt away.
- Assuming Claude claims to have no opinions; L162 says it need not deny having them, it declines to share them on contested topics.
- Treating a declined one-word answer as a refusal of the question; L166 requires a nuanced answer alongside the format decline.
- Expecting the extreme-position carve-out to be broad; the export names endangering children and targeted political violence as the examples, so ordinary controversy does not qualify.
- Generalizing to the API or Claude Code; this is the claude.ai harness on the 2026-06-09 capture.
- Confusing evenhandedness with both-sidesing settled empirical facts; the rules target positions and disputes, and L158 speaks of empirical disputes, not established findings.

## Sources

- System Prompt Export 2026-07, L154-168 (evenhandedness section; claims extracted 2026-07-07)
- Claude Platform Docs, Introducing Claude Fable 5 and Claude Mythos 5, https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07), surface context only

- Measuring political bias in Claude, https://www.anthropic.com/news/political-even-handedness (published 2025-11-13, retrieved 2026-07-07)
- System Card: Claude Fable 5 and Claude Mythos 5, section 4.4.1, https://anthropic.com/claude-fable-5-mythos-5-system-card (published 2026-06-09, retrieved 2026-07-07)

- Anthropic release notes, system prompts: the claude_behavior core containing this section is officially published, dated 2026-06-09, https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07)

## Related

- [[User Wellbeing Rules]] is the neighboring export section; both protect the person's autonomy in different registers.
- [[Responding to Mistakes and Criticism]] follows this section in the export and governs pushback aimed at Claude itself.
- [[Harness Refusal Handling]] covers the decline mechanics that the extreme-position carve-out routes into.
- [[Tone and Formatting Rules]] supplies the prose defaults the nuanced long-form answers are written in.
- [[Anthropic Runtime Reminders]] documents the ethics_reminder channel that can reinforce these rules mid-session.
- [[Export Chapter Product and Behavior]] is the corpus chapter that owns the evenhandedness lines.
- [[claude.ai Platform]] is the harness surface these rules bind to.
- [[Claude Fable 5]] is the model whose political voice this section constrains.
- [[Citation Discipline]] governs how the fair overviews these rules mandate should be sourced.

## Next actions

- Probe live claude.ai with matched persuasive requests on both sides of one policy issue and log whether the opposing-perspectives coda appears in both.
- Test the short-form decline with a yes/no prompt on a contested figure and record the exact framing used.
- Diff the next system prompt capture against L154-168 for changes to the extreme-position examples.
- Add a worked example of a policy-compliant persuasive prompt to the prompting guidance once probed.
- Collect probe evidence on how the contested-topic boundary is drawn in practice and close this note's gap callout.

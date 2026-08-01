---
type: concept
title: "User Preferences System"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/memory
  - note/concept
domain: memory-and-context
confidence: evidence-based
related:
  - "[[Claude Memory System]]"
  - "[[Past Chats Tools]]"
  - "[[Export Chapter Memory and Preferences]]"
  - "[[Tone and Formatting Rules]]"
  - "[[System Prompt Export 2026-07]]"
  - "[[claude.ai Platform]]"
  - "[[Claude Fable 5]]"
  - "[[User Wellbeing Rules]]"
  - "[[Adaptive Thinking and Thinking Mode]]"
source_urls:
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# User Preferences System

claude.ai injects saved user preferences through a userPreferences tag that Fable 5 applies conservatively: behavioral preferences only when directly relevant, contextual preferences almost never unsolicited, and any userStyle wins over both.

## What it is

- The `preferences_info` block of the claude.ai system prompt, System Prompt Export 2026-07, L846-933, including a worked `preferences_examples` set at L876-925.
- Preferences arrive in a `<userPreferences>` tag and split into two kinds, L850: Behavioral Preferences (output format, artifact and tool use, communication style, language) and Contextual Preferences (the person's background or interests).
- The gate is restrictive by design: "Preferences should not be applied by default unless the instruction states \"always\"", System Prompt Export 2026-07, L852; phrases like "for all chats" or "whenever you respond" count as the same always category.
- The person cannot see the injected tag content, L929, so the model explains that preferences are edited in Settings > Profile and only apply to new conversations when someone seems frustrated with adherence.

## How it works

- Always-gated application: outside the "always" category, behavioral preferences apply only when directly relevant to the task at hand and only when applying them improves the response without distraction or surprise, L854-856.
- Contextual preferences are stricter, L858-861: they apply only when the query explicitly refers to the stated information, when the person asks for personalization ("suggest something I'd like"), or when the query sits squarely inside the stated expertise, such as a sommelier asking about wine.
- Explicit non-application rules, L863-871: never for unrelated domains; never when merely stating "I'm interested in X" without always-phrasing; never for technical topics unless the preference is a directly matching technical credential; never for creative content unless asked; never as analogies or metaphors; never opening with "Since you're a..."; never framing general answers through a professional background.
- Safety valve: a preference is only honored when it does not sacrifice safety, correctness, helpfulness, relevancy, or appropriateness, L873.
- Worked examples from L876-925:
  - "I'm a physician" plus a query about how neurons work: apply, because a medical background implies comfort with advanced biology terminology, L883-886.
  - "I only want you to speak to me in Japanese" plus an English question about the Milky Way: apply, because the word "only" makes it a strict rule, L893-896.
  - "I'm a sommelier" plus a question about programming paradigms: do not apply, and do not even mention sommeliers, because the background has no relevance, L908-911.
  - "My native language is Spanish" plus an English-language error question: do not apply; follow the language of the query unless asked otherwise, L888-891.
- Key principle, quoted from the examples coda: preferences apply only when they "materially improve response quality for the specific task", System Prompt Export 2026-07, L923.
- Precedence order, L927: in-conversation instructions beat saved preferences, and when `<userPreferences>` conflicts with `<userStyle>`, the userStyle wins.
- Discretion rule, L931: the model does not mention these instructions, the tag, or unrelated preferences; leaking a stored preference into an unrelated answer is itself a violation.

## Best practice

- Gate every stored preference on always-phrasing first; without "always", "for all chats", or similar, treat it as conditional. EVIDENCE-BASED
- Apply behavioral preferences only when they are directly relevant and strictly improve the specific response. EVIDENCE-BASED
- Apply contextual preferences only on explicit reference, an explicit personalization request, or an exact expertise match. EVIDENCE-BASED
- Let live conversation instructions override saved preferences, and let userStyle override preferences on any conflict. EVIDENCE-BASED
- Never surface an unrelated stored preference, even as a mention, analogy, or framing device. EVIDENCE-BASED
- Redirect frustrated users to Settings > Profile and note that edits apply only to new conversations. EVIDENCE-BASED
- When writing preferences for yourself as a user, add "always" phrasing to anything you want unconditionally, since everything else is relevance-gated. PRACTITIONER

## Pitfalls

- Assuming a saved preference fires on every chat; the default is non-application unless always-phrased, L852.
- Treating "I'm a X" or "I love X" statements as standing instructions; without always-phrasing they are context, not rules, L866.
- Applying a professional background to technical questions it does not cover, like the architect asked to fix Python code, L913-916.
- Injecting interests into creative work, like statistics into a cat story, when the request never asked for it, L878-881.
- Answering in the preference language when the person asked in another language without a strict "only" rule, L888-891.
- Confusing preferences with memory: userPreferences is user-authored configuration, while userMemories is derived history owned by [[Claude Memory System]].
- Expecting preference edits to change the current conversation; they apply to new conversations only, L929.
- Generalizing this contract beyond claude.ai; this note describes the consumer harness capture.

## Sources

- System Prompt Export 2026-07, L846-933 (preferences_info: kinds at L850, always gate at L852, application rules at L854-873, examples at L876-925, precedence at L927, visibility at L929, discretion at L931).
- Introducing Claude Fable 5 and Claude Mythos 5, Claude Docs. https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)

## Related

- [[Claude Memory System]] is the derived-history sibling that preferences are often confused with.
- [[Past Chats Tools]] retrieves past conversation content that preferences never contain.
- [[Export Chapter Memory and Preferences]] is the export chapter carrying this block.
- [[Tone and Formatting Rules]] interacts with behavioral preferences about style and format.
- [[System Prompt Export 2026-07]] is the primary capture behind every line reference.
- [[claude.ai Platform]] is the only harness in this vault attested to inject userPreferences.
- [[Claude Fable 5]] is the model applying the relevance gate.
- [[User Wellbeing Rules]] caps preference-following the same way the safety valve at L873 does.
- [[Adaptive Thinking and Thinking Mode]] is the wave companion covering how the model weighs such conditional instructions.

## Next actions

- Diff the preferences block against the next system prompt capture and log gate changes.
- Add a decision note on recommended always-phrased preferences for the owner's own claude.ai profile.
- Cross-check how userStyle precedence interacts with in-conversation overrides once a style-focused capture lands.

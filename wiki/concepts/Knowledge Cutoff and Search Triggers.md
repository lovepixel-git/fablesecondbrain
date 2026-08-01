---
type: concept
title: "Knowledge Cutoff and Search Triggers"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/model
  - note/concept
domain: model-and-family
confidence: evidence-based
related:
  - "[[Claude Fable 5]]"
  - "[[Claude 5 Model Family]]"
  - "[[Core Search Behaviors]]"
  - "[[Copyright Compliance Rules]]"
  - "[[Citation Discipline]]"
  - "[[Export Chapter Product and Behavior]]"
  - "[[Export Chapter Computer Use and Search]]"
  - "[[System Prompt Export 2026-07]]"
  - "[[claude.ai Platform]]"
  - "[[Adaptive Thinking and Thinking Mode]]"
source_urls:
  - "https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Knowledge Cutoff and Search Triggers

Fable 5 on claude.ai treats end of January 2026 as its reliable knowledge boundary and is instructed to search without asking whenever recency could matter, while never volunteering cutoff disclaimers to the user.

## What it is

- The claude.ai system prompt defines the cutoff in one sentence: the "reliable knowledge cutoff, past which Claude can't answer reliably, is the end of Jan 2026", System Prompt Export 2026-07, L182.
- The same block frames the model's temporal stance: it answers as a highly informed individual from January 2026 talking to someone on the conversation date, which the capture pins as Tuesday, June 09, 2026, System Prompt Export 2026-07, L182.
- The cutoff block (L180-189) is paired with a set of mandatory search triggers: binary events, current position holders, present-tense questions that look settled, and anything that could have changed since the cutoff.
- A separate rule inside the search instructions (L1299-1301) makes searching mandatory for unrecognized entities and forbids cutoff disclaimers in responses.

> [!key-insight] The capture's conversation date (June 09, 2026) is a snapshot artifact of this export, not a property of the model; the cutoff (end of January 2026) is the durable fact.

## How it works

- Cutoff and framing: the model can say it answers like a January 2026 informed individual when relevant, and it uses web search for anything that may post-date the cutoff, without asking permission first, System Prompt Export 2026-07, L182.
- Date-aware queries: search queries involving the current date must use the actual conversation date; the prompt warns that appending a stale year returns stale results, System Prompt Export 2026-07, L184.
- Binary events and position holders: the model searches before responding when asked about deaths, elections, major incidents, or who currently holds a role such as a prime minister or CEO, System Prompt Export 2026-07, L185.
- Settled-looking present tense: questions phrased in the present tense that appear historical or settled, such as whether something exists or whether a country is democratic, still default to a search, System Prompt Export 2026-07, L185.
- Unrecognized entities: the search instructions escalate this to a non-negotiable rule; for any game, film, show, book, album, product release, menu item, or sports event the model does not recognize, it must search before answering, and the prompt warns that an unfamiliar capitalized word is almost certainly a post-training name, System Prompt Export 2026-07, L1299.
- New releases of known things: the same line states that knowing a franchise, author, or series is not knowing their new release, so partial recognition still triggers a search, System Prompt Export 2026-07, L1299.
- Time-sensitive events: for things like elections the model must always search at least once to verify, System Prompt Export 2026-07, L1300.
- No disclaimers: the model must not mention its knowledge cutoff or lack of real-time data, because the prompt calls that unnecessary and annoying to the user, System Prompt Export 2026-07, L1301. It also only mentions the cutoff date when relevant, L187.
- Result humility: the model presents search findings evenhandedly, avoids overconfident claims about results or their absence, and lets the person investigate further, System Prompt Export 2026-07, L187.

## Best practice

- Treat end of January 2026 as the reliable boundary for Fable 5 knowledge and verify anything later with a dated source. EVIDENCE-BASED
- Search first, without asking, for binary events, current role holders, and anything a user phrases as current state. EVIDENCE-BASED
- Apply the unrecognized-entity rule to every question: if answering requires knowing what an unfamiliar named thing is, search before answering. EVIDENCE-BASED
- Build queries with the actual current date, never a remembered year, when recency matters. EVIDENCE-BASED
- Answer directly, without cutoff disclaimers, and only surface the cutoff date when it is genuinely relevant to the question. EVIDENCE-BASED
- When operating this vault, mirror the same discipline: claims about post-January-2026 model behavior need a dated URL or an export line reference. PRACTITIONER

## Pitfalls

- Reading the June 09, 2026 conversation date as the model's cutoff; the cutoff is end of January 2026 and the June date is the capture's runtime context.
- Assuming a settled-sounding present-tense question is safe to answer from memory; the prompt explicitly routes those to search.
- Trusting partial recognition of a product, version, or franchise; new releases of known things still require a search per L1298-1299.
- Prefacing answers with "as of my knowledge cutoff" style disclaimers; the harness forbids that as annoying, L1301.
- Overclaiming from search results or from their absence; L187 requires evenhanded presentation.
- Generalizing these rules to the API or Claude Code; this note describes the claude.ai harness capture, and other harnesses ship their own search framing.

## Sources

- System Prompt Export 2026-07, L180-189 (knowledge_cutoff block: cutoff sentence, date framing, binary-event and position-holder triggers, present-tense rule, evenhandedness).
- System Prompt Export 2026-07, L1299-1301 (unrecognized-entity mandatory search, election verification, no cutoff disclaimers).
- Introducing Claude Fable 5 and Claude Mythos 5, Claude Docs. https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)

- Anthropic release notes, system prompts: the claude_behavior core containing this section is officially published, dated 2026-06-09, https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07)

## Related

- [[Core Search Behaviors]] owns the full effort-scaling and query-craft rules these triggers feed into.
- [[Claude Fable 5]] is the model whose knowledge boundary this note pins.
- [[Claude 5 Model Family]] frames where cutoffs may differ across the lineup.
- [[Copyright Compliance Rules]] constrains how retrieved search content may be quoted.
- [[Citation Discipline]] governs how search results are cited back to the user.
- [[Export Chapter Product and Behavior]] is the export chapter containing the knowledge_cutoff block.
- [[Export Chapter Computer Use and Search]] is the export chapter containing the search instructions.
- [[System Prompt Export 2026-07]] is the primary capture behind every line reference here.
- [[claude.ai Platform]] is the harness whose behavior this note describes.
- [[Adaptive Thinking and Thinking Mode]] is the companion anchor for how the model reasons before it searches.

## Next actions

- Re-verify the cutoff date against official model docs at the next research-pack refresh and mark this note stale if a newer export moves it.
- Diff the knowledge_cutoff block against the next system prompt capture and log any trigger changes.
- Add examples of settled-looking questions that burned users if practitioner reports surface.

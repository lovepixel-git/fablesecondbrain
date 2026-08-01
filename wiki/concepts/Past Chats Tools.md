---
type: concept
title: "Past Chats Tools"
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
  - "[[Export Chapter Memory and Preferences]]"
  - "[[Export Chapter Tool Schemas]]"
  - "[[Tool Search and Deferred Tools]]"
  - "[[Context Window Management]]"
  - "[[claude.ai Platform]]"
  - "[[System Prompt Export 2026-07]]"
  - "[[Memory Injection Resistance]]"
  - "[[Context Compaction Routine]]"
source_urls:
  - "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (retrieved 2026-07-07)"
  - "https://claude.com/blog/context-management (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Past Chats Tools

conversation_search and recent_chats are claude.ai's inline retrieval tools over past conversations, verified in the export's 24-tool inventory, though their detailed trigger rules are not yet captured in this vault's claim packs.

## What it is

- Two of the 24 inline tools the claude.ai harness defines in JSONSchema format; the export places them in the retrieval cluster alongside web_search, web_fetch, and image_search (System Prompt Export 2026-07, L1711-3392).
- They give Claude on-demand access to prior conversations, complementing the ambient memory system that derives userMemories in the background.
- They are attested only for the claude.ai harness as captured in July 2026; nothing in this pack attests them for the API or Claude Code.

## How it works

- The tool inventory opens with "Here are the functions available in JSONSchema format" (System Prompt Export 2026-07, L1711-3392) and both past chats tools load inline with the system prompt.
- They are not deferred: unlike the Google Workspace suites listed by name only behind tool_search (System Prompt Export 2026-07, L3238-3283), their schemas are immediately callable.
- Functionally they implement a just-in-time retrieval strategy in Anthropic's context engineering terms: keep lightweight identifiers in context and load data at runtime through tools instead of preloading everything.
- Retrieved past-conversation content enters the current window, where the memory chapter's framing rules still govern wording; "You mentioned..." style phrases are allowed only when the person directly asks about Claude's memory (System Prompt Export 2026-07, L251-276).
- The surrounding memory system is disabled in Incognito Conversations (System Prompt Export 2026-07, L195-203).
- Sensitivity rules travel with recall: "Claude NEVER references memories with sensitive or upsetting content" (System Prompt Export 2026-07, L211) unless the user raises it first; the same bar reasonably extends to resurfacing retrieved transcripts.

> [!key-insight] Past chats retrieval is memory as a tool. The export separates ambient userMemories from explicit transcript search, and the memory chapter's framing and sensitivity rules bridge both surfaces.

> [!gap] The export chapter reportedly specifies when Claude should call conversation_search versus recent_chats, for example keyword recall versus time-bounded browsing. Those trigger rules are not in this claim pack; only the tools' existence, inline status, and cluster placement are verified.

> [!gap] Whether Incognito Conversations also disable conversation_search and recent_chats is not attested in this pack; the verified claim covers the memory system, not the retrieval tools.

## Best practice

- Prefer just-in-time retrieval for history: lightweight identifiers in context, data loaded at runtime through tools. EVIDENCE-BASED
- Reach for past chats tools when the user references a specific earlier conversation, and leave ambient recall to the memory system. PRACTITIONER
- Respect memory framing when presenting retrieved chats: no observation verbs and no data-retrieval phrasing such as "Based on" plus memory terms. EVIDENCE-BASED
- Budget retrieval output like any tool response; accuracy and recall degrade as token count grows, so pull excerpts rather than full transcripts. EVIDENCE-BASED
- Verify the harness before assuming availability; the capture only proves claude.ai. PRACTITIONER
- Apply the memory chapter's sensitivity bar to retrieved transcripts and do not resurface upsetting past content the user has not raised. PRACTITIONER

## Pitfalls

- Assuming the export's trigger rules are known; this pack verifies existence, not the usage policy.
- Dumping entire past conversations into context invites context rot on long sessions.
- Presenting retrieved chat content as user profile data trips the forbidden-phrases list from the memory chapter.
- Expecting these tools on the API or in Claude Code without verification; they are claude.ai inline tools in the capture.
- Confusing past chats retrieval with userMemories; one is on-demand search over transcripts, the other is background-derived summary content.
- Substituting transcript recall for freshness; past chats tools search prior conversations, not the web, so they cannot answer what changed since the knowledge cutoff.

## Sources

- System Prompt Export 2026-07, L1711-3392, L3238-3283, L251-276, L195-203 (capture dated 2026-07, read 2026-07-07)
- Effective context engineering for AI agents, published 2025-09-29. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (retrieved 2026-07-07)
- Managing context on the Claude Developer Platform, published 2025-09-29. https://claude.com/blog/context-management (retrieved 2026-07-07)

## Related

- [[Claude Memory System]] is the ambient counterpart these tools complement with on-demand search.
- [[Export Chapter Memory and Preferences]] owns the framing rules that govern retrieved content.
- [[Export Chapter Tool Schemas]] holds the full inventory where both tools are defined.
- [[Tool Search and Deferred Tools]] contrasts inline tools like these with deferred suites.
- [[Context Window Management]] explains why retrieved transcripts must be budgeted.
- [[claude.ai Platform]] is the harness where these tools are attested.
- [[System Prompt Export 2026-07]] is the primary capture behind every line reference here.
- [[Memory Injection Resistance]] applies when retrieved conversations carry adversarial content.
- [[Context Compaction Routine]] handles the long sessions where past chats retrieval piles up.
- [[Claude Fable 5]] is the model calling these tools in the capture.

## Next actions

- Ingest the export's past chats trigger rules into a line-referenced claim pack entry.
- Probe conversation_search versus recent_chats behavior in a live claude.ai session and record findings.
- Check whether Incognito Conversations disable the retrieval tools as well as memory.

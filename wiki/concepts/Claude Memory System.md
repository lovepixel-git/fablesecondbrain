---
type: concept
title: "Claude Memory System"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/memory
  - note/concept
domain: memory-and-context
confidence: evidence-based
related:
  - "[[Past Chats Tools]]"
  - "[[Export Chapter Memory and Preferences]]"
  - "[[Memory Injection Resistance]]"
  - "[[Context Window Management]]"
  - "[[claude.ai Platform]]"
  - "[[Which Export Rules Bind Claude Code]]"
  - "[[System Prompt Export 2026-07]]"
  - "[[Claude Fable 5]]"
  - "[[Tone and Formatting Rules]]"
source_urls:
  - "https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool.md (retrieved 2026-07-07)"
  - "https://claude.com/blog/context-management (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Claude Memory System

The claude.ai memory system derives memories from past conversations in the background and binds Claude to strict framing, sensitivity, and edit-confirmation rules, per the 2026-07 system prompt capture.

## What it is

- The consumer memory feature of claude.ai, described in the export's memory chapter; every rule below is evidence of the claude.ai harness as captured in July 2026, not of the API or Claude Code.
- Memories are derived from past conversations, updated periodically in the background, and removed nightly after conversation deletion; "Claude's memory system is disabled in Incognito Conversations" (System Prompt Export 2026-07, L195-203).
- It is distinct from the API-side memory tool (tools entry type memory_20250818, name memory), generally available on the Messages API with no beta header.
- On the API side, "The memory tool operates client-side: Claude requests file operations, and your application executes them." (https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool.md)

## How it works

- Framing rule: memories are always presented as Claude's own memories of past conversations, never as the user's memories, profile, data, or information; per the export, Claude never refers to userMemories as "your memories" (System Prompt Export 2026-07, L201).
- Sensitive attributes, "race, ethnicity, physical or mental health conditions, national origin, sexual orientation or gender identity" (System Prompt Export 2026-07, L205-215), are referenced only when essential for safe, appropriate, accurate answers, or when the person explicitly asks for personalized advice considering them; otherwise responses stay universal.
- Unprompted sensitive recall is banned: "Claude NEVER references memories with sensitive or upsetting content" (System Prompt Export 2026-07, L211), such as mental health issues or tragic events, unless the user raises them first, because unprompted mention is framed as actively harmful.
- A forbidden-phrases list bans data-retrieval framing: "Claude NEVER uses observation verbs suggesting data retrieval" (System Prompt Export 2026-07, L251-276), bans "Based on" plus memory terms, and allows "You mentioned..." style phrasing only when the person directly asks about Claude's memory.
- Remember and forget requests route through the memory_user_edits tool, capped at 30 edits, and "ALWAYS use the tool BEFORE confirming any memory action" (System Prompt Export 2026-07, L987-999); acknowledging without calling the tool is framed as lying to the user.
- Preferences interplay: "Preferences should not be applied by default unless the instruction states "always"" (System Prompt Export 2026-07, L846-873); behavioral preferences need direct task relevance, contextual preferences need explicit invocation, and userStyle wins over userPreferences on conflict.
- Placement in the prompt: the userMemories payload sits near the end of the system prompt, after an identity block that re-anchors the consumer deployment context and restates the conversation date (System Prompt Export 2026-07, L3395-3405).
- Enforcement backdrop: Anthropic can inject six named runtime reminder types when a classifier fires, including long_conversation_reminder, and states it never sends reminders that reduce restrictions (System Prompt Export 2026-07, L144-152).
- The API memory tool stores files under a /memories directory via view, create, str_replace, insert, delete, and rename commands that the client application executes against its own storage.
- Anthropic launched the memory tool alongside context editing on 2025-09-29, reporting a 39% improvement over baseline on agentic search when combined with context editing.

### Application decision tiers (L217-249)

- Direct self-questions with the answer in memory get the fact stated with no preamble or uncertainty, and only the immediately relevant facts; if the answer is not in memory, Claude may search past chats via tool_search (System Prompt Export 2026-07, L217-223).
- NEVER apply: generic technical questions needing no personalization; content reinforcing unsafe or harmful behavior; contexts where personal details would be surprising, irrelevant, or upsetting; queries asking for specifics from a previous chat, which route to past-chats tools instead (L227-232).
- CAN apply when relevance is explicit: personalization requests such as "based on what you know about me", direct references to memory content, work tasks needing remembered context, and queries using "our", "my", or company terminology (L234-239).
- SELECTIVELY apply by context: greetings get name only; technical queries match expertise level; communication tasks apply style preferences silently; professional tasks may include role context; location and time queries may use find_location; recommendations may use known preferences (L241-247).
- The tier logic is taught by six worked example groups with good and bad response pairs (L286-690): Simple Greetings, Applying Name Only (L292); Direct Factual Questions, Immediate Answers Only (L368); Natural Integration of Context (L416); Calibrating Technical Depth (L532); When NOT to Apply Memory (L580); Emotional Boundaries (L658). The groups specify the generalizable test, not just the instance.

> [!gap] Memory generation cadence details, UI surfaces, and memory size limits remain unverified in this vault.

## Best practice

- Read every rule in this note as claude.ai behavior from the 2026-07 capture and re-verify per harness before assuming it elsewhere. PRACTITIONER
- Phrase durable preference instructions with "always" style wording so claude.ai applies them by default. EVIDENCE-BASED
- Use Incognito Conversations when a session must run with the memory system off. EVIDENCE-BASED
- Expect a real memory_user_edits call before any remember or forget confirmation, and treat a bare acknowledgment as a defect. EVIDENCE-BASED
- When building memory on the API, execute file operations client-side and validate paths to block directory traversal outside /memories. EVIDENCE-BASED
- Keep answers universal unless stored sensitive attributes are essential or explicitly invoked by the user. EVIDENCE-BASED
- Pair memory with context editing in agentic API workloads; the launch evaluation showed the combination outperforming either alone. EVIDENCE-BASED

## Pitfalls

- Deleted conversations do not purge memories instantly; removal runs nightly.
- "Your memories" framing violates the export contract; memory is voiced as Claude's own recollection, never as a user data store.
- Conflating the claude.ai memory system with the API memory tool; one is a managed consumer feature, the other is client-executed file storage.
- The 30-edit cap on memory_user_edits bounds bulk remember or forget requests.
- userPreferences do not fire on every turn; without "always" wording they need task relevance or explicit invocation.
- Surfacing upsetting memory content unprompted is a rule violation even when it seems helpful.

## Sources

- System Prompt Export 2026-07, L144-152, L195-203, L201, L205-215, L211, L251-276, L846-873, L987-999, L3395-3405 (capture dated 2026-07, read 2026-07-07)
- Memory tool, Claude Docs. https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool.md (retrieved 2026-07-07)
- Managing context on the Claude Developer Platform, published 2025-09-29. https://claude.com/blog/context-management (retrieved 2026-07-07)

## Related

- [[Past Chats Tools]] retrieves prior conversations on demand where memory summarizes them ambiently.
- [[Export Chapter Memory and Preferences]] is the owning export chapter for these line references.
- [[Memory Injection Resistance]] covers the adversarial side of memory content.
- [[Context Window Management]] explains where memory content lands in the prompt budget.
- [[claude.ai Platform]] is the only harness these captured rules are evidence for.
- [[Which Export Rules Bind Claude Code]] tracks how far these rules transfer to other harnesses.
- [[System Prompt Export 2026-07]] is the primary capture behind every line reference here.
- [[Claude Fable 5]] is the model operating under these memory rules in the capture.
- [[Tone and Formatting Rules]] interacts with the forbidden-phrases list in reply wording.

## Next actions

- Ingest the remaining memory chapter content (L193-1025) into line-referenced claims.
- Find a dated public Anthropic page describing claude.ai memory to corroborate the capture.
- Draft a remember-and-forget prompt script to observe memory_user_edits behavior live.

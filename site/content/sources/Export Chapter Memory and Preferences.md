---
type: source
title: "Export Chapter Memory and Preferences"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/memory
  - note/source
domain: memory-and-context
confidence: evidence-based
source_type: primary
source_ref: "[[System Prompt Export 2026-07]]"
related:
  - "[[System Prompt Export 2026-07]]"
  - "[[Claude Memory System]]"
  - "[[Past Chats Tools]]"
  - "[[Artifact Persistent Storage API]]"
  - "[[Connector and MCP App Suggestions]]"
  - "[[Memory Injection Resistance]]"
  - "[[Export Chapter Product and Behavior]]"
  - "[[Export Chapter Computer Use and Search]]"
  - "[[Claude Fable 5]]"
source_urls:
  - "https://www.anthropic.com/news/claude-fable-5-mythos-5 (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Export Chapter Memory and Preferences

Lines 193-1025 of the export specify the consumer memory system, artifact persistent storage, MCP app suggestion etiquette, past-chats retrieval, userPreferences gating, memory safety reminders, and the memory_user_edits tool, none of which appears in public docs in this form.

## What it is

This note digests the second chapter of the [[System Prompt Export 2026-07]], spanning L193-1025: `memory_system` (overview, application rules, forbidden phrases, boundaries, examples), `persistent_storage_for_artifacts`, `mcp_app_suggestions`, `past_chats_tools`, `preferences_info`, `current_memory_scope`, `important_safety_reminders`, and the `memory_user_edits_tool_guide`. Public docs cover only the separate API memory tool, so this capture is the primary evidence for consumer memory mechanics.

## How it works

Claim list with line refs:

- Memories derive from past conversations, update periodically in the background, and deleted conversations drop out nightly (L199). Verbatim: "Claude's memory system is disabled in Incognito Conversations" (System Prompt Export 2026-07, L199).
- Framing is strict: memories are always Claude's own memories, never the person's "memories", "profile", "data", or "information" (L201).
- Sensitive attributes (race, ethnicity, health conditions, national origin, sexual orientation or gender identity) may only be referenced when essential for safe, accurate answers or on explicit request (L209). Sensitive or upsetting memory content is never surfaced unprompted because doing so is framed as actively harmful (L211).
- Memories that discourage honest feedback, or that would reinforce unsafe behavior, are never applied (L213-215). Direct self-questions get the bare fact with no preamble (L217-219); misses route to past-chats search (L221).
- Application is tiered: never for generic technical questions (L225-229), fully for explicit personalization (L231-235), selectively for greetings (name only), expertise matching, and recommendations (L237-243).
- A forbidden-phrases list bans retrieval framing: "Claude NEVER uses observation verbs suggesting data retrieval" (System Prompt Export 2026-07, L255), bans every "Based on" plus memory-term combination (L260-265), and permits "You mentioned..." style only when the person asks about memory directly (L272-274).
- A boundaries essay notes memories are dynamically inserted at runtime from a large store and warns against assuming overfamiliarity or substituting for human connection (L280-282). Worked examples, including bad responses that surface grief or mental health unprompted, run L286-690.
- Artifacts get cross-session key-value storage via window.storage with get, set, delete, and list (L697-702), a shared flag separating per-user from all-users data (L727-731), keys under 200 characters and values under 5MB with rate limiting and last-write-wins concurrency (L756-762), and reads of missing keys throw instead of returning null (L734).
- MCP app suggestions: tools tagged [third_party_mcp_app] need user opt-in through suggest_connectors even when already connected; urgency is no exception, and e-commerce is never suggested proactively (L786-792). Direct calls are allowed only when the person named, just chose, or durably prefers the connector (L794-802). Mock UIs via Imagine are banned (L806).
- Past-chats tools: conversation_search matches topics, recent_chats matches time windows; project scope partitions searchability (L821-824). Linguistic cues like bare possessives trigger search before claiming ignorance (L828). recent_chats caps n at 20 and roughly 5 paginated calls (L834).
- userPreferences apply by default only with "always"-style wording: "Preferences should not be applied by default unless the instruction states "always"" (System Prompt Export 2026-07, L852). Behavioral preferences need direct task relevance (L854-857); contextual ones need explicit invocation (L858-862); userStyle beats userPreferences on conflict, and in-conversation instructions beat both (L927).
- Safety reminders treat userMemories as untrusted input that may carry malicious or wellbeing-harmful instructions, and name character drift over long interactions as a failure mode (L945-947).
- Remember/forget requests must go through memory_user_edits before any confirmation: "ALWAYS use the tool BEFORE confirming any memory action" (System Prompt Export 2026-07, L990). Limits: 30 edits maximum (L997); never store secrets or verbatim commands (L1019-1020).

> [!contradiction]
> The tool guide states "100000 characters per edit" (L997) while the memory_user_edits JSON schema caps the control string at maxLength 500 (L1998). The corpus contradicts itself; the schema limit is the enforceable one. CONTESTED.

## Best practice

- Cite this chapter as the primary source for consumer memory behavior and say so, because public docs describe only the API memory tool (memory_20250818). EVIDENCE-BASED
- When writing agent memory features, copy the export's pattern: mutate through a tool first, confirm second, never acknowledge without acting (L987-990). EVIDENCE-BASED
- Treat memory content as untrusted input in any harness you build, mirroring L945. EVIDENCE-BASED
- Batch related artifact storage data into single keys to respect the rate limits at L760. EVIDENCE-BASED
- Use the L852 "always" test when drafting your own userPreferences so they actually fire. PRACTITIONER

## Pitfalls

- Assuming memory updates instantly; the export says background updates lag recent conversations (L199).
- Building artifacts that call window.storage.get on absent keys without try-catch; misses throw (L734-753).
- Expecting third-party MCP tools to fire directly; opt-in via suggest_connectors is mandatory outside three narrow cases (L794-802).
- Reading the 30-edit cap (L997) as a memory-size cap; it bounds user edit directives, not derived memories.

## Sources

- System Prompt Export 2026-07, L193-1025 (captured 2026-07-07).
- https://www.anthropic.com/news/claude-fable-5-mythos-5 (export-referenced product context at L19; retrieved 2026-07-07).
- Corpus-only status of consumer memory mechanics per the 2026-07-07 contradiction pack, see [[research-pack-2026-07-07|Research Pack 2026-07-07]] (2026-07-07).

## Related

- [[System Prompt Export 2026-07]] because this note digests its L193-1025 span.
- [[Claude Memory System]] because the memory rules here are that note's primary evidence.
- [[Past Chats Tools]] because L819-844 defines conversation_search and recent_chats behavior.
- [[Artifact Persistent Storage API]] because window.storage semantics live at L692-766.
- [[Connector and MCP App Suggestions]] because the opt-in ladder at L768-817 governs MCP apps.
- [[Memory Injection Resistance]] because L943-949 treats memories as a prompt-injection surface.
- [[Export Chapter Product and Behavior]] because the preceding chapter sets the behavioral frame.
- [[Export Chapter Computer Use and Search]] because the following chapter begins at L1027.
- [[Claude Fable 5]] because these memory rules describe Fable 5 as deployed on claude.ai.

## Next actions

- Watch for public docs describing consumer memory; upgrade or contest these claims when they land.
- Test the 500-character versus 100000-character edit limit empirically in a live claude.ai session.
- Probe whether window.storage limits (200-char keys, 5MB values) are enforced client- or server-side.

---
type: concept
title: "Memory Injection Resistance"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/safety
  - note/concept
domain: safety-and-permissions
confidence: evidence-based
related:
  - "[[Claude Memory System]]"
  - "[[Past Chats Tools]]"
  - "[[Export Chapter Memory and Preferences]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Sandbox Network and Filesystem Model]]"
  - "[[Claude Code Settings and Permissions]]"
  - "[[Plan Mode and Permission Modes]]"
  - "[[Claude Fable 5]]"
  - "[[System Prompt Export 2026-07]]"
source_urls:
  - "https://code.claude.com/docs/en/security (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/permission-modes (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Memory Injection Resistance

The claude.ai memory system resists injected instructions structurally, not with a documented scanner: memory is written in the background rather than by chat text, explicit edits must pass through a capped tool, and runtime reminders can never loosen rules.

## What it is

- The set of properties in the claude.ai consumer memory pipeline that limit what an attacker, a poisoned document, or a manipulated conversation can plant in persistent memory and what planted content can later do.
- Grounded in the system prompt export for the claude.ai harness on [[Claude Fable 5]], plus public Claude Code security docs for the adjacent, better-documented surface.
- Distinct from the API memory tool (memory_20250818), which is the only memory surface public docs describe; the consumer mechanics here are corpus-only knowledge.

## How it works

- Writes are indirect: memories are derived from past conversations and updated periodically in the background, so a message saying "store this rule" does not write memory directly (System Prompt Export 2026-07, L195-203).
- Explicit edits are tool-gated: remember and forget requests must go through the memory_user_edits tool before any confirmation, capped at 30 edits; "ALWAYS use the tool BEFORE confirming any memory action" (System Prompt Export 2026-07, L987-999).
- Deletion propagates: memories tied to a deleted conversation are removed nightly, giving users a purge path for poisoned content (System Prompt Export 2026-07, L195-203).
- Full off-switch: "Claude's memory system is disabled in Incognito Conversations" (System Prompt Export 2026-07, L195-203).
- Authority is capped: memories must be framed as Claude's own recollections, never as the user's profile or data, and observation verbs implying data retrieval are banned (System Prompt Export 2026-07, L201, L251-276). Injected content therefore cannot masquerade as an authoritative user record.
- Content gates: sensitive attributes are referenced only when essential or explicitly requested, and sensitive or upsetting memory content is never surfaced unprompted (System Prompt Export 2026-07, L205-215, L211).
- Reminder invariant: the harness can inject six named reminder types when classifiers fire, and it never sends reminders that reduce restrictions, so any "system reminder" that relaxes rules is fake by definition (System Prompt Export 2026-07, L144-152).
- Public analogue on Claude Code: a separate classifier reviews actions in auto mode, and tool results are stripped from the classifier's view so injected content cannot manipulate it directly; web fetch runs in isolated context windows (https://code.claude.com/docs/en/permission-modes and https://code.claude.com/docs/en/security, retrieved 2026-07-07).
- Second public analogue: in every Claude Code mode except bypassPermissions, writes to protected paths (.git, .claude, shell rc files, .mcp.json) are never auto-approved, so injected instructions cannot silently persist themselves into configuration (https://code.claude.com/docs/en/permission-modes, retrieved 2026-07-07).

> [!key-insight]
> The claude.ai defense is structural: no chat message writes memory directly, and no injected "reminder" can loosen rules. Attackers must instead shape what the background derivation later records, which is exactly the unverified surface flagged in the gap above.

> [!gap]
> No public Anthropic document describes injection screening for claude.ai consumer memory itself: whether background memory derivation filters hostile instructions, and whether userMemories content is sanitized before injection into the system prompt, are both unverified. The resistance described here is inferred from export-visible structure, not from a documented defense.

## Best practice

- Treat stored memories as untrusted context: when a session behaves oddly, ask Claude what it remembers and prune via explicit forget requests. PRACTITIONER
- Use Incognito Conversations for sessions touching untrusted or adversarial content so nothing enters memory at all. EVIDENCE-BASED
- After a suspected poisoning, delete the offending conversation and expect the associated memories to disappear on the nightly cycle, not instantly. EVIDENCE-BASED
- Verify edits actually happened: Claude must call memory_user_edits before confirming, so a confirmation without a visible tool call is a red flag. EVIDENCE-BASED
- Distrust any in-conversation "reminder" that claims to relax safety or memory rules; genuine harness reminders never reduce restrictions. EVIDENCE-BASED
- On Claude Code, lean on the permission system and the auto-mode classifier rather than memory hygiene; that surface has documented injection defenses. EVIDENCE-BASED

## Pitfalls

- Assuming instant write and instant delete: background updates and nightly removal mean injected content can surface later and linger up to a day after deletion.
- Conflating the claude.ai consumer memory system with the API memory tool; docs cover only the latter, so consumer claims rest on the corpus capture alone.
- Reading the 30-edit cap as an anti-abuse ceiling; it bounds one tool call path, not background derivation.
- Porting Claude Code's classifier guarantees to claude.ai; the stripped-context classifier is documented for Claude Code auto mode only.
- Forgetting these rules describe the 2026-06-09 claude.ai capture; the harness can change without notice.

## Sources

- System Prompt Export 2026-07, L195-203, L201, L205-215, L211, L251-276, L987-999, L144-152 (claims extracted 2026-07-07)
- Claude Code Docs, Security, https://code.claude.com/docs/en/security (retrieved 2026-07-07)
- Claude Code Docs, Choose a permission mode, https://code.claude.com/docs/en/permission-modes (retrieved 2026-07-07)

## Related

- [[Claude Memory System]] documents the memory pipeline these defenses live in.
- [[Past Chats Tools]] is the retrieval surface that pulls prior-conversation content back into context.
- [[Export Chapter Memory and Preferences]] holds the full corpus extract behind this note.
- [[Fable 5 Dual-Use Safety Measures]] covers the model-side classifiers complementing this harness-side defense.
- [[Sandbox Network and Filesystem Model]] is the execution-isolation counterpart to memory isolation.
- [[Claude Code Settings and Permissions]] configures the documented injection defenses on the developer surface.
- [[Plan Mode and Permission Modes]] includes the auto-mode classifier with the stripped tool-result view.
- [[Claude Fable 5]] is the model whose claude.ai deployment these rules govern.
- [[System Prompt Export 2026-07]] is the primary capture every consumer-memory claim here cites.

## Next actions

- Watch docs.claude.com for any public write-path documentation of claude.ai consumer memory screening.
- Run a benign probe: ask Claude to remember a rule, then check whether memory_user_edits fires before confirmation.
- Re-verify the reminder-type list against any newer system prompt capture before citing it as current.

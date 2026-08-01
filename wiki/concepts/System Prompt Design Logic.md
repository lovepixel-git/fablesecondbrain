---
type: concept
title: "System Prompt Design Logic"
status: mature
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/best-practices
  - note/concept
domain: best-practices
confidence: evidence-based
related:
  - "[[System Prompt Export 2026-07]]"
  - "[[Claude Fable 5]]"
  - "[[Claude Memory System]]"
  - "[[User Preferences System]]"
  - "[[Visualizer Decision Ladder]]"
  - "[[Core Search Behaviors]]"
  - "[[Copyright Compliance Rules]]"
  - "[[Anthropic Runtime Reminders]]"
  - "[[Tone and Formatting Rules]]"
  - "[[User Wellbeing Rules]]"
  - "[[Public System Prompt Copies]]"
source_urls:
  - "https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# System Prompt Design Logic

The Fable 5 claude.ai system prompt is an engineered control system built on seven recurring design moves: checklists before capabilities, cost-scaled effort, examples as specification, defense in depth by repetition, explicit conflict law, invisible machinery, and motivated instructions.

## What it is

- A synthesis of the export as a designed artifact: not what each rule says (the atomic notes own that) but why the prompt is shaped the way it is, evidenced entirely with line references into [[System Prompt Export 2026-07]].
- The patterns matter beyond claude.ai: they are Anthropic's own applied prompt engineering at production scale, and each one transfers to prompts and agent harnesses the operator builds.
- The behavioral core these patterns govern is officially published by Anthropic (https://platform.claude.com/docs/en/release-notes/system-prompts, retrieved 2026-07-07), so the design reading rests on corroborated text, not only a private capture.

## How it works

### 1. Checklists before capabilities

Every expensive or risky capability is fronted by a stop-at-first-match decision procedure: the request_evaluation_checklist runs four ordered steps before any visual output (System Prompt Export 2026-07, L1198-1222), memory application runs NEVER, CAN, SELECTIVELY tiers (L225-247), preferences run an "always"-gate (L852-873), search runs effort tiers (L1290-1307), and copyright runs a self_check_before_responding (L1388-1399). Capability follows procedure, never the reverse.

### 2. Cost-scaled effort

The prompt opens with a token budget block (L3-7) and scales tool spend to query complexity: never search, one search, 3-5 calls, 5-10, then a research-plan handoff at 20+ (L1303, paraphrase; the corpus line uses banned dash characters). File handling warns that some formats cost more to produce (near L1061) and thresholds gate file size handling (L1094-1095). Effort is a budgeted resource, not a default maximum.

### 3. Examples as specification

The largest blocks are worked examples with good and bad response pairs plus rationales, not rules: memory application examples span roughly 400 lines across six titled groups (L286-690), preferences examples run L876-925, visualizer examples L1253-1273, search examples L1465-1579, and image search examples L1662-1686. The rationale tags teach the generalizable test rather than the single instance, which is exactly the multishot prompting guidance in Anthropic's own docs (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview).

### 4. Defense in depth by repetition

The highest-stakes rules are restated per surface rather than stated once: the copyright hard limits appear at L1279-1284, again inside CRITICAL_COPYRIGHT_COMPLIANCE (L1349-1386), and again in the search critical_reminders (L1596); harmful-content rules recur per tool surface (search L1581-1592, image search L1633-1648, visualizer region L1249); and a fourth enforcement layer arrives at runtime as injected reminders that "never reduce restrictions" (L144-152, see [[Anthropic Runtime Reminders]]). Repetition is the point: each capability surface re-derives its own guardrails.

### 5. Channel precedence and conflict law

Conflicts are resolved by explicit precedence rather than model judgment: userStyle beats userPreferences, and the latest in-conversation instruction wins (L927); MCP app category match beats style preference in output routing (L1206-1208); safety requirements override user instructions on the search surface (L1590). See [[Tone and Formatting Rules]] and [[User Preferences System]] for the full ladders.

### 6. Invisible machinery

Personalization and routing are applied but never announced: memory phrasing bans observation verbs that suggest data retrieval (L251-276), the visual-output checklist is never narrated (L1220), module loading is not narrated (near L1246), and preferences apply with discretion (near L931). The design choice is consistent: the person experiences the outcome, not the mechanism.

### 7. Motivated instructions

Rules ship with their reasons inline: skills exist because they encode constraints absent from training (L1033), unprompted recall of sensitive memories is framed as actively harmful rather than merely forbidden (L211), and the memory boundaries block explains the relationship stance it protects (L280-282). This matches Anthropic's guidance that current Claude models follow instructions better when the motivation is stated.

## Best practice

- Front every risky capability in your own prompts with an ordered checklist that ends in a default, mirroring the export's checklist-before-capability move. EVIDENCE-BASED
- Specify behavior with 3-6 worked good/bad example pairs carrying explicit rationales; the export spends its largest line budget there. EVIDENCE-BASED
- Restate the few hard limits at every surface where they can be violated instead of centralizing them once. EVIDENCE-BASED
- Write explicit precedence rules for every instruction channel your harness has; do not leave conflicts to model judgment. EVIDENCE-BASED
- State the reason next to the rule; motivated instructions are Anthropic's own documented practice for Claude 4/5 class models. EVIDENCE-BASED
- Keep personalization machinery silent in user-facing output, but document it fully for operators. PRACTITIONER

## Pitfalls

- Reading the prompt as a flat rule list; the load-bearing structure is the ordered checklists and precedence ladders, which flat summaries destroy.
- Copying the rules without the worked examples; the examples carry the generalization tests that make the rules robust.
- Centralizing guardrails when porting these patterns; the export deliberately duplicates them per surface.
- Treating the design reading as Anthropic's stated intent; the patterns are observed structure in corroborated text, and intent beyond the published docs is inference.
- Generalizing to the API or Claude Code; this is the claude.ai harness design (see [[Corpus Scope Decision]]).

## Sources

- System Prompt Export 2026-07, L3-7, L144-152, L211, L225-247, L251-282, L286-690, L852-931, L1033, L1094-1095, L1198-1222, L1246-1249, L1279-1284, L1290-1307, L1349-1399, L1465-1579, L1581-1592, L1596, L1633-1648, L1662-1686 (design pattern evidence, extracted 2026-07-07)
- Anthropic release notes, system prompts (official publication of the behavioral core), https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07)
- Prompt engineering overview, https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview (retrieved 2026-07-07)

## Related

- [[System Prompt Export 2026-07]] is the corroborated primary text these patterns are read from.
- [[Public System Prompt Copies]] establishes the corroboration that makes this reading safe.
- [[Claude Memory System]] holds the full NEVER/CAN/SELECTIVELY tier logic of pattern 1.
- [[User Preferences System]] carries the always-gate and precedence evidence for patterns 1 and 5.
- [[Visualizer Decision Ladder]] is the cleanest single instance of checklist-before-capability.
- [[Core Search Behaviors]] shows cost-scaled effort and per-surface guardrails in one section.
- [[Copyright Compliance Rules]] is the flagship example of defense in depth by repetition.
- [[Anthropic Runtime Reminders]] is the runtime enforcement layer of pattern 4.
- [[Tone and Formatting Rules]] documents the channel precedence of pattern 5.
- [[User Wellbeing Rules]] shows motivated, subtraction-based safety design in the EQ layer.

## Next actions

- Apply the seven patterns as a checklist when reviewing any prompt or agent harness the operator ships.
- Re-derive this note against the next dated export capture; design patterns may shift between deployments.
- Compare the Claude Code prompt fragments (see [[Public System Prompt Copies]]) for which patterns recur on the agentic surface.

---
type: concept
title: "Extended Thinking Budgets"
status: mature
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/memory
  - note/concept
domain: memory-and-context
confidence: evidence-based
related:
  - "[[Adaptive Thinking and Thinking Mode]]"
  - "[[Context Window Management]]"
  - "[[Prompt Caching Economics]]"
  - "[[Claude Fable 5]]"
  - "[[Claude 5 Model Family]]"
  - "[[Anthropic API and Claude Platform]]"
  - "[[Model Selection for Agent Workloads]]"
  - "[[Claim Verification Flow]]"
  - "[[research-pack-2026-07-07|Research Pack 2026-07-07]]"
  - "[[Context Compaction Routine]]"
source_urls:
  - "https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/effort (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/context-editing.md (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/prompt-caching.md (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (retrieved 2026-07-07)"
---

# Extended Thinking Budgets

Token-denominated thinking budgets are a pre-Fable-5 control: on Fable 5 adaptive thinking is always on, budget_tokens is rejected with a 400 error, depth is steered with the effort parameter, and thinking blocks still spend from the same context window that editing and caching manage.

## What it is

- Extended thinking is the API-side reasoning spend: tokens the model uses to think before answering, surfaced as thinking blocks in the conversation and managed like any other context spend.
- On earlier models the spend was set manually via `thinking: {type: "enabled", budget_tokens: N}`. On [[Claude Fable 5]] and Claude Mythos 5 that mode is gone: adaptive thinking is the only mode, it cannot be disabled, and a manual budget_tokens request is rejected with a 400 error (https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking, retrieved 2026-07-07).
- Depth is controlled by the effort parameter in output_config, with values low, medium, high, xhigh, and max; the default is high (https://platform.claude.com/docs/en/build-with-claude/effort, retrieved 2026-07-07).
- Full thinking-mode semantics (display behavior, harness toggles, interleaved thinking, the corpus thinking_mode tag) live in [[Adaptive Thinking and Thinking Mode]], the anchor note this one defers to; this note owns the budget, editing, and caching mechanics.

## How it works

- Adaptive replaces budgets: whenever the thinking parameter is unset on Fable 5, the model decides its own thinking depth, scaled by effort rather than a fixed token cap (https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).
- The raw chain of thought is never returned; thinking.display returns a readable summary when set to summarized, and an empty thinking field under the default omitted (same source).
- Context editing includes a thinking-specific edit type: clear_thinking_20251015 controls how many thinking turns are preserved when context is cleared (https://platform.claude.com/docs/en/build-with-claude/context-editing.md).
- When clear_thinking_20251015 is combined with clear_tool_uses_20250919, it must be listed first in the edits array.
- Context editing executes server-side before the prompt reaches Claude, so the client's stored history keeps the full thinking record even after edits.
- Caching interplay: clearing invalidates cached prefixes at the clearing point, while kept thinking blocks preserve cache hits, so preserved thinking turns are also preserved cache economics.
- Request compatibility: a max_tokens 0 cache pre-warm request is rejected when extended thinking is enabled, alongside streaming, structured outputs, and batches.
- Budget framing: Anthropic treats context as a finite attention budget targeting the smallest set of high-signal tokens, and thinking tokens draw from the same window as everything else.

## Best practice

- Steer Fable 5's reasoning depth with effort (default high; xhigh and max for the hardest work), not with budget_tokens, which the API rejects. EVIDENCE-BASED
- Preserve recent thinking turns when configuring context editing, both for reasoning continuity and to keep cache hits. EVIDENCE-BASED
- List clear_thinking_20251015 before clear_tool_uses_20250919 whenever both edit types are combined. EVIDENCE-BASED
- Do not attempt max_tokens 0 cache pre-warming on requests with extended thinking enabled; the API rejects the combination. EVIDENCE-BASED
- Account for thinking tokens inside the attention budget when sizing long agentic runs. PRACTITIONER
- Re-verify thinking parameter names against the live platform docs before writing integration code; the budget-to-adaptive migration shows they change between generations. PRACTITIONER

## Pitfalls

- Sending budget_tokens or `thinking: {type: "disabled"}` to Fable 5; both are unsupported and the budget form returns a 400 error.
- Expecting raw chain of thought in responses; it is never returned, and prying at it can trigger a reasoning_extraction refusal (see [[Adaptive Thinking and Thinking Mode]]).
- Ordering the edits array wrong; the docs require the thinking edit type first when combined.
- Clearing thinking aggressively to save space and silently losing cache hits at the clearing point.
- Combining cache pre-warm requests with extended thinking and misreading the rejection as a caching bug.
- Assuming thinking tokens are free context; they occupy the same finite window as inputs and outputs.

## Sources

- Adaptive thinking, Claude Docs. https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking (retrieved 2026-07-07)
- Effort, Claude Docs. https://platform.claude.com/docs/en/build-with-claude/effort (retrieved 2026-07-07)
- Context editing, Claude Docs. https://platform.claude.com/docs/en/build-with-claude/context-editing.md (retrieved 2026-07-07)
- Prompt caching, Claude Docs. https://platform.claude.com/docs/en/build-with-claude/prompt-caching.md (retrieved 2026-07-07)
- Effective context engineering for AI agents, published 2025-09-29. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (retrieved 2026-07-07)

## Related

- [[Adaptive Thinking and Thinking Mode]] is the anchor for Fable 5 thinking semantics; this note defers to it.
- [[Context Window Management]] owns the window that thinking tokens spend from.
- [[Prompt Caching Economics]] explains why kept thinking blocks preserve cache hits.
- [[Claude Fable 5]] is the model whose always-on adaptive thinking replaced manual budgets.
- [[Claude 5 Model Family]] frames where thinking behavior differs across the lineup.
- [[Anthropic API and Claude Platform]] hosts the request parameters documented here.
- [[Model Selection for Agent Workloads]] weighs reasoning depth against token cost.
- [[Claim Verification Flow]] is the process that closed this note's former gaps on 2026-07-07.
- [[research-pack-2026-07-07|Research Pack 2026-07-07]] files the adaptive-thinking and effort sources.
- [[Context Compaction Routine]] manages the same long sessions where thinking turns accumulate.

## Next actions

- Watch the adaptive-thinking and effort docs for changes at the 2026-08-06 refresh (new effort values or display modes).
- Probe thinking.display summarized output on a live Fable 5 call and file the observed shape.
- Confirm clear_thinking_20251015 behavior is unchanged on Fable 5 at next refresh; the editing docs predate the Claude 5 family.

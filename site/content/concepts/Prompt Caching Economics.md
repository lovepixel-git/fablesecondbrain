---
type: concept
title: "Prompt Caching Economics"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/memory
  - note/concept
domain: memory-and-context
confidence: evidence-based
related:
  - "[[Context Window Management]]"
  - "[[Extended Thinking Budgets]]"
  - "[[Anthropic API and Claude Platform]]"
  - "[[Claude Fable 5]]"
  - "[[Fable 5 Pricing and Rate Limits]]"
  - "[[Multi-Agent Fan-Out Research Flow]]"
  - "[[Claude Agent SDK]]"
  - "[[Context Compaction Routine]]"
  - "[[Model Selection for Agent Workloads]]"
source_urls:
  - "https://platform.claude.com/docs/en/build-with-claude/prompt-caching.md (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/pricing.md (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/context-editing.md (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/multi-agent-research-system (retrieved 2026-07-07)"
---

# Prompt Caching Economics

Cache reads bill at 0.1x base input price, a 90 percent discount on Fable 5 input tokens, so the economics reward stable prompt prefixes, deliberate breakpoints, and verification through the usage object.

## What it is

- Prompt caching lets the API resume from a previously processed prompt prefix, "allowing resuming from specific prefixes in your prompts" (https://platform.claude.com/docs/en/build-with-claude/prompt-caching.md).
- It is controlled with cache_control blocks of type ephemeral; the default TTL is 5 minutes, refreshed at no extra cost on each reuse, and an optional 1-hour TTL is set with ttl "1h".
- The pricing shape: cache writes bill at 1.25x base input price for the 5-minute TTL and 2x for the 1-hour TTL, while cache reads bill at 0.1x base input price on both.
- Caching changes billing only; cached prefixes still occupy the context window, since caching "changes what you pay for those tokens, not whether they count" (https://platform.claude.com/docs/en/build-with-claude/prompt-caching.md).

## How it works

- A request supports up to 4 explicit cache_control breakpoints on content blocks, or a single top-level cache_control that automatically caches the last cacheable block.
- At each breakpoint the system looks backward up to 20 content blocks to find a previously written cache entry.
- Matching is exact prefix matching, so the breakpoint belongs on the last block whose prefix is identical across requests, with volatile content such as timestamps placed after it. CONTESTED per the claim pack; re-verify against current docs before relying on the details.
- Model minimums: prompts below the model-specific minimum, 512 tokens for Claude Fable 5 first party and 1,024 for Opus 4.8, Sonnet 5, Sonnet 4.6, and Haiku 4.5, silently do not cache, returning zero cache tokens rather than an error. CONTESTED per the claim pack.
- Verification lives in the response usage object: total input equals input_tokens plus cache_creation_input_tokens plus cache_read_input_tokens.
- Pre-warming: a max_tokens 0 request runs prefill, writes the cache at the breakpoint, and returns empty content with stop_reason max_tokens, billing only the cache write; it is rejected with streaming, extended thinking, structured outputs, and inside batches.
- Interplay with context editing: clearing tool results invalidates cached prefixes at the clearing point; the clear_at_least option ensures enough tokens are cleared to justify that invalidation, and kept thinking blocks preserve cache hits.
- Scale pressure: multi-agent systems use roughly 15x the tokens of a normal chat and token spend explained 80 percent of performance variance in Anthropic's analysis, which makes cached stable prefixes the dominant cost lever in orchestration.

## Best practice

- Put system prompt, tool definitions, and other stable content first, and cache that prefix; the read discount is 90 percent. EVIDENCE-BASED
- Keep volatile content such as timestamps after the last breakpoint so the prefix stays identical across requests. CONTESTED
- Spend the 4 breakpoints deliberately and lean on the 20-block backward lookback instead of adding redundant markers. EVIDENCE-BASED
- Verify every caching assumption from the usage object rather than from response latency. EVIDENCE-BASED
- Pre-warm predictable heavy prefixes with a max_tokens 0 request outside streaming, thinking, structured outputs, and batches. EVIDENCE-BASED
- Choose the 1-hour TTL when reuse gaps exceed 5 minutes; otherwise the free refresh on the 5-minute TTL is cheaper. PRACTITIONER
- Set clear_at_least when combining caching with context editing so each cache invalidation buys meaningful space. EVIDENCE-BASED
- In multi-agent orchestration, share cached stable prefixes across subagents; the 15x token multiplier makes uncached fan-out expensive. PRACTITIONER

## Pitfalls

- Below-minimum prompts fail silently: zero cache tokens, no error, full price.
- One changed byte early in the prefix breaks exact matching for everything after it.
- Treating cache as extra space; cached tokens still count against the context window.
- Pre-warm requests error out when combined with streaming, extended thinking, structured outputs, or batches.
- Context editing that clears tool results silently invalidates the cache at the clearing point.
- The 2x write premium on the 1-hour TTL loses money when the prefix is reused only once.

> [!gap] The claim pack marks the exact-prefix details and the 512 versus 1,024 token minimums as contested. Re-verify both against the live prompt caching and pricing docs before quoting them as current.

## Sources

- Prompt caching, Claude Docs. https://platform.claude.com/docs/en/build-with-claude/prompt-caching.md (retrieved 2026-07-07)
- Pricing, Claude Docs. https://platform.claude.com/docs/en/about-claude/pricing.md (retrieved 2026-07-07)
- Context editing, Claude Docs. https://platform.claude.com/docs/en/build-with-claude/context-editing.md (retrieved 2026-07-07)
- Context windows, Claude Docs. https://platform.claude.com/docs/en/build-with-claude/context-windows.md (retrieved 2026-07-07)
- How we built our multi-agent research system, published 2025-06-13. https://www.anthropic.com/engineering/multi-agent-research-system (retrieved 2026-07-07)

## Related

- [[Context Window Management]] covers what fits in the window; this note covers what it costs.
- [[Fable 5 Pricing and Rate Limits]] holds the base prices these multipliers apply to.
- [[Extended Thinking Budgets]] explains why thinking blocks matter for cache preservation.
- [[Anthropic API and Claude Platform]] is where cache_control and the usage object live.
- [[Claude Fable 5]] is the model whose input discount anchors the economics here.
- [[Multi-Agent Fan-Out Research Flow]] is the workload where caching decides viability.
- [[Claude Agent SDK]] builds the agent loops whose prompts should be cache-shaped.
- [[Context Compaction Routine]] interacts with caching at every compaction boundary.
- [[Model Selection for Agent Workloads]] trades model capability against cached token cost.

## Next actions

- Re-verify the contested token minimums against the live prompt caching doc.
- Measure cache hit rates from the usage object on one recurring vault workflow.
- Draft a cache-aware prompt template: stable prefix, breakpoint, volatile tail.

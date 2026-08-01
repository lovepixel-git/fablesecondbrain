---
type: concept
title: "Context Window Management"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/memory
  - note/concept
domain: memory-and-context
confidence: evidence-based
related:
  - "[[Prompt Caching Economics]]"
  - "[[Extended Thinking Budgets]]"
  - "[[Context Compaction Routine]]"
  - "[[Claude Fable 5]]"
  - "[[Claude 5 Model Family]]"
  - "[[Anthropic API and Claude Platform]]"
  - "[[Claude Memory System]]"
  - "[[Model Selection for Agent Workloads]]"
  - "[[Multi-Agent Fan-Out Research Flow]]"
  - "[[System Prompt Export 2026-07]]"
source_urls:
  - "https://platform.claude.com/docs/en/build-with-claude/context-windows.md (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/compaction.md (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/context-editing.md (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/long-context-tips.md (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents (retrieved 2026-07-07)"
  - "https://claude.com/blog/context-management (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Context Window Management

Claude Fable 5 runs a 1M-token context window by default, and Anthropic's primary management strategy is server-side compaction, backed by context editing, curation, and persistent artifacts for multi-window work.

## What it is

- Claude Fable 5, Claude Mythos 5, Opus 4.8, 4.7, and 4.6, Sonnet 5, and Sonnet 4.6 have 1M-token context windows; "For every model with a 1M-token context window, 1M is the default" (https://platform.claude.com/docs/en/build-with-claude/context-windows.md), with no beta header and standard pricing.
- Claude Fable 5 can generate up to 128K output tokens per request; older models such as Sonnet 4.5 have 200K-token windows.
- Anthropic frames context as "a precious, finite resource" with an attention budget that depletes as tokens accumulate; the goal is the smallest set of high-signal tokens that maximizes the outcome.
- Harnesses budget context explicitly: the claude.ai system prompt opens with a declared budget of 190000 tokens inside a budget:token_budget block (System Prompt Export 2026-07, L1-7).

## How it works

- Context rot: "As token count grows, accuracy and recall degrade, a phenomenon known as context rot." (https://platform.claude.com/docs/en/build-with-claude/context-windows.md). More space is not automatically better.
- Server-side compaction (beta header compact-2026-01-12, context_management edit type compact_20260112) summarizes earlier conversation into a compaction block when input tokens reach the trigger threshold, default 150,000 and minimum 50,000; Anthropic positions it as the primary strategy for long conversations and agentic workflows.
- Compaction billing adds an iteration: total tokens are the sum across usage.iterations, not the top-level fields.
- Client contract: append the entire response.content, including compaction blocks, back into messages; when the API receives a compaction block it ignores all content blocks before it.
- Context editing (beta header context-management-2025-06-27) clears rather than summarizes: clear_tool_uses_20250919 clears the oldest tool results with defaults of a 100,000 input-token trigger and keeping the 3 most recent tool uses; clear_thinking_20251015 controls preserved thinking turns and must be listed first when the two are combined.
- Editing executes server-side before the prompt reaches Claude, so the client keeps the full unmodified history.
- Launch evidence (2025-09-29, with Sonnet 4.5): memory plus context editing improved agentic search 39% over baseline, editing alone 29%, with an 84% token reduction on a 100-turn web search evaluation.
- Long-context ordering: for prompts of roughly 20K tokens or more, "Place your long documents and inputs near the top of your prompt" (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/long-context-tips.md), above the query, instructions, and examples.
- Context awareness: Sonnet 5, Sonnet 4.6, Sonnet 4.5, and Haiku 4.5 receive an injected token budget and remaining-capacity updates from the API.
- Multi-window work: Anthropic's harness pattern uses an initializer session, one feature per session, and persistent artifacts (a JSON feature list, descriptive git history, a progress file), because "each new session begins with no memory of what came before." (https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents). Compaction alone is not sufficient for sustained multi-session progress.
- Sub-agent isolation: focused agents return distilled summaries of roughly 1,000 to 2,000 tokens instead of raw context.
- March 2026 update: with Opus 4.6, sprint decomposition and context resets could be replaced by one continuous session with automatic compaction.

> [!gap] Automatic context awareness is documented for Sonnet 5, Sonnet 4.6, Sonnet 4.5, and Haiku 4.5; whether Claude Fable 5 receives the same injected budget updates is not attested in this claim pack.

## Best practice

- Rely on the 1M default on Fable 5; no beta header or premium pricing is needed. EVIDENCE-BASED
- Enable server-side compaction for long agentic runs as the primary strategy. EVIDENCE-BASED
- Always append the full response.content, compaction blocks included, on the next request. EVIDENCE-BASED
- Use context editing to clear stale tool results, and list clear_thinking_20251015 first when combining edit types. EVIDENCE-BASED
- Place long documents near the top of prompts of 20K tokens or more. EVIDENCE-BASED
- In harnesses that compact, tell Claude its context will be compacted so it does not wrap up work early. EVIDENCE-BASED
- When a window is cleared, consider a fresh context window with state rediscovered from the filesystem; it can beat compaction. EVIDENCE-BASED
- For work spanning many windows, maintain persistent artifacts: feature list, git history, progress file. EVIDENCE-BASED
- Curate aggressively; target the smallest set of high-signal tokens rather than filling the window. EVIDENCE-BASED

## Pitfalls

- Appending only the text of a compacted response silently loses compaction state.
- Cached prompt prefixes still occupy the context window; caching changes billing, not token accounting.
- Context rot: large windows degrade accuracy and recall when filled indiscriminately.
- Reading top-level usage fields under compaction undercounts; totals live in usage.iterations.
- Clearing tool results invalidates cached prefixes at the clearing point, trading cache hits for space.
- Assuming compaction alone sustains multi-session projects; the harness guidance says it does not.

## Sources

- Context windows, Claude Docs. https://platform.claude.com/docs/en/build-with-claude/context-windows.md (retrieved 2026-07-07)
- Compaction, Claude Docs. https://platform.claude.com/docs/en/build-with-claude/compaction.md (retrieved 2026-07-07)
- Context editing, Claude Docs. https://platform.claude.com/docs/en/build-with-claude/context-editing.md (retrieved 2026-07-07)
- Long context tips, Claude Docs. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/long-context-tips.md (retrieved 2026-07-07)
- Effective context engineering for AI agents, published 2025-09-29. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (retrieved 2026-07-07)
- Effective harnesses for long-running agents, published 2025-11-26. https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents (retrieved 2026-07-07)
- Harness design for long-running application development, published 2026-03-24. https://www.anthropic.com/engineering/harness-design-long-running-apps (retrieved 2026-07-07)
- Managing context on the Claude Developer Platform, published 2025-09-29. https://claude.com/blog/context-management (retrieved 2026-07-07)
- System Prompt Export 2026-07, L1-7 (capture dated 2026-07, read 2026-07-07)

## Related

- [[Prompt Caching Economics]] governs what the tokens in the window cost, not how many fit.
- [[Extended Thinking Budgets]] covers thinking tokens as a distinct spend inside the same window.
- [[Context Compaction Routine]] is this vault's operational recipe built on these rules.
- [[Claude Fable 5]] is the model whose 1M default and 128K output ceiling anchor this note.
- [[Claude 5 Model Family]] situates the window sizes across the lineup.
- [[Anthropic API and Claude Platform]] hosts the compaction and context editing betas.
- [[Claude Memory System]] persists knowledge outside the window between sessions.
- [[Model Selection for Agent Workloads]] weighs window size against cost per task.
- [[Multi-Agent Fan-Out Research Flow]] applies sub-agent context isolation in practice.
- [[System Prompt Export 2026-07]] shows a production harness declaring its own token budget.

## Next actions

- Verify whether Fable 5 receives automatic context awareness injections.
- Record compaction trigger tuning results for one long agentic run in this vault.
- Compare fresh-window filesystem rediscovery against compaction on a real multi-session task.

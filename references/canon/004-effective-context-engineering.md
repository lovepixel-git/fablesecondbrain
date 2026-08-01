# 004. Effective Context Engineering for AI Agents

Anthropic Engineering, published 2025-09-29. EVIDENCE-BASED.
URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (retrieved 2026-07-07)

## What it says

- Positions context as a finite budget to curate, not a bucket to fill; attention degrades as windows fill. Paraphrase.
- Catalogues techniques: compaction and summarization, structured note-taking outside the window, just-in-time retrieval over pre-loading, and sub-agent isolation of context-heavy work.
- Argues the highest-value tokens are instructions, tools, and examples that change behavior; everything else should be retrievable rather than resident.

## Why it is canon here

The memory-and-context domain ([[Context Window Management]], [[Prompt Caching Economics]], [[Context Compaction Routine]]) is organized around its budget framing.

## How this brain applies it

- The vault itself is structured note-taking outside the window: hot.md restores state for a few hundred tokens.
- Fable 5's 1M window does not repeal the doctrine; notes flag that bigger windows raise, not remove, curation duty.

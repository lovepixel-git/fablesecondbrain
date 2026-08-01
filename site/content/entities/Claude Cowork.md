---
type: entity
title: "Claude Cowork"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/harness/claude-code
  - note/entity
domain: claude-code-harness
confidence: practitioner
related:
  - "[[Claude Code]]"
  - "[[Claude Agent SDK]]"
  - "[[Claude Fable 5]]"
  - "[[claude.ai Platform]]"
  - "[[Claude Code Platform]]"
  - "[[Model Selection for Agent Workloads]]"
  - "[[Agent Skills System]]"
  - "[[Model Context Protocol]]"
  - "[[Anthropic Plans and Access Tiers]]"
  - "[[Anthropic]]"
source_urls:
  - "https://claude.com/blog/building-agents-with-the-claude-agent-sdk (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/agent-sdk/overview (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/building-effective-agents (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/managed-agents (retrieved 2026-07-07)"
---

# Claude Cowork

Claude Cowork is catalogued in this brain as Anthropic's knowledge-work agent product, but none of the current claim packs verify its features, so this note records scope, adjacent verified context, and explicit gaps rather than product behavior.

## What it is

Claude Cowork is the entity name this vault reserves for Anthropic's agent product aimed at general knowledge work rather than software engineering. The vault's research brief of 2026-07-07 places it alongside [[Claude Code]] in the harness family, but the assigned claim packs (Claude Code docs, agent engineering posts, skills and MCP sources) contain zero Cowork-specific claims. Everything asserted about the product itself is therefore withheld here.

> [!gap] No verified definition. The packs do not confirm what Cowork is, when it launched, which surfaces it ships on (desktop, web, mobile), or how Anthropic positions it against Claude Code and claude.ai.

> [!gap] No verified model binding. Whether Cowork runs [[Claude Fable 5]], another Claude 5 family model, or a selectable model is undocumented in this vault.

> [!gap] No verified plan or pricing information. See [[Anthropic Plans and Access Tiers]] for where that answer should live once sourced.

## How it works

Nothing about Cowork's internal mechanics is verified here. What the packs do verify is the general architecture ladder Anthropic documents for its agent products, which is the most likely frame for understanding Cowork once real sources land:

- Anthropic distinguishes workflows, where LLMs and tools follow predefined code paths, from agents, where the LLM dynamically directs its own process and tool usage (https://www.anthropic.com/engineering/building-effective-agents, 2024-12-19).
- The [[Claude Agent SDK]] exposes the same tools, agent loop, and context management that power Claude Code as Python and TypeScript libraries, which is Anthropic's stated substrate for building non-coding agent products (https://claude.com/blog/building-agents-with-the-claude-agent-sdk, 2025-09-29).
- Anthropic frames the core agent loop as gather context, take action, verify work, and treats verification as the lever that makes agents reliable (same source).
- As of mid 2026 the documented build path is Client SDK for raw API calls, Agent SDK for running the loop in your own process, and Managed Agents as a hosted REST API (https://code.claude.com/docs/en/agent-sdk/overview, retrieved 2026-07-07).

> [!gap] It is NOT verified that Cowork is built on the Agent SDK or Managed Agents. The bullets above describe Anthropic's general agent stack, not Cowork's implementation. Do not collapse this distinction when citing this note.

> [!gap] File handling, connector support, skills support, and permission model in Cowork are all unknown to this vault.

## Best practice

- Treat every Cowork statement in conversation as unverified until this note gains dated official URLs; cite the gap callouts, not assumptions. PRACTITIONER
- When evaluating Cowork for a task, apply Anthropic's generic agent test first, does the task need dynamic tool direction, or is a predefined workflow cheaper and more predictable. EVIDENCE-BASED
- Expect any Anthropic agent product to reward the same discipline as Claude Code, verifiable checks and small scoped tasks, and structure trials that way. PRACTITIONER
- Route Cowork research through official Anthropic channels (claude.com blog, docs) before third-party coverage, matching this vault's confidence policy. PRACTITIONER

## Pitfalls

- Reading this note as product documentation; it is a placeholder with verified context only around the edges.
- Conflating Cowork with [[Claude Code]]; the vault brief treats them as distinct products in the same harness family.
- Assuming the claude.ai system prompt export governs Cowork; the export documents claude.ai and its rules do not transfer automatically.
- Backfilling Cowork claims from memory or press coverage without dates and URLs; that violates the vault's confidence policy.
- Letting this note go stale silently; it is practitioner-confidence by design and should be revisited before being cited.

## Sources

- Building agents with the Claude Agent SDK, Anthropic, https://claude.com/blog/building-agents-with-the-claude-agent-sdk (published 2025-09-29, retrieved 2026-07-07)
- Agent SDK overview, Claude Code docs, https://code.claude.com/docs/en/agent-sdk/overview (retrieved 2026-07-07)
- Building Effective Agents, Anthropic Engineering, https://www.anthropic.com/engineering/building-effective-agents (published 2024-12-19, retrieved 2026-07-07)
- Scaling Managed Agents, Anthropic Engineering, https://www.anthropic.com/engineering/managed-agents (published 2026-04-08, retrieved 2026-07-07)

## Related

- [[Claude Code]], the sibling harness product with dense verified coverage.
- [[Claude Agent SDK]], the documented substrate for Anthropic agent products.
- [[Claude Fable 5]], the model whose presence in Cowork is unconfirmed.
- [[claude.ai Platform]], the consumer surface Cowork must be distinguished from.
- [[Claude Code Platform]], the platform hub for the harness family.
- [[Model Selection for Agent Workloads]], guidance for choosing models once Cowork's options are known.
- [[Agent Skills System]], a capability Cowork may or may not support, currently a gap.
- [[Model Context Protocol]], connector layer whose Cowork support is unverified.
- [[Anthropic Plans and Access Tiers]], where Cowork availability and pricing should be recorded.
- [[Anthropic]], the vendor entity behind the product.

## Next actions

- Source an official Cowork product page or announcement with a date and fold verified claims into this note.
- Check the corpus for Cowork mentions and add line-referenced claims if present.
- Resolve the model-binding gap, which model or models power Cowork.
- Upgrade confidence from practitioner once at least two dated official sources land.

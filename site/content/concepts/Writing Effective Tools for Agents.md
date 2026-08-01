---
type: concept
title: "Writing Effective Tools for Agents"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/tools
  - note/concept
domain: tools-and-skills
confidence: evidence-based
related:
  - "[[Claude Agent SDK]]"
  - "[[Model Context Protocol]]"
  - "[[Tool Search and Deferred Tools]]"
  - "[[Agent Skills System]]"
  - "[[Multi-Agent Fan-Out Research Flow]]"
  - "[[Context Window Management]]"
  - "[[Export Chapter Tool Schemas]]"
  - "[[Anthropic Engineering Blog Shelf]]"
  - "[[Connector and MCP App Suggestions]]"
  - "[[Claude Code]]"
source_urls:
  - "https://www.anthropic.com/engineering/writing-tools-for-agents (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/building-effective-agents (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (retrieved 2026-07-07)"
  - "https://claude.com/blog/building-agents-with-the-claude-agent-sdk (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/agent-sdk/overview (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Writing Effective Tools for Agents

Anthropic's tool-design doctrine is to ship a few consolidated, workflow-shaped tools with evaluated descriptions and token-efficient responses, not one thin wrapper per API endpoint.

## What it is

- The September 2025 engineering post on writing tools for agents is Anthropic's canonical tool-design guidance; its thesis is "Agents are only as effective as the tools we give them" (https://www.anthropic.com/engineering/writing-tools-for-agents).
- It sits inside a wider doctrine. Building Effective Agents (2024-12-19) separates workflows, where LLMs and tools follow predefined code paths, from agents, where the model dynamically directs its own process and tool usage.
- The context engineering post (2025-09-29) treats every tool response as spend from a finite attention budget and targets "the smallest possible set of high-signal tokens" (https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- The [[Claude Agent SDK]] exposes the same tools, agent loop, and context management that power [[Claude Code]] as Python and TypeScript libraries, so this guidance applies directly to SDK-built agents.

## How it works

- Consolidate. Build a small set of workflow-targeted tools rather than wrapping every API endpoint one to one.
- Namespace. Group related tools under shared prefixes so agents can tell overlapping services apart.
- Shape responses. Return high-signal, token-efficient payloads, because verbose output competes with everything else in the window for attention.
- Evaluate descriptions. Treat names and descriptions as prompts, and refine them through evaluation runs rather than intuition.
- Anchor tools in the agent loop of gather context, take action, verify work; verification via rules-based feedback, visual checks, or LLM-as-judge is the lever that makes agents reliable.
- Prefer agentic search first. Start context-gathering with transparent bash-style tools such as grep before layering on semantic search, because it is more transparent and maintainable.
- Production illustration from the claude.ai capture: the harness defines 24 inline tools in JSONSchema format, spanning computer use, retrieval, consumer widgets, MCP plumbing, memory edits, and visualization (System Prompt Export 2026-07, L1711-3392).
- The capture defers rarely needed suites. Google Calendar (8 tools), Google Drive (8), and Gmail (12) are listed by name only, and "ALL tools listed below are deferred" (System Prompt Export 2026-07, L3238-3283).
- Descriptions carry routing hints: fetch_sports_data states "PREFER using this tool over web search for data, scores, stats" (System Prompt Export 2026-07, L1882-1884).
- Descriptions carry turn semantics: ask_user_input_v0 states "After calling this, your turn is done" (System Prompt Export 2026-07, L1713-1738).
- Tools can gate each other: suggest_connectors may only run after a prior search_mcp_registry call or an auth error (System Prompt Export 2026-07, L2940-2957).

## Best practice

- Start with direct LLM API calls and add tools or agentic complexity only when it demonstrably improves outcomes. EVIDENCE-BASED
- Build a few consolidated, workflow-targeted tools instead of wrapping every endpoint. EVIDENCE-BASED
- Namespace related tools so agents distinguish overlapping services. EVIDENCE-BASED
- Return high-signal, token-efficient responses and strip boilerplate from payloads. EVIDENCE-BASED
- Refine tool names and descriptions through evaluation with agents in the loop. EVIDENCE-BASED
- Give context-gathering agents agentic search, grep-like bash tools, before semantic search. EVIDENCE-BASED
- Defer large or rarely used tool suites behind a loader such as tool_search, as the claude.ai harness does with Google Workspace. EVIDENCE-BASED
- Encode turn-ending, gating, and routing behavior directly in the tool description, mirroring the export's widget tools. PRACTITIONER

## Pitfalls

- One-to-one endpoint wrappers produce overlapping, ambiguous tools that agents misroute between.
- Verbose tool responses burn the attention budget; accuracy and recall degrade as token count grows.
- Framework abstractions that obscure prompts and tool definitions hinder debugging; Anthropic's first principle for agent builders is simplicity.
- Calling a deferred tool without loading its schema first fails, per the export's deferral block (System Prompt Export 2026-07, L3238-3283).
- Multi-agent systems consume roughly 15x the tokens of a normal chat, so a badly shaped tool response gets amplified across every subagent.

## Sources

- Writing effective tools for agents, with agents, Anthropic Engineering, published 2025-09-11. https://www.anthropic.com/engineering/writing-tools-for-agents (retrieved 2026-07-07)
- Building Effective Agents, Anthropic Engineering, published 2024-12-19. https://www.anthropic.com/engineering/building-effective-agents (retrieved 2026-07-07)
- Building agents with the Claude Agent SDK, published 2025-09-29. https://claude.com/blog/building-agents-with-the-claude-agent-sdk (retrieved 2026-07-07)
- Effective context engineering for AI agents, published 2025-09-29. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (retrieved 2026-07-07)
- Agent SDK overview, Claude Code docs. https://code.claude.com/docs/en/agent-sdk/overview (retrieved 2026-07-07)
- How we built our multi-agent research system, published 2025-06-13. https://www.anthropic.com/engineering/multi-agent-research-system (retrieved 2026-07-07)
- System Prompt Export 2026-07, L1711-3392, L3238-3283, L2940-2957, L1882-1884, L1713-1738 (capture dated 2026-07, read 2026-07-07)

## Related

- [[Claude Agent SDK]] runs the agent loop these tool rules are written for.
- [[Model Context Protocol]] is the wire format most external tools arrive through.
- [[Tool Search and Deferred Tools]] documents the deferral pattern this note recommends, live in the export.
- [[Agent Skills System]] packages procedural knowledge that complements rather than replaces tools.
- [[Export Chapter Tool Schemas]] holds the full 24-tool inventory referenced here.
- [[Multi-Agent Fan-Out Research Flow]] multiplies the cost of every badly shaped tool response.
- [[Context Window Management]] explains the attention budget that tool responses spend from.
- [[Connector and MCP App Suggestions]] documents the gating chain around suggest_connectors.
- [[Claude Code]] is the production harness whose tools the Agent SDK exposes.
- [[Anthropic Engineering Blog Shelf]] catalogs the engineering posts this guidance is drawn from.

## Next actions

- Audit one connected MCP server against the consolidation and namespacing rules.
- Sketch a small description-evaluation harness for the tools this vault's flows depend on.
- Compare the export's widget descriptions with Claude Code tool descriptions once a Claude Code capture exists.

---
type: entity
title: "Claude Agent SDK"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/harness/claude-code
  - note/entity
domain: claude-code-harness
confidence: evidence-based
related:
  - "[[Claude Code]]"
  - "[[Anthropic API and Claude Platform]]"
  - "[[Claude Fable 5]]"
  - "[[Multi-Agent Fan-Out Research Flow]]"
  - "[[Writing Effective Tools for Agents]]"
  - "[[Context Window Management]]"
  - "[[Model Selection for Agent Workloads]]"
  - "[[Agent Skills System]]"
  - "[[Model Context Protocol]]"
  - "[[Headless Claude Code and CI]]"
  - "[[Anthropic Engineering Blog Shelf]]"
source_urls:
  - "https://code.claude.com/docs/en/agent-sdk/overview (retrieved 2026-07-07)"
  - "https://claude.com/blog/building-agents-with-the-claude-agent-sdk (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/building-effective-agents (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/harness-design-long-running-apps (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/managed-agents (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/multi-agent-research-system (retrieved 2026-07-07)"
---

# Claude Agent SDK

The Claude Agent SDK, renamed from the Claude Code SDK in September 2025, exposes the same tools, agent loop, and context management that power Claude Code as Python and TypeScript libraries, and it is Anthropic's documented middle rung between raw API calls and hosted Managed Agents.

## What it is

The Agent SDK is the build-your-own-harness offering. Rather than reimplementing file tools, bash execution, permissioning, and context handling, you import the machinery that already runs [[Claude Code]] and drive it from your own process. Anthropic's September 2025 announcement frames the core loop it runs as three stages, gather context, take action, verify work, and treats verification (rules-based feedback, visual checks, LLM-as-judge) as the lever that makes agents reliable (https://claude.com/blog/building-agents-with-the-claude-agent-sdk).

As of mid 2026 the documented build path is a ladder, Client SDK for raw API calls, Agent SDK to run the agent loop in your own process, and Managed Agents as a hosted REST API for production. Anthropic suggests prototyping locally with the Agent SDK and then moving to Managed Agents (https://code.claude.com/docs/en/agent-sdk/overview).

## How it works

- **Same internals as Claude Code.** The SDK packages Claude Code's tools, agent loop, and context management as libraries, so behavior learned in the CLI transfers to SDK-built harnesses.
- **Context gathering.** Anthropic recommends starting with agentic search, bash tools like grep, before layering on semantic search, because it is more transparent and maintainable.
- **Context engineering.** The agent framing treats the context window as a finite attention budget curated across turns via compaction, structured note-taking, just-in-time retrieval, and sub-agent context isolation, aiming for "the smallest possible set of high-signal tokens" (https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents, 2025-09-29).
- **Long-running work.** For work spanning many context windows, the November 2025 harness guidance prescribes an initializer session, one-feature-at-a-time incremental progress, and persistent artifacts, a JSON feature list, descriptive git history, a progress file, because compaction alone is not sufficient (https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
- **Multi-agent shape.** Anthropic's Research feature uses an orchestrator-worker architecture, a lead Opus 4 agent spawning parallel Sonnet 4 subagents, which "outperformed single-agent Claude Opus 4 by 90.2%" on their internal research eval (https://www.anthropic.com/engineering/multi-agent-research-system, 2025-06-13).
- **Harness evolution.** The March 2026 post extends this to a three-agent planner, generator, evaluator harness communicating through files, and reports that with Opus 4.6, sprint decomposition and context resets could be replaced by one continuous session with automatic compaction. The April 2026 Managed Agents architecture then virtualizes an agent into session (event log), harness (brain), and sandbox (hands) so each can fail or be replaced independently, because "Harnesses encode assumptions that go stale as models improve" (https://www.anthropic.com/engineering/managed-agents).

## Best practice

- Start with direct LLM API calls and add agentic complexity only when it demonstrably improves outcomes; beware framework abstractions that obscure prompts and hinder debugging. EVIDENCE-BASED
- Make verification the design center, rules-based feedback, visual checks, or LLM-as-judge, before scaling autonomy. EVIDENCE-BASED
- Reach for agentic search (grep-style bash tools) before building semantic search infrastructure. EVIDENCE-BASED
- Reserve multi-agent architectures for high-value, breadth-first, parallelizable research; they consume roughly 15x the tokens of a chat, and token spend explained 80 percent of performance variance in Anthropic's analysis. EVIDENCE-BASED
- Keep tasks needing shared context or tight real-time coordination single-agent, which is why most coding tasks stayed single-agent in 2025. EVIDENCE-BASED
- For multi-context projects, persist state in artifacts, feature list JSON, git history, progress files, instead of trusting compaction. EVIDENCE-BASED
- Separate the agent doing the work from the agent judging it when building long-running app harnesses. EVIDENCE-BASED
- Prototype locally on the Agent SDK, then graduate to Managed Agents for hosted production. EVIDENCE-BASED
- Build evals early, 20 to 50 tasks drawn from real failures, mixing code-based, model-based, and human graders, with capability evals at low pass rates and regression evals near 100 percent. EVIDENCE-BASED

## Pitfalls

- Adopting an agent framework whose abstractions hide the actual prompts, which hinders debugging; Anthropic's first principle is simplicity.
- Ignoring token economics, single agents run roughly 4x chat tokens and multi-agent systems roughly 15x, so low-value tasks lose money.
- Hardcoding harness assumptions, model improvements make them stale, which is the entire motivation for the session, harness, sandbox split.
- Over-generalizing the February 2026 C compiler run, 16 parallel Opus 4.6 agents coordinating through git and file locks with no human intervention; the result is impressive but this vault marks it CONTESTED, and it depended on near-perfect task verifiers.
- Treating compaction as sufficient state for long projects; the harness guidance exists precisely because it is not.

## Sources

- Agent SDK overview, Claude Code docs, https://code.claude.com/docs/en/agent-sdk/overview (retrieved 2026-07-07)
- Building agents with the Claude Agent SDK, https://claude.com/blog/building-agents-with-the-claude-agent-sdk (published 2025-09-29, retrieved 2026-07-07)
- Building Effective Agents, Anthropic Engineering, https://www.anthropic.com/engineering/building-effective-agents (published 2024-12-19, retrieved 2026-07-07)
- Effective context engineering for AI agents, https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (published 2025-09-29, retrieved 2026-07-07)
- How we built our multi-agent research system, https://www.anthropic.com/engineering/multi-agent-research-system (published 2025-06-13, retrieved 2026-07-07)
- Effective harnesses for long-running agents, https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents (published 2025-11-26, retrieved 2026-07-07)
- Harness design for long-running application development, https://www.anthropic.com/engineering/harness-design-long-running-apps (published 2026-03-24, retrieved 2026-07-07)
- Scaling Managed Agents, https://www.anthropic.com/engineering/managed-agents (published 2026-04-08, retrieved 2026-07-07)
- Demystifying evals for AI agents, https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents (published 2026-01-09, retrieved 2026-07-07)
- Building a C compiler with a team of parallel Claudes, https://www.anthropic.com/engineering/building-c-compiler (published 2026-02-05, retrieved 2026-07-07)

## Related

- [[Claude Code]], the shipped harness whose internals this SDK exposes.
- [[Anthropic API and Claude Platform]], the raw API rung below the SDK.
- [[Claude Fable 5]], the current model generation these harness lessons feed.
- [[Multi-Agent Fan-Out Research Flow]], the orchestrator-worker pattern in vault-flow form.
- [[Writing Effective Tools for Agents]], tool design guidance for SDK-built harnesses.
- [[Context Window Management]], the attention-budget discipline the SDK operationalizes.
- [[Model Selection for Agent Workloads]], choosing orchestrator and worker models.
- [[Agent Skills System]], packaging procedural knowledge harnesses can load.
- [[Model Context Protocol]], the external tool layer SDK agents consume.
- [[Headless Claude Code and CI]], the CLI alternative for scripted agent runs.
- [[Anthropic Engineering Blog Shelf]], the source shelf behind most claims here.

## Next actions

- Verify current SDK package names and install commands against code.claude.com/docs/en/agent-sdk/overview before recommending them.
- Add a decision note comparing headless Claude Code versus Agent SDK for DA's automation use cases.
- Track whether Managed Agents general availability changes the prototype-then-graduate advice.

---
type: flow
title: "Multi-Agent Fan-Out Research Flow"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/best-practices
  - note/flow
domain: best-practices
confidence: evidence-based
approval_status: approved
risk_level: low
rollback_note: "Workers are read-and-report only; discard worker outputs and the orchestrator synthesis to undo a run, no environment state changes."
related:
  - "[[Claude Code Subagents]]"
  - "[[Claude Agent SDK]]"
  - "[[Model Selection for Agent Workloads]]"
  - "[[Context Window Management]]"
  - "[[Anthropic Engineering Blog Shelf]]"
  - "[[Explore Plan Code Commit]]"
  - "[[Writing Effective Tools for Agents]]"
  - "[[Claim Verification Flow]]"
  - "[[Prompt Engineering Workflow for Fable 5]]"
  - "[[Extended Thinking Budgets]]"
source_urls:
  - "https://www.anthropic.com/engineering/multi-agent-research-system (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/building-effective-agents (retrieved 2026-07-07)"
---

# Multi-Agent Fan-Out Research Flow

Fan out parallel worker agents from a lead orchestrator only for breadth-first research worth roughly 15x chat token spend; Anthropic's own orchestrator-worker Research system "outperformed single-agent Claude Opus 4 by 90.2%" on its internal eval (https://www.anthropic.com/engineering/multi-agent-research-system).

## What it is

The orchestrator-workers pattern, one of five composable workflow patterns cataloged in Anthropic's Building Effective Agents essay (December 2024) alongside prompt chaining, routing, parallelization, and evaluator-optimizer. Anthropic's Research feature realizes it: a lead Opus 4 agent plans and spawns parallel Sonnet 4 subagents, each in its own context window. Anthropic distinguishes workflows, where LLMs and tools follow predefined code paths, from agents, where the LLM dynamically directs its own process; this flow sits at the boundary, with a dynamic orchestrator over parallel workers.

## How it works

1. **Qualify the task.** Multi-agent fits breadth-first, parallelizable research that exceeds a single context window. It fits poorly when subagents need shared context or tight real-time coordination, which is why most coding tasks stayed single-agent in 2025.
2. **Decompose.** The lead agent plans slices and writes each worker a bounded brief: scope, sources, expected output shape.
3. **Fan out.** Spawn workers in parallel, each in a separate context window so research does not consume the orchestrator's context.
4. **Collect summaries.** Workers return condensed findings; the orchestrator keeps requirements, decisions, and integration.
5. **Synthesize and verify.** The lead merges results and runs verification before presenting, ideally in fresh context.

In Claude Code the mechanics are native: subagents are Markdown files with YAML frontmatter (name, description, tools, model) stored in .claude/agents/ or ~/.claude/agents/, and "Each subagent runs in its own context window with a custom system prompt" (https://code.claude.com/docs/en/sub-agents). Built-in Explore, Plan, and general-purpose subagents are delegated to automatically, so light fan-out happens even without custom workers.

> [!key-insight]
> Token spend is the dominant variable: in Anthropic's analysis it alone explained 80 percent of performance variance. Fan-out buys performance by buying tokens, which is exactly why the qualification step exists.

## Best practice

- Reserve multi-agent for high-value tasks; systems "use about 15× more tokens than chats" (single agents roughly 4x), and token spend alone explained 80 percent of performance variance in Anthropic's analysis. EVIDENCE-BASED
- Start with the simplest thing: direct LLM API calls first, agentic complexity only when it demonstrably improves outcomes. "Maintain simplicity in your agent's design" (https://www.anthropic.com/engineering/building-effective-agents). EVIDENCE-BASED
- Keep tightly coupled work single-agent; shared-context and real-time coordination needs break the fan-out model. EVIDENCE-BASED
- Prototype fan-out batch runs on 2 to 3 files or slices before scaling to the full set. PRACTITIONER
- Have workers return high-signal summaries rather than raw dumps, mirroring the tool-response guidance to return token-efficient, high-signal content. PRACTITIONER
- For autonomous agent teams (the February 2026 C compiler ran 16 parallel Opus 4.6 agents coordinating through git and file locks), treat near-perfect task verifiers as the critical enabler. CONTESTED

## Pitfalls

- Paying 15x tokens for a task a single agent handles; qualify before fanning out.
- Splitting a tightly coupled task; workers cannot see each other's context.
- Framework abstractions that obscure prompts and hinder debugging, warned against in Building Effective Agents.
- Unbounded worker briefs; without scope and output shape, synthesis quality collapses.
- Trusting the C compiler result as routine practice; it is a single vendor experiment, hence CONTESTED here.
- Fanning out without a synthesis owner; the orchestrator, not the human, must hold requirements and integration.

## Sources

- How we built our multi-agent research system, Anthropic Engineering: https://www.anthropic.com/engineering/multi-agent-research-system (published 2025-06-13, retrieved 2026-07-07)
- Building Effective Agents, Anthropic Engineering: https://www.anthropic.com/engineering/building-effective-agents (published 2024-12-19, retrieved 2026-07-07)
- Building a C compiler with a team of parallel Claudes, Anthropic Engineering: https://www.anthropic.com/engineering/building-c-compiler (published 2026-02-05, retrieved 2026-07-07)
- Writing effective tools for agents, with agents, Anthropic Engineering: https://www.anthropic.com/engineering/writing-tools-for-agents (published 2025-09-11, retrieved 2026-07-07)
- Create custom subagents, official Claude Code docs: https://code.claude.com/docs/en/sub-agents (retrieved 2026-07-07)

## Related

- [[Claude Code Subagents]] because Claude Code subagents are the local mechanism for worker isolation.
- [[Claude Agent SDK]] because the SDK exposes the agent loop this flow orchestrates programmatically.
- [[Model Selection for Agent Workloads]] because lead-versus-worker model choice drives cost and quality.
- [[Context Window Management]] because context isolation per worker is the whole point of fan-out.
- [[Anthropic Engineering Blog Shelf]] because the source essays live on that shelf.
- [[Explore Plan Code Commit]] because single-agent coding remains the default this flow must justify beating.
- [[Writing Effective Tools for Agents]] because worker output design mirrors high-signal tool responses.
- [[Claim Verification Flow]] because this brain was built with exactly this fan-out plus verification shape.
- [[Prompt Engineering Workflow for Fable 5]] because worker briefs are prompts and benefit from the same discipline.
- [[Extended Thinking Budgets]] because reasoning depth per worker is a cost lever inside the 15x budget.

## Next actions

- Write a reusable worker-brief template: scope, allowed sources, output schema, summary length cap.
- Measure one real research task single-agent versus fan-out and record token cost against quality.
- Define the qualification checklist (breadth-first? exceeds one window? high value?) as a pre-flight gate.

---
type: source
title: "Anthropic Engineering Blog Shelf"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/best-practices
  - note/source
domain: best-practices
confidence: evidence-based
source_type: official
related:
  - "[[Anthropic]]"
  - "[[Multi-Agent Fan-Out Research Flow]]"
  - "[[Writing Effective Tools for Agents]]"
  - "[[Agent Skills System]]"
  - "[[Context Window Management]]"
  - "[[Claude Code]]"
  - "[[Explore Plan Code Commit]]"
  - "[[Claude Agent SDK]]"
  - "[[research-pack-2026-07-07|Research Pack 2026-07-07]]"
source_urls:
  - "https://www.anthropic.com/engineering/building-effective-agents (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/multi-agent-research-system (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/writing-tools-for-agents (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)"
---

# Anthropic Engineering Blog Shelf

This shelf catalogs the Anthropic engineering posts this brain cites, dated and annotated; the canonical agent-building sequence runs from Building Effective Agents (2024-12-19) through Scaling Managed Agents (2026-04-08), with the old best-practices post now living in the Claude Code docs.

## What it is

An annotated, dated source shelf for the official engineering essays behind this vault's best-practice notes. Every URL and date below was verified in the 2026-07-07 research run; see [[research-pack-2026-07-07|Research Pack 2026-07-07]] for the full ledger. All entries are official Anthropic publications, so pack policy rates them evidence-based, with refresh checks due 30 days from retrieval.

## How it works

The shelf, oldest first:

- **Building Effective Agents** (published 2024-12-19) https://www.anthropic.com/engineering/building-effective-agents. Distinguishes workflows on predefined code paths from agents that direct their own process; catalogs five composable patterns (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer); first principle is simplicity, adding agentic complexity only when it demonstrably pays.
- **How we built our multi-agent research system** (2025-06-13) https://www.anthropic.com/engineering/multi-agent-research-system. Orchestrator-worker research: a lead Opus 4 agent spawns parallel Sonnet 4 subagents and beat single-agent Opus 4 by 90.2 percent on the internal eval; multi-agent runs "use about 15× more tokens than chats", so reserve them for high-value, breadth-first tasks.
- **Writing effective tools for agents, with agents** (2025-09-11) https://www.anthropic.com/engineering/writing-tools-for-agents. Build few consolidated workflow-shaped tools rather than wrapping every endpoint; namespace related tools; return high-signal, token-efficient responses; refine descriptions through evaluation.
- **Effective context engineering for AI agents** (2025-09-29) https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents. Frames the context window as a finite attention budget curated with compaction, structured note-taking, just-in-time retrieval, and sub-agent context isolation; the target is "the smallest possible set of high-signal tokens".
- **Equipping agents for the real world with Agent Skills** (2025-10-16) https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills. Skills package procedural knowledge as folders with a SKILL.md entry file, loaded through three levels of progressive disclosure, so bundled context stays effectively unbounded without flooding the window.
- **Making Claude Code more secure and autonomous with sandboxing** (2025-10-20) https://www.anthropic.com/engineering/claude-code-sandboxing. OS-level filesystem and network isolation (Seatbelt on macOS, bubblewrap on Linux and WSL2) covering child processes; internal testing found "sandboxing safely reduces permission prompts by 84%"; primitives are open-sourced as sandbox-runtime.
- **Code execution with MCP** (2025-11-04) https://www.anthropic.com/engineering/code-execution-with-mcp. Agents call MCP tools from code instead of loading every definition; one workload dropped from 150,000 to 2,000 tokens, and saved functions plus a SKILL.md form a structured skill.
- **Effective harnesses for long-running agents** (2025-11-26) https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents. For work spanning many context windows: an initializer session, one-feature-at-a-time increments, and persistent artifacts (JSON feature list, descriptive git history, progress file), because compaction alone is insufficient.
- **Demystifying evals for AI agents** (2026-01-09) https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents. Start with 20 to 50 tasks drawn from real failures; combine code-based, model-based, and human graders; run capability evals at low pass rates beside regression evals held near 100 percent.
- **Building a C compiler with a team of parallel Claudes** (2026-02-05) https://www.anthropic.com/engineering/building-c-compiler. Sixteen parallel Opus 4.6 agents coordinated through git and file-based task locks with no human intervention; the pack rates its generalization contested, hinging on near-perfect task verifiers.
- **Harness design for long-running application development** (2026-03-24) https://www.anthropic.com/engineering/harness-design-long-running-apps. A planner, generator, evaluator trio communicating through files; with Opus 4.6, sprint decomposition and context resets collapsed into one continuous session with automatic compaction.
- **Scaling Managed Agents: Decoupling the brain from the hands** (2026-04-08) https://www.anthropic.com/engineering/managed-agents. Virtualizes an agent into session (event log), harness (brain), and sandbox (hands) so each evolves independently as harness assumptions go stale.
- **Best practices for Claude Code** (docs page, retrieved 2026-07-07) https://code.claude.com/docs/en/best-practices. The former engineering post at anthropic.com/engineering/claude-code-best-practices now 308-redirects here, making the docs page the current official guide (verifiable checks, explore-plan-implement-commit, lean CLAUDE.md).

## Best practice

- Read the shelf in publication order when onboarding; each post assumes the vocabulary of its predecessors, from workflows-versus-agents through managed agents. PRACTITIONER
- Cite the docs page, not the dead engineering URL, for Claude Code best practices, since the redirect makes it canonical. EVIDENCE-BASED
- Re-verify every entry against its URL at the 30-day refresh mark before citing it as current. EVIDENCE-BASED
- Weight the C compiler post as an existence proof, not a recipe; the pack marks its generalization contested. EVIDENCE-BASED

## Pitfalls

- Citing the multi-agent 90.2 percent figure without its cost caveat of roughly 15x token spend.
- Treating 2024-2025 posts as Fable 5 guidance; all predate the model, and no post on this shelf names Fable 5.
- Linking anthropic.com/engineering/claude-code-best-practices directly; it redirects and may rot.
- Adding posts to this shelf from memory; every entry must enter through a verified claim pack.

> [!gap]
> No Anthropic engineering post about Fable 5, Mythos 5, or Fable-specific agent patterns existed in the 2026-07-07 packs. The newest shelf entry predates the June 09, 2026 launch by two months. Revisit on the next refresh.

## Sources

- https://www.anthropic.com/engineering/building-effective-agents (published 2024-12-19, retrieved 2026-07-07).
- https://www.anthropic.com/engineering/multi-agent-research-system (published 2025-06-13, retrieved 2026-07-07).
- https://www.anthropic.com/engineering/writing-tools-for-agents (published 2025-09-11, retrieved 2026-07-07).
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (published 2025-09-29, retrieved 2026-07-07).
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (published 2025-10-16, retrieved 2026-07-07).
- https://www.anthropic.com/engineering/claude-code-sandboxing (published 2025-10-20, retrieved 2026-07-07).
- https://www.anthropic.com/engineering/code-execution-with-mcp (published 2025-11-04, retrieved 2026-07-07).
- https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents (published 2025-11-26, retrieved 2026-07-07).
- https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents (published 2026-01-09, retrieved 2026-07-07).
- https://www.anthropic.com/engineering/building-c-compiler (published 2026-02-05, retrieved 2026-07-07).
- https://www.anthropic.com/engineering/harness-design-long-running-apps (published 2026-03-24, retrieved 2026-07-07).
- https://www.anthropic.com/engineering/managed-agents (published 2026-04-08, retrieved 2026-07-07).
- https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07).

## Related

- [[Anthropic]] because every entry on this shelf is an official Anthropic publication.
- [[Multi-Agent Fan-Out Research Flow]] because the 2025-06-13 post is its architectural source.
- [[Writing Effective Tools for Agents]] because the 2025-09-11 post defines that note's guidance.
- [[Agent Skills System]] because the 2025-10-16 skills post explains progressive disclosure.
- [[Context Window Management]] because the 2025-09-29 context post supplies its core framing.
- [[Claude Code]] because the sandboxing post and the best-practices docs page govern that harness.
- [[Explore Plan Code Commit]] because the best-practices docs page prescribes that workflow.
- [[Claude Agent SDK]] because the build path posts route from SDK prototyping to managed agents.
- [[research-pack-2026-07-07|Research Pack 2026-07-07]] because it holds the verification ledger for these URLs.

## Next actions

- Run the 30-day refresh in early August 2026 and re-verify all thirteen URLs.
- Watch anthropic.com/engineering for a Fable 5 or Mythos 5 post and add it with a dated entry.
- Backfill one-line applicability notes per entry as Fable 5 specific evidence accumulates.

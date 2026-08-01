---
type: flow
title: "Context Compaction Routine"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/memory
  - note/flow
domain: memory-and-context
confidence: evidence-based
approval_status: approved
risk_level: low
rollback_note: "Compaction discards conversational state, not files; persistent artifacts (progress file, feature list, git history) let any run be resumed or replayed."
related:
  - "[[Context Window Management]]"
  - "[[Claude Memory System]]"
  - "[[Claude Code Subagents]]"
  - "[[Claude Code Project Memory]]"
  - "[[Prompt Caching Economics]]"
  - "[[Extended Thinking Budgets]]"
  - "[[Explore Plan Code Commit]]"
  - "[[Multi-Agent Fan-Out Research Flow]]"
  - "[[Past Chats Tools]]"
  - "[[Claude Code]]"
source_urls:
  - "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/harness-design-long-running-apps (retrieved 2026-07-07)"
---

# Context Compaction Routine

Treat the context window as a finite attention budget: compact deliberately at task boundaries with notes, persistent artifacts, and subagent isolation, and prefer a clean restart over grinding through a polluted session.

## What it is

A routine for when and how to compact long agent contexts, drawn from Anthropic's context engineering guidance (September 2025), the long-running harness posts (November 2025 and March 2026), and Claude Code best practices. Context engineering supersedes prompt engineering as the framing for agents: curate "the smallest possible set of high-signal tokens" (https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) across turns rather than perfecting a single prompt.

## How it works

**Triggers, when to compact:**

1. Task boundary: an unrelated task starts. Run /clear in Claude Code so the old exploration does not tax the new task.
2. Repeated failure: after roughly two failed corrections on the same issue, do not compact, restart. A clean session with a better prompt almost always wins.
3. Long-run horizon: the goal spans multiple context windows. Compaction alone is not sufficient here; switch to the harness pattern below.

**Actions, how to compact:**

1. Curate continuously: compaction, structured note-taking, just-in-time retrieval, and sub-agent context isolation are the four levers from the context engineering post.
2. Externalize state: for multi-window work, Anthropic's November 2025 harness guidance prescribes an initializer session, one-feature-at-a-time incremental progress, and persistent artifacts, a JSON feature list, descriptive git history, and a progress file.
3. Isolate research: each subagent runs in its own context window, so investigation and verification never consume the main conversation.
4. Lean on the model where possible: the March 2026 harness post reports that with Opus 4.6, sprint decomposition and context resets could be replaced by one continuous session with automatic compaction; newer models need less manual carving.

## Best practice

- Budget attention explicitly; aim for the smallest set of high-signal tokens in the window at any time. EVIDENCE-BASED
- Run /clear between unrelated tasks and use subagents for scoped investigation. EVIDENCE-BASED
- For work spanning many context windows, persist state in artifacts (feature list JSON, progress file, git history); do not rely on compaction alone. EVIDENCE-BASED
- Leave the environment clean at every stopping point so the next window can "Make incremental progress towards its goal while also leaving the environment in a clean state" (https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents). EVIDENCE-BASED
- Prefer restart over correction spirals; two failed fixes on one issue is the restart signal. EVIDENCE-BASED
- Gather context agentically first (grep-style search) before layering semantic search; it is more transparent and maintainable. EVIDENCE-BASED
- Re-check harness assumptions per model generation; automatic compaction on newer models can replace manual reset machinery. EVIDENCE-BASED
- In this vault, mirror the pattern: hot.md is the compacted state, log.md is the append-only history, index.md is the retrieval map. PRACTITIONER

## Pitfalls

- Compacting when you should restart; a polluted session summarized is still polluted.
- Relying on compaction for multi-window projects; without persistent artifacts the agent loses the plot between windows.
- Letting subagent transcripts flow back raw into the orchestrator; request summaries, keep isolation.
- Carrying harness workarounds (sprint decomposition, forced resets) onto model generations that no longer need them; the machinery itself then wastes context.
- Compacting away the verification trail; progress claims must stay auditable against tool results.

## Sources

- Effective context engineering for AI agents, Anthropic Engineering: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (published 2025-09-29, retrieved 2026-07-07)
- Effective harnesses for long-running agents, Anthropic Engineering: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents (published 2025-11-26, retrieved 2026-07-07)
- Harness design for long-running application development, Anthropic Engineering: https://www.anthropic.com/engineering/harness-design-long-running-apps (published 2026-03-24, retrieved 2026-07-07)
- Best practices for Claude Code, official docs: https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)

## Related

- [[Context Window Management]] because this routine is the operational half of that concept.
- [[Claude Memory System]] because product memory persists what compaction would otherwise discard.
- [[Claude Code Subagents]] because subagent isolation is the cheapest form of compaction.
- [[Claude Code Project Memory]] because every-session facts belong there, not in the transcript.
- [[Prompt Caching Economics]] because compaction changes cache hit patterns and cost.
- [[Extended Thinking Budgets]] because thinking output competes for the same attention budget.
- [[Explore Plan Code Commit]] because /clear boundaries align with that loop's task boundaries.
- [[Multi-Agent Fan-Out Research Flow]] because fan-out is compaction by parallel context isolation.
- [[Past Chats Tools]] because retrieval from past conversations is just-in-time context.
- [[Claude Code]] because /clear, subagents, and auto memory are its concrete controls.

## Next actions

- Define this vault's compaction contract: what hot.md must always carry after a working session.
- Add a progress-file template (goal, done, next, blockers) for any run expected to exceed one window.
- Test automatic compaction behavior on a long Fable 5 session and note where manual notes still win.

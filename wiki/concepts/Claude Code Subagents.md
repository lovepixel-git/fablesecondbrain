---
type: concept
title: "Claude Code Subagents"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/harness/claude-code
  - note/concept
domain: claude-code-harness
confidence: evidence-based
related:
  - "[[Claude Code]]"
  - "[[Multi-Agent Fan-Out Research Flow]]"
  - "[[Context Window Management]]"
  - "[[Claude Code Hooks]]"
  - "[[Agent Skills System]]"
  - "[[Plan Mode and Permission Modes]]"
  - "[[Claude Code Project Memory]]"
  - "[[Claude Agent SDK]]"
  - "[[Model Selection for Agent Workloads]]"
source_urls:
  - "https://code.claude.com/docs/en/sub-agents (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)"
  - "https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026 (retrieved 2026-07-07)"
---

# Claude Code Subagents

Subagents are Markdown-defined workers that each run in their own context window, so research, review, and verification stop consuming the main conversation's budget.

## What it is

A custom subagent is a Markdown file with YAML frontmatter stored in `.claude/agents/` for project scope or `~/.claude/agents/` for user scope. The frontmatter fields are name, description, tools, and model, so each agent can be scoped to a narrow toolset and pinned to a fit-for-purpose model. The docs state the isolation property directly: "Each subagent runs in its own context window with a custom system prompt" (https://code.claude.com/docs/en/sub-agents).

Claude Code also ships built-in Explore, Plan, and general-purpose subagents and delegates to them automatically, so delegation happens even with zero custom agents defined.

## How it works

- The main session dispatches a task; the subagent works in a separate context with its own system prompt and returns results, keeping intermediate reading out of the parent transcript.
- Tool scoping in frontmatter limits what a subagent may touch; a read-only reviewer simply gets no edit tools.
- The model field lets heavy reasoning agents and cheap scanning agents coexist; see [[Model Selection for Agent Workloads]].
- As of v2.1.198 the /agents creation wizard is removed; the official path is asking Claude to write the agent file or editing it directly.
- Official best practice uses a fresh-context verification subagent as one way to gate work harder, alongside Stop hooks (https://code.claude.com/docs/en/best-practices).
- Subagents implement half of the official context-management practice: run /clear between unrelated tasks and delegate scoped investigation so the parent transcript stays small (https://code.claude.com/docs/en/best-practices).
- Plugins can bundle agent definitions alongside skills, hooks, and MCP servers, so a team's reviewer and verifier agents are distributable (https://code.claude.com/docs/en/plugins).

> [!key-insight] The docs' restart rule extends to delegation: "A clean session with a better prompt almost always outperforms a long session" (https://code.claude.com/docs/en/best-practices). A fresh subagent context is that clean session in miniature.

## Best practice

- Delegate scoped investigation to subagents so the main context stays reserved for requirements, decisions, and integration. EVIDENCE-BASED
- Use a fresh-context verification subagent to check completed work, since it judges the diff without the parent's accumulated bias. EVIDENCE-BASED
- Isolate research and review in subagent contexts as the default pattern for context hygiene. PRACTITIONER
- Prototype fan-out batch runs on 2 or 3 files before scaling to the whole tree. PRACTITIONER
- Keep each agent's description precise about when it applies; delegation quality follows description quality. PRACTITIONER
- Ask subagents for summaries, not raw output, so results land small in the parent context. PRACTITIONER
- After roughly two failed corrections on one issue, restart with a better prompt instead of continuing to correct in place. EVIDENCE-BASED
- Give reviewer agents narrow, read-oriented toolsets so their verdicts stay independent of their ability to change the code. PRACTITIONER

## Pitfalls

- Expecting the /agents wizard: it is gone as of v2.1.198; write the file or ask Claude to.
- Giving every agent every tool, which forfeits the safety value of tool scoping.
- Treating the subagent's context as shared: it does not see the parent conversation, so the dispatch prompt must carry all needed facts.
- Over-delegating trivial work; a subagent round trip costs more than a direct call for one-line answers.
- Scaling a fan-out before prototyping it; batch mistakes multiply across every file the batch touches.
- Letting subagent output dump raw file contents into the parent, which recreates the pollution delegation was meant to prevent.

> [!gap] The verified pack does not document subagent concurrency limits, dispatch depth (whether subagents can spawn subagents), or exact context inheritance rules beyond the separate-window property. Verify against https://code.claude.com/docs/en/sub-agents before designing deep hierarchies.

## Sources

- Create custom subagents, official docs, https://code.claude.com/docs/en/sub-agents (retrieved 2026-07-07).
- Best practices for Claude Code, official docs, https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07).
- Claude Code Advanced Best Practices, SmartScope, https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026 (published 2026-07-06, retrieved 2026-07-07).

## Related

- [[Claude Code]] is the host harness that dispatches and supervises subagents.
- [[Multi-Agent Fan-Out Research Flow]] is the vault's operational recipe built on this feature.
- [[Context Window Management]] explains the budget pressure subagents relieve.
- [[Claude Code Hooks]] can pair a Stop hook with a verifier subagent for hard gates.
- [[Agent Skills System]] lets plugins bundle agent definitions alongside skills.
- [[Plan Mode and Permission Modes]] includes a built-in Plan subagent for research.
- [[Claude Code Project Memory]] stays lean when investigation happens in child contexts.
- [[Claude Agent SDK]] exposes comparable agent-building primitives programmatically.
- [[Model Selection for Agent Workloads]] guides the per-agent model field.
- [[Headless Claude Code and CI]] runs fan-out as separate processes when in-session subagents are not enough.

## Next actions

- Write one read-only reviewer agent in .claude/agents/ with edit tools removed.
- Add a verification subagent to the main repo and wire it into the finish routine.
- Test a 3-file fan-out prototype before any large batch run.
- Close the concurrency and dispatch-depth gap from the official subagent docs.

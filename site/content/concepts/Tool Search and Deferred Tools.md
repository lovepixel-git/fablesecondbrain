---
type: concept
title: "Tool Search and Deferred Tools"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/tools
  - note/concept
domain: tools-and-skills
confidence: practitioner
related:
  - "[[Agent Skills System]]"
  - "[[Model Context Protocol]]"
  - "[[Writing Effective Tools for Agents]]"
  - "[[Context Window Management]]"
  - "[[Tool Search Behavior Probe]]"
  - "[[Connector and MCP App Suggestions]]"
  - "[[Claude Code]]"
  - "[[Prompt Caching Economics]]"
source_urls:
  - "https://www.anthropic.com/engineering/code-execution-with-mcp (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/mcp (retrieved 2026-07-07)"
---

# Tool Search and Deferred Tools

Deferred tool loading exists for context economy: keep tool definitions out of the context window until a task actually needs them, the same progressive-disclosure logic that governs skills.

## What it is

Deferred tools are the tool-schema application of a principle Anthropic applies across its agent stack: do not pay context for capability you are not using. Instead of loading every tool definition upfront, a harness exposes lightweight references and loads full schemas on demand, discovered via search when needed.

Two costs motivate the design: every always-loaded schema competes with task content on every turn, and connector growth multiplies that baseline across all sessions.

The verified evidence base for the rationale is strong. Skill metadata costs about 100 tokens until used; "Progressive disclosure ensures only relevant content occupies the context window at any given time" (https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview). For MCP tools, Anthropic's code-execution pattern reports "This reduces the token usage from 150,000 tokens to 2,000 tokens" (https://www.anthropic.com/engineering/code-execution-with-mcp), a 98.7 percent saving on one workload.

> [!gap] The verified claim packs document the context-economy rationale but not the concrete deferred-tool mechanism itself: how a harness lists deferred names, the search or selection syntax, or the failure mode when an unloaded tool is called. Empirical observations belong in [[Tool Search Behavior Probe]].

> [!gap] No verified public Anthropic URL in the current packs documents a first-party tool search API feature for Fable 5. Treat any specific parameter names or endpoint claims as unverified until [[Claim Verification Flow]] confirms them.

## How it works

- The general pattern: definitions stay summarized or absent until relevance is established, then load in full. Skills do this in three levels (metadata, body, bundled files).
- Anthropic's code-execution-with-MCP approach goes further: the agent calls MCP tools from code instead of holding every tool definition in context, and saved functions plus a SKILL.md form a structured skill (https://www.anthropic.com/engineering/code-execution-with-mcp).
- Output size is policed too: in Claude Code, MCP tool output over 10,000 tokens triggers a warning, configurable via MAX_MCP_OUTPUT_TOKENS (https://code.claude.com/docs/en/mcp).
- Large connector catalogs are the pressure source: each always-loaded schema competes with task context, so deferral scales the number of connectable tools without scaling baseline cost.
- Discovery is description-driven: the resident summary (a skill description, a tool name) is the only signal available when deciding what to load, so summaries carry the whole retrieval burden.

> [!key-insight] One rule spans skills, MCP code execution, and deferred schemas: resident context carries summaries, and demonstrated relevance triggers the full load.

## Best practice

- Prefer on-demand surfaces (skills, code-execution over MCP, deferred schemas) over always-loaded definitions when catalogs grow. EVIDENCE-BASED
- For workloads spanning many MCP tools, call them from code; Anthropic reports the 150,000 to 2,000 token reduction for this pattern. EVIDENCE-BASED
- Invest in dense, discovery-oriented names and descriptions, since summaries are all the model sees before loading. PRACTITIONER
- Cap tool output and tune MAX_MCP_OUTPUT_TOKENS so one verbose tool cannot flood the window. EVIDENCE-BASED
- Probe deferred-tool behavior empirically in each harness before building workflows that depend on it. PRACTITIONER
- Re-audit the resident summary layer whenever a connector is added, since deferral makes catalogs easier to grow than to review. PRACTITIONER

## Pitfalls

- Assuming deferral is free: discovery adds a search step, and a wrong description means the right tool is never found.
- Assuming identical behavior across harnesses; the mechanism is harness-specific and this vault has verified only the rationale, not per-harness mechanics.
- Trusting deferred catalogs blindly: MCP guidance warns to verify trust before connecting servers, and deferral makes the catalog easier to grow than to audit.
- Confusing deferral with output control; a deferred tool still returns arbitrarily large results unless capped.
- Writing vault notes about mechanics from memory; this topic is exactly where invented harness behavior would enter, which is why the gaps above stay open until probed.

## Sources

- Code execution with MCP, Anthropic Engineering, https://www.anthropic.com/engineering/code-execution-with-mcp (published 2025-11-04, retrieved 2026-07-07).
- Equipping agents for the real world with Agent Skills, Anthropic Engineering, https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (published 2025-10-16, retrieved 2026-07-07).
- Agent Skills overview, Claude Platform docs, https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview (retrieved 2026-07-07).
- Connect Claude Code to tools via MCP, Claude Code docs, https://code.claude.com/docs/en/mcp (retrieved 2026-07-07).

## Related

- [[Agent Skills System]] is the fully documented progressive-disclosure sibling.
- [[Model Context Protocol]] supplies the tool catalogs that make deferral necessary.
- [[Writing Effective Tools for Agents]] covers the description quality deferral depends on.
- [[Context Window Management]] frames the budget arithmetic behind the design.
- [[Tool Search Behavior Probe]] is where observed mechanics get recorded and tested.
- [[Connector and MCP App Suggestions]] shows the claude.ai surface for connector discovery.
- [[Claude Code]] enforces the MCP output warning and MAX_MCP_OUTPUT_TOKENS.
- [[Prompt Caching Economics]] interacts with what stays stable in the prompt prefix.
- [[Export Chapter Tool Schemas]] documents how the export renders tool definitions.
- [[Claim Verification Flow]] gates any new mechanic claims before they enter this note.

## Next actions

- Run the probes in [[Tool Search Behavior Probe]] and record per-harness mechanics.
- Measure baseline token cost of currently connected MCP servers in one session.
- Trial the code-execution pattern on one multi-tool MCP workload and compare tokens.
- Search for official Anthropic documentation of a tool search API and cite it if found.

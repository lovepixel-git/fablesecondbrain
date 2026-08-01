---
type: experiment
title: "Tool Search Behavior Probe"
status: seed
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/tools
  - note/experiment
domain: tools-and-skills
confidence: practitioner
related:
  - "[[Tool Search and Deferred Tools]]"
  - "[[Connector and MCP App Suggestions]]"
  - "[[Writing Effective Tools for Agents]]"
  - "[[Model Context Protocol]]"
  - "[[System Prompt Export 2026-07]]"
  - "[[Export Chapter Tool Schemas]]"
  - "[[Corpus Scope Decision]]"
  - "[[claude.ai Platform]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://www.anthropic.com/engineering/writing-tools-for-agents (retrieved 2026-07-07)"
  - "https://modelcontextprotocol.io/specification/latest (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Tool Search Behavior Probe

A designed, not yet run, probe testing whether deferred tools in the claude.ai harness stay name-only until a tool_search call loads their schemas, as the corpus plumbing implies.

## What it is

- An experiment design (status: seed) grounded in the corpus's deferred-tool plumbing: Google Calendar, Drive, and Gmail tools are listed name-only behind tool_search, and suggest_connectors is gated on a prior search_mcp_registry call with user opt-in for third-party MCP apps (System Prompt Export 2026-07, L2940-3283).
- The corpus attests the plumbing's existence, not its runtime behavior; this probe converts the static capture into falsifiable behavioral predictions.
- Scope is the claude.ai harness on a current Fable 5 session, per [[Corpus Scope Decision]]; results say nothing about other harnesses.

## How it works

### Hypotheses

- H1: a deferred tool cannot be invoked before its schema is loaded; a direct call attempt fails with a schema or validation error rather than executing.
- H2: when a task requires a deferred tool, the model reliably issues a tool_search call first, without user prompting.
- H3: suggest_connectors fires only after a search_mcp_registry call has occurred, matching the documented gating.

### Method (designed, not run)

1. In a live claude.ai session with Google connectors enabled, issue 10 tasks that each require one deferred tool (list calendar events, search Gmail threads, and similar).
2. For each task, record the full tool-call sequence and whether the first relevant call is a tool_search.
3. Run 5 adversarial variants instructing the model to call the deferred tool directly without searching, and record the failure mode verbatim.
4. Run 3 connector-suggestion tasks and record whether suggest_connectors ever precedes search_mcp_registry.
5. Log all transcripts with dates into the vault for citation.

### Measures

- Search-first rate across the 10 base tasks (H2 predicts near 100 percent).
- Direct-call outcome distribution: error type, recovery behavior, wasted turns (H1).
- Gating compliance count for suggest_connectors (H3 predicts zero violations).
- Overhead: extra turns and latency attributable to schema loading.

## Best practice

- Probe corpus plumbing claims behaviorally before building workflows on them; a capture proves presence, not behavior. PRACTITIONER
- Keep tool inventories high-signal regardless of loading mechanics; description quality is "by far the most important factor in tool performance." (https://www.anthropic.com/engineering/writing-tools-for-agents). EVIDENCE-BASED
- Measure prompt-level steering effects before trusting them in production, mirroring official prompting guidance on wording sensitivity. EVIDENCE-BASED
- Pin the harness and date in every probe log so results stay comparable across snapshots. PRACTITIONER

## Pitfalls

- Running the probe on the wrong surface: the corpus claims are claude.ai evidence, and tool loading may differ elsewhere.
- Harness drift: the corpus is a June 9, 2026 snapshot; the live harness may have changed plumbing since, so a failed prediction may mean drift, not a wrong reading.
- Conflating connector opt-in UX (a user consent step) with model-side gating when scoring H3.
- Small-N overconfidence: 10 base tasks bound the claim strength; report rates, not certainties.
- Deleting transcripts: without logged evidence the probe results cannot be cited under the vault's confidence rules.

## Sources

- System Prompt Export 2026-07, L2940-3283 (snapshot dated 2026-06-09, cited 2026-07-07).
- Writing effective tools for agents, with agents, https://www.anthropic.com/engineering/writing-tools-for-agents (retrieved 2026-07-07, published 2025-09-11).
- Model Context Protocol specification, https://modelcontextprotocol.io/specification/latest (retrieved 2026-07-07, revision 2025-11-25).

## Related

- [[Tool Search and Deferred Tools]] is the concept this probe stress-tests.
- [[Connector and MCP App Suggestions]] owns the suggest_connectors gating under H3.
- [[Writing Effective Tools for Agents]] supplies the description-quality baseline.
- [[Model Context Protocol]] defines the registry and server plumbing behind connectors.
- [[System Prompt Export 2026-07]] provides the L2940-3283 plumbing evidence.
- [[Export Chapter Tool Schemas]] catalogs the schemas whose deferral is at issue.
- [[Corpus Scope Decision]] confines the probe's conclusions to claude.ai.
- [[claude.ai Platform]] is the execution surface for the method.
- [[Claim Verification Flow]] will ingest the results into tagged claims.

## Next actions

- Schedule a live claude.ai session with Google connectors enabled to run the method.
- Pre-register the three hypotheses and thresholds in this note before the first run.
- After the run, promote status from seed and file results with dated transcripts.

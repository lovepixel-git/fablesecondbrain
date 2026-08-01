---
type: entity
title: "Anthropic API and Claude Platform"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/model
  - note/entity
domain: model-and-family
confidence: evidence-based
related:
  - "[[Claude Fable 5]]"
  - "[[Claude 5 Model Family]]"
  - "[[Claude Console and API Platform]]"
  - "[[docs.claude.com]]"
  - "[[Anthropic]]"
  - "[[Claude Agent SDK]]"
  - "[[Fable 5 Pricing and Rate Limits]]"
  - "[[Prompt Caching Economics]]"
  - "[[Extended Thinking Budgets]]"
  - "[[Model Context Protocol]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Harness Refusal Handling]]"
  - "[[Fable Mythos 5 System Card]]"
source_urls:
  - "https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/migration-guide (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback (retrieved 2026-07-07)"
  - "https://www.anthropic.com/claude/fable (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/building-effective-agents (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/agent-sdk/overview (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/managed-agents (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/writing-tools-for-agents (retrieved 2026-07-07)"
---

# Anthropic API and Claude Platform

The Anthropic API is the raw model surface beneath every Claude harness. For Fable 5 work, the current verified platform layer includes model IDs, 1M context and 128k output specs, adaptive thinking constraints, refusal and fallback semantics, Covered Model retention, and documented cloud availability.

## What it is

The API and its console are where developers call Claude models directly, without a harness. In Anthropic's documented build path it is the bottom rung, the Client SDK makes raw API calls, the [[Claude Agent SDK]] runs the agent loop in your own process, and Managed Agents is the hosted REST API for production (https://code.claude.com/docs/en/agent-sdk/overview). Platform-level developer documentation lives under platform.claude.com/docs, which is where the Agent Skills platform docs verified in this vault are hosted (https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

Anthropic's founding guidance for this surface is simplicity, "Maintain simplicity in your agent's design" (https://www.anthropic.com/engineering/building-effective-agents), start with direct LLM API calls and add agentic machinery only when it demonstrably improves outcomes. For Fable 5, the migration guide and models overview are mandatory checks because dateless post-4.6 model IDs are pinned snapshots rather than evergreen moving aliases.

## How it works

- **Direct calls first.** The API is the recommended starting point before any framework; workflows with predefined code paths are distinguished from agents that direct their own tool use, and many production needs are met by the simpler workflow patterns (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer).
- **Current model IDs.** The official model pages verify claude-fable-5 and claude-mythos-5, alongside claude-opus-4-8, claude-sonnet-5, and claude-haiku-4-5-20251001. Treat them as pinned snapshots.
- **Fable 5 request constraints.** Fable 5 and Mythos 5 use adaptive thinking as the only thinking mode, expose thinking depth through effort, and reject unsupported manual thinking-budget or sampling controls documented for earlier models.
- **Refusal shape.** Fable 5 dual-use classifier refusals return HTTP 200 with stop_reason "refusal" and stop_details naming the category. A refusal before any output is not billed and does not count against rate limits.
- **Fallback paths.** Integrations can use server-side fallbacks, SDK refusal-fallback middleware, or manual retry with fallback credit to route refused Fable 5 requests to Claude Opus 4.8.
- **Cloud availability.** Current Fable 5 sources verify availability on the Claude API, Claude Platform on AWS, Amazon Bedrock, Google Cloud, and Microsoft Foundry; Mythos 5 remains restricted to approved Project Glasswing customers.
- **Tools at the API level.** Anthropic's tool guidance applies here, build a few consolidated, workflow-targeted tools rather than wrapping every endpoint, namespace related tools, and return high-signal token-efficient responses, because "Agents are only as effective as the tools we give them" (https://www.anthropic.com/engineering/writing-tools-for-agents, 2025-09-11).
- **Hosted production tier.** Managed Agents virtualizes an agent into session, harness, and sandbox behind a REST API, giving the platform a hosted top rung above raw calls (https://www.anthropic.com/engineering/managed-agents, 2026-04-08).

> [!gap] Endpoints and request shape. The claim packs do not verify the current Messages API endpoint paths, versioning headers, or streaming event format. Pull these from docs.claude.com or platform.claude.com before writing integration code.

## Best practice

- Start integrations with direct API calls and the simplest workflow pattern that works; add agents only when dynamic tool direction demonstrably pays for itself. EVIDENCE-BASED
- Design API-level tools as consolidated workflow tools with token-efficient responses, and refine descriptions through evaluation rather than intuition. EVIDENCE-BASED
- Treat the context window as a finite attention budget in every API integration, curating for the smallest high-signal token set. EVIDENCE-BASED
- Verify endpoint paths, version headers, and streaming events against live official docs at integration time; those request-shape details remain outside this note. PRACTITIONER
- Branch on stop_reason refusal in application code; HTTP status alone is insufficient for Fable 5. EVIDENCE-BASED
- Choose a fallback path deliberately and log fallback billing separately from Fable 5 billing. EVIDENCE-BASED
- Prototype agent behavior locally, Agent SDK, before committing to the hosted Managed Agents tier. EVIDENCE-BASED
- Route pricing and rate limit questions to [[Fable 5 Pricing and Rate Limits]] rather than answering from memory. PRACTITIONER

## Pitfalls

- Answering endpoint path or streaming-event questions from this note; those remain explicit gaps.
- Wrapping every upstream API endpoint as a separate tool, which bloats context and degrades agent performance.
- Skipping the workflow-versus-agent decision and defaulting to agents, paying token and latency costs without outcome gains.
- Assuming platform.claude.com and docs.claude.com carry identical content; this vault has verified only specific pages on each.
- Treating claude.ai model switching as identical to API fallback; the API exposes stop_reason refusal and explicit fallback configuration, while app surfaces can switch models in the conversation.

## Sources

- Agent Skills, Claude Platform Docs, https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview (retrieved 2026-07-07)
- Models overview, Claude Platform Docs, https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)
- Introducing Claude Fable 5 and Claude Mythos 5, Claude Platform Docs, https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)
- Model migration guide, Claude Platform Docs, https://platform.claude.com/docs/en/about-claude/models/migration-guide (retrieved 2026-07-07)
- Refusals and fallback, Claude Platform Docs, https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback (retrieved 2026-07-07)
- Claude Fable, Anthropic, https://www.anthropic.com/claude/fable (retrieved 2026-07-07)
- Building Effective Agents, Anthropic Engineering, https://www.anthropic.com/engineering/building-effective-agents (published 2024-12-19, retrieved 2026-07-07)
- Agent SDK overview, Claude Code docs, https://code.claude.com/docs/en/agent-sdk/overview (retrieved 2026-07-07)
- Scaling Managed Agents, Anthropic Engineering, https://www.anthropic.com/engineering/managed-agents (published 2026-04-08, retrieved 2026-07-07)
- Writing effective tools for agents, with agents, Anthropic Engineering, https://www.anthropic.com/engineering/writing-tools-for-agents (published 2025-09-11, retrieved 2026-07-07)
- Effective context engineering for AI agents, https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (published 2025-09-29, retrieved 2026-07-07)

## Related

- [[Claude Fable 5]], the model this API serves.
- [[Claude 5 Model Family]], the full lineup addressable through this surface.
- [[Claude Console and API Platform]], the platform hub page for this surface.
- [[docs.claude.com]], the documentation root for verifying the gaps above.
- [[Anthropic]], the vendor operating the API and console.
- [[Claude Agent SDK]], the next rung up the documented build path.
- [[Fable 5 Pricing and Rate Limits]], the owning note for cost and limit questions.
- [[Prompt Caching Economics]], API-level cost lever for repeated context.
- [[Extended Thinking Budgets]], API-level reasoning budget control.
- [[Model Context Protocol]], the tool connectivity standard adjacent to this surface.
- [[Fable 5 Dual-Use Safety Measures]], the refusal and fallback layer API callers must handle.
- [[Harness Refusal Handling]], the app-level prose refusal layer that differs from API semantics.
- [[Fable Mythos 5 System Card]], the public evaluation evidence now available for this model family.

## Next actions

- Capture the Messages API reference (endpoints, headers, streaming) with retrieval dates and close the endpoint gap.
- Re-check the migration guide before every production model migration.
- Add request and response code examples once endpoint references are captured.

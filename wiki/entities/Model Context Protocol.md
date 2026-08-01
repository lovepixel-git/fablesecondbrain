---
type: entity
title: "Model Context Protocol"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/tools
  - note/entity
domain: tools-and-skills
confidence: evidence-based
related:
  - "[[Claude Code]]"
  - "[[Connector and MCP App Suggestions]]"
  - "[[Tool Search and Deferred Tools]]"
  - "[[Writing Effective Tools for Agents]]"
  - "[[Agent Skills System]]"
  - "[[Claude Agent SDK]]"
  - "[[Anthropic API and Claude Platform]]"
  - "[[Memory Injection Resistance]]"
  - "[[Sandbox Network and Filesystem Model]]"
  - "[[claude.ai Platform]]"
source_urls:
  - "https://modelcontextprotocol.io/specification/latest (retrieved 2026-07-07)"
  - "https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/mcp (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/code-execution-with-mcp (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (retrieved 2026-07-07)"
  - "https://github.com/modelcontextprotocol/servers (retrieved 2026-07-07)"
---

# Model Context Protocol

MCP is an open JSON-RPC 2.0 protocol, current specification revision 2025-11-25, that standardizes how agents reach external tools and data through hosts, clients, and servers, and Claude Code consumes it over stdio, HTTP, SSE, and WebSocket transports with explicit trust warnings.

## What it is

"MCP provides a standardized way to connect LLMs with the context they need" (https://modelcontextprotocol.io/specification/latest). The architecture has three roles, hosts, clients, and servers. Servers offer resources, prompts, and tools; clients may offer sampling, roots, and elicitation back to servers. The spec's trust principles require explicit user consent for all data access and tool invocation, and hosts must not transmit resource data elsewhere without consent.

The steering group maintains the modelcontextprotocol/servers repository with seven actively maintained reference servers (Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking, Time) intended as demonstrations rather than production deployments, with twelve former servers archived and the MCP Registry as the browseable catalog. This vault marks that inventory CONTESTED pending re-verification.

MCP and skills are complementary, MCP connects agents to external tools and data while [[Agent Skills System]] encodes procedural knowledge, including workflows that use those external tools.

## How it works

- **Wire protocol.** JSON-RPC 2.0 between host, client, and server; revision 2025-11-25 is current.
- **Claude Code transports.** stdio, HTTP (recommended for remote servers, streamable-http accepted as an alias), SSE, and WebSocket; "The SSE (Server-Sent Events) transport is deprecated." (https://code.claude.com/docs/en/mcp).
- **Claude Code scopes.** Local scope is the default, stored in ~/.claude.json; project scope is .mcp.json checked into version control; user scope is account-wide. Project-scoped servers stay pending approval until the user trusts the workspace, and /mcp handles OAuth 2.0 for remote servers.
- **Output limits.** MCP tool output over 10,000 tokens triggers a warning, configurable via MAX_MCP_OUTPUT_TOKENS.
- **Code execution pattern.** Anthropic's code-execution approach has agents call MCP tools from code instead of loading every tool schema into context; one workload dropped from 150,000 tokens to 2,000 tokens, a 98.7 percent saving, and saved functions plus a SKILL.md form a structured skill (https://www.anthropic.com/engineering/code-execution-with-mcp, 2025-11-04).
- **Security model.** The spec's security document catalogs attack classes with normative mitigations, confused deputy in OAuth proxy servers (per-client consent required), SSRF via OAuth metadata discovery (enforce HTTPS, block private IP ranges), session hijacking ("MCP servers MUST use secure, non-deterministic session IDs." bound to user identity), local server compromise (show the exact command and require consent), and OAuth URL injection (allow only http and https schemes, never open URLs via shell) (https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

> [!gap] How claude.ai consumes MCP (connectors, remote server directory, per-plan availability) is not covered by this vault's assigned packs; see [[Connector and MCP App Suggestions]] and source before asserting.

## Best practice

- "Verify you trust each server before connecting it." (https://code.claude.com/docs/en/mcp); servers that fetch external content create prompt injection risk. EVIDENCE-BASED
- Prefer the HTTP transport for remote servers and migrate off deprecated SSE configs. EVIDENCE-BASED
- Treat tool descriptions and annotations as untrusted unless they come from a trusted server, per the spec's own direction to implementors. EVIDENCE-BASED
- Never build servers that accept passthrough tokens; "MCP Servers MUST NOT use sessions for authentication." and authorization-enabled servers MUST verify all inbound requests. EVIDENCE-BASED
- For tool-heavy workloads, adopt the code-execution pattern, calling MCP tools from code, to collapse context cost by orders of magnitude. EVIDENCE-BASED
- Apply general tool design discipline to MCP servers, few consolidated workflow tools, namespacing, token-efficient responses, description refinement through evals. EVIDENCE-BASED
- Check .mcp.json into version control for team-shared project servers, and keep personal experiments at local scope. PRACTITIONER

## Pitfalls

- Connecting fetch-capable servers casually; fetched content can carry injected instructions that redirect tool use or exfiltrate data.
- Treating the seven reference servers as production software; the repo describes them as reference implementations, and this vault holds the claim as contested anyway.
- Forgetting that "Tools represent arbitrary code execution and must be treated with appropriate caution." (https://modelcontextprotocol.io/specification/latest).
- Letting a server return unbounded output; the 10,000 token warning exists because oversized tool results wreck the context budget.
- Assuming project .mcp.json servers activate on clone; they stay pending until the workspace is trusted.
- Building OAuth proxy servers without per-client consent, the textbook confused deputy setup the spec forbids.

## Sources

- Model Context Protocol Specification, revision 2025-11-25, https://modelcontextprotocol.io/specification/latest (published 2025-11-25, retrieved 2026-07-07)
- MCP Security Best Practices, https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices (published 2025-11-25, retrieved 2026-07-07)
- Connect Claude Code to tools via MCP, official docs, https://code.claude.com/docs/en/mcp (retrieved 2026-07-07)
- Code execution with MCP, Anthropic Engineering, https://www.anthropic.com/engineering/code-execution-with-mcp (published 2025-11-04, retrieved 2026-07-07)
- Equipping agents for the real world with Agent Skills, https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (published 2025-10-16, retrieved 2026-07-07)
- modelcontextprotocol/servers repository, https://github.com/modelcontextprotocol/servers (retrieved 2026-07-07)
- Writing effective tools for agents, with agents, https://www.anthropic.com/engineering/writing-tools-for-agents (published 2025-09-11, retrieved 2026-07-07)

## Related

- [[Claude Code]], the harness whose MCP consumption is best verified here.
- [[Connector and MCP App Suggestions]], the claude.ai-side connector behavior note.
- [[Tool Search and Deferred Tools]], the context-saving counterpart to loading full schemas.
- [[Writing Effective Tools for Agents]], design guidance every MCP server should follow.
- [[Agent Skills System]], the complementary procedural knowledge layer.
- [[Claude Agent SDK]], harnesses built on it consume MCP the same way.
- [[Anthropic API and Claude Platform]], the platform surface adjacent to MCP connectivity.
- [[Memory Injection Resistance]], defense posture against injected instructions from tools.
- [[Sandbox Network and Filesystem Model]], the execution environment MCP servers run against.
- [[claude.ai Platform]], the consumer surface whose MCP story is still a gap here.

## Next actions

- Re-verify the reference server inventory against the servers repo README and resolve the contested tag.
- Source claude.ai connector documentation to close the consumer-surface gap.
- Audit DA's configured MCP servers against the spec's security best practices, especially fetch-capable ones.

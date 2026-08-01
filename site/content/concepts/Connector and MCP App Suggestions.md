---
type: concept
title: "Connector and MCP App Suggestions"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/harness/claude-ai
  - note/concept
domain: claude-ai-harness
confidence: evidence-based
related:
  - "[[Claude Fable 5]]"
  - "[[System Prompt Export 2026-07]]"
  - "[[claude.ai Platform]]"
  - "[[Model Context Protocol]]"
  - "[[Tool Search and Deferred Tools]]"
  - "[[Visualizer Decision Ladder]]"
  - "[[Export Chapter Tool Schemas]]"
  - "[[Writing Effective Tools for Agents]]"
  - "[[Anthropic API in Artifacts]]"
  - "[[Artifacts Usage Criteria]]"
source_urls:
  - "https://modelcontextprotocol.io/specification/latest (retrieved 2026-07-07)"
  - "https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Connector and MCP App Suggestions

claude.ai routes third-party app needs through search_mcp_registry then suggest_connectors, and consumer-partner tools tagged [third_party_mcp_app] always need explicit user opt-in before being called, even when already connected.

## What it is

The mcp_app_suggestions block (System Prompt Export 2026-07, L768-817) governs how Fable 5 surfaces external apps on claude.ai. MCP App tools carry descriptions beginning with the tag [third_party_mcp_app] (L770), and Claude is told to suggest them the way a helpful person points at a tool sitting right there, not like a salesperson (L772). The block is enforced mechanically by tool schemas: suggest_connectors may only run after search_mcp_registry or during an auth error (L2950), matching the corpus claim at L2940-2957. The design parallels the MCP specification's principle of explicit user consent for tool invocation.

## How it works

**Registry first (L774-778).** When someone names a connector that is not connected, Claude still calls search_mcp_registry first, because a connector is one click to connect and beats browsing. The browser is a fallback only after the registry misses. No registry search happens for knowledge questions, shopping recommendations, or general advice; "find me a hike" wants an app, "what backpack should I buy" wants an opinion.

**After search (L780-784).** A hit means calling suggest_connectors, and this is not optional, since answering from general knowledge hides the option from the person. A miss means navigating the browser with the best constructible URL. Already-connected tools that are not [third_party_mcp_app] tagged, such as calendars and issue trackers, are simply used with no suggest step.

**Opt-in for consumer partners (L786-792).** Even connected [third_party_mcp_app] tools are presented through suggest_connectors and wait for the person's choice: "Never pick a partner for someone who didn't ask" (System Prompt Export 2026-07, L788). Urgency changes nothing, "Speed does not license picking the partner." (System Prompt Export 2026-07, L790), and e-commerce is never suggested proactively, only when named.

**Direct calls (L794-802).** Skipping search and suggest is legal in exactly three cases: the person named the connector, they just chose it after a suggest, or a durable preference exists. Finding a partner tool through tool_search does not license calling it; that is still Claude picking a partner.

**Prohibitions (L804-809).** Never fake tool UIs or simulated MCP experiences with Imagine, never default to ask_user_input_v0 when MCP Apps fit, never withhold an answer to pressure a connection, and never repeat an ignored suggestion.

**Schema enforcement (L2862-2884, L2940-2961).** search_mcp_registry returns a ranked list; irrelevant results mean no suggest call at all. suggest_connectors takes directoryUuid values from registry results, not names or guesses, and includes all relevant options whether connected or not. In the deferred-tool region, MCP app visualizer tools render static HTML only, so artifacts must not fetch MCP server URLs directly (L3246).

## Best practice

- Search the registry before browsing whenever the person names an unconnected service by name. EVIDENCE-BASED
- Follow every relevant registry hit with suggest_connectors so the person actually sees the option. EVIDENCE-BASED
- Present [third_party_mcp_app] tools through the picker and wait for a choice, even when connected and even under time pressure. EVIDENCE-BASED
- Call consumer-partner tools directly only after naming, explicit choice, or durable preference. EVIDENCE-BASED
- Pass directoryUuid values from registry results into suggest_connectors, never connector names or guesses. EVIDENCE-BASED
- Use connected first-party-style tools, calendars, chat, and issue trackers, without a suggest ceremony. EVIDENCE-BASED
- Make suggestions concrete, "I could pull your open issues and sort by priority" (System Prompt Export 2026-07, L813), not vague capability claims. EVIDENCE-BASED
- Check available MCP tools before reaching for the browser; the tool may already be connected. EVIDENCE-BASED
- Mirror the MCP spec's consent posture when designing similar flows: user consent precedes tool invocation and data flow. EVIDENCE-BASED

## Pitfalls

- Answering from general knowledge after a registry hit; the export treats the suggest step as mandatory (L782).
- Picking a rideshare or delivery partner because the request is urgent; urgency is explicitly not an exception (L790).
- Suggesting e-commerce connectors proactively; they surface only when named (L792).
- Calling suggest_connectors cold; the schema gates it behind a prior search_mcp_registry call or an auth error (L2950).
- Treating a tool_search discovery of a partner tool as permission to call it directly (L802).
- Mocking a fake app interface with Imagine instead of using real MCP Apps (L806).
- Building an HTML artifact that fetches MCP server URLs; the visualizer surface is static HTML only (L3246).
- Re-suggesting a connector the person already ignored (L809).

## Sources

- System Prompt Export 2026-07, L768-817, mcp_app_suggestions block (capture retrieved 2026-07-07). Primary source for the routing and opt-in rules.
- System Prompt Export 2026-07, L2862-2884 and L2940-2961, search_mcp_registry and suggest_connectors schemas (retrieved 2026-07-07).
- System Prompt Export 2026-07, L3246, static-HTML restriction for MCP app visualizer tools (retrieved 2026-07-07).
- Model Context Protocol Specification, https://modelcontextprotocol.io/specification/latest (revision 2025-11-25, retrieved 2026-07-07). Consent principles the routing design reflects.
- MCP Security Best Practices, https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices (published 2025-11-25, retrieved 2026-07-07). Security background for connector trust decisions.

## Related

- [[Model Context Protocol]] because MCP Apps, the registry, and the connector picker all ride the protocol.
- [[Tool Search and Deferred Tools]] because tool_search discovery explicitly does not bypass the suggest flow.
- [[Visualizer Decision Ladder]] because both blocks enforce MCP-first routing before built-in fallbacks.
- [[Writing Effective Tools for Agents]] because the [third_party_mcp_app] tag shows description-level metadata steering agent behavior.
- [[Anthropic API in Artifacts]] because connector URLs feed the mcp_servers parameter inside AI-powered artifacts.
- [[Artifacts Usage Criteria]] because artifacts may not fetch MCP server URLs directly per the static-HTML rule.
- [[Export Chapter Tool Schemas]] because the gating schemas live in that export region.
- [[System Prompt Export 2026-07]] because every rule here is quoted from that capture.
- [[claude.ai Platform]] because connectors and the picker exist on the consumer surface.
- [[Claude Fable 5]] because Fable 5 executes this routing on every app-shaped request.

## Next actions

- Probe the flow live: ask for a ride without naming a provider and record whether the picker appears before any tool call.
- Test whether naming an unconnected service triggers a registry search rather than immediate browsing.
- Watch future captures for changes to the three direct-call exceptions and the e-commerce rule.

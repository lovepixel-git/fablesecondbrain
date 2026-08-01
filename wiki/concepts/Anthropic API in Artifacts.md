---
type: concept
title: "Anthropic API in Artifacts"
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
  - "[[Anthropic API and Claude Platform]]"
  - "[[Model Context Protocol]]"
  - "[[Artifacts Usage Criteria]]"
  - "[[Artifact Persistent Storage API]]"
  - "[[Context Window Management]]"
  - "[[Export Chapter Artifacts API and Citations]]"
  - "[[Model Selection for Agent Workloads]]"
source_urls:
  - "https://modelcontextprotocol.io/specification/latest (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/code-execution-with-mcp (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Anthropic API in Artifacts

claude.ai artifacts can call the Anthropic /v1/messages endpoint directly with no API key, pinned to Sonnet 4 with max_tokens 1000, optionally passing an mcp_servers parameter and a web search tool, which the export calls "Claude in Claude" or "Claudeception".

## What it is

The anthropic_api_in_artifacts block (System Prompt Export 2026-07, L3407-3713) lets Fable 5 build AI-powered artifacts: HTML or React apps that themselves query Claude at runtime. The overview names the capability directly; users may call it "Claude in Claude", "Claudeception", or AI-powered apps (L3411). Authentication is invisible to the artifact: "The assistant should never pass in an API key, as this is handled already" (System Prompt Export 2026-07, L3417). The harness proxies and bills the calls, so artifact code just fetches https://api.anthropic.com/v1/messages.

## How it works

**Fixed call shape (L3419-3432).** The template POSTs JSON with model "claude-sonnet-4-20250514" annotated "Always use Sonnet 4", and max_tokens 1000 annotated as already handled, so both values are constants regardless of the Fable 5 model running the conversation. Responses land in data.content as a mix of block types: text, tool_use, tool_result, image, and document (L3437-3448).

**Structured output (L3453-3459).** For dynamic UI data, the artifact's system prompt must demand JSON only, with no preamble and no Markdown backticks, and the client must parse defensively.

**MCP servers (L3463-3538).** Calls may include an mcp_servers array of {type: "url", url, name} objects so artifacts can act on external services. Available URLs come from the user's connectors; this capture embeds Google Drive, Gmail, Google Calendar, Canva, and Figma server URLs (L3482). Response handling filters blocks by type, never by position: text, mcp_tool_use, and mcp_tool_result blocks are extracted with filters, and tool results are parsed as JSON with a plain-text fallback (L3484-3534). See [[Model Context Protocol]] for the underlying protocol.

**Web search (L3540-3566).** Adding {"type": "web_search_20250305", "name": "web_search"} to tools gives the embedded model live search; MCP and web search combine for complex workflows.

**Files (L3584-3634).** PDFs and images enter messages as base64 blocks with correct media_type, using document and image content types.

**State (L3636-3685).** The context_window_management section warns "Claude has no memory between completions. Always include all relevant state in each request." (System Prompt Export 2026-07, L3638). Multi-turn artifacts resend full conversation history; games and apps serialize complete state into each prompt and ask for JSON deltas back.

**Errors and UI (L3687-3711).** API calls sit in try-catch, JSON code fences are stripped before parsing, and React artifacts never use HTML form tags, only onClick and onChange handlers.

> [!key-insight]
> The embedded model is pinned to a May 2025 Sonnet 4 string even though Fable 5 runs the conversation, so Claudeception apps are one model generation behind their author by design in this capture.

## Best practice

- Never inject or request an API key inside artifact code; the harness authenticates every /v1/messages call. EVIDENCE-BASED
- Hardcode model "claude-sonnet-4-20250514" and max_tokens 1000 exactly as templated. EVIDENCE-BASED
- Extract response data by filtering data.content on block type, never by array position. EVIDENCE-BASED
- Pass mcp_servers entries only for services the user is actually connected to, taking URLs from the embedded connector list. EVIDENCE-BASED
- For structured output, demand JSON-only responses in the call's system prompt, then strip code fences and parse inside try-catch. EVIDENCE-BASED
- Resend full conversation history or full serialized app state on every call, since completions share no memory. EVIDENCE-BASED
- Use onClick and onChange handlers instead of form tags in React artifacts. EVIDENCE-BASED
- Combine window.storage persistence with Claudeception calls for stateful AI apps, storing state between sessions and inlining it into prompts. PRACTITIONER
- Design for the 1000-token response ceiling: chunk long generations into multiple calls. PRACTITIONER

## Pitfalls

- Reading data.content[0].text and assuming the first block is the answer; MCP responses interleave block types (L3492-3513).
- Parsing MCP tool results with regex instead of JSON.parse with a text fallback (L3515-3534).
- Expecting the embedded model to remember the previous fetch; every completion is stateless (L3638).
- Passing an mcp_servers URL for a service the user never connected; only connector-backed URLs are available (L3482).
- Forgetting to strip ```json fences before JSON.parse, which throws on fenced output (L3689-3700).
- Upgrading the model string to a Fable 5 identifier; the capture pins Sonnet 4 and the proxy expectation may break otherwise.
- Confusing this proxied capability with direct [[Anthropic API and Claude Platform]] access; billing, auth, and limits are the harness's, not the user's key.

## Sources

- System Prompt Export 2026-07, L3407-3713, anthropic_api_in_artifacts block (capture retrieved 2026-07-07). Primary source for call shape, MCP usage, files, state, and error rules.
- System Prompt Export 2026-07, L3482, embedded connector MCP server list (retrieved 2026-07-07).
- Model Context Protocol Specification, https://modelcontextprotocol.io/specification/latest (revision 2025-11-25, retrieved 2026-07-07). Protocol background for the mcp_servers parameter.
- Code execution with MCP, https://www.anthropic.com/engineering/code-execution-with-mcp (published 2025-11-04, retrieved 2026-07-07). Related engineering pattern of calling MCP tools from code.

## Related

- [[Artifacts Usage Criteria]] because Claudeception apps must still satisfy the base artifact rules, including the form-tag ban's React context.
- [[Artifact Persistent Storage API]] because window.storage supplies the persistence that stateless completions lack.
- [[Model Context Protocol]] because the mcp_servers parameter runs MCP tool calls inside the API request.
- [[Anthropic API and Claude Platform]] because the artifact endpoint mirrors the public /v1/messages API with proxied auth.
- [[Context Window Management]] because resend-all-state is a context strategy imposed by statelessness.
- [[Model Selection for Agent Workloads]] because the Sonnet 4 pin is a deliberate model-selection decision worth tracking.
- [[System Prompt Export 2026-07]] because every constant here is quoted from that capture.
- [[claude.ai Platform]] because the proxy, billing, and connector list exist only on the consumer surface.
- [[Export Chapter Artifacts API and Citations]] because that chapter note maps this export region.
- [[Claude Fable 5]] because Fable 5 authors the artifacts that embed the older model.

## Next actions

- Build a minimal Claudeception artifact and confirm the Sonnet 4 pin and 1000-token cap behave as documented.
- Test an mcp_servers call against a connected Google Calendar and record the block-type sequence returned.
- Watch future captures for the pinned model string changing to a Claude 5 family identifier.

---
type: source
title: "Export Chapter Tool Schemas"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/tools
  - note/source
domain: tools-and-skills
confidence: evidence-based
source_type: primary
source_ref: "[[System Prompt Export 2026-07]]"
related:
  - "[[System Prompt Export 2026-07]]"
  - "[[Tool Search and Deferred Tools]]"
  - "[[Writing Effective Tools for Agents]]"
  - "[[Past Chats Tools]]"
  - "[[Connector and MCP App Suggestions]]"
  - "[[Visualizer Decision Ladder]]"
  - "[[Export Chapter Computer Use and Search]]"
  - "[[Export Chapter Artifacts API and Citations]]"
  - "[[Tool Search Behavior Probe]]"
source_urls:
  - "https://www.anthropic.com/news/claude-fable-5-mythos-5 (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Export Chapter Tool Schemas

Lines 1693-3405 of the export define 24 inline tools in JSONSchema, from computer use through consumer widgets to MCP plumbing, then re-anchor Claude's identity as Anthropic's consumer chat surface before the userMemories placeholder.

## What it is

This note digests the fourth chapter of the [[System Prompt Export 2026-07]], spanning L1693-3405. After the invocation syntax (L1693-1709) comes the declaration "Here are the functions available in JSONSchema format" (System Prompt Export 2026-07, L1711), then 24 tool definitions, a deferred-tools directory, and the closing identity block (L3395-3405).

## How it works

The 24 tools by group, with schema line refs and notable details:

- Computer use: bash_tool (L1792) and create_file (L1850) both require a description parameter explaining why; create_file fails on existing paths (L1852). str_replace (L2903) demands a unique old_str, warns that prior view output goes stale after each edit, and lists five read-only mounts (L2905). view (L2980) lists directories two levels deep and truncates files over 16,000 characters from the middle (L3024). present_files (L2549) exposes container files to the user, most relevant path first (L2568).
- Retrieval: web_search (L3214) takes a bare query. web_fetch (L3083) fetches only exact URLs given by the user or returned by prior search or fetch calls (L3086), and its schema carries allowed/blocked domain lists, an is_zdr Zero Data Retention flag (L3144-3147), a 100-per-hour rate limit key (L3198), and a dark-launch flag (L3177). image_search (L1943) returns 3-5 images. conversation_search (L1819) caps at 10 results; recent_chats (L2594) caps n at 20 with before/after pagination.
- Consumer widgets: ask_user_input_v0 (L1713) renders 1-3 questions with 2-4 tappable options as single_select, multi_select, or rank_priorities, and calling it ends the turn: "After calling this, your turn is done" (System Prompt Export 2026-07, L1738). fetch_sports_data (L1882) spans a 20-league enum from nfl to cricket and mma with SportRadar game IDs; verbatim: "PREFER using this tool over web search for data, scores, stats" (System Prompt Export 2026-07, L1884). weather_fetch (L3036) picks units by home location. places_search (L2462) batches 1-10 queries with location bias; places_map_display_v0 (L2167) renders results. recipe_display_v0 (L2652) scales servings via 4-character ingredient IDs. message_compose_v1 (L2046) drafts email, text, or other messages as labeled strategy variants. recommend_claude_apps (L2826) suggests from a 10-app enum spanning desktop, mobile, Claude Code variants, Excel, PowerPoint, and Chrome (L2838-2849).
- MCP plumbing: search_mcp_registry (L2862) searches connectors by keyword, for named products and bare intents alike. suggest_connectors (L2940) renders a picker, requires directoryUuid values from a prior registry search or an auth error, and ends the turn (L2950-2957). tool_search (L3238) loads deferred tools; verbatim: "ALL tools listed below are deferred" (System Prompt Export 2026-07, L3240), and calling one without loading fails.
- Memory: memory_user_edits (L1975) with view, add, remove, replace; control strings cap at maxLength 500 (L1998).
- Visualizer pair: visualize:read_me (L3312) loads one of seven design modules (diagram, mockup, interactive, data_viz, art, chart, elicitation) silently before visualize:show_widget (L3351), which auto-detects SVG versus HTML, exposes a global sendPrompt(text) hook (L3356), and demands 1-4 loading messages kept deliberately boring for serious topics (L3367).
- Deferred directory: Google Calendar (8 tools), Google Drive (8), and Gmail (12) are listed name-only behind tool_search (L3250-3282); parameter guessing is explicitly forbidden (L3242).
- Identity re-anchor: after the schemas, the prompt restates that Claude is created by Anthropic, the date is Tuesday, June 09, 2026, and the surface is claude.ai or the Claude app, then opens the userMemories placeholder (L3395-3405).

Schema conventions worth noting across the set: every mutating computer tool (bash_tool, create_file, str_replace, view) requires a human-readable description or rationale parameter; create_file even fixes parameter ordering, description first and file_text last (L1860-1868). Consumer widgets encode product judgment directly in schema descriptions, such as show_widget demanding boring loading messages for serious topics (L3367) and snake_case disambiguating titles (L3376). Defaults are conservative: conversation_search returns 5 results, recent_chats returns 3, tool_search returns 5.

> [!contradiction]
> web_fetch exposes an is_zdr flag (L3144-3147), yet public docs designate Fable 5 a Covered Model with mandatory 30-day retention, not eligible for Zero Data Retention. The flag reads as a shared per-tool schema key, vestigial for this model. CONTESTED.

## Best practice

- Load deferred tools through tool_search before calling them and reuse the returned parameter names exactly; the export states unloaded calls fail (L3240-3242). EVIDENCE-BASED
- Treat turn-ending tools (ask_user_input_v0, suggest_connectors) as terminal: write the framing line, call, stop (L1738, L2957). EVIDENCE-BASED
- Follow the schema discipline visible here when designing your own tools: required description fields, enums over free text, and explicit caps. PRACTITIONER
- Prefer purpose-built widgets over web search where the export does (sports data at L1884, places, weather). EVIDENCE-BASED
- Cite tool behavior from schema lines, not tool names, since names recur across harnesses with different shapes. PRACTITIONER

## Pitfalls

- Guessing Gmail, Drive, or Calendar parameters from memory; the directory is name-only (L3242).
- Reading is_zdr as evidence Fable 5 sessions can run under ZDR; retention docs say otherwise.
- Continuing output after ask_user_input_v0 or suggest_connectors; the selection arrives as the next user message.
- Editing files straight from view output with line-number prefixes; the prefix is display-only (L2905, L2987).
- Assuming this 24-tool inventory exists in Claude Code; that harness ships a different toolset.

## Sources

- System Prompt Export 2026-07, L1693-3405 (captured 2026-07-07).
- https://www.anthropic.com/news/claude-fable-5-mythos-5 (product frame for the harness carrying these tools; retrieved 2026-07-07).
- ZDR contradiction resolution from the 2026-07-07 claim packs, see [[research-pack-2026-07-07|Research Pack 2026-07-07]] (2026-07-07).

## Related

- [[System Prompt Export 2026-07]] because this note digests its L1693-3405 span.
- [[Tool Search and Deferred Tools]] because the deferred directory at L3238-3283 grounds that note.
- [[Writing Effective Tools for Agents]] because these schemas are worked examples of Anthropic tool design.
- [[Past Chats Tools]] because conversation_search and recent_chats schemas live here.
- [[Connector and MCP App Suggestions]] because search_mcp_registry and suggest_connectors define the picker flow.
- [[Visualizer Decision Ladder]] because the visualize read_me and show_widget pair implements its final step.
- [[Export Chapter Computer Use and Search]] because chapter three sets the usage rules for these tools.
- [[Export Chapter Artifacts API and Citations]] because the next chapter begins at L3407.
- [[Tool Search Behavior Probe]] because the deferred-tool failure claim at L3240 is testable.

## Next actions

- Probe tool_search live: call a deferred Gmail tool unloaded and record the failure mode.
- Compare this 24-tool inventory against the next capture to track additions and removals.
- Document the widget-versus-web-search preference rules as a reusable routing table.
- Resolve the memory_user_edits 500-character schema cap against the 100000-character guide text noted in [[Export Chapter Memory and Preferences]].

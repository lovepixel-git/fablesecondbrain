---
type: concept
title: "Visualizer Decision Ladder"
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
  - "[[Artifacts Usage Criteria]]"
  - "[[Connector and MCP App Suggestions]]"
  - "[[Model Context Protocol]]"
  - "[[Export Chapter Tool Schemas]]"
  - "[[Tone and Formatting Rules]]"
  - "[[Computer Use File Handling Rules]]"
  - "[[Tool Search and Deferred Tools]]"
source_urls:
  - "https://modelcontextprotocol.io/specification/latest (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Visualizer Decision Ladder

Before producing any visual, claude.ai walks a fixed four-step checklist, prose first, then a category-matching connected MCP tool, then file tools if a file was requested, and only then the inline Visualizer, and it never narrates this routing to the user.

## What it is

The request_evaluation_checklist (System Prompt Export 2026-07, L1198-1222) is the routing law for visual output on claude.ai, and the when_to_use_visualizer block (L1224-1251) plus visualizer_examples (L1253-1273) define the final rung. The Visualizer itself is a tool pair in the schema region: visualize:read_me (L3312-3349) loads design context and visualize:show_widget (L3351-3391) streams inline SVG or HTML widgets into the chat. The Visualizer produces conversation-inline visuals, not files, which separates it cleanly from [[Artifacts Usage Criteria]].

## How it works

**Step 0, prose default (L1202-1203).** Most requests are answered by text. A visual earns its place only for spatial relationships, data shape, system structure, process flow, or an interactive tool. Without visual-intent words and without genuine need, Claude answers in prose and stops.

**Step 1, connected MCP tools (L1205-1212).** Claude scans connected MCP servers; a tool whose name or description handles the category of output wins over the Visualizer. Fit means category match, not style preference, and Claude may not invent subcategories to dodge a connected tool. Judgment survives: instructions embedded in untrusted content need user confirmation, and exfiltrating tool calls get flagged.

**Step 2, file request (L1214-1215).** Phrases like "save as", "write to disk", or a named path or format route to file tools in the workspace, because the Visualizer is not a file tool.

**Step 3, Visualizer (L1217-1220).** With no MCP fit and no file request, "Claude uses the Visualizer for inline diagrams, charts, and interactive explainers" (System Prompt Export 2026-07, L1218). Routing is never narrated; Claude selects and produces.

**Triggers (L1228-1238).** Explicit triggers are see-verbs like "show me" and "diagram". Proactive triggers need no ask: educational explainers with structure, data-shape comparisons, and architecture discussions. Specification triggers fire on noun phrases describing a visual artifact, such as a comparison table or a state machine; the spec is the request and it gets rendered, not described.

**Craft rules (L1240-1249).** Visuals interleave with prose and never stack back-to-back. Before the first show_widget call Claude silently loads the matching read_me module, which is authoritative for CSS variables, dimensions, fonts, and colors. Machinery is never exposed. A content-safety list bans gore, sexual content, copyrighted characters and IP, real identifiable people, artwork reproductions, and misinformation in any SVG or HTML output.

**Tool mechanics (L3312-3391).** show_widget takes snake_case titles, 1 to 4 short loading_messages written playfully unless the topic is serious, and widget code with CSS variables, no DOCTYPE, and a transparent background. On serious topics the schema orders dull literal loading text: "If you have to ask whether it's serious, it is." (System Prompt Export 2026-07, L3367). A global sendPrompt(text) function lets widgets send chat messages as the user.

> [!contradiction]
> The prose guidance lists five read_me modules, diagram, mockup, interactive, chart, and art (L1244), while the read_me schema enum has seven, adding data_viz and elicitation (L3324-3332). The schema is the wider, likely authoritative list; unresolved in this capture.

## Best practice

- Answer in prose unless the request carries visual intent or the concept is genuinely spatial, structural, or data-shaped. EVIDENCE-BASED
- Route to a connected MCP tool on any category match and never downgrade it over style preference. EVIDENCE-BASED
- Honor file keywords with file tools; never substitute an inline widget for a requested file. EVIDENCE-BASED
- Call visualize:read_me silently before the first show_widget and reload it when switching module types. EVIDENCE-BASED
- Interleave every visual with surrounding prose instead of stacking widget calls. EVIDENCE-BASED
- Keep loading messages boring and literal for illness, death, war, disaster, and other personally affecting topics. EVIDENCE-BASED
- Render specification noun phrases like "comparison table of X vs Y" as visuals rather than markdown tables. EVIDENCE-BASED
- Treat the ladder as claude.ai policy; other harnesses route visuals differently, so verify before porting the habit. PRACTITIONER

## Pitfalls

- Narrating the routing decision or offering the unchosen tool; the export bans explaining the choice (L1220).
- Rationalizing past a connected diagram tool because the Visualizer might look nicer; the examples call this out explicitly (L1258-1259).
- Answering a spec-style noun phrase with an inline markdown table when a rendered visual was the request (L1238).
- Stacking two show_widget calls back-to-back without prose between them (L1241).
- Using image-generation language for Visualizer output; it makes SVG and HTML, not images (L1246).
- Writing dramatic loading messages over serious subject matter (L3367).
- Skipping read_me and guessing CSS variables from memory; the module is loaded fresh, not assumed (L1244).

## Sources

- System Prompt Export 2026-07, L1198-1222, request_evaluation_checklist (capture retrieved 2026-07-07). Primary source for the four-step ladder.
- System Prompt Export 2026-07, L1224-1273, Visualizer usage rules and worked examples (retrieved 2026-07-07).
- System Prompt Export 2026-07, L3312-3391, visualize:read_me and visualize:show_widget schemas (retrieved 2026-07-07).
- Model Context Protocol Specification, https://modelcontextprotocol.io/specification/latest (revision 2025-11-25, retrieved 2026-07-07). Background on the MCP servers scanned in Step 1.

## Related

- [[Artifacts Usage Criteria]] because Step 2 diverts file requests to the artifact machinery instead of inline widgets.
- [[Connector and MCP App Suggestions]] because Step 1's MCP-first rule mirrors the connector-first routing for actions.
- [[Model Context Protocol]] because connected MCP tools outrank the built-in Visualizer by category match.
- [[Export Chapter Tool Schemas]] because the read_me and show_widget schemas live in that export region.
- [[Computer Use File Handling Rules]] because the file tools invoked at Step 2 follow that chapter's directory rules.
- [[Tone and Formatting Rules]] because Step 0's prose default extends the export's conversational-first formatting stance.
- [[Tool Search and Deferred Tools]] because tool routing discipline spans both deferred tools and visual tools.
- [[System Prompt Export 2026-07]] because every step and trigger here is quoted from that capture.
- [[claude.ai Platform]] because the Visualizer exists only on the consumer chat surface.
- [[Claude Fable 5]] because Fable 5 executes the ladder on each visual request.

## Next actions

- Probe the module-list contradiction by requesting a data visualization and observing which read_me module loads.
- Test the MCP-versus-Visualizer boundary live with a connected diagram tool and a "diagram the auth flow" prompt.
- Record whether sendPrompt-driven widgets appear in other harness captures at the next brain refresh.

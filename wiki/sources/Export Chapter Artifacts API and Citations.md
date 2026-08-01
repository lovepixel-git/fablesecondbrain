---
type: source
title: "Export Chapter Artifacts API and Citations"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/harness/claude-ai
  - note/source
domain: claude-ai-harness
confidence: evidence-based
source_type: primary
source_ref: "[[System Prompt Export 2026-07]]"
related:
  - "[[System Prompt Export 2026-07]]"
  - "[[Anthropic API in Artifacts]]"
  - "[[Citation Discipline]]"
  - "[[Agent Skills System]]"
  - "[[Sandbox Network and Filesystem Model]]"
  - "[[Model Context Protocol]]"
  - "[[Export Chapter Tool Schemas]]"
  - "[[Export Chapter Computer Use and Search]]"
  - "[[Claude Fable 5]]"
source_urls:
  - "https://api.anthropic.com/v1/messages (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Export Chapter Artifacts API and Citations

Lines 3407-3826 of the export let artifacts call the Anthropic API with harness-handled auth pinned to a Sonnet 4 snapshot, define cite-tag mechanics, inventory ten skills, and reveal a wildcard network allowlist, five read-only mounts, and thinking_mode auto.

## What it is

This note digests the final chapter of the [[System Prompt Export 2026-07]], spanning L3407-3826: `anthropic_api_in_artifacts`, `citation_instructions`, the user location line, the skills inventory, `network_configuration`, `filesystem_configuration`, the `thinking_mode` tag, and the start of the Human turn with a userPreferences placeholder.

## How it works

Claim list with line refs:

- Artifacts can call the standard /v1/messages endpoint directly, a capability users may call "Claude in Claude", "Claudeception", or AI-powered artifacts (L3411). Auth is invisible: "The assistant should never pass in an API key, as this is handled already" (System Prompt Export 2026-07, L3417).
- The example call pins model to claude-sonnet-4-20250514 with the comment to always use Sonnet 4, and fixes max_tokens at 1000 (L3426-3427), regardless of Fable 5 running the outer conversation.
- Responses return mixed content blocks (text, tool_use, tool_result, image, document) that must be filtered by type, never by position (L3437-3448, L3492-3513). Structured output is prompted as JSON-only with fences stripped before parsing (L3453-3457, L3689-3696).
- Artifact API calls accept an mcp_servers parameter, illustrated with Asana, Gmail, and Salesforce (L3464), and the prompt embeds the user's live connector list: Google Drive, Gmail, Google Calendar, Canva, and Figma (L3482). Web search is enabled inside artifacts via the web_search_20250305 tool type (L3548-3560), and MCP plus search can be combined (L3566).
- The artifact-side model is stateless between completions, so full history and complete application state must ride in every request (L3636-3681). React artifacts must never use HTML form tags, only event handlers (L3705-3709).
- Citations: every specific claim following from web_search results gets cite tags whose index encodes document and sentence spans, DOC_INDEX-START:END, comma-separated for multiple sections (L3719-3723), using the minimum sentences needed (L3725), and never citing document_context (L3727). Verbatim: "Claims must be in your own words, never exact quoted text" (System Prompt Export 2026-07, L3729).
- The user's approximate location (Reykjavík, Capital Region, IS in this capture) is injected in plain text (L3738).
- The skills inventory lists ten skills with filesystem locations: docx, pdf, pptx, xlsx, product-self-knowledge, frontend-design, file-reading, and pdf-reading under /mnt/skills/public, plus learn and skill-creator under /mnt/skills/examples (L3740-3791).
- product-self-knowledge overrides training memory for Anthropic product facts: "Any time you would otherwise rely on memory for Anthropic product details, verify here instead" (System Prompt Export 2026-07, L3757).
- Network config for bash_tool: Enabled true, Allowed Domains *, with an x-deny-reason header explaining egress failures (L3797-3801). Filesystem config mounts five directories read-only: /mnt/user-data/uploads, /mnt/transcripts, and the three /mnt/skills trees (L3807-3812).
- thinking_mode is set to auto (L3818), and the Human turn opens with a userPreferences placeholder (L3820-3826).

> [!contradiction]
> The pinned claude-sonnet-4-20250514 (L3426) is absent from the documented 2026-07-07 lineup (claude-fable-5, claude-mythos-5, claude-opus-4-8, claude-sonnet-5, claude-haiku-4-5). The pin may still be served but is stale relative to public docs, plausibly a deliberate cost and latency choice. CONTESTED.

> [!contradiction]
> The wildcard allowlist (L3799) sits in tension with public Claude Code sandbox guidance warning that broad allowlists enable exfiltration; the docs describe a different surface, so this is tension, not direct conflict. CONTESTED.

## Best practice

- Build AI-powered artifacts against /v1/messages with no key handling and type-filtered block parsing, exactly as specified (L3417, L3492-3513). EVIDENCE-BASED
- Pass full state in every artifact-internal API call; the inner model has no memory between completions (L3638). EVIDENCE-BASED
- Follow the paraphrase-only citation rule in any cited answer: cite tags grant attribution, not reproduction (L3729). EVIDENCE-BASED
- Route Anthropic product questions through product-self-knowledge style verification instead of model memory (L3756-3758). EVIDENCE-BASED
- Do not assume the Sonnet 4 pin performs like Fable 5; scope inner-model expectations to a small, cheap model. PRACTITIONER

## Pitfalls

- Passing an API key inside artifact code; the harness already injects auth (L3417).
- Raising max_tokens above 1000 expecting effect; the export fixes it (L3427).
- Reading data.content[0] positionally; block order is not guaranteed (L3492-3496).
- Citing sentences from document_context, which the rules exclude (L3727).
- Generalizing the wildcard egress allowlist to Claude Code, where sandbox policy differs.

## Sources

- System Prompt Export 2026-07, L3407-3826 (captured 2026-07-07).
- https://api.anthropic.com/v1/messages (endpoint named in the export at L3420; retrieved 2026-07-07).
- Model-pin and allowlist contradiction resolutions from the 2026-07-07 claim packs, see [[research-pack-2026-07-07|Research Pack 2026-07-07]] (2026-07-07).

## Related

- [[System Prompt Export 2026-07]] because this note digests its final chapter, L3407-3826.
- [[Anthropic API in Artifacts]] because the Claudeception capability at L3407-3482 is its source.
- [[Citation Discipline]] because cite-tag mechanics at L3715-3735 define that policy.
- [[Agent Skills System]] because the ten-skill inventory at L3740-3791 lists the installed skills.
- [[Sandbox Network and Filesystem Model]] because L3795-3816 gives the egress and mount configuration.
- [[Model Context Protocol]] because mcp_servers wiring at L3463-3482 embeds live MCP endpoints.
- [[Export Chapter Tool Schemas]] because the preceding chapter ends at the identity block L3395-3405.
- [[Export Chapter Computer Use and Search]] because artifact criteria there pair with the API here.
- [[Claude Fable 5]] because the outer model delegating to the pinned Sonnet 4 is Fable 5.

## Next actions

- Test whether the Sonnet 4 pin still resolves from a live artifact and log the response model.
- Re-capture after the next artifacts update; the mcp_servers connector list is per-user and volatile.
- Verify the wildcard egress claim by fetching a novel domain from bash_tool in a live session.

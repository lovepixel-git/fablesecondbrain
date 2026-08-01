---
type: source
title: "Export Chapter Computer Use and Search"
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
  - "[[Computer Use File Handling Rules]]"
  - "[[Artifacts Usage Criteria]]"
  - "[[Agent Skills System]]"
  - "[[Copyright Compliance Rules]]"
  - "[[Visualizer Decision Ladder]]"
  - "[[Export Chapter Memory and Preferences]]"
  - "[[Export Chapter Tool Schemas]]"
  - "[[Claude Fable 5]]"
source_urls:
  - "https://docs.claude.com (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Export Chapter Computer Use and Search

Lines 1027-1692 of the export mandate SKILL.md-first computer use, a three-directory file scheme, 20-line artifact thresholds, a visual-output routing checklist, effort-scaled search, and copyright hard limits of one sub-15-word quote per source.

## What it is

This note digests the third chapter of the [[System Prompt Export 2026-07]], spanning L1027-1692: `computer_use` (skills, file creation, file handling, outputs, sharing, artifact criteria, package management), the `request_evaluation_checklist` and Visualizer sections, `search_instructions` with `CRITICAL_COPYRIGHT_COMPLIANCE`, `harmful_content_safety`, and `using_image_search_tool`. It governs how the claude.ai harness produces files, visuals, and searched answers.

## How it works

Claim list with line refs:

- Skills are mandatory reading: "Reading the relevant SKILL.md is a required first step before writing any code" (System Prompt Export 2026-07, L1033), because skills encode environment constraints missing from training data; several may apply at once (L1031-1033). The check is unconditional, and task-to-skill mapping is spelled out: pptx, xlsx, docx, pdf (not pypdf), frontend-design (L1192).
- The computer is a Linux box (Ubuntu 24) with bash, str_replace, create_file, and view; the filesystem resets between tasks (L1067-1069).
- File locations: uploads at `/mnt/user-data/uploads`, scratch at the container scratch directory which users cannot see, and deliverables copied to `/mnt/user-data/outputs`, the only path users see (L1076-1079). Files under 100 lines are written in one call; longer builds go outline first (L1094-1095). Sharing requires present_files with no long postamble (L1102).
- Artifact thresholds: any code over 20 lines, standalone documents over 20 lines or 1500 characters, long-form creative writing, and reusable content become artifacts; lists, tables, and enumerated content never do, regardless of length (L1121-1136). Verbatim: "A standalone text-heavy document >20 lines or >1500 characters" (System Prompt Export 2026-07, L1128). Only .md, .html, .jsx, .mermaid, .svg, and .pdf render specially (L1140).
- React artifacts get a pinned library list (lucide-react 0.383.0, recharts, d3, three r128 with named geometry caveats, shadcn/ui, and more) and Tailwind core classes only (L1150-1160). HTML artifacts may import external scripts solely from cdnjs.cloudflare.com (L1147).
- Browser storage is banned: "NEVER use localStorage, sessionStorage, or ANY browser storage APIs in artifacts" (System Prompt Export 2026-07, L1163); state lives in React state or in-memory variables, with an explain-and-offer-alternative exception on explicit request (L1162-1164).
- Package management: npm works normally with globals under the container user npm-global directory; pip always needs `--break-system-packages` (L1172-1173).
- Visual output routing walks a fixed ladder: prose if no visual is needed (L1203), a category-matching connected MCP tool next, with subdividing categories to dodge a tool called out as rationalization (L1206-1208), file tools if a file was requested (L1214-1215), and the inline Visualizer last (L1217-1218). Routing is never narrated (L1220). Specification-style noun phrases like "comparison table" count as visual requests without any verb (L1238).
- Search scales with complexity: 1 call for single facts, 3-5 medium, 5-10 deeper, and 20-plus redirects to the Research feature (L1303). Queries stay 1-6 words with no operators (L1314-1318).
- The unrecognized entity rule makes search non-negotiable for any game, film, show, book, album, product, or event Claude cannot place, including opinion questions (L1299). Knowledge-cutoff disclaimers are banned as annoying (L1301).
- Copyright hard limits: "15+ words from any single source is a SEVERE VIOLATION" (System Prompt Export 2026-07, L1280), one quote per source maximum after which the source is closed (L1374-1377), and lyrics, poems, and haikus are never reproduced in any form (L1354). Displacive summaries over 30 words and structure-mirroring are also banned (L1356-1357).
- File-creation triggers separate standalone artifacts from conversational answers: a blog post, story, or article is always a file, while strategies, summaries, and outlines stay inline; tone and length do not change the bucket (L1059). Anything over 10 lines of code becomes a file (L1057), and docx is reserved for explicit Word requests because it costs far more time and tokens (L1061).
- Worked routing decisions at L1181-1187 show the boundary cases: attached-file summaries stay in conversation, knowledge questions take no tools, and web-search answers stay conversational without report-style headers (L1186).
- Harmful-content search rules ban citing extremist sources like the 88 Precepts and locating harmful archives (L1584-1585). Image search wants 3-6 word queries, 3-4 images, interleaved with prose, never ending a response (L1652-1658), with a long blocked-category list including copyrighted characters and celebrity photos (L1636-1646).

## Best practice

- Adopt SKILL.md-first as a general agent pattern: read the relevant skill before any file-producing step, even on familiar formats (L1031-1033). EVIDENCE-BASED
- Deliver files only through the outputs directory plus present_files; anything left in scratch is invisible to users (L1076-1113). EVIDENCE-BASED
- Apply the 20-line and 1500-character thresholds when deciding chat versus artifact in claude.ai-style UIs (L1121-1136). EVIDENCE-BASED
- Enforce the one-quote, sub-15-word rule in every derived document, including this vault, since it applies to artifacts too (L1279-1284). EVIDENCE-BASED
- Reuse the effort-scaling table (1, 3-5, 5-10, redirect at 20+) as a budget heuristic for your own research agents. PRACTITIONER

## Pitfalls

- Writing deliverables to the scratch directory and assuming the user sees them; only `/mnt/user-data/outputs` renders (L1079).
- Putting lists or tables in artifacts; the export forbids it at any length (L1133).
- Using localStorage in artifacts, which fails inside claude.ai (L1162-1163).
- Treating these copyright limits as legal advice; the export itself bars fair-use determinations (L1355).
- Assuming this chapter binds Claude Code; it describes the claude.ai container, a different surface.

## Sources

- System Prompt Export 2026-07, L1027-1692 (captured 2026-07-07).
- https://docs.claude.com (mandated product-docs search target per export L29; retrieved 2026-07-07).
- https://cdnjs.cloudflare.com (sole permitted external script host per export L1147; retrieved 2026-07-07).
- Claim-pack verification of thresholds and copyright limits, see [[research-pack-2026-07-07|Research Pack 2026-07-07]] (2026-07-07).

## Related

- [[System Prompt Export 2026-07]] because this note digests its L1027-1692 span.
- [[Computer Use File Handling Rules]] because the three-directory scheme at L1074-1089 is its source.
- [[Artifacts Usage Criteria]] because the 20-line and 1500-character thresholds live at L1117-1140.
- [[Agent Skills System]] because the SKILL.md-first mandate at L1031-1046 grounds that note.
- [[Copyright Compliance Rules]] because the hard limits at L1279-1385 define that policy.
- [[Visualizer Decision Ladder]] because the routing checklist at L1198-1222 is its source text.
- [[Export Chapter Memory and Preferences]] because the prior chapter ends at L1025.
- [[Export Chapter Tool Schemas]] because the tool definitions this chapter references start at L1693.
- [[Claude Fable 5]] because these rules describe Fable 5 operating the claude.ai computer.

## Next actions

- Verify the React library pin list against a live artifact session before relying on versions.
- Diff the copyright block against the next capture; its numbered limits are likely to move.
- Probe whether the Visualizer ladder holds when both an MCP diagram tool and a file request coexist.

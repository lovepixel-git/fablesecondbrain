---
type: concept
title: "Artifacts Usage Criteria"
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
  - "[[Artifact Persistent Storage API]]"
  - "[[Anthropic API in Artifacts]]"
  - "[[Visualizer Decision Ladder]]"
  - "[[Computer Use File Handling Rules]]"
  - "[[Export Chapter Artifacts API and Citations]]"
  - "[[Tone and Formatting Rules]]"
  - "[[Which Export Rules Bind Claude Code]]"
source_urls:
  - "https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Artifacts Usage Criteria

claude.ai promotes content to an artifact when it is standalone and reusable, meaning any code over 20 lines or a text-heavy document over 20 lines or 1500 characters, and it never uses artifacts for lists, tables, or enumerated content at any length.

## What it is

The artifact criteria are the claude.ai rules that decide whether Fable 5 answers inline in chat or writes a separate rendered file. In the July 2026 capture an artifact is defined concretely as a file written with the create_file tool into `/mnt/user-data/outputs`; when the file carries one of the recognized extensions it renders in the user interface (System Prompt Export 2026-07, L1117-1119). This is a file-based artifact model layered on the computer-use container, and the prompt explicitly bans emitting legacy `<artifact>` or `<antartifact>` tags in responses (L1166). The criteria describe the claude.ai harness only; [[Which Export Rules Bind Claude Code]] covers how far they transfer.

## How it works

**Positive criteria (L1121-1128).** Artifacts are used for custom code solving a specific user problem, data visualizations, algorithms, technical reference, any code snippet over 20 lines, content meant for use outside the conversation such as reports, articles, presentations, and blog posts, long-form creative writing, structured reference content users will save or follow, iterations on an existing artifact, and any "A standalone text-heavy document >20 lines or >1500 characters" (System Prompt Export 2026-07, L1128).

**Negative criteria (L1130-1136).** No artifact for code of 20 lines or fewer that answers a question, short creative writing, brief reference content or single recipes, short conversational prose, anything the user asked to keep short, and, hardest of all, "Lists, tables, enumerated content, regardless of length" (System Prompt Export 2026-07, L1133).

**Rendering formats (L1138-1140).** Artifacts are single files unless asked otherwise; HTML and React keep CSS and JS in the same file. Six extensions render specially: .md, .html, .jsx, .mermaid, .svg, and .pdf.

**Markdown discipline (L1142-1144).** Markdown files are for standalone written content; docx replaces markdown only when the user explicitly wants Word. Web search responses and research summaries stay conversational and must not become markdown files or adopt report-style headers, deferring to [[Tone and Formatting Rules]].

**React and HTML rules (L1146-1160).** HTML artifacts may import external scripts only from cdnjs.cloudflare.com. React components need a default export and no required props, and may use only Tailwind core utility classes because no compiler runs. The pinned library set includes lucide-react@0.383.0, recharts, mathjs, lodash, d3, plotly, three at r128 (no OrbitControls, no CapsuleGeometry), papaparse, SheetJS, shadcn/ui, chart.js, tone, mammoth, and tensorflow.

**Browser storage ban (L1162-1164).** The prompt orders "NEVER use localStorage, sessionStorage, or ANY browser storage APIs in artifacts" (System Prompt Export 2026-07, L1163) because they fail inside claude.ai. State lives in React state or in-memory JS variables; the sanctioned persistence path is [[Artifact Persistent Storage API]]. When a user explicitly asks for localStorage, Claude explains the failure and offers in-memory storage or copying the code out.

## Best practice

- Apply the 20-line and 1500-character thresholds mechanically; length, not perceived importance, decides artifact promotion. EVIDENCE-BASED
- Keep lists, tables, and enumerated content inline in chat no matter how long they grow. EVIDENCE-BASED
- Ship single-file artifacts with CSS and JS inlined unless the user asks for a multi-file layout. EVIDENCE-BASED
- In React artifacts, restrict styling to Tailwind core utility classes and import only the pinned library set at the documented versions. EVIDENCE-BASED
- Replace every localStorage or sessionStorage call with useState, useReducer, or plain JS objects, and reach for window.storage when persistence across sessions matters. EVIDENCE-BASED
- Choose .md for standalone prose and reserve docx for an explicit Word request or a formal deliverable signal. EVIDENCE-BASED
- When porting artifact code out of claude.ai, reintroduce a bundler and real storage APIs before deploying elsewhere. PRACTITIONER
- Treat the criteria as claude.ai-specific policy, not model behavior; verify against the harness in use before assuming they apply. PRACTITIONER

## Pitfalls

- Wrapping a long comparison table in an artifact; the export forbids artifacts for enumerated content regardless of length (L1133).
- Using localStorage because the pattern is idiomatic on the open web; the artifact silently fails in claude.ai (L1162-1164).
- Importing Tailwind classes that need the JIT compiler; only pre-defined base-stylesheet classes resolve (L1150).
- Using THREE.CapsuleGeometry or OrbitControls with the pinned three r128 build (L1151).
- Turning a web research answer into a .md report; the export keeps search responses conversational (L1143-1144).
- Emitting `<artifact>` or `<antartifact>` tags from older prompt eras; the current capture bans them outright (L1166).
- Assuming these thresholds bind Claude Code or the API; the capture documents claude.ai only.

## Sources

- System Prompt Export 2026-07, L1117-1168, artifact_usage_criteria block (capture retrieved 2026-07-07). Primary source for every criterion above.
- System Prompt Export 2026-07, L1119 and L1140, artifact definition and rendering extensions (retrieved 2026-07-07).
- Agent Skills overview, https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview (retrieved 2026-07-07). Background on the skills that gate file creation in the same chapter.
- Equipping agents for the real world with Agent Skills, https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (published 2025-10-16, retrieved 2026-07-07). Context on skill-encoded environment constraints.

## Related

- [[Artifact Persistent Storage API]] because window.storage is the only sanctioned persistence path once browser storage is banned.
- [[Anthropic API in Artifacts]] because AI-powered artifacts extend these same files with /v1/messages calls.
- [[Visualizer Decision Ladder]] because the routing checklist decides between inline visuals and artifact files.
- [[Computer Use File Handling Rules]] because artifacts are created through the same create_file and outputs-directory machinery.
- [[System Prompt Export 2026-07]] because the criteria are quoted directly from this capture.
- [[claude.ai Platform]] because the criteria apply to the consumer chat surface only.
- [[Tone and Formatting Rules]] because conversational answers must not adopt report structure even when long.
- [[Export Chapter Artifacts API and Citations]] because that chapter note maps the surrounding export region.
- [[Which Export Rules Bind Claude Code]] because artifact thresholds do not automatically transfer to other harnesses.
- [[Claude Fable 5]] because Fable 5 is the model executing these criteria in the capture.

## Next actions

- Probe the 20-line boundary live on claude.ai with 19, 20, and 21 line code answers and record where promotion flips.
- Test whether a very long requested table really stays inline and note any drift from L1133.
- Cross-check the pinned React library versions against a fresh capture at the next brain refresh.

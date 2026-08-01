---
type: meta
title: "Tag Taxonomy"
status: evergreen
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/best-practices
  - note/meta
domain: best-practices
confidence: evidence-based
related:
  - "[[CONVENTIONS]]"
  - "[[Start Here]]"
  - "[[index]]"
  - "[[overview]]"
  - "[[hot]]"
  - "[[log]]"
---

# Tag Taxonomy

Lowercase hierarchical tags only. Every note carries exactly one domain tag and one type tag; confidence tags are optional extras used in dashboards.

## Domain tags (exactly one per note, drives graph colors)

- `fable5/model` for model-and-family notes
- `fable5/harness/claude-ai` for claude.ai harness notes
- `fable5/harness/claude-code` for Claude Code harness notes
- `fable5/tools` for tools-and-skills notes
- `fable5/memory` for memory-and-context notes
- `fable5/communication` for communication-rules notes
- `fable5/safety` for safety-and-permissions notes
- `fable5/best-practices` for best-practices notes

## Type tags (exactly one per note)

`note/entity`, `note/concept`, `note/flow`, `note/source`, `note/platform`, `note/account`, `note/decision`, `note/deliverable`, `note/question`, `note/gap`, `note/experiment`, `note/meta`

## Confidence tags (optional, dashboard filters)

`confidence/evidence-based`, `confidence/practitioner`, `confidence/contested`, `confidence/folklore`

Graph color groups in `.obsidian/graph.json` key on the 8 domain tags. When a new domain emerges, add the tag here first, then the color group, then the notes.

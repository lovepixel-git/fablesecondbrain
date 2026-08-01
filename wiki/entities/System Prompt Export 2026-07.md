---
type: entity
title: "System Prompt Export 2026-07"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/harness/claude-ai
  - note/entity
domain: claude-ai-harness
confidence: evidence-based
related:
  - "[[Export Chapter Product and Behavior]]"
  - "[[Export Chapter Memory and Preferences]]"
  - "[[Export Chapter Computer Use and Search]]"
  - "[[Export Chapter Tool Schemas]]"
  - "[[Export Chapter Artifacts API and Citations]]"
  - "[[Which Export Rules Bind Claude Code]]"
  - "[[Export Omits Claude Code Harness]]"
  - "[[Corpus Scope Decision]]"
  - "[[Corpus Ingestion Flow]]"
  - "[[Confidence Tag Policy]]"
  - "[[Claude Fable 5]]"
source_urls:
  - "https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# System Prompt Export 2026-07

The System Prompt Export 2026-07 is this vault's primary corpus metadata: a 3826-line capture of the claude.ai consumer system prompt running Claude Fable 5, stored immutably in the private vault with sha256 prefix 48358a42, captured 2026-07-07, and citable only with line references. The raw capture is omitted from this public release.

## What it is

- A single private fixture file of 3826 lines, sha256 prefix 48358a42, captured 2026-07-07, with provenance metadata recorded per [[CONVENTIONS]].
- Its internal conversation date is pinned to Tuesday, June 09, 2026 (System Prompt Export 2026-07, L180-189), making the content a launch-day snapshot even though the capture date is 2026-07-07.
- It documents the claude.ai consumer harness for [[Claude Fable 5]]: identity, behavior rules, memory system, artifacts runtime, tool schemas, citations, skills, and sandbox configuration.
- The vault splits it into five chapter notes: [[Export Chapter Product and Behavior]], [[Export Chapter Memory and Preferences]], [[Export Chapter Computer Use and Search]], [[Export Chapter Tool Schemas]], and [[Export Chapter Artifacts API and Citations]].
- Immutability rule: files under .raw/ are never edited; any correction happens in wiki notes that cite the corpus, never in the corpus itself.

## How it works

- The capture opens with a budget declaration: a budget:token_budget block of "190000" tokens (System Prompt Export 2026-07, L1-7).
- Early identity content names Fable 5 "the first model in Anthropic's new Claude 5 family" (L13-19), the shared underlying model with Mythos 5 (L17), the model lineup (L21-23), and product surfaces including Claude Cowork and beta agents (L25-27).
- Behavior infrastructure follows: six runtime-injected reminder types (L144-152) and the knowledge cutoff plus pinned date (L180-189).
- Consumer memory rules span L195-276 with the memory_user_edits tool at L987-999; userPreferences rules sit at L846-873.
- Computer use and skills: SKILL.md-first rule (L1031-1046), container directory scheme (L1074-1089), artifact thresholds (L1117-1140), storage API (L692-703), copyright limits (L1279-1377), and search rules (L1296-1303).
- Tool schemas occupy the bulk: "Here are the functions available in JSONSchema format" (L1711-3392) defines 24 inline tools, with deferred Google Workspace tools listed name-only (L3238-3283).
- A closing block re-anchors identity on the consumer surface (L3395-3405), documents artifact API calls (L3407-3482), citation mechanics (L3715-3735), the ten-skill inventory (L3740-3791), and sandbox configuration with "Allowed Domains: *" (L3795-3816).

## What it can and cannot evidence

- It CAN evidence the claude.ai consumer harness as captured: per [[Confidence Tag Policy]], corpus-only claims are EVIDENCE-BASED primary sources with mandatory line references.
- It CANNOT evidence API behavior, the Claude Code harness (see [[Export Omits Claude Code Harness]]), other harness versions, or anything after the capture.
- It is already stale in places: the lineup names Sonnet 4.6 and omits Mythos 5, both superseded by current docs (see [[Claude 5 Model Family]]).

## Best practice

- Cite with line references formatted like L123-145 and name the claude.ai harness in every corpus-derived claim. EVIDENCE-BASED
- Treat each claim as evidence of that capture, not a universal guarantee across harnesses, accounts, or dates. EVIDENCE-BASED
- Keep verbatim quotes at 15 words or fewer, attributed as System Prompt Export 2026-07, L<start>-<end>. EVIDENCE-BASED
- Mark any export-versus-docs conflict CONTESTED with a contradiction callout in the owning note until a newer official source resolves it. EVIDENCE-BASED
- Prefer chapter notes for synthesis and reserve direct corpus reads for verification passes. PRACTITIONER

## Pitfalls

- Editing the raw file; any change breaks the sha256 48358a42 provenance chain in .raw/.manifest.json.
- Citing corpus content without a line reference; unreferenced claims fail [[Claim Verification Flow]].
- Generalizing consumer-harness rules to Claude Code or the API; see [[Which Export Rules Bind Claude Code]].
- Treating the pinned 2026-06-09 lineup as current; Sonnet 5 and Mythos 5 postdate or exceed it.
- Reading the 190000 token budget as the model's context window; the API default is 1M tokens.

## Sources

- System Prompt Export 2026-07, L1-7, L13-27, L144-152, L180-189 (captured 2026-07-07)
- System Prompt Export 2026-07, L195-276, L692-703, L846-873, L987-999 (captured 2026-07-07)
- System Prompt Export 2026-07, L1031-1046, L1074-1089, L1117-1140, L1279-1377 (captured 2026-07-07)
- System Prompt Export 2026-07, L1711-3392, L3395-3405, L3407-3482, L3715-3816 (captured 2026-07-07)
- Models overview (staleness cross-check), https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)
- Introducing Claude Fable 5 and Claude Mythos 5 (staleness cross-check), https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)

## Corroboration (verified 2026-07-07)

- OFFICIAL SUBSET: Anthropic publishes the Fable 5 claude.ai system prompt (claude_behavior core only, dated 2026-06-09) at https://platform.claude.com/docs/en/release-notes/system-prompts; this capture is a superset of it and nothing in the official text contradicts it. EVIDENCE-BASED
- COMMUNITY LINEAGE: the June 2026 community capture lineage, 1,585 lines with several mirrors, matches this capture's section set; this 3,826-line 2026-07-07 capture additionally carries full tool schemas and injected account blocks. See [[Public System Prompt Copies]] for the survey. PRACTITIONER
- Comparison rule: diff captures section-by-section, never by line count; line counts vary with tool schemas and injected blocks. EVIDENCE-BASED

## Related

- [[Export Chapter Product and Behavior]] - chapter covering identity, lineup, and behavior rules.
- [[Export Chapter Memory and Preferences]] - chapter covering the consumer memory system.
- [[Export Chapter Computer Use and Search]] - chapter covering container, skills, and search rules.
- [[Export Chapter Tool Schemas]] - chapter covering the 24-tool inline inventory.
- [[Export Chapter Artifacts API and Citations]] - chapter covering artifact API calls and cite tags.
- [[Which Export Rules Bind Claude Code]] - which captured rules carry over to Claude Code, if any.
- [[Export Omits Claude Code Harness]] - the key scope limit of this fixture.
- [[Corpus Scope Decision]] - why this capture is the vault's evidence boundary.
- [[Corpus Ingestion Flow]] - how the fixture entered .raw/ with its manifest.
- [[Confidence Tag Policy]] - how corpus-only claims are tagged and caveated.
- [[Claude Fable 5]] - the model this harness capture runs.

## Next actions

- Schedule a re-capture to detect drift from the 2026-06-09 pinned content, then diff against this fixture.
- Resolve the 190000 token budget question if docs ever document context provisioning for claude.ai.
- Audit chapter notes for line references that fall outside their chapter's range.

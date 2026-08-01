---
type: concept
title: "Computer Use File Handling Rules"
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
  - "[[Agent Skills System]]"
  - "[[Artifacts Usage Criteria]]"
  - "[[Sandbox Network and Filesystem Model]]"
  - "[[Export Chapter Computer Use and Search]]"
  - "[[Export Omits Claude Code Harness]]"
  - "[[Which Export Rules Bind Claude Code]]"
  - "[[Visualizer Decision Ladder]]"
source_urls:
  - "https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Computer Use File Handling Rules

claude.ai's computer-use container enforces a three-directory scheme, uploads in /mnt/user-data/uploads, scratch work in a hidden container directory which users never see, and deliverables copied to /mnt/user-data/outputs, with a mandatory SKILL.md read before any code or file work.

## What it is

The computer_use chapter (System Prompt Export 2026-07, L1027-1196) governs how Fable 5 uses its Linux computer on claude.ai: an Ubuntu 24 machine with bash, str_replace, create_file, and view tools, a hidden scratch working directory, and a filesystem that resets between tasks (L1067-1069). The chapter binds four things together: the skills mandate, file-location law, output strategy, and package management. Artifacts are downstream of these rules because an artifact is just a create_file write into the outputs directory per [[Artifacts Usage Criteria]].

## How it works

**Skills first (L1031-1046, L1190-1193).** "Reading the relevant SKILL.md is a required first step before writing any code" (System Prompt Export 2026-07, L1033). The check is unconditional: Claude scans available_skills and views every plausibly relevant SKILL.md because skills encode environment constraints such as available libraries, rendering quirks, and output paths that are absent from training data. The reminder block maps tasks explicitly: pptx for decks, xlsx for spreadsheets, docx for Word documents, pdf for PDFs (not pypdf), and frontend-design for any web UI. Public Agent Skills docs describe the same SKILL.md format and progressive disclosure model.

**Three directories (L1074-1089).** User uploads land at /mnt/user-data/uploads and every in-context file also exists there on disk. All new work starts in the hidden scratch directory, which users cannot see. Finished deliverables move to /mnt/user-data/outputs: "Copy completed files here; it's how the user sees Claude's work." (System Prompt Export 2026-07, L1079). Only final deliverables belong there, though simple single-file tasks under 100 lines may be written there directly.

**In-context versus on-disk (L1083-1085).** Some upload types (md, txt, html, csv, png, pdf) are already visible in context, so Claude decides whether computer access is needed at all: converting an image needs the computer, transcribing visible text does not.

**Output strategy (L1093-1096).** Files under 100 lines are created in one tool call straight into outputs. Longer files build iteratively, outline, then sections, then review, then a final copy to outputs, and long content almost always has a matching skill. Files must actually be created, not just displayed in chat.

**Sharing (L1100-1113).** Finished work is shared with present_files plus a succinct summary, files not folders, and no long postambles; without the outputs copy and the present_files call, users cannot access anything.

**Packages (L1170-1177).** npm works normally with globals in the container user npm-global directory. pip always takes --break-system-packages. Virtual environments are created for complex Python projects, and tool availability is verified before use.

**File-creation triggers (L1051-1061).** Standalone artifacts (blog posts, articles, stories) become files however casually requested; strategies, summaries, and outlines stay inline. docx costs far more time and tokens, so markdown or inline wins when in doubt.

## Best practice

- View every plausibly relevant SKILL.md before the first line of code, file, or bash work, without first judging whether the task needs it. EVIDENCE-BASED
- Draft in the hidden scratch directory and copy only final deliverables to /mnt/user-data/outputs. EVIDENCE-BASED
- End every file-producing task with a present_files call and a one-line summary, no postamble. EVIDENCE-BASED
- Write files under 100 lines in a single create_file call directly to outputs; build longer files iteratively. EVIDENCE-BASED
- Always pass --break-system-packages to pip and expect npm globals in the container user npm-global directory. EVIDENCE-BASED
- Answer questions about in-context uploads directly instead of reflexively reading them from disk. EVIDENCE-BASED
- Default to markdown or inline over docx unless the user clearly wants a Word deliverable. EVIDENCE-BASED
- Treat /mnt/user-data/uploads and the skills trees as read-only and copy files out before editing them. EVIDENCE-BASED
- Expect the filesystem to reset between tasks and never rely on scratch state surviving a session. PRACTITIONER

## Pitfalls

- Leaving the deliverable in the hidden scratch directory; users never see that directory, so the work is effectively lost (L1078-1079).
- Showing file content in chat without creating the file; the export marks actual creation as required (L1096).
- Editing an uploaded file in place under /mnt/user-data/uploads; the mount is read-only per the str_replace schema (L2905).
- Running pip install without --break-system-packages, which fails on this Ubuntu 24 image (L1173).
- Skipping the SKILL.md read on a familiar format; the mandate exists precisely because constraints are environment-specific (L1033).
- Sharing a folder or writing a long postamble after present_files (L1102).
- Assuming these paths exist in Claude Code; the capture documents the claude.ai container only, see [[Export Omits Claude Code Harness]].

## Sources

- System Prompt Export 2026-07, L1027-1196, computer_use chapter (capture retrieved 2026-07-07). Primary source for directories, strategy, sharing, and packages.
- System Prompt Export 2026-07, L2905, read-only mounts in the str_replace schema (retrieved 2026-07-07).
- Agent Skills overview, https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview (retrieved 2026-07-07). Public documentation of the SKILL.md format the mandate relies on.
- Equipping agents for the real world with Agent Skills, https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (published 2025-10-16, retrieved 2026-07-07). Rationale for skills encoding environment constraints.

## Related

- [[Agent Skills System]] because the SKILL.md-first mandate is this chapter's strongest rule.
- [[Artifacts Usage Criteria]] because artifacts are create_file writes into the outputs directory defined here.
- [[Sandbox Network and Filesystem Model]] because read-only mounts and network egress frame these directory rules.
- [[Visualizer Decision Ladder]] because Step 2 of the visual checklist hands file requests to these file tools.
- [[Export Chapter Computer Use and Search]] because that chapter note maps this export region in full.
- [[Which Export Rules Bind Claude Code]] because path and package rules here are harness-specific.
- [[Export Omits Claude Code Harness]] because the capture says nothing about Claude Code's own file model.
- [[System Prompt Export 2026-07]] because every path and rule here is quoted from that capture.
- [[claude.ai Platform]] because the container and directory scheme belong to the consumer surface.
- [[Claude Fable 5]] because Fable 5 operates the computer under these rules.

## Next actions

- Verify the under-100-line direct-write behavior live by requesting one short and one long file on claude.ai.
- Test whether pip without --break-system-packages actually fails in the current container and note the error.
- Compare this directory scheme against the Claude Code sandbox model and record differences in the harness notes.

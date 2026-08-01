---
type: question
title: "Which Export Rules Bind Claude Code"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/harness/claude-code
  - note/question
domain: claude-code-harness
confidence: practitioner
question: "Which rules in the System Prompt Export 2026-07, if any, also bind Claude Code sessions?"
answer_quality: draft
related:
  - "[[Corpus Scope Decision]]"
  - "[[Export Omits Claude Code Harness]]"
  - "[[System Prompt Export 2026-07]]"
  - "[[Claude Code]]"
  - "[[Claude Code Platform]]"
  - "[[claude.ai Platform]]"
  - "[[Copyright Compliance Rules]]"
  - "[[Citation Discipline]]"
  - "[[Sandbox Network and Filesystem Model]]"
  - "[[Claude Code Hooks]]"
source_urls:
  - "https://code.claude.com/docs/en/overview (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Which Export Rules Bind Claude Code

Unresolved: the export is a claude.ai capture, so none of its rules are proven to bind Claude Code, whose behavior is documented separately at code.claude.com.

## What it is

- An open question left behind by [[Corpus Scope Decision]]: the corpus contains rich behavioral rules, but every one of them is attested only for the claude.ai harness.
- Candidate rules whose reach is unknown include the copyright hard limits (quotes over 15 words as severe violations, one quote per source, absolute lyrics ban, System Prompt Export 2026-07, L1279-1377), citation mechanics (L3715-3735), search effort scaling and the unrecognized-entity search mandate (L180-189, L1296-1303), artifact usage thresholds (L1117-1140), and the six runtime-injected reminder types with the rule that reminders never reduce restrictions (L144-152).
- The question matters because operators reading the export may wrongly assume Claude Code enforces the same limits, or wrongly assume it enforces none of them.

## How it works

### What we know

- The corpus is a June 9, 2026 claude.ai consumer prompt snapshot; nothing in it describes the Claude Code harness (see [[Export Omits Claude Code Harness]]).
- Claude Code has its own documented rule surface: CLAUDE.md memory, permission modes, settings, hooks, subagents, and skills, canonical at code.claude.com after the 301/308 redirects (https://code.claude.com/docs/en/overview).
- The public Claude Code docs verified on 2026-07-07 do not republish the export's copyright, citation, search, or artifact rules, so no documented overlap is established.
- One concrete tension exists: the corpus shows claude.ai container egress with a wildcard domain allowlist (L1074-1089, L3795-3816), while public Claude Code sandbox guidance warns that broad allowlists enable exfiltration; the docs describe a different surface, so this is a divergence signal, not a contradiction.

### What remains unknown

- Whether shared policy layers (for example copyright limits) are injected into Claude Code sessions by a prompt we have never captured.
- Whether model-level training makes some export rules behave identically everywhere even without prompt text.

### What would resolve it

- A captured Claude Code system prompt of comparable fidelity to the claude.ai export.
- An official Anthropic statement mapping which policy layers are shared across harnesses.
- Behavioral probes: identical quote-length, citation, and artifact-threshold tasks run in both harnesses and diffed.

## Best practice

- Treat every export rule as claude.ai-only until a probe or capture proves otherwise. PRACTITIONER
- Source all Claude Code behavior claims from code.claude.com pages, which the redirect chain establishes as canonical (https://code.claude.com/docs/en/overview). EVIDENCE-BASED
- When writing cross-harness guidance, mark the harness on every claim, per [[Corpus Scope Decision]]. PRACTITIONER
- Design probes with per-rule falsifiable predictions instead of one vague "same rules" test. PRACTITIONER

## Pitfalls

- Assuming a rule as fundamental-sounding as the copyright quote limit must be universal; it is attested only at L1279-1377 of a claude.ai capture.
- Assuming the inverse, that Claude Code is unconstrained, because its docs are silent on content rules.
- Treating the sandbox allowlist tension as a contradiction; the two sources describe different surfaces.
- Letting this question rot: the corpus snapshot ages while Claude Code ships weekly, so the divergence only grows.

## Sources

- System Prompt Export 2026-07, L144-152, L180-189, L1074-1089, L1117-1140, L1279-1377, L3715-3735, L3795-3816 (snapshot dated 2026-06-09, cited 2026-07-07).
- Claude Code Overview, https://code.claude.com/docs/en/overview (retrieved 2026-07-07).
- Best practices for Claude Code, https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07).

## Related

- [[Corpus Scope Decision]] draws the scope boundary that generates this question.
- [[Export Omits Claude Code Harness]] is the gap register entry behind the missing capture.
- [[System Prompt Export 2026-07]] holds every rule whose reach is in question.
- [[Claude Code]] is the harness whose binding rules are unknown.
- [[Claude Code Platform]] describes the documented rule surface we do have.
- [[claude.ai Platform]] is the surface the export rules provably bind.
- [[Copyright Compliance Rules]] is the highest-stakes candidate rule set.
- [[Citation Discipline]] is another candidate rule set attested only on claude.ai.
- [[Sandbox Network and Filesystem Model]] holds the allowlist divergence detail.
- [[Claude Code Hooks]] shows how operators can impose equivalent rules locally regardless.

## Next actions

- Design the cross-harness quote-length probe (pairs with [[Tool Search Behavior Probe]] methodology).
- Watch code.claude.com docs for any content-policy page that would document overlap.
- Upgrade answer_quality past draft once one probe has run in both harnesses.

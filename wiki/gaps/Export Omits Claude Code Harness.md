---
type: gap
title: "Export Omits Claude Code Harness"
status: developing
created: 2026-07-07
updated: 2026-07-09
tags:
  - fable5/harness/claude-code
  - note/gap
domain: claude-code-harness
confidence: evidence-based
related:
  - "[[System Prompt Export 2026-07]]"
  - "[[Corpus Scope Decision]]"
  - "[[Which Export Rules Bind Claude Code]]"
  - "[[Claude Code]]"
  - "[[Claude Code Platform]]"
  - "[[claude.ai Platform]]"
  - "[[Export Chapter Product and Behavior]]"
  - "[[Export Chapter Tool Schemas]]"
  - "[[Claude Code Quickstart for Fable 5]]"
source_urls:
  - "https://code.claude.com/docs/en/overview (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)"
  - "https://github.com/anthropics/claude-code (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Export Omits Claude Code Harness

The System Prompt Export 2026-07 contains no Claude Code system prompt, tool schemas, or harness rules, so every Claude Code claim in this vault rests on web documentation, never on the corpus.

> [!gap]
> The corpus covers claude.ai only. There is no captured Claude Code system prompt of comparable fidelity, which means the vault's primary-source evidence class (rule 1 of the confidence policy) is unavailable for the entire claude-code-harness domain. All Claude Code claims are corroborated instead through code.claude.com documentation and dated practitioner posts.

## What it is

- A gap register entry documenting the corpus's coverage boundary.
- Positive evidence of the boundary: the corpus inventory is consumer-shaped end to end, including a 24-tool inline harness inventory of consumer widgets (System Prompt Export 2026-07, L1711-3392), the claude.ai container layout with /mnt/user-data paths (L1074-1089), consumer memory mechanics (L195-276), the claude.ai skills surface under /mnt/skills (L3740-3791), and an identity block restating the June 09, 2026 date (L3395-3405). None of it describes the Claude Code harness.
- Further consumer-only inventory reinforces the boundary: deferred-tool plumbing behind tool_search (L2940-3283), userPreferences application rules (L846-873), and the artifact usage thresholds (L1117-1140) all belong to the claude.ai surface.
- The complementary decision, [[Corpus Scope Decision]], turns this observation into a binding tagging rule.

## How it works

- Consequence for evidence classes: claude.ai notes can cite primary capture lines; Claude Code notes cite only rule 2 sources, chiefly code.claude.com pages, whose canonical status is established by the 301 redirects from docs.claude.com and the 308 redirect from the former engineering best-practices post (https://code.claude.com/docs/en/overview).
- Consequence for open questions: whether export rules (copyright, citation, search, artifacts) bind Claude Code is undecidable from current evidence; tracked in [[Which Export Rules Bind Claude Code]].
- Consequence for freshness: Claude Code documentation reflects a fast release train (auto memory default since v2.1.59, auto mode v2.1.83+, /agents wizard removed v2.1.198), while the corpus is frozen at June 9, 2026, so the two evidence pools age at different speeds.
- Consequence for tooling notes: tool_search and deferred-tool claims are claude.ai evidence, so Claude Code tool behavior must be sourced from its own documentation pages.
- Consequence for automation notes: the documented non-interactive surface (claude -p, --bare) exists only in web sources, so [[Headless Claude Code and CI]] carries no primary capture either.
- The gap does not lower confidence on documented Claude Code claims; rule 2 evidence remains EVIDENCE-BASED. Only the primary capture class is missing.
- The gap closes only with a Claude Code prompt capture or an official publication of its system prompt and tool schemas.

## Best practice

- Never cite corpus line references for Claude Code behavior; use code.claude.com pages with retrieval dates. PRACTITIONER
- Record Claude Code version numbers (v2.1.59, v2.1.83, v2.1.198) alongside claims, since docs describe a moving target. PRACTITIONER
- Treat practitioner posts on Claude Code as rule 3 sources unless they cite official docs, then verify the doc directly. PRACTITIONER
- Revisit this gap at every brain refresh; a public prompt capture would reshape the whole claude-code-harness domain. PRACTITIONER
- Mirror the corpus-side chapter structure when a Claude Code capture arrives so the two harnesses stay comparable note-for-note. PRACTITIONER

## Pitfalls

- Silently borrowing claude.ai container facts (uploads, outputs, /mnt paths) into Claude Code notes; the surfaces differ.
- Assuming the corpus omission means Claude Code has no system prompt; it means we have not captured one.
- Citing the GitHub repository as behavioral documentation; it anchors the project but the docs pages carry the behavior claims.
- Forgetting that the wildcard egress allowlist detail (L3795-3816) is claude.ai evidence, despite its relevance to Claude Code sandbox debates.
- Citing the claude.ai skills surface under /mnt/skills as evidence about Claude Code skills; the two skill systems are documented separately.
- Treating this gap as permanent; harness prompts change, and a future export may include Claude Code, so this register entry carries a standing watch duty.

## Sources

- System Prompt Export 2026-07, L195-276, L1074-1089, L1711-3392, L3395-3405, L3740-3791 (snapshot dated 2026-06-09, cited 2026-07-07).
- Claude Code Overview, https://code.claude.com/docs/en/overview (retrieved 2026-07-07).
- Best practices for Claude Code, https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07).
- anthropics/claude-code repository, https://github.com/anthropics/claude-code (retrieved 2026-07-07).

## Partial fill available (found 2026-07-07)

- The Claude Code prompt fragments are publicly extracted per release at link omitted for public release (v2.1.202, 2026-07-06, 515+ prompt strings including a Fable 5 model identity fragment). Ingesting a pinned release into .raw/ via the [[Corpus Ingestion Flow]] would close most of this gap; until then the gap stands. PRACTITIONER

## Related

- [[System Prompt Export 2026-07]] is the corpus whose boundary this entry records.
- [[Corpus Scope Decision]] converts the boundary into a tagging rule.
- [[Which Export Rules Bind Claude Code]] is the open question the boundary creates.
- [[Claude Code]] is the harness left without primary-source coverage.
- [[Claude Code Platform]] collects the documentation-based coverage we do have.
- [[claude.ai Platform]] is the surface the corpus fully describes.
- [[Export Chapter Product and Behavior]] shows the consumer-shaped content inventory.
- [[Export Chapter Tool Schemas]] details corpus tool schemas, all claude.ai-side.
- [[Claude Code Quickstart for Fable 5]] is a downstream deliverable built entirely on web sources.
- [[Headless Claude Code and CI]] is another documentation-only coverage area this gap affects.

## Next actions

- Watch for any credible Claude Code system prompt capture and ingest it as a new corpus.
- Add version-number fields to claude-code-harness notes at the next lint pass.
- Re-check the docs redirect chain at the next brain refresh to confirm canonical status.

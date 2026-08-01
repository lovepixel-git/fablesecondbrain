---
type: source
title: "Public System Prompt Copies"
status: developing
created: 2026-07-07
updated: 2026-07-09
tags:
  - fable5/harness/claude-ai
  - note/source
domain: claude-ai-harness
confidence: evidence-based
related:
  - "[[System Prompt Export 2026-07]]"
  - "[[Claude Fable 5]]"
  - "[[Anthropic]]"
  - "[[Export Omits Claude Code Harness]]"
  - "[[Corpus Scope Decision]]"
  - "[[Corpus Ingestion Flow]]"
  - "[[Brain Refresh Flow]]"
  - "[[Confidence Tag Policy]]"
  - "[[claude.ai Platform]]"
  - "[[Claude Code Platform]]"
  - "[[research-pack-2026-07-07|Research Pack 2026-07-07]]"
source_urls:
  - "https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07)"
  - "link omitted for public release (retrieved 2026-07-07)"
  - "AlphaSignal analysis, link omitted for public release (retrieved 2026-07-07)"
  - "Horia Stan analysis, link omitted for public release (retrieved 2026-07-07)"
  - "Community mirror, gist, and repository-search links omitted for public release (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Public System Prompt Copies

Every known public copy of the Fable 5 system prompt, official and community, corroborates this vault's 3,826-line capture of 2026-07-07, and nothing found online contradicts it (web and GitHub survey, 2026-07-07). No verified Claude Mythos 5 system-prompt leak was found on GitHub.

## What it is

A corroboration survey of the public copies of the Claude Fable 5 claude.ai system prompt: Anthropic's official excerpt, community mirror lineage, the Claude Code extraction project, and the analysis posts. It establishes where this vault's own capture, [[System Prompt Export 2026-07]], sits in that landscape and why line counts differ across copies. Evidence was fetched and verified on 2026-07-07, but live mirror and search links are omitted from this public release.

## Official Anthropic copy

Anthropic publishes the Claude Fable 5 claude.ai system prompt, dated 2026-06-09, at https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07). It covers ONLY the claude_behavior core: product_information, refusal_handling with child safety, legal_and_financial_advice, tone_and_formatting, user_wellbeing, anthropic_reminders, evenhandedness, responding_to_mistakes_and_criticism, and knowledge_cutoff. The page states these prompts cover claude.ai web and mobile only and do not apply to the Claude API. As of 2026-07-07 it still shows the June 9 version despite the July redeployment, so it is authoritative for the behavior core but stale on tooling and on anything added since June. EVIDENCE-BASED.

## Community lineage

The canonical community lineage began with a June 10, 2026 capture of 1,585 lines and roughly 120k characters, later expanded to roughly 3,200 lines. Mirror links are omitted from this public release. Mirrors and descendants:

- One roughly 2,400-line mirror includes the token budget line and the request_evaluation_checklist absent from the first capture.
- One 1,593-line mirror tracks the June 9 state.
- One verification repository published full and lite variants, plus 27 behavioral comparison experiments dated 2026-06-15 concluding the prompt changes style, not quality.
- One archive claimed roughly 1,580 lines and split the material into full prompt, tools, highlights, and analysis.

All community copies are PRACTITIONER: independently captured, mutually consistent, but not mechanically verifiable against Anthropic.

## GitHub leak sweep

GitHub repository search on 2026-07-07 found 18 repositories for the query `claude-fable-5` plus `system prompt`. The first page is not 18 independent leaks. It is mostly mirrors, prompt archives, analyses, derivative prompt toolkits, and Claude Code repackagings that reuse the same Fable prompt lineage.

No direct Mythos 5 system-prompt leak was found. The repository search query `claude-mythos-5` plus `system prompt` returned zero repositories. The broader query `Claude Mythos` plus `leak` returned many results, but the visible first page was low-signal: repeated Aether Guardian nodes, joke or entertainment projects, theoretical reconstructions, and prompt-inspired scaffolds rather than a Mythos 5 prompt artifact.

Important false positives:

- One community item titled "Mythos system prompt" is actually a Fable prompt copy because the file heading says Claude Fable 5 system prompt and the content is the known Fable claude.ai prompt. Treat it as mislabeled Fable evidence, not Mythos evidence.
- OpenMythos is a theoretical reconstruction based on public research and speculation and says it is unaffiliated with Anthropic.
- One Mythos scaffold is an agent-workflow scaffold inspired by Mythos Preview behavior, not a leaked model prompt.
- One Mythos Preview project explicitly says it is not real Claude Mythos Preview and is entertainment software.
- Repeated Baobabebal Aether Guardian nodes label themselves Claude Mythos Leak, but the inspected repository only exposes a README/image anchor and no verifiable Mythos prompt or model artifact.

Derivative Fable packages:

- One Fable mode package bundles the Fable prompt into a Claude Code and Opus 4.8 workflow. It usefully states the ceiling: this transfers disposition and workflow rules, not Fable's raw model capability.
- One Fable CLAUDE.md package repackages Fable behavioral artifacts into a CLAUDE.md-style operating file with trace examples. Treat it as derivative practice material, not a fresh leak.

## This vault's capture

System Prompt Export 2026-07 capture: 3,826 lines, captured 2026-07-07, after the July redeployment. The raw capture is omitted from this public release. It is a superset of both the official subset and the June community captures, adding the full tool JSON schemas and the account-specific injected blocks. Nothing found online on 2026-07-07 contradicts it. Per [[Corpus Scope Decision]] it is the primary source for this brain, and per [[Confidence Tag Policy]] claims sourced from it are EVIDENCE-BASED with mandatory line references.

## Claude Code side

link omitted for public release (retrieved 2026-07-07) mechanically extracts Claude Code's prompt fragments per release, currently v2.1.202 (2026-07-06) with 515+ prompt strings, including a Fable 5 model identity fragment. This is the best public source for the harness prompt this vault's corpus does not include; see [[Export Omits Claude Code Harness]]. Mechanical extraction from the shipped binary makes it more trustworthy than hand captures. PRACTITIONER, leaning strong.

## Analyses

- AlphaSignal analysis, link omitted for public release (retrieved 2026-07-07): treats the leaked prompt as an agent-design manual and correctly flags the claude.ai-only scope. PRACTITIONER.
- Horia Stan analysis, link omitted for public release (retrieved 2026-07-07): a full readthrough of the leak. PRACTITIONER.

## Line-count reconciliation

The June leak is 1,585 lines; this vault's capture is 3,826. The gap is explained, not contradictory:

- Tool JSON schemas: full function schemas are present in this capture and absent or truncated in the June leaks.
- Injected blocks: account-specific and connector-specific sections (enabled tools, user context) vary per account and are captured here in full.
- Capture date: this copy postdates the July redeployment; one community lineage has grown to roughly 3,200 lines as it caught up, and another roughly 2,400-line mirror sits between, with the token budget line and request_evaluation_checklist marking incremental additions.

Rule: compare copies section-by-section, never by raw line count. Shared sections (the behavior core, search instructions, artifacts) match across copies; the deltas are schemas, injections, and date.

## Best practice

- EVIDENCE-BASED: state the trust ladder explicitly when citing any copy: official Anthropic page > mechanical extraction (Piebald) > known community collections > anonymous pastes.
- EVIDENCE-BASED: for the behavior core, cite the official page; it is Anthropic's own text, even if dated June 9.
- PRACTITIONER: for tool blocks, schemas, and injected sections, cite this vault's capture with line numbers and corroborate against at least one community collection.
- PRACTITIONER: classify GitHub Mythos hits aggressively. A title containing "Mythos leak" is not evidence unless the repo contains a dated prompt artifact that is not just the Fable prompt mentioning Mythos.
- PRACTITIONER: re-run this survey during every [[Brain Refresh Flow]]; the official page updating past June 9 or a community collection changing again are the two cheapest staleness signals.

## Pitfalls

- The official page covers claude.ai web and mobile only; none of these copies binds the Claude API or [[Claude Code Platform]] behavior.
- The official page is stale relative to the July redeployment; citing it for tooling behavior silently imports June state.
- Line counts differ for benign reasons; treating 1,585 versus 3,826 as a contradiction is the classic mistake this note exists to prevent.
- Community repos rewrite history; a link that showed 1,585 lines in June shows roughly 3,200 today, so always pin the retrieval date.
- Injected blocks in this vault's capture are account-specific; do not present connector lists or user context sections as universal Fable 5 behavior.
- Mislabeled Mythos copies are easy to overread. The inspected "Mythos system prompt" community copy is actually a Fable prompt copy because it names Claude Fable 5 as the active iteration.
- Derivative "Fable mode" or "Fable Lite" packages do not recreate Fable weights. They can transfer style, workflow rules, and operating discipline only.

## Sources

- Anthropic system prompt release notes, 2026-06-09 version, https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07).
- Community capture lineage, 2026-06-10, plus expansion state (retrieved 2026-07-07; link omitted).
- Community mirror of the Fable 5 prompt capture (retrieved 2026-07-07; link omitted).
- Community mirror of the 2026-06-09 state (retrieved 2026-07-07; link omitted).
- Behavioral verification repository with experiments dated 2026-06-15 (retrieved 2026-07-07; link omitted).
- Piebald-AI claude-code-system-prompts, v2.1.202 of 2026-07-06 (retrieved 2026-07-07).
- GitHub repository searches for Fable and Mythos prompt leaks, retrieved 2026-07-07; search URLs omitted.
- Mislabeled Mythos prompt community copy, retrieved 2026-07-07, classified as mislabeled Fable prompt; link omitted.
- Community mirror, derivative package, reconstruction, scaffold, and entertainment repositories, retrieved 2026-07-07; links omitted.
- AlphaSignal and Horia Stan analyses, links omitted for public release (retrieved 2026-07-07).
- System Prompt Export 2026-07, captured 2026-07-07.

## Related

- [[System Prompt Export 2026-07]] because it is the vault capture every copy here is measured against.
- [[Claude Fable 5]] because all copies document this model's claude.ai deployment.
- [[Anthropic]] because the official page is the only first-party copy.
- [[Export Omits Claude Code Harness]] because Piebald's extraction fills exactly that gap.
- [[Corpus Scope Decision]] because it fixes this vault's capture as the primary source.
- [[Corpus Ingestion Flow]] because new captures enter the vault through it.
- [[Brain Refresh Flow]] because this survey must be re-run before the 2026-08-06 staleness date.
- [[Confidence Tag Policy]] because the trust ladder here maps directly onto the tag assignments.
- [[claude.ai Platform]] because every copy scopes to this harness only.
- [[Claude Code Platform]] because its prompt lineage is tracked separately by Piebald.
- [[research-pack-2026-07-07|Research Pack 2026-07-07]] because the fetch evidence behind this survey lives there.

## Next actions

- Watch the official page for a post-June-9 version; when it updates, diff the behavior core against L-referenced notes.
- Section-diff the expanded roughly 3,200-line community copy against this vault's 3,826 lines to enumerate the exact injected-block delta.
- Record Piebald v2.1.202 in `references/source-ledger.json` if not already ledgered.
- Re-run GitHub searches monthly for `claude-mythos-5 system prompt`, `Claude Mythos leak`, and `Claude Fable 5 system prompt`, then separate prompt artifacts from derivative packages.

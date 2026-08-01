---
type: platform
title: "claude.ai Platform"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/harness/claude-ai
  - note/platform
domain: claude-ai-harness
confidence: evidence-based
related:
  - "[[Claude Fable 5]]"
  - "[[Anthropic Plans and Access Tiers]]"
  - "[[System Prompt Export 2026-07]]"
  - "[[Export Chapter Product and Behavior]]"
  - "[[Artifacts Usage Criteria]]"
  - "[[Claude Memory System]]"
  - "[[Past Chats Tools]]"
  - "[[Tone and Formatting Rules]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Claude Code Platform]]"
source_urls:
  - "https://www.anthropic.com/news/claude-fable-5-mythos-5 (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
---

# claude.ai Platform

claude.ai is Anthropic's consumer harness, and since June 9, 2026 it serves Claude Fable 5 to Pro, Max, Team, and Enterprise subscribers, with the behavior of that surface documented in this vault by the System Prompt Export 2026-07 capture.

## What it is

The consumer chat surface for Claude, distinct from the Claude Code developer harness and from raw API access. In this brain's scoping rules, claims sourced from the system prompt export describe exactly this harness: the [[Confidence Tag Policy]] requires each export-backed note to say it describes claude.ai, and the capture is treated as evidence of that surface at capture time, not as a universal guarantee about the model. Everything platform-specific, tool selection, formatting rules, memory behavior, artifact criteria, lives in the export chapter notes rather than here.

## How it works

- **Model access by plan.** Claude Fable 5 "is deployed in claude.ai and Claude Code for Pro, Max, Team, and Enterprise users" per the launch documentation (https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5). Claude Mythos 5 never appears on claude.ai; it is restricted to Project Glasswing partners.
- **Safety behavior on the surface.** Fable 5 includes safety classifiers that can decline requests; Anthropic states "They trigger, on average, in less than 5% of sessions." (https://www.anthropic.com/news/claude-fable-5-mythos-5). When a refusal fires, "Queries on some topics will instead receive a response from Claude Opus 4.8." on consumer surfaces.
- **Availability history.** Launch June 9, 2026; all Fable 5 access suspended under US export controls from June 12; Anthropic reports the controls lifted June 30 with global restoration July 1, while Al Jazeera reports restoration beginning July 2, so exact timing stays contested.
- **Documentation of behavior.** The vault's primary evidence for what runs on claude.ai is the dated system prompt capture, ingested through the [[Corpus Ingestion Flow]] and cited with line references.
- **Position in the product family.** claude.ai is one of three access routes to Fable 5, next to the Claude Code harness and the usage-priced API and clouds; it is the only route where the harness, not the customer, owns the system prompt end to end.

> [!key-insight]
> For this vault, claude.ai is both a product and a measurement target: the export capture makes it the only harness whose system prompt is directly citable, line by line, which is why the confidence policy grants export claims primary-source status for this surface only.

## Best practice

- Attribute every export-derived behavior claim to this harness explicitly; never generalize claude.ai capture text to Claude Code or the API. PRACTITIONER
- Track plan gating from the models documentation, not from memory; plan-to-model mapping changed twice in June 2026 alone. EVIDENCE-BASED
- Expect classifier-driven fallbacks in a small share of sessions and treat an Opus 4.8 answer on a sensitive topic as designed behavior, not a bug. EVIDENCE-BASED
- Re-verify surface behavior after every new export capture; the capture date bounds what this note can assert. PRACTITIONER
- When teaching users which surface they are on, anchor on billing: claude.ai access rides subscription plans, API access rides usage pricing. EVIDENCE-BASED
- Frame Fable 5 on this surface correctly: it is a Mythos-class model made safe for general use, which is precisely what lets it front a consumer product at all. EVIDENCE-BASED

## Pitfalls

- Reading export claims as model claims; the export documents one harness's system prompt, and the same model behaves differently under other harnesses.
- Assuming Mythos 5 reachability from a high-tier plan; "Access is invitation-only and there is no self-serve sign-up." (https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5).
- Citing pre-June-30 availability statements as current; the export-control window makes date checking mandatory for this platform.
- Conflating the claude.ai fallback experience with API refusal semantics; the API returns stop_reason refusal for developers to handle, while the consumer surface reroutes.
- Forgetting the retention floor: Covered Model status means 30-day retention applies to Fable 5 traffic regardless of surface or plan.

> [!gap]
> This worker was not assigned the corpus file, so per-tool details of what runs on claude.ai in the 2026-07 capture (artifacts, memory, search, connectors) are not asserted here; they are owned by [[Export Chapter Product and Behavior]] and its sibling chapter notes with line references.

> [!gap]
> Whether any Fable 5 access exists on the claude.ai free tier is not stated in this brain's verified sources; the packs name only Pro, Max, Team, and Enterprise.

## Sources

- Claude Fable 5 and Claude Mythos 5, Anthropic news: https://www.anthropic.com/news/claude-fable-5-mythos-5 (published 2026-06-09, retrieved 2026-07-07)
- Introducing Claude Fable 5 and Claude Mythos 5, Claude Platform docs: https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)
- Redeploying Claude Fable 5, Anthropic news: https://www.anthropic.com/news/redeploying-fable-5 (published 2026-06-30, retrieved 2026-07-07)
- US lifts restrictions on Anthropic's powerful AI models Fable and Mythos, Al Jazeera: https://www.aljazeera.com/economy/2026/7/1/us-lifts-restrictions-on-powerful-ai-models-fable-mythos-anthropic-says (published 2026-07-01, retrieved 2026-07-07)

## Related

- [[Claude Fable 5]] because it is the flagship model this surface serves.
- [[Anthropic Plans and Access Tiers]] because plan gating decides who sees Fable 5 here.
- [[System Prompt Export 2026-07]] because the capture is the primary evidence for this surface.
- [[Export Chapter Product and Behavior]] because per-feature behavior claims live there with L-refs.
- [[Artifacts Usage Criteria]] because artifacts are a signature capability of this harness.
- [[Claude Memory System]] because product memory is a claude.ai surface feature.
- [[Past Chats Tools]] because conversation retrieval shapes what this surface can recall.
- [[Tone and Formatting Rules]] because the export's response style rules bind this surface.
- [[Fable 5 Dual-Use Safety Measures]] because classifier fallbacks are user-visible here.
- [[Claude Code Platform]] because the developer harness is the contrast that scopes this note.

## Next actions

- Fill the tool-inventory gap from the export chapter notes once corpus-assigned notes land.
- Add a dated plan-gating table when a source enumerates free-tier model access.
- Re-verify the restoration timeline when Anthropic or the docs publish a definitive date.
- Cross-check surface behavior notes against the next export capture's diff.

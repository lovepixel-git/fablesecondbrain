---
type: entity
title: "Claude 5 Model Family"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/model
  - note/entity
domain: model-and-family
confidence: evidence-based
related:
  - "[[Claude Fable 5]]"
  - "[[Claude Mythos 5]]"
  - "[[Mythos-Class Model Tier]]"
  - "[[Model Selection for Agent Workloads]]"
  - "[[Fable 5 Pricing and Rate Limits]]"
  - "[[Prompt Caching Economics]]"
  - "[[Fable Mythos 5 System Card]]"
  - "[[Fable Mythos Operating Doctrine]]"
  - "[[Project Glasswing]]"
  - "[[Anthropic]]"
  - "[[docs.claude.com]]"
  - "[[System Prompt Export 2026-07]]"
  - "[[No Public Fable 5 Benchmark Data]]"
source_urls:
  - "https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/claude-fable-5-mythos-5 (retrieved 2026-07-07)"
  - "https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf (published 2026-06-09, retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Claude 5 Model Family

The current Claude lineup as of 2026-07-07 is five pinned-snapshot models: Claude Fable 5 and Claude Mythos 5 at $10/$50 per MTok with 1M context, Claude Opus 4.8 at $5/$25 with 1M context, Claude Sonnet 5 at $3/$15 with 1M context, and Claude Haiku 4.5 at $1/$5 with 200k context.

## What it is

- The Claude 5 generation opens with [[Claude Fable 5]] and [[Claude Mythos 5]], announced 2026-06-09 on one shared underlying model, defining the [[Mythos-Class Model Tier]] above the Opus class.
- Current API model IDs are claude-fable-5, claude-mythos-5, claude-opus-4-8, claude-sonnet-5, and claude-haiku-4-5-20251001 (alias claude-haiku-4-5).
- Every Claude model ID is a pinned snapshot; dateless IDs from the 4.6 generation onward are also pinned snapshots, not evergreen pointers.
- Four of the five are generally available; Mythos 5 is restricted to approved Project Glasswing organizations with no self-serve signup.
- [[Fable Mythos 5 System Card]] now gives public evaluation evidence for the top shared Fable/Mythos model, especially safety, cyber, CBRN, prompt-injection, and behavioral evaluations.

> [!gap] The research pack does not define the formal boundary of "Claude 5 family" membership: the claude.ai capture calls Fable 5 the first Claude 5 family model, Sonnet 5 carries the 5 name, but whether Opus 4.8 and Haiku 4.5 count as family members is unstated. This note therefore covers the current lineup, not a certified family roster.

## How it works

- Price ladder per MTok input/output: Fable 5 and Mythos 5 at $10/$50, Opus 4.8 at $5/$25, Sonnet 5 at $3/$15, Haiku 4.5 at $1/$5.
- Sonnet 5 currently runs a promotional rate; the docs note "Introductory pricing of $2 / $10 per MTok applies to Claude Sonnet 5" (https://platform.claude.com/docs/en/about-claude/models/overview).
- Context windows: 1M tokens for Fable 5, Mythos 5, Opus 4.8, and Sonnet 5; 200k for Haiku 4.5.
- Fable 5 and Mythos 5 add up to 128k output tokens per request, a January 2026 knowledge cutoff, and the Claude Opus 4.7 tokenizer, which produces roughly 30% more tokens than pre-4.7 models for the same text.
- The family interlocks operationally: refused Fable 5 requests fall back to Claude Opus 4.8, and rerouted requests bill at the serving model's prices.
- App surfaces can also switch away from Fable 5 when safeguards fire, so logging the actual serving model matters in family-level comparisons.
- Fable 5 and Mythos 5 are Covered Models with mandatory 30-day retention and no zero data retention; the pack documents no such designation for Opus 4.8, Sonnet 5, or Haiku 4.5.
- The claude.ai capture of 2026-06-09 lists a different lineup: "'claude-fable-5', 'claude-opus-4-8', 'claude-sonnet-4-6', and 'claude-haiku-4-5-20251001'" (System Prompt Export 2026-07, L21-23).

> [!contradiction] The corpus lineup names Sonnet 4.6 where current docs name Sonnet 5, and omits Mythos 5 entirely. Resolution: the capture is a launch-day snapshot pinned to 2026-06-09; Sonnet 5 evidently shipped after that date, and Mythos 5 is excluded from the consumer prompt because it is Glasswing-restricted. The corpus lineup is stale, not wrong for its date. CONTESTED

> [!gap] Knowledge cutoffs for Opus 4.8, Sonnet 5, and Haiku 4.5 are not in the research pack; only the Fable 5 and Mythos 5 cutoff (January 2026) is verified. Re-verify before citing any other cutoff.

## Best practice

- Pin exact model IDs in production configs; every current ID including the dateless ones is a snapshot, so upgrades are always explicit. EVIDENCE-BASED
- Default agent workloads to the cheapest capable family member and escalate to Fable 5 only when the task demands it; see [[Model Selection for Agent Workloads]]. PRACTITIONER
- Configure Fable 5 refusal fallback to Opus 4.8 so declined requests degrade inside the family instead of failing. EVIDENCE-BASED
- Re-verify the lineup against the models overview page before citing it; the June capture went stale within a month. PRACTITIONER
- Budget with the caching discount in mind on high-volume work; see [[Prompt Caching Economics]] before comparing raw list prices. PRACTITIONER

## Pitfalls

- Treating dateless model IDs as evergreen aliases that silently upgrade; they are pinned snapshots.
- Copying the corpus lineup (Sonnet 4.6, no Mythos 5) into current documentation.
- Assuming Haiku 4.5 shares the 1M window; it is the lone 200k model in the lineup.
- Quoting Sonnet 5 at $2/$10 as list price; that is introductory pricing over a $3/$15 list rate.
- Ranking the family by a single benchmark number; the system card gives public Fable/Mythos evidence, but family-wide general-purpose comparisons still require task-specific evals.

## Sources

- Models overview, https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)
- Introducing Claude Fable 5 and Claude Mythos 5, https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)
- Claude Fable 5 and Claude Mythos 5, https://www.anthropic.com/news/claude-fable-5-mythos-5 (published 2026-06-09, retrieved 2026-07-07)
- System Card: Claude Fable 5 and Claude Mythos 5, https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf (published 2026-06-09, retrieved 2026-07-07)
- System Prompt Export 2026-07, L13-19, L21-23 (captured 2026-07-07)

## Related

- [[Claude Fable 5]] - the flagship generally available model of the generation.
- [[Claude Mythos 5]] - the trusted-access classifier-lifted entry in the lineup.
- [[Mythos-Class Model Tier]] - the new top tier the 5 generation introduces.
- [[Model Selection for Agent Workloads]] - choosing among these five for agent tasks.
- [[Fable 5 Pricing and Rate Limits]] - detailed cost mechanics at the top of the ladder.
- [[Prompt Caching Economics]] - how the 90% caching discount reshapes the price ladder.
- [[Fable Mythos 5 System Card]] - public evidence for top-tier evaluations.
- [[Fable Mythos Operating Doctrine]] - practical model selection posture for Fable and Mythos.
- [[Project Glasswing]] - the restricted access program for Mythos 5.
- [[Anthropic]] - the vendor shipping and gating this lineup.
- [[docs.claude.com]] - the models overview page this note tracks.
- [[System Prompt Export 2026-07]] - the launch-day capture with the stale lineup.
- [[No Public Fable 5 Benchmark Data]] - resolved-gap audit trail and reminder that broad benchmark coverage remains uneven.

## Next actions

- Recheck the models overview page for the end of Sonnet 5 introductory pricing and any new snapshot IDs.
- Close the family-boundary gap when Anthropic publishes a definitive Claude 5 family definition.
- Verify knowledge cutoffs for Opus 4.8, Sonnet 5, and Haiku 4.5 before any cross-model cutoff claim.

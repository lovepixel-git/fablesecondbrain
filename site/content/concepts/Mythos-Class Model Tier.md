---
type: concept
title: "Mythos-Class Model Tier"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/model
  - note/concept
domain: model-and-family
confidence: evidence-based
related:
  - "[[Claude Fable 5]]"
  - "[[Claude Mythos 5]]"
  - "[[Claude 5 Model Family]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Project Glasswing]]"
  - "[[Fable Mythos 5 System Card]]"
  - "[[Fable Mythos Operating Doctrine]]"
  - "[[Mythos 5 Access Criteria]]"
  - "[[Model Selection for Agent Workloads]]"
  - "[[Fable 5 Pricing and Rate Limits]]"
  - "[[No Public Fable 5 Benchmark Data]]"
  - "[[Anthropic]]"
source_urls:
  - "https://www.anthropic.com/news/claude-fable-5-mythos-5 (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)"
  - "https://www.anthropic.com/glasswing (retrieved 2026-07-07)"
  - "https://www.anthropic.com/claude/mythos (retrieved 2026-07-07)"
  - "https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf (published 2026-06-09, retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/expanding-project-glasswing (published 2026-06-02, retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Mythos-Class Model Tier

The Mythos class is Anthropic's capability tier above Opus, launched 2026-06-09 as two variants of one underlying model: [[Claude Fable 5]] with dual-use safety classifiers for general availability, and [[Claude Mythos 5]] without them for approved partners only.

## What it is

- A new top capability tier positioned above the Opus class in Anthropic's lineup. Anthropic's launch post states "Fable 5's capabilities exceed those of any model we've ever made generally available." (https://www.anthropic.com/news/claude-fable-5-mythos-5, published 2026-06-09).
- Fable 5 is the Mythos class made safe for general use; AWS markets it as Mythos-class capabilities with built-in safeguards (https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available, published 2026-06-09).
- Claude Mythos 5 succeeds Claude Mythos Preview and remains restricted; both new models cost less than half of Mythos Preview.
- The system card now grounds the tier beyond launch language: Anthropic classifies Mythos 5 as CB-1 and Cyber Tier 1, documents major cyber capability increases, and reports Fable safeguards catching nearly all tested ExploitBench episodes.
- The system prompt export describes Fable 5 as "the first model in Anthropic's new Claude 5 family" (System Prompt Export 2026-07, L13-19).

> [!contradiction]
> The export's "first model in the Claude 5 family" wording is launch framing: Mythos 5 shipped the same day on the same underlying model, and Sonnet 5 exists in the current documented lineup. The export's API lineup (L21-23) also names Sonnet 4.6 and omits Mythos 5. The corpus is a 2026-06-09 snapshot, stale rather than wrong for its date.

## How it works

- One model, two releases: "Claude Fable 5 and Claude Mythos 5 share the same underlying model" (System Prompt Export 2026-07, L17). Public docs confirm the split: Fable 5 includes safety classifiers that can decline requests; Mythos 5 does not (https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5, retrieved 2026-07-07).
- Shared specs: a 1M-token context window by default, up to 128k output tokens per request, and a January 2026 knowledge cutoff.
- Both use the tokenizer introduced with Claude Opus 4.7, which produces roughly 30% more tokens than pre-4.7 models for the same text.
- Adaptive thinking is the only thinking mode: it cannot be disabled, depth is controlled by the effort parameter, and raw chain of thought is never returned.
- Model IDs are claude-fable-5 and claude-mythos-5; every Claude model ID is a pinned snapshot, and dateless IDs from the 4.6 generation onward are pinned snapshots too, not evergreen pointers.
- Pricing is identical for both: $10 per million input tokens and $50 per million output tokens, with a 90% prompt-caching input discount and US-only inference at 1.1x pricing.
- Access split: Fable 5 is generally available on the Claude API, Claude Platform on AWS, Amazon Bedrock, Google Cloud, and Microsoft Foundry, and runs in claude.ai and Claude Code for Pro, Max, Team, and Enterprise. Mythos 5 is invitation-only inside Project Glasswing, a defensive cybersecurity program that began with 12 founding organizations and later expanded to about 150 additional organizations across more than 15 countries (https://www.anthropic.com/news/expanding-project-glasswing, published 2026-06-02).
- Governance: both are designated Covered Models with mandatory 30-day data retention for safety monitoring and no zero-data-retention option; retained data is not used for training.
- Tier volatility: US export controls applied 2026-06-12 suspended all access to both models; Anthropic reports the controls lifted 2026-06-30 with Fable 5 restored globally 2026-07-01 and Mythos 5 restored for approved US organizations (https://www.anthropic.com/news/redeploying-fable-5, published 2026-06-30).
- Public eval signal: [[Fable Mythos 5 System Card]] resolves the former "no public benchmark data" gap for safety and dual-use evaluation evidence, while broader general-purpose benchmark tables remain thinner.

## Best practice

- Treat "Mythos class" as a capability tier label and "Fable 5" as the only self-serve way to buy it; plan agent architectures around Fable 5, not Mythos 5. EVIDENCE-BASED
- Budget tokens with the Opus 4.7 tokenizer in mind: the same prompt costs roughly 30% more tokens than on pre-4.7 models. EVIDENCE-BASED
- Pin behavior expectations to snapshot IDs: claude-fable-5 is a pinned snapshot, so upgrades are explicit new IDs, not silent swaps. EVIDENCE-BASED
- Use the system card for tier evidence and the launch post for product positioning; they answer different questions. EVIDENCE-BASED
- Verify tier availability before committing a workload: the June 2026 export-control suspension shows access to this tier can vanish and return within weeks. PRACTITIONER
- When the vault export and current docs disagree on the lineup, prefer the dated docs page and mark the corpus claim as a snapshot. PRACTITIONER

## Pitfalls

- Assuming Mythos 5 is a bigger model: it is the same underlying model as Fable 5 without the classifiers, not extra capability weights.
- Assuming Mythos Preview is still the top tier; Mythos 5 succeeds it and undercuts its price by more than half.
- Treating dateless model IDs as evergreen aliases; from the 4.6 generation onward they are pinned snapshots.
- Trusting a single date for the July restoration: Anthropic says lifted 2026-06-30 and restored 2026-07-01, while Al Jazeera reports notification 2026-07-01 and restoration from 2026-07-02 (https://www.aljazeera.com/economy/2026/7/1/us-lifts-restrictions-on-powerful-ai-models-fable-mythos-anthropic-says, published 2026-07-01). CONTESTED until reconciled.
- Expecting self-serve Mythos 5 access; there is no sign-up path, only Anthropic, AWS, or Google Cloud account teams.

## Sources

- Anthropic, Claude Fable 5 and Claude Mythos 5, https://www.anthropic.com/news/claude-fable-5-mythos-5 (published 2026-06-09, retrieved 2026-07-07)
- Claude Platform Docs, Introducing Claude Fable 5 and Claude Mythos 5, https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)
- Claude Platform Docs, Models overview, https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)
- AWS News Blog, Anthropic Claude Fable 5 on AWS, https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available (published 2026-06-09, retrieved 2026-07-07)
- Anthropic, Project Glasswing, https://www.anthropic.com/glasswing (published 2026-04-07, retrieved 2026-07-07)
- Claude Mythos, https://www.anthropic.com/claude/mythos (retrieved 2026-07-07)
- System Card: Claude Fable 5 and Claude Mythos 5, https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf (published 2026-06-09, retrieved 2026-07-07)
- Expanding Project Glasswing, https://www.anthropic.com/news/expanding-project-glasswing (published 2026-06-02, retrieved 2026-07-07)
- Anthropic, Redeploying Claude Fable 5, https://www.anthropic.com/news/redeploying-fable-5 (published 2026-06-30, retrieved 2026-07-07)
- System Prompt Export 2026-07, L13-19, L17, L21-23 (claims extracted 2026-07-07)

## Related

- [[Claude Fable 5]] is the generally available variant of this tier and the vault's main subject.
- [[Claude Mythos 5]] is the classifier-free variant restricted to Project Glasswing partners.
- [[Claude 5 Model Family]] places the Mythos class inside the wider current lineup.
- [[Fable 5 Dual-Use Safety Measures]] details the classifiers that make Fable 5 the releasable variant.
- [[Project Glasswing]] explains how trusted-access Mythos work is operationalized.
- [[Fable Mythos 5 System Card]] is the official evidence base for tier capability and safety posture.
- [[Fable Mythos Operating Doctrine]] is the practical operating layer for this tier.
- [[Mythos 5 Access Criteria]] tracks who can actually obtain the unclassified variant.
- [[Model Selection for Agent Workloads]] weighs this tier against Opus, Sonnet, and Haiku for real work.
- [[Fable 5 Pricing and Rate Limits]] carries the $10/$50 economics of the tier.
- [[No Public Fable 5 Benchmark Data]] is now a resolved-gap audit trail; general-purpose benchmark coverage remains comparatively thin.
- [[Anthropic]] is the entity defining and gating the tier.
- [[System Prompt Export 2026-07]] is the primary capture containing the launch-day framing quoted here.

## Next actions

- Re-check the models overview page after 2026-08-01 for lineup changes above or beside the Mythos class.
- Resolve the contested restoration dates when a second official dated source appears.
- Watch for broader public general-purpose benchmark tables beyond the system card's safety and dual-use evaluations.

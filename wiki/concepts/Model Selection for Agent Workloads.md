---
type: concept
title: "Model Selection for Agent Workloads"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/best-practices
  - note/concept
domain: best-practices
confidence: practitioner
related:
  - "[[Claude Fable 5]]"
  - "[[Claude 5 Model Family]]"
  - "[[Mythos-Class Model Tier]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Fable 5 Pricing and Rate Limits]]"
  - "[[Prompt Caching Economics]]"
  - "[[Extended Thinking Budgets]]"
  - "[[Context Window Management]]"
  - "[[Claude Agent SDK]]"
  - "[[Anthropic API and Claude Platform]]"
source_urls:
  - "https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
  - "https://simonwillison.net/2026/Jun/9/claude-fable-5 (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Model Selection for Agent Workloads

For agent work in July 2026, default to Sonnet 5 at $3/$15, escalate to Fable 5 at $10/$50 only when the task needs frontier capability and can tolerate refusal-fallback plumbing, and keep Haiku 4.5 for high-volume subagent steps.

## What it is

- A decision rule over the current documented lineup: Fable 5 ($10/$50 per MTok, 1M context, 128k output), Opus 4.8 ($5/$25, 1M context), Sonnet 5 ($3/$15, 1M context), and Haiku 4.5 ($1/$5, 200k context) (https://platform.claude.com/docs/en/about-claude/models/overview, retrieved 2026-07-07).
- Sonnet 5 launched with a discount: "Introductory pricing of $2 / $10 per MTok applies to Claude Sonnet 5" (https://platform.claude.com/docs/en/about-claude/models/overview, retrieved 2026-07-07).
- Fable 5 is the capability ceiling for self-serve access; [[Claude Mythos 5]] is invitation-only and out of scope for normal agent stacks.

> [!contradiction]
> The claude.ai export's lineup (System Prompt Export 2026-07, L21-23) lists claude-sonnet-4-6 and omits Mythos 5, while the current docs list claude-sonnet-5 and claude-mythos-5. The export is a 2026-06-09 snapshot; select models from the dated docs page, not the corpus.

## How it works

- Capability axis: Fable 5 is Mythos-class, above the Opus class; Anthropic states its capabilities exceed any previously generally available model (https://www.anthropic.com/news/claude-fable-5-mythos-5, published 2026-06-09).
- Cost axis is not just the sticker price: Fable 5 uses the Opus 4.7 tokenizer, producing roughly 30% more tokens than pre-4.7 models for the same text, which inflates both input and output bills.
- Caching axis: Fable 5 offers a 90% prompt-caching input discount, which rewards agent loops with large stable system prompts; US-only inference costs 1.1x.
- Thinking axis: adaptive thinking is always on for Fable 5 and cannot be disabled; depth is steered with the effort parameter, and raw chain of thought is never returned.
- Refusal axis: only Fable 5 carries dual-use classifiers (cyber, bio, frontier_llm, reasoning_extraction). Refusals return HTTP 200 with stop_reason refusal and can fall back to Opus 4.8 server-side, via SDK middleware, or by manual retry with fallback credit.
- Compliance axis: Fable 5 is a Covered Model with mandatory 30-day retention and no zero-data-retention option; workloads contractually requiring ZDR must use a non-covered model.
- Context axis: Fable 5, Opus 4.8, and Sonnet 5 all offer 1M-token windows; Haiku 4.5 stops at 200k, which bounds its role to scoped subtasks.
- Field report: Simon Willison's day-one testing found Fable 5 slow and expensive but exceptionally capable, spending $110.42 in about 5.5 hours; "The challenge is finding tasks that it can't do." (https://simonwillison.net/2026/Jun/9/claude-fable-5, published 2026-06-09).

## Best practice

- Start agent pipelines on Sonnet 5 and promote individual stages to Fable 5 only when evaluation shows a capability gap; the price gap is 3x or more per token. PRACTITIONER
- Route high-volume, low-stakes subagent calls (classification, extraction, triage) to Haiku 4.5 and keep its 200k window in mind when packing context. PRACTITIONER
- If a stage runs Fable 5 unattended, wire the server-side fallbacks parameter or SDK refusal middleware to Opus 4.8 before shipping. EVIDENCE-BASED
- Recompute budgets with the Opus 4.7 tokenizer's roughly 30% token inflation before comparing Fable 5 quotes against 4.5-era baselines. EVIDENCE-BASED
- Exploit the 90% prompt-caching discount by freezing system prompts and tool schemas across loop iterations. EVIDENCE-BASED
- Exclude Fable 5 from any workload that requires zero data retention; the Covered Model designation makes 30-day retention mandatory. EVIDENCE-BASED
- Treat day-one speed and cost impressions as provisional; they come from one practitioner on launch day. CONTESTED

## Pitfalls

- Choosing Fable 5 by default "because it is the best": latency, token inflation, and refusal plumbing make it the wrong default for most agent steps.
- Ignoring refusal handling because triggers average under 5% of sessions; security and bio-adjacent agent workloads concentrate well above the average.
- Selecting Opus 4.8 as the fallback target but forgetting rerouted requests are billed at Opus prices, not Fable prices.
- Copying the model lineup out of the system prompt export; it is a stale launch-day snapshot.
- Assuming availability is constant: Fable 5 was suspended 2026-06-12 under export controls and restored 2026-07-01, so single-model architectures carry regulatory risk.

## Sources

- Claude Platform Docs, Models overview, https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)
- Claude Platform Docs, Introducing Claude Fable 5 and Claude Mythos 5, https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)
- Anthropic, Claude Fable 5 and Claude Mythos 5, https://www.anthropic.com/news/claude-fable-5-mythos-5 (published 2026-06-09, retrieved 2026-07-07)
- Simon Willison, Initial impressions of Claude Fable 5, https://simonwillison.net/2026/Jun/9/claude-fable-5 (published 2026-06-09, retrieved 2026-07-07)
- Anthropic, Redeploying Claude Fable 5, https://www.anthropic.com/news/redeploying-fable-5 (published 2026-06-30, retrieved 2026-07-07)
- System Prompt Export 2026-07, L21-23 (claims extracted 2026-07-07)

## Related

- [[Claude Fable 5]] is the frontier option this rule decides for or against.
- [[Claude 5 Model Family]] catalogs the candidates and their spec sheets.
- [[Mythos-Class Model Tier]] explains what capability the top tier actually buys.
- [[Fable 5 Dual-Use Safety Measures]] defines the refusal behavior selection must plan around.
- [[Fable 5 Pricing and Rate Limits]] holds the detailed economics behind the price axis.
- [[Prompt Caching Economics]] quantifies the 90% caching discount that changes the math for loops.
- [[Extended Thinking Budgets]] covers steering always-on adaptive thinking with effort.
- [[Context Window Management]] matters when choosing between 1M and 200k windows.
- [[Claude Agent SDK]] is where refusal-fallback middleware lives in practice.
- [[Anthropic API and Claude Platform]] is the surface where all of these knobs are set.

## Next actions

- Build a small eval set from this vault's real agent tasks and measure Sonnet 5 vs Fable 5 stage by stage.
- Re-check Sonnet 5 introductory pricing expiry on the models overview page in August 2026.
- Record observed refusal rates per workload to replace the launch-day sub-5% average with local data.

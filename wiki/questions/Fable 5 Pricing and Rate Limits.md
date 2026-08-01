---
type: question
title: "Fable 5 Pricing and Rate Limits"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/model
  - note/question
domain: model-and-family
confidence: evidence-based
question: "What rate limits apply to Claude Fable 5 on the API and on claude.ai plans, beyond the fully documented pricing?"
answer_quality: draft
related:
  - "[[Claude Fable 5]]"
  - "[[Claude 5 Model Family]]"
  - "[[Prompt Caching Economics]]"
  - "[[Anthropic Plans and Access Tiers]]"
  - "[[Model Selection for Agent Workloads]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Mythos 5 Access Criteria]]"
  - "[[Anthropic API and Claude Platform]]"
  - "[[Fable Mythos 5 System Card]]"
  - "[[No Public Fable 5 Benchmark Data]]"
source_urls:
  - "https://www.anthropic.com/news/claude-fable-5-mythos-5 (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)"
  - "https://www.anthropic.com/claude/fable (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Fable 5 Pricing and Rate Limits

Pricing is fully documented at $10/$50 per MTok with a 90% caching discount, but numeric rate limits for Fable 5 remain unverified in every source this vault has checked.

## What it is

- A question note separating what is settled (list pricing, billing behavior) from what is open (rate-limit tiers, plan quotas).
- Pricing facts here are evidence-based against dated Anthropic pages retrieved 2026-07-07; the rate-limit side is a genuine hole in the claim packs.

## How it works

### What we know (pricing)

- Fable 5 and Mythos 5 both cost "$10 per million input tokens and $50 per million output tokens", less than half the price of Claude Mythos Preview (https://www.anthropic.com/news/claude-fable-5-mythos-5).
- The product page adds a 90% prompt-caching input discount and US-only inference at 1.1x pricing (https://www.anthropic.com/claude/fable).
- The rest of the lineup prices below it: Opus 4.8 at $5/$25 per MTok, Sonnet 5 at $3/$15 (with documented introductory pricing of $2/$10), Haiku 4.5 at $1/$5 (https://platform.claude.com/docs/en/about-claude/models/overview).
- Billing interacts with safety: a refusal that arrives before any output is not billed and does not count against rate limits, and requests rerouted to Claude Opus 4.8 fallback are billed at the serving model's prices.
- Cost anecdote: day-one testing by Simon Willison spent $110.42 in about 5.5 hours; a contested single-practitioner data point, not a planning basis.

### What we do not know (rate limits)

> [!gap]
> No verified source in this vault states numeric API rate limits (requests per minute, tokens per minute) or tier thresholds for claude-fable-5, and none states claude.ai plan quotas for Fable 5 usage beyond its availability to Pro, Max, Team, and Enterprise users. The only rate number captured anywhere is the claude.ai web_fetch tool's 100-per-hour limit (System Prompt Export 2026-07, L3083-3089), which is a harness tool limit, not an API model limit.

### What would resolve it

- A rate-limits page on platform.claude.com listing claude-fable-5 tiers, retrieved and dated.
- Console screenshots or API error headers from a live account showing concrete limits.

## Best practice

- Model costs from list price plus the 90% caching discount, then validate against a small live run. EVIDENCE-BASED
- Count refusal economics into budgets: pre-output refusals are free, fallback responses bill at Opus 4.8 prices. EVIDENCE-BASED
- Do not extrapolate rate limits from the web_fetch 100-per-hour figure; it is a claude.ai tool limit. PRACTITIONER
- Treat the $110.42 day-one spend anecdote as contested color, not capacity planning input. PRACTITIONER

## Pitfalls

- Confusing harness tool limits captured in the corpus with API model rate limits.
- Budgeting US-only inference workloads at list price; the documented multiplier is 1.1x.
- Assuming introductory Sonnet 5 pricing ($2/$10) is permanent when comparing tiers.
- Assuming rate limits are uniform across Bedrock, Google Cloud, and Microsoft Foundry deployments; no source verifies any of them.

## Sources

- Claude Fable 5 and Claude Mythos 5, https://www.anthropic.com/news/claude-fable-5-mythos-5 (retrieved 2026-07-07, published 2026-06-09).
- Models overview, https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07).
- Claude Fable product page, https://www.anthropic.com/claude/fable (retrieved 2026-07-07).
- Refusals and fallback, https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback (retrieved 2026-07-07).
- Initial impressions of Claude Fable 5, https://simonwillison.net/2026/Jun/9/claude-fable-5 (retrieved 2026-07-07, published 2026-06-09).
- System Prompt Export 2026-07, L3083-3089 (snapshot dated 2026-06-09, cited 2026-07-07).

## Related

- [[Claude Fable 5]] is the model whose limits are in question.
- [[Claude 5 Model Family]] provides the lineup pricing context.
- [[Prompt Caching Economics]] quantifies the 90% discount lever.
- [[Anthropic Plans and Access Tiers]] covers the Pro, Max, Team, and Enterprise surface.
- [[Model Selection for Agent Workloads]] consumes these numbers for routing decisions.
- [[Fable 5 Dual-Use Safety Measures]] explains the refusal billing interaction.
- [[Mythos 5 Access Criteria]] is the sibling question on the restricted twin model.
- [[Anthropic API and Claude Platform]] is where rate-limit documentation would land.
- [[Fable Mythos 5 System Card]] is the public evaluation source that complements pricing.
- [[No Public Fable 5 Benchmark Data]] is now a resolved-gap audit trail; broad general-purpose benchmark coverage remains uneven.

## Next actions

- Search platform.claude.com for a rate-limits page listing claude-fable-5 and capture it dated.
- Record observed limits from the first production API account with Fable 5 access.
- Upgrade answer_quality past draft once one numeric limit is verified.

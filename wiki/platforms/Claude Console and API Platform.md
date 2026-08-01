---
type: platform
title: "Claude Console and API Platform"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/model
  - note/platform
domain: model-and-family
confidence: evidence-based
related:
  - "[[Anthropic API and Claude Platform]]"
  - "[[Claude Fable 5]]"
  - "[[Claude 5 Model Family]]"
  - "[[Fable 5 Pricing and Rate Limits]]"
  - "[[Prompt Caching Economics]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Mythos 5 Access Criteria]]"
  - "[[Model Selection for Agent Workloads]]"
  - "[[Extended Thinking Budgets]]"
  - "[[Anthropic]]"
source_urls:
  - "https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback (retrieved 2026-07-07)"
---

# Claude Console and API Platform

Claude Fable 5 is "generally available on the Claude API, Claude Platform on AWS, Amazon Bedrock" plus Google Cloud and Microsoft Foundry (https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5), priced at $10 per million input tokens and $50 per million output tokens, with pinned snapshot model IDs, refusal fallback to Opus 4.8, and mandatory 30-day retention.

## What it is

The developer access layer for the Claude model family: the first-party Claude API plus cloud distribution. Fable 5 ships on Amazon Bedrock in the US East (N. Virginia) and Europe (Stockholm) regions, on Google Cloud, and on Microsoft Foundry. Claude Mythos 5 is not on this self-serve path at all; it is limited to approved Project Glasswing customers via Anthropic, AWS, or Google Cloud account teams.

## How it works

- **Model IDs.** Current IDs are claude-fable-5, claude-mythos-5, claude-opus-4-8, claude-sonnet-5, and claude-haiku-4-5-20251001 (alias claude-haiku-4-5). Every Claude model ID is a pinned snapshot; dateless IDs from the 4.6 generation onward are also pinned snapshots, not evergreen pointers.
- **Specs.** Fable 5 and Mythos 5 share a 1M-token context window by default, up to 128k output tokens per request, a January 2026 knowledge cutoff, and the Opus 4.7 tokenizer, which produces roughly 30 percent more tokens than pre-4.7 models for the same text.
- **Pricing.** Fable 5 and Mythos 5: "$10 per million input tokens and $50 per million output tokens" (https://www.anthropic.com/news/claude-fable-5-mythos-5), less than half of Claude Mythos Preview, with a 90 percent prompt-caching input discount and US-only inference at 1.1x pricing. Below them: Opus 4.8 at $5/$25 (1M context), Sonnet 5 at $3/$15 (1M context), Haiku 4.5 at $1/$5 (200k context).
- **Refusal semantics.** "A refusal is a successful HTTP 200 response" (https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback) with stop_reason refusal and a stop_details object naming the category (cyber, bio, frontier_llm, reasoning_extraction). A refusal arriving before any output is not billed and does not count against rate limits.
- **Fallback paths.** Refused Fable 5 requests reach Claude Opus 4.8 three ways: the server-side fallbacks parameter (beta header server-side-fallback-2026-06-01), SDK refusal-fallback middleware (TypeScript, Python, Go, Java, C#), or manual retry with fallback credit; rerouted requests bill at the serving model's prices.
- **Data handling.** Fable 5 and Mythos 5 are Covered Models: they "carry 30-day data retention and are not available under zero data retention" (https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5), with retained data used for safety purposes, not training.
- **Thinking.** Adaptive thinking is always on; depth is controlled with the effort parameter, budget_tokens returns a 400 error, and raw chain of thought is never returned (thinking.display yields a summary or empty field).
- **Availability history.** GA on June 9, 2026; all access suspended under US export controls from June 12; Anthropic reports the controls lifted June 30 with Fable 5 restored globally July 1 and Mythos 5 restored for a set of approved US organizations.

> [!key-insight]
> Fable 5's API contract makes safety a first-class response state, not an error: a classifier decline arrives as a normal 200 with stop_reason refusal, is free if it fires before output, and has documented fallback machinery. Clients that only handle HTTP errors will misread designed behavior as an outage.

## Best practice

- Pin behavior expectations to the snapshot ID you deploy; there is no evergreen pointer to silently upgrade you. EVIDENCE-BASED
- Wire a fallback path before production: server-side fallbacks parameter or SDK middleware, so classifier refusals degrade to Opus 4.8 instead of failing. EVIDENCE-BASED
- Budget with the new tokenizer in mind; identical text costs roughly 30 percent more tokens than on pre-4.7 models. EVIDENCE-BASED
- Exploit the 90 percent prompt-caching input discount for repeated system prompts and corpora. EVIDENCE-BASED
- Check zero-data-retention requirements first; Covered Model status makes Fable 5 ineligible, which disqualifies some compliance regimes. EVIDENCE-BASED
- Confirm regional availability per cloud; Bedrock coverage is N. Virginia and Stockholm, not every region. EVIDENCE-BASED
- Consider US-only inference deliberately; the 1.1x price premium buys a data-locality property, not capability. EVIDENCE-BASED

## Pitfalls

- Treating a refusal as an HTTP error; it is a 200 with stop_reason refusal, and error-path-only handling misses it.
- Billing surprises on fallback: rerouted requests are billed at the serving model's prices, not Fable 5's.
- Sending budget_tokens or prefilled assistant turns; both return 400 errors on this model generation.
- Assuming availability is stable: all access was suspended June 12 to June 30, 2026 under US export controls, and restoration timing is reported inconsistently across Anthropic and press.
- Requesting Mythos 5 through the console; "Access is invitation-only and there is no self-serve sign-up." (https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5).

## Sources

- Models overview, Claude Platform docs: https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)
- Introducing Claude Fable 5 and Claude Mythos 5, Claude Platform docs: https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)
- Refusals and fallback, Claude Platform docs: https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback (retrieved 2026-07-07)
- Claude Fable 5 and Claude Mythos 5, Anthropic news: https://www.anthropic.com/news/claude-fable-5-mythos-5 (published 2026-06-09, retrieved 2026-07-07)
- Anthropic Claude Fable 5 on AWS, AWS News Blog: https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available (published 2026-06-09, retrieved 2026-07-07)

## Related

- [[Anthropic API and Claude Platform]] because this note is the platform view of that API surface.
- [[Claude Fable 5]] because the flagship model's API behavior is defined here.
- [[Claude 5 Model Family]] because the ID and pricing table spans the whole lineup.
- [[Fable 5 Pricing and Rate Limits]] because it deepens the pricing and limit facts summarized here.
- [[Prompt Caching Economics]] because the 90 percent caching discount dominates input cost math.
- [[Fable 5 Dual-Use Safety Measures]] because refusal categories and classifiers originate there.
- [[Mythos 5 Access Criteria]] because the non-self-serve exception is detailed there.
- [[Model Selection for Agent Workloads]] because price and context specs drive model choice.
- [[Extended Thinking Budgets]] because budget_tokens rejection changes thinking control on this platform.
- [[Anthropic]] because the vendor's distribution strategy explains the multi-cloud footprint.

## Next actions

- Add SDK middleware language coverage notes once a fallback implementation is tested here.
- Re-verify Bedrock region list at the next refresh; regional rollouts expand quickly.
- Record observed stop_details payloads from a real refusal to ground the semantics claim.
- Compare cached versus uncached input costs on this vault's recurring corpus prompts.

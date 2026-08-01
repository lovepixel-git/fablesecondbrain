---
type: entity
title: "Claude Fable 5"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/model
  - note/entity
domain: model-and-family
confidence: evidence-based
related:
  - "[[Claude Mythos 5]]"
  - "[[Claude 5 Model Family]]"
  - "[[Mythos-Class Model Tier]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Fable Mythos 5 System Card]]"
  - "[[Fable Mythos Operating Doctrine]]"
  - "[[Project Glasswing]]"
  - "[[Fable 5 Pricing and Rate Limits]]"
  - "[[Model Selection for Agent Workloads]]"
  - "[[No Public Fable 5 Benchmark Data]]"
  - "[[Anthropic]]"
  - "[[Extended Thinking Budgets]]"
  - "[[docs.claude.com]]"
source_urls:
  - "https://www.anthropic.com/news/claude-fable-5-mythos-5 (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback (retrieved 2026-07-07)"
  - "https://www.anthropic.com/claude/fable (retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/redeploying-fable-5 (retrieved 2026-07-07)"
  - "https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf (published 2026-06-09, retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Claude Fable 5

Claude Fable 5 is Anthropic's most capable generally available model, a Mythos-class system launched 2026-06-09 with a 1M token context window, up to 128k output tokens, a January 2026 knowledge cutoff, built-in safety classifiers, and $10/$50 per MTok pricing under the pinned model ID claude-fable-5.

## What it is

- Announced 2026-06-09 alongside [[Claude Mythos 5]]. Anthropic states "Fable 5's capabilities exceed those of any model we've ever made generally available" (https://www.anthropic.com/news/claude-fable-5-mythos-5).
- It sits in the [[Mythos-Class Model Tier]], a capability tier positioned above the Opus class, delivering Mythos-level capability with built-in safeguards for broad access.
- Fable 5 and Mythos 5 share one underlying model; Fable 5 adds dual-use safety measures. The claude.ai capture confirms "Claude Fable 5 and Claude Mythos 5 share the same underlying model" (System Prompt Export 2026-07, L17).
- [[Fable Mythos 5 System Card]] now supplies the public evidence base behind the tier claim: it records the deployment split, threshold judgments, red-team results, cyber evals, and behavioral evaluations.
- The API model ID is claude-fable-5, a pinned snapshot; dateless IDs from the 4.6 generation onward are pinned snapshots, not evergreen pointers.
- The claude.ai capture introduces it as "the first model in Anthropic's new Claude 5 family" (System Prompt Export 2026-07, L13-19).

> [!contradiction] "First Claude 5 model" is launch framing. Mythos 5 shipped the same day on the same underlying model, preceded by Claude Mythos Preview. Treat the corpus wording as imprecise. CONTESTED

## How it works

- Specs: 1M token context window by default, up to 128k output tokens per request, January 2026 knowledge cutoff, and the Claude Opus 4.7 tokenizer, which produces roughly 30% more tokens than pre-4.7 models for the same text.
- Safety classifiers can decline requests in four categories: cyber (offensive cybersecurity), bio (biological harm), frontier_llm (assisting competing AI development, framed at launch as an anti-distillation safeguard), and reasoning_extraction (reproducing internal reasoning in response text).
- A refusal returns HTTP 200 with stop_reason "refusal" and a stop_details object naming the category; a refusal that arrives before any output is not billed and does not count against rate limits.
- Refused requests fall back to Claude Opus 4.8 via three paths: the server-side fallbacks parameter (beta header server-side-fallback-2026-06-01), SDK refusal-fallback middleware (TypeScript, Python, Go, Java, C#), or a manual retry with fallback credit; rerouted requests bill at the serving model's prices.
- Anthropic reports the classifiers "trigger, on average, in less than 5% of sessions" and that over 1,000 hours of external red-teaming produced no universal jailbreaks (https://www.anthropic.com/news/claude-fable-5-mythos-5).
- The system card extends the safety evidence: more than 100,000 external red-team attempts, two task-specific jailbreaks but no universal jailbreak, and Fable safeguards flagging 407 of 410 ExploitBench episodes.
- Adaptive thinking is the only thinking mode: thinking cannot be disabled, depth is steered with the effort parameter, and raw chain of thought is never returned; thinking.display yields a summary or an empty field.
- Pricing: $10 per million input tokens and $50 per million output tokens, less than half the price of Claude Mythos Preview, with a 90% prompt-caching input discount and US-only inference at 1.1x pricing.
- Fable 5 is a Covered Model: mandatory 30-day data retention for safety monitoring, no zero data retention option, and retained data is used for safety purposes, not training.
- Availability: generally available on the Claude API, Claude Platform on AWS, Amazon Bedrock (US East N. Virginia, Europe Stockholm), Google Cloud, and Microsoft Foundry, and deployed in claude.ai and Claude Code for Pro, Max, Team, and Enterprise users.
- US export controls applied 2026-06-12 suspended all access; Anthropic dates the lift to 2026-06-30 with global restoration 2026-07-01. The exact timing is disputed, see [[Anthropic]] for the contested timeline.

> [!contradiction] The claude.ai capture opens with a 190000 token budget block (System Prompt Export 2026-07, L1-7), far below the API's 1M default, and public docs do not list Fable 5 as a context-awareness model. Unresolved by public docs. CONTESTED

## Best practice

- Name the harness when citing behavior: corpus claims evidence the claude.ai capture, not the API or Claude Code. EVIDENCE-BASED
- Handle stop_reason "refusal" explicitly and configure fallback to Claude Opus 4.8 so agent loops never stall on a declined request. EVIDENCE-BASED
- Use prompt caching on long agent contexts; the documented 90% input discount dominates cost at large window sizes. EVIDENCE-BASED
- Estimate token costs against the Opus 4.7 tokenizer; identical text tokenizes roughly 30% larger than on pre-4.7 models. EVIDENCE-BASED
- Use the system card for public evaluation evidence and run task-level evals for your actual workflow before treating Fable as cost-effective. EVIDENCE-BASED
- Cap spend before open-ended testing; day-one practitioner testing burned $110.42 in about 5.5 hours while finding the model slow but exceptionally capable. CONTESTED

## Pitfalls

- Assuming the 1M context window applies inside claude.ai; the capture pins a 190000 token budget.
- Treating a refusal as an HTTP error; it is a successful 200 response with stop_reason "refusal".
- Requesting zero data retention; Covered Model status makes 30-day retention mandatory.
- Reading "first model in the Claude 5 family" as precise history; Mythos 5 co-launched the same day.
- Quoting a Mythos 5 underlying capability number as a deployed Fable 5 score without checking whether Fable safeguards or fallback changed the result.
- Saying there is no public evaluation evidence; that gap is now resolved by [[Fable Mythos 5 System Card]], though broad general-purpose benchmark coverage is still thinner than safety and dual-use coverage.

## Sources

- Claude Fable 5 and Claude Mythos 5, https://www.anthropic.com/news/claude-fable-5-mythos-5 (published 2026-06-09, retrieved 2026-07-07)
- Introducing Claude Fable 5 and Claude Mythos 5, https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)
- Models overview, https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)
- Refusals and fallback, https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback (retrieved 2026-07-07)
- Claude Fable product page, https://www.anthropic.com/claude/fable (retrieved 2026-07-07)
- Redeploying Claude Fable 5, https://www.anthropic.com/news/redeploying-fable-5 (published 2026-06-30, retrieved 2026-07-07)
- System Card: Claude Fable 5 and Claude Mythos 5, https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf (published 2026-06-09, retrieved 2026-07-07)
- Initial impressions of Claude Fable 5, https://simonwillison.net/2026/Jun/9/claude-fable-5 (published 2026-06-09, retrieved 2026-07-07)
- System Prompt Export 2026-07, L1-7, L13-19, L17 (captured 2026-07-07)

## Related

- [[Claude Mythos 5]] - the trusted-access sibling running the same underlying model.
- [[Claude 5 Model Family]] - where Fable 5 sits in the current lineup and pricing ladder.
- [[Mythos-Class Model Tier]] - the capability tier Fable 5 brings to general availability.
- [[Fable 5 Dual-Use Safety Measures]] - classifier categories, refusal shape, and fallback paths in depth.
- [[Fable Mythos 5 System Card]] - the public evaluation and safety evidence source.
- [[Fable Mythos Operating Doctrine]] - the practical model-use doctrine for Fable and Mythos.
- [[Project Glasswing]] - the trusted-access program for the classifier-lifted sibling.
- [[Fable 5 Pricing and Rate Limits]] - cost mechanics including caching and US-only inference.
- [[Model Selection for Agent Workloads]] - when Fable 5 beats cheaper family members.
- [[No Public Fable 5 Benchmark Data]] - resolved-gap audit trail and remaining benchmark caveat.
- [[Anthropic]] - the vendor and the June 2026 export-control episode.
- [[System Prompt Export 2026-07]] - primary evidence for the claude.ai deployment of Fable 5.
- [[Extended Thinking Budgets]] - how always-on adaptive thinking interacts with effort settings.

## Next actions

- Watch https://platform.claude.com/docs/en/about-claude/models/overview for a dated claude-fable-5 snapshot alias or a successor ID.
- Resolve the 190000 token budget contradiction against any future context-awareness docs update.
- Add broader general-purpose benchmark tables if Anthropic publishes them beyond the current system-card evaluations.

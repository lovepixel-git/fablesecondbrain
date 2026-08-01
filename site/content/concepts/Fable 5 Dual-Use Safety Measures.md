---
type: concept
title: "Fable 5 Dual-Use Safety Measures"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/safety
  - note/concept
domain: safety-and-permissions
confidence: evidence-based
related:
  - "[[Claude Fable 5]]"
  - "[[Claude Mythos 5]]"
  - "[[Mythos-Class Model Tier]]"
  - "[[Project Glasswing]]"
  - "[[Fable Mythos 5 System Card]]"
  - "[[Fable Mythos Operating Doctrine]]"
  - "[[Mythos 5 Access Criteria]]"
  - "[[Model Selection for Agent Workloads]]"
  - "[[Anthropic API and Claude Platform]]"
  - "[[Fable 5 Pricing and Rate Limits]]"
  - "[[Memory Injection Resistance]]"
  - "[[Sandbox Network and Filesystem Model]]"
source_urls:
  - "https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback (retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/claude-fable-5-mythos-5 (retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/fable-safeguards-jailbreak-framework (retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/redeploying-fable-5 (retrieved 2026-07-07)"
  - "https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf (published 2026-06-09, retrieved 2026-07-07)"
  - "https://support.claude.com/en/articles/15363606-why-claude-switched-models-in-your-conversation-with-fable-5 (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Fable 5 Dual-Use Safety Measures

Fable 5 is the classifier-guarded release of the Mythos-class model: four refusal categories (cyber, bio, frontier_llm, reasoning_extraction) make the shared Fable/Mythos model broadly releasable, return HTTP 200 with stop_reason refusal on the API, and can fall back to Claude Opus 4.8.

## What it is

- The safety layer that makes Mythos-class capability generally releasable: "Claude Fable 5 includes safety classifiers that can decline requests" while [[Claude Mythos 5]] ships without them (https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5, retrieved 2026-07-07).
- Four documented refusal categories: cyber (offensive cybersecurity), bio (biological harm), frontier_llm (assisting competing AI development, described at launch as an anti-distillation safeguard), and reasoning_extraction (reproducing internal reasoning in response text).
- Anthropic reports the classifiers fire rarely: "They trigger, on average, in less than 5% of sessions." (https://www.anthropic.com/news/claude-fable-5-mythos-5, published 2026-06-09).
- Pre-launch assurance: over 1,000 hours of external red-teaming produced no universal jailbreaks. The system card expands this to more than 100,000 external red-team attempts, with two task-specific jailbreaks found rather than a universal one.
- The system card reports that Fable safeguards flagged 407 of 410 ExploitBench episodes, which makes the safety layer measurable rather than merely descriptive.

## How it works

- Refusal semantics: "A refusal is a successful HTTP 200 response" (https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback, retrieved 2026-07-07) with stop_reason "refusal" and a stop_details object naming the category that fired.
- Billing: a refusal that arrives before any output is not billed and does not count against rate limits.
- Fallback to Opus 4.8 takes three paths: the server-side fallbacks parameter (beta header server-side-fallback-2026-06-01), SDK refusal-fallback middleware (TypeScript, Python, Go, Java, C#), or a manual retry with fallback credit. Rerouted requests are billed at the serving model's prices.
- Product framing matches: "Queries on some topics will instead receive a response from Claude Opus 4.8." (https://www.anthropic.com/news/claude-fable-5-mythos-5, published 2026-06-09).
- Claude app surfaces also expose this as model switching rather than an API object: a support article says Claude may switch from Fable 5 to another model after checking conversation memory, connected app context, web search, and file content.
- Cyber scoping: Anthropic sorts activity into four tiers from prohibited use to benign use and states "We do not intend to block all cybersecurity-related activities." Its proposed Cyber Jailbreak Severity scale scores jailbreaks 0 to 4 on capability gain, breadth, ease of weaponization, and discoverability (https://www.anthropic.com/news/fable-safeguards-jailbreak-framework, published 2026-07-02).
- Incident response in practice: after an Amazon-reported cyber jailbreak and US export controls on 2026-06-12, Anthropic deployed a classifier blocking the technique in over 99% of cases; controls lifted 2026-06-30 and Fable 5 redeployed globally 2026-07-01 (https://www.anthropic.com/news/redeploying-fable-5, published 2026-06-30).
- Data governance backstop: Fable 5 and Mythos 5 are Covered Models with mandatory 30-day retention for safety monitoring, no zero-data-retention option, and retained data excluded from training.
- On claude.ai, the harness adds runtime nudges: classifiers can inject six named reminder types including cyber_warning and ethics_reminder, and reminders never reduce restrictions (System Prompt Export 2026-07, L144-152).

## Best practice

- Build every Fable 5 integration to branch on stop_reason refusal; it arrives as HTTP 200, so error-code handling alone never sees it. EVIDENCE-BASED
- Use stop_details to log which category fired; category counts tell you whether your workload sits near the cyber or bio boundary. PRACTITIONER
- For unattended agents, enable the server-side fallbacks parameter or SDK middleware so refusals degrade to Opus 4.8 instead of failing the run. EVIDENCE-BASED
- For app and Claude Code work, interpret unexpected model switches as a safeguard path first, then inspect whether memory, files, web search, or connector context pulled the session across a category boundary. EVIDENCE-BASED
- Expect fallback answers to be billed at the serving model's own prices and reconcile cost reports accordingly. EVIDENCE-BASED
- Do not tune prompts to skirt the classifiers; the June 2026 jailbreak episode shows Anthropic patches techniques fast and regulators can suspend the model entirely. PRACTITIONER
- Legitimate defensive security work should proceed normally; the four-tier cyber framework explicitly protects benign use. EVIDENCE-BASED
- Treat [[Project Glasswing]] as the operational complement to this safety layer: Fable keeps broad users inside safeguards, while Mythos access is narrowed to trusted defensive workflows. EVIDENCE-BASED

## Pitfalls

- Reading the sub-5% trigger rate as near-zero for your workload; security-heavy or bio-adjacent sessions concentrate refusals far above the average. PRACTITIONER caution.
- Assuming Mythos 5 is a workaround: it drops the classifiers but is invitation-only via Project Glasswing.
- Forgetting that a refusal after partial output is billed; only refusals before any output are free.
- Treating "no universal jailbreaks in 1,000+ hours" as "unjailbreakable"; a working cyber jailbreak still triggered export controls within days of launch.
- Treating the 407 of 410 ExploitBench flagging figure as proof of perfect coverage; it is one official evaluation, not a guarantee for all future prompt shapes.
- Citing third-party summaries when the official 319-page system card is now captured directly in [[Fable Mythos 5 System Card]].

## Sources

- Claude Platform Docs, Refusals and fallback, https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback (retrieved 2026-07-07)
- Claude Platform Docs, Introducing Claude Fable 5 and Claude Mythos 5, https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)
- Anthropic, Claude Fable 5 and Claude Mythos 5, https://www.anthropic.com/news/claude-fable-5-mythos-5 (published 2026-06-09, retrieved 2026-07-07)
- Anthropic, More details on Fable 5's cyber safeguards, https://www.anthropic.com/news/fable-safeguards-jailbreak-framework (published 2026-07-02, retrieved 2026-07-07)
- Anthropic, Redeploying Claude Fable 5, https://www.anthropic.com/news/redeploying-fable-5 (published 2026-06-30, retrieved 2026-07-07)
- System Card: Claude Fable 5 and Claude Mythos 5, https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf (published 2026-06-09, retrieved 2026-07-07)
- Why Claude switched models in your conversation with Fable 5, https://support.claude.com/en/articles/15363606-why-claude-switched-models-in-your-conversation-with-fable-5 (retrieved 2026-07-07)
- Zvi Mowshowitz, The System Card, https://thezvi.substack.com/p/claude-fable-5-and-mythos-5-the-system (published 2026-06-12, retrieved 2026-07-07)
- System Prompt Export 2026-07, L144-152 (claims extracted 2026-07-07)

## Related

- [[Claude Fable 5]] is the model these measures gate.
- [[Claude Mythos 5]] is the same model released without the classifiers.
- [[Mythos-Class Model Tier]] explains why a safety split was needed at this capability level.
- [[Project Glasswing]] is the restricted-access channel for classifier-lifted use.
- [[Fable Mythos 5 System Card]] is the official evidence base for this safety layer.
- [[Fable Mythos Operating Doctrine]] turns these mechanics into operating practice.
- [[Mythos 5 Access Criteria]] covers the restricted path around the classifiers.
- [[Model Selection for Agent Workloads]] folds refusal-fallback into model choice.
- [[Anthropic API and Claude Platform]] hosts the refusal and fallback API surface.
- [[Fable 5 Pricing and Rate Limits]] interacts with unbilled refusals and fallback billing.
- [[Memory Injection Resistance]] covers the adjacent claude.ai defense against injected instructions.
- [[Sandbox Network and Filesystem Model]] is the execution-side safety complement to these model-side classifiers.

## Next actions

- Probe which stop_details categories fire on this vault's own security research prompts and record rates.
- Track the CJS framework page for adoption or revisions after 2026-07-02.
- Re-verify the sub-5% trigger claim if Anthropic publishes post-redeployment numbers.

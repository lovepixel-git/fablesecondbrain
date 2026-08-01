---
type: gap
title: "No Public Fable 5 Benchmark Data"
status: mature
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/model
  - note/gap
domain: model-and-family
confidence: evidence-based
related:
  - "[[Claude Fable 5]]"
  - "[[Claude Mythos 5]]"
  - "[[Claude 5 Model Family]]"
  - "[[Model Selection for Agent Workloads]]"
  - "[[Mythos-Class Model Tier]]"
  - "[[Fable Mythos 5 System Card]]"
  - "[[Fable Mythos Operating Doctrine]]"
  - "[[Anthropic]]"
  - "[[docs.claude.com]]"
  - "[[Fable 5 Pricing and Rate Limits]]"
  - "[[Confidence Tag Policy]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://www.anthropic.com/system-cards (retrieved 2026-07-07)"
  - "https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf (published 2026-06-09, retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/claude-fable-5-mythos-5 (published 2026-06-09, retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)"
---

# No Public Fable 5 Benchmark Data

Resolved 2026-07-07: this was a true gap before the Fable/Mythos system card was integrated, but it is no longer correct to say the vault has no public benchmark or evaluation data for Fable 5.

> [!done]
> The 319-page Claude Fable 5 and Claude Mythos 5 system card is now captured in [[Fable Mythos 5 System Card]] and references/source-ledger.json. It supplies public evaluation evidence for cyber capability, safeguards, prompt injection behavior, wellbeing, evenhandedness, child safety, and biosecurity threshold analysis.

## What changed

- The old gap asserted that every capability claim rested on launch framing or practitioner anecdote.
- The system card now provides dated official evidence for the shared Fable/Mythos underlying model, including public cyber and safety evaluations.
- The most important cyber figures now captured in the claim ledger are Mythos 5 ExploitBench mean score 10.75, CyberGym target reproduction 83.8 percent, Firefox 147 working exploit success 88.4 percent, and Fable safeguards flagging 407 of 410 ExploitBench episodes.
- The system card also records that Anthropic classified Mythos 5 as CB-1 and Cyber Tier 1, while stating that the CB-2 judgment is less clear than for prior models and that the model can significantly uplift well-resourced threat actors.

## Remaining caution

This gap is resolved, but the evidence is uneven. The public record is strongest for safety, dual-use, and red-team evaluations. General-purpose public benchmark tables for everyday coding, reasoning, vision, and agentic productivity remain thinner than the safety-card evidence.

## Best practice

- Use [[Fable Mythos 5 System Card]] as the primary source for public evaluation data. EVIDENCE-BASED
- Stop saying "no public Fable 5 benchmark data"; say "public general-purpose benchmark coverage is thinner than safety and dual-use evaluation coverage." EVIDENCE-BASED
- Keep practitioner impressions separate from system-card evidence when ranking Fable 5 against Opus 4.8, Sonnet 5, or competitor models. PRACTITIONER
- Before spending heavily on Fable 5, still run task-level evals for the actual workload. PRACTITIONER

## Pitfalls

- Treating a resolved gap as still active and downgrading every Fable 5 capability claim unnecessarily.
- Treating safety and cyber evals as a full substitute for product-specific coding, writing, or agentic evals.
- Ignoring that Fable 5 and Mythos 5 share the same underlying model, while Fable 5 includes safeguards that change some observable behavior.

## Sources

- Anthropic system cards index, https://www.anthropic.com/system-cards (retrieved 2026-07-07)
- System Card: Claude Fable 5 and Claude Mythos 5, https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf (published 2026-06-09, retrieved 2026-07-07)
- Claude Fable 5 and Claude Mythos 5, https://www.anthropic.com/news/claude-fable-5-mythos-5 (published 2026-06-09, retrieved 2026-07-07)
- Models overview, https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)

## Related

- [[Fable Mythos 5 System Card]] is the note that closed this gap.
- [[Claude Fable 5]] is the generally available model whose public evaluation record is now richer.
- [[Claude Mythos 5]] shares the underlying model and carries the strongest dual-use eval evidence.
- [[Mythos-Class Model Tier]] uses the system-card evidence to ground tier claims.
- [[Model Selection for Agent Workloads]] should still require workload-specific evals.
- [[Fable Mythos Operating Doctrine]] turns the resolved evidence into operating practice.
- [[Confidence Tag Policy]] defines how remaining benchmark-light claims should be tagged.

## Next actions

- Keep this file as a resolved-gap audit trail until no active notes link to it as an open gap.
- Watch for broader general-purpose benchmark tables and route them into [[Fable Mythos 5 System Card]].
- Retag downstream notes that still imply zero public evaluation data.

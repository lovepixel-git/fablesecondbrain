---
type: entity
title: "Claude Mythos 5"
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
  - "[[Claude 5 Model Family]]"
  - "[[Mythos-Class Model Tier]]"
  - "[[Project Glasswing]]"
  - "[[Fable Mythos 5 System Card]]"
  - "[[Fable Mythos Operating Doctrine]]"
  - "[[Mythos 5 Access Criteria]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Anthropic]]"
  - "[[Fable 5 Pricing and Rate Limits]]"
  - "[[System Prompt Export 2026-07]]"
  - "[[docs.claude.com]]"
source_urls:
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)"
  - "https://www.anthropic.com/glasswing (retrieved 2026-07-07)"
  - "https://www.anthropic.com/claude/mythos (retrieved 2026-07-07)"
  - "https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf (published 2026-06-09, retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/expanding-project-glasswing (published 2026-06-02, retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/claude-fable-5-mythos-5 (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback (retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/redeploying-fable-5 (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Claude Mythos 5

Claude Mythos 5 is the trusted-access sibling of [[Claude Fable 5]]: the same underlying model offered to approved [[Project Glasswing]] partners with Fable's cyber, bio and chemistry, frontier LLM, and reasoning extraction safeguards lifted, and still bound by Covered Model 30-day data retention.

## What it is

- Announced 2026-06-09 together with Claude Fable 5; the two share one underlying model, and Mythos 5 omits the dual-use safety measures Fable 5 adds. The claude.ai capture states "Claude Fable 5 and Claude Mythos 5 share the same underlying model" (System Prompt Export 2026-07, L17).
- The docs draw the safety line plainly: "Claude Fable 5 includes safety classifiers that can decline requests" while Claude Mythos 5 does not include these classifiers (https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback).
- It succeeds Claude Mythos Preview and anchors the [[Mythos-Class Model Tier]], the capability tier above the Opus class.
- The system card is now the strongest public evidence source for what "Mythos-class" means: Anthropic classifies Mythos 5 as CB-1 and Cyber Tier 1, while documenting a major capability jump and warning that the CB-2 judgment is less clear than for earlier models.
- Its model ID claude-mythos-5 appears in the current documented lineup; every current Claude model ID is a pinned snapshot.
- Specs match Fable 5: 1M token context window by default, up to 128k output tokens, January 2026 knowledge cutoff, and the Claude Opus 4.7 tokenizer.
- Pricing also matches: $10 per million input tokens and $50 per million output tokens, less than half the price of Claude Mythos Preview.
- The current Anthropic Mythos product page says access is for a small set of trusted partners doing cybersecurity work, with biology access planned soon.

## How it works

- Access runs through Project Glasswing, a defensive cybersecurity program that began with 12 founding organizations, was later summarized as about 50 initial partners, and expanded to about 150 additional organizations across more than 15 countries. "Access is invitation-only and there is no self-serve sign-up." (https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5).
- Getting access requires contacting an Anthropic, AWS, or Google Cloud account team; there is no public waitlist.
- Mythos 5 is a Covered Model: mandatory 30-day data retention for safety monitoring, no zero data retention option, and retained data serves safety purposes, not training.
- Adaptive thinking is the only thinking mode, the same as Fable 5: no disable switch, depth via the effort parameter, and raw chain of thought never returned.
- With no safety classifiers there is no refusal-and-fallback machinery; the stop_reason "refusal" flow and Opus 4.8 fallback paths documented for Fable 5 are a Fable 5 concern.
- During the June 2026 export-control episode Anthropic suspended all access from 2026-06-12; after the lift, Fable 5 returned globally while Mythos 5 was restored only for a set of approved US organizations (https://www.anthropic.com/news/redeploying-fable-5).
- Public evaluation evidence includes Mythos 5 ExploitBench mean score 10.75, CyberGym target reproduction 83.8 percent, Firefox 147 working exploit success 88.4 percent, and CBRN analysis that leaves Mythos 5 below CB-2 but near enough to require careful treatment.
- The claude.ai consumer capture omits Mythos 5 from its model lineup entirely (System Prompt Export 2026-07, L21-23), consistent with its restriction to Glasswing partners.

> [!gap] The research pack does not describe the contractual usage terms, monitoring obligations, or approval criteria Glasswing partners accept for classifier-free access. Track this in [[Mythos 5 Access Criteria]] and re-verify before advising anyone on eligibility.

## Best practice

- Route Mythos 5 access requests through an Anthropic, AWS, or Google Cloud account team; no self-serve path exists. EVIDENCE-BASED
- Plan compliance reviews around mandatory 30-day retention; zero data retention is unavailable on Covered Models. EVIDENCE-BASED
- Prototype on Claude Fable 5 first; the underlying model is identical and generally available, so most work ports directly. PRACTITIONER
- Do not plan for Mythos 5 inside claude.ai or Claude Code; the consumer capture omits it and docs restrict it to approved organizations. EVIDENCE-BASED
- Treat post-restoration availability as US-approved-organizations only until docs say otherwise. EVIDENCE-BASED
- Treat Mythos 5 as a high-trust operational instrument, not merely an uncensored chat model; the Glasswing record is about defensive security workflows, validation, disclosure, and remediation. EVIDENCE-BASED

## Pitfalls

- Assuming Mythos 5 is a bigger or smarter model; the difference is the absence of safety classifiers, not capability.
- Calling Mythos 5 "unrestricted" without the trust context; Anthropic still gates access, retains data for safety monitoring, and limits use to vetted partners.
- Searching for a public signup or waitlist; access is invitation-only through account teams.
- Expecting refusal fallback behavior; without classifiers the documented fallback paths do not apply.
- Assuming global availability returned after the export-control lift; restoration was scoped to approved US organizations.
- Citing the claude.ai corpus for Mythos 5 behavior; the consumer capture omits the model entirely.

## Sources

- Introducing Claude Fable 5 and Claude Mythos 5, https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)
- Models overview, https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)
- Project Glasswing, https://www.anthropic.com/glasswing (published 2026-04-07, retrieved 2026-07-07)
- Claude Mythos, https://www.anthropic.com/claude/mythos (retrieved 2026-07-07)
- System Card: Claude Fable 5 and Claude Mythos 5, https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf (published 2026-06-09, retrieved 2026-07-07)
- Expanding Project Glasswing, https://www.anthropic.com/news/expanding-project-glasswing (published 2026-06-02, retrieved 2026-07-07)
- Claude Fable 5 and Claude Mythos 5, https://www.anthropic.com/news/claude-fable-5-mythos-5 (published 2026-06-09, retrieved 2026-07-07)
- Refusals and fallback, https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback (retrieved 2026-07-07)
- Redeploying Claude Fable 5, https://www.anthropic.com/news/redeploying-fable-5 (published 2026-06-30, retrieved 2026-07-07)
- System Prompt Export 2026-07, L17, L21-23 (captured 2026-07-07)

## Related

- [[Claude Fable 5]] - the generally available sibling with safety classifiers added.
- [[Claude 5 Model Family]] - the lineup context where Mythos 5 is the restricted entry.
- [[Mythos-Class Model Tier]] - the capability tier both siblings define.
- [[Project Glasswing]] - the defensive-security program that operationalizes Mythos access.
- [[Fable Mythos 5 System Card]] - the official evidence base for Mythos capability and safeguards.
- [[Fable Mythos Operating Doctrine]] - how to operate the model family without flattening the safety distinction.
- [[Mythos 5 Access Criteria]] - what is known and unknown about qualifying for access.
- [[Fable 5 Dual-Use Safety Measures]] - the exact safeguards Mythos 5 ships without.
- [[Anthropic]] - the vendor, Project Glasswing, and the export-control timeline.
- [[Fable 5 Pricing and Rate Limits]] - shared $10/$50 pricing mechanics.
- [[System Prompt Export 2026-07]] - the consumer capture whose lineup omits Mythos 5.
- [[docs.claude.com]] - where the invitation-only status is documented.

## Next actions

- Fill the Glasswing usage-terms gap by checking https://www.anthropic.com/glasswing for program detail updates.
- Watch the models overview page for any widening of Mythos 5 availability beyond approved US organizations.
- Cross-check future claude.ai captures for whether Mythos 5 ever appears in a consumer lineup.

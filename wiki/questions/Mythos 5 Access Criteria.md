---
type: question
title: "Mythos 5 Access Criteria"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/model
  - note/question
domain: model-and-family
confidence: evidence-based
question: "What must an organization be or do to obtain Claude Mythos 5 access through Project Glasswing?"
answer_quality: draft
related:
  - "[[Claude Mythos 5]]"
  - "[[Mythos-Class Model Tier]]"
  - "[[Project Glasswing]]"
  - "[[Fable Mythos 5 System Card]]"
  - "[[Fable Mythos Operating Doctrine]]"
  - "[[Claude Fable 5]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Anthropic]]"
  - "[[Anthropic Plans and Access Tiers]]"
  - "[[Fable 5 Pricing and Rate Limits]]"
  - "[[Claude 5 Model Family]]"
source_urls:
  - "https://www.anthropic.com/glasswing (retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/expanding-project-glasswing (published 2026-06-02, retrieved 2026-07-07)"
  - "https://www.anthropic.com/claude/mythos (retrieved 2026-07-07)"
  - "https://www.anthropic.com/research/glasswing-initial-update (published 2026-05-22, retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)"
---

# Mythos 5 Access Criteria

The gate is documented (invitation-only Project Glasswing membership via an account team) but the actual approval criteria behind that gate are not public in any source this vault has verified.

## What it is

- A question note on what is known versus unknown about getting Claude Mythos 5, the unclassified twin of Fable 5 that ships without safety classifiers.
- Mythos 5 shares Fable 5's specs and $10/$50 per MTok pricing but is excluded from the general lineup and from the claude.ai consumer prompt.
- This is an access question, not a capability question: the system card now gives public evidence of Mythos capability, but it does not publish the written approval rubric for obtaining it.

## How it works

### What we know

- Mythos 5 is not generally available: it is limited to approved customers in Project Glasswing, and "Access is invitation-only and there is no self-serve sign-up." (https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5).
- Project Glasswing is a defensive cybersecurity program with 12 founding organizations, including Anthropic itself and 11 external partners named at launch such as AWS, Apple, Google, Microsoft, and NVIDIA (https://www.anthropic.com/glasswing, published 2026-04-07).
- Anthropic later described about 50 initial partners and an expansion to about 150 additional organizations across more than 15 countries, spanning power, water, healthcare, communications, hardware, vendors, nonprofits, open source maintainers, and safety testers (https://www.anthropic.com/news/expanding-project-glasswing, published 2026-06-02).
- The current Mythos product page says access is for a small set of trusted partners in cybersecurity, with biology access planned soon (https://www.anthropic.com/claude/mythos, retrieved 2026-07-07).
- Mythos 5 succeeds Claude Mythos Preview, and the documented request path is contacting an Anthropic, AWS, or Google Cloud account team.
- The safety difference is explicit: Fable 5 includes safety classifiers that can decline requests, while Mythos 5 does not include these classifiers.
- Both models are Covered Models with mandatory 30-day retention for safety monitoring and no zero-data-retention option; retained data serves safety purposes, not training.
- Export controls interrupted access: US controls applied June 12, 2026 suspended both models; Anthropic states the controls were lifted June 30 with Fable 5 restored globally July 1 and Mythos 5 restored for a set of approved US organizations.
- The Cyber Verification Program support page is not the Mythos path; it covers Opus and Sonnet real-time cyber safeguards, not Glasswing admission.

### What we do not know

> [!gap]
> No verified source states the written approval criteria for Glasswing membership, the vetting process, contract terms, monitoring obligations, whether the approved-organization set changed after the export-control episode, or any plan to widen Mythos access beyond trusted partners.

### What would resolve it

- A published Glasswing membership criteria document or application page.
- Dated reporting naming organizations approved or rejected and why.

## Best practice

- Route access requests through an Anthropic, AWS, or Google Cloud account team; that is the only documented path. EVIDENCE-BASED
- Plan architectures on Fable 5, which delivers Mythos-level capabilities with safeguards and is generally available. EVIDENCE-BASED
- Note the restoration-scope asymmetry after the export-control episode: Fable 5 global, Mythos 5 approved US organizations only. EVIDENCE-BASED
- Treat Glasswing fit as an operational trust case: defensive mission, high-value software, validation capacity, disclosure process, and remediation plan. PRACTITIONER
- Treat any third-party claim about Glasswing criteria as unverified until Anthropic documents it. PRACTITIONER

## Pitfalls

- Assuming money is the gate; pricing is identical to Fable 5, so approval, not budget, is the constraint.
- Treating the 12 founding organizations as the full current membership; Anthropic later reported about 50 initial partners and about 150 additional organizations.
- Reading "restored for a set of approved US organizations" as the original partner list; the mapping is unverified.
- Confusing the Cyber Verification Program with Mythos access; the support page scope is Opus and Sonnet safeguards.
- Date confusion around restoration: Anthropic says lifted June 30, restored July 1, while Al Jazeera reports notification July 1 and restoration from July 2; treat exact dates as contested.

## Sources

- Project Glasswing, https://www.anthropic.com/glasswing (retrieved 2026-07-07, published 2026-04-07).
- Expanding Project Glasswing, https://www.anthropic.com/news/expanding-project-glasswing (retrieved 2026-07-07, published 2026-06-02).
- Claude Mythos, https://www.anthropic.com/claude/mythos (retrieved 2026-07-07).
- Project Glasswing initial update, https://www.anthropic.com/research/glasswing-initial-update (retrieved 2026-07-07, published 2026-05-22).
- Introducing Claude Fable 5 and Claude Mythos 5, https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07).
- Models overview, https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07).
- Redeploying Claude Fable 5, https://www.anthropic.com/news/redeploying-fable-5 (retrieved 2026-07-07, published 2026-06-30).
- Real-time cyber safeguards on Claude Opus and Sonnet, https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude-opus-and-sonnet (retrieved 2026-07-07).
- US lifts restrictions on Anthropic's AI models, https://www.aljazeera.com/economy/2026/7/1/us-lifts-restrictions-on-powerful-ai-models-fable-mythos-anthropic-says (retrieved 2026-07-07, published 2026-07-01).

## Related

- [[Claude Mythos 5]] is the model this access gate protects.
- [[Mythos-Class Model Tier]] explains the capability tier above Opus that both twins share.
- [[Project Glasswing]] is the program-level record behind the gate.
- [[Fable Mythos 5 System Card]] separates capability evidence from access eligibility.
- [[Fable Mythos Operating Doctrine]] describes how to reason about Fable versus Mythos in practice.
- [[Claude Fable 5]] is the generally available alternative with classifiers.
- [[Fable 5 Dual-Use Safety Measures]] details the classifier difference that justifies the gate.
- [[Anthropic]] runs Project Glasswing and the account-team access path.
- [[Anthropic Plans and Access Tiers]] situates Glasswing among other access mechanisms.
- [[Fable 5 Pricing and Rate Limits]] is the sibling question on the open twin.
- [[Claude 5 Model Family]] shows where Mythos 5 sits in the lineup docs.

## Next actions

- Watch anthropic.com/glasswing for published membership criteria or an application flow.
- Log any dated reporting that names post-restoration approved organizations.
- Upgrade answer_quality past draft only once written criteria, contract terms, or monitoring obligations surface.

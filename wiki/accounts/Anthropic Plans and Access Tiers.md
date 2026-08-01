---
type: account
title: "Anthropic Plans and Access Tiers"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/model
  - note/account
domain: model-and-family
confidence: evidence-based
related:
  - "[[Claude Fable 5]]"
  - "[[Claude Mythos 5]]"
  - "[[Project Glasswing]]"
  - "[[Mythos 5 Access Criteria]]"
  - "[[Mythos-Class Model Tier]]"
  - "[[Fable Mythos Operating Doctrine]]"
  - "[[claude.ai Platform]]"
  - "[[Claude Code Platform]]"
  - "[[Claude Console and API Platform]]"
  - "[[Fable 5 Pricing and Rate Limits]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Anthropic]]"
source_urls:
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
  - "https://www.anthropic.com/glasswing (retrieved 2026-07-07)"
  - "https://www.anthropic.com/claude/mythos (retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/expanding-project-glasswing (published 2026-06-02, retrieved 2026-07-07)"
---

# Anthropic Plans and Access Tiers

Claude Fable 5 ships to the paid subscription tiers, Pro, Max, Team, and Enterprise, on both claude.ai and Claude Code, while Claude Mythos 5 stays invitation-only through Project Glasswing with no self-serve sign-up.

## What it is

The map from Anthropic account type to model access as of July 2026. Three access routes exist: subscription plans (claude.ai and Claude Code), usage-priced API and cloud access (Claude API, Amazon Bedrock, Google Cloud, Microsoft Foundry), and the gated Glasswing program for Mythos 5. The tier question matters because Fable 5 is a Mythos-class model made broadly available: "Fable 5's capabilities exceed those of any model we've ever made generally available." (https://www.anthropic.com/news/claude-fable-5-mythos-5), while the classifier-free Mythos 5 is deliberately withheld from general tiers.

## How it works

- **Subscription tiers.** Fable 5 is deployed in claude.ai and Claude Code for Pro, Max, Team, and Enterprise users, generally available since June 9, 2026, with the June 12 to July 1 export-control interruption in between.
- **Pricing position.** Fable 5 and Mythos 5 share the same $10/$50 per MTok rate, less than half the price of the Claude Mythos Preview they succeed, so the Glasswing gate is about eligibility, not price.
- **API and cloud.** Any API customer reaches Fable 5 at $10 per million input tokens and $50 per million output tokens; the same GA covers Claude Platform on AWS, Amazon Bedrock (US East N. Virginia, Europe Stockholm), Google Cloud, and Microsoft Foundry.
- **Glasswing gate.** Claude Mythos 5 is limited to approved customers in Project Glasswing, a defensive cybersecurity program that began with 12 founding organizations, was later summarized as about 50 initial partners, and expanded to about 150 additional organizations across more than 15 countries. It succeeds Claude Mythos Preview, and access requires contacting an Anthropic, AWS, or Google Cloud account team: "Access is invitation-only and there is no self-serve sign-up." (https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5).
- **Current Mythos page.** Anthropic's current Mythos page says access is for a small set of trusted partners doing cybersecurity work, with biology access planned soon, and that restored access on July 1, 2026 was limited to a set of US organizations.
- **What separates the tiers technically.** Fable 5 includes safety classifiers that can decline requests; Mythos 5 does not include these classifiers. The tier boundary is therefore a safety boundary, not just a commercial one.
- **Covered Model terms.** Both models carry mandatory 30-day data retention for safety monitoring and are excluded from zero data retention, regardless of account tier.
- **Assurance behind the broad tier.** Anthropic backs the wide Fable 5 release with red-teaming evidence: over 1,000 hours of external red-teaming produced no universal jailbreaks, and the classifiers "trigger, on average, in less than 5% of sessions" per the launch post.

> [!key-insight]
> The tier map encodes Anthropic's dual-use bet: identical capability class, two distributions. Fable 5 pairs Mythos-level capability with classifiers and sells broadly; Mythos 5 removes the classifiers and narrows distribution to vetted defenders. Account tier is the delivery mechanism for that safety split.

## Best practice

- Choose the access route by need: subscription for interactive claude.ai and Claude Code work, API for programmatic and volume workloads. PRACTITIONER
- Do not plan projects around Mythos 5 unless a Glasswing invitation exists; the approval path runs through Anthropic, AWS, or Google Cloud account teams, not a signup form. EVIDENCE-BASED
- Verify tier claims against the dated docs page before quoting them; access rules changed twice within June 2026. EVIDENCE-BASED
- For compliance-sensitive accounts, check the Covered Model retention terms early; no tier buys zero data retention on Fable 5 or Mythos 5. EVIDENCE-BASED
- Treat Fable 5 on a paid plan as the practical ceiling of Anthropic capability for general users; Mythos-level capability without classifiers is not purchasable. EVIDENCE-BASED
- Treat Mythos 5 as a program relationship, not a premium plan. PRACTITIONER
- Budget API access against the published rates: Fable 5 at $10/$50 per MTok sits above Opus 4.8 ($5/$25), Sonnet 5 ($3/$15), and Haiku 4.5 ($1/$5), so tier choice and model choice are separate decisions. EVIDENCE-BASED

## Pitfalls

- Assuming a Max or Enterprise plan implies eventual Mythos 5 access; plan tier and Glasswing approval are unrelated gates.
- Reading "generally available" as uninterrupted: all Fable 5 access was suspended June 12 to June 30, 2026 under US export controls, and the exact restoration date is contested between Anthropic (July 1) and Al Jazeera (July 2).
- Equating claude.ai plan features with API entitlements; the API is usage-priced and independent of subscription tier.
- Overlooking that Mythos 5's restoration after the export-control lift covered only a set of approved US organizations, narrower than Fable 5's global restoration.
- Presenting the original 12 founding organizations as the whole program; the expansion materially changed the program size and sectors.
- Presenting the tier map without dates; every statement here is as of July 2026 and access policy has already changed twice since launch.

> [!gap]
> Whether the claude.ai free tier receives any Fable 5 access, and what usage caps distinguish Pro from Max for Fable 5, is not stated in this brain's verified sources; the packs name only the four paid tiers. File under [[Fable 5 Pricing and Rate Limits]] when a source lands.

## Sources

- Introducing Claude Fable 5 and Claude Mythos 5, Claude Platform docs: https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)
- Claude Fable 5 and Claude Mythos 5, Anthropic news: https://www.anthropic.com/news/claude-fable-5-mythos-5 (published 2026-06-09, retrieved 2026-07-07)
- Project Glasswing, Anthropic: https://www.anthropic.com/glasswing (published 2026-04-07, retrieved 2026-07-07)
- Claude Mythos, Anthropic: https://www.anthropic.com/claude/mythos (retrieved 2026-07-07)
- Expanding Project Glasswing, Anthropic: https://www.anthropic.com/news/expanding-project-glasswing (published 2026-06-02, retrieved 2026-07-07)
- Models overview, Claude Platform docs: https://platform.claude.com/docs/en/about-claude/models/overview (retrieved 2026-07-07)
- Redeploying Claude Fable 5, Anthropic news: https://www.anthropic.com/news/redeploying-fable-5 (published 2026-06-30, retrieved 2026-07-07)

## Related

- [[Claude Fable 5]] because tier access defines who can use the flagship model.
- [[Claude Mythos 5]] because the gated sibling defines the ceiling above the tiers.
- [[Project Glasswing]] because it is the actual Mythos 5 access program.
- [[Mythos 5 Access Criteria]] because the Glasswing approval path is detailed there.
- [[Mythos-Class Model Tier]] because the capability class explains why the gate exists.
- [[Fable Mythos Operating Doctrine]] because model choice needs operational context, not just account labels.
- [[claude.ai Platform]] because subscription tiers manifest there first.
- [[Claude Code Platform]] because the same plans gate the developer harness.
- [[Claude Console and API Platform]] because usage-priced access bypasses plan tiers.
- [[Fable 5 Pricing and Rate Limits]] because caps and pricing flesh out tier value.
- [[Fable 5 Dual-Use Safety Measures]] because classifiers are the technical tier boundary.
- [[Anthropic]] because the vendor sets and revises this access policy.

## Next actions

- Source the free-tier and Pro-versus-Max usage cap facts and close the gap callout.
- Add the Glasswing partner list beyond the five named founders when published.
- Re-verify tier availability after the next model or plan announcement.
- Note which tier this vault's own operation runs on and what that implies for Fable 5 access.

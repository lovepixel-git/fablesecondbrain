---
type: entity
title: "Anthropic"
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
  - "[[Claude Mythos 5]]"
  - "[[Claude 5 Model Family]]"
  - "[[Claude Code]]"
  - "[[Claude Cowork]]"
  - "[[Claude Beta Surface Agents]]"
  - "[[Anthropic API and Claude Platform]]"
  - "[[claude.ai Platform]]"
  - "[[Mythos 5 Access Criteria]]"
  - "[[docs.claude.com]]"
source_urls:
  - "https://www.anthropic.com/news/claude-fable-5-mythos-5 (retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/redeploying-fable-5 (retrieved 2026-07-07)"
  - "https://www.aljazeera.com/economy/2026/7/1/us-lifts-restrictions-on-powerful-ai-models-fable-mythos-anthropic-says (retrieved 2026-07-07)"
  - "https://www.anthropic.com/glasswing (retrieved 2026-07-07)"
  - "https://www.anthropic.com/claude/fable (retrieved 2026-07-07)"
  - "https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Anthropic

Anthropic is the AI company behind the Claude models and product surfaces; in June 2026 it shipped Claude Fable 5 and Claude Mythos 5, weathered a US export-control suspension of both models, and restored access by early July under a contested exact timeline.

## What it is

- The maker of the [[Claude 5 Model Family]]: Claude Fable 5, Claude Mythos 5, Opus 4.8, Sonnet 5, and Haiku 4.5, all pinned-snapshot model IDs.
- Product surfaces per the claude.ai capture include [[Claude Code]] and "Claude Cowork, an agentic knowledge-work desktop app for non-developers" (System Prompt Export 2026-07, L25-27).
- The same capture lists beta agents Claude in Chrome, Claude in Excel, and Claude in Powerpoint, all usable as tools by Cowork; see [[Claude Beta Surface Agents]].
- Distribution spans the Claude API, Claude Platform on AWS, Amazon Bedrock, Google Cloud, and Microsoft Foundry, plus claude.ai and Claude Code for Pro, Max, Team, and Enterprise users.
- It runs Project Glasswing, a defensive cybersecurity program with 12 founding partners including AWS, Apple, Google, Microsoft, and NVIDIA, which gates [[Claude Mythos 5]] access (https://www.anthropic.com/glasswing, published 2026-04-07).

> [!gap] The research pack contains no claim about Anthropic's advertising policy stance. Do not state a position on ads in Claude products until a dated source lands in the pack.

## How it works

- Safety posture on the flagship: Fable 5 ships with safety classifiers that can decline requests, Mythos 5 ships without them to approved organizations only, and both are Covered Models with mandatory 30-day retention used for safety purposes, not training.
- Export-control episode, June 2026: US export controls applied on 2026-06-12 led Anthropic to suspend all access to Fable 5 and Mythos 5.
- Anthropic's account of the restoration: "the export controls on Fable 5 and Mythos 5 have been lifted" (https://www.anthropic.com/news/redeploying-fable-5), dating the lift to 2026-06-30, with Fable 5 restored globally on 2026-07-01 and Mythos 5 restored for a set of approved US organizations.
- The platform docs confirm access has been restored as of the 2026-07-07 retrieval.
- Al Jazeera reports a different sequence: Commerce Department notification on 2026-07-01 with restoration beginning 2026-07-02.

> [!contradiction] Restoration timing is reported inconsistently: Anthropic says lift 2026-06-30 and global restoration 2026-07-01; Al Jazeera says notification 2026-07-01 and restoration from 2026-07-02. Prefer Anthropic's first-party dates but carry both until a definitive account appears. CONTESTED

- The company positions Fable 5 as its most capable widely released model, stating "Fable 5's capabilities exceed those of any model we've ever made generally available" (https://www.anthropic.com/news/claude-fable-5-mythos-5).
- Its own consumer harness distrusts model memory for product facts: "Any time you would otherwise rely on memory for Anthropic product details, verify here instead" (System Prompt Export 2026-07, L3756-3758).

## Best practice

- Corroborate every Anthropic product claim with a dated public Anthropic URL before tagging it; that is what upgrades a claim to EVIDENCE-BASED. EVIDENCE-BASED
- Track anthropic.com/news for availability changes; the June 2026 suspension shows GA access can vanish within days of launch. EVIDENCE-BASED
- Cite the restoration timeline with both first-party and press dates until the discrepancy resolves. CONTESTED
- Confirm Covered Model retention terms with an account team before committing regulated workloads. PRACTITIONER
- Verify product facts against current docs instead of training memory, exactly as Anthropic instructs its own harness. EVIDENCE-BASED

## Pitfalls

- Assuming general availability is durable; the export-control suspension hit three days after launch.
- Conflating Project Glasswing (the program, published 2026-04-07) with Mythos 5 (the model it gates).
- Citing a single restoration date without flagging the Anthropic versus Al Jazeera discrepancy.
- Stating an ads policy position; the pack holds no evidence either way.
- Treating the claude.ai capture's product list as complete or current; it is a 2026-06-09 snapshot.

## Sources

- Claude Fable 5 and Claude Mythos 5, https://www.anthropic.com/news/claude-fable-5-mythos-5 (published 2026-06-09, retrieved 2026-07-07)
- Redeploying Claude Fable 5, https://www.anthropic.com/news/redeploying-fable-5 (published 2026-06-30, retrieved 2026-07-07)
- US lifts restrictions on Anthropic's powerful AI models Fable and Mythos, https://www.aljazeera.com/economy/2026/7/1/us-lifts-restrictions-on-powerful-ai-models-fable-mythos-anthropic-says (published 2026-07-01, retrieved 2026-07-07)
- Project Glasswing, https://www.anthropic.com/glasswing (published 2026-04-07, retrieved 2026-07-07)
- Claude Fable product page, https://www.anthropic.com/claude/fable (retrieved 2026-07-07)
- Anthropic Claude Fable 5 on AWS, https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available (published 2026-06-09, retrieved 2026-07-07)
- System Prompt Export 2026-07, L25-27, L3756-3758 (captured 2026-07-07)

## Related

- [[Claude Fable 5]] - the flagship GA model at the center of the June 2026 events.
- [[Claude Mythos 5]] - the restricted sibling gated behind Project Glasswing.
- [[Claude 5 Model Family]] - the full lineup Anthropic currently ships.
- [[Claude Code]] - Anthropic's developer agent harness.
- [[Claude Cowork]] - the knowledge-work desktop app named in the capture.
- [[Claude Beta Surface Agents]] - Chrome, Excel, and Powerpoint beta agents.
- [[Anthropic API and Claude Platform]] - the first-party API distribution channel.
- [[claude.ai Platform]] - the consumer surface the corpus documents.
- [[Mythos 5 Access Criteria]] - how Glasswing gating works in practice.
- [[docs.claude.com]] - the documentation site this brain cites for product facts.

## Next actions

- Watch for a definitive account reconciling the 2026-06-30/07-01 versus 07-01/07-02 restoration dates.
- Add an ads policy claim to the pack if a dated Anthropic statement is found, then close the gap callout.
- Track whether Claude Cowork and the beta surface agents gain public documentation beyond the capture.

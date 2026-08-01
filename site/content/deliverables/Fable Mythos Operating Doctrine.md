---
type: deliverable
title: "Fable Mythos Operating Doctrine"
status: mature
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/best-practices
  - note/deliverable
domain: best-practices
confidence: evidence-based
related:
  - "[[Claude Fable 5]]"
  - "[[Claude Mythos 5]]"
  - "[[Project Glasswing]]"
  - "[[Fable Mythos 5 System Card]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Adaptive Thinking and Thinking Mode]]"
  - "[[System Prompt Design Logic]]"
  - "[[Claude Code Quickstart for Fable 5]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://www.anthropic.com/news/claude-fable-5-mythos-5 (published 2026-06-09, retrieved 2026-07-07)"
  - "https://www.anthropic.com/claude/mythos (retrieved 2026-07-07)"
  - "https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf (published 2026-06-09, retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/migration-guide (retrieved 2026-07-07)"
  - "https://support.claude.com/en/articles/15363606-why-claude-switched-models-in-your-conversation-with-fable-5 (retrieved 2026-07-07)"
---

# Fable Mythos Operating Doctrine

Operate Fable 5 as the general-access Mythos-class workhorse and Mythos 5 as a restricted, monitored, trusted-access capability for vetted defensive cyber and biology work.

## What it is

- A practical doctrine for the knowledge, principles, methodology, mentality, skills, and execution posture of current Fable and Mythos-class models.
- It distills official docs, support pages, Project Glasswing updates, and the Fable/Mythos 5 system card.
- It is not an access request guide or a cyber operations playbook.
- It is a decision guide for safe, high-leverage model use.

## How it works

1. Capability is shared, deployment is not.
   Fable 5 and Mythos 5 share the same underlying model. Fable is broadly available with safeguards. Mythos removes relevant safeguards but is restricted to trusted partners.

2. Treat Fable as a safeguarded router.
   In cyber, biology, distillation, reasoning-extraction, and narrow frontier-LLM development contexts, Fable 5 is not just a model response. It can block, refuse, silently limit effectiveness in some frontier-AI cases, or route to Opus 4.8 depending on surface.

3. Treat Mythos as governed access.
   Mythos 5 is not a better subscription tier. It is a trusted-access program for work Anthropic considers too dual-use for ordinary broad release.

4. Keep the evidence boundary sharp.
   System prompt exports prove claude.ai behavior. API docs prove API behavior. Support articles prove product-surface behavior. System cards prove evaluation and safety claims.

5. Optimize for verification, not vibes.
   The model class is strong enough that false confidence becomes expensive. Every serious workflow needs tests, logs, fallback accounting, and source-dated claims.

6. Use adaptive thinking correctly.
   Fable and Mythos use adaptive thinking. Do not send manual thinking budgets. Use the effort parameter for depth, and treat thinking blocks as display or continuation state, never as raw reasoning.

7. Design for fallbacks.
   In Claude apps, automatic model switching can rerun blocked Fable requests on Opus 4.8 and then leave the conversation on Opus. In the API, fallback is opt-in or client-side.

8. Log the serving model.
   If a Fable session switches to Opus, outputs are not Fable outputs. Record model, surface, fallback event, refusal category, and billing consequence.

9. Respect retention constraints.
   Fable 5 and Mythos 5 are Covered Models. If zero data retention is mandatory, do not route work to them.

10. Keep dual-use work in the right lane.
    Ordinary defensive work can often use Fable or Opus. High-risk dual-use work belongs in documented verification or trusted-access programs, not prompt workarounds.

## Best practice

- Start from Fable 5 for ambitious coding, agentic, vision, and knowledge-work tasks when cost and retention are acceptable. EVIDENCE-BASED
- Use Sonnet or Opus when Fable's safeguard boundary would add friction and Mythos access is not available. PRACTITIONER
- Use Mythos only when the organization is approved and the task fits the trusted-access purpose. EVIDENCE-BASED
- For Claude Code, give Fable a verifiable check: tests, build, screenshot comparison, or a deterministic report. EVIDENCE-BASED
- For long jobs, preserve state outside the chat: repo files, progress notes, source ledgers, and test artifacts. EVIDENCE-BASED
- For research, ask for dated official sources first, then record claims in the ledger before they become doctrine. EVIDENCE-BASED
- For model migration, remove manual thinking budgets, remove unsupported assistant prefill, rebaseline costs, and handle refusals as successful stop reasons. EVIDENCE-BASED
- For cyber and bio tasks, expect broad blocking, especially when the request or attached context looks near high-risk use. EVIDENCE-BASED
- For prompt design, use the seven prompt-design moves from [[System Prompt Design Logic]]: checklist before capability, cost-scaled effort, examples as spec, repeated guardrails, conflict law, invisible machinery, and motivated instructions. EVIDENCE-BASED
- For any public claim, attach source type, retrieval date, confidence, and scope. EVIDENCE-BASED

## Pitfalls

- Treating Mythos as just "Fable but unlocked." The access model, monitoring, and purpose are part of the product.
- Treating Fable fallback output as Fable output.
- Comparing Fable and Mythos benchmarks without noting whether Fable's classifiers fired.
- Designing a workflow that depends on zero data retention.
- Asking Fable to expose raw chain of thought or to transcribe internal reasoning.
- Using public prompt captures to claim Claude Code behavior.
- Ignoring the Project Glasswing lesson that patching throughput is the bottleneck after model-assisted discovery.
- Treating press-only country or partner claims as official program facts.
- Treating "no CB-2" as "low bio risk." Anthropic says the judgment is less clear than before and risk is higher than for previous models.
- Treating "no universal jailbreak" as "no jailbreak risk."

## Sources

- Claude Fable 5 and Claude Mythos 5, Anthropic: https://www.anthropic.com/news/claude-fable-5-mythos-5 (published 2026-06-09, retrieved 2026-07-07).
- Claude Mythos product page, Anthropic: https://www.anthropic.com/claude/mythos (retrieved 2026-07-07).
- Claude Fable 5 and Claude Mythos 5 System Card, Anthropic PDF: https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf (published 2026-06-09, retrieved 2026-07-07).
- Migration guide, Claude Platform Docs: https://platform.claude.com/docs/en/about-claude/models/migration-guide (retrieved 2026-07-07).
- Refusals and fallback, Claude Platform Docs: https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback (retrieved 2026-07-07).
- Why Claude switched models in your conversation with Fable 5, Claude Help Center: https://support.claude.com/en/articles/15363606-why-claude-switched-models-in-your-conversation-with-fable-5 (retrieved 2026-07-07).
- Data retention practices for Mythos-class models, Claude Help Center: https://support.claude.com/en/articles/15425996 (retrieved 2026-07-07).
- Project Glasswing initial update, Anthropic: https://www.anthropic.com/research/glasswing-initial-update (published 2026-05-22, retrieved 2026-07-07).

## Related

- [[Claude Fable 5]] is the general-access model this doctrine mostly operates.
- [[Claude Mythos 5]] is the trusted-access model this doctrine scopes narrowly.
- [[Project Glasswing]] explains the trusted-access program logic.
- [[Fable Mythos 5 System Card]] supplies the public evaluation evidence.
- [[Fable 5 Dual-Use Safety Measures]] details classifier and fallback behavior.
- [[Adaptive Thinking and Thinking Mode]] defines the reasoning controls.
- [[System Prompt Design Logic]] supplies the prompt-design philosophy.
- [[Claude Code Quickstart for Fable 5]] turns part of this doctrine into a setup sequence.
- [[Claim Verification Flow]] is the evidence discipline behind every claim here.

## Next actions

- Convert this doctrine into a one-page checklist for daily Claude Code work.
- Build a capability matrix from the system card that separates unsafeguarded Mythos results from deployed Fable results.
- Add a fallback logging schema for Claude Code and API harnesses.
- Create an internal eval pack for the user's actual workflows before making model-cost recommendations.
- Re-run this doctrine after each source refresh or model redeployment.

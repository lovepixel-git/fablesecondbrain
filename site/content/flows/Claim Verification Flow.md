---
type: flow
title: "Claim Verification Flow"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/best-practices
  - note/flow
domain: best-practices
confidence: practitioner
approval_status: approved
risk_level: low
rollback_note: "Verification changes confidence fields and callouts in wiki notes under git; revert the verification commit to restore prior tags."
related:
  - "[[Confidence Tag Policy]]"
  - "[[Citation Discipline]]"
  - "[[Brain Refresh Flow]]"
  - "[[Corpus Ingestion Flow]]"
  - "[[Multi-Agent Fan-Out Research Flow]]"
  - "[[Claude Code Subagents]]"
  - "[[No Public Fable 5 Benchmark Data]]"
  - "[[Anthropic Engineering Blog Shelf]]"
  - "[[Explore Plan Code Commit]]"
  - "[[research-pack-2026-07-07|Research Pack 2026-07-07]]"
source_urls:
  - "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents (retrieved 2026-07-07)"
  - "https://knightli.com/en/2026/06/10/claude-fable-5-prompting-guide/ (retrieved 2026-07-07)"
---

# Claim Verification Flow

Every claim in this brain survives an adversarial check before it is asserted: an independent second source confirms it or the claim is downgraded to CONTESTED with a caveat, and verification runs in fresh context rather than as author self-critique.

## What it is

The verify pattern used to build this brain. Each research claim ships with a primary source, a retrieval date, and a SECOND-SOURCE line; the confidence tag is then assigned by the [[Confidence Tag Policy]] ladder (evidence-based, practitioner, contested, folklore-demoted). The pattern applies Anthropic's own findings about verification: on long autonomous Fable 5 runs, forcing every progress claim to be audited against a tool result nearly eliminates fabricated status reports, and "separate fresh-context verifier subagents outperform self-critique" is the operative design rule (https://knightli.com/en/2026/06/10/claude-fable-5-prompting-guide/).

## How it works

1. **Draft.** State the claim declaratively with its primary source URL and retrieval date. Corpus claims additionally carry an exact line reference.
2. **Attack.** Actively hunt a disconfirming or independent corroborating source. A second page on the same site counts only when it is a distinct document; a bestseller or popularity is not evidence.
3. **Tag.** Corroborated by authoritative primary data or an official dated URL: EVIDENCE-BASED. Plausible operational advice without official confirmation: PRACTITIONER. Sources conflict: CONTESTED, with a `> [!contradiction]` callout in the owning note until a newer official source resolves it. No credible support: FOLKLORE, demoted and never asserted as fact.
4. **Verify fresh.** A verifier that did not write the claim rechecks it, in a separate context, mirroring how eval design separates the agent doing the work from the agent judging it.
5. **Record.** File the claim with its tag, sources, and dates so the [[Brain Refresh Flow]] can re-verify it later.

Worked examples from this brain's own packs: the Fable 5 restoration timeline is CONTESTED because Anthropic says lifted June 30 and restored July 1 while Al Jazeera reports notification July 1 and restoration July 2; Simon Willison's day-one impressions stay CONTESTED as a single practitioner account.

> [!key-insight]
> The flow's asymmetry is deliberate: promoting a claim requires new independent evidence, demoting one requires only a single credible conflict. Errors therefore decay toward CONTESTED instead of hardening into vault facts.

## Best practice

- Require an independent second source before asserting; single-sourced claims stay flagged. PRACTITIONER
- Use fresh-context verifiers, not self-critique; the separation measurably improves reliability on Fable 5 class models. EVIDENCE-BASED
- Audit progress claims against tool results, not memory; on long runs "this nearly eliminated fabricated status reports even on tasks designed to elicit them" (https://knightli.com/en/2026/06/10/claude-fable-5-prompting-guide/). PRACTITIONER
- Combine grader types the way Anthropic's eval guidance does, code-based, model-based, and human, rather than trusting any single judge. EVIDENCE-BASED
- Seed the check set from real failures: start with 20 to 50 tasks drawn from actual mistakes, and watch for saturation, since "Eval saturation occurs when an agent passes all solvable tasks" (https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents). EVIDENCE-BASED
- Downgrade loudly: CONTESTED claims keep both sources and a visible callout instead of silently picking a winner. PRACTITIONER
- Date everything; an undated verification cannot be re-verified. PRACTITIONER

## Pitfalls

- Circular corroboration: a syndicated copy of the primary source is not a second source.
- Letting the author verify its own work in the same context; that is self-critique, the weaker pattern.
- Treating vendor claims as settled: the multi-agent 90.2 percent figure and the C compiler team result are single-vendor experiments and are handled with care in this vault.
- Tag inflation: promoting PRACTITIONER advice to EVIDENCE-BASED because it appears often; frequency is popularity, not evidence.
- Verifying the link instead of the claim; content drifts under stable URLs.

## Sources

- Demystifying evals for AI agents, Anthropic Engineering: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents (published 2026-01-09, retrieved 2026-07-07)
- Claude Fable 5 prompting guide (fresh-context verifier finding), Knight Li: https://knightli.com/en/2026/06/10/claude-fable-5-prompting-guide/ (published 2026-06-10, retrieved 2026-07-07)
- Harness design for long-running application development (worker versus judge separation), Anthropic Engineering: https://www.anthropic.com/engineering/harness-design-long-running-apps (published 2026-03-24, retrieved 2026-07-07)
- Redeploying Claude Fable 5 (contested-timeline worked example), Anthropic: https://www.anthropic.com/news/redeploying-fable-5 (published 2026-06-30, retrieved 2026-07-07)

## Related

- [[Confidence Tag Policy]] because the tag ladder is this flow's output vocabulary.
- [[Citation Discipline]] because sources, dates, and L-refs are the verifiable inputs.
- [[Brain Refresh Flow]] because refresh is this flow rerun on aging claims.
- [[Corpus Ingestion Flow]] because newly filed corpus claims enter verification immediately.
- [[Multi-Agent Fan-Out Research Flow]] because this brain's build ran verification as a fan-out stage.
- [[Claude Code Subagents]] because fresh-context verifiers are implemented as subagents.
- [[No Public Fable 5 Benchmark Data]] because that note shows the flow first refusing to invent evidence, then resolving the gap when the system card was integrated.
- [[Anthropic Engineering Blog Shelf]] because most evidence-based tags trace to shelf posts.
- [[Explore Plan Code Commit]] because its verify-before-commit step is the same principle in code.
- [[research-pack-2026-07-07|Research Pack 2026-07-07]] because the pack holds the verified claim records.

## Next actions

- Build the brain's regression set: 20 spot-check claims re-verified on every audit run.
- Add a lint rule flagging any claim body without a date or second-source marker.
- Re-run verification on all CONTESTED claims when the next official source lands.
- Pair each single-sourced practitioner claim with an official doc candidate at the next refresh.

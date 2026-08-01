---
type: deliverable
title: "Fable 5 Best Practices Cheat Sheet"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/best-practices
  - note/deliverable
domain: best-practices
confidence: evidence-based
related:
  - "[[Claude Fable 5]]"
  - "[[Model Selection for Agent Workloads]]"
  - "[[Prompting Fable 5 One-Pager]]"
  - "[[Claude Code Quickstart for Fable 5]]"
  - "[[Extended Thinking Budgets]]"
  - "[[Claude Code Hooks]]"
  - "[[Context Window Management]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Prompt Caching Economics]]"
  - "[[Explore Plan Code Commit]]"
source_urls:
  - "https://www.anthropic.com/news/claude-fable-5-mythos-5 (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview (retrieved 2026-07-07)"
---

# Fable 5 Best Practices Cheat Sheet

The fifteen highest-leverage verified practices for operating Claude Fable 5 across model choice, prompting, context, and safety, each with a source and a confidence tag.

## What it is

- A one-page operator cheat sheet distilled from the vault's verified claim packs of 2026-07-07.
- Scope: the model itself (choice, effort, refusals, cost) plus the two main harness disciplines, prompting and Claude Code operation.
- Every practice below is a single claim with a single tag; deeper treatment lives in the linked notes.

## How it works

- Claims were verified against dated official pages (Anthropic news, Claude Platform docs, code.claude.com docs) and tagged per [[Confidence Tag Policy]].
- EVIDENCE-BASED means a dated public Anthropic URL corroborates the practice; PRACTITIONER means converging field practice without official confirmation.
- Sources are cited inline per practice and collected under Sources.

## Best practice

1. Default to Fable 5 when capability dominates cost; Anthropic states "Fable 5's capabilities exceed those of any model we've ever made generally available." (https://www.anthropic.com/news/claude-fable-5-mythos-5). EVIDENCE-BASED
2. Control depth with the `effort` parameter, not thinking budgets: high is the default, xhigh serves the most capability-sensitive workloads, and `budget_tokens` returns a 400 error on Fable 5 (https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking). EVIDENCE-BASED
3. Lower effort before switching models for cost control; "Lower effort settings on Claude Fable 5 still perform well" and often exceed xhigh performance of prior models (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5). EVIDENCE-BASED
4. Architect for refusals: handle stop_reason "refusal" with its stop_details category, and enable Claude Opus 4.8 fallback via the server-side fallbacks parameter (beta header server-side-fallback-2026-06-01) or SDK middleware; a refusal before any output is unbilled (https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback). EVIDENCE-BASED
5. Exploit the 90% prompt-caching input discount against the $10/$50 per MTok list price on repeated-context workloads (https://www.anthropic.com/claude/fable). EVIDENCE-BASED
6. Write clear, explicit instructions with numbered steps when order matters, and request above-and-beyond behavior explicitly (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview). EVIDENCE-BASED
7. Give the motivation behind an instruction; Fable 5 performs better when told why a request matters, since "Claude is smart enough to generalize from the explanation." (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5). EVIDENCE-BASED
8. Structure complex prompts with consistent XML tags and wrap 3 to 5 relevant, diverse few-shot examples in example tags (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview). EVIDENCE-BASED
9. In long-context prompts (20k+ tokens), put documents at the top, the query at the end, and ask for grounding quotes first; end-placed queries improved response quality "up to 30% in tests" (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview). EVIDENCE-BASED
10. Never instruct Fable 5 to echo or transcribe its internal reasoning in response text; that can trigger the reasoning_extraction refusal category. Read structured thinking blocks instead (https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking). EVIDENCE-BASED
11. Refactor prompts and skills written for earlier models rather than copying them; overly prescriptive instructions can degrade output quality on the stronger model (https://knightli.com/en/2026/06/10/claude-fable-5-prompting-guide/). PRACTITIONER
12. In Claude Code, give the model a verifiable check so the loop closes without you: "Give Claude a check it can run: tests, a build, a screenshot to compare." (https://code.claude.com/docs/en/best-practices). EVIDENCE-BASED
13. Follow explore, plan, implement, commit, but skip the overhead for small fixes: "If you could describe the diff in one sentence, skip the plan." (https://code.claude.com/docs/en/best-practices). EVIDENCE-BASED
14. Keep CLAUDE.md short and broadly applicable, target under 200 lines per file, and move procedures into skills that load on demand (https://code.claude.com/docs/en/memory). EVIDENCE-BASED
15. Practice context economy: /clear between unrelated tasks, delegate scoped research to subagents, and after roughly two failed corrections start a fresh session with a better prompt (https://code.claude.com/docs/en/best-practices). EVIDENCE-BASED

## Pitfalls

- Enforcing mandatory rules with prose instead of hooks; hooks are deterministic, and policy hooks must exit 2 because exit 1 does not block (practitioner consensus, https://blakecrosley.com/blog/claude-code-hooks-explained).
- Forgetting Fable 5 is a Covered Model: 30-day data retention for safety monitoring is mandatory and zero data retention is unavailable, which matters for compliance-sensitive deployments.
- Budgeting from anecdote: day-one testing found Fable 5 slow and expensive ($110.42 in about 5.5 hours), but that figure is a contested single-practitioner data point.
- Assuming safety classifiers rarely matter; Anthropic reports they trigger in under 5% of sessions on average, which is still frequent at production volume.
- Aggressive CRITICAL/MUST phrasing carried over from older prompts causes tool overtriggering on current models.

## Sources

- Claude Fable 5 and Claude Mythos 5, https://www.anthropic.com/news/claude-fable-5-mythos-5 (retrieved 2026-07-07, published 2026-06-09).
- Introducing Claude Fable 5 and Claude Mythos 5, https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07).
- Refusals and fallback, https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback (retrieved 2026-07-07).
- Prompt engineering overview, https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview (retrieved 2026-07-07).
- Best practices for Claude Code, https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07).
- Claude Code hooks explained, https://blakecrosley.com/blog/claude-code-hooks-explained (retrieved 2026-07-07, published 2026-07-01).
- Initial impressions of Claude Fable 5, https://simonwillison.net/2026/Jun/9/claude-fable-5 (retrieved 2026-07-07, published 2026-06-09).
- Claude Fable product page, https://www.anthropic.com/claude/fable (retrieved 2026-07-07).

## Related

- [[Claude Fable 5]] is the model every practice here targets.
- [[Model Selection for Agent Workloads]] expands practices 1 to 3 into a full decision guide.
- [[Prompting Fable 5 One-Pager]] expands practices 6 to 11 with mechanics.
- [[Claude Code Quickstart for Fable 5]] expands practices 12 to 15 into a setup path.
- [[Extended Thinking Budgets]] explains why budget_tokens gave way to effort.
- [[Claude Code Hooks]] covers the deterministic enforcement layer behind the hooks pitfall.
- [[Context Window Management]] deepens the context economy practices.
- [[Fable 5 Dual-Use Safety Measures]] details the classifier and refusal machinery behind practice 4.
- [[Prompt Caching Economics]] quantifies practice 5.
- [[Explore Plan Code Commit]] is the workflow behind practice 13.

## Next actions

- Re-verify all fifteen practices at the next brain refresh against their source URLs.
- Add a PRACTITIONER section if field consensus diverges from official guidance.
- Test practice 3 (effort downshift) on a real workload and record results.

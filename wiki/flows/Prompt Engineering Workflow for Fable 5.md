---
type: flow
title: "Prompt Engineering Workflow for Fable 5"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/best-practices
  - note/flow
domain: best-practices
confidence: evidence-based
approval_status: approved
risk_level: low
rollback_note: "Prompt text is versioned alongside its eval results; reverting means restoring the previous prompt file and rerunning the test set."
related:
  - "[[Prompting Fable 5 One-Pager]]"
  - "[[Claude Fable 5]]"
  - "[[Extended Thinking Budgets]]"
  - "[[Tone and Formatting Rules]]"
  - "[[Writing Effective Tools for Agents]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Claude 5 Model Family]]"
  - "[[Context Window Management]]"
  - "[[Fable 5 Best Practices Cheat Sheet]]"
  - "[[Explore Plan Code Commit]]"
source_urls:
  - "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5 (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking (retrieved 2026-07-07)"
---

# Prompt Engineering Workflow for Fable 5

Prompt work on Fable 5 is empirical: define success criteria and tests before tuning, write clear instructions with their motivation, structure with XML, control depth with the effort parameter instead of thinking budgets, and refactor rather than copy prompts written for older models.

## What it is

A stepwise workflow for Claude 5 class models built from Anthropic's consolidated Prompting best practices reference, which covers Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, Claude Sonnet 5, and Claude Haiku 4.5, with a dedicated Fable 5 page. Legacy technique URLs (use-xml-tags, chain-of-thought, claude-4-best-practices) now redirect to that living reference.

## How it works

1. **Set up the loop.** Before tuning, have "A clear definition of the success criteria for your use case" (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview), a way to test against it, and a first draft prompt.
2. **Write clear, explicit instructions.** Be specific about output and constraints, number steps when order matters, and explicitly request above-and-beyond behavior instead of hoping the model infers it.
3. **Add motivation.** Explaining why a request matters improves compliance; Fable 5 in particular performs better when told why. "Claude is smart enough to generalize from the explanation." (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5).
4. **Structure with XML.** Wrap instructions, context, examples, and inputs in consistent descriptive tags, nest for hierarchy, and include 3 to 5 relevant, diverse few-shot examples in example tags.
5. **Order long context.** For 20k+ token prompts, put longform documents at the top with XML metadata and the query at the end; ask for grounding quotes before the answer.
6. **Tune reasoning and effort.** Prefer general instructions like think thoroughly over prescriptive step plans. Adaptive thinking is always on for Fable 5 (budget_tokens returns a 400 error); the effort parameter is the primary intelligence, latency, and cost control, with high as default and xhigh for the most capability-sensitive work.
7. **Measure and iterate.** Steering phrases like "Please think hard before responding." are wording-sensitive; measure against the test set before production.

## Best practice

- Treat prompting as an empirical activity: criteria, tests, then tuning. EVIDENCE-BASED
- Be explicit; "Claude responds well to clear, explicit instructions." (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview). EVIDENCE-BASED
- Give the motivation behind instructions, especially on Fable 5. EVIDENCE-BASED
- Use XML tags for any complex prompt; they let Claude parse structure unambiguously. EVIDENCE-BASED
- Put queries after long documents; end placement improves quality "by up to 30% in tests" per the docs. EVIDENCE-BASED
- Prefer general reasoning instructions; the model's own reasoning frequently exceeds a human-prescribed plan, and manual chain-of-thought tags are only a fallback when thinking is off. EVIDENCE-BASED
- Control depth with effort, not budgets; lower effort on Fable 5 often exceeds xhigh performance of prior models. EVIDENCE-BASED
- Refactor prompts when migrating: instructions written for weaker models are "often too prescriptive for Claude Fable 5 and can degrade output quality" (https://knightli.com/en/2026/06/10/claude-fable-5-prompting-guide/). PRACTITIONER
- On long autonomous runs, instruct the model to audit every progress claim against a tool result from the session; this nearly eliminates fabricated status reports, and fresh-context verifier subagents outperform self-critique. EVIDENCE-BASED
- Ask the model to self-check its answer before finishing. EVIDENCE-BASED

## Pitfalls

- Prefilled assistant responses: unsupported from Claude 4.6 models onward, they return a 400 error; migrate to structured outputs, no-preamble instructions, user-turn continuations, or tool calling.
- Asking Fable 5 to echo or transcribe its internal reasoning in response text; that can trigger the reasoning_extraction refusal category. Read structured thinking blocks or use a send-to-user tool instead.
- Sending budget_tokens to Fable 5 or Mythos 5; adaptive thinking is always on and the request 400s.
- Aggressive CRITICAL and MUST phrasing carried over from older models causes tool overtriggering on Opus 4.5 and 4.6 class models; dial it back.
- Suggestion language when you want action; explicit action language (Change this function) makes Claude act.

## Sources

- Prompt engineering overview, Claude Platform docs: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview (retrieved 2026-07-07)
- Prompting Claude Fable 5, Claude Platform docs: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5 (retrieved 2026-07-07)
- Adaptive thinking, Claude Platform docs: https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking (retrieved 2026-07-07)
- Claude Fable 5 prompting guide, Knight Li: https://knightli.com/en/2026/06/10/claude-fable-5-prompting-guide/ (published 2026-06-10, retrieved 2026-07-07)

## Related

- [[Prompting Fable 5 One-Pager]] because it is the compressed daily-use version of this workflow.
- [[Claude Fable 5]] because model-specific behavior (effort, refusals, adaptive thinking) shapes every step.
- [[Extended Thinking Budgets]] because budgets are superseded by adaptive thinking and effort on Fable 5.
- [[Tone and Formatting Rules]] because output constraints belong in the explicit-instructions step.
- [[Writing Effective Tools for Agents]] because tool descriptions are prompts and follow the same discipline.
- [[Fable 5 Dual-Use Safety Measures]] because the reasoning_extraction category constrains what prompts may ask.
- [[Claude 5 Model Family]] because the consolidated reference spans the whole current lineup.
- [[Context Window Management]] because long-context ordering is a context-budget decision.
- [[Fable 5 Best Practices Cheat Sheet]] because the cheat sheet indexes these rules for quick recall.
- [[Explore Plan Code Commit]] because coding prompts feed that loop's explore and plan stages.

## Next actions

- Build a 20-case test set from real Fable 5 tasks before the next prompt revision.
- Audit existing skills and prompts for prefill usage, budget_tokens, and CRITICAL-heavy phrasing.
- A/B the effort parameter (high versus xhigh) on the heaviest recurring workload and record cost deltas.

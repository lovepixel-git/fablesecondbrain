---
type: deliverable
title: "Prompting Fable 5 One-Pager"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/best-practices
  - note/deliverable
domain: best-practices
confidence: evidence-based
related:
  - "[[Prompt Engineering Workflow for Fable 5]]"
  - "[[Claude Fable 5]]"
  - "[[Extended Thinking Budgets]]"
  - "[[Writing Effective Tools for Agents]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Fable 5 Best Practices Cheat Sheet]]"
  - "[[Context Window Management]]"
  - "[[Model Selection for Agent Workloads]]"
  - "[[Tone and Formatting Rules]]"
source_urls:
  - "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5 (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/writing-tools-for-agents (retrieved 2026-07-07)"
---

# Prompting Fable 5 One-Pager

Prompt Fable 5 with clear goals, stated motivation, and XML structure, let adaptive thinking manage depth through the effort parameter, and never ask it to transcribe its internal reasoning.

## What it is

- The prompting essentials for Claude 5 class models, distilled from claims verified on 2026-07-07.
- Anthropic now consolidates guidance into one living reference, Prompting best practices, covering Fable 5, Mythos 5, Opus 4.8, Sonnet 5, and Haiku 4.5, with dedicated model pages for Fable 5, Sonnet 5, and Opus 4.8; legacy technique URLs (use-xml-tags, chain-of-thought, claude-4-best-practices) redirect there (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview).
- Prompt engineering is treated as empirical: before tuning, define success criteria, build tests against them, and have a first draft prompt.

## How it works

- Clarity first: Claude responds well to clear, explicit instructions; be specific about output and constraints, use numbered steps when order matters, and request above-and-beyond behavior explicitly.
- Motivation helps: telling Fable 5 why a request matters improves compliance, because "Claude is smart enough to generalize from the explanation."
- Structure with XML: wrap instructions, context, examples, and inputs in consistent, descriptive tags; nest for hierarchy; give 3 to 5 relevant, diverse few-shot examples in example tags.
- Long context has an ordering rule: place longform documents at the top and the query at the end (up to 30% better in tests), structure documents with XML metadata, and ask for grounding quotes before the answer.
- Thinking is adaptive and always on for Fable 5 and Mythos 5: budget_tokens returns a 400 error, depth is controlled with the effort parameter (high default, xhigh for capability-sensitive work), interleaved thinking between tool calls enables automatically, and raw chain of thought is never returned.
- Thinking is promptable: system-prompt guidance can suppress or encourage thinking, and per-message phrases such as "Please think hard before responding." steer single turns, but steering is wording-sensitive and should be measured before production.
- Tools follow their own rules: detailed tool descriptions of at least 3 to 4 sentences are the biggest lever on tool-use performance, current models parallelize independent tool calls by default, and a use_parallel_tool_calls block can push parallel usage to roughly 100 percent.

## Best practice

- Prefer general reasoning instructions like think thoroughly over prescriptive step-by-step plans; "Claude's reasoning frequently exceeds what a human would prescribe." (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview). EVIDENCE-BASED
- Never ask Fable 5 to reproduce its internal reasoning in response text; it can trigger the reasoning_extraction refusal category, so read structured thinking blocks instead (https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking). EVIDENCE-BASED
- Refactor prompts written for earlier models instead of copying them; legacy scaffolding is "often too prescriptive for Claude Fable 5 and can degrade output quality" (https://knightli.com/en/2026/06/10/claude-fable-5-prompting-guide/). PRACTITIONER
- Use action language for tool work; explicit phrasing like "Change this function" makes Claude act, while suggestion language yields only suggestions (https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview). EVIDENCE-BASED
- Dial back aggressive CRITICAL/MUST phrasing written for older models; it causes overtriggering on current models. EVIDENCE-BASED
- For long autonomous runs, instruct the model to audit every progress claim against a tool result from the session; this nearly eliminates fabricated status reports, and fresh-context verifier subagents outperform self-critique (https://knightli.com/en/2026/06/10/claude-fable-5-prompting-guide/). PRACTITIONER
- Replace prefill patterns before migrating: prefilled assistant responses return a 400 error from Claude 4.6 models onward; use structured outputs, direct no-preamble instructions, user-turn continuations, or tool calling (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview). EVIDENCE-BASED
- Show reasoning patterns via thinking tags inside few-shot examples, and reserve manual chain-of-thought tags as a fallback for when thinking is off. EVIDENCE-BASED
- Ask Claude to self-check its answer before finishing when correctness matters. EVIDENCE-BASED

## Pitfalls

- Sending budget_tokens to Fable 5; adaptive thinking is the only mode and the parameter 400s.
- Relying on prefilled assistant messages; unsupported from 4.6 onward.
- Copying old prompt libraries verbatim into Fable 5 systems; over-prescription degrades quality.
- Shipping thinking-steering phrases without measurement; steering is sensitive to exact wording.
- Writing one-line tool descriptions; description quality is "by far the most important factor in tool performance." (https://www.anthropic.com/engineering/writing-tools-for-agents).
- Requesting reasoning transcripts for UX transparency; use a send-to-user tool or thinking summaries instead.
- Prompting for parallelism you already have; independent tool calls parallelize by default, and the use_parallel_tool_calls block is a tuning knob, not an enabler.

## Sources

- Prompt engineering overview, https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview (retrieved 2026-07-07).
- Prompting Claude Fable 5, https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5 (retrieved 2026-07-07).
- Adaptive thinking, https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking (retrieved 2026-07-07).
- Writing effective tools for agents, with agents, https://www.anthropic.com/engineering/writing-tools-for-agents (retrieved 2026-07-07, published 2025-09-11).
- Claude Fable 5 prompting guide, https://knightli.com/en/2026/06/10/claude-fable-5-prompting-guide/ (retrieved 2026-07-07, published 2026-06-10).

## Related

- [[Prompt Engineering Workflow for Fable 5]] turns these essentials into a repeatable workflow.
- [[Claude Fable 5]] is the model whose behavior these rules target.
- [[Extended Thinking Budgets]] documents the budget-to-effort transition behind the 400 error.
- [[Writing Effective Tools for Agents]] deepens the tool-description lever.
- [[Fable 5 Dual-Use Safety Measures]] explains the reasoning_extraction refusal category.
- [[Fable 5 Best Practices Cheat Sheet]] places prompting inside the full operating picture.
- [[Context Window Management]] extends the long-context ordering rule.
- [[Model Selection for Agent Workloads]] pairs effort tuning with model choice.
- [[Tone and Formatting Rules]] covers the output-side conventions prompts interact with.

## Next actions

- Benchmark two effort levels on a recurring workload and record deltas.
- Convert one legacy prescriptive prompt to Fable 5 style and A/B the outputs.
- Re-verify the consolidated guidance page at the next brain refresh.

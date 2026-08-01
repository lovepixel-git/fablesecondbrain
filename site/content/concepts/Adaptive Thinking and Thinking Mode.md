---
type: concept
title: "Adaptive Thinking and Thinking Mode"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/memory
  - note/concept
domain: memory-and-context
confidence: evidence-based
related:
  - "[[Claude Fable 5]]"
  - "[[Claude Mythos 5]]"
  - "[[Claude 5 Model Family]]"
  - "[[Claude Code]]"
  - "[[Extended Thinking Budgets]]"
  - "[[Context Window Management]]"
  - "[[Prompt Caching Economics]]"
  - "[[System Prompt Export 2026-07]]"
  - "[[claude.ai Platform]]"
  - "[[Claude Code Platform]]"
  - "[[Claude Console and API Platform]]"
  - "[[Knowledge Cutoff and Search Triggers]]"
source_urls:
  - "https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/build-with-claude/effort (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/model-config (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Adaptive Thinking and Thinking Mode

Adaptive thinking is the always-on reasoning system of Fable 5, tuned only through the effort parameter, and the phrase "thinking mode" names two additional, unrelated harness controls; this note is the vault's single source of truth for all three layers, and other notes defer to it.

## What it is

- Anthropic's docs call adaptive thinking "the only thinking mode on Claude Fable 5 and Claude Mythos 5" (https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking, retrieved 2026-07-07). It is always on: the model decides per request whether and how much to think.
- Three distinct layers share the "thinking mode" vocabulary and must never be conflated:
  1. API layer: adaptive thinking plus the `effort` parameter in `output_config`. This is the only layer that actually controls reasoning depth on Fable 5.
  2. claude.ai harness layer: the system prompt scaffold carries a literal `<thinking_mode>auto</thinking_mode>` tag, System Prompt Export 2026-07, L3818. That tag is the harness's own directive to the model, not an API parameter.
  3. Claude Code harness layer: `/config` exposes a "thinking mode" toggle saved as `alwaysThinkingEnabled` in settings. On Fable 5 this toggle is inert because thinking cannot be turned off (https://code.claude.com/docs/en/model-config, retrieved 2026-07-07).

> [!key-insight] "thinking_mode" is NOT an API parameter. The corpus tag at L3818 is a claude.ai prompt-scaffold directive, and Claude Code's "thinking mode" is a client-side toggle. Only `effort` inside `output_config` changes Fable 5 reasoning behavior at the API.

- The former `> [!gap]` callouts in [[Extended Thinking Budgets]] on adaptive thinking, effort, and thinking display are closed as of 2026-07-07; that note keeps the context-editing and caching mechanics and defers thinking-mode semantics here.

## How it works

- Always on: adaptive thinking applies whenever the `thinking` parameter is unset; `thinking: {type: disabled}` is not supported on Fable 5 or Mythos 5 (adaptive-thinking doc, retrieved 2026-07-07).
- Effort controls depth: values are `low`, `medium`, `high`, `xhigh`, and `max`, default `high`, set inside `output_config`. `xhigh` is available on Fable 5, Mythos 5, Opus 4.8, Opus 4.7, and Sonnet 5 (https://platform.claude.com/docs/en/build-with-claude/effort, retrieved 2026-07-07).
- Manual budgets are gone: passing a manual `budget_tokens` value is rejected with a 400 error on Fable 5. Sampling knobs are locked too: non-default `temperature`, `top_p`, or `top_k` are rejected with a 400 error (adaptive-thinking doc, retrieved 2026-07-07).
- Visibility: raw chain of thought is never returned. `thinking.display: "summarized"` returns a readable summary; `"omitted"`, the default on these models, returns an empty thinking field (adaptive-thinking doc, retrieved 2026-07-07).
- Interleaving: adaptive thinking automatically enables interleaved thinking, so the model can think between tool calls without a beta header (adaptive-thinking doc, retrieved 2026-07-07).
- Extraction refusals: attempts to extract raw reasoning can be refused with `stop_details.category` set to `"reasoning_extraction"` (adaptive-thinking doc, retrieved 2026-07-07).
- claude.ai harness: the export's scaffold ends with the `<thinking_mode>auto</thinking_mode>` tag immediately before the Human turn, System Prompt Export 2026-07, L3818, showing the consumer harness delegates thinking depth to the model rather than pinning a budget.
- Claude Code: the model-config doc states "Thinking cannot be turned off on Fable 5." and notes that `MAX_THINKING_TOKENS=0` turns thinking off on the API for other models but not for Fable 5 (retrieved 2026-07-07).

## Best practice

- Treat this note as the single source of truth for thinking behavior; when another vault note discusses thinking modes, it should link here instead of restating parameters. PRACTITIONER
- Control reasoning depth on Fable 5 only through `effort` in `output_config`; leave the `thinking` parameter unset. EVIDENCE-BASED
- Remove `budget_tokens`, custom `temperature`, `top_p`, and `top_k` from request templates before migrating to Fable 5; each triggers a 400 error. EVIDENCE-BASED
- Set `thinking.display: "summarized"` when an application needs to show users a reasoning trace; expect an empty thinking field under the default `"omitted"`. EVIDENCE-BASED
- Use `xhigh` or `max` effort for deep agentic work and `low` for latency-sensitive routing, keeping the default `high` otherwise. PRACTITIONER
- In Claude Code on Fable 5, ignore the `alwaysThinkingEnabled` toggle when debugging behavior differences; it cannot disable thinking on this model. EVIDENCE-BASED
- Do not design prompts that ask Fable 5 to reveal raw chain of thought; the API refuses with a `reasoning_extraction` stop category. EVIDENCE-BASED

## Pitfalls

- Conflating the three layers: sending `thinking_mode` as an API parameter because the corpus scaffold contains that tag; the API does not accept it.
- Expecting `MAX_THINKING_TOKENS=0` or the Claude Code toggle to silence thinking on Fable 5; both are inert on this model.
- Carrying `budget_tokens` forward from Sonnet-era extended thinking code and misreading the resulting 400 error as an outage.
- Tuning `temperature` for creativity on Fable 5; any non-default sampling value is rejected, so variation must come from prompting.
- Logging the empty thinking field under `"omitted"` display and concluding the model did not think; adaptive thinking still ran.
- Assuming the summarized display is the raw reasoning; it is a readable summary, and the raw chain of thought is never returned.
- Citing the L3818 tag as evidence about the API; it is evidence about the claude.ai harness capture only.

## Sources

- Adaptive thinking, Claude Docs. https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking (retrieved 2026-07-07)
- Effort, Claude Docs. https://platform.claude.com/docs/en/build-with-claude/effort (retrieved 2026-07-07)
- Model configuration, Claude Code Docs. https://code.claude.com/docs/en/model-config (retrieved 2026-07-07)
- System Prompt Export 2026-07, L3818 (claude.ai harness capture, `thinking_mode` tag).

## Related

- [[Claude Fable 5]] is the model whose thinking cannot be turned off at any layer.
- [[Claude Mythos 5]] shares adaptive thinking as its only thinking mode.
- [[Claude 5 Model Family]] frames which models accept `xhigh` effort.
- [[Claude Code]] hosts the inert `alwaysThinkingEnabled` toggle described here.
- [[Extended Thinking Budgets]] keeps the context-editing and caching mechanics and defers thinking semantics to this note.
- [[Context Window Management]] owns the window that thinking tokens still spend from.
- [[Prompt Caching Economics]] explains why preserved thinking blocks preserve cache hits.
- [[System Prompt Export 2026-07]] is the primary capture containing the L3818 harness tag.
- [[claude.ai Platform]] is the harness whose scaffold sets thinking_mode to auto.
- [[Claude Code Platform]] is the harness whose /config toggle is inert on Fable 5.
- [[Claude Console and API Platform]] is where effort and display are actually configured.
- [[Knowledge Cutoff and Search Triggers]] covers the other model-behavior anchor of this wave.

## Next actions

- Re-verify effort defaults and display semantics against the live docs at the next research-pack refresh.
- Add a comparison note on effort versus legacy budget_tokens cost behavior if Anthropic publishes pricing guidance.

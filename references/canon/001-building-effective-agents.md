# 001. Building Effective Agents

Anthropic Engineering, published 2024-12-19. EVIDENCE-BASED.
URL: https://www.anthropic.com/engineering/building-effective-agents (retrieved 2026-07-07)

## What it says

- Distinguishes workflows (predefined code paths orchestrating LLM calls) from agents (the model dynamically directs its own process and tool usage). Paraphrase.
- Advocates starting with the simplest composable patterns before reaching for autonomy: prompt chaining, routing, parallelization (sectioning and voting), orchestrator-workers, evaluator-optimizer.
- Frames agent design around three principles, paraphrased: keep designs simple, make the agent's planning transparent, and craft the agent-computer interface (tools) as carefully as any human interface.
- Warns that added complexity must buy real outcome improvements; many production wins come from workflows, not full agents.

## Why it is canon here

It is the root document of Anthropic's agent-building doctrine; the Fable 5 Brain's orchestration notes ([[Multi-Agent Fan-Out Research Flow]], [[Model Selection for Agent Workloads]]) inherit its vocabulary and its simplicity-first stance.

## How this brain applies it

- Workflow-versus-agent framing anchors wiki/concepts and wiki/flows guidance.
- The orchestrator-workers pattern is exactly how this brain was built: a main session orchestrating verified parallel workers.
- Tool-interface care maps to [[Writing Effective Tools for Agents]].

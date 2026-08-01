# 003. How We Built Our Multi-Agent Research System

Anthropic Engineering, published 2025-06-13. EVIDENCE-BASED.
URL: https://www.anthropic.com/engineering/multi-agent-research-system (retrieved 2026-07-07)

## What it says

- Documents an orchestrator-worker research architecture: a lead agent decomposes a question, spawns parallel searchers, and synthesizes.
- Reports that multi-agent fan-out buys breadth and wall-clock speed at a real token premium; parallelism pays when the task genuinely decomposes. Paraphrase.
- Stresses prompt engineering of the workers (explicit effort scaling, clear boundaries) and evaluation of end-to-end outcomes rather than per-step correctness.

## Why it is canon here

It is the official precedent for the fan-out research pattern this brain uses for its own source pack, and the reference point for [[Multi-Agent Fan-Out Research Flow]].

## How this brain applies it

- The P2 research phase of this brain (7 parallel researchers, adversarial verifiers, one synthesizing orchestrator) is a direct application.
- Worker prompts in this vault's flows carry explicit boundaries and manifests, per its worker-prompting lessons.

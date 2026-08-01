# 002. Best Practices for Claude Code

Anthropic, official docs (formerly the anthropic.com/engineering/claude-code-best-practices post). Living page. EVIDENCE-BASED.
URL: https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)

## What it says

- Establishes the canonical agentic coding loop, paraphrased: explore first, plan explicitly, implement, then commit; plan mode exists to separate thinking from mutation.
- CLAUDE.md is the durable project memory: keep it curated, scoped, and short enough to always load.
- Permissions are a safety surface: allowlist deliberately, use hooks for guardrails, prefer narrow tool grants.
- Recommends subagents for parallelizable or context-heavy work and headless mode for CI.

## Why it is canon here

It is the primary official operating manual for the harness half of this brain's domain; the entire claude-code-harness domain traces to it.

## How this brain applies it

- [[Explore Plan Code Commit]] is its loop, recorded as a flow with rollback discipline.
- [[CLAUDE.md Project Memory]], [[Claude Code Hooks]], [[Claude Code Subagents]], [[Plan Mode and Permission Modes]], [[Headless Claude Code and CI]] each expand one of its chapters with dated citations.

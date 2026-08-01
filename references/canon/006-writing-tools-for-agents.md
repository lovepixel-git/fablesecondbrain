# 006. Writing Effective Tools for Agents, With Agents

Anthropic Engineering, published 2025-09-11. EVIDENCE-BASED.
URL: https://www.anthropic.com/engineering/writing-tools-for-agents (retrieved 2026-07-07)

## What it says

- Tools are contracts for non-deterministic callers: names, descriptions, and response shapes must be unambiguous to a model, not just a human. Paraphrase.
- Recommends consolidating overlapping tools, returning token-efficient high-signal responses, and namespacing related tools.
- Advocates evaluating tools with realistic agent tasks and letting Claude itself propose tool improvements.

## Why it is canon here

The tools-and-skills domain ([[Writing Effective Tools for Agents]], [[Tool Search and Deferred Tools]], [[Model Context Protocol]]) applies its contract framing.

## How this brain applies it

- The brain's own adapter scripts follow it: single-purpose commands, deterministic output, loud failures.
- MCP server guidance in this vault inherits its response-shaping and namespacing rules.

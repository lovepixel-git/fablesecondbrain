---
type: meta
title: "overview"
status: evergreen
created: 2026-07-07
updated: 2026-07-09
tags:
  - fable5/best-practices
  - note/meta
domain: best-practices
confidence: evidence-based
related:
  - "[[index]]"
  - "[[hot]]"
  - "[[log]]"
  - "[[Start Here]]"
  - "[[CONVENTIONS]]"
  - "[[Claude Fable 5]]"
  - "[[Claude Code]]"
source_urls:
  - "https://www.anthropic.com/news/claude-fable-5-mythos-5 (retrieved 2026-07-07)"
---

# Overview

The Fable 5 Brain is a source-cited Obsidian knowledge brain about [[Claude Fable 5]], Anthropic's Mythos-class model announced 2026-06-09, the harnesses it runs in, and current operating best practices. Every claim carries a dated citation or a line reference into the immutable system prompt export, and a confidence tag per [[Confidence Tag Policy]].

## What the brain knows

- **The model and family**: [[Claude Fable 5]] and [[Claude Mythos 5]] share one underlying model; Fable ships safety classifiers ([[Fable 5 Dual-Use Safety Measures]]), Mythos is invitation-only. Specs: 1M context, 128k output, $10/$50 per MTok, adaptive thinking always on ([[Extended Thinking Budgets]]). The wider [[Claude 5 Model Family]] covers Opus 4.8, Sonnet 5, and Haiku 4.5.
- **Mythos and Glasswing doctrine**: [[Project Glasswing]], [[Fable Mythos 5 System Card]], and [[Fable Mythos Operating Doctrine]] now anchor the trusted-access side: public system-card evaluations, Glasswing vulnerability-disclosure outcomes, access limits, and the practical Fable-versus-Mythos operating posture.
- **The claude.ai harness**: fixture-grounded notes from [[System Prompt Export 2026-07]], chaptered in wiki/sources: artifacts criteria, storage API, memory system, search and copyright rules, 24 tool schemas.
- **The Claude Code harness**: research-grounded notes on CLAUDE.md, hooks, subagents, plan mode, permissions, headless CI, per official docs ([[Claude Code]]).
- **Best practices**: the flows and deliverables distill Anthropic's agent-building canon (references/canon) into runnable playbooks like [[Explore Plan Code Commit]] and [[Multi-Agent Fan-Out Research Flow]].
- **Behavior and values**: dedicated notes on the harness's emotional-intelligence and conduct layer, grounded in the export and the Fable 5 system card: [[User Wellbeing Rules]], [[Evenhandedness Rules]], [[Responding to Mistakes and Criticism]], [[Harness Refusal Handling]], [[Child Safety Rules]], [[Anthropic Runtime Reminders]], plus the thinking-patterns anchor [[Adaptive Thinking and Thinking Mode]].

## How it stays honest

96 verified sources in references/source-ledger.json with refresh_due dates; 187 claim rows (references/claim-ledger.md); contradictions carry callouts; gaps are registered in wiki/gaps, not papered over. The former "no public Fable 5 benchmark data" gap is now resolved by the public Fable/Mythos 5 system card, and the GitHub sweep now separates Fable prompt mirrors from unverified Mythos leak claims. The corpus is immutable in .raw/ with sha256 provenance.

## Where to start

[[Start Here]] for the read order, [[index]] for the full catalog, [[hot]] for what changed last.

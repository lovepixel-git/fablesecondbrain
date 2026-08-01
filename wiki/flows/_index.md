---
type: meta
title: "Flows Hub"
status: evergreen
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/best-practices
  - note/meta
domain: best-practices
confidence: evidence-based
related:
  - "[[index]]"
  - "[[overview]]"
  - "[[hot]]"
  - "[[log]]"
  - "[[Start Here]]"
  - "[[CONVENTIONS]]"
---

# Flows

Operating playbooks: when to run them and what they produce.

- [[Brain Refresh Flow]] (best-practices, developing): When a source's refresh_due date in (path) passes, this brain stops trusting it: scan the ledger, re-fetch every stale URL, re-verify the claims each one supports, then bump dates, and demote anyth...
- [[Claim Verification Flow]] (best-practices, developing): Every claim in this brain survives an adversarial check before it is asserted: an independent second source confirms it or the claim is downgraded to CONTESTED with a caveat, and verification runs ...
- [[Context Compaction Routine]] (memory-and-context, developing): Treat the context window as a finite attention budget: compact deliberately at task boundaries with notes, persistent artifacts, and subagent isolation, and prefer a clean restart over grinding thr...
- [[Corpus Ingestion Flow]] (best-practices, developing): A new system prompt export enters this vault only through .raw: save it under a dated name, record its sha256 in (path) parse and diff it with (path) then file findings as wiki notes with line-refe...
- [[Explore Plan Code Commit]] (best-practices, developing): Explore Plan Code Commit is the officially recommended Claude Code loop: research in read-only plan mode, approve a written plan, implement against a runnable check, then commit, and skip the plan ...
- [[Multi-Agent Fan-Out Research Flow]] (best-practices, developing): Fan out parallel worker agents from a lead orchestrator only for breadth-first research worth roughly 15x chat token spend; Anthropic's own orchestrator-worker Research system "outperformed single-...
- [[Prompt Engineering Workflow for Fable 5]] (best-practices, developing): Prompt work on Fable 5 is empirical: define success criteria and tests before tuning, write clear instructions with their motivation, structure with XML, control depth with the effort parameter ins...

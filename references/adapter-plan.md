# Fable 5 Brain Adapter Plan

Status: required before domain-adapted maturity.

## Raw Input Types

- System prompt export metadata captured from a live claude.ai Fable 5 session, with raw capture omitted from this public release
- Claude Code changelog and release notes snapshots
- Anthropic model documentation snapshots for Fable 5

## Required Implementation

- Define one schema per raw input type.
- Build at least one real domain importer or ingestion path.
- Build one domain-specific synthesis module.
- Build one report renderer with source citations.
- Add sanitized fixtures and tests for every supported input type.

## Safety Refusals

- No claim about Fable 5 behavior without a dated source or a verbatim quote from the export
- Never present folklore or contested guidance as evidence-based
- No irreversible recommendation without owner, confidence, source, and rollback note
- Do not call this brain market-ready unless the audit gate passes

## Completion Gate

This plan is complete only when domain-specific importer, synthesis, report,
fixtures, and tests replace the generic scaffold.

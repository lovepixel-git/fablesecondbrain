---
type: decision
title: "Frontmatter Dialect Decision"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/best-practices
  - note/decision
domain: best-practices
confidence: practitioner
approval_status: approved
risk_level: low
rollback_note: "Restore the frontmatter contract block in wiki/meta/CONVENTIONS.md from git history; the dialect is additive, so existing notes stay valid."
related:
  - "[[CONVENTIONS]]"
  - "[[Tag Taxonomy]]"
  - "[[Confidence Tag Policy]]"
  - "[[Corpus Scope Decision]]"
  - "[[System Prompt Export 2026-07]]"
  - "[[Claude Code Project Memory]]"
  - "[[Claude Fable 5]]"
  - "[[Start Here]]"
  - "[[index]]"
source_urls:
  - "https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/memory (retrieved 2026-07-07)"
---

# Frontmatter Dialect Decision

Every note in this vault uses one merged frontmatter dialect, the claude-obsidian status vocabulary plus house enrichment fields for provenance and confidence, exactly as codified in [[CONVENTIONS]].

## What it is

- A decision record ratifying the YAML frontmatter contract for every wiki page in the Fable 5 Brain.
- The dialect merges two ingredient sets instead of inventing a third:
  - Base keys from the claude-obsidian wiki skill: `type`, `title`, `status`, `created`, `updated`, and `tags` with a `note/<type>` mirror tag.
  - House enrichment keys for this research vault: `domain`, `confidence`, `related`, `source_urls`, `sources`, and the mutation trio `approval_status`, `risk_level`, `rollback_note`.
- The status vocabulary stays `seed`, `developing`, `mature`, `evergreen`, unchanged from the claude-obsidian dialect, so existing plugin tooling keeps working.
- The master copy of the contract lives in wiki/meta/CONVENTIONS.md; CLAUDE.md carries only a summary and is restored from the master if an upgrade clobbers it.

## How it works

- `type` is one of: source, entity, concept, flow, platform, account, decision, deliverable, question, gap, experiment, comparison, meta.
- `domain` is one of eight fixed values: model-and-family, claude-ai-harness, claude-code-harness, tools-and-skills, memory-and-context, communication-rules, safety-and-permissions, best-practices.
- `confidence` follows [[Confidence Tag Policy]]: evidence-based, practitioner, or contested at note level, with per-claim tags in the body.
- YAML stays flat: ISO dates, lists as `- item`, wikilinks quoted, no nested maps.
- `related` carries at least 6 quoted wikilinks; this brain's authoring runs target 8 or more.
- `source_urls` entries carry a retrieval date suffix so staleness checks have something to bite on.
- `sources` lists `[[System Prompt Export 2026-07]]` only when a note uses corpus claims, which keeps corpus provenance queryable.
- `approval_status`, `risk_level`, and `rollback_note` appear only on decision and flow notes that recommend mutations, like this one.
- `updated` is bumped on every edit; the lint and audit gates read all of these fields mechanically.

## Best practice

- Keep the master contract in [[CONVENTIONS]] and treat CLAUDE.md as a replaceable summary layer; restore from the master after any generator upgrade. PRACTITIONER
- Keep the agent-facing summary short; official Claude Code guidance warns "Bloated CLAUDE.md files cause Claude to ignore your actual instructions!" (https://code.claude.com/docs/en/best-practices). EVIDENCE-BASED
- Mirror the official sizing guidance, "target under 200 lines per CLAUDE.md file", when projecting this contract into the agent layer (https://code.claude.com/docs/en/memory). EVIDENCE-BASED
- Quote every wikilink inside YAML lists so Obsidian and strict YAML parsers agree on the value. PRACTITIONER
- Keep `related` at or above the floor so graph traversal never dead-ends on a leaf note. PRACTITIONER
- Add the mutation trio only where a note recommends changing live state; inert notes stay lean. PRACTITIONER
- Date every `source_urls` entry so rule 5 of [[Confidence Tag Policy]], the staleness rule, stays checkable. PRACTITIONER

## Pitfalls

- Nested YAML maps break the flat-YAML rule and the vault linter.
- Unquoted wikilinks in YAML lists parse as nested sequences and corrupt the field.
- Importing a draft/final status vocabulary from other vaults; only seed, developing, mature, and evergreen are valid here.
- Forgetting the `note/<type>` mirror tag, which desynchronizes tag queries from `type` queries.
- Adding `approval_status` to concept or entity notes; the contract scopes it to mutation-recommending decisions and flows.
- Em dashes anywhere in a note, including YAML strings; the style rule bans them vault-wide.

## Sources

- Best practices for Claude Code, https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07); brevity rationale for the contract summary layer.
- How Claude remembers your project: CLAUDE.md and auto memory, https://code.claude.com/docs/en/memory (retrieved 2026-07-07); the under-200-line sizing guidance.

## Related

- [[CONVENTIONS]] holds the master copy of the contract this decision ratifies.
- [[Tag Taxonomy]] defines the lowercase hierarchical tags the dialect requires.
- [[Confidence Tag Policy]] governs the `confidence` key this dialect carries.
- [[Corpus Scope Decision]] is the sibling decision that governs the `sources` key.
- [[System Prompt Export 2026-07]] is the corpus that `sources` entries point to.
- [[Claude Code Project Memory]] documents the agent memory layer the contract summary lives in.
- [[Claude Fable 5]] is the subject this dialect exists to describe accurately.
- [[Start Here]] onboards new readers into the dialect.
- [[index]] is the master catalog that lists every note written in this dialect.

## Next actions

- Add a lint rule that rejects notes missing the `note/<type>` mirror tag.
- Spot-check five existing notes for unquoted YAML wikilinks.
- Revisit the `related` floor once the vault passes 100 notes.

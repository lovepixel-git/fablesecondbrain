---
type: concept
title: "Claude Code Project Memory"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/harness/claude-code
  - note/concept
domain: claude-code-harness
confidence: evidence-based
related:
  - "[[Claude Code]]"
  - "[[Claude Code Hooks]]"
  - "[[Claude Code Settings and Permissions]]"
  - "[[Agent Skills System]]"
  - "[[Claude Code Subagents]]"
  - "[[Claude Memory System]]"
  - "[[Context Window Management]]"
  - "[[Explore Plan Code Commit]]"
  - "[[Claude Code Quickstart for Fable 5]]"
source_urls:
  - "https://code.claude.com/docs/en/memory (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/overview (retrieved 2026-07-07)"
---

# CLAUDE.md Project Memory

CLAUDE.md is Claude Code's always-loaded instruction file, and it earns its context cost only when kept under 200 lines of facts Claude cannot infer from the code itself.

## What it is

CLAUDE.md is the persistent memory contract between a repository and [[Claude Code]]. It carries build commands, style rules that differ from defaults, repo etiquette, and gotchas. The official docs at code.claude.com (the canonical home; the old anthropic.com engineering post 308-redirects there) describe a defined scope order:

- Managed policy, for example /etc/claude-code/CLAUDE.md on Linux.
- User scope at ~/.claude/CLAUDE.md, applied to every project.
- Project scope at ./CLAUDE.md or ./.claude/CLAUDE.md, shared with the team.
- ./CLAUDE.local.md, gitignored personal overrides for one machine.

Two companions extend it. `.claude/rules/` holds path-scoped rules activated via `paths` frontmatter. Auto memory, on by default since v2.1.59, is a second system: "notes Claude writes itself based on your corrections and preferences" stored under ~/.claude/projects/<project>/memory/ (https://code.claude.com/docs/en/memory).

## How it works

- Parent-directory CLAUDE.md files load in full at session launch; subdirectory files load on demand when Claude works in those paths.
- `@path/to/import` syntax pulls other files in, recursively up to four hops.
- Claude Code does not read AGENTS.md natively. The docs are blunt: "Claude Code reads CLAUDE.md, not AGENTS.md." The official pattern for AGENTS.md repos is a CLAUDE.md that imports it, or a symlink (https://code.claude.com/docs/en/memory).
- From auto memory, the first 200 lines or 25KB of MEMORY.md load into every session; /memory inspects and edits it, and `autoMemoryEnabled: false` disables it.
- Content divides by load pattern: every-session facts belong in CLAUDE.md, while multi-step procedures move into skills because "a skill's body loads only when it's used" (https://code.claude.com/docs/en/best-practices).
- The VS Code extension shares CLAUDE.md, conversation history, settings, and MCP config with the terminal CLI, so one memory file governs both surfaces (https://code.claude.com/docs/en/vs-code).

> [!key-insight] CLAUDE.md is advisory prose with an always-loaded cost. Every line must either change behavior or be deleted; enforcement belongs in hooks and permissions, procedures in skills.

## Best practice

- Target under 200 lines per CLAUDE.md file; official sizing guidance is explicit on this number. EVIDENCE-BASED
- Include only what Claude cannot infer from code: build commands, non-default style rules, repo etiquette, gotchas. EVIDENCE-BASED
- Run /init to generate a starter file, then prune it ruthlessly rather than letting it grow. EVIDENCE-BASED
- Mark critical rules with emphasis like IMPORTANT or YOU MUST so they survive attention dilution. EVIDENCE-BASED
- Move occasionally relevant domain knowledge and multi-step procedures into skills, keeping CLAUDE.md for broadly applicable facts. EVIDENCE-BASED
- Enforce mandatory rules with hooks and permission rules, not CLAUDE.md prose, because CLAUDE.md instructions are advisory while hooks are deterministic. EVIDENCE-BASED
- Review auto memory with /memory every few weeks so self-written notes stay accurate. PRACTITIONER
- Reserve managed policy files like /etc/claude-code/CLAUDE.md for organization-wide rules only, since they load for every user on the machine. PRACTITIONER

## Pitfalls

- Bloat destroys adherence. The docs warn: "Bloated CLAUDE.md files cause Claude to ignore your actual instructions!" (https://code.claude.com/docs/en/best-practices).
- Assuming AGENTS.md is read. It is not; without an import or symlink those instructions are invisible.
- Treating CLAUDE.md as an enforcement layer. It cannot guarantee behavior; that is what [[Claude Code Hooks]] are for.
- Forgetting CLAUDE.local.md is gitignored, so teammates never see rules placed there.
- Not knowing auto memory exists. Claude writes its own per-repo notes, and only the first 200 lines or 25KB of MEMORY.md load, so unreviewed or overlong memory silently drifts.
- Duplicating machine-readable configuration in prose; permission rules and hooks belong in settings files, where the harness executes them.

## Sources

- How Claude remembers your project: CLAUDE.md and auto memory, official docs, https://code.claude.com/docs/en/memory (retrieved 2026-07-07).
- Best practices for Claude Code, official docs, formerly the anthropic.com engineering post, https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07).
- Claude Code Overview, official docs, https://code.claude.com/docs/en/overview (retrieved 2026-07-07).
- Use Claude Code in VS Code, official docs, https://code.claude.com/docs/en/vs-code (retrieved 2026-07-07).

## Related

- [[Claude Code]] is the harness that loads and obeys these memory files.
- [[Claude Code Hooks]] provide the deterministic enforcement that advisory CLAUDE.md text cannot.
- [[Claude Code Settings and Permissions]] follow a parallel scope hierarchy for machine-readable config.
- [[Agent Skills System]] is where procedures go when CLAUDE.md grows past its budget.
- [[Claude Code Subagents]] run in separate contexts and rely on lean shared memory.
- [[Claude Memory System]] is the claude.ai counterpart; keep the two systems distinct.
- [[Context Window Management]] explains why every-session token cost matters.
- [[Explore Plan Code Commit]] is the workflow a good CLAUDE.md accelerates.
- [[Claude Code Quickstart for Fable 5]] covers /init during first-run setup.
- [[Which Export Rules Bind Claude Code]] clarifies that claude.ai export rules do not flow through CLAUDE.md.
- [[docs.claude.com]] hosts the broader Claude docs; its Claude Code pages 301-redirect to code.claude.com.

## Next actions

- Run /init in the most-used repos and prune each result under 200 lines.
- Inspect auto memory with /memory in one active repo and correct stale notes.
- Move any multi-step procedure text out of user-level CLAUDE.md into skills.
- Add a CLAUDE.md import line or symlink in any repo that maintains an AGENTS.md.

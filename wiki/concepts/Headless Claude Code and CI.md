---
type: concept
title: "Headless Claude Code and CI"
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
  - "[[Claude Agent SDK]]"
  - "[[Plan Mode and Permission Modes]]"
  - "[[Claude Code Settings and Permissions]]"
  - "[[Claude Code Hooks]]"
  - "[[Claude Code Platform]]"
  - "[[Multi-Agent Fan-Out Research Flow]]"
  - "[[Sandbox Network and Filesystem Model]]"
source_urls:
  - "https://code.claude.com/docs/en/headless (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/permission-modes (retrieved 2026-07-07)"
---

# Headless Claude Code and CI

Non-interactive mode, `claude -p`, is the official path for CI, scripts, and pipelines, and `--bare` is the recommended flag for reproducible scripted runs.

## What it is

Headless mode runs Claude Code without an interactive terminal session: one prompt in, structured output out. The docs position it as the automation surface for CI, scripts, and pipelines (https://code.claude.com/docs/en/headless). Key machinery:

- Output formats: text, json, and stream-json.
- `--json-schema` for structured output that downstream tooling can parse safely.
- `--allowedTools` for pre-approving actions with the same permission-rule syntax settings files use.
- `--continue` and `--resume` for multi-step automation across invocations.
- `--bare`, which skips auto-discovery of hooks, skills, plugins, MCP servers, and CLAUDE.md.

## How it works

- A pipeline invokes `claude -p "<task>"` with flags fixing permissions, output format, and context; the process exits when the task completes, emitting the chosen format.
- The docs recommend the stripped-down profile for automation: "--bare is the recommended mode for scripted and SDK calls" (https://code.claude.com/docs/en/headless), because ambient config makes runs machine-dependent.
- Auto mode interacts specially with -p: its classifier still reviews actions, and repeated blocks abort the session instead of pausing for a prompt (https://code.claude.com/docs/en/permission-modes).
- bypassPermissions is officially restricted to isolated environments such as containers and VMs, and refuses to start as root, which shapes how CI runners must be provisioned.
- The headless guide is part of the canonical code.claude.com docs set; former docs.claude.com Claude Code pages 301-redirect there (https://code.claude.com/docs/en/overview).

> [!key-insight] Headless success is a provisioning problem: fix the config with --bare, fix the permissions with --allowedTools, fix the output with --json-schema, and give the run a check it can iterate against.

## Best practice

- Use `--bare` for scripted and SDK calls so runs are reproducible across machines. EVIDENCE-BASED
- Pre-approve exactly the needed tools with `--allowedTools` permission-rule syntax instead of loosening the whole mode. EVIDENCE-BASED
- Emit json or stream-json with `--json-schema` when another program consumes the result. EVIDENCE-BASED
- Give the run a verifiable check (tests, build exit code, linter) so it can iterate until the check passes without a human in the loop. EVIDENCE-BASED
- Run permissive modes only inside disposable, isolated runners, per the containers-and-VMs restriction. EVIDENCE-BASED
- Chain multi-step jobs with `--continue` and `--resume` rather than cramming one giant prompt. EVIDENCE-BASED
- Prototype a batch job on 2 or 3 files before scaling a fan-out across the tree. PRACTITIONER

## Pitfalls

- Forgetting `--bare`, so a CI run silently inherits local hooks, plugins, MCP servers, and CLAUDE.md and behaves differently per machine.
- Using auto mode in -p without handling the abort path; repeated classifier blocks kill the session, and a pipeline that ignores exit status reports false success.
- Running as root with bypassPermissions expected to work; it refuses to start.
- Parsing free-text output; without `--json-schema` the format is not a contract.
- Expecting local hooks and CLAUDE.md to apply under --bare; the flag exists precisely to skip them, so required facts and guards must be passed explicitly.

> [!gap] The verified pack does not cover the official GitHub Actions integration or its workflow syntax. Confirm current guidance at https://code.claude.com/docs/en/headless before wiring Actions jobs.

## Sources

- Run Claude Code programmatically, official docs, https://code.claude.com/docs/en/headless (retrieved 2026-07-07).
- Best practices for Claude Code, official docs, https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07).
- Choose a permission mode, official docs, https://code.claude.com/docs/en/permission-modes (retrieved 2026-07-07).
- Claude Code Advanced Best Practices, SmartScope, https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026 (published 2026-07-06, retrieved 2026-07-07).

## Related

- [[Claude Code]] is the interactive product this mode strips down for automation.
- [[Claude Agent SDK]] is the programmatic sibling; --bare is recommended for SDK calls too.
- [[Plan Mode and Permission Modes]] defines the mode semantics -p runs inherit.
- [[Claude Code Settings and Permissions]] shares its rule syntax with --allowedTools.
- [[Claude Code Hooks]] are skipped under --bare, a deliberate reproducibility trade.
- [[Claude Code Platform]] situates headless mode among the harness surfaces.
- [[Multi-Agent Fan-Out Research Flow]] can drive batches of headless workers.
- [[Sandbox Network and Filesystem Model]] describes the isolation CI runners need for permissive modes.
- [[Explore Plan Code Commit]] still applies; plan interactively, execute headlessly.
- [[Claude Code Project Memory]] is skipped under --bare, so bake required facts into the prompt.

## Next actions

- Convert one recurring scripted task to `claude -p --bare` with `--json-schema` output.
- Add exit-status handling for the auto-mode abort path in any pipeline using -p.
- Verify current GitHub Actions guidance to close the gap above.
- Prototype the next batch job on 3 files before running it across the repo.

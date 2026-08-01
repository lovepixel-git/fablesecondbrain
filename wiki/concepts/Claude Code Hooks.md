---
type: concept
title: "Claude Code Hooks"
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
  - "[[Claude Code Project Memory]]"
  - "[[Claude Code Settings and Permissions]]"
  - "[[Plan Mode and Permission Modes]]"
  - "[[Claude Code Subagents]]"
  - "[[Headless Claude Code and CI]]"
  - "[[Agent Skills System]]"
  - "[[Memory Injection Resistance]]"
source_urls:
  - "https://code.claude.com/docs/en/hooks (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)"
  - "https://blakecrosley.com/blog/claude-code-hooks-explained (retrieved 2026-07-07)"
  - "https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026 (retrieved 2026-07-07)"
---

# Claude Code Hooks

Hooks are the deterministic layer of Claude Code: shell commands that fire at fixed lifecycle events and, unlike advisory CLAUDE.md text, guarantee an action happens every time.

## What it is

A hook is a user-defined command bound to a lifecycle event in the Claude Code harness. The official docs draw the core contrast: "Unlike CLAUDE.md instructions which are advisory, hooks are deterministic and guarantee the action happens" (https://code.claude.com/docs/en/hooks). Hooks are the official mechanism for anything that must happen on every matching occurrence: formatting, policy guards, logging, notifications, verification gates.

Documented event families:

- Per session: SessionStart and SessionEnd.
- Per turn: UserPromptSubmit and Stop.
- Per tool call: PreToolUse and PostToolUse.
- Plus PermissionRequest and compaction events.

## How it works

- Hooks are configured in settings JSON (see [[Claude Code Settings and Permissions]]) with matchers that select which tools or events trigger them.
- Exit-code semantics carry the control flow: exit code 2 from a hook blocks the action, and the hook's stderr is fed back to Claude so it can adapt. Any other nonzero code does not block.
- Because settings files exist at managed, user, project, and local scopes, hooks can be personal, team-shared, or org-enforced.
- Hooks pair with verification: official best practice is giving Claude a check it can run, and checks "can gate harder" via Stop hooks or a fresh-context verification subagent (https://code.claude.com/docs/en/best-practices).
- Plugins ship hooks too: a plugin bundles hooks/hooks.json alongside skills, agents, and MCP servers, so guard packs are distributable across teams (https://code.claude.com/docs/en/plugins).

> [!key-insight] Hooks are the deterministic layer around a probabilistic model. Anything the model must never skip, format, verify, or refuse belongs in a hook, not in instructions.

## Best practice

- Use hooks, not CLAUDE.md prose, for any rule that must be enforced rather than suggested. EVIDENCE-BASED
- Return exit code 2 to block; treat stderr as the message channel that tells Claude why it was blocked. EVIDENCE-BASED
- Center production setups on the five workhorse events: PreToolUse, PostToolUse, UserPromptSubmit, SessionStart, and Stop. PRACTITIONER
- Use a Stop hook as a hard verification gate so a session cannot end while tests or lint fail. EVIDENCE-BASED
- Combine hooks with permission rules for defense in depth: "If a rule must be enforced, use Hooks or permissions" (https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026). PRACTITIONER
- Keep guard scripts fast and specific; a PreToolUse guard runs on every matching tool call. PRACTITIONER
- Scope team-binding hooks to project settings under version control so every teammate inherits the same guards. PRACTITIONER

## Pitfalls

- The exit-code footgun: practitioners flag that exit code 1 fails without blocking. "Exit 1 does not block anything" (https://blakecrosley.com/blog/claude-code-hooks-explained). Policy hooks must exit 2.
- Writing policy in CLAUDE.md and expecting hook-like guarantees; advisory text can be ignored under context pressure.
- Forgetting matchers, so a hook fires on every tool call instead of the intended subset.
- Ignoring hook scope: a guard in user settings does not protect teammates; a project-scope hook does.
- Headless runs with --bare skip auto-discovered hooks entirely, so a pipeline that assumes local guards run unprotected (see [[Headless Claude Code and CI]]).

> [!gap] The verified pack lists the event families but not each event's full input schema or JSON payload fields. Consult https://code.claude.com/docs/en/hooks before building a new guard.

## Sources

- Hooks reference, official docs, https://code.claude.com/docs/en/hooks (retrieved 2026-07-07).
- Best practices for Claude Code, official docs, https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07).
- Claude Code Hooks Explained: The Deterministic Layer Around Your Agent, Blake Crosley, https://blakecrosley.com/blog/claude-code-hooks-explained (published 2026-07-01, retrieved 2026-07-07).
- Claude Code Advanced Best Practices, SmartScope, https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026 (published 2026-07-06, retrieved 2026-07-07).
- Create plugins, Claude Code docs, https://code.claude.com/docs/en/plugins (retrieved 2026-07-07).

## Related

- [[Claude Code]] hosts the lifecycle events hooks attach to.
- [[Claude Code Project Memory]] is the advisory layer hooks harden.
- [[Claude Code Settings and Permissions]] is where hooks are declared and scoped.
- [[Plan Mode and Permission Modes]] handles interactive gating; hooks gate programmatically.
- [[Claude Code Subagents]] can serve as fresh-context verifiers that hooks trigger.
- [[Headless Claude Code and CI]] relies on hooks for unattended policy since no human watches.
- [[Agent Skills System]] packages hooks inside plugins via hooks/hooks.json.
- [[Memory Injection Resistance]] motivates guard hooks against hostile content.
- [[Explore Plan Code Commit]] gains a verification backstop from Stop hooks.
- [[Sandbox Network and Filesystem Model]] bounds what a hook script itself can reach.

## Next actions

- Audit existing guards to confirm every blocking path exits 2, not 1.
- Add a Stop hook that runs the project test suite as a session gate.
- Read the full hooks reference to fill the payload-schema gap above.
- Decide which guards belong in project scope versus user scope and move them.

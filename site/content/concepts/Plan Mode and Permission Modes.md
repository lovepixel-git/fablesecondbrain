---
type: concept
title: "Plan Mode and Permission Modes"
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
  - "[[Explore Plan Code Commit]]"
  - "[[Claude Code Settings and Permissions]]"
  - "[[Claude Code Hooks]]"
  - "[[Headless Claude Code and CI]]"
  - "[[Claude Code Subagents]]"
  - "[[Sandbox Network and Filesystem Model]]"
  - "[[Claude Code Quickstart for Fable 5]]"
source_urls:
  - "https://code.claude.com/docs/en/permission-modes (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)"
---

# Plan Mode and Permission Modes

Claude Code ships six permission modes, and the high-leverage move is plan mode for research before changes, with bypassPermissions reserved strictly for isolated environments.

## What it is

Permission modes set how much Claude Code may do before asking. The documented six:

- default, labeled Manual in the interface.
- acceptEdits (exact boundaries not captured in the verified pack; see the gap below).
- plan, the read-only research mode.
- auto, a research preview since v2.1.83 with a classifier reviewing each action.
- dontAsk (details not captured; see the gap below).
- bypassPermissions, which skips prompts entirely and refuses to start as root.

You cycle modes with Shift+Tab in the CLI, or set them via `--permission-mode` and the `defaultMode` setting.

Plan mode is the read-only research mode: "Plan mode tells Claude to research and propose changes without making them" (https://code.claude.com/docs/en/permission-modes). Auto mode (research preview, v2.1.83+) removes routine prompts by having "A separate classifier model reviews actions before they run" (same URL).

## How it works

- Plan mode entry: Shift+Tab, a /plan prompt prefix, or `claude --permission-mode plan`. Claude reads files and proposes a plan without editing source.
- Approving the plan switches the session into the chosen execution mode; Ctrl+G opens the plan in a text editor for direct edits before proceeding.
- Auto mode's classifier blocks scope escalation, unknown infrastructure, and hostile-content-driven actions; it pauses back to prompting after 3 consecutive or 20 total blocks, and in non-interactive -p runs repeated blocks abort the session.
- bypassPermissions skips prompts entirely and refuses to start as root. The docs restrict it: "Only use this mode in isolated environments like containers, VMs, or dev containers" (https://code.claude.com/docs/en/permission-modes).
- The modes implement the official workflow: explore, plan, implement, commit, per [[Explore Plan Code Commit]].
- Mode switching is consistent across surfaces: the JetBrains plugin runs the CLI in the IDE terminal with the same Shift+Tab cycling, and the VS Code extension adds plan review in its UI (https://code.claude.com/docs/en/vs-code).

> [!key-insight] Modes trade oversight for speed in explicit steps. Plan mode buys understanding before risk, auto mode buys speed with a classifier as chaperone, and bypassPermissions buys speed with isolation as the only safety net.

## Best practice

- Start non-trivial work in plan mode; research and a reviewed plan precede any edit. EVIDENCE-BASED
- Skip planning overhead for small, clearly scoped fixes: "If you could describe the diff in one sentence, skip the plan" (https://code.claude.com/docs/en/best-practices). EVIDENCE-BASED
- Edit the plan with Ctrl+G before approving when direction is close but not exact. EVIDENCE-BASED
- Use auto mode for prompt fatigue only after accepting its research-preview status and block thresholds. EVIDENCE-BASED
- Confine bypassPermissions to containers, VMs, or dev containers, never a primary workstation. EVIDENCE-BASED
- Pin a per-project `defaultMode` in settings so each repo opens in its intended posture. PRACTITIONER
- Give the execution phase a verifiable check (tests, build exit code, screenshot comparison) so plan approval hands off to a self-correcting loop. EVIDENCE-BASED

## Pitfalls

- Running bypassPermissions on the host machine; the isolation restriction exists because nothing prompts before destructive actions.
- Treating plan mode output as executed work; nothing changes until the plan is approved into an execution mode.
- Relying on auto mode in CI-style -p runs without handling the abort path repeated classifier blocks trigger.
- Confusing permission modes with permission rules; modes set the interaction posture, rules in settings decide specific allows and denies (see [[Claude Code Settings and Permissions]]).
- Planning everything: for a fix you can describe in one sentence, plan mode is overhead, not safety.

> [!gap] The verified pack does not detail the exact behavioral difference between dontAsk and bypassPermissions, or acceptEdits boundaries. Check https://code.claude.com/docs/en/permission-modes before relying on either.

## Sources

- Choose a permission mode, official docs, https://code.claude.com/docs/en/permission-modes (retrieved 2026-07-07).
- Best practices for Claude Code, official docs, formerly the anthropic.com engineering post, https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07).
- Use Claude Code in VS Code, official docs, https://code.claude.com/docs/en/vs-code (retrieved 2026-07-07).

## Related

- [[Claude Code]] is the harness whose interaction posture these modes control.
- [[Explore Plan Code Commit]] is the official workflow plan mode anchors.
- [[Claude Code Settings and Permissions]] holds defaultMode and the rule lists modes interact with.
- [[Claude Code Hooks]] adds deterministic gates that apply in every mode.
- [[Headless Claude Code and CI]] inherits mode semantics through --permission-mode flags.
- [[Claude Code Subagents]] include a built-in Plan agent for the research phase.
- [[Sandbox Network and Filesystem Model]] provides the isolation bypassPermissions presumes.
- [[Claude Code Quickstart for Fable 5]] teaches Shift+Tab cycling on day one.
- [[Claude Code Project Memory]] can note the intended mode posture per repo.

## Next actions

- Set defaultMode per repo so risky projects open in Manual and sandboxes in auto.
- Practice the Ctrl+G plan-edit flow once so it is available under time pressure.
- Resolve the dontAsk versus bypassPermissions gap from the official mode docs.
- Trial auto mode in one sandboxed repo and log how often the classifier blocks.

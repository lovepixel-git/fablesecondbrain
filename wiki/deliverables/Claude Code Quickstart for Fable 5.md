---
type: deliverable
title: "Claude Code Quickstart for Fable 5"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/harness/claude-code
  - note/deliverable
domain: claude-code-harness
confidence: evidence-based
related:
  - "[[Claude Code]]"
  - "[[Claude Code Project Memory]]"
  - "[[Plan Mode and Permission Modes]]"
  - "[[Claude Code Settings and Permissions]]"
  - "[[Claude Code Hooks]]"
  - "[[Claude Code Subagents]]"
  - "[[Headless Claude Code and CI]]"
  - "[[Explore Plan Code Commit]]"
  - "[[Fable 5 Best Practices Cheat Sheet]]"
  - "[[Agent Skills System]]"
source_urls:
  - "https://code.claude.com/docs/en/overview (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/memory (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/permission-modes (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/settings (retrieved 2026-07-07)"
---

# Claude Code Quickstart for Fable 5

Install Claude Code from the official per-surface guides, seed a short CLAUDE.md with /init, start work in plan mode, tighten permissions in settings, then run the explore, plan, implement, commit loop with a verifiable check.

## What it is

- A zero-to-productive path for running Claude Fable 5 inside Claude Code, built only from claims verified on 2026-07-07.
- Fable 5 is deployed in claude.ai and Claude Code for Pro, Max, Team, and Enterprise users (https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5).
- The canonical documentation lives at code.claude.com/docs: docs.claude.com Claude Code pages 301-redirect there, and the former engineering best-practices post 308-redirects to code.claude.com/docs/en/best-practices.

## How it works

1. Install and pick a surface. The docs carry per-surface guides for CLI, VS Code, JetBrains, Desktop, and Web (https://code.claude.com/docs/en/overview). For IDE work the VS Code extension is "the recommended way to use Claude Code in VS Code."; it bundles its own CLI copy while sharing ~/.claude/settings.json, history, CLAUDE.md, and MCP config with the terminal.
2. Seed project memory. Run /init to generate a starter CLAUDE.md; include only what Claude cannot infer from code (build commands, divergent style rules, repo etiquette, gotchas) and target under 200 lines per file. Scopes load in order: managed policy, user ~/.claude/CLAUDE.md, project ./CLAUDE.md or ./.claude/CLAUDE.md, and gitignored ./CLAUDE.local.md. @path imports recurse up to four hops; "Claude Code reads CLAUDE.md, not AGENTS.md." (https://code.claude.com/docs/en/memory).
3. Know the second memory. Auto memory is on by default since v2.1.59: Claude saves per-repository learnings under ~/.claude/projects/<project>/memory/, the first 200 lines or 25KB of MEMORY.md load each session, /memory inspects it, and autoMemoryEnabled false disables it.
4. Learn the six permission modes: default (Manual), acceptEdits, plan, auto, dontAsk, bypassPermissions, cycled with Shift+Tab or set via --permission-mode and defaultMode. Plan mode is read-only research: "Plan mode tells Claude to research and propose changes without making them.", entered via Shift+Tab, a /plan prefix, or claude --permission-mode plan, with Ctrl+G opening the plan in an editor (https://code.claude.com/docs/en/permission-modes).
5. Configure settings. Priority order: managed org settings, then command-line arguments, then .claude/settings.local.json, then project .claude/settings.json, then user ~/.claude/settings.json; permission rules merge across scopes and most edits hot-reload (https://code.claude.com/docs/en/settings).
6. Run the first agentic loop: explore and plan in plan mode, approve into an execution mode, implement, commit. Give the model a check it can run, "tests, a build, a screenshot to compare", so it iterates until the check passes instead of using you as the verification loop.

## Best practice

- Skip planning overhead on small fixes: "If you could describe the diff in one sentence, skip the plan." (https://code.claude.com/docs/en/best-practices). EVIDENCE-BASED
- Reserve bypassPermissions for isolated environments like containers or VMs; it refuses to start as root (https://code.claude.com/docs/en/permission-modes). EVIDENCE-BASED
- Try auto mode (research preview, v2.1.83+) for prompt fatigue: a separate classifier model reviews actions, blocking scope escalation and hostile-content-driven actions, pausing after 3 consecutive or 20 total blocks. EVIDENCE-BASED
- Enforce must-happen rules with hooks, not CLAUDE.md prose; hooks run deterministically at lifecycle events and exit code 2 blocks the action (https://code.claude.com/docs/en/hooks). EVIDENCE-BASED
- Put every-session facts in CLAUDE.md and multi-step procedures in skills, since "a skill's body loads only when it's used" (https://code.claude.com/docs/en/skills). EVIDENCE-BASED
- Isolate research and verification in subagents; each runs in its own context window with a custom system prompt (https://code.claude.com/docs/en/sub-agents). EVIDENCE-BASED
- For CI and scripts use claude -p with --allowedTools, json output, and the --bare flag, "the recommended mode for scripted and SDK calls" (https://code.claude.com/docs/en/headless). EVIDENCE-BASED
- Prototype fan-out batch runs on 2 or 3 files before scaling to the whole repo. PRACTITIONER

## Pitfalls

- Bloated CLAUDE.md files cause Claude to ignore your actual instructions; ruthless pruning is official guidance, with IMPORTANT or YOU MUST emphasis reserved for critical rules.
- Hook scripts that exit 1 expecting a block; "Exit 1 does not block anything." Policy hooks must exit 2 (https://blakecrosley.com/blog/claude-code-hooks-explained).
- Correcting the same failure repeatedly in one session; official guidance says a clean session with a better prompt almost always outperforms a long session.
- Expecting AGENTS.md to load; the official pattern is a CLAUDE.md that imports it or a symlink.
- Looking for the /agents creation wizard; as of v2.1.198 it is removed in favor of asking Claude or editing agent files directly.
- In non-interactive auto-mode runs, repeated classifier blocks abort the session; plan permissions ahead for unattended work.

## Sources

- Claude Code Overview, https://code.claude.com/docs/en/overview (retrieved 2026-07-07).
- Best practices for Claude Code, https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07).
- CLAUDE.md and auto memory, https://code.claude.com/docs/en/memory (retrieved 2026-07-07).
- Choose a permission mode, https://code.claude.com/docs/en/permission-modes (retrieved 2026-07-07).
- Claude Code settings, https://code.claude.com/docs/en/settings (retrieved 2026-07-07).
- Hooks reference, https://code.claude.com/docs/en/hooks (retrieved 2026-07-07).
- Run Claude Code programmatically, https://code.claude.com/docs/en/headless (retrieved 2026-07-07).
- Use Claude Code in VS Code, https://code.claude.com/docs/en/vs-code (retrieved 2026-07-07).
- Introducing Claude Fable 5 and Claude Mythos 5, https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07).

## Related

- [[Claude Code]] is the harness this quickstart configures.
- [[Claude Code Project Memory]] deepens step 2 on memory scopes and imports.
- [[Plan Mode and Permission Modes]] deepens step 4 on the six modes.
- [[Claude Code Settings and Permissions]] deepens step 5 on the settings hierarchy.
- [[Claude Code Hooks]] covers the deterministic enforcement layer.
- [[Claude Code Subagents]] covers context-isolated delegation.
- [[Headless Claude Code and CI]] extends the loop into pipelines.
- [[Explore Plan Code Commit]] is the core workflow in step 6.
- [[Fable 5 Best Practices Cheat Sheet]] compresses this into fifteen practices.
- [[Agent Skills System]] explains the skills that replace custom commands.

## Next actions

- Verify the quickstart end-to-end on a fresh machine and note any drift from the docs.
- Add a worked example of a PreToolUse hook with exit 2 blocking.
- Track auto mode's exit from research preview status.

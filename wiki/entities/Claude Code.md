---
type: entity
title: "Claude Code"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/harness/claude-code
  - note/entity
domain: claude-code-harness
confidence: evidence-based
related:
  - "[[Claude Fable 5]]"
  - "[[Claude Code Platform]]"
  - "[[Claude Code Project Memory]]"
  - "[[Claude Code Hooks]]"
  - "[[Claude Code Subagents]]"
  - "[[Plan Mode and Permission Modes]]"
  - "[[Claude Code Settings and Permissions]]"
  - "[[Headless Claude Code and CI]]"
  - "[[Agent Skills System]]"
  - "[[Model Context Protocol]]"
  - "[[Claude Agent SDK]]"
  - "[[Explore Plan Code Commit]]"
source_urls:
  - "https://code.claude.com/docs/en/overview (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/memory (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/permission-modes (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/settings (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/hooks (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/sub-agents (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/headless (retrieved 2026-07-07)"
---

# Claude Code

Claude Code is Anthropic's agentic coding harness, shipped as a CLI with VS Code, JetBrains, Desktop, and Web surfaces, and its canonical documentation now lives at code.claude.com/docs.

## What it is

Claude Code is the agentic coding tool documented at code.claude.com/docs. The old docs.claude.com Claude Code pages 301-redirect there, and the former engineering post at anthropic.com/engineering/claude-code-best-practices 308-redirects to code.claude.com/docs/en/best-practices, which makes the docs page the current official best-practices guide. The docs cover memory, permission modes, settings, hooks, subagents, skills, non-interactive mode, and per-surface guides for CLI, VS Code, JetBrains, Desktop, and Web. The source repository is github.com/anthropics/claude-code.

The VS Code extension (also installable in Cursor and other forks) is the recommended IDE integration. It provides inline diffs, @-mentions with line ranges, plan review, and checkpoints, bundles its own CLI copy, and shares ~/.claude/settings.json, conversation history, CLAUDE.md, and MCP config with the terminal CLI. The JetBrains plugin runs the CLI in the IDE terminal with the same Shift+Tab mode switching.

> [!gap] The claim packs verify Claude Code mechanics but say nothing Fable 5 specific about its deployment in this harness. The system prompt export describes claude.ai, not Claude Code. See [[Export Omits Claude Code Harness]] and [[Which Export Rules Bind Claude Code]] before assuming export rules apply here.

## How it works

- **Project memory.** CLAUDE.md files load at defined scopes in order, managed policy (for example /etc/claude-code/CLAUDE.md on Linux), user ~/.claude/CLAUDE.md, project ./CLAUDE.md or ./.claude/CLAUDE.md, and gitignored ./CLAUDE.local.md. Parent-directory files load in full at launch, subdirectory files load on demand. @path imports recurse up to four hops. "Claude Code reads CLAUDE.md, not AGENTS.md." (https://code.claude.com/docs/en/memory); repos using AGENTS.md import it from CLAUDE.md or symlink it.
- **Auto memory.** A second memory system, on by default since v2.1.59, stores "notes Claude writes itself based on your corrections and preferences" (https://code.claude.com/docs/en/memory) under ~/.claude/projects/<project>/memory/. The first 200 lines or 25KB of MEMORY.md load every session; inspect via /memory, disable with autoMemoryEnabled false.
- **Permission modes.** Six modes, default (Manual), acceptEdits, plan, auto, dontAsk, bypassPermissions, cycled with Shift+Tab or set via --permission-mode and the defaultMode setting. Plan mode is read-only research; approving the plan switches into the chosen execution mode, and Ctrl+G opens the plan in a text editor.
- **Auto mode.** A research preview (v2.1.83+) where "A separate classifier model reviews actions before they run" (https://code.claude.com/docs/en/permission-modes), blocking scope escalation, unknown infrastructure, and hostile-content-driven actions. It pauses back to prompting after 3 consecutive or 20 total blocks; in -p runs repeated blocks abort the session.
- **Settings hierarchy.** Managed org settings override command-line arguments, then .claude/settings.local.json, then project .claude/settings.json, then user ~/.claude/settings.json. Permission rules merge across scopes rather than override, and most edits hot-reload.
- **Hooks.** Deterministic shell commands at lifecycle events (SessionStart, SessionEnd, UserPromptSubmit, Stop, PreToolUse, PostToolUse, PermissionRequest, compaction events), configured in settings JSON with matchers. Exit code 2 blocks the action and feeds stderr back to Claude.
- **Subagents.** Markdown files with YAML frontmatter (name, description, tools, model) in .claude/agents/ or ~/.claude/agents/. "Each subagent runs in its own context window with a custom system prompt" (https://code.claude.com/docs/en/sub-agents). Built-in Explore, Plan, and general-purpose subagents are delegated to automatically; the /agents wizard is removed as of v2.1.198.
- **Skills and commands.** "Custom commands have been merged into skills." (https://code.claude.com/docs/en/skills). A .claude/commands/deploy.md file and a .claude/skills/deploy/SKILL.md both create /deploy; skills add supporting files, disable-model-invocation control, $ARGUMENTS, and dynamic context injection, and follow the Agent Skills open standard.
- **Headless.** claude -p is the official CI and scripting path, with text, json, and stream-json output, --json-schema, --allowedTools pre-approval, --continue/--resume, and --bare to skip auto-discovery of hooks, skills, plugins, MCP servers, and CLAUDE.md for reproducible runs.

## Best practice

- Give Claude a verifiable check, tests, a build exit code, a linter, or a screenshot comparison, so it iterates until the check passes instead of using you as the verification loop. EVIDENCE-BASED
- Follow explore, plan, implement, commit; use plan mode to research first, but "If you could describe the diff in one sentence, skip the plan." (https://code.claude.com/docs/en/best-practices). EVIDENCE-BASED
- Keep CLAUDE.md ruthlessly pruned to what Claude cannot infer from code, target under 200 lines per file, and run /init for a starter. EVIDENCE-BASED
- Enforce mandatory rules with hooks and permission rules, not prose; "Unlike CLAUDE.md instructions which are advisory, hooks are deterministic and guarantee the action happens." (https://code.claude.com/docs/en/hooks). EVIDENCE-BASED
- Split persistent context by load pattern, every-session facts in CLAUDE.md, multi-step procedures in skills, because "a skill's body loads only when it's used" (https://code.claude.com/docs/en/skills). EVIDENCE-BASED
- Run /clear between unrelated tasks, and after roughly two failed corrections start a fresh session with a better prompt. EVIDENCE-BASED
- Restrict bypassPermissions to isolated environments such as containers, VMs, or dev containers; it refuses to start as root. EVIDENCE-BASED
- Make policy hooks exit with code 2; "Exit 1 does not block anything." (https://blakecrosley.com/blog/claude-code-hooks-explained). PRACTITIONER
- Prototype fan-out batch runs on 2 to 3 files before scaling to the full set. PRACTITIONER

## Pitfalls

- "Bloated CLAUDE.md files cause Claude to ignore your actual instructions!" (https://code.claude.com/docs/en/best-practices). Overlong memory files reduce adherence.
- Expecting AGENTS.md to be read natively; it is not, import or symlink it.
- Writing policy hooks that exit 1 and assuming they block; only exit 2 blocks.
- Relying on auto mode in unattended -p runs; repeated classifier blocks abort the session.
- Assuming a lower-scope settings file wins; managed org settings sit above everything, including CLI flags.
- Scripting against the /agents creation wizard; it is removed in v2.1.198 in favor of editing agent files directly.

## Sources

- Claude Code overview, official docs, https://code.claude.com/docs/en/overview (retrieved 2026-07-07)
- Best practices for Claude Code, official docs, https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)
- CLAUDE.md and auto memory, official docs, https://code.claude.com/docs/en/memory (retrieved 2026-07-07)
- Choose a permission mode, official docs, https://code.claude.com/docs/en/permission-modes (retrieved 2026-07-07)
- Claude Code settings, official docs, https://code.claude.com/docs/en/settings (retrieved 2026-07-07)
- Hooks reference, official docs, https://code.claude.com/docs/en/hooks (retrieved 2026-07-07)
- Create custom subagents, official docs, https://code.claude.com/docs/en/sub-agents (retrieved 2026-07-07)
- Run Claude Code programmatically, official docs, https://code.claude.com/docs/en/headless (retrieved 2026-07-07)
- Use Claude Code in VS Code, official docs, https://code.claude.com/docs/en/vs-code (retrieved 2026-07-07)
- Claude Code Hooks Explained, Blake Crosley, https://blakecrosley.com/blog/claude-code-hooks-explained (published 2026-07-01, retrieved 2026-07-07)
- Claude Code Advanced Best Practices, SmartScope, https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026 (published 2026-07-06, retrieved 2026-07-07)

## Related

- [[Claude Fable 5]], the model this harness runs in this brain's scope.
- [[Claude Code Platform]], the platform hub page for this surface.
- [[Claude Code Project Memory]], deep dive on the memory scopes summarized here.
- [[Claude Code Hooks]], the deterministic enforcement layer in detail.
- [[Claude Code Subagents]], isolated-context delegation mechanics.
- [[Plan Mode and Permission Modes]], the six modes and when to use each.
- [[Claude Code Settings and Permissions]], the settings hierarchy and rule merging.
- [[Headless Claude Code and CI]], the -p and --bare automation path.
- [[Agent Skills System]], the skills standard Claude Code implements and extends.
- [[Model Context Protocol]], how external tools connect to this harness.
- [[Claude Agent SDK]], the same internals exposed as libraries.
- [[Explore Plan Code Commit]], the canonical workflow flow note.
- [[Which Export Rules Bind Claude Code]], boundary between export claims and this harness.
- [[Export Omits Claude Code Harness]], why the corpus cannot source this note.

## Next actions

- Capture Fable 5 specific Claude Code behavior (model IDs, defaults) from official release notes when available.
- Verify the v2.1.x feature gates (auto memory v2.1.59, auto mode v2.1.83, wizard removal v2.1.198) against the CHANGELOG in github.com/anthropics/claude-code.
- Cross-check hook lifecycle event names against a live `claude` install on Aurora.

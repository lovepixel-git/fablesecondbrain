---
type: platform
title: "Claude Code Platform"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/harness/claude-code
  - note/platform
domain: claude-code-harness
confidence: evidence-based
related:
  - "[[Claude Code]]"
  - "[[Claude Code Hooks]]"
  - "[[Claude Code Subagents]]"
  - "[[Plan Mode and Permission Modes]]"
  - "[[Claude Code Settings and Permissions]]"
  - "[[Headless Claude Code and CI]]"
  - "[[Claude Code Project Memory]]"
  - "[[Agent Skills System]]"
  - "[[Which Export Rules Bind Claude Code]]"
  - "[[Claude Agent SDK]]"
source_urls:
  - "https://code.claude.com/docs/en/overview (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/vs-code (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)"
---

# Claude Code Platform

Claude Code is Anthropic's developer harness, reachable as a CLI, a VS Code extension, a JetBrains plugin, Desktop, and Web, documented canonically at code.claude.com/docs, and it serves Claude Fable 5 to Pro, Max, Team, and Enterprise users.

## What it is

The agentic coding surface built around a terminal-native agent loop. Its canonical documentation moved: docs.claude.com Claude Code pages 301-redirect to code.claude.com/docs, and the former engineering post at anthropic.com/engineering/claude-code-best-practices 308-redirects to code.claude.com/docs/en/best-practices, making the docs page the current official best-practices guide. The docs cover memory, permission modes, settings, hooks, subagents, skills, non-interactive mode, and per-surface guides for CLI, VS Code, JetBrains, Desktop, and Web. The same engine is exposed programmatically as the Claude Agent SDK.

## How it works

- **Surfaces.** The VS Code extension (also installable in Cursor and other forks) is the recommended IDE integration: "This is the recommended way to use Claude Code in VS Code." (https://code.claude.com/docs/en/vs-code). It provides inline diffs, @-mentions with line ranges, plan review, and checkpoints, bundles its own CLI copy, and shares ~/.claude/settings.json, conversation history, CLAUDE.md, and MCP config with the terminal CLI. The JetBrains plugin runs the CLI in the IDE terminal with the same Shift+Tab mode switching.
- **Memory.** Two systems: CLAUDE.md files loading across managed, user, project, and local scopes with sizing guidance to "target under 200 lines per CLAUDE.md file", plus auto memory (default-on since v2.1.59), where Claude saves per-repository learnings under ~/.claude/projects/<project>/memory/ and the first 200 lines or 25KB of MEMORY.md load into every session.
- **Control plane.** Six permission modes (default Manual, acceptEdits, plan, auto, dontAsk, bypassPermissions) cycled with Shift+Tab; settings merge across a documented hierarchy; hooks execute deterministically at lifecycle events; subagents run in separate context windows; custom slash commands and skills are one system following the Agent Skills open standard.
- **Automation.** Non-interactive mode (claude -p) is the official path for CI and pipelines with text, json, and stream-json output, and "--bare is the recommended mode for scripted and SDK calls" (https://code.claude.com/docs/en/headless).
- **Model availability.** Claude Fable 5 is deployed in Claude Code for Pro, Max, Team, and Enterprise users since the June 9, 2026 launch, with the June 12 to July 1 export-control interruption.
- **Context split by load pattern.** Official guidance puts broadly applicable, every-session facts in CLAUDE.md and moves multi-step procedures into skills, since "a skill's body loads only when it's used" (https://code.claude.com/docs/en/skills); CLAUDE.md also supports @path imports up to four hops.

> [!key-insight]
> The platform's design theme is determinism around a probabilistic core: hooks execute at lifecycle events regardless of what the model decides ("Unlike CLAUDE.md instructions which are advisory, hooks are deterministic and guarantee the action happens.", https://code.claude.com/docs/en/hooks), permission rules merge across scopes, and exit code 2 from a hook blocks the action while stderr feeds back to Claude.

## Best practice

- Read platform behavior from code.claude.com/docs, not from older anthropic.com or docs.claude.com URLs; both redirect. EVIDENCE-BASED
- Pick the surface by workflow, IDE extension for inline review, CLI for terminal-native work, headless -p for automation; configuration is shared underneath. EVIDENCE-BASED
- Restrict bypassPermissions to isolated environments; the docs say to use it only in containers, VMs, or dev containers, and it refuses to start as root. EVIDENCE-BASED
- Treat auto mode (research preview, v2.1.83+) as a monitored middle ground: "A separate classifier model reviews actions before they run" (https://code.claude.com/docs/en/permission-modes), and it pauses back to prompting after repeated blocks. EVIDENCE-BASED
- Constrain through systems, hooks and permission rules, rather than prompt prose, per converging official and practitioner guidance. PRACTITIONER
- Review auto memory with /memory periodically; the first 200 lines or 25KB of MEMORY.md enter every session, so stale self-written notes compound. EVIDENCE-BASED
- For CI, pre-approve tools with --allowedTools permission-rule syntax and use --json-schema when downstream steps parse output. EVIDENCE-BASED

## Pitfalls

- Citing the old best-practices blog URL as a source; it is a redirect, and content ownership now sits in the docs.
- Assuming AGENTS.md works: "Claude Code reads CLAUDE.md, not AGENTS.md." (https://code.claude.com/docs/en/memory); the official pattern is a CLAUDE.md that imports it.
- Forgetting auto memory exists; Claude writes its own per-repo notes, inspectable via /memory and disabled with autoMemoryEnabled false.
- Expecting the /agents creation wizard; as of v2.1.198 it is removed in favor of asking Claude or editing subagent files directly.
- Applying claude.ai export rules to this harness; the system prompt capture documents the consumer surface, and this platform's contract lives in its docs.

## Sources

- Claude Code Overview, official docs: https://code.claude.com/docs/en/overview (retrieved 2026-07-07)
- Best practices for Claude Code, official docs: https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)
- Use Claude Code in VS Code, official docs: https://code.claude.com/docs/en/vs-code (retrieved 2026-07-07)
- Run Claude Code programmatically, official docs: https://code.claude.com/docs/en/headless (retrieved 2026-07-07)
- How Claude remembers your project, official docs: https://code.claude.com/docs/en/memory (retrieved 2026-07-07)
- Choose a permission mode, official docs: https://code.claude.com/docs/en/permission-modes (retrieved 2026-07-07)
- Introducing Claude Fable 5 and Claude Mythos 5, Claude Platform docs: https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)

## Related

- [[Claude Code]] because this note covers the platform surfaces around that product.
- [[Claude Code Hooks]] because hooks are the platform's deterministic enforcement layer.
- [[Claude Code Subagents]] because separate-context subagents are a core platform primitive.
- [[Plan Mode and Permission Modes]] because the six-mode control plane defines what runs unprompted.
- [[Claude Code Settings and Permissions]] because the settings hierarchy configures every surface.
- [[Headless Claude Code and CI]] because -p with --bare is the platform's automation face.
- [[Claude Code Project Memory]] because scoped memory files are platform-level behavior.
- [[Agent Skills System]] because commands and skills merged into one extension system here.
- [[Which Export Rules Bind Claude Code]] because it resolves the claude.ai-versus-Code scoping question.
- [[Claude Agent SDK]] because the SDK exports this platform's engine as libraries.

## Next actions

- Record the installed Claude Code version and which documented features (auto mode, auto memory) it carries.
- Map this vault's own hook and settings usage against the documented hierarchy.
- Cross-check [[Export Omits Claude Code Harness]] once the corpus chapter notes are complete.
- Inventory this project's auto memory contents via /memory and prune stale self-written notes.

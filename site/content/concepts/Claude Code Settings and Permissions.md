---
type: concept
title: "Claude Code Settings and Permissions"
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
  - "[[Plan Mode and Permission Modes]]"
  - "[[Claude Code Project Memory]]"
  - "[[Headless Claude Code and CI]]"
  - "[[Agent Skills System]]"
  - "[[Sandbox Network and Filesystem Model]]"
  - "[[Which Export Rules Bind Claude Code]]"
source_urls:
  - "https://code.claude.com/docs/en/settings (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/permission-modes (retrieved 2026-07-07)"
  - "https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026 (retrieved 2026-07-07)"
---

# Claude Code Settings and Permissions

Claude Code settings resolve through a five-level hierarchy where managed org policy always wins, and permission rules merge across scopes instead of overriding each other.

## What it is

Settings files are the machine-readable configuration layer of [[Claude Code]]. They configure permission allow and deny rules, hooks, environment variables, and the model. The documented priority order, highest first:

1. Managed organization settings.
2. Command-line arguments.
3. Project-local `.claude/settings.local.json`.
4. Project `.claude/settings.json` (shared with the team).
5. User `~/.claude/settings.json`.

The docs state the resolution rule: "When the same setting appears in multiple scopes, Claude Code applies them in priority order" (https://code.claude.com/docs/en/settings). Permission rules are the exception: they merge across scopes rather than override, so a user allow and a project deny both apply.

## How it works

- Most settings edits hot-reload without restarting the session.
- Permission-rule syntax also powers headless pre-approval: `--allowedTools` in `claude -p` takes the same rule format (see [[Headless Claude Code and CI]]).
- `defaultMode` selects the starting permission mode per scope, connecting settings to [[Plan Mode and Permission Modes]].
- Hooks are declared here too, giving each scope its own deterministic guards.
- The VS Code extension bundles its own CLI copy but shares `~/.claude/settings.json`, conversation history, CLAUDE.md, and MCP config with the terminal CLI, so one settings file governs both surfaces (https://code.claude.com/docs/en/vs-code).
- Model selection lives here as well, so a repo can pin its model at project scope while a user default covers everything else.

> [!key-insight] The hierarchy answers "who wins", but permissions answer "everyone speaks": rules merge across scopes, so the effective policy is the union of every scope's allows and denies.

## Best practice

- Put team-binding rules in project `.claude/settings.json` under version control, and personal preferences in user or local scope. PRACTITIONER
- Enforce mandatory constraints with permission rules and hooks rather than instruction text: "If a rule must be enforced, use Hooks or permissions" (https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026). PRACTITIONER
- Remember merge semantics when debugging: a surprising deny may come from any scope, since permission rules accumulate. EVIDENCE-BASED
- Use managed settings for organization-wide policy, since nothing below can override them. EVIDENCE-BASED
- Keep `.claude/settings.local.json` for machine-specific experiments so the shared file stays clean. PRACTITIONER
- Rely on hot reload during rule iteration; most settings edits apply without restarting the session. EVIDENCE-BASED

## Pitfalls

- Assuming override semantics for permissions; rules merge, so deleting a project allow does not remove a user-scope allow.
- Editing user settings to fix a project problem, which silently changes behavior in every other repo.
- Forgetting command-line arguments outrank every settings file except managed policy, so a stale shell alias can shadow careful configuration.
- Treating settings as secret storage; they are plain JSON, often committed.
- Expecting settings alone to constrain a --bare headless run, which skips auto-discovered config; pass explicit flags instead.

> [!gap] The verified pack confirms allow and deny rule lists but does not document the full rule grammar (ask lists, tool-specifier patterns, directory extensions). Verify against https://code.claude.com/docs/en/settings before authoring complex rules.

## Sources

- Claude Code settings, official docs, https://code.claude.com/docs/en/settings (retrieved 2026-07-07).
- Choose a permission mode, official docs, https://code.claude.com/docs/en/permission-modes (retrieved 2026-07-07).
- Use Claude Code in VS Code, official docs, https://code.claude.com/docs/en/vs-code (retrieved 2026-07-07).
- Claude Code Advanced Best Practices, SmartScope, https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026 (published 2026-07-06, retrieved 2026-07-07).

## Related

- [[Claude Code]] reads this hierarchy at launch and on hot reload.
- [[Claude Code Hooks]] live inside these files and inherit their scoping.
- [[Plan Mode and Permission Modes]] are selected here via defaultMode.
- [[Claude Code Project Memory]] is the prose counterpart with a similar scope ladder.
- [[Headless Claude Code and CI]] reuses the permission-rule syntax in --allowedTools.
- [[Agent Skills System]] respects enterprise-over-personal-over-project precedence for skills.
- [[Sandbox Network and Filesystem Model]] bounds what any permission grant can reach.
- [[Which Export Rules Bind Claude Code]] separates harness config from claude.ai system-prompt rules.
- [[Claude Code Subagents]] can be constrained by the same permission rules.
- [[Claude Code Quickstart for Fable 5]] walks the first settings file setup.

## Next actions

- Audit which scope each active permission rule comes from in the main repo.
- Move any team-relevant allows from user scope into project settings.
- Read the settings reference to close the rule-grammar gap noted above.
- Verify no secrets sit in any committed settings file across active repos.

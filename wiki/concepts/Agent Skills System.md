---
type: concept
title: "Agent Skills System"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/tools
  - note/concept
domain: tools-and-skills
confidence: evidence-based
related:
  - "[[Claude Code]]"
  - "[[Tool Search and Deferred Tools]]"
  - "[[Claude Code Project Memory]]"
  - "[[Model Context Protocol]]"
  - "[[Writing Effective Tools for Agents]]"
  - "[[Claude Code Subagents]]"
  - "[[Context Window Management]]"
  - "[[Claude Code Hooks]]"
source_urls:
  - "https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/skills (retrieved 2026-07-07)"
  - "https://agentskills.io/home (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/plugins (retrieved 2026-07-07)"
---

# Agent Skills System

A skill is a folder with a SKILL.md entrypoint that loads through progressive disclosure, costing about 100 tokens until a matching task pulls in its full body.

## What it is

Skills package procedural knowledge for agents. The platform docs define the shape: "Every Skill requires a `SKILL.md` file with YAML frontmatter" (https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview). Required fields: `name` (max 64 characters; lowercase letters, numbers, and hyphens; the reserved words "anthropic" and "claude" are barred) and `description` (non-empty, max 1024 characters, stating what the skill does and when to use it).

The format, originally developed by Anthropic, is an open standard at agentskills.io adopted by Cursor, GitHub Copilot, VS Code, Gemini CLI, OpenAI Codex, OpenCode, Goose, and Amp. Claude Code follows the standard and extends it with invocation control, subagent execution, and dynamic context injection.

## How it works

- Progressive disclosure has three levels: frontmatter metadata (about 100 tokens per skill) always sits in the system prompt; the SKILL.md body (under 5k tokens) loads only when the task matches the description; bundled files and scripts load or execute only as needed. "Progressive disclosure ensures only relevant content occupies the context window at any given time" (https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).
- Skills versus slash commands: in Claude Code, "Custom commands have been merged into skills" (https://code.claude.com/docs/en/skills). A file at .claude/commands/deploy.md and a skill at .claude/skills/deploy/SKILL.md both create /deploy; skills add supporting-file directories, `disable-model-invocation` frontmatter, `$ARGUMENTS`, and dynamic context injection.
- Skills versus plugins: a plugin is a distribution wrapper that can bundle skills, commands, agents, hooks (hooks/hooks.json), MCP servers (.mcp.json), LSP servers (.lsp.json), monitors, bin/ executables, and default settings; only plugin.json sits inside .claude-plugin/. Plugins launched in public beta on 2025-10-09; a marketplace is any git repo or URL with .claude-plugin/marketplace.json.
- Load levels in Claude Code: enterprise (managed settings), personal (~/.claude/skills/), project (.claude/skills/), and plugins (namespaced plugin-name:skill-name). On name collisions, "enterprise overrides personal, and personal overrides project" (https://code.claude.com/docs/en/skills). Nested .claude/skills/ directories load on demand for monorepos.
- Skills and MCP are complementary: MCP connects agents to external tools and data, skills encode the procedural knowledge that uses them, and Anthropic's code-execution pattern turns saved functions plus a SKILL.md into a structured skill (https://www.anthropic.com/engineering/code-execution-with-mcp).

> [!key-insight] The whole system is a context ledger: about 100 tokens buys a skill's permanent listing, and everything else pays only on use. Description quality is therefore the entire discovery mechanism.

## Best practice

- Write descriptions that state both what the skill does and when to use it, since discovery runs on that text alone. EVIDENCE-BASED
- Put every-session facts in CLAUDE.md and multi-step procedures in skills, because a skill body costs nothing until used. EVIDENCE-BASED
- Start with standalone .claude/ configuration; convert to a plugin only when you need sharing, versioned releases, reuse, or marketplace distribution. EVIDENCE-BASED
- Treat skill installation like installing software: use trusted sources and audit every bundled file before use. EVIDENCE-BASED
- Treat skills that fetch external URLs as high risk, since fetched content can smuggle malicious instructions. EVIDENCE-BASED
- Prefer Anthropic's marketplaces: claude-plugins-official is curated, and claude-community entries are reviewed, safety-screened, and pinned to a commit SHA. EVIDENCE-BASED
- Keep SKILL.md bodies under 5k tokens and push reference material into bundled files that load only as needed. EVIDENCE-BASED
- Set disable-model-invocation when a skill must run only on explicit /command invocation, never autonomously. EVIDENCE-BASED

## Pitfalls

- Vague descriptions make a skill invisible; the model never loads a body whose trigger text does not match the task.
- Overlong bodies defeat the design; the body budget is under 5k tokens, with bulk material pushed to bundled files.
- Name collisions resolve by precedence, so an enterprise skill can silently shadow a project one.
- Unaudited third-party skills execute with your permissions; the official guidance is "Use Skills only from trusted sources: those you created yourself or obtained from Anthropic" (https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).
- Converting to a plugin costs namespacing: /deploy becomes plugin-name:deploy.
- Any git repo can serve as a marketplace via .claude-plugin/marketplace.json, so /plugin marketplace add is an act of trust, not a vetting step.

## Sources

- Agent Skills overview, Claude Platform docs, https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview (retrieved 2026-07-07).
- Extend Claude with skills, official docs, https://code.claude.com/docs/en/skills (retrieved 2026-07-07).
- Agent Skills open standard, https://agentskills.io/home (retrieved 2026-07-07).
- Equipping agents for the real world with Agent Skills, Anthropic Engineering, https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (published 2025-10-16, retrieved 2026-07-07).
- Create plugins, Claude Code docs, https://code.claude.com/docs/en/plugins (retrieved 2026-07-07).
- Customize Claude Code with plugins, Claude blog, https://claude.com/blog/claude-code-plugins (published 2025-10-09, retrieved 2026-07-07).
- Code execution with MCP, Anthropic Engineering, https://www.anthropic.com/engineering/code-execution-with-mcp (published 2025-11-04, retrieved 2026-07-07).

## Related

- [[Claude Code]] implements the standard plus invocation control and namespacing.
- [[Tool Search and Deferred Tools]] applies the same context-economy logic to tool schemas.
- [[Claude Code Project Memory]] holds always-loaded facts; skills hold on-demand procedures.
- [[Model Context Protocol]] connects tools and data; skills encode the workflows that use them.
- [[Writing Effective Tools for Agents]] shares the description-quality discipline.
- [[Claude Code Subagents]] can execute skills in isolated contexts.
- [[Context Window Management]] quantifies why the 100-token metadata design matters.
- [[Claude Code Hooks]] ship inside plugins alongside skills for enforced behavior.
- [[Connector and MCP App Suggestions]] covers the claude.ai side of extension discovery.

## Next actions

- Audit installed third-party skills and remove any with unreviewed bundled scripts.
- Rewrite the weakest skill description to state what it does and when to use it.
- Identify one .claude/ setup worth converting to a plugin for reuse across repos.
- Check name collisions across enterprise, personal, and project skill levels.

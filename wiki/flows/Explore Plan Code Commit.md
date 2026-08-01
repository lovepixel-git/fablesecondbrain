---
type: flow
title: "Explore Plan Code Commit"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/best-practices
  - note/flow
domain: best-practices
confidence: evidence-based
approval_status: approved
risk_level: low
rollback_note: "Explore and plan stages mutate nothing; implementation edits revert with git checkout or git revert of the flow's commits."
related:
  - "[[Plan Mode and Permission Modes]]"
  - "[[Claude Code]]"
  - "[[Claude Code Platform]]"
  - "[[Claude Code Project Memory]]"
  - "[[Claude Code Hooks]]"
  - "[[Claude Code Subagents]]"
  - "[[Context Window Management]]"
  - "[[Claim Verification Flow]]"
  - "[[Fable 5 Best Practices Cheat Sheet]]"
  - "[[Claude Code Quickstart for Fable 5]]"
source_urls:
  - "https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/permission-modes (retrieved 2026-07-07)"
---

# Explore Plan Code Commit

Explore Plan Code Commit is the officially recommended Claude Code loop: research in read-only plan mode, approve a written plan, implement against a runnable check, then commit, and skip the plan stage entirely for one-sentence diffs.

## What it is

The canonical agentic coding workflow from Anthropic's Claude Code best practices. The original engineering post at anthropic.com/engineering/claude-code-best-practices now 308-redirects to code.claude.com/docs/en/best-practices, which is the current official guide. The workflow's four stages separate context gathering from mutation so the model reads before it writes and verifies before it ships.

## How it works

1. **Explore.** Enter plan mode (Shift+Tab, a /plan prompt prefix, or `claude --permission-mode plan`). Plan mode is read-only: "Plan mode tells Claude to research and propose changes without making them." (https://code.claude.com/docs/en/permission-modes). Delegate scoped investigation to subagents so research does not consume the main context window.
2. **Plan.** Claude proposes a plan. Ctrl+G opens it in a text editor for direct edits before proceeding. Approving the plan switches the session into the chosen execution mode.
3. **Code.** Implement against a verifiable check. The docs' top practice: "Give Claude a check it can run: tests, a build, a screenshot to compare." (https://code.claude.com/docs/en/best-practices). Checks can gate harder via /goal conditions, Stop hooks, or a fresh-context verification subagent.
4. **Commit.** Land the change once the check passes, keeping git history descriptive so later sessions can reconstruct intent.

The docs also carve out the fast path: "If you could describe the diff in one sentence, skip the plan." (https://code.claude.com/docs/en/best-practices).

> [!key-insight]
> Each stage carries a different permission posture. Explore runs read-only, implementation runs in the chosen execution mode, and the six permission modes (default Manual, acceptEdits, plan, auto, dontAsk, bypassPermissions) are cycled with Shift+Tab or set via --permission-mode and the defaultMode setting. The loop is a permissions choreography as much as a prompting pattern.

## Best practice

- Give Claude a check it can run (tests, build exit code, linter, screenshot comparison) so it iterates until the check passes instead of using you as the verification loop. EVIDENCE-BASED
- Use plan mode for anything non-trivial; approving the plan switches into the chosen execution mode, so the mode transition is explicit, not accidental. EVIDENCE-BASED
- Skip planning overhead for small, clearly scoped fixes describable in one sentence. EVIDENCE-BASED
- Edit the plan directly with Ctrl+G before approving rather than steering with follow-up prompts. EVIDENCE-BASED
- Run /clear between unrelated tasks so stale exploration does not pollute the next loop. EVIDENCE-BASED
- After roughly two failed corrections on the same issue, restart: "A clean session with a better prompt almost always outperforms a long session" (https://code.claude.com/docs/en/best-practices). EVIDENCE-BASED
- Enforce mandatory rules with hooks and permission rules, not CLAUDE.md prose; keep CLAUDE.md short and ruthlessly pruned. PRACTITIONER
- Gate completion deterministically: Stop hooks or a fresh-context verification subagent catch premature "done" claims. EVIDENCE-BASED
- Set the project's defaultMode in settings so every session starts in the intended stage posture instead of relying on manual Shift+Tab discipline. EVIDENCE-BASED
- In the VS Code extension, review the plan and the inline diffs in the editor; plan review and checkpoints are built into the recommended IDE integration. EVIDENCE-BASED

## Pitfalls

- Relying on the human as the verification loop; without a runnable check Claude cannot close its own loop.
- Bloated project memory: "Bloated CLAUDE.md files cause Claude to ignore your actual instructions!" (https://code.claude.com/docs/en/best-practices).
- Applying full planning ceremony to one-line fixes; the docs explicitly say to skip it.
- Writing a policy hook that exits 1: "Exit 1 does not block anything." (https://blakecrosley.com/blog/claude-code-hooks-explained). Blocking hooks must exit 2.
- Grinding through a long correction session instead of restarting with a better prompt.
- Confusing plan-mode approval with permission approval; the approval also selects the execution mode for the rest of the session.

## Sources

- Best practices for Claude Code, official docs: https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)
- Choose a permission mode, official docs: https://code.claude.com/docs/en/permission-modes (retrieved 2026-07-07)
- Claude Code Hooks Explained, Blake Crosley: https://blakecrosley.com/blog/claude-code-hooks-explained (published 2026-07-01, retrieved 2026-07-07)
- Claude Code Advanced Best Practices, SmartScope: https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026 (published 2026-07-06, retrieved 2026-07-07)

## Related

- [[Plan Mode and Permission Modes]] because the explore stage runs entirely inside plan mode semantics.
- [[Claude Code]] because this is the harness the flow operates.
- [[Claude Code Platform]] because surface differences (CLI, IDE, web) change how you enter plan mode.
- [[Claude Code Project Memory]] because a short, pruned CLAUDE.md is the flow's persistent context layer.
- [[Claude Code Hooks]] because Stop and PreToolUse hooks make the verify step deterministic.
- [[Claude Code Subagents]] because scoped exploration and fresh-context verification belong in subagents.
- [[Context Window Management]] because /clear boundaries and restart discipline are context economics.
- [[Claim Verification Flow]] because both flows share the second-check-before-ship principle.
- [[Fable 5 Best Practices Cheat Sheet]] because the cheat sheet compresses this loop for daily use.
- [[Claude Code Quickstart for Fable 5]] because the quickstart walks a first run of this exact loop.

## Next actions

- Wire a Stop hook that runs the project test suite so the commit stage cannot fire on red.
- Compare plan quality with and without a prior subagent exploration pass on one real task.
- Add a repo checklist linking each stage to its permission mode and hook events.

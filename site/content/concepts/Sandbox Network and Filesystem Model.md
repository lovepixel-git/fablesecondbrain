---
type: concept
title: "Sandbox Network and Filesystem Model"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/safety
  - note/concept
domain: safety-and-permissions
confidence: evidence-based
related:
  - "[[Computer Use File Handling Rules]]"
  - "[[Claude Code]]"
  - "[[Claude Code Settings and Permissions]]"
  - "[[Plan Mode and Permission Modes]]"
  - "[[Export Chapter Computer Use and Search]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Memory Injection Resistance]]"
  - "[[claude.ai Platform]]"
  - "[[Anthropic Engineering Blog Shelf]]"
source_urls:
  - "https://code.claude.com/docs/en/sandboxing (retrieved 2026-07-07)"
  - "https://www.anthropic.com/engineering/claude-code-sandboxing (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/security (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Sandbox Network and Filesystem Model

Claude's execution sandboxes differ sharply by surface: the claude.ai container gives Fable 5 a three-directory filesystem with wildcard network egress, while Claude Code enforces OS-level isolation (Seatbelt, bubblewrap) behind a permission system that is read-only by default.

## What it is

- The combined filesystem and network isolation model around Claude's code execution, captured for claude.ai in the system prompt export and for Claude Code in public docs.
- On claude.ai, a per-session Linux container: uploads at /mnt/user-data/uploads, scratch work in a hidden container directory, and deliverables at /mnt/user-data/outputs, "the only way users see files" (System Prompt Export 2026-07, L1074-1089).
- On Claude Code, a sandboxed Bash tool with filesystem and network isolation enforced at the OS level: Seatbelt on macOS, bubblewrap on Linux and WSL2; restrictions apply to all child processes and native Windows is not supported (https://code.claude.com/docs/en/sandboxing, retrieved 2026-07-07).

## How it works

- claude.ai filesystem: five directories mount read-only (/mnt/user-data/uploads, /mnt/transcripts, and the three /mnt/skills trees); everything else Claude writes lives in a hidden scratch directory until copied to outputs (System Prompt Export 2026-07, L3795-3816, L1074-1089).
- claude.ai network: bash_tool egress is enabled with a wildcard domain allowlist, "Allowed Domains: *" (System Prompt Export 2026-07, L3795-3816).
- Claude Code baseline: strict read-only permissions by default; editing files and running system-modifying Bash commands require explicit approval, and write access is confined to the working directory and its subfolders (https://code.claude.com/docs/en/security, retrieved 2026-07-07).
- Claude Code protected paths: in every permission mode except bypassPermissions, writes to .git, .claude, shell rc files, and .mcp.json are never auto-approved, and allow rules cannot pre-approve them (https://code.claude.com/docs/en/permission-modes, retrieved 2026-07-07).
- Escape hatch economics: Anthropic reports "sandboxing safely reduces permission prompts by 84%" in internal testing, and the primitives are open source as the sandbox-runtime research preview (https://www.anthropic.com/engineering/claude-code-sandboxing, published 2025-10-20).
- Network caveat: the built-in Claude Code proxy allows domains by client-supplied hostname without inspecting TLS by default, so broad allowlists like github.com can enable exfiltration via domain fronting; "Effective sandboxing requires both filesystem and network isolation." (https://code.claude.com/docs/en/sandboxing, retrieved 2026-07-07).
- Injection defenses ride on the same rails: network commands like curl and wget are not auto-approved, web fetch runs in isolated context windows, and command injection detection flags suspicious Bash (https://code.claude.com/docs/en/security, retrieved 2026-07-07).

> [!contradiction]
> The claude.ai container ships wildcard network egress while Claude Code guidance warns that broad allowlists enable exfiltration. These are different surfaces with different threat models (claude.ai adds server-side controls the export does not describe), but the tension is real and unresolved by public docs.

## Best practice

- On claude.ai computer use, deliver every user-facing file to /mnt/user-data/outputs; work left in the hidden scratch directory is invisible to the user. EVIDENCE-BASED
- Treat the read-only mounts as immutable inputs: read uploads and skills in place, copy into the hidden scratch directory before modifying. EVIDENCE-BASED
- On Claude Code, keep sandboxing on and narrow the network allowlist to named hosts you actually need; wildcard or broad-domain entries defeat the isolation. EVIDENCE-BASED
- Reserve bypassPermissions for disposable containers and VMs; it disables prompts and safety checks and refuses to start as root. EVIDENCE-BASED
- Assume anything fetched over the wildcard claude.ai egress is untrusted input and cross-check it before it drives actions. PRACTITIONER
- For organizations, block bypass mode fleet-wide via permissions.disableBypassPermissionsMode in managed settings. EVIDENCE-BASED

## Pitfalls

- Expecting claude.ai isolation guarantees to match Claude Code: the export documents layout and egress, not enforcement internals.
- Reading "sandboxed" as "safe to run hostile code": Anthropic frames sandboxing as defense in depth, not a complete isolation boundary.
- Allowlisting large multi-tenant domains (github.com and similar) and assuming egress is contained; domain fronting rides through by hostname.
- Forgetting child processes inherit Claude Code sandbox restrictions, then misreading their failures as tool bugs.
- Relying on native Windows sandboxing; it does not exist, only WSL2 is supported.
- Citing the claude.ai container layout as current without re-verification; it is a 2026-06-09 capture.

## Sources

- System Prompt Export 2026-07, L1074-1089, L3795-3816 (claims extracted 2026-07-07)
- Claude Code Docs, Configure the sandboxed Bash tool, https://code.claude.com/docs/en/sandboxing (retrieved 2026-07-07)
- Claude Code Docs, Security, https://code.claude.com/docs/en/security (retrieved 2026-07-07)
- Claude Code Docs, Choose a permission mode, https://code.claude.com/docs/en/permission-modes (retrieved 2026-07-07)
- Anthropic Engineering, Making Claude Code more secure and autonomous with sandboxing, https://www.anthropic.com/engineering/claude-code-sandboxing (published 2025-10-20, retrieved 2026-07-07)

## Related

- [[Computer Use File Handling Rules]] operationalizes the three-directory scheme this note grounds.
- [[Claude Code]] is the harness whose sandbox enforces OS-level isolation.
- [[Claude Code Settings and Permissions]] is where allowlists and sandbox settings are configured.
- [[Plan Mode and Permission Modes]] defines the six modes the sandbox interacts with, including bypassPermissions.
- [[Export Chapter Computer Use and Search]] holds the corpus extract for the claude.ai container.
- [[Fable 5 Dual-Use Safety Measures]] is the model-side layer above this execution-side layer.
- [[Memory Injection Resistance]] covers the memory-side defenses against the same injected-content threat.
- [[claude.ai Platform]] is the surface running the wildcard-egress container.
- [[Anthropic Engineering Blog Shelf]] shelves the sandboxing engineering post cited here.

## Next actions

- Re-verify the wildcard "Allowed Domains: *" line against a fresh claude.ai capture before relying on it.
- Test whether the sandbox-runtime research preview fits this vault's local agent experiments.
- Draft a minimal Claude Code network allowlist for this project and measure the prompt-reduction effect.

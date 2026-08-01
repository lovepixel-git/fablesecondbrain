---
type: concept
title: "Tone and Formatting Rules"
status: mature
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/communication
  - note/concept
domain: communication-rules
confidence: evidence-based
related:
  - "[[Citation Discipline]]"
  - "[[Copyright Compliance Rules]]"
  - "[[Prompting Fable 5 One-Pager]]"
  - "[[Prompt Engineering Workflow for Fable 5]]"
  - "[[Artifacts Usage Criteria]]"
  - "[[Visualizer Decision Ladder]]"
  - "[[Export Chapter Product and Behavior]]"
  - "[[Claude Memory System]]"
  - "[[Claude Fable 5]]"
  - "[[User Preferences System]]"
source_urls:
  - "https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07)"
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Tone and Formatting Rules

The claude.ai system prompt gives Fable 5 a warm, prose-first voice with minimum formatting by default, then layers channel precedence on top: user styles outrank user preferences, preferences apply by default only with "always" wording, lists never become artifacts, and routing is never narrated.

## What it is

- The communication layer of the claude.ai harness for [[Claude Fable 5]]: the default tone rules (tone_and_formatting, System Prompt Export 2026-07, L80-92), the formatting rules (lists_and_bullets, L94-104), and the channels through which instructions about voice and layout actually bind.
- Relevant to prompting because these rules decide what the model sounds like with no instructions at all, and which channel (message, preference, or style) overrides the defaults most reliably.
- Bound to the consumer surface: the export captures claude.ai on Fable 5, deployed for Pro, Max, Team, and Enterprise users (https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5, retrieved 2026-07-07).

## How it works

### Default tone (L80-92)

- Warmth as baseline: "Claude uses a warm tone, treating people with kindness" and without negative assumptions about judgement or abilities; pushback stays constructive, with empathy and the person's best interests in mind (System Prompt Export 2026-07, L82).
- Explanations may use examples, thought experiments, or metaphors (L84); cursing is off unless the person asks or curses a lot themselves, and even then sparing (L86).
- Question discipline: Claude "avoids more than one per response" and tries to address even an ambiguous query before asking for clarification (System Prompt Export 2026-07, L88).
- Audience calibration: a suspected minor gets a friendly, age-appropriate conversation; otherwise the person is assumed to be a capable adult and treated as one (L90).
- Evidence hygiene in tone: a prompt implying a file is present does not mean one is; Claude checks for itself (L92).

### Lists and bullets (L94-104)

- Minimum formatting law: Claude avoids over-formatting with bold, headers, lists, and bullets, "using the minimum formatting needed for clarity"; lists and bullets appear only when asked or when content is multifaceted enough that they are essential, and bullets run at least 1-2 sentences (System Prompt Export 2026-07, L96).
- Prose is the default register: typical conversation and simple questions get natural prose, and casual responses can be short (L98).
- Reports, documents, technical documentation, and explanations are written as prose without bullets, numbered lists, or excessive bolding; inline enumerations read naturally as "some things include: x, y, and z" (L100).
- Declining softly: Claude "never uses bullet points when declining a task"; the additional care softens the blow (System Prompt Export 2026-07, L102).

### Channel precedence and routing

- Preference gating: "Preferences should not be applied by default unless the instruction states 'always'" (System Prompt Export 2026-07, L846-873); behavioral preferences otherwise need direct task relevance, and contextual preferences need explicit invocation. Detail in [[User Preferences System]].
- Precedence: when a userStyle and a userPreference conflict, userStyle wins (System Prompt Export 2026-07, L846-873).
- Format routing: lists, tables, and enumerated content never become artifacts regardless of length, while code over 20 lines and standalone text-heavy documents over 20 lines or 1500 characters do (System Prompt Export 2026-07, L1117-1140).
- Silent routing: visual output follows a fixed checklist (prose, then MCP tool, then file tools, then Visualizer) and the routing decision is never narrated to the user (System Prompt Export 2026-07, L1198-1222).
- Phrasing bans as tone control: for memory, "Claude NEVER uses observation verbs suggesting data retrieval" (System Prompt Export 2026-07, L251-276), showing the harness legislates wording down to verb choice.
- Enforcement backstop: classifier-triggered runtime reminders (including long_conversation_reminder) can re-tighten behavior mid-session and never reduce restrictions (System Prompt Export 2026-07, L144-152); see [[Anthropic Runtime Reminders]].

> [!key-insight]
> Tone flows through three channels with fixed precedence: per-message instructions steer the current task, userPreferences apply only when "always"-worded or task-relevant, and userStyle overrides userPreferences on conflict. Prompting that ignores the channel hierarchy produces intermittent, hard-to-debug voice drift.

## Best practice

- Expect prose by default; if you want bullets, tables, or headers on claude.ai, ask for them, because the harness treats formatting as opt-in. EVIDENCE-BASED
- Ask at most one thing per turn when mirroring the harness style; the model itself is bound to one question per response. EVIDENCE-BASED
- Put persistent voice requirements into a style rather than a preference; on conflict the style wins. EVIDENCE-BASED
- Phrase preferences you want applied everywhere with explicit "always" wording; otherwise they gate on task relevance. EVIDENCE-BASED
- Do not ask claude.ai to deliver lists or tables "as an artifact"; the harness excludes them from artifacts regardless of length. EVIDENCE-BASED
- Do not rely on Claude explaining why it chose prose, a tool, or the Visualizer; routing is deliberately unnarrated, so ask for the output form you want directly. EVIDENCE-BASED
- When per-message tone instructions fight harness defaults, repeat them near the task rather than once at session start; runtime reminders can re-tighten defaults mid-session. PRACTITIONER
- In this vault, follow the CONVENTIONS style law regardless of model defaults: declarative present tense and no em dashes. EVIDENCE-BASED

## Pitfalls

- Assuming preferences are always-on: without "always" wording, a stored preference silently fails to apply to most tasks.
- Fighting the artifact threshold by asking for a 25-line list as an artifact; the list exclusion beats the length trigger.
- Reading the absence of routing narration as indecision; the checklist ran, it is just not reported.
- Expecting heavily formatted reports by default; the export bans bullets and numbered lists in report prose unless asked (L100).
- Generalizing these rules to the API or Claude Code; they are claude.ai harness rules from the 2026-06-09 capture.

## Sources

- System Prompt Export 2026-07, L80-104 (tone_and_formatting and lists_and_bullets, extracted 2026-07-07)
- System Prompt Export 2026-07, L846-873, L1117-1140, L1198-1222, L251-276, L144-152 (channel and routing claims, extracted 2026-07-07)
- Claude Platform Docs, Introducing Claude Fable 5 and Claude Mythos 5, https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07), surface context only
- Vault law: wiki/meta/CONVENTIONS.md, style and body contract (dated 2026-07-07)

- Anthropic release notes, system prompts: the claude_behavior core containing this section is officially published, dated 2026-06-09, https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07)

## Related

- [[Citation Discipline]] governs how claims inside the formatted output are attributed.
- [[Copyright Compliance Rules]] caps quotation inside any tone or format.
- [[Prompting Fable 5 One-Pager]] compresses these rules into prompt guidance.
- [[Prompt Engineering Workflow for Fable 5]] is where style-versus-preference choices get engineered.
- [[Artifacts Usage Criteria]] holds the full artifact thresholds these formatting rules feed.
- [[Visualizer Decision Ladder]] details the silent visual-output routing checklist.
- [[Export Chapter Product and Behavior]] is the corpus chapter these tone sections live in.
- [[Claude Memory System]] shows the same phrasing-level control applied to memory language.
- [[Claude Fable 5]] is the model whose consumer voice these rules define.
- [[User Preferences System]] expands the preference-gating half of the channel hierarchy.
- [[User Wellbeing Rules]] covers the empathy side of the same behavioral layer.

## Next actions

- Test the style-beats-preference precedence with a live claude.ai probe and log the result.
- Compare a fresh capture against L80-104 and L846-873 to confirm the tone defaults and "always" gating survived past 2026-06-09.
- Log one claude.ai probe of the list-exclusion rule: request a 30-line list as an artifact and record what happens.

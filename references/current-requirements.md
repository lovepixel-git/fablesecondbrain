# Current Requirements

Status: researched 2026-07-07 from official Anthropic sources; adversarially verified (see claim-ledger.md).

## Refresh Cadence

30 days for official Anthropic docs and news; 90 days for practitioner sources; on-change for system prompt exports. Ledger enforcement via refresh_due in source-ledger.json.

## Required Source Standard

Use official, primary, vendor, standards-body, regulator, or API documentation
first. Record URL, retrieval date, version, deprecation or sunset notes, and
confidence.

## Source Log

| Source | URL | Retrieved | Version | Confidence | Notes |
|---|---|---:|---|---|---|
| Claude Fable 5 and Claude Mythos 5 announcement | https://www.anthropic.com/news/claude-fable-5-mythos-5 | 2026-07-07 | published 2026-06-09 | high | Launch facts, pricing, safety classifiers, Opus 4.8 fallback |
| Introducing Fable 5 and Mythos 5 (docs) | https://docs.claude.com/en/docs/about-claude/models/introducing-fable-mythos | 2026-07-07 | current | high | 1M context, 128k output, adaptive thinking always on, Covered Model retention |
| Models overview (docs) | https://docs.claude.com/en/docs/about-claude/models/overview | 2026-07-07 | current | high | Model IDs claude-fable-5, claude-opus-4-8, claude-sonnet-5, claude-haiku-4-5-20251001; pricing table |
| Refusals and fallback (docs) | https://docs.claude.com/en/docs/build-with-claude/refusals-fallback | 2026-07-07 | current | high | stop_reason refusal, categories cyber, bio, frontier_llm, reasoning_extraction |
| Redeploying Fable 5 (news) | https://www.anthropic.com/news/redeploying-fable-5 | 2026-07-07 | published 2026-06-30 | high | Export control suspension June 12 lifted; restoration July 1 |
| Fable and Mythos 5 system card | https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf | 2026-07-07 | published 2026-06-09 | high | Public safety, cyber, CBRN, prompt-injection, and safeguard evaluation evidence |
| Claude Mythos product page | https://www.anthropic.com/claude/mythos | 2026-07-07 | current | high | Current trusted-partner positioning, July 1 US restoration note, price and retention |
| Project Glasswing expansion | https://www.anthropic.com/news/expanding-project-glasswing | 2026-07-07 | published 2026-06-02 | high | About 150 additional organizations across more than 15 countries |
| Project Glasswing initial update | https://www.anthropic.com/research/glasswing-initial-update | 2026-07-07 | published 2026-05-22 | high | More than 10,000 high or critical vulnerabilities; remediation bottleneck |
| Anthropic CVD dashboard | https://red.anthropic.com/2026/cvd/ | 2026-07-07 | published 2026-05-22 | high | 1,596 disclosed vulnerabilities, 281 projects, 97 patched, 88 advisories |
| System prompt export metadata (corpus) | Raw capture omitted from public release | 2026-07-07 | sha256 prefix 48358a42 | high | claude.ai harness capture metadata, 3826 lines, immutable in the private vault |

Full ledger: references/source-ledger.json (96 sources, 81 official, primary, vendor, authority, or API-doc sources). Deprecation watch: dateless model IDs from the 4.6 generation onward are pinned snapshots; Mythos Preview superseded by Mythos 5.

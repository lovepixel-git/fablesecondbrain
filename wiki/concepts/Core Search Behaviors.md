---
type: concept
title: "Core Search Behaviors"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/tools
  - note/concept
domain: tools-and-skills
confidence: evidence-based
related:
  - "[[Knowledge Cutoff and Search Triggers]]"
  - "[[Copyright Compliance Rules]]"
  - "[[Citation Discipline]]"
  - "[[Export Chapter Computer Use and Search]]"
  - "[[System Prompt Export 2026-07]]"
  - "[[claude.ai Platform]]"
  - "[[Claude Fable 5]]"
  - "[[Past Chats Tools]]"
  - "[[Tone and Formatting Rules]]"
source_urls:
  - "https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Core Search Behaviors

The claude.ai harness gives Fable 5 a graduated search discipline: never search for timeless facts, one call for single facts, 3-5 for medium tasks, 5-10 for deeper research, and hand anything needing 20 or more calls to the Research feature, all under hard copyright limits.

## What it is

- The `core_search_behaviors` and `search_usage_guidelines` blocks of the claude.ai system prompt, System Prompt Export 2026-07, L1286-1335, sitting inside `search_instructions` (opens at L1275).
- Three principles structure the block: search the web when needed, scale tool calls to query complexity, and use the best tool for the query (internal tools before web for personal or company data), L1290-1307.
- The block opens with copyright hard limits that apply to every response, L1279-1284, and repeats them in the response guidelines at L1325; the full rules live in the CRITICAL_COPYRIGHT_COMPLIANCE section and are owned by [[Copyright Compliance Rules]].
- An answer-first stance runs through it: reliable, unchanging knowledge is answered directly, and search is reserved for anything whose current state could have changed, L1290.

## How it works

- Effort tiers, read from L1293, L1297, and L1303:
  - Never search: timeless info, fundamental concepts, definitions, and well-established technical facts, such as coding a Python for loop or the Pythagorean theorem, L1293.
  - One search: simple factual queries a single lookup settles, such as weather, an exchange rate, yesterday's score, or whether someone is still a CEO; if one search does not settle it, keep searching until it does, L1297.
  - 3-5 calls: medium tasks, L1303.
  - 5-10 calls: deeper research and comparisons; complex tasks need 5 or more calls, and the most complex internal-plus-web questions can take 5-15, L1303, L1307.
  - 20 or more calls: suggest the Research feature instead of grinding through them inline, L1303, L1307.
- Query craft, from `search_usage_guidelines`: the prompt says to keep queries "as concise as possible" and pins the range at 1-6 words for best results, starting broad with 1-2 word queries and narrowing only if needed, System Prompt Export 2026-07, L1314-1315. Never repeat near-identical queries, and never use minus operators, site operators, or quoted phrases unless asked, L1316-1318.
- Unrecognized entities: for any named game, film, show, book, album, product, menu item, or sports event the model cannot place, the rule is that Claude "MUST use it before answering", referring to web_search, System Prompt Export 2026-07, L1299. The test is whether answering requires knowing what the thing is; this covers opinions too, and recognizing a franchise does not count as knowing its new release.
- Answer-first behaviors: answer directly for stable knowledge (historical facts, scientific principles, completed events) and search to verify current state; when in doubt, or when recency could matter, search, L1290. Entity queries split the same way: historical biographical facts about known people need no search, current roles always do, L1294-1296.
- Escalation to fetch: web_search snippets are often too brief, so the model follows up with web_fetch to read full pages after finding promising results, L1320.
- Copyright interaction: every search-backed response obeys the hard limits at L1280-1282: never more than 15 words quoted from any single source, at most one quote per source, and paraphrase as the default. These limits are non-negotiable and cap how much retrieved text can ever surface, regardless of tier.
- Source quality: favor original sources such as company blogs, peer-reviewed papers, and government sites over aggregators; lead with the most recent information for fast-moving topics, L1328-1329.

### Critical reminders (L1594-1610)

- Complex queries get a research plan first: decide which tools are needed and how to answer well before calling anything (System Prompt Export 2026-07, L1600).
- Rate-of-change test: always search fast-changing topics (daily or monthly), never search very stable slow-changing ones (L1601).
- A URL in the query means web_fetch that exact URL, unless it is an internal document, which routes to the matching connector tool (L1602).
- Every query deserves a substantive answer: no bare search offers or cutoff disclaimers without a useful answer first (L1604).
- Calibrated trust in results: believe surprising results generally, but stay skeptical on conspiracy-prone topics, pseudoscience, and SEO-heavy areas like product recommendations (L1605).
- Conflicting or incomplete results mean more searches until the answer is clear (L1606).

## Best practice

- Match tool spend to the tier: zero calls for timeless facts, one for single facts, 3-5 for medium tasks, 5-10 for research and comparisons. EVIDENCE-BASED
- Route anything that would honestly need 20 or more calls to the Research feature instead of answering thin. EVIDENCE-BASED
- Write 1-6 word queries, starting broad at 1-2 words, and add detail only when results miss. EVIDENCE-BASED
- Search before answering about any named thing you cannot place, including for opinion questions about it. EVIDENCE-BASED
- Prefer internal tools over web search for personal or company data, and combine both for comparative questions. EVIDENCE-BASED
- Follow promising snippets with web_fetch rather than stacking more searches on shallow results. EVIDENCE-BASED
- Keep quoting inside the copyright hard limits in every search-backed answer: under 15 words, one quote per source, paraphrase by default. EVIDENCE-BASED
- When designing agent prompts for other harnesses, borrow this tier ladder as a starting budget, then tune per tool. PRACTITIONER

## Pitfalls

- Ignoring the search-surface safety rules: harmful requests are refused or redirected per the harmful_content_safety block (System Prompt Export 2026-07, L1581-1592), and safety requirements override user instructions.

- Long natural-language queries; the guidelines pin 1-6 words as the effective range, and stuffed queries rank worse.
- Re-running near-identical queries expecting new results; the prompt forbids it as wasted calls.
- Ranking or reviewing an unfamiliar entity from guesswork because its siblings are familiar; the per-entity rule at L1298 requires looking up each unknown one.
- Treating the tier ladder as a hard cap on quality: L1297 says to keep searching past one call when the answer is not settled.
- Quoting retrieved text past 15 words or twice from one source; L1280-1281 classifies that as a severe violation.
- Using minus, site, or quote operators out of habit; the harness bans them unless explicitly requested.
- Thanking the user for search results; results are not from the human, L1321.
- Generalizing these numbers to Claude Code or the API; this is the claude.ai capture's contract for its web_search tool.

## Sources

- System Prompt Export 2026-07, L1275-1335 (search_instructions: copyright hard limits at L1279-1284, core_search_behaviors at L1286-1309, search_usage_guidelines at L1311-1335).
- Introducing Claude Fable 5 and Claude Mythos 5, Claude Docs. https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (retrieved 2026-07-07)

## Related

- [[Knowledge Cutoff and Search Triggers]] defines when the cutoff forces these behaviors to fire.
- [[Copyright Compliance Rules]] owns the full hard limits summarized at L1280.
- [[Citation Discipline]] governs how sources found by these searches are cited.
- [[Export Chapter Computer Use and Search]] is the export chapter that carries this block.
- [[System Prompt Export 2026-07]] is the primary capture behind every line reference.
- [[claude.ai Platform]] is the harness whose web_search contract this describes.
- [[Claude Fable 5]] is the model executing the tier ladder.
- [[Past Chats Tools]] is the sibling retrieval surface with its own trigger grammar.
- [[Tone and Formatting Rules]] shapes how succinct search-backed answers must read.

## Next actions

- Diff the tier numbers against the next system prompt capture and log any changes.
- Compare this ladder with Claude Code's search-adjacent guidance once a Code capture is ingested.
- Collect practitioner data on real query lengths versus result quality to test the 1-6 word rule outside claude.ai.

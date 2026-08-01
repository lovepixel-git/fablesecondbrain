---
type: concept
title: "Image Search Decision Rules"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/tools
  - note/concept
domain: tools-and-skills
confidence: evidence-based
related:
  - "[[Claude Fable 5]]"
  - "[[System Prompt Export 2026-07]]"
  - "[[Core Search Behaviors]]"
  - "[[Knowledge Cutoff and Search Triggers]]"
  - "[[Copyright Compliance Rules]]"
  - "[[Visualizer Decision Ladder]]"
  - "[[Artifacts Usage Criteria]]"
  - "[[Export Chapter Computer Use and Search]]"
  - "[[claude.ai Platform]]"
  - "[[Public System Prompt Copies]]"
source_urls:
  - "https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Image Search Decision Rules

The claude.ai image search tool is governed by one enhance-understanding test, an explicit skip-list for text-shaped work, a lead-versus-interleave placement rule, and a hard 3 to 4 image budget per call (System Prompt Export 2026-07, L1614-1688).

## What it is

The `<using_image_search_tool>` block of the claude.ai system prompt (L1614-1688) defines when Fable 5 on claude.ai searches the web for images, how it phrases image queries, how many images it returns, and where those images land in the reply. The tool "takes a query, finds images on the web and returns them" with dimensions (System Prompt Export 2026-07, L1616). It sits alongside, and defers to, the copyright and content safety rules that precede it in the search instructions.

## How it works

### The enhance-understanding test (L1618)

The single core principle is a question: "Would images enhance the person's understanding or experience of this query?" (System Prompt Export 2026-07, L1618). If a visual would help the person understand, engage, or act, images are used. The prompt stresses this is "additive, not exclusive" (L1618): a query that needs a text explanation can still earn accompanying visuals. L1624 lists illustrative beneficiaries: places, animals, food, products, style, diagrams, historical photos, exercises, and even simple facts about visual things, with the Eiffel Tower construction-year query given as an example that should still show the tower. The list is explicitly "illustrative, not exhaustive" (L1625).

### The skip-list (L1627-1629)

Image search is not used for text-shaped work. The prompt names the skip cases at L1628: "text output (drafting emails, code, essays), numbers/data" (System Prompt Export 2026-07, L1628), plus coding queries, technical support, step-by-step instructions such as installing VS Code, math, and analysis of non-visual topics. L1629 repeats the rule for emphasis: technical queries, SaaS support, coding questions, and drafting of text and emails should not trigger image search "unless explicitly requested" (L1629).

### Content safety overlay (L1636-1646)

A blocked-category list overrides the enhance test entirely: harm-enabling or graphic imagery, pro-eating-disorder content, copyrighted characters and IP, licensed sports content, movie and TV and music imagery, celebrity and paparazzi photos, standalone artworks, and sexual or privacy-violating content are never searched (L1636-1646). Artworks may only be retrieved shown in a larger display context, such as inside a museum (L1645).

### Query construction and image budget (L1652-1653)

Queries are kept "specific (3-6 words)" with context included, the example being "Paris France Eiffel Tower" rather than "Paris" (System Prompt Export 2026-07, L1652). Every call requests "a minimum of 3 images" and sticks "to a maximum of 4 images" (System Prompt Export 2026-07, L1653).

### Lead versus interleave placement (L1654-1657)

Images render inline where the tool is called, so placement is a writing decision:

- Multi-item content (guides, lists, comparisons, timelines, steps): interleave. Write about the item, call the tool, continue, so "Each image sits next to the text it illustrates" (System Prompt Export 2026-07, L1655).
- "If the image IS the answer" (System Prompt Export 2026-07, L1656), as in "what does X look like" or "show me X" queries: lead with the image, then describe.
- Shopping and product queries: always interleave, because "front-loading product images looks like ads" (System Prompt Export 2026-07, L1657). The only exception is an explicit request to see a specific product, like the Adidas Samba.
- Never end the turn on an image search; "Always continue the response after an image search" (System Prompt Export 2026-07, L1658).

### Worked examples (L1662-1686)

- "Things to do in Tokyo" (L1666-1668): interleaved searches for Senso-ji, Shibuya crossing, and TeamLab Planets, one after the text describing each spot; the stated reason is that visual references help people pick attractions matching their interests.
- "What does a pangolin look like?" (L1670-1672): the search leads the reply because the image is the answer, with the description following.
- Datadog log filtering (L1682-1684): no image search at all, because the person needs text and code and "likely already knows what the Datadog UI looks like" (System Prompt Export 2026-07, L1684).

## Best practice

- EVIDENCE-BASED (L1618): run the enhance-understanding test first; when a visual adds nothing, skip the tool rather than decorating the answer.
- EVIDENCE-BASED (L1627-1629): treat coding, technical support, drafting, math, and data queries as no-image by default; only an explicit user request overrides.
- EVIDENCE-BASED (L1652-1653): build 3 to 6 word queries with disambiguating context and expect 3 to 4 images per call, never more.
- EVIDENCE-BASED (L1654-1658): interleave for multi-item content, lead only when the image is the answer, and always write text after the final image call.
- PRACTITIONER: when reverse-engineering claude.ai behavior for prompt design, mirror this two-gate pattern (utility test plus explicit skip-list) in custom tool instructions; it is the same shape as the ladder in [[Visualizer Decision Ladder]].

## Pitfalls

- The rules describe the claude.ai harness only; Claude Code has no image search tool, so none of this transfers there (see [[Export Omits Claude Code Harness]]).
- Front-loading product images is explicitly flagged as ad-like (L1657); an agent copying "lead with the visual" advice into shopping answers violates the prompt.
- The content safety list (L1636-1646) is absolute and sits above the enhance test; a query can pass the utility test and still be blocked, notably copyrighted characters, sports, and celebrity photos.
- The 3-image minimum per call (L1653) means a single marginal illustration is out of spec; if only one image is worth showing, the batch still returns 3 to 4.
- Ending a reply on an image search is prohibited (L1658); truncated responses that stop at an image violate the block.

## Sources

- System Prompt Export 2026-07, L1614-1688, `<using_image_search_tool>` block, captured 2026-07-07.
- Anthropic system prompt release notes, https://platform.claude.com/docs/en/release-notes/system-prompts (retrieved 2026-07-07); the official page documents the behavior core but not this tool block, which is corroborated only by full captures.

## Related

- [[System Prompt Export 2026-07]] because it is the primary source containing L1614-1688.
- [[Core Search Behaviors]] because image search inherits the general search instructions that precede it.
- [[Knowledge Cutoff and Search Triggers]] because rate-of-change reasoning decides text search the same way the enhance test decides image search.
- [[Copyright Compliance Rules]] because the blocked-category list extends the copyright guidance to imagery.
- [[Visualizer Decision Ladder]] because it is the sibling decision ladder for generated visuals rather than fetched ones.
- [[Artifacts Usage Criteria]] because artifacts are the other placement surface for visual output on claude.ai.
- [[Export Chapter Computer Use and Search]] because this block lives in the search chapter of the export.
- [[claude.ai Platform]] because these rules apply only to the claude.ai harness.
- [[Claude Fable 5]] because the model executing these rules is Fable 5.
- [[Public System Prompt Copies]] because community captures corroborate this block outside the official page.

## Next actions

- Diff this block against the next export capture during the [[Brain Refresh Flow]]; placement rules and the image budget are likely tuning targets.
- Verify whether the mid-century modern renovation example (L1678-1680) survives future revisions; it is the newest-looking example.

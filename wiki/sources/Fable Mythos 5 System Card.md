---
type: source
title: "Fable Mythos 5 System Card"
status: mature
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/model
  - note/source
domain: model-and-family
confidence: evidence-based
related:
  - "[[Claude Fable 5]]"
  - "[[Claude Mythos 5]]"
  - "[[Mythos-Class Model Tier]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Project Glasswing]]"
  - "[[Fable Mythos Operating Doctrine]]"
  - "[[Claude Character and Constitution]]"
  - "[[User Wellbeing Rules]]"
  - "[[Evenhandedness Rules]]"
source_urls:
  - "https://www.anthropic.com/system-cards (retrieved 2026-07-07)"
  - "https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf (published 2026-06-09, retrieved 2026-07-07)"
  - "https://www-cdn.anthropic.com/08ab9158070959f88f296514c21b7facce6f52bc.pdf (published 2026-04-07, retrieved 2026-07-07)"
---

# Fable Mythos 5 System Card

The Claude Fable 5 and Claude Mythos 5 system card is the primary public evidence source for the shared-weight model's capabilities, safety evaluations, threshold judgments, and deployment split.

## What it is

- Anthropic's 319-page system card for Claude Fable 5 and Claude Mythos 5, dated 2026-06-09 and listed on Anthropic's model system cards page.
- A paired source with the 245-page Claude Mythos Preview system card dated 2026-04-07, which explains why the earlier model was restricted to [[Project Glasswing]].
- The source that corrects this vault's earlier stale gap about missing public benchmark data.
- A source about configurations, not just model weights: Mythos 5 represents the underlying capability without the Fable safeguards, while Fable 5 represents the broadly deployed safeguarded experience.

## How it works

- The executive summary states that Fable 5 and Mythos 5 are two configurations of a new large language model.
- Anthropic describes Mythos 5 as the most capable model it had ever trained at publication time.
- Fable 5 has additional safeguards that block or route high-risk biology and cybersecurity tasks.
- Mythos 5 has relevant safeguards lifted and is made available only to a small number of trusted partners.
- In chemical and biological risk, Anthropic treats Mythos 5 as CB-1 but judges that it does not cross CB-2.
- That CB-2 judgment is explicitly less clear than for previous models, and Anthropic says unsafeguarded Mythos 5 can significantly uplift well-resourced threat actors.
- In cyber, Anthropic says Mythos 5 is the most capable model it has evaluated on cyber tasks.
- Fable 5's cyber classifiers flag cyber capability evaluations and cause fallback to Opus 4.8, making Fable's deployed cyber performance similar to Opus 4.8.
- In prompt-injection robustness, Anthropic reports that Mythos models are its most resilient models to date, with Fable inheriting the core-model gains.
- The card includes behavioral and welfare evaluations that already feed this vault's notes on [[Claude Character and Constitution]], wellbeing, child safety, evenhandedness, and mistakes.
- The system card's Fable scores must be read as production-safeguarded scores where classifiers and fallback can change the served model.

## Best practice

- Cite the system card for public benchmark and safety evidence before citing commentary. EVIDENCE-BASED
- Distinguish Mythos 5 underlying capability results from Fable 5 deployed results whenever classifiers could fire. EVIDENCE-BASED
- Treat Fable 5 as a router-plus-model in cyber and biology contexts, not as a pure benchmark of the unsafeguarded underlying model. EVIDENCE-BASED
- Use the Mythos Preview system card as historical baseline evidence, not current access evidence. EVIDENCE-BASED
- When quoting risk thresholds, preserve Anthropic's uncertainty language around CB-2 and well-resourced threat-actor uplift. EVIDENCE-BASED
- Keep system-card benchmark numbers in a separate source note from marketing claims and customer testimonials. PRACTITIONER

## Pitfalls

- Saying "Fable and Mythos have the same benchmark results" without checking whether Fable's classifiers affected that benchmark.
- Treating "does not cross CB-2" as "low biological risk." The card says risk is higher than for previous models and close enough to require detailed analysis.
- Treating CJS or jailbreak evidence as a guarantee. Anthropic says breaking safeguards is extremely difficult, not impossible.
- Mixing Mythos Preview and Mythos 5 results without date labels.
- Reusing system-card tables without reading evaluation conditions, effort settings, tools, sample counts, and safeguards status.
- Treating model welfare exploration as operational guidance for users; it is an exploratory safety analysis, not an operator promise.

## Sources

- Model system cards, Anthropic: https://www.anthropic.com/system-cards (retrieved 2026-07-07).
- Claude Fable 5 and Claude Mythos 5 System Card, Anthropic PDF: https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf (published 2026-06-09, retrieved 2026-07-07).
- Claude Mythos Preview System Card, Anthropic PDF: https://www-cdn.anthropic.com/08ab9158070959f88f296514c21b7facce6f52bc.pdf (published 2026-04-07, retrieved 2026-07-07).
- Claude Fable 5 and Claude Mythos 5, Anthropic launch post: https://www.anthropic.com/news/claude-fable-5-mythos-5 (published 2026-06-09, retrieved 2026-07-07).
- Project Glasswing, Anthropic: https://www.anthropic.com/glasswing (published 2026-04-07, retrieved 2026-07-07).
- More details on Fable 5's cyber safeguards, Anthropic: https://www.anthropic.com/news/fable-safeguards-jailbreak-framework (published 2026-07-02, retrieved 2026-07-07).

## Related

- [[Claude Fable 5]] because the system card defines the deployed general-release model.
- [[Claude Mythos 5]] because the system card defines the trusted-access configuration.
- [[Mythos-Class Model Tier]] because the card explains why the tier exists above Opus.
- [[Fable 5 Dual-Use Safety Measures]] because the card details the safeguards and fallback behavior.
- [[Project Glasswing]] because the system card and Glasswing program are coupled.
- [[Fable Mythos Operating Doctrine]] because the doctrine distills this card into operating rules.
- [[Claude Character and Constitution]] because the card reports behavioral and alignment audits.
- [[User Wellbeing Rules]] because the card records mental-health and self-harm evaluation findings.
- [[Evenhandedness Rules]] because the card reports political evenhandedness findings.

## Next actions

- Extract a capability matrix table from the system card into a dedicated report.
- Add page-level PDF references if the repo later stores immutable PDF text extracts under `.raw/`.
- Reconcile every old "no benchmark data" link to this source note.
- Add a Mythos Preview versus Mythos 5 comparison once the migration and deprecation docs are fully indexed.
- Refresh this note when Anthropic updates the system-card page or publishes a new risk report.

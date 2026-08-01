---
type: flow
title: "Brain Refresh Flow"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/best-practices
  - note/flow
domain: best-practices
confidence: practitioner
approval_status: approved
risk_level: low
rollback_note: "Refresh edits touch note frontmatter, claims, and the source ledger, all under git; revert the refresh commit to restore the prior state."
related:
  - "[[Claim Verification Flow]]"
  - "[[Corpus Ingestion Flow]]"
  - "[[Confidence Tag Policy]]"
  - "[[Citation Discipline]]"
  - "[[docs.claude.com]]"
  - "[[Anthropic Engineering Blog Shelf]]"
  - "[[Fable 5 Pricing and Rate Limits]]"
  - "[[No Public Fable 5 Benchmark Data]]"
  - "[[Claude Fable 5]]"
  - "[[CONVENTIONS]]"
source_urls:
  - "https://www.anthropic.com/news/redeploying-fable-5 (retrieved 2026-07-07)"
  - "https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)"
---

# Brain Refresh Flow

When a source's refresh_due date in references/source-ledger.json passes, this brain stops trusting it: scan the ledger, re-fetch every stale URL, re-verify the claims each one supports, then bump dates, and demote anything that no longer verifies.

## What it is

The maintenance loop that keeps this vault's claims current. The [[Confidence Tag Policy]] rule is explicit: anything past its refresh_due date in the ledger is stale and must be re-verified before being cited as current. The Fable 5 domain proves the need. Within three weeks of launch the facts changed twice: US export controls suspended all Fable 5 and Mythos 5 access on June 12, 2026, and Anthropic then announced "the export controls on Fable 5 and Mythos 5 have been lifted" (https://www.anthropic.com/news/redeploying-fable-5). URLs churn too: docs.claude.com Claude Code pages now 301-redirect to code.claude.com/docs, and legacy prompting technique pages redirect to a consolidated reference.

## How it works

1. **Ledger scan.** Read references/source-ledger.json and list every entry with refresh_due on or before today. Each hit is a stale source; every note citing it is a refresh candidate.
2. **Re-fetch.** Retrieve each stale URL. Record the new retrieval date, follow and note any redirect (a moved URL is a finding in itself), and flag fetch failures.
3. **Re-verify.** Diff the fetched content against the claims the source supports in the owning notes. Three outcomes: still supported, changed, or gone.
4. **Update.** Still supported: bump the retrieved date in source_urls and the ledger, and bump the note's updated field. Changed: rewrite the claim, and if the new source conflicts with another live source, set confidence to contested and add a `> [!contradiction]` callout in the owning note. Gone: mark the claim with a `> [!stale]` callout and hunt a replacement source before the claim can be cited again.
5. **Close out.** Append a log entry, refresh hot.md if hot facts moved, and run the lint and audit gates before committing.

> [!key-insight]
> Refresh priority follows volatility, not age. Availability and pricing claims moved twice in June 2026 while workflow guidance from 2024 still verifies; the ledger's refresh_due intervals should encode that difference instead of applying one uniform window.

Worked example from this domain: the legacy prompting URLs (use-xml-tags, chain-of-thought, claude-4-best-practices) did not die, they redirect to the consolidated Prompting best practices reference. A naive link check reports success; only a content re-verification notices that the owning notes should now cite the consolidated page.

## Best practice

- Run the scan on a schedule, not on demand; stale claims fail silently until something reads them. PRACTITIONER
- Treat redirects as signal: the docs migration to code.claude.com rewrote this brain's canonical Claude Code URLs once already. EVIDENCE-BASED
- Re-verify claims, not just links; a URL that still resolves can carry changed content, as the Fable 5 restoration timeline did across Anthropic and press accounts. EVIDENCE-BASED
- Downgrade before you delete: a conflicting refresh result becomes CONTESTED with a callout, preserving the audit trail. PRACTITIONER
- Give the refresh run a check it can run, mirroring the Claude Code principle of verifiable checks: the lint and audit scripts are this flow's pass condition. EVIDENCE-BASED
- Batch by source, not by note; one re-fetched URL usually clears claims across several notes at once. PRACTITIONER
- Never bump updated without an actual re-verification; a fresh date on a stale claim is worse than a stale date. PRACTITIONER

## Pitfalls

- Bumping dates in bulk without reading the fetched content; that converts stale claims into confidently wrong ones.
- Ignoring press-versus-vendor conflicts; Anthropic dates the export-control lift to June 30 with July 1 restoration while Al Jazeera reports July 1 notification and July 2 restoration, which is why that claim stays contested here.
- Letting a dead source linger uncited but undemoted; the stale callout must be visible in the owning note.
- Refreshing wiki notes but forgetting the ledger, which desynchronizes the next scan.
- Editing .raw captures during refresh; raw sources are immutable, refresh touches wiki and ledger only.

## Sources

- Redeploying Claude Fable 5, Anthropic: https://www.anthropic.com/news/redeploying-fable-5 (published 2026-06-30, retrieved 2026-07-07)
- US lifts restrictions on Anthropic's powerful AI models Fable and Mythos, Al Jazeera: https://www.aljazeera.com/economy/2026/7/1/us-lifts-restrictions-on-powerful-ai-models-fable-mythos-anthropic-says (published 2026-07-01, retrieved 2026-07-07)
- Best practices for Claude Code (verifiable checks principle), official docs: https://code.claude.com/docs/en/best-practices (retrieved 2026-07-07)
- Prompt engineering overview (consolidated reference the legacy URLs redirect to): https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview (retrieved 2026-07-07)

## Related

- [[Claim Verification Flow]] because refresh reruns that flow's second-source check on old claims.
- [[Corpus Ingestion Flow]] because a new export capture triggers the same diff-and-file machinery.
- [[Confidence Tag Policy]] because the staleness rule and demotion ladder live there.
- [[Citation Discipline]] because retrieval dates and line refs are what refresh actually bumps.
- [[docs.claude.com]] because the docs migration is the canonical example of URL churn.
- [[Anthropic Engineering Blog Shelf]] because shelf posts age and need the same re-verification.
- [[Fable 5 Pricing and Rate Limits]] because pricing is the fact class most likely to drift.
- [[No Public Fable 5 Benchmark Data]] because that gap note is the worked example of flipping a gap once public evaluation evidence lands.
- [[Claude Fable 5]] because the hub note aggregates the most refresh-sensitive claims.
- [[CONVENTIONS]] because gates, callouts, and log format come from the vault contract.

## Next actions

- Confirm every current ledger entry has a refresh_due value; add defaults where missing.
- Script the ledger scan step so the flow starts from a generated stale-source list.
- Schedule the first full refresh pass relative to the earliest refresh_due in the ledger.
- Assign shorter refresh intervals to pricing and availability claims than to workflow guidance.

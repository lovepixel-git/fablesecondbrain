# Confidence Tags

EVIDENCE-BASED: supported by controlled research or authoritative primary data.
PRACTITIONER: operationally useful applied judgment or field practice, not proven by studies.
CONTESTED: mixed, disputed, or failed-replication evidence; use with a caveat.
FOLKLORE: popular claim without credible support; demoted, never presented as fact.

Usage rule: every domain claim carries exactly one tag. Folklore is demoted, never asserted as truth. A bestseller or popularity is not evidence.

## Assignment policy for this domain

Fable 5 is new and public coverage is thin, so this brain applies the tags as follows:

1. A claim sourced only from the system prompt export is EVIDENCE-BASED with
   `source_type: primary` and a mandatory line reference (format `L123-145`). It is
   evidence of that capture, not a universal guarantee; the note must say which harness
   (claude.ai) it describes.
2. A claim corroborated by a dated public Anthropic URL (docs, news, engineering) is
   EVIDENCE-BASED.
3. Plausible operational advice without official confirmation is PRACTITIONER.
4. An export-versus-docs conflict is CONTESTED until resolved by a newer official
   source, with a `> [!contradiction]` callout in the owning note.
5. Anything past its `refresh_due` date in `references/source-ledger.json` is stale and
   must be re-verified before being cited as current.

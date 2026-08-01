---
type: concept
title: "Artifact Persistent Storage API"
status: developing
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/harness/claude-ai
  - note/concept
domain: claude-ai-harness
confidence: evidence-based
related:
  - "[[Claude Fable 5]]"
  - "[[System Prompt Export 2026-07]]"
  - "[[claude.ai Platform]]"
  - "[[Artifacts Usage Criteria]]"
  - "[[Anthropic API in Artifacts]]"
  - "[[Visualizer Decision Ladder]]"
  - "[[Computer Use File Handling Rules]]"
  - "[[Export Chapter Artifacts API and Citations]]"
  - "[[Export Chapter Product and Behavior]]"
  - "[[docs.claude.com]]"
source_urls:
  - "https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (retrieved 2026-07-07)"
sources:
  - "[[System Prompt Export 2026-07]]"
---

# Artifact Persistent Storage API

claude.ai artifacts persist data across sessions through a window.storage key-value API with get, set, delete, and list methods, a shared flag for per-user versus all-users scope, keys under 200 characters, values under 5MB, and last-write-wins concurrency.

## What it is

The persistent_storage_for_artifacts block of the July 2026 capture (System Prompt Export 2026-07, L692-766) gives artifacts a storage layer that survives page reloads and new conversations, enabling journals, trackers, leaderboards, and collaborative tools (L694). It exists because browser storage is banned outright in artifacts by [[Artifacts Usage Criteria]] (L1162-1164); window.storage is the replacement the harness injects. The export states "Artifacts access storage through window.storage with these methods" (System Prompt Export 2026-07, L697) and then defines exactly four async methods.

## How it works

**API surface (L699-702).** All methods are awaited and return an object or null: `window.storage.get(key, shared?)` returns {key, value, shared}, `set(key, value, shared?)` stores a value, `delete(key, shared?)` returns {key, deleted, shared}, and `list(prefix?, shared?)` returns {keys, prefix?, shared}.

**Scope model (L727-731).** Personal data uses shared:false, the default, and is visible only to the current user. Shared data uses shared:true and is readable and writable by every user of the artifact. The prompt requires informing users that shared data is visible to others, and the limitations section says to always pass the shared parameter explicitly rather than relying on the default (L762).

**Key design (L720-725).** Keys are hierarchical strings under 200 characters in `table_name:record_id` style, such as "todos:todo_1". Keys cannot contain whitespace, path separators, or quotes. Data updated together belongs in one key: the export's examples replace three sequential set calls with a single cards-and-benefits object, and replace a per-pixel get loop over a 48x48 board with one board-pixels key.

**Error semantics (L733-753).** Every operation can fail, so all calls sit in try-catch. Notably, "accessing non-existent keys will throw errors, not return null" (System Prompt Export 2026-07, L734), so existence checks are written as catch branches, not null checks.

**Hard limits (L756-762).** Text and JSON only, no file uploads. Keys under 200 characters. Values under 5MB per key. Requests are rate limited, which is the second reason to batch related data into single keys. Concurrent updates resolve last-write-wins.

**UX contract (L764).** Artifacts using storage implement proper error handling, show loading indicators, render data progressively instead of blocking the whole UI, and consider a reset option so users can clear their data.

> [!gap]
> No public docs.claude.com or help-center URL describing window.storage was captured in the research pack, so quota behavior per plan, storage lifetime after artifact deletion, and any admin controls are unverified beyond the export text.

## Best practice

- Wrap every window.storage call in try-catch and treat a thrown get as "key absent", not as a fatal error. EVIDENCE-BASED
- Pass the shared flag explicitly on every call, even when using the personal default. EVIDENCE-BASED
- Design hierarchical keys like `entries:123` and keep them under 200 characters with no whitespace, slashes, or quotes. EVIDENCE-BASED
- Batch state that changes together into one JSON value per key to respect rate limits and avoid sequential call chains. EVIDENCE-BASED
- Tell users plainly when shared:true data will be visible to everyone using the artifact. EVIDENCE-BASED
- Serialize with JSON.stringify on write and guard JSON.parse on read, since values are text only. EVIDENCE-BASED
- Add a visible reset control so users can clear stored state without developer help. EVIDENCE-BASED
- Keep single values well under the 5MB cap and paginate large datasets across prefixed keys. PRACTITIONER
- Do not build multi-user apps that need transactional integrity on this API; last-write-wins silently drops concurrent updates. PRACTITIONER

## Pitfalls

- Checking `if (result === null)` to detect missing keys; missing keys throw instead of returning null (L734).
- Looping storage calls per record; rate limiting makes per-item get and set patterns fail or crawl (L723-725, L760).
- Storing binary or file data; the API accepts text and JSON only (L757).
- Forgetting the shared flag and accidentally writing leaderboard data into personal scope, or personal data into shared scope.
- Assuming optimistic-lock or merge semantics; two simultaneous writers end with one winner and no conflict signal (L761).
- Falling back to localStorage when window.storage feels limiting; browser storage APIs fail in claude.ai artifacts (L1162-1164).
- Treating the export's description as an API guarantee outside claude.ai; the capture documents this harness only.

## Sources

- System Prompt Export 2026-07, L692-766, persistent_storage_for_artifacts block (capture retrieved 2026-07-07). Primary source for the full API surface, limits, and patterns.
- System Prompt Export 2026-07, L1162-1164, browser storage ban that motivates this API (retrieved 2026-07-07).
- Equipping agents for the real world with Agent Skills, https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (published 2025-10-16, retrieved 2026-07-07). Background only; does not document window.storage.

## Related

- [[Artifacts Usage Criteria]] because the browser storage ban there makes window.storage the only persistence path.
- [[Anthropic API in Artifacts]] because AI-powered artifacts combine storage with /v1/messages calls for stateful apps.
- [[System Prompt Export 2026-07]] because every limit and method signature here comes from that capture.
- [[claude.ai Platform]] because the API is injected by the consumer harness, not by the model.
- [[Computer Use File Handling Rules]] because artifact files themselves are created through the computer-use container.
- [[Visualizer Decision Ladder]] because inline Visualizer widgets are the non-persistent alternative to storage-backed artifacts.
- [[Export Chapter Artifacts API and Citations]] because that chapter note maps the artifact-related export regions.
- [[Export Chapter Product and Behavior]] because product-level behavior rules frame when artifacts appear at all.
- [[docs.claude.com]] because the missing public documentation should eventually be located there.
- [[Claude Fable 5]] because Fable 5 writes the artifact code that consumes this API.

## Next actions

- Build a small tracker artifact on claude.ai and verify the throw-on-missing-key behavior and the 5MB value cap empirically.
- Search docs.claude.com and the help center for official window.storage documentation to close the gap callout.
- Test whether stored values survive artifact remixing and conversation deletion, and record the result.

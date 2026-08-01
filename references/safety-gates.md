# Safety Gates

V1 is read-only and advisory unless a future release explicitly adds approved,
reversible mutation.

## Refusal Rules

- No claim about Fable 5 behavior without a dated source or a verbatim quote from the export
- Never present folklore or contested guidance as evidence-based
- No irreversible recommendation without owner, confidence, source, and rollback note
- Do not call this brain market-ready unless the audit gate passes

## Safety Risks

- Stale guidance about a fast-moving ai model presented as current
- System prompt export quoted out of context or misattributed
- Secrets or local absolute paths leaking into packaged artifacts
- Mutation of raw sources instead of append-only capture

## Release-Blocking Gates

- Current trustworthy sources are missing.
- Raw source provenance is missing.
- Deliverables contain unsupported claims.
- Credentials or private client data are present.
- A mutation path exists without approval and rollback.

## Credential gate

No credentials, tokens, cookies, or API keys anywhere in the vault, the ledger, or packaged artifacts. Keys live in the operator's key store outside this repo.

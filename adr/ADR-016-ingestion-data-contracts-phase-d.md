# ADR-016: Ingestion Data Contracts + Real Lineage (Phase D)

## Status

Accepted — 2026-07-05

## In one breath (panel)

I'd reject ingest that fails the data contract — missing owner, missing lineage URI — instead of computing the issue and then quietly indexing the junk anyway.

## Context

`enterprise_rag_platform`'s `DocumentChunker._validate()` already knew when a doc was missing an owner, a lineage URI, near-empty content, or freshness metadata. `/v1/ingest` threw that work away. A document with no owner and no source URI got indexed like it was clean. That's how retrieval demos look smart and provenance audits fail later.

Phase D of the top-1% program was supposed to "master data foundations." The real gap wasn't inventing a new contract — it was wiring the one we already computed.

## Decision

Full detail lives in [enterprise_rag_platform ADR-0005](https://github.com/vpeetla-ai/enterprise_rag_platform/blob/main/docs/adr/0005-ingestion-data-contract-and-lineage.md).

Plain English: make lineage real on the chunk, and stop pretending soft validation is enforcement.

- `Chunk` got a real `content_hash` (position-independent, unlike `chunk_id`'s hash) and `ingested_at`
- `/v1/ingest` returns **422** on hard contract violations instead of silent accept
- Soft issues (missing freshness) stay warnings — not rejections
- Refused: inventing a brand-new "data quality framework" when the bug was discard-after-validate

## Consequences

**Positive**

- Closes a real gap (validation computed, then discarded) rather than manufacturing scope
- Found 3 places that rebuild a `Chunk` and would have silently dropped the new lineage fields — including a Qdrant round-trip — covered with 9 new tests
- While writing those tests, found a worse CI scar: the workflow ran `python -m unittest discover`, which never collected bare pytest functions in `tests/test_api_auth.py`. Auth-gate tests from an earlier security fix had **never run in CI**. Switched to `pytest tests/` — 32 tests instead of 16

**Negative**

- 422 on `/v1/ingest` breaks callers that relied on silent accept — intentional; the violation was always real

## References

- [enterprise_rag_platform ADR-0005](https://github.com/vpeetla-ai/enterprise_rag_platform/blob/main/docs/adr/0005-ingestion-data-contract-and-lineage.md)
- `enterprise_rag_platform/tests/test_ingestion_contract.py`

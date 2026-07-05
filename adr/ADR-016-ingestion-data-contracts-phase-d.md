# ADR-016: Ingestion Data Contracts + Real Lineage (Phase D)

## Status

Accepted — 2026-07-05

## Context

Phase D of the top-1% AI Architect program targeted step 3 of the 15-step roadmap ("Master Data
Foundations") — a real, verified gap: `enterprise_rag_platform`'s `DocumentChunker._validate()`
already computed `IngestionIssue`s for missing owner, missing lineage URI, near-empty content,
and missing freshness metadata, but `/v1/ingest` discarded them entirely. A document with no
owner or no source URI was silently accepted and indexed.

## Decision

Full detail lives in [enterprise_rag_platform ADR-0005](https://github.com/vpeetla-ai/enterprise_rag_platform/blob/main/docs/adr/0005-ingestion-data-contract-and-lineage.md).
Summary: `Chunk` gained a real `content_hash` (position-independent, unlike `chunk_id`'s hash)
and `ingested_at`; `/v1/ingest` now rejects (422) hard data-contract violations instead of
silently indexing them, while soft issues (missing freshness metadata) surface as warnings, not
rejections.

## Consequences

### Positive
- Closes a real gap (validation computed, then discarded) rather than inventing a new
  requirement — matches this program's pattern of finding real bugs, not manufacturing scope.
- Found and fixed 3 places that reconstruct a `Chunk` explicitly and would have silently
  dropped the new lineage fields to their defaults — including a full round-trip through the
  optional Qdrant-backed persistent store, verified with 9 new tests.
- **Found and fixed a second, unrelated, more consequential gap while writing those tests**:
  the repo's own CI workflow ran `python -m unittest discover`, which only discovers
  `unittest.TestCase`-based tests. `tests/test_api_auth.py` — the RAG_API_KEY auth-gate tests
  from an earlier security fix — uses bare pytest-style functions and had **never actually run
  in CI**, silently reporting 0 collected tests from that file while the overall build still
  passed. Fixed by switching to `pytest tests/`, which discovers both styles: 32 tests run now
  instead of 16.

### Negative
- The 422 rejection on `/v1/ingest` is a behavior change for any caller relying on the old
  silent-accept path — intended, since the contract violation was always real, just ignored.

## References
- [enterprise_rag_platform ADR-0005](https://github.com/vpeetla-ai/enterprise_rag_platform/blob/main/docs/adr/0005-ingestion-data-contract-and-lineage.md)
- `enterprise_rag_platform/tests/test_ingestion_contract.py`

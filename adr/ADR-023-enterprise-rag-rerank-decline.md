# ADR-023: Cross-Encoder Rerank and Decline-to-Answer

**Status:** Accepted  
**Date:** Jul 2026  
**System:** Enterprise RAG Platform (`enterprise_rag_platform`)

## In one breath (panel)

I'd rerank with a cross-encoder after hybrid recall — and decline to answer when top evidence is weak instead of synthesizing a confident hallucination.

## Context

Hybrid retrieval alone returns plausible-but-wrong chunks. Heuristic score boosts paper over that. Production RAG needs a second pass that actually compares query↔passage, and a hard stop when the best hit isn't good enough. Access-before-ranking ([ADR-002](./ADR-002-authorization-before-ranking-rag.md)) stops unauthorized neighbors; it does not stop low-confidence authorized ones from becoming fluent lies.

## Decision

1. Add **`CrossEncoderReranker`** (`sentence-transformers/cross-encoder/ms-marco-MiniLM-L-6-v2`) after hybrid retrieval, with `ScoreBoostReranker` as lightweight fallback when ML deps aren't available
2. **Decline-to-answer** when top hit score &lt; `RAG_DECLINE_THRESHOLD` (default `0.15`) — emit `declined_low_confidence` instead of a grounded-looking answer

Refused: always answering "something" because empty responses feel bad in demos.

## Consequences

Pipeline becomes: Access filter → Hybrid retrieve → **Cross-encoder rerank** → Context → Generate → **Decline gate**.

Canonical diagram: [enterprise_rag_platform/docs/diagrams/canonical-architecture.mmd](https://github.com/vpeetla-ai/enterprise_rag_platform/blob/main/docs/diagrams/canonical-architecture.mmd). Complements ADR-002 — authorization first, then quality gates.

## Links

- [Case study](../case-studies/enterprise-rag-platform.md)
- [LinkedIn Launch Plan](../docs/LINKEDIN_LAUNCH_PLAN.md)
- Related: [ADR-002](./ADR-002-authorization-before-ranking-rag.md)

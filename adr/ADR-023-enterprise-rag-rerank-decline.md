# ADR-023: Cross-Encoder Rerank and Decline-to-Answer

**Status:** Accepted  
**Date:** Jul 2026  
**System:** Enterprise RAG Platform (`enterprise_rag_platform`)

## Context

Hybrid retrieval alone can return plausible-but-wrong chunks. Production RAG needs:

1. **Reranking** after hybrid recall — not only heuristic score boosts
2. **Decline-to-answer** when top evidence is below confidence — not hallucinated synthesis

## Decision

1. Add **`CrossEncoderReranker`** (`sentence-transformers/cross-encoder/ms-marco-MiniLM-L-6-v2`) after hybrid retrieval, with `ScoreBoostReranker` as lightweight fallback when ML deps unavailable.

2. Add **decline-to-answer** when top hit score &lt; `RAG_DECLINE_THRESHOLD` (default `0.15`) — emit `declined_low_confidence` risk flag instead of grounded answer.

## Consequences

- Pipeline: Access filter → Hybrid retrieve → **Cross-encoder rerank** → Context → Generate → **Decline gate**
- Canonical diagram: [enterprise_rag_platform/docs/diagrams/canonical-architecture.mmd](https://github.com/vpeetla-ai/enterprise_rag_platform/blob/main/docs/diagrams/canonical-architecture.mmd)
- Complements [ADR-002](./ADR-002-authorization-before-ranking-rag.md) (access before ranking)

## Links

- [Case study](../case-studies/enterprise-rag-platform.md)
- [LinkedIn Launch Plan](../docs/LINKEDIN_LAUNCH_PLAN.md)

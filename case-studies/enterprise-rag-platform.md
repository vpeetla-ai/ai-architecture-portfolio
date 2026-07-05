# Enterprise RAG Platform — Access-Aware Knowledge Layer

**Domain:** Enterprise RAG · Hybrid retrieval · Governance  
**Live demo:** [demo-omega-taupe.vercel.app](https://demo-omega-taupe.vercel.app)  
**Source:** [github.com/vpeetla-ai/enterprise_rag_platform](https://github.com/vpeetla-ai/enterprise_rag_platform)

## Problem

Production RAG is not "connect a vector DB." Enterprise knowledge requires access control, citation traceability, evaluation gates, and integration with governance for ingest and high-risk answers.

## Architecture

```text
Query + Principal → Access Filter → Hybrid Retriever → Reranker → Graph Expand
       → Context Assembly → LLM + Citations → Eval/HITL → Langfuse export
```

```mermaid
flowchart LR
    Q[Query] --> AF[Access filter] --> RET[Hybrid retriever] --> RR[Rerank]
    RR --> CTX[Context] --> LLM[LLM + citations] --> EV[Eval]
    EV -.-> LF[Langfuse<br/>trace-linked evals]
```

## Key outcome

Authorization **before** semantic ranking — not after generation.

## Trade-offs

| Decision | Rationale |
|----------|-----------|
| Access filter first | Prevent unauthorized content in context window |
| Hybrid lexical + semantic | Recall for exact terms and paraphrase |
| AegisAI HITL bridge | High-risk ingest and answer paths |
| Seeded demo corpus | Portfolio demo without mandatory vector DB |
| API-key gate, Principal still client-asserted ([ADR-0004](https://github.com/vpeetla-ai/enterprise_rag_platform/blob/main/docs/adr/0004-api-auth-and-principal-trust.md)) | Closes "anyone can call the API" but not "anyone can claim any identity in the request body" — the access-before-ranking guarantee holds only given a trustworthy Principal, which a real deployment must derive from a verified token |
| golden-eval-registry as a real CI gate, isolated pipeline not the demo singleton ([ADR-014](../adr/ADR-014-golden-eval-registry-real-ci-gate.md)) | CI now runs the shared `enterprise_rag_golden_v1` suite against a real, isolated `RagPipeline` and fails the build on regression — running it for the first time found and fixed a real bug in the fixture itself |
| Real ingestion data contract + lineage, not just computed-and-discarded validation ([ADR-0005](https://github.com/vpeetla-ai/enterprise_rag_platform/blob/main/docs/adr/0005-ingestion-data-contract-and-lineage.md) · [ADR-016](../adr/ADR-016-ingestion-data-contracts-phase-d.md)) | `/v1/ingest` now rejects bad documents (422) instead of silently indexing them; every chunk carries a real content hash + ingestion timestamp — found while writing the tests: a whole CI test file had never actually run |

## Related ADR

[ADR-002: Authorization before ranking](../adr/ADR-002-authorization-before-ranking-rag.md) · [ADR-0004: API auth and principal trust](https://github.com/vpeetla-ai/enterprise_rag_platform/blob/main/docs/adr/0004-api-auth-and-principal-trust.md) · [ADR-014: golden-eval-registry real CI gate](../adr/ADR-014-golden-eval-registry-real-ci-gate.md) · [ADR-016: Ingestion data contracts](../adr/ADR-016-ingestion-data-contracts-phase-d.md)

## Stack

FastAPI · Docker · Vercel · Render · Qdrant (optional)

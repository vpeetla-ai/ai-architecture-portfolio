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

## Related ADR

[ADR-002: Authorization before ranking](../architecture-decisions/002-authorization-before-ranking-rag.md)

## Stack

FastAPI · Docker · Vercel · Render · Qdrant (optional)

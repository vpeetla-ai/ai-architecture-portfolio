# ADR-002: Authorization Before Ranking in Enterprise RAG

**Status:** Accepted  
**Date:** 2026  
**System:** Enterprise RAG Platform  
**Live demo:** [demo-omega-taupe.vercel.app](https://demo-omega-taupe.vercel.app)

## Context

Most RAG implementations treat retrieval as a pure similarity problem: embed query, search vectors, assemble context, generate answer. Enterprise knowledge is not uniformly accessible — principals, groups, and clearance levels must filter what enters the context window *before* semantic ranking.

## Decision

Implement **authorization-before-ranking** as the primary architecture decision:

1. Resolve principal identity and group membership
2. Filter document/chunk candidates by access policy
3. Run hybrid retrieval (lexical + semantic) on the authorized subset only
4. Rerank, optionally expand via knowledge graph
5. Attach citations with traceability
6. Route high-risk answers through AegisAI HITL bridge

Vector database selection (Qdrant, pgvector, etc.) is an implementation detail — not the architecture.

## Trade-offs

| Choice | Rationale |
|--------|-----------|
| Filter before rank | Prevents leakage of unauthorized content into LLM context |
| Hybrid retrieval | Recall for exact terms + semantic paraphrase |
| Optional graph expansion | Deeper context when policy allows |
| HITL bridge | High-stakes answers require human gate |

## Proof

- [enterprise_rag_platform](https://github.com/vpeetla-ai/enterprise_rag_platform)
- Case study: [case-studies/enterprise-rag-platform.md](../case-studies/enterprise-rag-platform.md)

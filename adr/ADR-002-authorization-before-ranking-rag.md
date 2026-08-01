# ADR-002: Authorization Before Ranking in Enterprise RAG

**Status:** Accepted  
**Date:** 2026  
**System:** Enterprise RAG Platform  
**Live demo:** [demo-omega-taupe.vercel.app](https://demo-omega-taupe.vercel.app)

## In one breath (panel)

I'd filter by who the caller is *before* I rank — optimizing recall with unauthorized neighbors is how demos look smart and prod leaks.

## Context

Most RAG stacks treat retrieval as pure similarity: embed, search vectors, stuff context, generate. That fails the moment enterprise knowledge isn't uniformly accessible. Principals, groups, and clearance levels have to decide what enters the context window *before* semantic ranking — not after a pretty answer with a citation to something you shouldn't have seen.

I refused "post-filter the top-k" as the architecture. By then the model already saw the chunk.

## Decision

**Authorization-before-ranking** is the primary call. Vector DB choice (Qdrant, pgvector, …) is an implementation detail, not the story.

1. Resolve principal identity and group membership
2. Filter document/chunk candidates by access policy
3. Run hybrid retrieval (lexical + semantic) on the authorized subset only
4. Rerank; optionally expand via knowledge graph when policy allows
5. Attach citations with traceability
6. Route high-risk answers through the AegisAI HITL bridge

## Consequences

| Choice | Why |
|--------|-----|
| Filter before rank | Unauthorized content never reaches the LLM context |
| Hybrid retrieval | Exact terms and paraphrase both matter |
| Optional graph expansion | Deeper context only when policy allows |
| HITL bridge | High-stakes answers need a human gate |

**Scar:** ranking-first demos win recall bake-offs and lose trust reviews. I'd rather lose a few points of recall than explain a leak.

## Proof

- [enterprise_rag_platform](https://github.com/vpeetla-ai/enterprise_rag_platform)
- Case study: [case-studies/enterprise-rag-platform.md](../case-studies/enterprise-rag-platform.md)

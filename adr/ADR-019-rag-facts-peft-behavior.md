# ADR-019: RAG Holds Facts; PEFT Holds Format and Behavior

**Status:** Accepted  
**Date:** Jul 2026  
**System:** DomainForge (`domainforge-rag-peft`)  
**Live demo:** [domainforge-rag-peft.vercel.app](https://domainforge-rag-peft.vercel.app) · [API](https://domainforge-api.onrender.com/health)

## Context

Customer support triage needs two things at once:

1. **Grounded facts** from SOP documents (policies, procedures, citation `chunk_id`s)
2. **Reliable JSON** for downstream agents (`intent`, `suggested_action`, schema discipline)

Full fine-tuning memorizes stale policies and drifts when SOPs change. RAG-only models hallucinate field names and invent `chunk_id`s. Enterprise RAG (ADR-002) solves access-aware retrieval — but does not teach strict output grammar.

## Decision

Split the problem into two planes with separate data prep, eval metrics, and promotion gates:

| Plane | Responsibility | Data source | Mechanism |
|-------|----------------|-------------|-----------|
| **RAG** | Facts, policies, citations | 13 capstone SOP markdown docs | Chroma index → S1 naive → S2 hybrid BM25+lexical |
| **PEFT (QLoRA)** | JSON envelope, intent codes, action grammar | Bitext customer-support SFT (~27 intents) | TRL + PEFT adapter registry |

**Bitext SFT pairs are labels only** — not copied into the vector store as memorization targets.

**Solution ladder** for eval: S0 baseline → S1 naive RAG → S2 hybrid RAG → S3 PEFT+S2.

**Adapter promotion** (`POST /v1/adapters/promote`) remains API-key gated; blocked if faithfulness or format adherence regresses.

## Trade-offs

| Choice | Rationale | Cost |
|--------|-----------|------|
| Two pipelines | Each plane optimizes for what it does best | Two manifests, two prep CLIs |
| Capstone SOP corpus | Portfolio-safe, no employer supply-chain data | Not enterprise-scale doc count |
| Bitext public SFT | Realistic intent distribution without proprietary tickets | Domain mismatch vs SOP wording |
| `MOCK_LLM=true` on Render free tier | Demo RAG + eval without GPU | Production inference requires CUDA + Ollama/vLLM |
| Separate eval dimensions | Faithfulness (citations) ≠ format adherence | More golden fixtures to maintain |

## Consequences

- DomainForge complements [Enterprise RAG](https://github.com/vpeetla-ai/enterprise_rag_platform) (access-before-ranking) with an **MLOps adaptation layer**
- Interview narrative: "RAG for facts, fine-tune for behavior" — a Principal AI Architect decision, not a single-model shortcut
- Golden eval must score hallucination frequency and JSON schema separately

## Links

- Repo: [domainforge-rag-peft](https://github.com/vpeetla-ai/domainforge-rag-peft)
- Repo ADR: [ADR-001](https://github.com/vpeetla-ai/domainforge-rag-peft/blob/main/docs/adr/ADR-001-rag-vs-peft-separation.md)
- Case study: [domainforge-rag-peft.md](../case-studies/domainforge-rag-peft.md)
- Related: [ADR-002](ADR-002-authorization-before-ranking-rag.md) · [ADR-014](ADR-014-golden-eval-registry-real-ci-gate.md)
- Portfolio deep dive: [venkat-ai.com/projects/platform/domainforge](https://venkat-ai.com/projects/platform/domainforge)

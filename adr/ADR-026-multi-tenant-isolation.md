# ADR-026: Multi-Tenant Isolation for Governed Agent APIs

**Status:** Accepted  
**Date:** 2026-07-09  
**Systems:** Enterprise RAG (first), AegisAI gateway, Agent FinOps, org-wide API keys

## Context

Portfolio demos historically use a single tenant string (`acme`, `bank-demo`) with
client-asserted or weakly keyed boundaries. Enterprise reviewers ask for blast-radius,
quota, and data isolation before trusting access-before-ranking or FinOps meters.

## Decision

Define a **minimum multi-tenant contract** for production profiles
(`PRODUCTION_STRICT=true`):

| Boundary | Rule |
|----------|------|
| **Network / caller** | Per-tenant API key or JWT `tenant_id` claim — never a shared org key alone for write paths |
| **Data** | All retrieval, ingest, and report paths filter by verified `tenant_id` before ranking or archival |
| **Quota** | FinOps budgets scoped `tenant:{id}`; breach halts that tenant only |
| **Blast radius** | Gateway decisions and audit events carry `tenant_id`; one tenant freeze must not deny others |

### First wiring (demo-honest)

1. **Enterprise RAG** — JWT Principal (ADR-0006) already supplies `tenant_id`; document that
   ingest writers in strict mode should match JWT tenant to body tenant (follow-up enforcement).
2. **Thin demo header** — Accept `X-Tenant-Id` only when it matches verified Principal tenant;
   mismatch → 403.
3. **FinOps** — Prefer `scope_type=tenant` budgets in consumer wiring docs (AegisLoop / AegisAI).

## Alternatives

| Option | Why rejected (for now) |
|--------|------------------------|
| Full Kubernetes network policies per tenant | Overkill for free-tier demos |
| Separate DB schema per tenant | Correct at scale; premature without dedicated DBs |
| Soft multi-tenancy via prompt prefixes | Security theater |

## Consequences

- Positive: Interview and review answers map cleanly to Network / Data / Quota / Blast-radius.
- Positive: Aligns with ADR-002 (access-before-ranking) and ADR-024 (`PRODUCTION_STRICT`).
- Negative: Demo mode still allows shared keys and body tenants — must stay labeled demo.
- Follow-up: Enforce ingest tenant=JWT tenant under strict; per-tenant rate limits in AegisAI.

## Related

- [ADR-002 Authorization before ranking](./ADR-002-authorization-before-ranking-rag.md)
- [ADR-024 PRODUCTION_STRICT](./ADR-024-production-strict-fail-closed.md)
- Enterprise RAG `principal_auth.py` / ADR-0006

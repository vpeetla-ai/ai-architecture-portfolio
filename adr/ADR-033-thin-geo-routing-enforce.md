# ADR-033: Thin geo enforce dimension on the routing contract

**Status:** Accepted  
**Date:** 2026-08-12  
**Systems:** aegis-routing-contract, aegis-llm-gateway, aegisai-enterprise-agent-platform (deny theater)

## In one breath (panel)

I'd add optional allowed-regions on the existing enforce plane — not a sovereign residency platform — so one EU demo tenant can get a real 403 without pretending we shipped a seven-hop envelope.

## Context

LinkedIn / Principal thesis: model routing is becoming model + geography. Org reality (ADR-029): apps select; gateway enforces data-class + verifier independence. Building the full geo-aware control plane (topology registry, signed route tokens, per-hop evidence) before a named demand signal is overbuild.

## Decision

1. Extend `aegis-routing-contract` with `InferenceGeo`, `X-Jurisdiction`, `X-Allowed-Regions`, `X-Inference-Geo`.
2. When `X-Allowed-Regions` is present, gateway denies if inferred/declared provider geo ∉ set (`geo_region_not_allowed`).
3. Without those headers, behavior is unchanged (geo inactive) — no silent residency claim.
4. Demo tenant pattern: `acme-eu` + `X-Allowed-Regions: eu,private` against global OpenAI → 403.
5. Control Room “Run deny probes” includes the geo case alongside confidential / verifier.

**Explicit non-goals (still thesis-only):** 7-hop residency envelope, topology registry, signed TTL route contracts, RAG index-region, tool action_region, planned-vs-actual trajectory comparator, geo KPIs.

## Consequences

**Positive**

- Carousel stays honest: thin enforce spike exists; full sovereign router does not.
- ADR-029 selection story preserved — apps still select; plane only enforces.

**Negative / work ahead**

- Provider→geo map is a stub; real regional endpoints need topology work later.
- Consumers must send headers; no automatic jurisdiction from tenant id alone (except demo probes).

## Links

- Contract: [aegis-routing-contract](https://github.com/vpeetla-ai/aegis-routing-contract)
- Parent: [ADR-029](ADR-029-app-owned-role-aware-routing-contract.md)
- Operator: AegisAI Control Room → LLM metrics → Model routing → Run deny probes

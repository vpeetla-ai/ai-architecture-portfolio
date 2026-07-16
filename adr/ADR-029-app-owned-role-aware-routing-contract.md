# ADR-029: App-owned role-aware routing + shared enforce/record contract

**Status:** Accepted  
**Date:** 2026-07-15  
**Systems:** aegis-routing-contract (new), aegis-llm-gateway, omniforge, venkat-ai-platform, ai-content-factory, domainforge-rag-peft, aegisai-enterprise-agent-platform, agent-finops

## Context

ADR-028 federated the LLM plane (gateway + semantic cache) separate from AegisAI tool governance. A Principal thesis asks for **role-aware model routing** (five roles, four tiers, verifier independence, sensitivity→private, cost per compliant outcome).

Risk: stuffing a **model selector** into `aegis-llm-gateway` would (a) fight app-local brains that already choose buckets, and (b) blur ADR-028’s thin-plane story.

## Decision

1. **Apps select** models (OmniForge Multi-LLM Brain, VAP router, ACF agent maps, DomainForge cascade, AegisAI knowledge path).
2. **`aegis-llm-gateway` enforces + records** — never becomes the system of record for selection.
3. Shared schemas live in a dedicated package: **`aegis-routing-contract`** (ThesisRole, DataClass, ModelTier, RoutingDecisionV2, header names, `enforce_routing_policy`).
4. Apps keep local agent names; map via `CONSUMER_AGENT_ROLE_MAPS` → ThesisRole.
5. Sensitivity is **DataClass** (not a sixth agent role). Owner/Admin is **IdentityPrincipal** for HITL/override.
6. Verifier bar: **provider ≠ generator provider**; confidential → private tier only (fail-closed).
7. Outcome KPI (FinOps): eval pass + no policy deny + HITL when required + budget/kill-switch clear.

## Consequences

- Gateway gains header parsing, policy denies (403), decision audit API — still no picker.
- Org consumers migrate headers over ~90 days; interview claim stays honest: “app-owned selection, plane-owned governance.”
- Affirms ADR-028; does not invert it.

## Links

- Package: `aegis-routing-contract`
- Parent: [ADR-028](ADR-028-federated-ai-control-plane-k8s-analogy.md)

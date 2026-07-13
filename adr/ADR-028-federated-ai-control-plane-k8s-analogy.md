# ADR-028: Federated AI control plane — “Kubernetes of AI” meaning

**Status:** Accepted  
**Date:** 2026-07-13  
**Systems:** aegis-llm-gateway (new), aegis-semantic-cache (new), aegisai-enterprise-agent-platform, agent-finops, golden-eval-registry, venkat-ai-platform, ai-content-factory, and consumers

## Context

LinkedIn / portfolio narrative compares an **AI Control Plane** to what Kubernetes did for cloud: operate and govern many workloads without replacing the underlying compute (here: foundation models).

Risks if unconstrained:

1. **Overclaim** — implying a single product with 99.9% SLO, full SSO federation, and WORM compliance.
2. **AegisAI monolith** — stuffing LLM proxy, semantic cache, registries, and FinOps into the tool-gateway repo until it becomes unmaintainable.
3. **Loose side projects** — per-repo demos without a shared plane look disconnected.

Prior art in-org: ADR-001 (orchestration vs governance), ADR-004 (tool gateway + HITL), ADR-011 (FinOps standalone), ADR-024 (`PRODUCTION_STRICT`), ADR-026 (multi-tenant isolation).

## Decision

### What “Kubernetes of AI” means for vpeetla-ai

| Means | Does **not** mean |
|-------|-------------------|
| Operate & govern agents, tools, and model calls through a **federated control plane** | Replace or own foundation models |
| Shared planes: tool gateway, LLM gateway, cache, FinOps, eval | One monolith named “Control Plane” |
| Logical multi-tenant isolation now | Hard multi-tenant SLAs / 99.9% uptime claims |
| Fail-closed **architecture** with fail-open **toggle** for demos | Fail-open forever in production posture |
| Interview + product proof on free tiers | SOC2 / enterprise IdP completeness |

Public line: *“K8s analogy = operate & govern, not replace models.”*  
Ship narrative when ready: *“Shipped the Enterprise LLM Gateway Plane.”* — not “full control plane complete.”

### Federated plane (explicit non-monolith)

| Plane | Repo / service | Owns |
|-------|----------------|------|
| Tool governance | `aegisai-enterprise-agent-platform` | Tool authz, HITL, signed audit, agent registry |
| **LLM gateway** | **`aegis-llm-gateway` (new)** | OpenAI-shaped proxy, routing, quotas, stub/BYOK |
| **Semantic cache** | **`aegis-semantic-cache` (new)** | Embed + similarity lookup; separate scale path |
| FinOps | `agent-finops` | Metering, budgets, breach |
| Eval contracts | `golden-eval-registry` | Golden fixtures / CI gates |
| Orchestration | `venkat-ai-platform` (+ apps) | Graphs, missions, products — **consumers** of planes |

**AegisAI must not absorb LLM proxy or semantic cache.** It may *authorize* sensitive LLM routes via a hook; it does not terminate model HTTP.

### Posture flag

- Architecture defaults to **fail-closed** semantics (deny when policy/metering/cache dependency required and unavailable).
- Runtime flag (e.g. `CONTROL_PLANE_MODE=strict|demo`) may **fail-open** for standard demo performance — documented, never silent.

### Identity & audit (portfolio bar)

- Service API keys + human JWT (Clerk free tier expand) — enough for this phase.
- Signed audit packets remain the audit story (no WORM requirement this phase).

### UX

- Keep per-repo demos.
- Add a **Control Room** (extend AegisAI control UI or thin `aegis-control-room`) with tabs: gateway latency, cache hit/miss, tenant namespaces, registry self-serve.
- Self-serve form creates **real** agent registry entries (AegisAI registry API).

## Consequences

- Clear ownership stops AegisAI from becoming unmaintainable.
- All LLM-calling apps migrate behind `aegis-llm-gateway` over multi-week blocks.
- Interview playbook gains an SD entry on **gateway vs sidecar** and **cache-as-service** tradeoffs.
- Honest LinkedIn: gateway plane shipped; full “K8s of AI” remains a multi-plane journey.

## Links

- Plan: [docs/plans/LLM_GATEWAY_PLANE.md](../docs/plans/LLM_GATEWAY_PLANE.md)
- Related: ADR-001, ADR-004, ADR-011, ADR-024, ADR-026

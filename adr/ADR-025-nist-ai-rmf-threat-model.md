# ADR-025: NIST AI RMF Threat Model Mapped to the Governed Stack

**Status:** Accepted  
**Date:** 2026-07-09  
**Scope:** AegisAI gateway, Enterprise RAG, golden-eval-registry, org `PRODUCTION_STRICT`

## In one breath (panel)

I'd map Govern / Map / Measure / Manage to the controls we actually ship — and refuse a "NIST Compliant" badge without a formal assessment.

## Context

Principal reviewers ask how the portfolio maps to [NIST AI RMF 1.0](https://www.nist.gov/itl/ai-risk-management-framework) — not whether demos "feel safe." Free-tier reference demos intentionally fail open for missing secrets ([ADR-005](./ADR-005-reference-stack-free-tier.md), [ADR-024](./ADR-024-production-strict-fail-closed.md)). That must not be confused with a production threat posture.

This ADR is the org's concise threat-model anchor: which controls exist today, where they live, and which free-tier gaps stay honest.

## Decision

Treat NIST AI RMF functions as the risk vocabulary, and bind each function to concrete stack controls — architecture evidence, not a paper GRC program.

| RMF function | Threat / concern | Control in this stack | Evidence |
|--------------|------------------|------------------------|----------|
| **Govern** | Ungoverned side effects; unclear ownership of agent actions | AegisAI gateway + HITL before publish/deploy/notify; signed audit; kill switch | ADR-001, ADR-004; AegisAI `POST /api/gateway/tool-request` |
| **Map** | Over-claimed "production-ready"; missing identity/access model | Access-before-ranking RAG; principal clearance/groups; orchestration ≠ governance split | ADR-002; Enterprise RAG `AccessPolicy` |
| **Measure** | Silent regression of retrieval, gates, or graph HITL | Versioned golden-eval-registry suites as CI merge gates | ADR-014; `golden-eval-registry` scorers |
| **Manage** | Demo fail-open shipped as prod; spoofed principals; fake dashboard activity | Org `PRODUCTION_STRICT` fail-closed; JWT principal in strict RAG; no synthetic monitor seed in prod mode | ADR-024; Enterprise RAG ADR-0006; AegisAI monitor policy |

### Minimum threat list (honest)

| Threat | Mitigated when | Residual on free-tier demo |
|--------|----------------|----------------------------|
| Tool call without policy/HITL | Gateway enabled + fail-closed | Gateway may be disabled; demos fail open unless `PRODUCTION_STRICT` |
| Unauthorized chunk in LLM context | Access filter before hybrid rank | Client-asserted principal in demo mode (body-level spoof possible) |
| Prompt injection / jailbreak retrieval | Adversarial golden suite + decline/guardrails | Heuristic guardrails only; no continuous red-team SOC |
| Eval drift / metric gaming | Locked suite manifests + CI checkout of registry | Not every consumer suite kind is wired yet |
| Fake "agents in motion" telemetry | Seed monitor disabled under `PRODUCTION_STRICT` | Seeded activity is intentional in demo defaults |
| Cold-start / rate-limit availability | Documented free-tier boundary (ADR-005) | Ops honesty only — not a security control |

### `PRODUCTION_STRICT` (cross-cutting Manage)

When `PRODUCTION_STRICT=true`, consumers prefer deny over demo convenience: gateway required, fail-open ignored, principal verified where implemented, synthetic monitor seeds off. Unset/`false` preserves portfolio demos.

### Alternatives refused

1. **Full enterprise threat-model spreadsheet** — too heavy for portfolio scope; goes stale
2. **Map only to OWASP LLM Top 10** — useful later; RMF is the common language for AI program reviews
3. **"NIST Compliant" badge** — dishonest without formal assessment

## Consequences

**Positive**

- One page reviewers can cite for RMF ↔ repo mapping
- Separates *architecture controls* (gateway, access-before-ranking, golden gates) from *deploy maturity* (free-tier cold starts, optional OPA)

**Negative**

- Does not claim full NIST AI RMF conformity assessment, continuous monitoring, or third-party audit
- Several Manage controls are still rolling out repo-by-repo (ACF first for gateway strictness; RAG JWT; AegisAI seed suppression)

## Related

- [ADR-001](./ADR-001-orchestration-vs-governance-split.md) · [ADR-002](./ADR-002-authorization-before-ranking-rag.md) · [ADR-004](./ADR-004-gateway-hitl-side-effects.md)
- [ADR-005](./ADR-005-reference-stack-free-tier.md) · [ADR-014](./ADR-014-golden-eval-registry-real-ci-gate.md) · [ADR-024](./ADR-024-production-strict-fail-closed.md)
- [Top-1% 90-day backlog](../docs/TOP1PCT_90DAY_BACKLOG.md) item **P2.2**

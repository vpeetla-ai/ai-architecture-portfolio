# ADR-024: Org-Wide `PRODUCTION_STRICT` Fail-Closed Profile

**Status:** Accepted  
**Date:** 2026-07-09  
**Systems:** All side-effect and access-control consumers (ACF first; VAP, LoopForge, Enterprise RAG, AegisLoop next)

## In one breath (panel)

I'd make demos fail open by default and production fail closed behind one org flag — so "gateway down → allow" can never be mistaken for the prod story.

## Context

Demo defaults across the org intentionally **fail open** when AegisAI, FinOps, or identity deps are missing — so reviewers can run pipelines without every secret. Correct for local/stub demos. Wrong if marketed as production-safe.

Principal reviewers dig for: "What happens when the gateway is down?" Too many clients answered "allow." That's the scar this ADR closes — without killing zero-config portfolio demos.

## Decision

One org-wide environment contract:

| Variable | Meaning |
|----------|---------|
| `PRODUCTION_STRICT=true` | Production honesty profile |
| unset / `false` | Demo / local profile (current defaults) |

### Behavior matrix

| Dependency | Demo (default) | `PRODUCTION_STRICT=true` |
|------------|----------------|--------------------------|
| AegisAI gateway URL missing / disabled | Allow side effect (`gateway_disabled`) | **Deny** — require configured + enabled gateway |
| Gateway HTTP error | Allow if `*_FAIL_OPEN=true` | **Deny** — force fail-closed (`*_FAIL_OPEN` ignored) |
| FinOps service missing | Local estimate / continue | Halt or deny metered dispatch (consumer-specific) |
| Principal identity | Client-asserted OK (documented) | Verified token only (Enterprise RAG P1.5) |

### First consumer (Implemented)

**AI Content Factory** publish path (`backend/app/integrations/aegis_gateway.py` + settings):

- `production_strict=True` ⇒ `aegisai_gateway_fail_open=False` (forced)
- Gateway not enabled ⇒ `GatewayAuthz` blocked with reason `production_strict_gateway_required`

### Alternatives refused

1. **Per-repo flags only** — reviewers can't remember N names
2. **Always fail-closed** — kills zero-config portfolio demos
3. **Separate "prod" deploy with different code** — dual codepaths drift

## Consequences

**Positive**

- One env flag reviewers can ask for; demos stay easy; prod claims become testable
- Aligns with [ADR-004](./ADR-004-gateway-hitl-side-effects.md) without breaking Render free-tier demos

**Negative**

- Operators must set secrets **and** `PRODUCTION_STRICT` together — missing either fails closed (that's the point)

**Follow-up (Planned):** Propagate to LoopForge git/PR, VAP notify, AegisLoop mission ship, Enterprise RAG Principal (backlog P2.5 / P1.5)

## Related

- [ADR-004 Gateway + HITL](./ADR-004-gateway-hitl-side-effects.md)
- [Top-1% 90-day backlog](../docs/TOP1PCT_90DAY_BACKLOG.md) item **P1.4**
- ACF: `backend/app/core/config.py`, `backend/app/integrations/aegis_gateway.py`

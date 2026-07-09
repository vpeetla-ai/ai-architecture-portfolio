# ADR-024: Org-Wide `PRODUCTION_STRICT` Fail-Closed Profile

**Status:** Accepted  
**Date:** 2026-07-09  
**Systems:** All side-effect and access-control consumers (ACF first; VAP, LoopForge, Enterprise RAG, AegisLoop next)

## Context

Demo defaults across the org intentionally **fail open** when AegisAI, FinOps, or identity dependencies are missing — so portfolio reviewers can run pipelines without every secret. That is correct for local/stub demos and wrong if marketed as production-safe.

Principal reviewers dig for: “What happens when the gateway is down?” Today many clients answer “allow.”

## Decision

Introduce an org-wide environment contract:

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

### First consumer

**AI Content Factory** publish path (`backend/app/integrations/aegis_gateway.py` + settings):

- `production_strict=True` ⇒ `aegisai_gateway_fail_open=False` (forced)
- Gateway not enabled ⇒ `GatewayAuthz` blocked with reason `production_strict_gateway_required`

## Consequences

- **Positive:** One env flag reviewers can ask for; demos stay easy; prod claims become testable.
- **Positive:** Aligns with ADR-004 (gateway before side effects) without breaking Render free-tier demos.
- **Negative:** Operators must set secrets + `PRODUCTION_STRICT` together — missing either fails closed.
- **Follow-up:** Propagate to LoopForge git/PR, VAP notify, AegisLoop mission ship, Enterprise RAG Principal (backlog P2.5 / P1.5).

## Alternatives considered

1. **Per-repo flags only** — rejected; reviewers cannot remember N names.
2. **Always fail-closed** — rejected; kills zero-config portfolio demos.
3. **Separate “prod” deploy with different code** — rejected; dual codepaths drift.

## Related

- [ADR-004 Gateway + HITL](./ADR-004-gateway-hitl-side-effects.md)
- [Top-1% 90-day backlog](../docs/TOP1PCT_90DAY_BACKLOG.md) item **P1.4**
- ACF: `backend/app/core/config.py`, `backend/app/integrations/aegis_gateway.py`

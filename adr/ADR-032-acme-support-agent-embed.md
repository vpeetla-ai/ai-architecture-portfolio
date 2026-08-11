# ADR-032: Acme Support Agent Embed (FDE wedge on the spine)

## Status

Accepted — 2026-08-11

## In one breath (panel)

I'd prove FDE fit with one named customer embed — Acme support triage — on the existing spine, not by inventing a thirteenth SaaS product.

## Context

The public stack already shows governance (AegisAI), orchestration (VAP), access-aware RAG, FinOps, and evals. FDE panels still ask for identity (SSO/SCIM), inbound events, connector recovery, tenant health, and commercial metering. Inventing “CustomerOS” would dilute the Principal brand and violate ADR-030 (method over mega-product).

## Decision

Ship a **90-day Acme Support Agent Embed** as an inspectable wedge:

1. **Host on the spine** — AegisAI (identity, webhooks, connectors, HITL, health), Enterprise RAG Strict (knowledge), agent-finops (tenant meters + Stripe test), VAP (orchestration), portfolio `/fde` (runbook).
2. **Named path** — retrieve policy → draft reply → Slack notify / Salesforce case → HITL on irreversible actions → per-tenant meter.
3. **Demo vs Strict labeled** — public Free demos stay honesty-labeled; panel path uses Strict local/Render Starter + real IdP (Auth0/Okta) where possible.
4. **Refuse** — HubSpot/GWS full packs (adapter contract only); SOC2 attestation claims; fake customer logos; soft tenancy sold as Postgres RLS.

### Evidence classes

| Claim | Class |
|-------|--------|
| Open repos, CI gates, live Strict health | **O** |
| Auth0/Okta/Slack/Salesforce/Stripe **test** wiring | **O** when live; else **H** until configured |
| Lucid embed outcomes | **P** / Contextual — not this wedge |

## Implementation map (2026-08)

| Seam | Location |
|------|----------|
| SAML ACS + OIDC tenant claim | AegisAI `saml_acs.py`, `auth.py`, `oidc_jwks.py` |
| SCIM Users/Groups | AegisAI `/scim/v2/*` → `IdentityRBACService` |
| Webhooks HMAC/DLQ | AegisAI `webhook_engine.py` + `/api/webhooks/*` |
| Slack retry/DLQ | `notifications/delivery.py` |
| Salesforce Case | `connectors/salesforce_case.py` |
| Tenant health + TTFV | `tenant_ops.py` + Control Room `tenant-health` |
| Stripe test meters | agent-finops `stripe_meters.py` |
| PII shared | ERAG `guardrails.redact_pii` + AegisAI `pii_middleware.py` |
| One-click | `scripts/embed_acme_up.sh` / `embed_acme_down.sh` |
| Public surface | portfolio `/fde` Embed lab + this case study |

## Consequences

**Positive**

- Maps the twelve FDE checklist themes to Demonstrated artifacts without a sixth platform
- Preserves Principal hire headline; wedge lives under `/fde` + this ADR

**Negative / honest limits**

- Stripe = test mode only; HubSpot/GWS = adapter contract
- Webhook DLQ is process-memory on Demo; durable queue is Phase-2
- Strict Render twin may be undeployed — use local Strict + receipt script
- Tenancy = verified `tenant_id` + blast-radius kill-switch, **not** Postgres RLS

## Related

- ADR-026, ADR-030, ADR-031
- Case study: [acme-support-agent-embed.md](../case-studies/acme-support-agent-embed.md)
- Panel rubric: [ACME_EMBED_PANEL_RUBRIC.md](../docs/ACME_EMBED_PANEL_RUBRIC.md)
- Prior: [ADR-026](./ADR-026-multi-tenant-isolation.md) · [ADR-030](./ADR-030-fde-field-method-portfolio-proof.md)
- Live: https://venkat-ai.com/fde

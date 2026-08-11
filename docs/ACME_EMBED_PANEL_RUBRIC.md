# Acme Support Agent Embed — 20-minute panel rubric

**Goal:** Break a fake-customer embed before booking a loop. Demo vs Strict labeled.

**Wedge:** Support triage — retrieve policy → draft → Slack / Salesforce case → HITL → tenant meter.

## Script (~20 min)

| Min | Move | Pass if |
|-----|------|---------|
| 0–2 | Open `/fde` Embed lab + ADR-032 scope | Principal brand intact; no sixth platform claim |
| 2–5 | SSO: OIDC or SAML login to AegisAI | Principal/tenant from IdP claims |
| 5–7 | SCIM: show user/group provisioned | Create/update/deactivate path exists |
| 7–10 | Strict ERAG ask with citations | Access-before-ranking; spoof tenant → 403 |
| 10–13 | Slack notify; force failure → DLQ → replay | HMAC/idempotency; failure surfaced |
| 13–15 | Salesforce case create (sandbox) | OAuth + retry policy; not a silent stub |
| 15–17 | Tenant health + FinOps budget | One-tenant freeze; Stripe **test** invoice preview |
| 17–20 | Evidence pack + post-mortem template | IR artifact + customer-comms playbook |

## Break tests (must fail closed)

1. Body `tenant_id=attacker` under Strict while JWT says `acme` → **403**
2. Webhook with bad HMAC → **401/403**, no side effect
3. Slack upstream 500 → lands in **DLQ**, replayable
4. FinOps budget breach → **halt that tenant only**

## Honesty labels

| Surface | Label |
|---------|--------|
| Public Free Render | Demo — cold starts OK |
| Panel Strict | Strict-local or Starter twin |
| Stripe | Test mode only |
| HubSpot/GWS | Out of scope — adapter contract |

## Exit

If any break test is theater, stop and fix before claiming Demonstrated on the FDE checklist map.

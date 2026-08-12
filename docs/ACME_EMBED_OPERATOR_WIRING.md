# Acme Support Agent Embed — operator wiring

**Audience:** You (or a panel prep operator) configuring **live** IdP / Slack / Salesforce / Stripe test / Strict ERAG so the [20-minute panel rubric](./ACME_EMBED_PANEL_RUBRIC.md) is not theater.

**Code wedge:** ADR-032 · AegisAI · Enterprise RAG · agent-finops · [venkat-ai.com/fde](https://venkat-ai.com/fde)

**Honesty:** This guide wires **dev/free/sandbox/test** tenants only. Do not use live Stripe keys (`sk_live_*` is refused). HubSpot / Google Workspace remain [adapter contract only](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform/blob/main/docs/ADAPTER_CONTRACT_HUBSPOT_GWS.md).

---


## Zero-narration probe (code path)

Against a running AegisAI API:

```bash
export AEGISAI_URL=https://aegisai-api.onrender.com  # or local
./scripts/probe_acme_embed_panel.sh
# expect: acme_embed_probe_ok=true
```

Script lives in `aegisai-enterprise-agent-platform/scripts/`. Env templates: `./scripts/embed_acme_up.sh` (not live vendor wiring).

Model-plane deny theater (separate from tool glass-box): AegisAI Control Room → LLM metrics → Model routing → **Run deny probes** (ADR-029 + ADR-033).

## Where secrets live

| Concern | Put secrets in | Repo / surface |
|---------|----------------|----------------|
| AegisAI API | Render env **or** local `.embed-acme/aegisai.env` | `aegisai-enterprise-agent-platform` |
| FinOps + Stripe test | Render env **or** `.embed-acme/finops.env` | `agent-finops` |
| ERAG Strict | Render Strict service **or** local Strict | `enterprise_rag_platform` |
| Portfolio `/fde` | No secrets — links only | `venkat-ai-portfolio` |

Bring-up templates:

```bash
cd aegisai-enterprise-agent-platform
./scripts/embed_acme_up.sh          # writes .embed-acme/*.env (gitignored locally)
# Edit those files with real values from this guide, then:
set -a; source .embed-acme/aegisai.env; set +a
```

Teardown: `./scripts/embed_acme_down.sh`

---

## Quick map (what → where → env)

| Dependency | Dashboard | Primary env vars | Verify |
|------------|-----------|------------------|--------|
| **OIDC** | Auth0 or Okta free/dev | `AEGISAI_AUTH_MODE=oidc`, `AEGISAI_OIDC_ISSUER`, optional `AEGISAI_OIDC_JWKS_URI`, `AEGISAI_OIDC_AUDIENCE`, `AEGISAI_ENFORCE_AUTH=true` | `GET /api/auth/posture` → `jwks_verification: true` |
| **SAML** | Same IdP SAML app ACS | ACS URL → `POST {AegisAI}/api/auth/saml/acs`; optional `AEGISAI_SAML_SUCCESS_REDIRECT` | Browser IdP login **or** panel mode (below) |
| **SCIM** | IdP SCIM provisioning | Base URL `{AegisAI}/scim/v2`; Bearer / gateway auth as configured | `POST /scim/v2/Users` → user in `GET /api/identity/posture` |
| **Webhooks HMAC** | (internal) | `AEGISAI_WEBHOOK_HMAC_SECRET` | Bad sig → `401` on `POST /api/webhooks/ingest` |
| **Slack** | Slack app Incoming Webhook | `SLACK_APPROVAL_WEBHOOK_URL` | Deliver markdown; `SLACK_FORCE_FAIL=true` → DLQ |
| **Salesforce** | Scratch/sandbox + Connected App | `SALESFORCE_INSTANCE_URL`, `SALESFORCE_ACCESS_TOKEN` | Case create; unset → labeled `sandbox-sim` |
| **FinOps tenant budget** | agent-finops service | `AGENTFINOPS_API_URL`, `AGENTFINOPS_API_KEY` | `PUT /v1/budget/tenant/acme` then breach |
| **Stripe test** | Stripe Dashboard → test mode | `STRIPE_API_KEY=sk_test_…`, optional `STRIPE_METER_MIRROR=true` | `GET /v1/billing/stripe/invoice-preview/acme` |
| **ERAG Strict** | Render Starter twin **or** local | `PRODUCTION_STRICT=true`, `RAG_JWT_SECRET` | `/health` → `review_mode=strict`; spoof tenant → 403 |

---

## 1. Identity — Auth0 or Okta (OIDC + SAML + SCIM)

### 1.1 Create the tenant

1. Sign up: [Auth0](https://auth0.com/) free **or** [Okta Developer](https://developer.okta.com/).
2. Create an application for **AegisAI API** (OIDC) and optionally a **SAML** app for browser ACS.

### 1.2 OIDC (API Bearer / JWKS)

**Where to click**

- Auth0: Applications → your app → Settings → Domain, Audience (API).
- Okta: Security → API → Authorization Servers → Issuer URI; Applications → Client.

**Add to AegisAI (Render → Environment, or `.embed-acme/aegisai.env`)**

```bash
AEGISAI_AUTH_MODE=oidc
AEGISAI_ENFORCE_AUTH=true
AEGISAI_OIDC_ISSUER=https://YOUR_TENANT.auth0.com/   # or Okta issuer
# Optional if JWKS is not at {issuer}/.well-known/jwks.json:
AEGISAI_OIDC_JWKS_URI=https://YOUR_TENANT.auth0.com/.well-known/jwks.json
AEGISAI_OIDC_AUDIENCE=https://aegisai.api   # must match token aud if set
```

**Claim mapping (panel)**

| Claim | Used as |
|-------|---------|
| `sub` / `email` | `principal_id` |
| `groups` / `roles` | RBAC roles |
| `tenant_id` / `tid` / `org_id` | **wins over** spoofable `X-AegisAI-Tenant` |

**Verify**

```bash
curl -sS "$AEGISAI_URL/api/auth/posture" | jq .
# Call a gated route with Authorization: Bearer <access_token>
```

### 1.3 SAML ACS (browser login)

**ACS URL (configure in IdP SAML app)**

```text
https://<aegisai-host>/api/auth/saml/acs
```

Metadata helper: `GET /api/auth/saml/metadata`

**Env**

```bash
AEGISAI_SAML_DEFAULT_TENANT=acme
AEGISAI_SAML_ACS_SECRET=<long-random>          # signs session tokens
AEGISAI_SAML_SUCCESS_REDIRECT=https://<web>/   # optional; appends ?saml_session=
# Leave panel mode OFF when IdP posts real SAMLResponse:
AEGISAI_SAML_PANEL_MODE=false
```

**Panel fallback (no IdP yet — labeled)**

```bash
AEGISAI_SAML_PANEL_MODE=true
curl -sS -X POST "$AEGISAI_URL/api/auth/saml/acs" \
  -d 'principal_id=acme.sso@example.com&tenant_id=acme&roles=workflow_owner,reviewer'
# Use X-AegisAI-SAML-Session: <session_token> on later calls
```

Do **not** claim unlabeled “SSO done” while only panel mode is on.

### 1.4 SCIM Users / Groups

**IdP SCIM connector**

| Field | Value |
|-------|--------|
| Base URL | `https://<aegisai-host>/scim/v2` |
| Users | `/Users` |
| Groups | `/Groups` |
| Auth | Same as AegisAI mutating APIs (Bearer / gateway); for demos use control-plane headers if enforcement is off |

**Manual smoke**

```bash
curl -sS -X POST "$AEGISAI_URL/scim/v2/Users" \
  -H 'Content-Type: application/json' \
  -H 'X-AegisAI-Tenant: acme' \
  -H 'X-AegisAI-Principal: control-plane-admin' \
  -H 'X-AegisAI-Roles: admin' \
  -d '{"userName":"acme.analyst@example.com","tenantId":"acme","roles":["workflow_owner","reviewer"]}'
```

User should appear under `GET /api/identity/posture` and `GET /scim/v2/Users`.

---

## 2. Webhooks (HMAC + DLQ)

**Where:** AegisAI only (no external vendor).

```bash
AEGISAI_WEBHOOK_HMAC_SECRET=<shared-secret>   # same value used by senders
```

**Sign body** (Python): `hmac_sha256("sha256=" + hex(hmac(secret, raw_body)))` — see `WebhookEngine.sign_body`.

**Ingest**

```bash
# Reject (break test)
curl -sS -o /dev/null -w '%{http_code}\n' -X POST "$AEGISAI_URL/api/webhooks/ingest" \
  -H 'Content-Type: application/json' \
  -H 'X-AegisAI-Signature: sha256=deadbeef' \
  -d '{"webhook_id":"slack.interaction","tenant_id":"acme","payload":{"text":"x"}}'
# expect 401

# DLQ list / replay
curl -sS "$AEGISAI_URL/api/webhooks/dlq?tenant_id=acme"
curl -sS -X POST "$AEGISAI_URL/api/webhooks/<delivery_id>/replay" \
  -H 'X-AegisAI-Principal: control-plane-admin' -H 'X-AegisAI-Roles: admin'
```

Slack interactions can reuse webhook id `slack.interaction`.

---

## 3. Slack connector

### 3.1 Create Incoming Webhook

1. [api.slack.com/apps](https://api.slack.com/apps) → Create App → Incoming Webhooks → Activate.
2. Add webhook to `#acme-embed` (or similar).
3. Copy webhook URL.

### 3.2 Env (AegisAI)

```bash
SLACK_APPROVAL_WEBHOOK_URL=https://hooks.slack.com/services/...
# Optional channel label for HITL copy:
SLACK_APPROVAL_CHANNEL=#acme-embed
```

### 3.3 Failure drill

```bash
export SLACK_FORCE_FAIL=true   # process env for AegisAI API
# Trigger notify / delivery → lands in DLQ
curl -sS "$AEGISAI_URL/api/notifications/slack/dlq"
# Clear force flag, then:
curl -sS -X POST "$AEGISAI_URL/api/notifications/slack/dlq/replay?index=0" \
  -H 'X-AegisAI-Principal: control-plane-admin' -H 'X-AegisAI-Roles: admin'
```

---

## 4. Salesforce Case (sandbox)

### 4.1 Sandbox / scratch org

1. Enable a Developer Edition or scratch org.
2. Create a Connected App (OAuth) **or** use a session access token for panel day.
3. Confirm Case object create permission for the integration user.

### 4.2 Env (AegisAI)

```bash
SALESFORCE_INSTANCE_URL=https://your-domain.my.salesforce.com
SALESFORCE_ACCESS_TOKEN=<oauth_access_token>
# Optional:
SALESFORCE_API_VERSION=v59.0
```

**Without credentials:** connector returns `salesforce://sandbox-sim/...` with an explicit message — fine for code demos, **not** a live panel Salesforce claim.

### 4.3 Failure drill

```bash
SALESFORCE_FORCE_FAIL=true   # forces retry exhaustion
```

---

## 5. FinOps tenant budgets + Stripe test meters

### 5.1 Point AegisAI at FinOps

```bash
# On AegisAI
AGENTFINOPS_API_URL=https://agent-finops-api.onrender.com   # or local
AGENTFINOPS_API_KEY=<if set on FinOps>
```

### 5.2 Seed a low tenant budget (panel break)

```bash
curl -sS -X PUT "$FINOPS_URL/v1/budget/tenant/acme" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $AGENTFINOPS_API_KEY" \
  -d '{"budget_usd": 0.01}'

curl -sS "$AEGISAI_URL/api/tenants/acme/budget/preflight"
# After usage exceeds budget → breached; kill-switch scope tenant=acme freezes one tenant only
```

### 5.3 Stripe test mode (no live charges)

**Where:** [Stripe Dashboard](https://dashboard.stripe.com/) → toggle **Test mode** → Developers → API keys → Secret key `sk_test_…`.

Optional: Billing → Meters → create meter event name (default code expects `acme_llm_cost_millicents` or set `STRIPE_METER_EVENT_NAME`).

**On agent-finops**

```bash
STRIPE_API_KEY=sk_test_...
STRIPE_METER_LOCAL=true
STRIPE_METER_MIRROR=true          # mirror tenant usage records into meter events
STRIPE_METER_EVENT_NAME=acme_llm_cost_millicents
# Optional map: tenant → Stripe customer id
STRIPE_TENANT_CUSTOMER_MAP=acme:cus_test_acme
```

**Verify**

```bash
curl -sS -X POST "$FINOPS_URL/v1/billing/stripe/meter" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $AGENTFINOPS_API_KEY" \
  -d '{"tenant_id":"acme","value":1500}'

curl -sS "$FINOPS_URL/v1/billing/stripe/invoice-preview/acme"
```

`sk_live_*` is refused by design.

---

## 6. Enterprise RAG Strict twin

### 6.A Local (fastest for panels)

```bash
cd enterprise_rag_platform
./scripts/run_strict_local.sh
# or follow docs/STRICT_PANEL_PACK.md
export RAG_JWT_SECRET=...
python3 scripts/mint_panel_jwt.py   # default tenant_id=acme
./scripts/capture_strict_panel_receipt.sh
```

### 6.B Render Starter twin

```bash
cd enterprise_rag_platform
./scripts/setup_strict_render.sh    # prints dashboard steps + generates RAG_JWT_SECRET
```

| Setting | Value |
|---------|--------|
| Service | `enterprise-rag-api-strict` (see `render.yaml`) |
| Plan | **Starter** (Free cold-starts kill panels) |
| Env | `PRODUCTION_STRICT=true`, `RAG_JWT_SECRET=…` |
| Health | `GET /health` → `review_mode=strict`, `principal_source=jwt` |

**Break test:** JWT tenant `acme` + body `tenant_id=attacker` → **403**.

If the Strict host still returns host-level 404, it is **undeployed** — use local Strict and say so on `/fde` / spine-health.

---

## 7. Tenant health UI + onboarding TTFV

No extra vendor. After AegisAI is up:

| Surface | URL |
|---------|-----|
| API health | `GET /api/tenants/acme/health` |
| Onboarding | `POST /api/tenants/acme/onboarding/start` then `…/complete-step` |
| Control Room | `?view=product&module=tenant-health` |

Deep link example: `https://<aegisai-web>/?view=product&module=tenant-health`

---

## 8. Incident pack

```bash
curl -sS "$AEGISAI_URL/api/incidents/acme/case-drill-webhook/playbook" | jq .
# post_mortem_markdown + customer_comms_markdown + evidence_pack
```

Drill narrative: `aegisai-enterprise-agent-platform/docs/artifacts/acme-ir-drill-webhook-budget.md`

---

## 9. Automated harness (no externals required)

CI / pre-panel self-check without IdP or Slack:

```bash
cd aegisai-enterprise-agent-platform
GOLDEN_EVAL_REGISTRY_PATH=../golden-eval-registry \
  python scripts/run_acme_embed_harness.py --score
# expect passed: true (acme.embed_invariant_v1)
```

Suite: `golden-eval-registry/suites/acme_embed_invariant_v1/`

---

## Panel-day checklist (copy/paste)

- [ ] AegisAI + FinOps + Strict ERAG healthy
- [ ] OIDC JWKS green **or** SAML ACS + labeled panel mode documented
- [ ] SCIM user `acme.*` visible in identity posture
- [ ] Strict spoof-tenant → 403
- [ ] Bad webhook HMAC → 401
- [ ] Slack force-fail → DLQ → replay
- [ ] Salesforce Case **or** honest sandbox-sim label
- [ ] Tenant budget breach freezes **acme** only
- [ ] Stripe invoice preview (test mode)
- [ ] Evidence / post-mortem playbook JSON
- [ ] `/fde` Embed lab + ADR-032 open in browser

Rollback: `./scripts/embed_acme_down.sh` · activate tenant kill-switch · restore previous Render env.

---

## Related docs

| Doc | Repo |
|-----|------|
| [ADR-032](../adr/ADR-032-acme-support-agent-embed.md) | ai-architecture-portfolio |
| [Panel rubric](./ACME_EMBED_PANEL_RUBRIC.md) | ai-architecture-portfolio |
| [Case study](../case-studies/acme-support-agent-embed.md) | ai-architecture-portfolio |
| `scripts/embed_acme_up.sh` | aegisai-enterprise-agent-platform |
| `docs/STRICT_PANEL_PACK.md` | enterprise_rag_platform |
| `docs/ADAPTER_CONTRACT_HUBSPOT_GWS.md` | aegisai-enterprise-agent-platform |

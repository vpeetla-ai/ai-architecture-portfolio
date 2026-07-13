# Flagship plan: Enterprise LLM Gateway Plane

**Status:** Draft → execute in multi-week blocks  
**Narrative when done:** “Shipped the Enterprise LLM Gateway Plane.”  
**Governing ADR:** [ADR-028](../../adr/ADR-028-federated-ai-control-plane-k8s-analogy.md)

## Suggested top 3 (this flagship)

| Rank | Workstream | Why |
|------|------------|-----|
| **1** | `aegis-llm-gateway` + `aegis-semantic-cache` | Closes the biggest gap between LinkedIn claim and repos; shared by all LLM apps |
| **2** | Logical multi-tenant + fail-closed architecture / fail-open toggle | Portfolio-credible isolation without fake 99.9% SLO |
| **3** | Control Room + self-serve registry onboarding | Turns federated services into one “platform” glance for interviewers |

**Explicitly later / out of this flagship:** enterprise Okta SSO, WORM audit, GPU capacity ops, training-data provenance, claiming full “K8s of AI complete.”

**Hard constraint:** Do not grow AegisAI into an LLM proxy (fear #25).

---

## Target architecture

```text
Apps (VAP, ACF, Sentinel, DomainForge, OmniForge, …)
        │  OpenAI-shaped HTTPS
        ▼
┌───────────────────────────┐
│  aegis-llm-gateway        │  routing · quotas · stub/BYOK · tenant header
└───────────┬───────────────┘
            │ cache lookup / store
            ▼
┌───────────────────────────┐
│  aegis-semantic-cache     │  Redis + embed (Qdrant or Redis vector) · free tiers
└───────────────────────────┘
            │ meter / budget check
            ▼
┌───────────────────────────┐
│  agent-finops             │  existing
└───────────────────────────┘
            │ optional policy hook (sensitive routes)
            ▼
┌───────────────────────────┐
│  AegisAI                  │  tool gateway + HITL + agent registry (unchanged core)
└───────────────────────────┘
            │
            ▼
     Foundation model APIs (only when BYOK / live mode)
```

**Tenancy:** logical isolation now — `X-Tenant-Id` (or JWT `tid`) namespaces cache keys, quotas, and FinOps meters. Shared infra; no hard cell-per-tenant yet.

**Modes:**

| Mode | Behavior |
|------|----------|
| `stub` (default) | Deterministic responses; cache still records hits/misses on stub corpus |
| `byok` | User/session key; live providers; FinOps meters real tokens |
| `strict` | Fail-closed if FinOps/cache/policy required and down |
| `demo` | Fail-open for latency demos — flagged in UI |

---

## New repos

### 1. `aegis-llm-gateway`

- FastAPI · Python 3.11+
- `POST /v1/chat/completions` (+ optional `/v1/embeddings` passthrough)
- Router: model alias → provider cascade (stub | Groq | OpenAI | Anthropic)
- Quotas per tenant (RPM/TPM soft limits)
- Calls semantic-cache before provider; writes on miss
- Emits usage to agent-finops
- Optional: call AegisAI only for tagged high-risk routes (not every token)
- UI: thin health + Control Room embed metrics API
- `render.yaml` + Vercel metrics strip if needed

### 2. `aegis-semantic-cache`

- Separate service (scale independently from gateway)
- API: `Lookup(tenant, model, messages_hash_or_embedding)` / `Store(...)`
- Redis Cloud free tier for KV + TTL; Qdrant Cloud free for vector similarity (or Redis vector if simpler on free tier — pick one in Block 0 spike)
- Similarity threshold configurable; never cache across tenants
- Metrics: hit rate, p95 lookup, eviction

---

## Control Room + self-serve

**Where:** extend AegisAI control-plane UI (preferred — already “Monitor → Govern → Remediate”) with new tabs that **read** gateway/cache/finops APIs — do not move LLM proxy code into AegisAI.

**Tabs:**

1. Gateway — latency, error rate, stub vs BYOK mix  
2. Cache — hit/miss, tenant breakdown  
3. Tenants — logical namespaces, quota usage  
4. Registry — **self-serve form** → `POST` real agent registry entries  

Per-repo demos stay; each adds a one-liner: “LLM via aegis-llm-gateway.”

---

## Consumer migration order

| Order | App | Notes |
|-------|-----|-------|
| 1 | VAP | Highest interview leverage; multi-LLM already exists |
| 2 | ACF | Publish path already gateway-aware for tools |
| 3 | Sentinel | Single LLM summarize path — easy |
| 4 | DomainForge | Triage LLM calls |
| 5 | OmniForge | Keep self-contained fallback; prefer gateway when configured |
| 6 | VoiceForge / others | After core five stable |

Each migration: env `LLM_GATEWAY_URL` + feature flag; rollback = direct provider.

---

## Interview / playbook

Add SD entry (cloud or AI system design):

**“Design an enterprise LLM gateway with semantic cache — gateway vs sidecar; cache-in-process vs cache-as-service.”**

Must cover: tenancy keying, poisoning, TTL vs invalidation, fail-closed vs fail-open, FinOps metering placement, when sidecar wins (edge/low-latency single app).

Wire Interview map on `aegis-llm-gateway` README when live.

---

## Multi-week block schedule (high-leverage)

### Block 0 — Decisions & spikes (3–5 days)

- [ ] Publish ADR-028  
- [ ] Spike Redis vs Qdrant-for-cache on free tier; pick one  
- [ ] Canonical Mermaid: federated plane + gateway sequence  
- [ ] Repo names finalized: `aegis-llm-gateway`, `aegis-semantic-cache`  
- [ ] Non-goals locked in README templates  

### Block 1 — Skeleton planes (1 week)

- [ ] Scaffold both repos (FastAPI, tests, `PRODUCTION_STRICT` / mode flags)  
- [ ] Stub-first completions; cache miss→store→hit path in tests  
- [ ] Logical tenant header enforced in cache keys  
- [ ] Deploy free-tier Render APIs + health  

### Block 2 — FinOps + strict/demo posture (3–5 days)

- [x] Meter stub path via agent-finops (`POST /v1/usage` + API key)  
- [x] Budget breach → fail-closed in `strict` (HTTP 402); FinOps down → 503  
- [x] Demo mode fail-open documented (`GET /v1/posture` + `demo/index.html`)  

### Block 3 — First consumer: VAP (1 week)

- [x] VAP routes chat/completions through gateway (`LLM_GATEWAY_URL` → `chat_llm_for_bucket`)  
- [x] Golden/smoke test: stub path green in CI (`tests/test_llm_gateway.py`)  
- [x] Ops metrics show gateway dependency (`extra.llm_gateway` on `/api/v1/ops/metrics`)  
- [x] Docs: `.env.example`, `docs/INFERENCE.md`, README status + Interview map  
 

### Block 4 — ACF + Sentinel (1 week)

- [x] Same migration pattern (`LLM_GATEWAY_URL` → OpenAI-compatible completions)  
- [x] Regression: HITL/tool gateway unchanged (ACF publish + Sentinel `email.send`)  
- [x] Ops metrics show `extra.llm_gateway`; docs + Interview map updated  
 

### Block 5 — DomainForge + OmniForge (1 week)

- [ ] Gateway optional with clear env  
- [ ] OmniForge: “self-contained OR plane-connected” honesty in README  

### Block 6 — Control Room + self-serve (1 week)

- [ ] AegisAI UI tabs for gateway/cache metrics  
- [ ] Self-serve registry form → real entries  
- [ ] Portfolio diagram update (CONTEXT + venkat-ai.com/work)  

### Block 7 — Playbook + narrative (2–3 days)

- [ ] New SD question + Arena rubrics bump  
- [ ] LinkedIn: “Shipped the Enterprise LLM Gateway Plane”  
- [ ] Interview map links on new repos  

---

## Success criteria

| Criterion | Bar |
|-----------|-----|
| All primary apps | Configurable to call gateway (default stub) |
| Cache | Cross-request hit demonstrable; tenant isolation tested |
| FinOps | Meter events for gateway traffic |
| AegisAI | No LLM proxy code landed in core gateway package |
| Honesty | No 99.9% SLO claim; ADR-028 published |
| Interview | New SD entry live; Control Room shows hit/miss |

## Non-goals (this flagship)

- Replacing AegisAI tool gateway  
- Okta/Azure AD federation  
- Claiming full Kubernetes-of-AI complete  
- Hard multi-tenant cells / GPU procurement platform  
- Absorbing semantic cache into the gateway process “for speed” as the only option (sidecar/in-process may be discussed in playbook; **org default is cache-as-service**)

---

## Open spikes (resolve in Block 0)

1. Redis-only vector vs Redis+Qdrant for free-tier semantic cache  
2. Control Room: tabs inside AegisAI UI vs tiny `aegis-control-room` shell  
3. Exact tenant claim source: header-only vs Clerk JWT `org_id`

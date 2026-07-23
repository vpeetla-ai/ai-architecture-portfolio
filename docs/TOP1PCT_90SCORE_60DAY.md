# Top-1% → 90/100 score plan (60 days · ~$45/mo)

**Status:** ACTIVE  
**Started:** 2026-07-22  
**Tracking issue:** [#14](https://github.com/vpeetla-ai/ai-architecture-portfolio/issues/14)  
**Parent:** [`TOP1PCT_90DAY_EXECUTION.md`](./TOP1PCT_90DAY_EXECUTION.md) · [`TOP1PCT_GAP_PLAN.md`](./TOP1PCT_GAP_PLAN.md)  
**North star score:** ≥90/100 (thesis · operating · signal)  
**Freeze:** no new product repos  
**Interim:** [RENDER_FREE_INTERIM.md](./RENDER_FREE_INTERIM.md) — Starters deferred ~1–2 days

## Locked decisions

| Decision | Choice |
|----------|--------|
| Timeline | 60 days |
| Budget | ~$45/mo total |
| Cloud | **Dual split:** AWS = AegisAI ephemeral; GCP = FinOps + ERAG Cloud Run. [CLOUD_FREE_TIER_SPLIT.md](./CLOUD_FREE_TIER_SPLIT.md) |
| Render | **Free for now** — Starter later (owner) |
| Strict ERAG | Local Docker / GCP Cloud Run now; Render Strict twin after Starter |
| Signal | Agent drafts; owner publishes within 48h |

## Budget (interim)

| Item | ~$/mo |
|------|------:|
| Render Free spine | 0 |
| GCP Cloud Run ERAG lite (idle) | ~0 |
| AWS/GCP receipt-day spike | 0–10 |
| Render Starters (later) | +21–28 |

## Phase checklist

### P0 — Always-on spine — **PARKED** (Starter deferred)

- [x] Idle probe script
- [x] Free-tier honesty docs ([RENDER_FREE_INTERIM.md](./RENDER_FREE_INTERIM.md))
- [ ] Render Starter applied *(owner in 1–2 days)*
- [ ] Idle ≥15m → 3× `/health` &lt;3s
- [ ] G1 closed

### P1 — Strict ERAG

- [x] Render Blueprint twin + panel pack
- [x] **Local Strict** `scripts/run_strict_local.sh`
- [x] **GCP Strict** vars in `deploy/gcp/cloudrun`
- [ ] Owner: run local or GCP Strict once; paste health snippet in receipts
- [ ] Later: Render Strict Starter URL live

### P2 — Dual-cloud receipts — **ACTIVE THIS WEEK**

- [x] Split doc + AWS/GCP case studies + ERAG Cloud Run path
- [x] `scripts/init_cloud_receipt.sh`
- [ ] Owner: one AWS **or** GCP receipt day

### P3 — Signal — **ACTIVE**

- [x] Substack pack + LinkedIn week pack + 10 ADR drafts
- [ ] Owner publishes

### P4 — Harden — **DONE (agent)**

- [x] ACF honesty · NIST · FinOps ROI · hire links

### P5 — Conversion

- [x] Mocks scheduled · outreach DRAFT_READY
- [ ] Owner: mocks + send outreach
- [ ] Keyed golden path after warm spine (or with patience on Free)

## Progress log

| Date | Phase | Note |
|------|-------|------|
| 2026-07-22 | — | Tracker created |
| 2026-07-22 | P0 | Idle verify FAIL on Free cold starts |
| 2026-07-22 | P2 | Dual-cloud split shipped |
| 2026-07-22 | — | **Owner: keep Render Free for now; Starter in 1–2 days** — P0 parked; cloud+Strict local/GCP+signal active |

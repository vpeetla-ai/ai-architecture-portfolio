# Top-1% → 90/100 score plan (60 days · ~$45/mo)

**Status:** ACTIVE  
**Started:** 2026-07-22  
**Tracking issue:** [#14](https://github.com/vpeetla-ai/ai-architecture-portfolio/issues/14)  
**Parent:** [`TOP1PCT_90DAY_EXECUTION.md`](./TOP1PCT_90DAY_EXECUTION.md) · [`TOP1PCT_GAP_PLAN.md`](./TOP1PCT_GAP_PLAN.md)  
**North star score:** ≥90/100 (thesis · operating · signal)  
**Freeze:** no new product repos

## Locked decisions

| Decision | Choice |
|----------|--------|
| Timeline | 60 days |
| Budget | ~$45/mo total |
| Cloud | **Dual split:** AWS = AegisAI ephemeral control plane; GCP = FinOps + ERAG Cloud Run (Always Free–friendly). Render = warm spine. [CLOUD_FREE_TIER_SPLIT.md](./CLOUD_FREE_TIER_SPLIT.md) |
| Strict ERAG | Dual URL: Demo Starter + Strict Starter |
| Signal | Agent drafts; owner publishes within 48h |

## Budget

| Item | ~$/mo |
|------|------:|
| vap-api + aegisai-api + enterprise-rag-api Starter | 21 |
| enterprise-rag-api-strict Starter | 7 |
| GCP Cloud Run ERAG lite (idle scale-to-zero) | ~0 |
| AWS/GCP receipt-day spike (destroy same day) | 0–10 |
| LLM keys remainder | rest |

## Phase checklist (strike when exit met)

### P0 — Always-on spine

- [x] Idle probe script: [`scripts/probe_spine_idle.sh`](../scripts/probe_spine_idle.sh)
- [ ] Render Starter applied: `vap-api`, `aegisai-api`, `enterprise-rag-api` *(owner dashboard — MCP list_workspaces unauthorized)*
- [ ] Idle ≥15m → 3× `/health` &lt;3s each
- [ ] `/api/spine-health` warmOk 3/3 after idle
- [ ] G1 closed in gap plan

**Idle verify 2026-07-22T20:36Z FAIL:** sample1 vap=41s · aegisai=23s · erag=21s (then warm). Free-tier spin-down still active — confirm Render **Instance type = Starter** (not Free) on all three.

### P1 — Live Strict ERAG

- [x] `enterprise-rag-api-strict` in [`enterprise_rag_platform/render.yaml`](https://github.com/vpeetla-ai/enterprise_rag_platform/blob/main/render.yaml)
- [x] JWT mint script + [`STRICT_PANEL_PACK.md`](https://github.com/vpeetla-ai/enterprise_rag_platform/blob/main/docs/STRICT_PANEL_PACK.md)
- [x] Portfolio technical-review + spine-health Strict links
- [ ] Owner: Blueprint sync / create Strict service + set `RAG_JWT_SECRET`
- [ ] Strict `/health` → `review_mode=strict` live
- [ ] Body-spoof rejected under Strict (live verify)

### P2 — Dual-cloud free-tier receipts

- [x] [CLOUD_FREE_TIER_SPLIT.md](./CLOUD_FREE_TIER_SPLIT.md) — AWS vs GCP assignment
- [x] AWS case study + runbook; GCP case study + runbook
- [x] ERAG `deploy/gcp/cloudrun` Always Free–friendly path
- [x] Hire links for AWS + GCP + split doc
- [ ] Owner: one AWS **or** GCP receipt day; files under `docs/artifacts/aws-receipts/` or `gcp-receipts/`

### P3 — Signal

- [x] Substack publish pack [`P3_SUBSTACK_PUBLISH_PACK.md`](./P3_SUBSTACK_PUBLISH_PACK.md)
- [x] ≥8 ADR post drafts (posts 1–10 in calendar)
- [ ] Owner publishes (URLs recorded here)

### P4 — Harden

- [x] ACF / GOLDEN_PATH honest publish boundary
- [x] NIST one-pager
- [x] FinOps ROI one-pager
- [x] Hire signal links (NIST · FinOps ROI · AWS · GCP · cloud split)

### P5 — Conversion + rescore

- [x] 3 mock sessions **scheduled** with protocols
- [x] ≥10 outreach rows `DRAFT_READY`
- [ ] Keyed golden path re-run on warm spine (owner keys)
- [x] Skills audit canvas updated with path-to-90 scores
- [ ] Owner: complete mocks + send outreach + publish Substack

## Progress log

| Date | Phase | Note |
|------|-------|------|
| 2026-07-22 | — | Tracker created; implementation started |
| 2026-07-22 | P0–P5 | Agent deliverables shipped across portfolio / ERAG / venkat-ai-portfolio; owner actions listed above |
| 2026-07-22 | P0 | **VERIFY FAIL** after owner "done": idle ≥16m sample1 vap=41.3s aegisai=22.7s erag=21.3s; samples 2–3 warm. Starter instance type not effective yet. Strict twin 404. |
| 2026-07-22 | P1 | setup_strict_render.sh helper added; live Strict still pending dashboard create |
| 2026-07-22 | P2 | aws-receipts/ README scaffold |
| 2026-07-22 | P2 | Dual-cloud split: AWS=AegisAI ephemeral; GCP=FinOps+ERAG Cloud Run; plan updated |

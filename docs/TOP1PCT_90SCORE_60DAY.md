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
| Cloud | AWS free-tier receipts (tear-down), not always-on EKS |
| Strict ERAG | Dual URL: Demo Starter + Strict Starter |
| Signal | Agent drafts; owner publishes within 48h |

## Budget

| Item | ~$/mo |
|------|------:|
| vap-api + aegisai-api + enterprise-rag-api Starter | 21 |
| enterprise-rag-api-strict Starter | 7 |
| AWS free-tier evidence (tear down) | 0–10 |
| LLM keys remainder | rest |

## Phase checklist (strike when exit met)

### P0 — Always-on spine

- [x] Idle probe script: [`scripts/probe_spine_idle.sh`](../scripts/probe_spine_idle.sh)
- [ ] Render Starter applied: `vap-api`, `aegisai-api`, `enterprise-rag-api` *(owner dashboard — MCP list_workspaces unauthorized)*
- [ ] Idle ≥15m → 3× `/health` &lt;3s each
- [ ] `/api/spine-health` warmOk 3/3 after idle
- [ ] G1 closed in gap plan

**Baseline 2026-07-22 (warm, not idle):** vap 0.14s · aegisai **4.7s** · erag 0.25s — starters likely partial; aegisai still over 3s budget.

### P1 — Live Strict ERAG

- [x] `enterprise-rag-api-strict` in [`enterprise_rag_platform/render.yaml`](https://github.com/vpeetla-ai/enterprise_rag_platform/blob/main/render.yaml)
- [x] JWT mint script + [`STRICT_PANEL_PACK.md`](https://github.com/vpeetla-ai/enterprise_rag_platform/blob/main/docs/STRICT_PANEL_PACK.md)
- [x] Portfolio technical-review + spine-health Strict links
- [ ] Owner: Blueprint sync / create Strict service + set `RAG_JWT_SECRET`
- [ ] Strict `/health` → `review_mode=strict` live
- [ ] Body-spoof rejected under Strict (live verify)

### P2 — AWS free-tier receipts

- [x] Case study + runbook published in repo
- [x] Linked from hire signal links
- [ ] Owner: run apply→verify→destroy; attach receipts under `docs/artifacts/aws-receipts/`

### P3 — Signal

- [x] Substack publish pack [`P3_SUBSTACK_PUBLISH_PACK.md`](./P3_SUBSTACK_PUBLISH_PACK.md)
- [x] ≥8 ADR post drafts (posts 1–10 in calendar)
- [ ] Owner publishes (URLs recorded here)

### P4 — Harden

- [x] ACF / GOLDEN_PATH honest publish boundary
- [x] NIST one-pager
- [x] FinOps ROI one-pager
- [x] Hire signal links for all three (+ AWS case study)

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

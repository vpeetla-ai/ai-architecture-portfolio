# Top-1% → 90/100 score plan (60 days · ~$45/mo)

**Status:** ACTIVE  
**Started:** 2026-07-22  
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

- [ ] Render Starter applied: `vap-api`, `aegisai-api`, `enterprise-rag-api`
- [ ] Idle ≥15m → 3× `/health` &lt;3s each
- [ ] `/api/spine-health` warmOk 3/3 after idle
- [ ] G1 closed in gap plan

### P1 — Live Strict ERAG

- [ ] `enterprise-rag-api-strict` Blueprint + deploy docs
- [ ] Strict `/health` → `review_mode=strict`
- [ ] Body-spoof rejected under Strict
- [ ] Portfolio technical-review links Demo + Strict
- [ ] JWT panel pack (mint script + curl)

### P2 — AWS free-tier receipts

- [ ] Case study with apply/destroy evidence path
- [ ] Linked from hire / technical-review
- [ ] Honest: ephemeral proof, not always-on multi-cloud

### P3 — Signal

- [ ] Substack publish pack ready (draft + checklist)
- [ ] ≥8 ADR post drafts with CTAs
- [ ] Owner publishes (URLs recorded here)

### P4 — Harden

- [ ] ACF / GOLDEN_PATH honest publish boundary
- [ ] NIST one-pager with live proof links
- [ ] FinOps ROI one-pager
- [ ] Hire + technical-review link all three

### P5 — Conversion + rescore

- [ ] 3 mock sessions logged (or scheduled with plans)
- [ ] ≥10 outreach rows (template filled / real rows)
- [ ] Keyed golden path green on warm spine
- [ ] Skills audit canvas rescore ≥90 or ≤2 gaps

## Progress log

| Date | Phase | Note |
|------|-------|------|
| 2026-07-22 | — | Tracker created; implementation started |

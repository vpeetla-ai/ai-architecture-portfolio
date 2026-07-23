# Render free (interim) — operating honesty

**Decision (2026-07-22):** Keep spine APIs on **Render Free** for 1–2 days; apply **Starter** later.  
**Implication:** cold starts (~15–40s) after idle are **expected and documented** — not claimed as always-on.

## What still ships without Starter

| Workstream | Status |
|------------|--------|
| Dual-cloud free-tier split (AWS + GCP) | Active — primary infra skill path this week |
| Strict ERAG | Prefer **GCP Cloud Run Strict** or **local Docker Strict** until Render Strict Starter exists |
| Signal (Substack / LinkedIn drafts) | Active — owner publish |
| Mocks / outreach packs | Active — owner execute |
| Idle probe / G1 close | **Parked** until Starter applied |

## Panel script while on Free

1. Open `/spine-health` — if cold, wait one retry (honesty: Free spin-down).  
2. Prefer GCP ERAG Strict URL (after you deploy) or local Strict recipe in STRICT_PANEL_PACK.  
3. Do not tell interviewers the Render free APIs are “production always-on.”

## When Starters land

1. Instance type → Starter for vap / aegisai / erag (+ optional Strict).  
2. `./scripts/probe_spine_idle.sh`  
3. Un-park P0 checkboxes in TOP1PCT_90SCORE_60DAY.md.

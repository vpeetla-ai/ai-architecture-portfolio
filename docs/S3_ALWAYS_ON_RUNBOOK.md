# S3 — Always-on spine APIs + interview pack

**Status:** Complete (2026-07-18) — PRs merged; duplicate Vercel playbook project deleted  
**Plan:** [`TOP1PCT_90DAY_EXECUTION.md`](./TOP1PCT_90DAY_EXECUTION.md) · Decision **D2**

## S3.1 Render plan upgrades

| Service | Health | Blueprint target | Notes |
|---------|--------|------------------|-------|
| `aegisai-api` | https://aegisai-api.onrender.com/health | **starter** (already) | Confirm in dashboard |
| `vap-api` | https://vap-api.onrender.com/health | **starter** | `venkat-ai-platform/render.yaml` updated free→starter |
| `enterprise-rag-api` | https://enterprise-rag-api-4el1.onrender.com/health | **starter** | `enterprise_rag_platform/render.yaml` updated; live name may keep `-4el1` suffix |

### Apply (dashboard)

1. Open [Render Dashboard](https://dashboard.render.com) → select the vpeetla-ai workspace.
2. For **vap-api** and **enterprise-rag-api**: Settings → Instance type → **Starter** (or sync Blueprint).
3. Leave FinOps / gateway / cache / labs on free unless a panel requires them warm.
4. Verify warm path: three consecutive `/health` samples &lt; 3s with ≥15 min idle beforehand.

**90/100 P0 probe:** from `ai-architecture-portfolio` run `./scripts/probe_spine_idle.sh` (default waits 16 minutes).

Render MCP may be unauthorized for `list_workspaces` — plan changes ship as Blueprint PRs; apply requires dashboard (or re-auth MCP + `update_web_service`).

## S3.2 Spine health page

- Live UI: https://venkat-ai.com/spine-health (after portfolio deploy)
- Also embedded on `/proof`; linked from `/technical-review`
- API: `GET /api/spine-health` (server-side probes)

## S3.3 Hire funnel

`/hire` primary path: Technical review → Interview playbook → Practice Arena → Spine health.

Canonical playbook URL: https://ai-architect-interview-playbook.vercel.app  
Practice Arena: https://ai-architect-practice-arena.vercel.app

## S3.4 Duplicate Vercel playbook project

| Host | Role |
|------|------|
| `ai-architect-interview-playbook.vercel.app` | **Canonical** — keep |
| `ai-architect-interview-playbook-9xs.vercel.app` | **Deleted** (project `ai-architect-interview-playbook-9xss` removed 2026-07-18) |

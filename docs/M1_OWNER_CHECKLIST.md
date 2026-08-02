# Month 1 owner checklist — Always-on + Strict panel (G1 / G7)

Companion to [SIX_MONTH_PLATFORM_PLAN_2026.md](./SIX_MONTH_PLATFORM_PLAN_2026.md).
Agents prepare code/docs; **you** apply Render plans and publish signal.

## G1 — Always-on spine

1. Render dashboard → upgrade (or confirm Starter) for:
   - `vap-api`
   - `aegisai-api`
   - `enterprise-rag-api` (or current ERAG host)
   - optional: `acf-api-eub4`
2. Wait ≥15 minutes with no traffic.
3. Probe:

```bash
for u in \
  https://vap-api.onrender.com/health \
  https://aegisai-api.onrender.com/health \
  https://enterprise-rag-api-4el1.onrender.com/health
do
  echo "=== $u ==="
  for i in 1 2 3; do
    curl -sS -o /dev/null -w "%{http_code} %{time_total}\n" --max-time 5 "$u" || echo "fail"
  done
done
```

**Done when:** three consecutive successes with `time_total` &lt; 3s after idle.

See also: [S3_ALWAYS_ON_RUNBOOK.md](./S3_ALWAYS_ON_RUNBOOK.md) · [RENDER_FREE_INTERIM.md](./RENDER_FREE_INTERIM.md)

## G7 — Strict ERAG panel path

- Local: `enterprise_rag_platform` → `scripts/run_strict_local.sh` + link from `/technical-review`
- Or GCP Cloud Run Strict URL in `ERAG_STRICT_URL` for golden path
- Pack: [STRICT_PANEL_PACK](https://github.com/vpeetla-ai/enterprise_rag_platform/blob/main/docs/STRICT_PANEL_PACK.md)

## G3–G6 — Signal (owner)

| ID | Action |
|----|--------|
| G3 | Publish flagship Substack essay with proof links |
| G4 | ≥8 ADR LinkedIn posts from [S5_ADR_POST_CALENDAR](./S5_ADR_POST_CALENDAR.md) |
| G5 | 3 mock loops in [MOCK_LOOP_LOG](./interview/MOCK_LOOP_LOG.md) |
| G6 | ≥10 outreach rows in [OUTREACH_LOG](./outreach/OUTREACH_LOG.md) |

## Agent-completed in M1 kickoff (2026-08-02)

- [x] Six-month plan doc + portfolio README link
- [x] AegisAI README: ACF publish ✅ Wired
- [x] ACF publish intents (no fake URLs), quality rubrics, ERAG compose config
- [x] ACF ARCHITECTURE mermaid order aligned to `agents/graph.py`

# Panel day runbook — Render Free interim

**Use when:** Principal / Staff+ live review while spine APIs are still on **Render Free**.  
**Do not claim:** always-on, production multi-cloud, or warm Starter SLOs.  
**After Starter:** prefer [S3_ALWAYS_ON_RUNBOOK.md](./S3_ALWAYS_ON_RUNBOOK.md) + this Strict section.

Related: [RENDER_FREE_INTERIM.md](./RENDER_FREE_INTERIM.md) · [STRICT_PANEL_PACK](https://github.com/vpeetla-ai/enterprise_rag_platform/blob/main/docs/STRICT_PANEL_PACK.md) · [GOLDEN_PATH.md](./GOLDEN_PATH.md)

## T−30 minutes

1. Open https://venkat-ai.com/spine-health → **Recheck** once (first hit may take 15–40s).  
2. Open https://venkat-ai.com/technical-review — keep tab ready.  
3. Start Strict ERAG (pick one):
   - Local: `cd enterprise_rag_platform && ./scripts/run_strict_local.sh`
   - GCP: `./scripts/deploy_strict_gcp.sh <PROJECT>` (if already deployed, skip)
4. Capture Strict receipt (optional but strong):
   ```bash
   export ERAG_STRICT_URL=http://127.0.0.1:8080   # or Cloud Run URL
   export RAG_JWT_SECRET=…                        # same as Strict process
   ./scripts/capture_strict_panel_receipt.sh
   ```
5. Optional golden path with Strict probe:
   ```bash
   export ERAG_STRICT_URL=…
   python3 scripts/run_golden_path.py
   ```

## 15-minute live path

| Min | Say | Show |
|-----|-----|------|
| 0–2 | “Spine is Render Free today — cold starts labeled; Starter lands soon.” | `/spine-health` |
| 2–5 | Orchestration ≠ governance | VAP demo → AegisAI gateway / HITL |
| 5–8 | Access-before-ranking + anti-spoof | ERAG Demo UI + Strict `/health` `review_mode=strict` + spoof curl |
| 8–11 | Application HITL honesty | ACF Demo banner; publish needs Clerk |
| 11–14 | Meter + eval proof | FinOps / golden-path artifact + GER CI badge |
| 14–15 | Decisions | ADR-001 / ADR-0006 / NIST one-pager |

## Expected Free-tier friction (say out loud)

- First `/health` after idle: 15–40s → one Retry is normal.  
- Render Strict twin URL may 404 until Starter — use local/GCP Strict.  
- Golden path without keys: VAP/ERAG **401** is honesty, not failure (`stranger_replayable_ok`).

## Anti-scripts

- ❌ “These APIs are always warm / production.”  
- ❌ “Strict is the same process as Demo.”  
- ❌ Unauthenticated “live publish” on ACF.

# Golden path — stranger-replayable spine E2E

**Status:** S4.1 active  
**Script:** [`scripts/run_golden_path.py`](../scripts/run_golden_path.py) · wrapper [`scripts/run_golden_path.sh`](../scripts/run_golden_path.sh)  
**Latest artifact:** [`docs/artifacts/golden-path/latest.json`](./artifacts/golden-path/latest.json)

## What it proves

A cold reviewer can run one script and see the governed stack respond:

1. **Health** — VAP · ERAG · AegisAI · ACF · FinOps  
2. **Observability status** — compose-plane honesty probes (optional; never fail stranger gate)  
3. **Ask** — VAP `/chat` (API-key gated on live — see honesty)  
4. **Retrieve/answer** — ERAG `/v1/answer` (API-key gated on live)  
5. **Govern** — AegisAI `/api/gateway/tool-request` → typically `approval_required` + HITL  
6. **Application** — ACF `/health` (Clerk required for live publish)  
7. **Meter** — FinOps `/v1/usage`  
8. **Eval proof** — golden-eval-registry CI badge + `enterprise_rag_adversarial_v1`

## Run

```bash
cd ai-architecture-portfolio
# Optional but recommended on macOS system Python (fixes CERTIFICATE_VERIFY_FAILED):
#   pip install certifi
python3 scripts/run_golden_path.py
# or
./scripts/run_golden_path.sh
```

Optional full ask→answer (dashboard secrets — never commit):

```bash
export VAP_API_KEY=...
export RAG_API_KEY=...
# optional
export AGENTFINOPS_API_KEY=...
python3 scripts/run_golden_path.py
```

Optional Strict ERAG probe (local Docker or GCP — Free interim):

```bash
export ERAG_STRICT_URL=http://127.0.0.1:8080   # or Cloud Run Strict URL
# optional spoof reject check:
export RAG_JWT_SECRET=…   # same secret as Strict process
python3 scripts/run_golden_path.py
# summary.strict_erag_ok → true when /health review_mode=strict
```

Exit code `0` when **stranger-replayable** checks pass (health + AegisAI gate + FinOps meter; VAP/ERAG may honestly return 401 without keys). `ERAG_STRICT_URL` is optional and never fails the stranger gate when unset.

## Honesty

| Step | Without secrets | With keys |
|------|-----------------|-----------|
| Spine `/health` | ✅ | ✅ |
| Observability `/…/observability/status` | ✅ honesty-only (cold start may miss) | ✅ counted in `observability_status_ok` |
| VAP `/chat` | 401 expected (ADR-009) | ✅ (ephemeral OK if Postgres down) |
| ERAG `/v1/answer` | 401 expected | ✅ Demo principal |
| ERAG Strict | unset = skipped | ✅ set `ERAG_STRICT_URL` (+ optional `RAG_JWT_SECRET`) — [STRICT_PANEL_PACK](https://github.com/vpeetla-ai/enterprise_rag_platform/blob/main/docs/STRICT_PANEL_PACK.md) · [panel Free runbook](./PANEL_DAY_FREE_RUNBOOK.md) |
| AegisAI gateway | ✅ demo headers | ✅ |
| ACF live publish | **Not in golden path** | Clerk session required — path records `/health` only (G8 honest boundary) |
| FinOps `/v1/usage` | ✅ if key unset | ✅ |

### ACF publish boundary (permanent)

AI Content Factory’s end-user publish is behind Clerk HITL. The golden path **by design** does not automate a public publish side effect. Reviewers should open the ACF demo, read the Demo/Strict banner, and treat `/health` (+ optional authenticated dashboard) as application-layer proof. Claiming unauthenticated “live publish” would violate ADR-008 / hitl-side-effects.

## Artifact schema

Each run writes `docs/artifacts/golden-path/gp-<UTC>.json` and updates `latest.json`:

- `summary.stranger_replayable_ok`
- `summary.full_ask_answer_ok`
- `summary.strict_erag_ok` (`null` if `ERAG_STRICT_URL` unset)
- `summary.observability_status_ok` / `observability_status_total` (honesty probes; never fail stranger gate)
- per-step `latency_ms`, `http_status`, proof fields (`gateway_decision`, `auth_gated`, …)
- `summary.ci_proof` links the adversarial golden CI badge

## Reviewer entry points

- Portfolio technical review: https://venkat-ai.com/technical-review  
- Spine health: https://venkat-ai.com/spine-health  
- Case study: [case-studies/golden-path-spine-e2e.md](../case-studies/golden-path-spine-e2e.md)  
- GER CI: https://github.com/vpeetla-ai/golden-eval-registry/actions/workflows/ci.yml  

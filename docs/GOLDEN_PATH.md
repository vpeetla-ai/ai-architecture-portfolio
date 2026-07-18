# Golden path — stranger-replayable spine E2E

**Status:** S4.1 active  
**Script:** [`scripts/run_golden_path.py`](../scripts/run_golden_path.py) · wrapper [`scripts/run_golden_path.sh`](../scripts/run_golden_path.sh)  
**Latest artifact:** [`docs/artifacts/golden-path/latest.json`](./artifacts/golden-path/latest.json)

## What it proves

A cold reviewer can run one script and see the governed stack respond:

1. **Health** — VAP · ERAG · AegisAI · ACF · FinOps  
2. **Ask** — VAP `/chat` (API-key gated on live — see honesty)  
3. **Retrieve/answer** — ERAG `/v1/answer` (API-key gated on live)  
4. **Govern** — AegisAI `/api/gateway/tool-request` → typically `approval_required` + HITL  
5. **Application** — ACF `/health` (Clerk required for live publish)  
6. **Meter** — FinOps `/v1/usage`  
7. **Eval proof** — golden-eval-registry CI badge + `enterprise_rag_adversarial_v1`

## Run

```bash
cd ai-architecture-portfolio
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

Exit code `0` when **stranger-replayable** checks pass (health + AegisAI gate + FinOps meter; VAP/ERAG may honestly return 401 without keys).

## Honesty

| Step | Without secrets | With keys |
|------|-----------------|-----------|
| Spine `/health` | ✅ | ✅ |
| VAP `/chat` | 401 expected (ADR-009) | ✅ |
| ERAG `/v1/answer` | 401 expected | ✅ Demo principal |
| AegisAI gateway | ✅ demo headers | ✅ |
| ACF publish | `/health` only | Local `ALLOW_DEV_AUTH` or Clerk |
| FinOps `/v1/usage` | ✅ if key unset | ✅ |

## Artifact schema

Each run writes `docs/artifacts/golden-path/gp-<UTC>.json` and updates `latest.json`:

- `summary.stranger_replayable_ok`
- `summary.full_ask_answer_ok`
- per-step `latency_ms`, `http_status`, proof fields (`gateway_decision`, `auth_gated`, …)
- `summary.ci_proof` links the adversarial golden CI badge

## Reviewer entry points

- Portfolio technical review: https://venkat-ai.com/technical-review  
- Spine health: https://venkat-ai.com/spine-health  
- Case study: [case-studies/golden-path-spine-e2e.md](../case-studies/golden-path-spine-e2e.md)  
- GER CI: https://github.com/vpeetla-ai/golden-eval-registry/actions/workflows/ci.yml  

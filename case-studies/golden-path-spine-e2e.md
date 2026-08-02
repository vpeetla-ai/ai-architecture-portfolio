# Case study — Golden path spine E2E (S4 / G2)

**Last run:** `gp-20260718T234153Z`  
**Artifact:** [docs/artifacts/golden-path/latest.json](../docs/artifacts/golden-path/latest.json)  
**How to replay:** [docs/GOLDEN_PATH.md](../docs/GOLDEN_PATH.md)

## Problem

Slide decks say the platforms are wired. Strangers can’t replay slides. The scar is a portfolio that claims “ask → RAG → govern → meter” without a public JSON artifact anyone can re-run.

## What we decided

1. **Ship a stranger-replayable script** — walk the Principal spine and persist `latest.json`.
2. **Keyed private mutating calls** — `VAP_API_KEY` + `RAG_API_KEY` local only; never commit secrets. Without keys, record 401 honestly.
3. **Health + real ask/answer/gateway/meter steps** — not health-only theater. The script also probes `observability/status` compose honesty; those steps never fail the stranger gate on a cold miss.
4. **Keep free-tier honesty** — cold starts and degraded deps show up in the artifact.

## Measured signal (this run)

Keyed private run (`VAP_API_KEY` + `RAG_API_KEY` in local env only — never committed).

| Step | Result | Latency |
|------|--------|---------|
| VAP `/health` | ok | 137 ms |
| ERAG `/health` | ok · `review_mode=demo` | 253 ms |
| AegisAI `/health` | ok | 746 ms |
| ACF `/health` | ok · `database=error` (degraded) | 462 ms |
| FinOps `/health` | ok | 183 ms |
| VAP `/chat` | **200** ask reply (ephemeral; `thread_id=null` if Postgres persistence down) | 7455 ms |
| ERAG `/v1/answer` | **200** grounded Zephyr answer | 1350 ms |
| AegisAI gateway | `gateway_decision=approval_required` + HITL task | 4146 ms |
| FinOps `/v1/usage` | metered · `breached=false` | 216 ms |

**Summary flags:** `stranger_replayable_ok=true` · `full_ask_answer_ok=true` · `steps_http_ok=10/10`.

## Live proof

- Artifact: [latest.json](../docs/artifacts/golden-path/latest.json)
- Eval / CI: [![GER CI](https://github.com/vpeetla-ai/golden-eval-registry/actions/workflows/ci.yml/badge.svg)](https://github.com/vpeetla-ai/golden-eval-registry/actions/workflows/ci.yml)
- Adversarial suite: `enterprise_rag_adversarial_v1` (principal spoof / injection gates)

## Limitations / what we'd do differently

- Live VAP/ERAG mutating routes need API keys (ADR-009 / RAG API key).
- VAP `/chat` persistence is best-effort if Postgres is down (ephemeral 200).
- ACF live publish needs Clerk; golden path uses `/health` for the app layer — this run saw `database=error` (degraded).
- Free-tier cold starts happen; spine APIs target starter plans (S3 / G1).
- Re-run and refresh the artifact after meaningful spine changes — stale numbers are worse than an honest miss.

## Related

- Essay: [From Multi-Agent OS to Agent Governance](./from-multi-agent-os-to-agent-governance.md)
- ADR-001 · ADR-009 · ADR-014 · ADR-024
- Gap plan: [TOP1PCT_GAP_PLAN.md](../docs/TOP1PCT_GAP_PLAN.md)

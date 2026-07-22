# Case study — Golden path spine E2E (S4 / G2)

**Last run:** `gp-20260718T234153Z`  
**Artifact:** [docs/artifacts/golden-path/latest.json](../docs/artifacts/golden-path/latest.json)  
**How to replay:** [docs/GOLDEN_PATH.md](../docs/GOLDEN_PATH.md)

## Decision

Ship a **stranger-replayable** script that walks the Principal spine (ask → RAG → govern → app health → meter) and persists a public JSON artifact — instead of slide-deck claims about “wired platforms.”

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

## Eval / CI proof

[![GER CI](https://github.com/vpeetla-ai/golden-eval-registry/actions/workflows/ci.yml/badge.svg)](https://github.com/vpeetla-ai/golden-eval-registry/actions/workflows/ci.yml)

Adversarial suite: `enterprise_rag_adversarial_v1` (principal spoof / injection gates).

## Boundaries

- Live VAP/ERAG mutating routes require API keys (ADR-009 / RAG API key). Without keys, the artifact records 401 honestly and still counts as stranger-replayable.
- VAP `/chat` persistence is best-effort: if Postgres is unavailable, the graph still returns an ephemeral 200 (see venkat-ai-platform PR #3).
- ACF live publish requires Clerk; golden path uses `/health` for the application layer. This run saw ACF `database=error` (degraded) — separate from ask→answer.
- Free-tier services may cold-start; spine APIs target starter plans (S3 / G1).

## Related

- Essay: [From Multi-Agent OS to Agent Governance](./from-multi-agent-os-to-agent-governance.md)
- ADR-001 orchestration vs governance · ADR-009 VAP auth gate · ADR-014 golden-eval CI · ADR-024 PRODUCTION_STRICT
- Gap plan: [TOP1PCT_GAP_PLAN.md](../docs/TOP1PCT_GAP_PLAN.md)

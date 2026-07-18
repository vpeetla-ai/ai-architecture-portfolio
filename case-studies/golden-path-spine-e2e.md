# Case study — Golden path spine E2E (S4)

**Last run:** `gp-20260718T171049Z`  
**Artifact:** [docs/artifacts/golden-path/latest.json](../docs/artifacts/golden-path/latest.json)  
**How to replay:** [docs/GOLDEN_PATH.md](../docs/GOLDEN_PATH.md)

## Decision

Ship a **stranger-replayable** script that walks the Principal spine (ask → RAG → govern → app health → meter) and persists a public JSON artifact — instead of slide-deck claims about “wired platforms.”

## Measured signal (this run)

| Step | Result | Latency |
|------|--------|---------|
| VAP `/health` | ok | 181 ms |
| ERAG `/health` | ok · `review_mode=demo` | 171 ms |
| AegisAI `/health` | ok | 702 ms |
| ACF `/health` | ok | 222 ms |
| FinOps `/health` | ok | 145 ms |
| VAP `/chat` | **401 auth-gated** (expected without `VAP_API_KEY`) | 194 ms |
| ERAG `/v1/answer` | **401 auth-gated** (expected without `RAG_API_KEY`) | 211 ms |
| AegisAI gateway | `gateway_decision=approval_required` + HITL task | 4090 ms |
| FinOps `/v1/usage` | `cost_usd=0.00027` · `breached=false` | 182 ms |

**Summary flags:** `stranger_replayable_ok=true` · `full_ask_answer_ok=false` (keys not supplied in this run).

## Eval / CI proof

[![GER CI](https://github.com/vpeetla-ai/golden-eval-registry/actions/workflows/ci.yml/badge.svg)](https://github.com/vpeetla-ai/golden-eval-registry/actions/workflows/ci.yml)

Adversarial suite: `enterprise_rag_adversarial_v1` (principal spoof / injection gates).

## Boundaries

- Live VAP/ERAG mutating routes require API keys (ADR-009 / RAG API key) — the artifact records 401 honestly when keys are absent.
- ACF live publish requires Clerk; golden path uses `/health` for the application layer.
- Free-tier services may cold-start; spine APIs target starter plans (S3).

## Related

- Essay: [From Multi-Agent OS to Agent Governance](./from-multi-agent-os-to-agent-governance.md)
- ADR-001 orchestration vs governance · ADR-009 VAP auth gate · ADR-014 golden-eval CI · ADR-024 PRODUCTION_STRICT

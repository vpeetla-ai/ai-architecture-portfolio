# ADR-014: golden-eval-registry Becomes a Real CI Gate (2 of 6 Suite Kinds)

## Status

Accepted — 2026-07-05

> **Status footnote (2026-08-08):** The "2 of 6" count was true at acceptance. Suite kinds with real CI gates later grew to **10** (including `collaboration_scorecard` — see [ADR-031](./ADR-031-multi-agent-collaboration-scorecard.md)). Keep the historical title; do not restate "2 of 6" as current org metrics.

## In one breath (panel)

I'd rather run two suite kinds against real consumer output in CI than claim six golden suites when `validate.py` only checked that the JSONL was well-formed.

## Context

`golden-eval-registry`'s own [ADR-0001](https://github.com/vpeetla-ai/golden-eval-registry/blob/main/docs/adr/0001-versioned-golden-eval-registry.md)
named this as future work: "v1 validates fixtures only; cross-repo execution is future work."
`validate.py` checked manifests and JSONL shape — it never executed a case against anything.
Phase B of the top-1% AI Architect program ([ADR-013](./ADR-013-mcp-exposure-and-real-a2a-delegation.md)
was Phase A), closing the Phase 4 item in `docs/ORG_IMPROVEMENT_PLAN_2026.md`: "Consumer
adapters that import registry suites in platform CI."

Fixture existence and fixture correctness are different claims. I refused treating a green
schema check as an eval gate.

## Decision

`golden-eval-registry` gained `src/golden_eval_registry/runner.py` — `score_case`/`score_suite`
compare a consumer's real output against a case's `expect` block, per suite `kind`. Stays
dependency-light and provider-agnostic on purpose: each consumer knows how to reach itself and
hands real output here for scoring, rather than the registry embedding provider clients (see
[golden-eval-registry ADR-0002](https://github.com/vpeetla-ai/golden-eval-registry/blob/main/docs/adr/0002-real-scorer-and-first-ci-gate.md)).

Two consumers wired as real CI gates so far:
- `enterprise_rag_platform` checks this repo out and runs `enterprise_rag_golden_v1` against a
  real, isolated `RagPipeline` (not the API's demo-seeded singleton, which would let unrelated
  demo docs compete for ranking).
- `aegisloop-agentops-workbench` checks this repo out and runs `aegisloop_mission_gates_v1`
  against the real `runtime.evaluate()` gate function.

First real run of `enterprise_rag_golden_v1` found a real bug: the corpus fixture shared no
vocabulary with a destructive/PII-bearing query once the guardrail redacted the email, so the
case never grounded despite `expect: grounded=true` — a fixture that had never been checked
against real retrieval. Fixed and bumped (`1.0.0` → `1.0.1`), disclosed in golden-eval-registry
ADR-0002. That's the thesis: **only real execution proves fixture correctness.**

Also fixed while wiring: `/v1/answer` never included `document_id` on citations, so the suite's
`document_ids` check had nothing to compare — honest API gap, not a scoring workaround.

## Consequences

### Positive
- Closes `ORG_IMPROVEMENT_PLAN_2026.md` Phase 4 and golden-eval-registry ADR-0001's follow-up.
- Both CI gates verified passing in real GitHub Actions runs, not just locally.
- Surfaced and fixed a previously undetected fixture bug on first real execution — evidence the
  gate does work, not theater.

### Negative
- At acceptance, only **2 of 6** suite kinds (`rag_answer`, `mission_gate`) had a real scorer
  and gate; the rest were fixture-validation only. Say Planned vs Implemented out loud.
  *(Superseded count: see Status footnote + [ADR-031](./ADR-031-multi-agent-collaboration-scorecard.md).)*
- `actions/checkout`'s `path:` lands the sibling repo *inside* the workspace — both consumer
  workflows set `GOLDEN_EVAL_REGISTRY_PATH` explicitly; caught only by pushing and reading the
  real Actions run, not local testing alone.
- No cross-repo CI matrix or aggregated status badge yet — each consumer workflow is independent.

## References
- `golden-eval-registry/src/golden_eval_registry/runner.py`
- `golden-eval-registry/docs/adr/0002-real-scorer-and-first-ci-gate.md`
- `enterprise_rag_platform/tests/test_golden_eval_gate.py`, `.github/workflows/tests.yml`
- `aegisloop-agentops-workbench/services/api/tests/test_golden_eval_gate.py`, `.github/workflows/api-tests.yml`

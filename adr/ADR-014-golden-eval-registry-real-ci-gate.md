# ADR-014: golden-eval-registry Becomes a Real CI Gate (2 of 6 Suite Kinds)

## Status

Accepted — 2026-07-05

## Context

`golden-eval-registry`'s own [ADR-0001](https://github.com/vpeetla-ai/golden-eval-registry/blob/main/docs/adr/0001-versioned-golden-eval-registry.md)
explicitly named this as future work: "v1 validates fixtures only; cross-repo execution is
future work." `validate.py` checked that manifests and JSONL cases were well-formed — it never
executed a case against anything. This was Phase B of the org's top-1% AI Architect program
([ADR-013](./ADR-013-mcp-exposure-and-real-a2a-delegation.md) was Phase A), and directly closes
the item `docs/ORG_IMPROVEMENT_PLAN_2026.md`'s Phase 4 had already logged as outstanding:
"Consumer adapters that import registry suites in platform CI."

## Decision

`golden-eval-registry` gained `src/golden_eval_registry/runner.py` — `score_case`/`score_suite`
compare a consumer's real output against a case's `expect` block, per suite `kind`. It stays
dependency-light and provider-agnostic by design: each consumer already knows how to reach
itself, and hands the real output here for scoring, rather than the registry embedding
provider-specific client code (see [golden-eval-registry ADR-0002](https://github.com/vpeetla-ai/golden-eval-registry/blob/main/docs/adr/0002-real-scorer-and-first-ci-gate.md)).

Two consumers are wired as real CI gates so far:
- `enterprise_rag_platform`'s CI checks this repo out and runs `enterprise_rag_golden_v1`
  against a real, isolated `RagPipeline` (isolated rather than the API's demo-seeded singleton,
  which would otherwise let an unrelated demo document compete for retrieval ranking).
- `aegisloop-agentops-workbench`'s CI checks this repo out and runs `aegisloop_mission_gates_v1`
  against the real `runtime.evaluate()` gate function.

Running `enterprise_rag_golden_v1` for the first time immediately found a real bug: its own
corpus fixture shared no vocabulary with a destructive/PII-bearing query once the guardrail
layer redacted the email, so the case never actually grounded despite `expect: grounded=true` —
a fixture that had apparently never been checked against real retrieval behavior before. Fixed
the fixture and bumped its version (`1.0.0` → `1.0.1`), disclosed in golden-eval-registry's
ADR-0002. This is direct proof of the thesis motivating this whole phase: **fixture existence
and fixture correctness are different claims, and only real execution proves the second one.**

A second, unrelated real gap was also fixed while wiring this: `enterprise_rag_platform`'s
`/v1/answer` response never included `document_id` on citations, so the suite's `document_ids`
check had nothing to compare against — a small, honest API gap, not a scoring workaround.

## Consequences

### Positive
- Closes `ORG_IMPROVEMENT_PLAN_2026.md`'s Phase 4 backlog item and `golden-eval-registry`
  ADR-0001's explicit follow-up.
- Both new CI gates verified passing in real GitHub Actions runs, not just locally.
- Surfaced and fixed a real, previously-undetected fixture bug on first real execution —
  evidence the gate does real work, not theater.

### Negative
- Only 2 of 6 suite kinds (`rag_answer`, `mission_gate`) have a real scorer and a real gate;
  `harness_qa`, `repo_fix`, `graph_hitl`, `brief_gate` remain fixture-validation only.
- `actions/checkout`'s `path:` lands the sibling repo *inside* the workspace, not beside it —
  both consumer workflows had to set `GOLDEN_EVAL_REGISTRY_PATH` explicitly rather than relying
  on a relative-sibling-directory default (a local-dev convenience that doesn't hold in CI);
  this was itself caught only by pushing and checking the real Actions run, not by local testing
  alone.
- No cross-repo CI matrix or aggregated status badge yet — each consumer's workflow is
  independent.

## References
- `golden-eval-registry/src/golden_eval_registry/runner.py`
- `golden-eval-registry/docs/adr/0002-real-scorer-and-first-ci-gate.md`
- `enterprise_rag_platform/tests/test_golden_eval_gate.py`, `.github/workflows/tests.yml`
- `aegisloop-agentops-workbench/services/api/tests/test_golden_eval_gate.py`, `.github/workflows/api-tests.yml`

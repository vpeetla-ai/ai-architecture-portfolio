# ADR-031: Multi-agent collaboration scorecard (vector, not theater)

## Status

Accepted — 2026-08-08

## In one breath (panel)

I'd score multi-agent runs on a collaboration vector — CSS, TUE, hard gates, multi-trial — and refuse treating trace length or a `has_final` boolean as quality.

## Context

Single-agent golden suites (`mission_gate`, `rag_answer`, …) catch output regressions. They do **not** answer: did specialists contradict each other? Did tools fire when claimed? Did escalation bypass policy? Was the pass rate stable across trials?

AegisLoop's earlier `evaluate()` collapsed to theater: `quality = 94 if has_final and has_trace`. That green-washed collaboration. Inventing a 17th SaaS "eval product" would dilute the stack — the gap belonged in **golden-eval-registry** (portable scorer) + **AegisLoop** (live trajectories).

Thesis published as the Multi-Agent Evaluation Scorecard; this ADR binds it to shipped code.

## Decision

1. **GER owns the scorecard kind** — `collaboration_scorecard` with suite `multi_agent_collaboration_v1`: Collaboration Success Score (CSS), Tool-Use Efficiency (TUE), vector dimensions, and hard gates (contradiction, escalation bypass). Registry CI self-scores; consumers hand real trajectories.
2. **AegisLoop builds live trajectories** — `evaluate()` consumes the scorecard; research missions emit `tool_calls` for TUE; multi-trial CI gates mission classes; failures land in `runs/failures/` for promotion into GER.
3. **Ops loop without a new product** — `promote_failure.py`, weekly `collaboration-drift.yml`, and `/api/v1/ops/scorecard` / spine-health probes surface the vector. Failures become golden cases; drift alarms before narrative rot.
4. **Refuse** — scalar "quality %" from trace presence; a standalone multi-agent eval SaaS; claiming Stage-4 maturity without multi-trial + hard gates.

## Consequences

**Positive**

- Panel-ready falsifiable claim: collaboration is gated, not vibed
- Same GER discipline as ADR-014 — kind + consumer CI, not schema-only fixtures
- Honest Stage progression: Stage 1.5 → Stage 3/4 depth on one mission class without inventing a product

**Negative / honest limits**

- Coverage is AegisLoop-first; other fleets still need trajectory adapters
- CSS/TUE thresholds are org-tuned heuristics — label **H** in interviews unless measured baselines exist
- Multi-trial CI cost grows with mission classes; keep the gated set small

## Links

- Case study: [aegisloop-agentops.md](../case-studies/aegisloop-agentops.md) · [golden-eval-registry.md](../case-studies/golden-eval-registry.md)
- GER: `scorecard.py`, suite `multi_agent_collaboration_v1`
- AegisLoop: trajectory `evaluate()`, multi-trial CI, ops scorecard
- Prior: [ADR-014](./ADR-014-golden-eval-registry-real-ci-gate.md) · [ADR-003](./ADR-003-mission-based-agentops.md)
- Playbook: `ai-system-design/26-multi-agent-collaboration-evaluation-scorecard.md`

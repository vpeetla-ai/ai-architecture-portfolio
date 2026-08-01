# ADR-011: AgentFinOps as a Standalone Service, Not Embedded Per-Repo Logic

## Status

Accepted — 2026-07-04

## In one breath (panel)

I'd put cost truth in its own ledger service and refuse per-repo "FinOps" dashboards that invent numbers from character counts — report cost here; let each product enforce its own halt.

## Context

The 2026-07-03 audit found `aegisai-enterprise-agent-platform` and
`aegisloop-agentops-workbench` both shipping "FinOps" from fabricated data — AegisAI's
`RegisteredAgent.monthly_cost_usd` is a static seed that never updates from usage; AegisLoop's
`estimate_mission_cost` guesses tokens from output character count even when a real, metered
API call already returned `usage`/`usageMetadata` and we discarded it. Logged as the top Phase
6 item in `docs/ORG_IMPROVEMENT_PLAN_2026.md`, and referenced from the portfolio FinOps thesis
card behind the Substack piece "Enterprise AI FinOps Architecture" (2026-06-09).

First instinct was to patch both repos in place. I reconsidered for two reasons: (1) every other
capability here is already a single-purpose repo — VAP, AegisAI, Enterprise RAG, AegisLoop,
LoopForge — not shared modules bolted sideways; (2) a shared ledger is the only way to get a
real cross-repo / cross-tenant budget total, which siloed per-repo modules structurally cannot
provide. I refused leaving the fake dashboards as the story.

## Decision

New repo: [`agent-finops`](https://github.com/vpeetla-ai/agent-finops). Mirrors AegisAI's
`sdk/python/aegisai_gateway` + service split — shared capability, thin client:

1. FastAPI service with its own ledger (SQLite dev / Postgres prod) recording real usage events
   and detecting budget breaches (`POST /v1/usage`, `GET`/`PUT /v1/budget/{scope_type}/{scope_value}`).
2. Python SDK (`agent_finops_client`) with graceful local fallback when unconfigured — consumers
   never hard-fail just because this service isn't wired yet.
3. **This service reports cost truth; it does not enforce.** AegisAI's kill-switch and
   AegisLoop's mission-dispatch guard stay each repo's job — ADR-001's split extended to
   cost-truth vs enforcement.

Built in stages: service first (this ADR — 22 tests, verified against a live running instance,
not just mocks); consumer wiring in AegisAI and AegisLoop as follow-up (AegisLoop landed in
ADR-012).

## Consequences

### Positive
- One canonical pricing table (`agent_finops.pricing.RATES`) instead of drifting copies.
- Schema supports `scope_type="tenant"` for real cross-platform budget totals once more than
  one consumer is wired — impossible with siloed modules.
- Adds another org repo with the same documentation discipline: honest status table, ADR,
  architecture/product docs, demo, CI.

### Negative
- Another service to deploy; SDK local-fallback exists so that's non-fatal.
- Doesn't fix the two fake dashboards by itself — that's Stage 2. Until consumers wire in,
  this ADR answers "what should replace them," not "are they replaced." Label Planned vs
  Implemented accordingly on the portfolio card.

### Follow-ups
- Wire `aegisai-enterprise-agent-platform`'s `WebsiteBuildOrchestrator` as first consumer,
  budget breach → existing `KillSwitchService`.
- Wire `aegisloop-agentops-workbench` mission runtime as second consumer (done in ADR-012).
- Update both README FinOps rows and the portfolio FinOps thesis card once real.

## References
- [agent-finops](https://github.com/vpeetla-ai/agent-finops), specifically
  [ADR-0001](https://github.com/vpeetla-ai/agent-finops/blob/main/docs/adr/0001-standalone-cost-governance-service.md)
  (repo-local decision this ADR summarizes at org level)
- [ORG_IMPROVEMENT_PLAN_2026.md](../docs/ORG_IMPROVEMENT_PLAN_2026.md) Phase 6
- [ADR-001: Orchestration vs governance split](./ADR-001-orchestration-vs-governance-split.md)

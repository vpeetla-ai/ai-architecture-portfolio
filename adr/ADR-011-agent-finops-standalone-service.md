# ADR-011: AgentFinOps as a Standalone Service, Not Embedded Per-Repo Logic

## Status

Accepted — 2026-07-04

## Context

The 2026-07-03 security/architecture audit found `aegisai-enterprise-agent-platform` and
`aegisloop-agentops-workbench` both ship a "FinOps" module computing cost from fabricated data —
AegisAI's `RegisteredAgent.monthly_cost_usd` is a static seed value that never updates from real
usage; AegisLoop's `estimate_mission_cost` guesses tokens from output character count even when a
real, metered API call is made. Both repos' own LLM clients already receive real token usage from
their provider responses (`usage`/`usageMetadata` fields) and discard it. This was logged as the
top Phase 6 item in `docs/ORG_IMPROVEMENT_PLAN_2026.md` and is referenced from the portfolio
site's FinOps thesis card as the concrete proof behind the Substack piece "Enterprise AI FinOps
Architecture" (2026-06-09).

The initial plan was to fix this inside each of the two repos directly. Reconsidered in favor of
a standalone repo, for two reasons: (1) it matches how every other capability in this org is
already structured — VAP (orchestration), AegisAI (governance), Enterprise RAG (knowledge),
AegisLoop (fleet ops), LoopForge (self-improvement) are each their own single-purpose repo, not
shared modules bolted onto each other; (2) a shared ledger is the only way to get a real
cross-repo/cross-tenant budget total, which per-repo FinOps modules structurally cannot provide.

## Decision

New repo: [`agent-finops`](https://github.com/vpeetla-ai/agent-finops). Mirrors AegisAI's own
`sdk/python/aegisai_gateway` + service split — the org's established "shared capability + thin
client" pattern:

1. A FastAPI service with its own ledger (SQLite dev / Postgres prod) recording real usage events
   and detecting budget breaches (`POST /v1/usage`, `GET`/`PUT /v1/budget/{scope_type}/{scope_value}`).
2. A Python SDK (`agent_finops_client`) with graceful local-fallback when unconfigured — a
   consumer never hard-fails just because this service isn't deployed or wired yet.
3. **This service reports cost truth; it does not enforce.** AegisAI's kill-switch and
   AegisLoop's mission-dispatch guard remain each repo's own responsibility — consistent with
   ADR-001's orchestration-vs-governance split, extended here to cost-truth-vs-enforcement.

Built in stages: the service itself first (this ADR — 22 tests, verified against a live running
instance, not just mocks), consumer wiring in AegisAI and AegisLoop as a tracked follow-up.

## Consequences

### Positive
- One canonical pricing table (`agent_finops.pricing.RATES`) instead of drifting per-repo copies.
- Schema supports `scope_type="tenant"` for real cross-platform budget totals once more than one
  consumer is wired — impossible with siloed per-repo FinOps modules.
- Adds an 18th repo to the org with the same documentation discipline as the other 17: honest
  status table, ADR, architecture/product docs, demo, CI.

### Negative
- A new service to deploy and keep available; the SDK's local-fallback mode exists specifically
  so this is non-fatal.
- Doesn't fix the two fake dashboards by itself — that's Stage 2, not yet done. Until AegisAI and
  AegisLoop are wired as consumers, this ADR closes the "what should replace them" architecture
  question but not the "are they actually replaced" product question.

### Follow-ups
- Wire `aegisai-enterprise-agent-platform`'s `WebsiteBuildOrchestrator` (5 agents map 1:1 to
  existing registry entries) as the first consumer, budget breach → existing `KillSwitchService`.
- Wire `aegisloop-agentops-workbench`'s mission runtime as the second consumer.
- Update both repos' README FinOps rows and the portfolio's FinOps thesis card once real.

## References
- [agent-finops](https://github.com/vpeetla-ai/agent-finops), specifically
  [ADR-0001](https://github.com/vpeetla-ai/agent-finops/blob/main/docs/adr/0001-standalone-cost-governance-service.md)
  (the repo-local decision record this ADR summarizes at the org level)
- [ORG_IMPROVEMENT_PLAN_2026.md](../docs/ORG_IMPROVEMENT_PLAN_2026.md) Phase 6
- [ADR-001: Orchestration vs governance split](./ADR-001-orchestration-vs-governance-split.md)

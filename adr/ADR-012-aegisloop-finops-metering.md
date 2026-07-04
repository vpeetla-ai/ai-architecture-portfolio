# ADR-012: Real Usage Metering + Mission Budget Guard for AegisLoop

## Status

Accepted — 2026-07-04

## Context

`aegisloop-agentops-workbench`'s `finops.py::estimate_mission_cost` computed cost from output
character count and trace-entry heuristics, even in `gateway` mode where a real OpenAI-compatible
call is made and the response's real `usage` field is available and discarded — the second half
of the gap [ADR-011](./ADR-011-agent-finops-standalone-service.md) built `agent-finops` to fix,
alongside AegisAI's identical pattern (see [ADR-011](./ADR-011-agent-finops-standalone-service.md)
and [aegisai ADR-0004](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform/blob/main/adr/0004-real-finops-metering-website-build.md)).

Only two of five mission types (`research`, `content`) call an LLM at all — `incident`,
`migration`, and `security` are fully deterministic/heuristic and were never in scope. Unlike
AegisAI, this repo has no persistent per-agent registry to attribute cost against, and no
kill-switch to trip on a breach.

## Decision

1. `LLMClient.complete()` now returns a `CompletionResult` (`text`, `provider`, `model`,
   `prompt_tokens`, `completion_tokens`) instead of a bare `str | None`. `OllamaClient` parses
   real `prompt_eval_count`/`eval_count` from Ollama's own response (real counts even though
   local inference is genuinely free — honest metering, not just honest cost).
   `NetlifyAIGatewayClient` parses real `usage.prompt_tokens`/`completion_tokens` from the
   OpenAI-compatible response, previously discarded.
2. A shared `Agent.meter_llm()` on the base class (used by both `research.py`'s and
   `content.py`'s LLM-calling agents) calls `agent_finops_client.FinOpsClient.record_usage(...)`
   against a **stable** scope (`scope_type="repo", scope_value="aegisloop-agentops-workbench"`)
   — not the ephemeral per-mission `run_id`, which an operator could never pre-set a budget
   against via agent-finops's `PUT /v1/budget` before the mission exists.
3. **Two independent halt conditions**, either can stop the mission: agent-finops's own
   `breached` signal on that stable scope (a real, settable cross-mission budget), and a local
   `MISSION_BUDGET_USD` threshold (default $2.00) checked against `context.finops_cost_usd`
   accumulated within a single mission run. The mission loop in `runtime.py` (`run_mission` and
   `stream_mission`) now breaks out of the agent loop when `context.finops_breached` is set,
   instead of dispatching every agent unconditionally.
4. `finops.py` (the heuristic) is deleted, not deprecated — nothing called it after this change,
   and this org's convention is to remove dead code rather than leave it commented out.

## Consequences

### Positive
- Both real-LLM mission types are now honestly metered — this closes AegisLoop's half of the
  gap that motivated `agent-finops` in the first place.
- The stable-scope choice means an operator can actually configure a meaningful cross-mission
  budget, unlike a naive per-run_id scope that could never be pre-configured.
- 9 new tests: real Ollama/Netlify token parsing (mocked HTTP), metering no-ops on zero-token
  completions, cost accumulation, both halt conditions independently verified.

### Negative
- No kill-switch exists here (unlike AegisAI) — enforcement is "refuse to dispatch further
  agents in this mission," not a persistent block on future missions. A repeat offender would
  need the stable-scope budget in agent-finops to actually be set and stay breached.
- `incident`/`migration`/`security` missions remain unmetered — correctly, since they never call
  an LLM, but worth stating explicitly so it doesn't read as an oversight.
- Same caveat as every other opt-in gate this session: `AGENTFINOPS_API_URL` unset means cost is
  computed locally and never reported as breached to agent-finops (only the local
  `MISSION_BUDGET_USD` check still applies).

## References
- `services/api/src/agent_loop/llm.py::CompletionResult`
- `services/api/src/agent_loop/agents/base.py::Agent.meter_llm`
- `services/api/src/agent_loop/runtime.py::run_mission`, `stream_mission`
- `services/api/tests/test_finops_metering.py`, `test_llm_usage_parsing.py`
- [agent-finops](https://github.com/vpeetla-ai/agent-finops)

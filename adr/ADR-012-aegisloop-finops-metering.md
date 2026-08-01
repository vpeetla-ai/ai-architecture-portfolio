# ADR-012: Real Usage Metering + Mission Budget Guard for AegisLoop

## Status

Accepted — 2026-07-04

## In one breath (panel)

I'd meter AegisLoop from real provider token counts, delete the character-count heuristic, and halt the mission on budget breach — inventing FinOps from string length was the scar that forced agent-finops.

## Context

`aegisloop-agentops-workbench`'s `finops.py::estimate_mission_cost` computed cost from output
character count and trace-entry heuristics, even in `gateway` mode where a real
OpenAI-compatible call returns `usage` and we threw it away — AegisLoop's half of the gap
[ADR-011](./ADR-011-agent-finops-standalone-service.md) built `agent-finops` to fix (AegisAI's
half: [aegisai ADR-0004](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform/blob/main/adr/0004-real-finops-metering-website-build.md)).

Only two of five mission types (`research`, `content`) call an LLM — `incident`, `migration`,
and `security` are deterministic/heuristic and were never in scope. Unlike AegisAI, this repo
has no persistent per-agent registry and no kill-switch. I refused deprecating the heuristic
"for later" while still showing a FinOps number in the UI.

## Decision

1. `LLMClient.complete()` returns a `CompletionResult` (`text`, `provider`, `model`,
   `prompt_tokens`, `completion_tokens`) instead of a bare `str | None`. `OllamaClient` parses
   real `prompt_eval_count`/`eval_count` (honest metering even when local inference is free).
   `NetlifyAIGatewayClient` parses real `usage.prompt_tokens`/`completion_tokens`, previously
   discarded.
2. Shared `Agent.meter_llm()` records via `agent_finops_client.FinOpsClient.record_usage(...)`
   against a **stable** scope (`scope_type="repo", scope_value="aegisloop-agentops-workbench"`)
   — not ephemeral `run_id`, which an operator could never pre-budget via `PUT /v1/budget`.
3. **Two independent halt conditions**, either can stop the mission: agent-finops `breached` on
   that stable scope, and a local `MISSION_BUDGET_USD` threshold (default $2.00) against
   `context.finops_cost_usd` within one run. `runtime.py` (`run_mission` / `stream_mission`)
   breaks out when `context.finops_breached` is set instead of dispatching every agent
   unconditionally.
4. Delete `finops.py` (the heuristic) — nothing called it after this change; we remove dead
   code rather than leave it commented.

## Consequences

### Positive
- Both real-LLM mission types are honestly metered — closes AegisLoop's half of the ADR-011 gap.
- Stable-scope choice means an operator can actually set a cross-mission budget.
- 9 new tests: real Ollama/Netlify token parsing (mocked HTTP), metering no-ops on zero-token
  completions, cost accumulation, both halt conditions independently verified.

### Negative
- No kill-switch here (unlike AegisAI) — enforcement is "refuse further agents in this mission,"
  not a persistent block on future missions. Repeat offenders need the stable-scope budget set
  and remaining breached in agent-finops.
- `incident`/`migration`/`security` stay unmetered — correctly, since they never call an LLM;
  say so explicitly so it doesn't read as an oversight.
- Opt-in gate: `AGENTFINOPS_API_URL` unset means cost is local only; only `MISSION_BUDGET_USD`
  still applies. Demo-open vs wired-up honesty.

## References
- `services/api/src/agent_loop/llm.py::CompletionResult`
- `services/api/src/agent_loop/agents/base.py::Agent.meter_llm`
- `services/api/src/agent_loop/runtime.py::run_mission`, `stream_mission`
- `services/api/tests/test_finops_metering.py`, `test_llm_usage_parsing.py`
- [agent-finops](https://github.com/vpeetla-ai/agent-finops)

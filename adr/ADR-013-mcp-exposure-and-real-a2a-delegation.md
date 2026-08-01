# ADR-013: Bidirectional MCP + Real A2A Discovery (AegisAI, VAP, AegisLoop)

## Status

Accepted — 2026-07-04

## In one breath (panel)

I'd expose AegisAI's governed tools as MCP and make AegisLoop a real A2A client against VAP's agent cards — a server nobody calls and a one-way MCP proxy aren't a protocol story.

## Context

[ADR-009](./ADR-009-vap-auth-gate.md) corrected the record: VAP's A2A implementation
(`backend/app/api/routes/a2a.py`) is real. Two adjacent gaps remained while mapping the org
against a well-known 15-step AI Architect roadmap (agentic / protocol trends step):

1. **MCP was one-directional.** AegisAI's `McpGovernanceProxy`
   (`application/gateway/mcp_proxy.py`) gates *outbound* MCP tool calls agents make to external
   servers — but nothing *exposed* AegisAI's own governed capabilities as MCP tools an external
   client (Claude Code, Cursor, Claude Desktop) could call.
2. **VAP's A2A discovery surface was never actually called.** AegisLoop's
   `integrations/vap_delegate.py::delegate_to_vap` already delegated missions to VAP
   (`VAP_DELEGATION_ENABLED=true`) — but it picked the orchestrator from a hardcoded local dict
   (`MISSION_ORCHESTRATOR`) and POSTed straight to `/orchestrators/{id}/run`, never hitting
   `/orchestrators/{id}/agent-card`. VAP was a real A2A *server*; nothing in the org was a real
   A2A *client*.

I refused claiming "we do MCP and A2A" while both loops were half-closed.

## Decision

**MCP exposure** lives inside `aegisai-enterprise-agent-platform` (deepens the gateway identity;
not a new repo): `interfaces/mcp/server.py` (`mcp.server.fastmcp.FastMCP`) exposes four tools —
`list_registered_agents`, `check_agent_budget`, `get_kill_switch_status`, `run_website_build` —
importing the same module-level singletons `interfaces/http/api.py` already builds.
`run_website_build` calls the same `WebsiteBuildOrchestrator` instance an HTTP caller would, so
FinOps metering and kill-switch ([aegisai ADR-0004](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform/blob/main/adr/0004-real-finops-metering-website-build.md))
apply to MCP callers — a second front door onto the same governed core, not a bypass. See
[aegisai ADR-0005](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform/blob/main/adr/0005-mcp-tool-exposure.md).

**Real A2A delegation**: `vap_delegate.py::delegate_to_vap` now calls `_fetch_agent_card()` —
a real `GET /orchestrators/{id}/agent-card` — before `POST /orchestrators/{id}/run`. If
discovery fails, delegation returns `None` and the existing local-fleet fallback in `runtime.py`
takes over unchanged. VAP is the A2A server; AegisLoop is the org's first real A2A client.

## Consequences

### Positive
- MCP is bidirectional: gate outbound (agent → external MCP) and expose inbound (external
  client → AegisAI), both tested.
- A2A moves from "one repo has a server nobody calls" to "server + real, tested client" — the
  protocol loop is closed.
- No duplicated business logic — thin protocol adapters over code that already existed and was
  already governed.
- 7 new tests in aegisai (`test_mcp_tool_exposure.py`) + 3 in aegisloop
  (`test_vap_a2a_discovery.py`), plus live verification: a local VAP instance served a genuine
  `agent-card` to AegisLoop (downstream `/run` then failed only because no LLM key was set in
  that ad hoc env — environment gap, not code; graceful-`None` fallback handled it).

### Negative
- MCP's `run_website_build` has no HTTP session for identity, so
  `AEGISAI_ENFORCE_AUTH=true` needs the MCP caller to pass `principal_id` explicitly — real
  ergonomic gap vs header-based HTTP auth.
- `delegate_to_vap`'s discovery + run are still two sequential HTTP calls with no shared
  session/retry budget; flaky networks can fail discovery even when `/run` would succeed.
  Accepted for genuine protocol compliance.

## References
- `aegisai-enterprise-agent-platform/services/api/src/aegisai/interfaces/mcp/server.py`
- `aegisai-enterprise-agent-platform/adr/0005-mcp-tool-exposure.md`
- `aegisloop-agentops-workbench/services/api/src/agent_loop/integrations/vap_delegate.py`
- `venkat-ai-platform/backend/app/api/routes/a2a.py`
- [ADR-009: VAP auth gate (documents VAP's A2A server is real)](./ADR-009-vap-auth-gate.md)

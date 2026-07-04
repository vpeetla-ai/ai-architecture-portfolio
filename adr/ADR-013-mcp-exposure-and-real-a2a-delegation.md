# ADR-013: Bidirectional MCP + Real A2A Discovery (AegisAI, VAP, AegisLoop)

## Status

Accepted — 2026-07-04

## Context

[ADR-009](./ADR-009-vap-auth-gate.md) corrected the record that VAP's A2A implementation
(`backend/app/api/routes/a2a.py`) is real, not absent. But two adjacent gaps remained,
both found while mapping this org against a well-known 15-step "AI Architect roadmap"
(the step covering agentic-AI/protocol trends):

1. **MCP was one-directional.** `aegisai-enterprise-agent-platform`'s `McpGovernanceProxy`
   (`application/gateway/mcp_proxy.py`) gates *outbound* MCP tool calls agents make to
   external servers — but nothing in the org *exposed* AegisAI's own governed capabilities
   as MCP tools an external client (Claude Code, Cursor, Claude Desktop) could call.
2. **VAP's real A2A discovery surface was never actually called.** `aegisloop-agentops-
   workbench`'s existing `integrations/vap_delegate.py::delegate_to_vap` already delegated
   full missions to VAP (`VAP_DELEGATION_ENABLED=true`) — but it picked the target
   orchestrator from a hardcoded local dict (`MISSION_ORCHESTRATOR`) and POSTed straight to
   `/orchestrators/{id}/run`, never calling VAP's own `/orchestrators/{id}/agent-card`
   discovery endpoint. VAP was a real A2A *server*; nothing in the org was a real A2A
   *client*.

## Decision

**MCP exposure** lives inside `aegisai-enterprise-agent-platform` (deepens its existing
gateway identity, rather than a new repo): new `interfaces/mcp/server.py` (`mcp.server.
fastmcp.FastMCP`) exposes four tools — `list_registered_agents`, `check_agent_budget`,
`get_kill_switch_status`, `run_website_build` — importing the same module-level singletons
`interfaces/http/api.py` already builds. `run_website_build` calls the exact same
`WebsiteBuildOrchestrator` instance an HTTP caller would, so real FinOps metering and
kill-switch enforcement ([ADR-0004](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform/blob/main/adr/0004-real-finops-metering-website-build.md))
apply identically to MCP callers — a second front door onto the same governed core, not a
parallel bypass. See [aegisai ADR-0005](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform/blob/main/adr/0005-mcp-tool-exposure.md).

**Real A2A delegation**: `vap_delegate.py::delegate_to_vap` now calls a new
`_fetch_agent_card()` — a real `GET /orchestrators/{id}/agent-card` — before ever invoking
`POST /orchestrators/{id}/run`. If discovery fails, delegation returns `None` and the
existing graceful fallback to the local agent fleet in `runtime.py` takes over unchanged.
This turns an already-real (but protocol-agnostic) HTTP call into genuine discover-then-
invoke A2A semantics: VAP is the A2A server, AegisLoop is the org's first real A2A client.

## Consequences

### Positive
- MCP is now bidirectional across the org: gate inbound (agent → external MCP server) and
  expose outbound (external client → AegisAI) both exist and are tested.
- A2A moves from "one repo has a real server nobody calls" to "one repo has a real server,
  another repo is a real, tested client" — the actual protocol loop is closed.
- No duplicated business logic in either case — both changes are thin protocol adapters over
  code that already existed and was already governed/tested.
- 7 new tests in `aegisai` (`test_mcp_tool_exposure.py`) + 3 new tests in `aegisloop`
  (`test_vap_a2a_discovery.py`), plus a live verification: a real local VAP instance served a
  genuine `agent-card` response to AegisLoop's discovery call (the downstream `/run` call
  then failed only because no LLM API key was configured in that ad hoc local environment —
  an environment gap, not a code gap; the existing graceful-`None` fallback handled it
  correctly).

### Negative
- MCP's `run_website_build` tool has no HTTP session to resolve identity from, so principal
  enforcement (`AEGISAI_ENFORCE_AUTH=true`) requires the MCP caller to pass `principal_id`
  explicitly — a real, if minor, ergonomic gap versus header-based HTTP auth.
- `delegate_to_vap`'s discovery + run are still two sequential HTTP calls with no shared
  session/retry budget; a flaky network could fail discovery even when `/run` itself would
  have succeeded. Accepted as a reasonable tradeoff for genuine protocol compliance.

## References
- `aegisai-enterprise-agent-platform/services/api/src/aegisai/interfaces/mcp/server.py`
- `aegisai-enterprise-agent-platform/adr/0005-mcp-tool-exposure.md`
- `aegisloop-agentops-workbench/services/api/src/agent_loop/integrations/vap_delegate.py`
- `venkat-ai-platform/backend/app/api/routes/a2a.py`
- [ADR-009: VAP auth gate (documents VAP's A2A server is real)](./ADR-009-vap-auth-gate.md)

# ADR-010: API-Key Gate on AegisLoop's Mission-Run Routes (Backend + Netlify Function)

## Status

Accepted — 2026-07-03

## Context

`POST /api/missions/run` and `POST /api/missions/stream`
(`aegisloop-agentops-workbench/services/api/src/agent_loop/main.py`) had no caller
authentication at all, despite invoking a real LLM per hit. The same gap existed
independently in the standalone Netlify serverless function
(`infra/netlify/functions/mission-run.ts`), which calls OpenAI directly in `gateway` mode and
also proxies to the FastAPI backend when `AGENT_LOOP_API_URL` is configured — two separate
unauthenticated entry points to the same cost surface, matching the pattern found and fixed in
5 other org repos this session (loop-engine-agent-platform ADR-002, sentinel-brief ADR-0002,
aegisai-enterprise-agent-platform ADR-0003, VAP ADR-009, enterprise_rag_platform ADR-0004).

## Decision

1. Add an `AEGISLOOP_API_KEY`-gated check to both entry points — `_require_api_key` in the
   FastAPI backend's `main.py`, and an equivalent header check in the Netlify function — each
   enforced only when the env var is set (dev/demo defaults stay open).
2. When the Netlify function proxies to the FastAPI backend, it now forwards the same key as
   an `X-API-Key` header, so turning on enforcement on the backend doesn't silently break the
   proxy path.
3. Add an optional, browser-local API-key field to the static demo UI
   (`app/index.html`/`app/app.js`), sent only if filled in — never baked into the deployed
   static bundle.

## Consequences

### Positive
- Closes a real gap present in *two* independent code paths (Python backend and TypeScript
  serverless function) that both reach the same underlying cost surface.
- Consistent with the identical fix pattern now applied across 6 repos in the org.

### Negative
- `AEGISLOOP_API_KEY` must be set on both Render (backend) and Netlify (function) — and kept
  in sync between them — for enforcement to actually take effect; unset on either side leaves
  that entry point open.
- `/health`, `/api/missions`, and `/api/runs` remain intentionally open (read-only, low cost,
  meant to be publicly browsable per this repo's portfolio-demo positioning).

## References
- `aegisloop-agentops-workbench/services/api/src/agent_loop/main.py::_require_api_key`
- `aegisloop-agentops-workbench/infra/netlify/functions/mission-run.ts`
- Same pattern: [loop-engine-agent-platform ADR-002](https://github.com/vpeetla-ai/loop-engine-agent-platform/blob/main/docs/ADR-002-repo-fix-auth-and-isolation.md), [sentinel-brief ADR-0002](https://github.com/vpeetla-ai/sentinel-brief/blob/main/docs/adr/0002-runs-auth-and-llm-synthesis.md), [aegisai ADR-0003](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform/blob/main/adr/0003-orchestrator-auth-gate.md), [VAP ADR-009](./ADR-009-vap-auth-gate.md), [enterprise_rag_platform ADR-0004](https://github.com/vpeetla-ai/enterprise_rag_platform/blob/main/docs/adr/0004-api-auth-and-principal-trust.md)

# ADR-010: API-Key Gate on AegisLoop's Mission-Run Routes (Backend + Netlify Function)

## Status

Accepted — 2026-07-03

## In one breath (panel)

I'd gate both AegisLoop entry points that burn LLM — FastAPI and the Netlify function — with the same API key, because fixing one and leaving the other open is how you fake a security story.

## Context

`POST /api/missions/run` and `POST /api/missions/stream`
(`aegisloop-agentops-workbench/services/api/src/agent_loop/main.py`) had no caller auth despite
invoking a real LLM per hit. The same gap lived independently in the Netlify serverless
function (`infra/netlify/functions/mission-run.ts`), which calls OpenAI directly in `gateway`
mode and also proxies to FastAPI when `AGENT_LOOP_API_URL` is set — two unauthenticated doors
onto the same cost surface. Same scar pattern already fixed in five other org repos that
session (LoopForge ADR-002, sentinel-brief ADR-0002, aegisai ADR-0003, VAP ADR-009, enterprise
RAG ADR-0004).

I refused "we secured the Python path" while the Netlify function stayed public.

## Decision

1. Add an `AEGISLOOP_API_KEY`-gated check to both entry points — `_require_api_key` in FastAPI
   `main.py`, and an equivalent header check in the Netlify function — each enforced only when
   the env var is set (dev/demo stays open).
2. When Netlify proxies to FastAPI, forward the same key as `X-API-Key` so turning on backend
   enforcement doesn't silently break the proxy.
3. Optional browser-local API-key field in the static demo UI (`app/index.html` / `app/app.js`),
   sent only if filled in — never baked into the static bundle.

## Consequences

### Positive
- Closes a real gap in *two* independent code paths that share one cost surface.
- Same fix pattern now across six repos.

### Negative
- `AEGISLOOP_API_KEY` must be set on **both** Render and Netlify — and kept in sync — or one
  door stays open. **Demo vs Strict:** unset = open; set = gated.
- `/health`, `/api/missions`, and `/api/runs` stay intentionally open (read-only, low cost,
  portfolio-demo browsing). That's a product choice, not an oversight — label it.

## References
- `aegisloop-agentops-workbench/services/api/src/agent_loop/main.py::_require_api_key`
- `aegisloop-agentops-workbench/infra/netlify/functions/mission-run.ts`
- Same pattern: [loop-engine-agent-platform ADR-002](https://github.com/vpeetla-ai/loop-engine-agent-platform/blob/main/docs/ADR-002-repo-fix-auth-and-isolation.md), [sentinel-brief ADR-0002](https://github.com/vpeetla-ai/sentinel-brief/blob/main/docs/adr/0002-runs-auth-and-llm-synthesis.md), [aegisai ADR-0003](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform/blob/main/adr/0003-orchestrator-auth-gate.md), [VAP ADR-009](./ADR-009-vap-auth-gate.md), [enterprise_rag_platform ADR-0004](https://github.com/vpeetla-ai/enterprise_rag_platform/blob/main/docs/adr/0004-api-auth-and-principal-trust.md)

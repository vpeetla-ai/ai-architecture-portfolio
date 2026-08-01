# ADR-009: API-Key Gate on VAP's Chat/Orchestrator/Ingest/RAG/Threads Routes

## Status

Accepted — 2026-07-03

## In one breath (panel)

I'd put an API-key gate on every VAP route that spends LLM money, writes vectors, notifies channels, or reads thread history — leaving those open on a public Render URL was a live scar, not a demo feature.

## Context

A security audit of `venkat-ai-platform` found `POST /chat`, `POST /chat/stream`,
`POST /orchestrators/{id}/run`, `POST /ingest`, `POST /rag/retrieve`, and
`GET /threads/{id}/messages` had **no authentication dependency at all**
(`backend/app/api/routes/{chat,orchestrators,ingest,rag,threads}.py`) — the only `Depends(...)`
was `get_db`. Every one of those routes matters if an anonymous caller hits them:

- `/chat` and `/orchestrators/{id}/run` invoke the LangGraph pipeline (real LLM calls) and can
  set `notify_channels` — a **real** Slack/Telegram/WhatsApp message with no gate.
- `/ingest` writes into Qdrant (and optionally Pinecone) — corpus poisoning.
- `/rag/retrieve` burns embedding + vector query compute per call.
- `/threads/{id}/messages` returns chat history given only the UUID — info leak if a thread ID
  is logged or shared.

`render.yaml` deploys this publicly; the Vercel frontend calls these routes with `fetch` — no
server-side proxy, no credential. Same pattern we'd already fixed in three other org repos
(`loop-engine-agent-platform` ADR-002, `sentinel-brief` ADR-0002, `aegisai` ADR-0003). VAP
simply had no auth mechanism yet.

Two earlier claims still held: Pinecone is ingest-mirror-only (Qdrant is the query path —
`app/memory/vector_store.py`), and there is no HITL UI (README already says pair with AegisAI).
One assumption we corrected: VAP has a **real** A2A surface (`backend/app/api/routes/a2a.py`),
contrary to an earlier "no A2A in the org" finding. I refused leaving the spend/notify paths
open while celebrating A2A discovery.

## Decision

1. Add a `VAP_API_KEY`-gated `require_api_key` dependency (`backend/app/api/deps.py`), enforced
   only when the env var is set (dev/demo default stays open — same pattern as the sibling
   ADRs), applied to all six routes above.
2. A2A discovery endpoints (`/.well-known/agent.json`, `/a2a/agent-card`,
   `/orchestrators/{id}/agent-card`) stay open — public by A2A spec.
3. Optional, browser-local-only API key field on the Settings page
   (`frontend/src/app/settings/page.tsx`, zustand-persist) so the UI keeps working once
   `VAP_API_KEY` is set — never baked into the deployed bundle.
4. `run_daily_brief` (ARQ cron) runs in-process, not over HTTP — unaffected; no cron caller
   update needed here.

## Consequences

### Positive
- Closes a real live gap: anonymous callers could burn LLM spend, spam notify channels, poison
  the vector store, or read any thread.
- Same fix pattern now across four repos.
- Corrects the A2A record — real server, not absent — which matters for the 2026 protocol story.

### Negative
- `VAP_API_KEY` must actually be set on Render (and typed into Settings) or nothing changes —
  same manual deploy step as the other fixes. **Demo vs Strict:** unset = open (demo); set =
  gated.
- Durable scheduled-job gap (ARQ + Redis only) remains — separate infra decision.
- FinOps-style real cost tracking was out of scope here (ADR-011 later).

### Follow-ups
- Durable job queue for VAP's scheduled cron (replace or back Redis/ARQ with a persisted queue).

## References
- `backend/app/api/deps.py::require_api_key`
- `backend/app/api/routes/{chat,orchestrators,ingest,rag,threads}.py`
- Same pattern: [loop-engine-agent-platform ADR-002](https://github.com/vpeetla-ai/loop-engine-agent-platform/blob/main/docs/ADR-002-repo-fix-auth-and-isolation.md), [sentinel-brief ADR-0002](https://github.com/vpeetla-ai/sentinel-brief/blob/main/docs/adr/0002-runs-auth-and-llm-synthesis.md), [aegisai-enterprise-agent-platform ADR-0003](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform/blob/main/adr/0003-orchestrator-auth-gate.md)

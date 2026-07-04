# ADR-009: API-Key Gate on VAP's Chat/Orchestrator/Ingest/RAG/Threads Routes

## Status

Accepted — 2026-07-03

## Context

A security audit of `venkat-ai-platform` (part of an org-wide review this session) found
`POST /chat`, `POST /chat/stream`, `POST /orchestrators/{id}/run`, `POST /ingest`,
`POST /rag/retrieve`, and `GET /threads/{id}/messages` had **no authentication dependency at
all** (`backend/app/api/routes/{chat,orchestrators,ingest,rag,threads}.py`) — the only
`Depends(...)` in any of these files was `get_db` for the database session, not an auth check.
Every one of these routes does something that matters if triggered by an anonymous caller:

- `/chat` and `/orchestrators/{id}/run` invoke the LangGraph pipeline (real LLM calls) and can
  set `notify_channels`, which sends a **real message to Slack/Telegram/WhatsApp** — an
  irreversible external side effect with no gate at all.
- `/ingest` writes directly into the Qdrant (and optionally Pinecone) vector store — anyone
  could poison the RAG corpus.
- `/rag/retrieve` runs a real embedding + vector query per call (compute cost).
- `/threads/{id}/messages` returns a user's chat history given only the UUID — no ownership
  check, an info-leak if a thread ID is ever logged or shared.

`render.yaml` deploys this publicly on Render with a Vercel frontend that calls these routes
directly with `fetch` — no server-side proxy, no credential. This matches a pattern found and
fixed in 3 other org repos this session (`loop-engine-agent-platform` ADR-002, `sentinel-brief`
ADR-0002, `aegisai-enterprise-agent-platform` ADR-0003) — VAP simply hadn't had any auth
mechanism at all yet, rather than having one that was inconsistently applied.

Two claims from an earlier eagle-view review were re-verified and confirmed still accurate:
Pinecone is genuinely ingest-mirror-only (Qdrant is the sole query path —
`app/memory/vector_store.py`), and there is no HITL approval UI (README already says "pair with
AegisAI for full queue"). One assumption from the org-wide 2026-trends analysis was corrected:
VAP has a **real** A2A (Agent-to-Agent) implementation (`backend/app/api/routes/a2a.py` —
`.well-known/agent.json` discovery + per-orchestrator agent cards), contradicting the earlier
"no A2A anywhere in the org" finding.

## Decision

1. Add a `VAP_API_KEY`-gated `require_api_key` dependency (`backend/app/api/deps.py`), enforced
   only when the env var is set (dev/demo default stays open — same pattern as the other 3
   ADRs above), applied to all 6 routes listed above.
2. A2A's discovery endpoints (`/.well-known/agent.json`, `/a2a/agent-card`,
   `/orchestrators/{id}/agent-card`) stay open — they're meant to be public per the A2A spec.
3. Add an optional, browser-local-only API key field to the frontend's Settings page
   (`frontend/src/app/settings/page.tsx`, backed by `useSettingsStore`'s existing
   zustand-persist pattern, same as its notify-channel toggles) so the real product UI keeps
   working once `VAP_API_KEY` is set — not baked into the deployed bundle, just stored in the
   browser that types it in.
4. `run_daily_brief` (the ARQ-scheduled cron job) runs in-process, not over HTTP, so it's
   unaffected by this gate — no cron caller needed updating here (unlike the other 3 repos).

## Consequences

### Positive
- Closes a real, live gap: an anonymous caller could previously trigger LLM spend, spam real
  Slack/Telegram/WhatsApp channels, poison the vector store, or read any thread's chat history.
- Consistent with the same fix pattern now applied across 4 repos in the org.
- Corrects the record on A2A — it's real, not absent, which matters for how the org's
  2026-protocol-stack story gets told going forward.

### Negative
- `VAP_API_KEY` must actually be set on Render (and the frontend Settings page filled in) for
  this to matter — same manual deploy step required in the other 3 fixes.
- The durable-scheduled-job gap (ARQ + Redis only, no persistence if Redis is down when the
  daily brief fires) remains unresolved — a separate infra decision, not addressed here.
- FinOps-style real cost tracking is out of scope here too, consistent with ADR-0003's finding
  in the sibling aegisai repo.

### Follow-ups
- ADR-010 (proposed): durable job queue for VAP's scheduled cron (replace or back Redis/ARQ
  with a persisted queue).

## References
- `backend/app/api/deps.py::require_api_key`
- `backend/app/api/routes/{chat,orchestrators,ingest,rag,threads}.py`
- Same pattern: [loop-engine-agent-platform ADR-002](https://github.com/vpeetla-ai/loop-engine-agent-platform/blob/main/docs/ADR-002-repo-fix-auth-and-isolation.md), [sentinel-brief ADR-0002](https://github.com/vpeetla-ai/sentinel-brief/blob/main/docs/adr/0002-runs-auth-and-llm-synthesis.md), [aegisai-enterprise-agent-platform ADR-0003](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform/blob/main/adr/0003-orchestrator-auth-gate.md)

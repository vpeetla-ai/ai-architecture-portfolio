# Trace-linked observability — LLMOps pattern

Canonical package: `packages/vpeetla_observability/`

**Org spec:** three evaluation levels linked to one `trace_id` — export to Langfuse when `LANGFUSE_*` keys are set.

## Three evaluation levels

| Level | Question | Examples |
|-------|----------|----------|
| **system** | Did the workflow complete? | `pipeline.execute`, `sentinel_brief.run` |
| **trace** | Which path did the agent take? | `source.hn`, `gateway.authorize_email`, `eval.brief_gate` |
| **node** | Was each step correct? | `research`, `fetch_sources`, `llm.research` |

## Platform adoption

| Repo | Integration | Import path |
|------|-------------|-------------|
| **ai-content-factory** | ✅ Full — middleware, pipeline, all graph nodes | `app.vpeetla_observability.*` |
| **sentinel-brief** | ✅ Full — brief runner + graph nodes | `app.vpeetla_observability.*` |
| **aegisloop** | ✅ Mission spans + Langfuse export | `agent_loop.vpeetla_observability.*` (synced) |
| **venkat-ai-platform** | 🟡 Package synced; wire middleware on integrate | `app.vpeetla_observability.*` |
| **loop-engine** | 🟡 Package synced + legacy `langfuse_export.py` | `loop_engine.vpeetla_observability.*` |
| **aegisai** | 🟡 Package synced + LangSmith/Langfuse bootstrap | `aegisai.vpeetla_observability.*` |
| **enterprise_rag** | ✅ Langfuse export on `/v1/answer` | `enterprise_rag.ops.langfuse_export` |

## Sync to platform repos

```bash
./scripts/sync-observability.sh
```

## Usage in FastAPI + LangGraph

Import path varies by repo layout — always use the **namespaced copy** under `app/` (or equivalent), not a top-level `vpeetla_observability` package:

```python
from app.vpeetla_observability.middleware import TraceRequestMiddleware
from app.vpeetla_observability.observe import observe_node
from app.vpeetla_observability.recorder import TraceRecorder, set_recorder
from app.vpeetla_observability.spans import eval_score, system_span

app.add_middleware(TraceRequestMiddleware, service_name="my-api")

@observe_node("research")
async def research_node(state):
    ...

recorder = TraceRecorder.create(run_id=run_id, trace_id=run_id)
set_recorder(recorder)
with system_span("workflow.run"):
    result = await graph.ainvoke({"run_id": run_id, "trace_id": run_id})
with eval_score("task.success", True):
    pass
```

## Langfuse keys

Set in local `.env` and production dashboard (never commit secrets):

```bash
LANGFUSE_PUBLIC_KEY=pk-lf-...
LANGFUSE_SECRET_KEY=sk-lf-...
LANGFUSE_HOST=https://cloud.langfuse.com
LANGFUSE_ENABLED=true
```

Get keys: [cloud.langfuse.com](https://cloud.langfuse.com) → Project → Settings → API Keys.

Per-repo deploy notes: `ai-content-factory/docs/DEPLOYMENT.md` §8, `sentinel-brief/docs/DEPLOY.md`.

## Leadership takeaway

Observability tells you **what happened**. Trace-linked evaluation tells you **whether it was good, why it failed, and what to fix next**.

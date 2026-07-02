# Trace-linked observability — LLMOps pattern

Canonical package: `packages/vpeetla_observability/`

## Three evaluation levels

| Level | Question | Examples |
|-------|----------|----------|
| **system** | Did the workflow complete? | `pipeline.execute`, `sentinel_brief.run` |
| **trace** | Which path did the agent take? | `source.hn`, `gateway.authorize_email`, `eval.brief_gate` |
| **node** | Was each step correct? | `research`, `fetch_sources`, `llm.research` |

## Sync to platform repos

```bash
./scripts/sync-observability.sh
```

## Usage in FastAPI + LangGraph

```python
from vpeetla_observability.middleware import TraceRequestMiddleware
from vpeetla_observability.observe import observe_node
from vpeetla_observability.recorder import TraceRecorder, set_recorder
from vpeetla_observability.spans import eval_score, system_span

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

Set `LANGFUSE_PUBLIC_KEY` + `LANGFUSE_SECRET_KEY` to export traces and eval scores to Langfuse.

## Leadership takeaway

Observability tells you **what happened**. Trace-linked evaluation tells you **whether it was good, why it failed, and what to fix next**.

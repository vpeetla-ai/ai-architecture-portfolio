# vLLM Architecture Lab — Inference Education Platform

**Domain:** LLM inference · KV cache · production serving  
**Live demo:** [vllm-architecture-lab.vercel.app](https://vllm-architecture-lab.vercel.app)  
**API:** [vllm-architecture-lab-api.onrender.com](https://vllm-architecture-lab-api.onrender.com)  
**Source:** [vllm-architecture-lab](https://github.com/vpeetla-ai/vllm-architecture-lab)

## Problem

Platform engineers need to reason about **PagedAttention, continuous batching, and KV memory budgets** before tuning production inference — not just call an API.

## Architecture

```text
Educational simulator (Python)  →  FastAPI  →  Interactive demo UI
```

| Component | Role |
|-----------|------|
| `BlockSpaceManager` | Paged KV blocks — allocation / eviction |
| `Scheduler` | Continuous batching decisions |
| `LLMEngine` | End-to-end request lifecycle |
| FastAPI | `/api/simulate`, `/api/memory/budget`, `/v1/completions` stub |
| Demo UI | 5 tabs: Architecture, KV Cache, Batching, Memory, FDE Relevance |

## Key decisions

- **Simulator-first** — teach mechanics without GPU cluster cost
- **Honest scope** — educational, not a production vLLM fork
- **FDE relevance tab** — maps inference concepts to forward-deployed engineering interviews

## Trade-offs

| Choice | Why | Cost |
|--------|-----|------|
| Python simulator | Readable, testable | Not bit-accurate vs CUDA kernels |
| Render API + Vercel UI | Free-tier portfolio demo | Cold starts |
| Stub OpenAI completions | Shows API shape | No real model weights |

## Impact

- Seventh layer of governed AI stack: **How do LLMs serve at scale?**
- Cross-linked from VAP model-router docs and `vllm-inference` org skill
- 6 pytest cases on engine invariants

## Stack

Python · FastAPI · Vanilla JS demo · Vercel · Render

## Related

- [vllm-inference skill](https://github.com/vpeetla-ai/vpeetla-ai-skills/tree/main/skills/vllm-inference)
- [VAP inference docs](https://github.com/vpeetla-ai/venkat-ai-platform/blob/main/docs/INFERENCE.md)
- Pairs with [LoopForge](https://github.com/vpeetla-ai/loop-engine-agent-platform) (agent loops) and [Enterprise RAG](https://github.com/vpeetla-ai/enterprise_rag_platform) (retrieval)

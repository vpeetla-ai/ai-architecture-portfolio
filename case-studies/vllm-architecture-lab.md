# vLLM Architecture Lab — Inference Education Platform

**Domain:** LLM inference · KV cache · production serving  
**Live demo:** [vllm-architecture-lab.vercel.app](https://vllm-architecture-lab.vercel.app)  
**API:** [vllm-architecture-lab-api.onrender.com](https://vllm-architecture-lab-api.onrender.com)  
**Source:** [vllm-architecture-lab](https://github.com/vpeetla-ai/vllm-architecture-lab)

## Problem

Platform engineers tune production inference before they can reason about PagedAttention, continuous batching, and KV budgets — then wonder why multi-LoRA economics don’t show up. The scar is treating vLLM as a black box and “learning” from vendor slides.

## What we decided

1. **Simulator-first** — teach block allocation, eviction, and batching without an H100 cluster.
2. **Honest scope** — educational lab, **not** a production vLLM fork.
3. **Pair with DomainForge** — adapters come from the MLOps layer; serve path is the ADR-022 target ([ADR-022](../adr/ADR-022-domainforge-vllm-multi-lora-serving.md)).
4. **UI surfaces the mechanics** — Architecture · KV · Batching · Memory · FDE Relevance.

## Architecture

Canonical: [docs/diagrams/canonical-architecture.mmd](https://github.com/vpeetla-ai/vllm-architecture-lab/blob/main/docs/diagrams/canonical-architecture.mmd)

| Component | Role |
|-----------|------|
| `BlockSpaceManager` | Paged KV blocks — allocation / eviction |
| `Scheduler` | Continuous batching decisions |
| `LLMEngine` | End-to-end request lifecycle |
| Demo UI | Architecture · KV · Batching · Memory · FDE Relevance |

```text
DomainForge (train adapters) → Ollama path (today) → vLLM multi-LoRA (target ADR-022)
vLLM Lab (understand WHY serving works) — educational simulator, not production fork
```

## Live proof

- UI: [vllm-architecture-lab.vercel.app](https://vllm-architecture-lab.vercel.app)
- API: [vllm-architecture-lab-api.onrender.com](https://vllm-architecture-lab-api.onrender.com)

## Limitations / what we'd do differently

- This does not serve real CUDA multi-LoRA. Don’t imply DomainForge adapters are already swapped per-request on GPU here.
- Simulator numbers are for intuition; they’re not a load-test of a production cluster.
- Next: keep Path B (ADR-022) clearly labeled Accepted — educational until a real multi-LoRA serve receipt exists.

## Related

[ADR-022](../adr/ADR-022-domainforge-vllm-multi-lora-serving.md) · [DomainForge case study](./domainforge-rag-peft.md)

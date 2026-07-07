# vLLM Architecture Lab — Inference Education Platform

**Domain:** LLM inference · KV cache · production serving  
**Live demo:** [vllm-architecture-lab.vercel.app](https://vllm-architecture-lab.vercel.app)  
**API:** [vllm-architecture-lab-api.onrender.com](https://vllm-architecture-lab-api.onrender.com)  
**Source:** [vllm-architecture-lab](https://github.com/vpeetla-ai/vllm-architecture-lab)

## Problem

Platform engineers need to reason about **PagedAttention, continuous batching, and KV memory budgets** before tuning production inference — and understand how **multi-LoRA serving** changes fine-tune economics.

## Architecture

Canonical: [docs/diagrams/canonical-architecture.mmd](https://github.com/vpeetla-ai/vllm-architecture-lab/blob/main/docs/diagrams/canonical-architecture.mmd)

| Component | Role |
|-----------|------|
| `BlockSpaceManager` | Paged KV blocks — allocation / eviction |
| `Scheduler` | Continuous batching decisions |
| `LLMEngine` | End-to-end request lifecycle |
| Demo UI | Architecture · KV · Batching · Memory · FDE Relevance |

## Train → serve economics (portfolio narrative)

```text
DomainForge (train adapters) → Ollama path (today) → vLLM multi-LoRA (target ADR-022)
vLLM Lab (understand WHY serving works) — educational simulator, not production fork
```

vLLM 0.15+ multi-LoRA enables hundreds of adapters per GPU with per-request swap — this lab teaches the **underlying mechanics** (PagedAttention, batching) that make those economics possible.

## Key decisions

- **Simulator-first** — teach without H100 cluster cost
- **Honest scope** — not a production vLLM fork
- **Pairs with DomainForge** — adapters come from MLOps layer; serve path in [ADR-022](../adr/ADR-022-domainforge-vllm-multi-lora-serving.md)

## Related

[ADR-022: DomainForge → vLLM multi-LoRA target](../adr/ADR-022-domainforge-vllm-multi-lora-serving.md) · [DomainForge case study](domainforge-rag-peft.md)

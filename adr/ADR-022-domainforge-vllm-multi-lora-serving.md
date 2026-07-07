# ADR-022: DomainForge Adapters on vLLM Multi-LoRA Serving (Target)

**Status:** Proposed  
**Date:** Jul 2026  
**Systems:** DomainForge (`domainforge-rag-peft`), vLLM Architecture Lab (`vllm-architecture-lab`)

## Context

DomainForge trains and registers QLoRA/DPO adapters (S3/S4) for structured JSON triage. vLLM 0.15+ ships **multi-LoRA serving** for MoE and dense models — hundreds of adapters on one GPU with per-request swap.

The portfolio today demonstrates:

- **Train + eval** — DomainForge S0→S4 ladder, adapter promote gate
- **Inference education** — vLLM Lab PagedAttention + continuous batching simulator

The gap is a **production serving path** connecting promoted adapters to a multi-LoRA endpoint.

## Decision

Adopt vLLM multi-LoRA as the **target production inference plane** for DomainForge adapters, with Ollama as the intermediate GPU path (already documented in `GPU_OLLAMA_PIPELINE.md`).

```text
Train (GPU) → merge adapter → export
  → Path A: Ollama Modelfile (current)
  → Path B: vLLM LoRA module registry (target)
Serve: single base model + N adapters, swap per request
```

## Architecture (target)

See [vllm-architecture-lab/docs/diagrams/canonical-architecture.mmd](https://github.com/vpeetla-ai/vllm-architecture-lab/blob/main/docs/diagrams/canonical-architecture.mmd) — dashed `DomainForge → multi-LoRA` edge.

## Trade-offs

| Choice | Rationale | Cost |
|--------|-----------|------|
| vLLM multi-LoRA vs one-GPU-per-adapter | Economics at scale; matches industry direction | Ops complexity; GPU host required |
| Ollama first | Simpler portfolio demo on RunPod | Not multi-tenant LoRA at scale |
| Educational lab stays a simulator | Honest scope — not a vLLM fork | No production SLA from lab repo |

## Consequences

- DomainForge README status row: `vLLM production serve` remains **Planned** until Path B is implemented
- LinkedIn narrative: train (DomainForge) + understand (vLLM Lab) + serve (future integration)
- Case study update when bench numbers exist on real vLLM endpoint

## Links

- [DomainForge ADR-019](./ADR-019-rag-facts-peft-behavior.md)
- [DomainForge GPU pipeline](https://github.com/vpeetla-ai/domainforge-rag-peft/blob/main/docs/GPU_OLLAMA_PIPELINE.md)
- [LinkedIn Launch Plan](../docs/LINKEDIN_LAUNCH_PLAN.md)

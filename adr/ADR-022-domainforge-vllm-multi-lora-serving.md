# ADR-022: DomainForge Adapters on vLLM Multi-LoRA Serving

**Status:** Accepted (educational Path B)  
**Date:** Jul 2026 (updated 2026-07-09)  
**Systems:** DomainForge (`domainforge-rag-peft`), vLLM Architecture Lab (`vllm-architecture-lab`)

## Context

DomainForge trains and registers QLoRA/DPO adapters (S3/S4) for structured JSON triage. vLLM 0.15+ ships **multi-LoRA serving** for MoE and dense models — hundreds of adapters on one GPU with per-request swap.

The portfolio demonstrates:

- **Train + eval** — DomainForge S0→S4 ladder, adapter promote gate
- **Inference education** — vLLM Lab PagedAttention + continuous batching simulator
- **Path B (thin slice)** — DomainForge → OpenAI-compatible chat with `adapter_id` on vLLM Lab

## Decision

1. **Path A (current GPU demo):** Ollama Modelfile after merge/export.
2. **Path B (now shipped as educational):** DomainForge `VLLM_BASE_URL` routes PEFT solutions to
   vLLM Lab `POST /v1/chat/completions` with model/`adapter_id` (`domainforge-triage-v0`).
   Lab exposes `GET /v1/adapters` mock registry. **Not** CUDA multi-LoRA kernels or production SLAs.
3. Keep targeting real vLLM multi-LoRA on GPU hosts as the eventual economics proof.

```text
Train (GPU) → merge adapter → export
  → Path A: Ollama Modelfile
  → Path B: vLLM Lab chat + adapter_id (educational; this ADR)
Serve (future): real vLLM LoRA modules on one GPU
```

## Trade-offs

| Choice | Gain | Trade |
|--------|------|-------|
| Educational Path B now | Runnable DomainForge↔vLLM wire for interviews | Not production throughput / memory numbers |
| Keep Ollama Path A | Real adapter weights on GPU demos | Not multi-tenant LoRA swap |
| Simulator stays pure-Python | Inspectable for CI | No CUDA fidelity |

## Consequences

- DomainForge README: vLLM row → 🟡 Educational Path B
- LinkedIn narrative: train + understand + **wired** educational serve (honest about CUDA gap)
- Follow-up: real vLLM Docker with LoRA modules when GPU budget allows

## Links

- [DomainForge ADR-019](./ADR-019-rag-facts-peft-behavior.md)
- DomainForge `domainforge/serve/vllm.py`, vLLM Lab `/v1/chat/completions`
- [LinkedIn Launch Plan](../docs/LINKEDIN_LAUNCH_PLAN.md)

# ADR-022: DomainForge Adapters on vLLM Multi-LoRA Serving

**Status:** Accepted (educational Path B)  
**Date:** Jul 2026 (updated 2026-07-09)  
**Systems:** DomainForge (`domainforge-rag-peft`), vLLM Architecture Lab (`vllm-architecture-lab`)

## In one breath (panel)

I'd wire DomainForge to an OpenAI-shaped vLLM Lab chat with `adapter_id` for interview proof — and refuse to call that CUDA multi-LoRA economics.

## Context

DomainForge trains and registers QLoRA/DPO adapters (S3/S4) for structured JSON triage. Real vLLM 0.15+ can serve many LoRA adapters on one GPU with per-request swap. The portfolio already had train+eval (DomainForge) and a pure-Python PagedAttention / continuous-batching simulator (vLLM Lab). Missing piece: a thin, honest wire from adapter promote → serve path without inventing throughput SLAs we don't measure.

## Decision

1. **Path A (current GPU demo):** Ollama Modelfile after merge/export — real adapter weights when a GPU host exists
2. **Path B (shipped as educational):** DomainForge `VLLM_BASE_URL` routes PEFT solutions to vLLM Lab `POST /v1/chat/completions` with model/`adapter_id` (`domainforge-triage-v0`). Lab exposes `GET /v1/adapters` mock registry. **Not** CUDA multi-LoRA kernels. **Not** production SLAs
3. Keep real vLLM multi-LoRA on GPU hosts as the eventual economics proof — planned, not claimed

```text
Train (GPU) → merge adapter → export
  → Path A: Ollama Modelfile
  → Path B: vLLM Lab chat + adapter_id (educational; this ADR)
Serve (future): real vLLM LoRA modules on one GPU
```

Refused: LinkedIn copy that implies Path B is multi-tenant LoRA swap at scale.

## Consequences

| Choice | Gain | Trade |
|--------|------|-------|
| Educational Path B now | Runnable DomainForge↔vLLM wire for interviews | No production throughput / memory numbers |
| Keep Ollama Path A | Real adapter weights on GPU demos | Not multi-tenant LoRA swap |
| Simulator stays pure-Python | Inspectable for CI | No CUDA fidelity |

DomainForge README vLLM row stays 🟡 Educational Path B. Follow-up when GPU budget allows: real vLLM Docker with LoRA modules.

## Links

- [DomainForge ADR-019](./ADR-019-rag-facts-peft-behavior.md)
- DomainForge `domainforge/serve/vllm.py`, vLLM Lab `/v1/chat/completions`
- [LinkedIn Launch Plan](../docs/LINKEDIN_LAUNCH_PLAN.md)

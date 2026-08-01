# DomainForge — Enterprise RAG + PEFT Triage Pipeline

**Domain:** Enterprise RAG · Parameter-efficient fine-tuning · Eval harness  
**Live demo:** [domainforge-rag-peft.vercel.app](https://domainforge-rag-peft.vercel.app)  
**API:** [domainforge-api.onrender.com](https://domainforge-api.onrender.com)  
**Bench:** [/bench](https://domainforge-rag-peft.vercel.app/bench)  
**Source:** [domainforge-rag-peft](https://github.com/vpeetla-ai/domainforge-rag-peft)

## Problem

Support automation needs grounded SOP citations *and* reliable JSON for routing. Fine-tune everything and you bake stale facts into weights. RAG-only and the model invents field names and `chunk_id`s. The scar is collapsing two failure modes into one knob.

## What we decided

1. **RAG = facts, PEFT = behavior** — separate eval dimensions and promotion gates ([ADR-019](../adr/ADR-019-rag-facts-peft-behavior.md)).
2. **S0→S4 ladder** — baseline → naive RAG → hybrid → QLoRA → DPO-aligned ([ADR-020](../adr/ADR-020-dpo-after-sft-alignment.md)).
3. **Adapter promotion gated** — API-key; blocked on regression.
4. **Local AI bench** — same triage JSON contract on Ollama ([case study](./domainforge-local-ai-bench.md)).
5. **vLLM multi-LoRA as Path B target** — train/eval today; CUDA LoRA serve not claimed yet ([ADR-022](../adr/ADR-022-domainforge-vllm-multi-lora-serving.md)).

## Architecture

Canonical: [docs/diagrams/canonical-architecture.mmd](https://github.com/vpeetla-ai/domainforge-rag-peft/blob/main/docs/diagrams/canonical-architecture.mmd)

```text
SOP corpus → hybrid RAG (S1/S2)  |  Bitext → QLoRA (S3) → DPO (S4)
Both → FastAPI /v1/query → golden eval S0→S4 → optional Ollama / vLLM serve
```

## Live proof

- UI: [domainforge-rag-peft.vercel.app](https://domainforge-rag-peft.vercel.app)
- API: [domainforge-api.onrender.com](https://domainforge-api.onrender.com)
- Bench: [/bench](https://domainforge-rag-peft.vercel.app/bench)

### Ollama bench (reference targets)

| Model | Metric | Notes |
|-------|--------|-------|
| llama3.2:3b | P50/P95 ms, tokens/s | Run via `/bench` when Ollama local |
| mistral:7b | P50/P95 ms, tokens/s | Same golden triage JSON prompt |
| GPU pipeline | Real S3/S4 adapters | `scripts/gpu_pipeline.sh` on RunPod |

*Populate after GPU run — honest empty until measured.*

## Limitations / what we'd do differently

- ADR-022 Path B is educational / planned — don’t sell OpenAI-compatible adapter chat as CUDA multi-LoRA already shipping.
- GPU pipeline numbers stay blank until measured; inventing tokens/s would break the honesty rule.
- I’d tighten promotion UX so regression blocks are obvious in the UI, not only in API responses.

## Related ADR

[ADR-019](../adr/ADR-019-rag-facts-peft-behavior.md) · [ADR-020](../adr/ADR-020-dpo-after-sft-alignment.md) · [ADR-022](../adr/ADR-022-domainforge-vllm-multi-lora-serving.md) · [Enterprise RAG](./enterprise-rag-platform.md) · [vLLM Lab](./vllm-architecture-lab.md) · [VoiceForge](./voiceforge-assistant.md)

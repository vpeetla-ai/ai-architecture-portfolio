# DomainForge — Enterprise RAG + PEFT Triage Pipeline

**Domain:** Enterprise RAG · Parameter-efficient fine-tuning · Eval harness  
**Live demo:** [domainforge-rag-peft.vercel.app](https://domainforge-rag-peft.vercel.app)  
**API:** [domainforge-api.onrender.com](https://domainforge-api.onrender.com)  
**Bench:** [/bench](https://domainforge-rag-peft.vercel.app/bench)  
**Source:** [domainforge-rag-peft](https://github.com/vpeetla-ai/domainforge-rag-peft)

## Problem

Support automation needs **grounded citations** from SOPs and **reliable JSON** for routing — base models hallucinate field names and invent `chunk_id`s. A single "fine-tune everything" or "RAG only" approach fails one dimension or the other.

## Architecture

Canonical: [docs/diagrams/canonical-architecture.mmd](https://github.com/vpeetla-ai/domainforge-rag-peft/blob/main/docs/diagrams/canonical-architecture.mmd)

```text
SOP corpus → hybrid RAG (S1/S2)  |  Bitext → QLoRA (S3) → DPO (S4)
Both → FastAPI /v1/query → golden eval S0→S4 → optional Ollama / vLLM serve
```

## Key decisions

- **RAG = facts, PEFT = behavior** — [ADR-019](../adr/ADR-019-rag-facts-peft-behavior.md)
- **S0→S4 ladder** — baseline → naive RAG → hybrid → PEFT → **DPO-aligned** ([ADR-020](../adr/ADR-020-dpo-after-sft-alignment.md))
- **Adapter promotion gated** — API-key; blocked on regression
- **Local AI bench** — `POST /v1/bench/ollama` + UI `/bench` ([case study](domainforge-local-ai-bench.md))
- **vLLM multi-LoRA target** — [ADR-022](../adr/ADR-022-domainforge-vllm-multi-lora-serving.md) (planned)

## Ollama bench (reference targets)

| Model | Metric | Notes |
|-------|--------|-------|
| llama3.2:3b | P50/P95 ms, tokens/s | Run via `/bench` when Ollama local |
| mistral:7b | P50/P95 ms, tokens/s | Same golden triage JSON prompt |
| GPU pipeline | Real S3/S4 adapters | `scripts/gpu_pipeline.sh` on RunPod |

*Populate table after GPU run — honest empty until measured.*

## Impact

- Answers **"How do we adapt models to domain format?"**
- Pairs with [Enterprise RAG](enterprise-rag-platform.md), [vLLM Lab](vllm-architecture-lab.md), [VoiceForge](voiceforge-assistant.md)

## Related ADR

[ADR-019](../adr/ADR-019-rag-facts-peft-behavior.md) · [ADR-020](../adr/ADR-020-dpo-after-sft-alignment.md) · [ADR-022](../adr/ADR-022-domainforge-vllm-multi-lora-serving.md)

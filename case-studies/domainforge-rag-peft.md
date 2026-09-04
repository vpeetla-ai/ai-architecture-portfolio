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

### GPU pipeline — real, 2026-09-04

Real S3/S4 adapters, trained on a rented GCP L4 (`scripts/gpu_pipeline.sh`), receipt committed in
[modelforge-llmops](./modelforge-llmops.md) (`docs/receipts/peft_gpu.json`, run
`peft-20260904T055541Z`):

| Stage | Real numbers |
|-------|--------------|
| S3 QLoRA SFT | 378 train examples, 27 val, 200 steps, 829.01s wall, 4-bit QLoRA |
| S4 DPO | 16 preference pairs, 3 val, 100 steps, 1018.11s wall, beta=0.1 |

**What this does not yet claim:** a quality or preference-win-rate score for the trained adapter.
`domainforge/generation/baseline.py`'s `generate_triage_json()` — the function every S0-S4 "solution"
runs through, S3/S4 included — is a template/keyword simulator, not live inference through the trained
adapter (its own docstring says so). Scoring the real adapter's actual generations against the golden
suite is open work, not silently assumed. See [ADR-035](../adr/ADR-035-real-gpu-receipt-methodology.md).

## Limitations / what we'd do differently

- ADR-022 Path B is educational / planned — don’t sell OpenAI-compatible adapter chat as CUDA multi-LoRA already shipping.
- The GPU pipeline numbers above are real training config/timing, not a quality score — don't read "training completed" as "adapter quality verified."
- I’d tighten promotion UX so regression blocks are obvious in the UI, not only in API responses.

## Related ADR

[ADR-019](../adr/ADR-019-rag-facts-peft-behavior.md) · [ADR-020](../adr/ADR-020-dpo-after-sft-alignment.md) · [ADR-022](../adr/ADR-022-domainforge-vllm-multi-lora-serving.md) · [ADR-035](../adr/ADR-035-real-gpu-receipt-methodology.md) · [Enterprise RAG](./enterprise-rag-platform.md) · [vLLM Lab](./vllm-architecture-lab.md) · [VoiceForge](./voiceforge-assistant.md) · [ModelForge](./modelforge-llmops.md)

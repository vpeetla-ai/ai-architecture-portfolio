# DomainForge Local AI Benchmark

**Domain:** Local SLM inference · Structured JSON · Quantization comparison  
**Live bench:** [domainforge-rag-peft.vercel.app/bench](https://domainforge-rag-peft.vercel.app/bench)  
**API:** `POST /v1/bench/ollama`  
**Source:** [domainforge-rag-peft](https://github.com/vpeetla-ai/domainforge-rag-peft)

## Problem

Portfolio Pillar 2 requires honest local-model benchmarking — tokens/sec, P50/P95 latency, and structured JSON quality — not just "Ollama is wired."

## Architecture

```text
Golden triage prompt → Ollama /api/generate → latency + token stats → bench UI table
```

## Key decisions

- **Reuse DomainForge triage JSON prompt** — same schema contract as S0→S4 ladder
- **API-first bench** — `domainforge/bench/ollama.py` + `scripts/ollama_bench.sh` for CI/local
- **UI `/bench` route** — portfolio-visible comparison table (llama3.2:3b vs mistral:7b)
- **GPU path documented** — `docs/GPU_OLLAMA_PIPELINE.md` + `scripts/gpu_pipeline.sh` for Phase C

## Impact

- Closes Portfolio Phase B — local AI benchmark deliverable
- Pairs with [DomainForge](domainforge-rag-peft.md) (fine-tuning) and [vLLM Lab](vllm-architecture-lab.md) (inference education)

## Related

- [ADR-019: RAG facts + PEFT behavior](../adr/ADR-019-rag-facts-peft-behavior.md)
- [GPU Ollama pipeline](https://github.com/vpeetla-ai/domainforge-rag-peft/blob/main/docs/GPU_OLLAMA_PIPELINE.md)

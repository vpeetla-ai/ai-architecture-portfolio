# DomainForge Local AI Benchmark

**Domain:** Local SLM inference · Structured JSON · Quantization comparison  
**Live bench:** [domainforge-rag-peft.vercel.app/bench](https://domainforge-rag-peft.vercel.app/bench)  
**API:** `POST /v1/bench/ollama`  
**Source:** [domainforge-rag-peft](https://github.com/vpeetla-ai/domainforge-rag-peft)

## Problem

“Ollama is wired” isn’t a benchmark. Portfolio Pillar 2 needs tokens/sec, P50/P95, and structured JSON quality on a golden triage prompt — or the local-model claim is brochure copy.

## What we decided

1. **Reuse the DomainForge triage JSON prompt** — same schema contract as the S0→S4 ladder ([ADR-019](../adr/ADR-019-rag-facts-peft-behavior.md)).
2. **API-first bench** — `domainforge/bench/ollama.py` + `scripts/ollama_bench.sh` for CI/local.
3. **UI `/bench` route** — llama3.2:3b vs mistral:7b table a stranger can open.
4. **GPU path documented, not invented** — `docs/GPU_OLLAMA_PIPELINE.md` + `scripts/gpu_pipeline.sh`; numbers stay blank until measured.

## Architecture

```text
Golden triage prompt → Ollama /api/generate → latency + token stats → bench UI table
```

## Live proof

- Bench UI: [domainforge-rag-peft.vercel.app/bench](https://domainforge-rag-peft.vercel.app/bench)
- Parent case study: [DomainForge](./domainforge-rag-peft.md)
- Inference education sibling: [vLLM Lab](./vllm-architecture-lab.md)

## Limitations / what we'd do differently

- Bench requires a reachable Ollama; empty UI without a local/GPU runner is honest, not a failure of the page.
- Don’t paste fake P50s into the DomainForge table — measure or leave blank.
- Next: keep GPU pipeline results versioned next to the prompt hash so regressions are visible.

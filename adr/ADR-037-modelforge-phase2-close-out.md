# ADR-037: ModelForge Phase 2 Close-Out — Real GPU on the Pipeline's Actual Model

**Status:** Accepted
**Date:** 2026-09-03
**Deciders:** Venkata Peetla (Principal AI Architect)
**Repos:** `modelforge-llmops`, `domainforge-rag-peft`, `aegis-llm-gateway`
**Supersedes evidence in:** ADR-034 (methodology unchanged; underlying receipts upgraded)

## In one breath (panel)

ADR-034 closed ModelForge's Definition-of-Done with a real but modest receipt (TinyLlama-1.1B on a T4); this closes the gap between "DoD checkbox ticked" and "the pipeline's actual configured 7B model, measured on the GPU class the README claims."

## Context

ADR-034's DoD closed on 2026-08-24 with real receipts — `peft_gpu.json` and `vllm_cuda.json`, both TinyLlama-1.1B on a Tesla T4. Genuinely real, not fabricated. But a stand-in model, not `docker-compose.vllm.yml`'s actual `mistralai/Mistral-7B-Instruct-v0.3`, and not DomainForge's real triage data.

A second real GPU session, rented L4 this time, ran the pipeline's actual model end to end: real QLoRA SFT (378 examples) → DPO (16 pairs) on Mistral-7B, and upstream vLLM serving that same checkpoint. Methodology in ADR-035 — manifest-sourced numbers, `known_gaps` stated plainly.

Two more things closed in the same window:

- **`aegis-llm-gateway` load test** — real Locust run, 30 concurrent users, 60s: 61,168 requests, 0 failures, 1022.75 req/s, p50 2ms/p95 6ms/p99 35ms. Run locally against stub mode, not the shared Render deploy — no reason to degrade it for real visitors.
- **SLM bake-off** — local-Ollama half was already real. The cloud half (Groq `openai/gpt-oss-20b`, 3/3 schema-pass, 0.386s mean vs local's 3.415s) closed once `GROQ_API_KEY` existed as a repo secret, via a new `workflow_dispatch`-only `slm-bakeoff-cloud.yml`.

Landing the real `peft_gpu.json` took three attempts, not one, and that's worth saying plainly. The first two real training runs — each a genuine ~30-minute SFT+DPO pass — got destroyed before their receipts could be committed:

1. The workflow's top-level checkout defaulted to `clean: true`, which wiped the DomainForge sibling checkout — adapters, manifests, all of it — even on a `mode=vllm-only` run that explicitly skips the step checking that sibling out.
2. A `docker compose up -d` vLLM container from an earlier run never got torn down. It sat on ~20GB of the L4's 23GB VRAM and starved the next PEFT run's model load.

Both fixed now. Third attempt landed clean.

## Decision

Update `modelforge-llmops`'s receipts and status claims to the stronger evidence without re-litigating ADR-034's methodology:

- `vllm_cuda.json` replaced in full: run `vllm-20260903T225117Z`, 1x NVIDIA L4, `mistralai/Mistral-7B-Instruct-v0.3` via upstream `vllm/vllm-openai:v0.8.5`, 13.74 tok/s, TTFT p50 371.67ms/p95 372.75ms — the pipeline's real configured model, not a stand-in.
- `peft_gpu.json` replaced in full: run `peft-20260904T055541Z`, real QLoRA SFT (378 examples, 200 steps, 829.01s) + DPO (16 preference pairs, 100 steps, 1018.11s, beta=0.1) on `mistralai/Mistral-7B-Instruct-v0.3` on the same L4 — the TinyLlama/T4 receipt is fully superseded, not just supplemented.
- `QUANT_SERVE_TRADEOFFS.md`'s FP16/unquantized row backed by the real vLLM number instead of staying purely narrative.
- README status table and `MODEL_PLANE_100_TRACKER.md` change log updated to point at the new run IDs, keeping ADR-034's "DoD closed" framing intact — this is a strength upgrade, not a reopening.

## Consequences

### Positive

- The headline receipt a reviewer clicks now matches the model the architecture docs actually describe (Mistral-7B), removing the "well, it was a toy model" objection.
- `aegis-llm-gateway`'s load-test receipt gives the gateway plane a real systems-engineering data point it previously lacked entirely.

### Trade-offs

- The TinyLlama receipt at least attempted a `delta_schema_pass` metric, small and low-signal as it was. The Mistral-7B receipt reports none, per ADR-035 — no fabricated number beats a low-signal real one. Higher honesty, fewer numbers on the page, until the eval-harness gap closes.
- Three GPU-billed attempts to land one receipt. Real cost, real infrastructure, not a paper pipeline.

### Refused

- Silently replacing the T4/TinyLlama receipt in the case-study narrative without noting the model/GPU class changed — the upgrade is stated explicitly here and in the tracker change log.

## Links

- `modelforge-llmops` commits: `2f227da`, `db4efc9`, `73fb3f6`, `ebf6bb2` (checkout-clean fix), `2e509cf` (vLLM-teardown fix), `053dae7` (real PEFT receipt), `9074caa` (SLM bake-off cloud comparator)
- `aegis-llm-gateway` commit: `25913cb`
- ADR-034 · ADR-035

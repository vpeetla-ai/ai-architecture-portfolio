# ADR-037: ModelForge Phase 2 Close-Out — Real GPU on the Pipeline's Actual Model

**Status:** Accepted
**Date:** 2026-09-03
**Deciders:** Venkata Peetla (Principal AI Architect)
**Repos:** `modelforge-llmops`, `domainforge-rag-peft`, `aegis-llm-gateway`
**Supersedes evidence in:** ADR-034 (methodology unchanged; underlying receipts upgraded)

## In one breath (panel)

ADR-034 closed ModelForge's Definition-of-Done with a real but modest receipt (TinyLlama-1.1B on a T4); this closes the gap between "DoD checkbox ticked" and "the pipeline's actual configured 7B model, measured on the GPU class the README claims."

## Context

ADR-034's Definition of Done was satisfied on 2026-08-24 with real GPU receipts — `peft_gpu.json` (TinyLlama-1.1B, LoRA-fp16, Tesla T4) and `vllm_cuda.json` (TinyLlama-1.1B, Tesla T4, 53.66 tok/s). Both were genuinely real, not fabricated, but both used a small stand-in model rather than `docker-compose.vllm.yml`'s actually-configured `mistralai/Mistral-7B-Instruct-v0.3`, and rather than DomainForge's real triage training data.

As part of closing Critical Gap #1 org-wide, a second real GPU session (this time on a rented GCP L4, 2026-09-03) ran the pipeline's actual configured model end to end: DomainForge's real QLoRA SFT (378 examples) → DPO (16 preference pairs) on Mistral-7B, and upstream vLLM serving that same Mistral-7B checkpoint. See ADR-035 for the methodology this receipt pair follows (manifest-sourced real numbers, explicit `known_gaps` where the eval harness can't yet score adapter quality).

Two adjacent Phase 2/4 items were also closed in the same window:

- **`aegis-llm-gateway` load-test evidence** — real Locust run (30 concurrent users, 60s, 61,168 requests, 0 failures, 1022.75 req/s, p50 2ms/p95 6ms/p99 35ms) against a locally-run stub-mode instance, converting "policy engineering" framing into a measured systems-engineering claim. Deliberately run locally, not against the shared live Render free-tier deployment, to avoid degrading it for real visitors.
- **SLM bake-off** — the local-Ollama half (`llama3.2:1b` CPU, 3/3 schema-pass) was already real from ADR-034's window; the cloud-API comparator (Groq `openai/gpt-oss-20b`, 3/3 schema-pass, 0.386s mean vs the local 3.415s mean) was closed in the same window via a new `workflow_dispatch`-only `slm-bakeoff-cloud.yml`, once `GROQ_API_KEY` was available as a repo secret.

Getting the real `peft_gpu.json` committed took three attempts, not one — worth recording plainly rather than smoothing over. The first two real training runs (each a genuine ~30-minute SFT+DPO pass on the L4) were destroyed before their receipts could be committed, by two separate, now-fixed infrastructure bugs: (1) the workflow's top-level `actions/checkout@v4` step defaulted to `clean: true`, which silently deleted the DomainForge sibling checkout — and its adapters and manifests — via `git clean -ffdx`, even on a `mode=vllm-only` run that explicitly skips the step that checks that sibling out; (2) a `docker compose up -d` vLLM container from an earlier run was never torn down, so it sat holding ~20GB of the L4's 23GB VRAM and starved the next PEFT run's model load. Both are fixed (`clean: false` on the top-level checkout; an `if: always()` `docker compose down` step) and the third attempt succeeded cleanly.

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

- `peft_gpu.json`'s quality signal is narrower than before in one sense: the TinyLlama receipt (ADR-034 era) at least attempted a `delta_schema_pass` metric (even if a small, low-signal one on a 1.1B model); the new Mistral-7B receipt reports none at all, per ADR-035's decision to not fabricate one. Net honesty is higher; net "numbers on the page" is lower until the eval-harness gap is closed.
- Three GPU-billed training attempts were needed to land one committed receipt, due to the two infra bugs above — a real cost (time and modest spend) of running real infrastructure rather than a paper pipeline.

### Refused

- Silently replacing the T4/TinyLlama receipt in the case-study narrative without noting the model/GPU class changed — the upgrade is stated explicitly here and in the tracker change log.

## Links

- `modelforge-llmops` commits: `2f227da`, `db4efc9`, `73fb3f6`, `ebf6bb2` (checkout-clean fix), `2e509cf` (vLLM-teardown fix), `053dae7` (real PEFT receipt), `9074caa` (SLM bake-off cloud comparator)
- `aegis-llm-gateway` commit: `25913cb`
- ADR-034 · ADR-035

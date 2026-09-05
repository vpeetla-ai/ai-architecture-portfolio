# ADR-035: Real-GPU Receipt Methodology — and What "Known Gaps" Means

**Status:** Accepted
**Date:** 2026-09-03
**Deciders:** Venkata Peetla (Principal AI Architect)
**Repos:** `domainforge-rag-peft`, `modelforge-llmops`

## In one breath (panel)

A receipt that reports a number the pipeline didn't actually measure is worse than reporting no number at all — I'd rather ship a GPU receipt that says "here's what we proved, here's what we didn't" than one that looks complete and isn't.

## Context

Critical Gap #1 was LLM engineering depth. Closing it meant one thing: a real GPU training run for DomainForge's QLoRA+DPO pipeline and real upstream vLLM serving — not another simulator. Rented a GCP L4 spot instance, registered it as a GitHub Actions self-hosted runner (`llm-l4-spot`) for `modelforge-llmops`'s `gpu-receipts.yml`.

Getting a run to complete meant working through a real infra gauntlet, one bug at a time:

- NVIDIA driver too old for the kernel (`follow_pfn` was removed; needed ≥580.x, had 550.54.15)
- Docker + NVIDIA Container Toolkit missing
- PEP 668 blocking pip installs
- 10GB disk, needed 200GB
- Python 3.13 vs. the training stack's `torch<2.5.0` pin — fixed with a `uv`-managed 3.11 venv
- missing transitive deps (`rich`, `sentencepiece`, `protobuf`)
- 16GB RAM not enough for SFT+DPO in one process — upgraded to 32GB
- and the actual root cause of the DPO OOM: `dpo.py` loaded the full 7B model in fp32 with no quantization, unlike the working QLoRA path in `qlora.py`. Two other fixes (`gc.collect()`/`empty_cache()`, splitting SFT/DPO into separate processes) didn't touch it — only reading the two files side by side did.

Training then completed for real — SFT: 378 examples, 200 steps, ~14min; DPO: 16 pairs, 100 steps, ~17min, repeatably. Then a worse problem showed up in the receipt itself. `export_modelforge_receipt.py` read `s3_peft_hybrid.json`/`s4_dpo_peft.json` to report the adapter's "quality" — except those were fixtures committed 2026-07-06, copy-pasted from `s0_baseline.json` and never regenerated, because `domainforge-eval compare` only ever scores S0/S1/S2 by default. Worse than that: `generate_triage_json()`, the function every S0-S4 "solution" runs through including S3/S4, is a template/keyword simulator, not real inference — its own docstring says so. Wired as-is, the receipt would have presented four-month-old placeholder numbers as this run's DPO-adapter quality score.

Options considered:

1. **Wire real adapter inference into the eval harness now** — score S3/S4 for real, so the receipt can carry a genuine quality/win-rate number. Real engineering lift (loading LoRA weights, running generation, scoring against a rubric); more GPU billing time on an already-long session.
2. **Publish the receipt with the stale numbers anyway** — fast, but knowingly ships a number that misrepresents what was measured. Refused outright — this is exactly the failure mode the remediation plan committed not to produce.
3. **Report only what was genuinely measured, and say plainly what wasn't** — rewrite the exporter to source real numbers from each training stage's own `training_manifest.json` (example/pair counts, step counts, real wall-clock seconds — all real, all traceable to an actual run), drop the fabricated-looking quality claim entirely, and add an explicit `known_gaps` field naming the eval-harness limitation by file and reason.

## Decision

**Option 3.** Real inference wiring (option 1) stays on the list — a named follow-up, not something quietly dropped.

`export_modelforge_receipt.py` now takes `--sft-manifest`/`--dpo-manifest` instead of `--s0`/`--s3`/`--s4`. `peft_gpu.json` reports `sft.{train_examples,val_examples,max_steps,wall_seconds}` and `dpo.{train_pairs,val_pairs,max_steps,wall_seconds,beta}` — every field traces to an actual run — plus a `known_gaps` array that just says it: DomainForge's eval harness isn't wired to real adapter inference, so no quality or win-rate number is claimed.

The vLLM half was a smaller bug: `capture_vllm_metrics.py` needs `httpx`, the workflow never installed it. One line. That receipt (`vllm_cuda.json`, run `vllm-20260903T225117Z`) is fully real — upstream `vllm/vllm-openai:v0.8.5` serving the pipeline's actual model (`mistralai/Mistral-7B-Instruct-v0.3`, no smaller stand-in) on the rented L4: 13.74 tok/s, TTFT p50 371.67ms/p95 372.75ms, 5 real round-trips, `nvidia-smi` proof of ~20.4GB held by a live server.

## Consequences

### Positive

- Every field in both receipts traces to a command run on real hardware. No hand-typed numbers.
- `known_gaps` names the eval-harness limitation instead of leaving it for a careful reader to find.
- Manifest-sourced numbers + a known-gaps field is now the pattern for every GPU receipt in this org, not a one-off.

### Trade-offs

- `peft_gpu.json` carries no quality/win-rate signal at all right now. Real gap, disclosed, not papered over.
- Real S3/S4 inference — load the LoRA weights, generate, score against a rubric — is still open work, and it costs more GPU time.

### Refused

- Publishing a receipt built from a file the pipeline being measured never touched.
- Widening the script quietly to fake a win-rate so an incomplete measurement looks finished.

## Links

- `domainforge-rag-peft` commits: `967ee36` (DPO quantization fix), `88ece03` (exporter rewrite)
- `modelforge-llmops` commits: `2f227da` (workflow wiring + httpx fix), `db4efc9` (real vLLM receipt), `73fb3f6` (docs backfill)
- ADR-019 · ADR-020 · ADR-034

# ADR-035: Real-GPU Receipt Methodology — and What "Known Gaps" Means

**Status:** Accepted
**Date:** 2026-09-03
**Deciders:** Venkata Peetla (Principal AI Architect)
**Repos:** `domainforge-rag-peft`, `modelforge-llmops`

## In one breath (panel)

A receipt that reports a number the pipeline didn't actually measure is worse than reporting no number at all — I'd rather ship a GPU receipt that says "here's what we proved, here's what we didn't" than one that looks complete and isn't.

## Context

Closing Critical Gap #1 (LLM engineering depth) meant producing a real, evidenced GPU training run — not a simulated one — for DomainForge's QLoRA+DPO pipeline and for upstream vLLM serving. A GCP `g2-standard-4`/`g2-standard-8` spot L4 instance was rented and registered as a GitHub Actions self-hosted runner (`llm-l4-spot`) for `modelforge-llmops`'s `gpu-receipts.yml`.

Getting a real training run to complete at all required fixing a real chain of infrastructure bugs in sequence: missing NVIDIA driver (kernel/driver API mismatch — `follow_pfn` removed from newer kernels, needed driver ≥580.x not the pinned 550.54.15), Docker + NVIDIA Container Toolkit, PEP 668 externally-managed-environment blocking pip installs, disk space (10GB → 200GB), a Python 3.13/3.11 mismatch (DomainForge's training stack pins `torch<2.5.0`, unavailable for 3.13 — fixed with a `uv`-managed 3.11 venv), missing transitive dependencies (`rich`, `sentencepiece`, `protobuf`), host RAM exhaustion under SFT+DPO in one process (16GB → 32GB machine-type upgrade), and finally a real code bug: `domainforge/train/dpo.py`'s `train_dpo()` loaded the full 7B model in unquantized `torch.float32` (~28GB) with no `BitsAndBytesConfig`, unlike the working QLoRA path in `qlora.py` — the actual root cause of every DPO-stage CUDA OOM, found only by reading the two files side by side after two other fix attempts (in-process `gc.collect()`/`empty_cache()`, then decomposing the pipeline into separate SFT/DPO OS processes) failed to resolve it.

Once training finally succeeded for real (SFT: 378 examples, 200 steps, ~14min wall; DPO: 16 pairs, 100 steps, ~17min wall, both real and repeatable), a second, more serious problem surfaced in the receipt-export step itself: `export_modelforge_receipt.py` read `data/eval/results/s3_peft_hybrid.json` and `s4_dpo_peft.json` to report the trained adapter's "quality" — but those files were **stale fixtures committed on 2026-07-06**, copy-pasted from `s0_baseline.json` and never regenerated, because `domainforge-eval compare` only ever scores S0/S1/S2 by default. Worse: `domainforge/generation/baseline.py`'s `generate_triage_json()` — the function every S0-S4 "solution" runs through, including S3/S4 — is a template/keyword simulator, not real inference through a trained adapter (its own docstring says so). The receipt, as originally wired, would have presented four-month-old, unrelated placeholder numbers as if they were this run's DPO-adapter quality score.

Options considered:

1. **Wire real adapter inference into the eval harness now** — score S3/S4 for real, so the receipt can carry a genuine quality/win-rate number. Real engineering lift (loading LoRA weights, running generation, scoring against a rubric); more GPU billing time on an already-long session.
2. **Publish the receipt with the stale numbers anyway** — fast, but knowingly ships a number that misrepresents what was measured. Refused outright — this is exactly the failure mode the remediation plan committed not to produce.
3. **Report only what was genuinely measured, and say plainly what wasn't** — rewrite the exporter to source real numbers from each training stage's own `training_manifest.json` (example/pair counts, step counts, real wall-clock seconds — all real, all traceable to an actual run), drop the fabricated-looking quality claim entirely, and add an explicit `known_gaps` field naming the eval-harness limitation by file and reason.

## Decision

**Accept option 3**, with the real-inference wiring (option 1) tracked as a named follow-up, not silently deferred.

`scripts/export_modelforge_receipt.py` now takes `--sft-manifest`/`--dpo-manifest` (each stage's real `training_manifest.json`) instead of `--s0`/`--s3`/`--s4`. The resulting `peft_gpu.json` reports `sft.{train_examples,val_examples,max_steps,wall_seconds}` and `dpo.{train_pairs,val_pairs,max_steps,wall_seconds,beta}` — every field traceable to an actual training run — plus a `known_gaps` array stating in plain language that DomainForge's S0-S4 eval harness isn't wired to real adapter inference, so no quality or preference-win-rate score is claimed.

The vLLM half of this receipt pair had a smaller, more ordinary bug: `capture_vllm_metrics.py` needs `httpx`, and the workflow's vLLM step never installed anything (unlike the PEFT step's dedicated venv) — a one-line fix. That receipt (`vllm_cuda.json`, run `vllm-20260903T225117Z`) is fully real: upstream `vllm/vllm-openai:v0.8.5` serving the pipeline's actual configured model (`mistralai/Mistral-7B-Instruct-v0.3`, not a smaller stand-in) on the real rented L4, 13.74 tok/s, TTFT p50 371.67ms/p95 372.75ms, captured over 5 real HTTP round-trips with `nvidia-smi` proof of ~20.4GB VRAM held by a live server process.

## Consequences

### Positive

- Every field in both receipts now traces to an actual command run on real hardware — no hand-typed numbers anywhere.
- `known_gaps` makes the eval-harness limitation a first-class, named fact instead of an implicit blind spot a careful reader would have to discover themselves.
- The methodology (manifest-sourced numbers + explicit known-gaps field) is now the pattern for any future GPU receipt in this org, not a one-off patch.

### Trade-offs

- `peft_gpu.json` currently carries no quality/win-rate signal at all — a real gap in what the receipt proves, honestly disclosed rather than papered over.
- Wiring real S3/S4 adapter inference (loading the trained LoRA weights and generating real completions, scored against a rubric) remains open work, costed at further GPU-rental time.

### Refused

- Publishing a receipt with numbers pulled from a file the pipeline being measured never touched.
- Silently widening a script's scope (adding a fake win-rate) to make an incomplete measurement look complete.

## Links

- `domainforge-rag-peft` commits: `967ee36` (DPO quantization fix), `88ece03` (exporter rewrite)
- `modelforge-llmops` commits: `2f227da` (workflow wiring + httpx fix), `db4efc9` (real vLLM receipt), `73fb3f6` (docs backfill)
- ADR-019 · ADR-020 · ADR-034

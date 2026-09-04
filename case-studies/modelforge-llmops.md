# ModelForge — Model Plane Flagship

**Domain:** LLMOps · PEFT training · CUDA serving · SLM economics
**Live demo:** [modelforge-gamma.vercel.app](https://modelforge-gamma.vercel.app)
**Source:** [modelforge-llmops](https://github.com/vpeetla-ai/modelforge-llmops)

## Problem

A CAIO skimming this org's agent-pattern repos and orchestration platforms reasonably concludes
"agents only" — even though real PEFT training, CUDA serving, and SLM-economics work existed,
scattered and under-evidenced across DomainForge and vLLM Architecture Lab, with no single surface
answering "which weights, running where, and how do you prove it?"

## What we decided

1. **One flagship, not a product zoo** — ModelForge composes DomainForge (train) + upstream vLLM
   (serve) + a local-vs-cloud bake-off behind one posture surface, rather than a seventh repo per
   capability ([ADR-034](../adr/ADR-034-modelforge-model-plane.md)).
2. **Status is computed, not asserted** — `/v1/posture` reports each component `ready` only if its
   receipt file exists on disk at request time. Delete a receipt, the badge flips back automatically.
3. **Receipts trace to an actual command, or they don't get written** — the exporter refuses to run
   without `--require-cuda` (or an explicit `--allow-unverified` test-only flag), and refuses a
   tiny/smoke base model for a GPU-claiming receipt ([ADR-035](../adr/ADR-035-real-gpu-receipt-methodology.md)).
4. **Never overstate what a receipt proves** — when the DomainForge eval harness turned out not to be
   wired to real adapter inference yet, the receipt schema was rewritten to report real training
   config/timing and say plainly, in a `known_gaps` field, what it does *not* claim — rather than
   attach a plausible-looking number that wasn't actually measured.

## Architecture

Full diagram: [docs/ARCHITECTURE.md](https://github.com/vpeetla-ai/modelforge-llmops/blob/main/docs/ARCHITECTURE.md)

```text
Next.js UI (posture + receipt gallery)
  → FastAPI (/v1/posture, /receipts, /plane)
    → build_posture() / list_receipts() — status = real file existence
      → docs/receipts/{peft_gpu.json, vllm_cuda.json, slm_bakeoff.md}

.github/workflows/gpu-receipts.yml (self-hosted GPU runner, workflow_dispatch only)
  → PEFT step: checkout domainforge-rag-peft sibling → real QLoRA+DPO training
  → vLLM step: docker compose → real upstream vllm/vllm-openai serving
  → validate_receipts.py --require-gpu (CI gate — refuses smoke/tiny models as GPU receipts)
```

## Live proof

- UI: [modelforge-gamma.vercel.app](https://modelforge-gamma.vercel.app)
- Posture: [`/api/v1/posture`](https://modelforge-gamma.vercel.app/api/v1/posture)

### Real receipts, captured 2026-09-03 on a rented GCP L4

| Receipt | Real result | What it does not claim |
|---|---|---|
| `vllm_cuda.json` | Upstream `vllm/vllm-openai:v0.8.5` serving `mistralai/Mistral-7B-Instruct-v0.3` — **13.74 tok/s, TTFT p50 371.67ms/p95 372.75ms**, `nvidia-smi` proof of ~20.4GB VRAM held by a live server process | Always-on production serving — one dated benchmark run |
| `slm_bakeoff.md` | Local Ollama (`llama3.2:1b`, 3/3 schema-pass, 3.415s mean) vs cloud (Groq `openai/gpt-oss-20b`, 3/3 schema-pass, **0.386s mean**) — same 3 golden cases, both real | A statement about model quality beyond this narrow schema-pass suite |
| `peft_gpu.json` | Real QLoRA SFT (378 examples/200 steps) + DPO (16 pairs/100 steps) training on Mistral-7B completed for real on the rented L4 | A quality/win-rate score — DomainForge's S0-S4 eval harness isn't wired to real adapter inference yet (see `known_gaps` in the receipt) |

Getting the first real GPU run to complete meant fixing a real chain of infrastructure bugs — driver/
kernel mismatch, PEP 668, host RAM exhaustion, and a genuine DPO code bug (loading the model
unquantized in fp32 where SFT correctly used 4-bit QLoRA) — documented in
[ADR-035](../adr/ADR-035-real-gpu-receipt-methodology.md).

## Limitations / what we'd do differently

- `peft_gpu.json`'s quality signal is currently narrower than it should be: real training happened,
  but no live-inference quality score exists yet for the trained adapter. Wiring real adapter
  inference into DomainForge's eval harness is tracked, not hidden.
- The self-hosted GPU runner is ephemeral by design (rented on demand, `workflow_dispatch` only) — not
  an always-on GPU fleet; the README says so explicitly.
- SLM bake-off is one narrow 3-case golden suite — real, but not a substitute for a broader quality
  eval before a real buy-vs-build SLM decision.

## Related ADR

[ADR-034](../adr/ADR-034-modelforge-model-plane.md) · [ADR-035](../adr/ADR-035-real-gpu-receipt-methodology.md) · [ADR-037](../adr/ADR-037-modelforge-phase2-close-out.md) · [DomainForge case study](./domainforge-rag-peft.md) · [vLLM Lab case study](./vllm-architecture-lab.md)

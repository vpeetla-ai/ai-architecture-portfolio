# Panel scripts — Model Plane (ModelForge)

**Use with:** https://modelforge-gamma.vercel.app · [ADR-034](../adr/ADR-034-modelforge-model-plane.md) · [tracker](./MODEL_PLANE_100_TRACKER.md)

## 30s — “agents only” rebuttal

> I’m not an agents-only architect. Agents are how work gets done; the **model plane** is how I decide buy vs RAG vs PEFT vs self-host. ModelForge is the control UI — DomainForge trains adapters, CUDA vLLM serves them, SLM bake-off proves when small models win, and the LLM gateway enforces + records.

**Three links (&lt;30s):** ModelForge live · DomainForge · ADR-034

## 60s — depth

> Facts stay in RAG (ADR-019). Behavior and schema go in PEFT — QLoRA then DPO (ADR-020). Serving math I teach in the vLLM lab; production numbers come from real CUDA vLLM with LoRA modules (ADR-022 Path A). Gateway apps select; the plane enforces and records (ADR-028/029). I don’t pretrain foundations — wrong economics for enterprise triage. I own the adaptation and serving loop end-to-end.

## Trap answers

| Trap | Answer |
|------|--------|
| “Have you trained your own LLM?” | “I adapt open bases with PEFT; I don’t pretend to pretrain 7B+ from scratch. Here’s the adapter receipt and eval delta.” |
| “Show me vLLM experience” | “Educational lab for internals; ModelForge Serve receipt for CUDA metrics from upstream vLLM.” |
| “Why not always GPT-4?” | “SLM bake-off: schema tasks often win on small local models for cost/latency/privacy — table is public.” |
| “Isn’t this just agents?” | “Agents call tools; ModelForge is weights, serve, and route — different plane, same org.” |

## Rehearsal checklist

- [ ] Open posture API — say smoke vs ready aloud
- [ ] Click PEFT + vLLM CUDA receipts (T4 micro honesty)
- [ ] Click SLM + gateway receipts
- [ ] Close with buy/RAG/PEFT/self-host tree

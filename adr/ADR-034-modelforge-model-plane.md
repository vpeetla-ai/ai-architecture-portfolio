# ADR-034: ModelForge as the Model Plane Flagship

**Status:** Accepted  
**Date:** 2026-08-23  
**Deciders:** Venkata Peetla (Principal AI Architect)  
**Plan:** [MODEL_PLANE_100_PLAN.md](../docs/MODEL_PLANE_100_PLAN.md)

## In one breath (panel)

I’d rather add one Model Plane product a CAIO can open than keep PEFT and vLLM buried in a teaching drawer while they conclude I only know agents.

## Context

The public D1 spine (govern · orchestrate · RAG · publish · ADRs) is strong on **agentic GenAI**. Model-side work already exists:

- DomainForge — RAG facts vs PEFT behavior (ADR-019/020)
- vLLM Architecture Lab — educational paging/batching (ADR-022 Path B)
- aegis-llm-gateway — apps select; plane enforces+records (ADR-028/029)

But hire narrative explicitly demotes DomainForge / vLLM Lab to “Teaching drawer / not hire hero.” A CAIO skim therefore collapses the portfolio to “agents only,” even though PEFT/LLMOps code exists.

Options considered:

1. **Narrative-only fix** — promote DomainForge on the profile without a new repo  
2. **Convert vLLM Lab to production CUDA** — breaks the lab’s educational honesty contract  
3. **New ModelForge flagship** — compose train · serve · bench · route behind one hire-facing UI  

## Decision

**Accept option 3.** Create **`modelforge-llmops` (ModelForge)** as the sixth spine layer — **Models** — peer to governance/orchestration/knowledge/application.

ModelForge owns:

- Hire-facing Model Plane UI and receipt gallery
- Orchestration of DomainForge training exports
- Upstream CUDA vLLM serve path (Path A) with published metrics
- SLM vs API bake-off presentation
- Bridge to aegis-llm-gateway for enforce+record

DomainForge remains the PEFT/RAG training system.  
vLLM Architecture Lab remains educational (Path B).  
No additional model-zoo repos after ModelForge (freeze exception is this single flagship).

## Consequences

### Positive

- One clickable answer to “show me models, not just agents”
- Clear separation: concepts lab ≠ production serve ≠ PEFT training
- Aligns panel story with CAIO expectations (SLM, PEFT, CUDA, LLMOps)

### Trade-offs

- One more deployable (Vercel + API host); cold-start honesty required
- Temporary freeze exception — must not reopen the product zoo
- GPU receipts need ephemeral cloud GPU spend (RunPod etc.)

### Refused

- Claiming Path B educational multi-LoRA as CUDA production
- Pretending foundation-model pretraining is in scope
- Renaming DomainForge alone without a Model Plane product surface

## Links

- Plan: [MODEL_PLANE_100_PLAN.md](../docs/MODEL_PLANE_100_PLAN.md)
- Tracker: [MODEL_PLANE_100_TRACKER.md](../docs/MODEL_PLANE_100_TRACKER.md)
- ADR-019 · ADR-020 · ADR-022 · ADR-028 · ADR-029

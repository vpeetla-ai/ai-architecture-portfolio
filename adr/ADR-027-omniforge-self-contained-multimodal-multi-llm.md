# ADR-027: OmniForge — self-contained multimodal multi-LLM platform

**Status:** Accepted  
**Date:** 2026-07-10  
**Systems:** omniforge

## In one breath (panel)

I'd ship one self-contained multimodal demo with task-class multi-LLM routing and in-repo FinOps/export gates — without requiring half the sibling stack to be wired first.

## Context

The org already ships orchestration (VAP), governance (AegisAI), voice (VoiceForge), and FinOps as separate layers. Leaders still need **one inspectable product** that answers multimodal asks (text, image, voice) with multi-agent fan-out and task-class multi-LLM routing. Forcing a reviewer to stand up half the stack for a demo is how portfolio narratives die in cold starts.

## Decision

Ship **OmniForge** as a **self-contained monorepo**:

1. Multimodal ingest → planner → parallel agents + in-process MCP tools → synthesizer
2. Multi-LLM Brain with buckets (`fast` / `structured` / `reasoning` / `vision`) and provider cascades (Groq / OpenAI / Anthropic → mock)
3. Every LLM call emits a `RoutingDecision` (waterfall proof); A/B single vs routed is first-class
4. In-repo FinOps budget halt and export policy gate (`PRODUCTION_STRICT`) — **no runtime dependency** on sibling vpeetla-ai services

Duplicating patterns from sibling repos is intentional. Refused: making OmniForge a thin UI over "start all five platforms first."

## Consequences

**Positive**

- Flagship demo works on mock with zero paid keys; live mode unlocks when keys exist
- Owns the "answer anything with the right models" question without replacing VAP / AegisAI / VoiceForge
- Portfolio stack map gains a clear multimodal + routing spine

**Negative**

- Pattern duplication means drift risk vs sibling repos — acceptable for a self-contained demo; not a claim that OmniForge supersedes the federated planes ([ADR-028](./ADR-028-federated-ai-control-plane-k8s-analogy.md))

## Links

- Repo: https://github.com/vpeetla-ai/omniforge
- Repo ADR: https://github.com/vpeetla-ai/omniforge/blob/main/docs/adr/ADR-001-omniforge-self-contained-multimodal-multi-llm.md

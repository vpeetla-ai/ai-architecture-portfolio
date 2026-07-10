# ADR-027: OmniForge — self-contained multimodal multi-LLM platform

**Status:** Accepted  
**Date:** 2026-07-10  
**Systems:** omniforge

## Context

The org already ships orchestration (VAP), governance (AegisAI), voice (VoiceForge), and FinOps as separate layers. Leaders still need **one inspectable product** that answers multimodal asks (text, image, voice) with multi-agent fan-out and **task-class multi-LLM routing** — without requiring half the stack to be wired for a demo.

## Decision

Ship **OmniForge** as a **self-contained monorepo**:

1. Multimodal ingest → planner → parallel agents + in-process MCP tools → synthesizer
2. Multi-LLM Brain with buckets (`fast` / `structured` / `reasoning` / `vision`) and provider cascades (Groq / OpenAI / Anthropic → mock)
3. Every LLM call emits a `RoutingDecision` (waterfall proof); A/B single vs routed is first-class
4. In-repo FinOps budget halt and export policy gate (`PRODUCTION_STRICT`) — **no runtime dependency** on sibling vpeetla-ai services

Duplicating patterns from sibling repos is intentional.

## Consequences

- Flagship demo works on mock with zero paid keys; live mode unlocks when keys exist
- Does not replace VAP/AegisAI/VoiceForge — owns the “answer anything with the right models” question
- Portfolio stack map gains: *How do we answer multimodal questions with the right agents, tools, and models?*

## Links

- Repo: https://github.com/vpeetla-ai/omniforge
- Repo ADR: https://github.com/vpeetla-ai/omniforge/blob/main/docs/adr/ADR-001-omniforge-self-contained-multimodal-multi-llm.md

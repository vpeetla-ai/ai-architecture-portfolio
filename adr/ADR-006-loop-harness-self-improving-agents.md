# ADR-006: Loop Harness for Self-Improving Agents

**Status:** Accepted  
**Date:** 2026  
**System:** LoopForge (`loop-engine-agent-platform`)  
**Portfolio:** [venkat-ai.com/work](https://venkat-ai.com/work)

## In one breath (panel)

I'd put self-improvement in its own harness — evaluate, mutate RAG config, write memory — not as prompt "reflection" stuffed into the orchestrator or the gateway.

## Context

You can ship orchestration (VAP), governance (AegisAI), and RAG (Enterprise RAG) and still watch agents fail the same edge queries with no versioned way to improve retrieval or keep lessons. Prompt-only reflection doesn't version RAG configs and doesn't leave an auditable trail a reviewer can trust.

2025–2026 work (MemPro, MUSE, Loop Engineering) treats **system-level evolution** as the product: evaluators + memory + tunable pipelines. I refused merging that loop into VAP or AegisAI — different job, different failure modes.

## Decision

Add a sixth reference layer: **LoopForge** — Agent → Harness → Loops → Memory.

1. **Harness** owns ODAEU scheduling and trace export
2. **Inner ReAct** uses MCP tools on a real corpus
3. **Outer Evolve** mutates RAG config on eval failure and writes procedural memory
4. Do **not** merge self-improvement into orchestration or governance repos

Governance can wrap MCP side effects later; the loop still doesn't own policy.

## Consequences

**Positive**

- Inspectable RAG version tree for technical review panels
- Clear portfolio story for applied AI / loop engineering roles
- Composable with the existing stack — gateway can wrap MCP side effects in a later pass

**Negative**

- Another repo to maintain
- v1 uses simplified hybrid retrieval — pair with Enterprise RAG for production embeddings; don't claim they're the same layer

## Proof

[demo-omega-taupe.vercel.app](https://demo-omega-taupe.vercel.app) · [loopforge-api.onrender.com](https://loopforge-api.onrender.com)

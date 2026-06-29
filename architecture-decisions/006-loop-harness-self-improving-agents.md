# ADR-006: Loop Harness for Self-Improving Agents

**Status:** Accepted  
**Date:** 2026  
**System:** LoopForge (`loop-engine-agent-platform`)  
**Portfolio:** [venkat-ai.com/work](https://venkat-ai.com/work)

## Context

Enterprise agent programs deploy orchestration (VAP), governance (AegisAI), and RAG (Enterprise RAG) — but agents still fail on edge queries with no mechanism to improve retrieval or store lessons. Prompt-only "reflection" does not version RAG configs or create auditable improvement trails.

2025–2026 research (MemPro, MUSE, Loop Engineering) treats **system-level evolution** as the product: evaluators + memory + tunable pipelines.

## Decision

Add a sixth reference layer: **LoopForge** — Agent → Harness → Loops → Memory.

1. **Harness** owns ODAEU scheduling and trace export
2. **Inner ReAct** uses MCP tools on a real corpus
3. **Outer Evolve** mutates RAG config on eval failure and writes procedural memory
4. Do not merge self-improvement into orchestration or governance repos

## Consequences

**Positive**

- Inspectable RAG version tree for technical review panels
- Clear portfolio story for applied AI / loop engineering roles
- Composable with existing stack — governance can wrap MCP side effects in v2

**Negative**

- Additional repo to maintain
- v1 uses simplified hybrid retrieval — pairs with Enterprise RAG for production embeddings

## Proof

[loop-engine-agent-platform.vercel.app](https://loop-engine-agent-platform.vercel.app)

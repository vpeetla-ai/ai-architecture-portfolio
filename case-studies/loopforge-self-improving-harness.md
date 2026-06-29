# LoopForge — Self-Improving Agent Harness

**Domain:** Loop engineering · Applied AI  
**Live demo:** [loop-engine-agent-platform.vercel.app](https://loop-engine-agent-platform.vercel.app)  
**Source:** [loop-engine-agent-platform](https://github.com/vpeetla-ai/loop-engine-agent-platform)

## Problem

Static RAG configs and one-shot agents do not improve. When retrieval recall or answer faithfulness fails, teams manually tweak `top_k`, hybrid weights, and prompts — with no version history or procedural memory.

## Architecture

```text
Agent → Harness → Loops → Memory
```

| Component | Role |
|-----------|------|
| **Harness** | ODAEU scheduler, iteration budget, trace export |
| **ReAct loop** | Inner tool use via MCP (`read_file`, `search_docs`) |
| **Evolve loop** | Outer loop on eval failure — tune RAG + write lesson |
| **Memory** | Procedural lessons + RAG config version tree |
| **Evaluator** | Recall + faithfulness gates |

## Key decisions

- Separate harness from agent — inspired by MemPro, MUSE, Harness Engineering research
- RAG pipeline as evolvable config (`top_k`, `hybrid_alpha`, `rerank_threshold`)
- MCP bridge for real corpus tools — extensible to stdio MCP servers
- LSS-inspired loop declaration in YAML

## Trade-offs

| Choice | Why | Cost |
|--------|-----|------|
| JSON file memory (v1) | Zero-infra demo on free tier | Not multi-tenant |
| MockLLM default | Recruiters can run without API keys | Less impressive answer quality offline |
| Hybrid lexical scorer | Transparent tuning signal | Not production embeddings |

## Impact

- Demonstrates **measurable RAG version progression** across eval failures
- Sixth layer of governed AI reference stack: **How do agents improve?**
- Portfolio flagship for loop engineering + applied AI recruiting

## Stack

Python · FastAPI · MCP · Vercel · Render · Groq (optional)

## Related

- [ADR-001 in repo](https://github.com/vpeetla-ai/loop-engine-agent-platform/blob/main/docs/ADR-001-loop-harness-memory.md)
- Pairs with VAP (orchestration), Enterprise RAG (knowledge), AegisAI (governance)

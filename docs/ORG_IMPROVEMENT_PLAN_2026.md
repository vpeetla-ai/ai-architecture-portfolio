# vpeetla-ai Org Improvement Plan — 2026

**Principal AI Architect review** — product + architecture alignment with current agentic AI trends.

> Trends anchor: [MCP + A2A protocol stack](https://niteagent.com/blog/2026-06-07-agent-protocol-stack-mcp-a2a-production/), [production agent patterns](https://internative.net/insights/blog/agentic-ai-architecture-2026), [MLflow production agents](https://mlflow.org/articles/building-production-ready-ai-agents-in-2026/), [skill management](https://tobias-weiss.org/content/ai/agent-skill-management/).

---

## Executive summary

The org already leads on **governed multi-agent systems** (orchestration + gateway + RAG + AgentOps + loops + inference lab + org skills). The highest ROI improvements are:

1. **Portfolio truthfulness** — align site copy with each repo's honest status table
2. **Protocol stack completion** — MCP everywhere tools exist; document A2A boundaries
3. **Observability parity** — Langfuse/OTel on every platform API path
4. **Gateway on all side effects** — including LoopForge git push / PR create
5. **Eval-as-product** — golden fixtures + regression gates per platform repo

---

## 2026 reference architecture (target state)

```text
Skills (vpeetla-ai-skills)     → how agents & engineers develop
Orchestration (VAP)            → what agents do        [MCP client]
Governance (AegisAI)           → what agents may do    [gateway + HITL]
Knowledge (Enterprise RAG)     → what they may know  [access-before-ranking]
AgentOps (AegisLoop)           → how fleets run      [missions + eval gates]
Application (Content Factory)  → what they produce   [HITL publish]
Self-improvement (LoopForge)   → how they improve    [ODAEU harness]
Inference (vLLM Lab)           → how LLMs serve      [PagedAttention edu]
Patterns (×5)                  → composable units    [stub-first traces]
```

**Protocol layers (ADR-007):**

| Layer | Standard | Our implementation |
|-------|----------|------------------|
| Tool access | MCP | LoopForge `mcp/bridge.py`; extend to VAP tools |
| Agent coordination | A2A (document) | VAP orchestrator → specialists (in-process today) |
| Engineering discipline | Agent Skills | `vpeetla-ai-skills` — Cursor + Codex |
| Observability | OpenTelemetry | Enterprise RAG OTLP; Langfuse on VAP/AegisLoop/Content Factory |
| Governance | Gateway + HITL | AegisAI — extend to all side-effect paths |

---

## Per-repo improvement backlog

### P0 — Credibility (this sprint)

| Repo | Product | Architecture | Action |
|------|---------|--------------|--------|
| venkat-ai-portfolio | Metric drift (10 vs 12 demos) | Single `data/metrics.ts` | ✅ Fix counts; honest AegisAI/Content Factory claims |
| loop-engine-agent-platform | No status table | No gateway on PR push | Add honest table; gateway on git side effects |
| ai-content-factory | Smoke-only tests | Gateway not in status table | Add gateway row; pytest for graph/HITL |
| vpeetla-ai-skills | No vllm mapping | No MCP/observability skills | New skills + repo map |

### P1 — Platform depth (2–4 weeks)

| Repo | Improvement |
|------|-------------|
| **venkat-ai-platform** | HITL deep-link to AegisAI; MCP tool registry doc |
| **aegisai** | Postgres registry persistence; Content Factory cron gateway |
| **enterprise_rag_platform** | `docs/ARCHITECTURE.md` hub; live LLM answer path |
| **aegisloop** | Fix stale mermaid; mission architecture doc; more tests |
| **ai-content-factory** | Real OAuth publish; gateway fail-closed prod mode |
| **loop-engine** | Langfuse on harness iterations; eval regression suite |
| **vllm-architecture-lab** | Cross-link from VAP model-router docs |

### P2 — Pattern repos (ongoing)

| Improvement | All 5 patterns |
|-------------|----------------|
| Honest status table (stub ✅, gateway ❌) | Compact 5-row table in README |
| Shared trace JSON schema | Export format for portfolio comparison |
| "Compose into VAP" guide | Link pattern → orchestrator slot |

### P3 — Portfolio & narrative

| Item | Owner repo |
|------|------------|
| Case study: vLLM Architecture Lab | ai-architecture-portfolio |
| Case study: vpeetla-ai-skills | ai-architecture-portfolio |
| Substack: 2026 Agent Protocol Stack essay | ai-content-factory `docs/content/` |
| Generated status dashboard from repo tables | venkat-ai-portfolio CI |

---

## Trend alignment scorecard

| 2026 trend | Current strength | Gap |
|------------|------------------|-----|
| MCP tool standardization | LoopForge + Content Factory + VAP docs | Stdio MCP server packaging (Phase 3) |
| Agent skills (SKILL.md) | vpeetla-ai-skills org-wide (19 skills) | Versioning semver |
| Gateway governance | AegisAI + Content Factory + LoopForge git | Pattern repos N/A (honest ❌) |
| HITL before side effects | AegisAI + Content Factory + LoopForge | VAP notify partial |
| Evals + regression | Enterprise RAG, AegisLoop, Content Factory pytest | Pattern golden cross-repo |
| Observability (OTel/Langfuse) | 6/7 platforms | Enterprise RAG OTLP |
| Inference optimization | vLLM lab + VAP INFERENCE.md | Self-hosted vLLM behind router |
| Honest implementation tables | 7/7 platforms + patterns | Portfolio CI validator |
| A2A inter-agent protocol | In-process LangGraph | Document as future A2A peer layer |

---

## Canonical metrics (portfolio source of truth)

| Metric | Value | Notes |
|--------|-------|-------|
| Platform live demos | **7** | AegisAI, VAP, Enterprise RAG, AegisLoop, Content Factory, LoopForge, vLLM Lab |
| Pattern live demos | **5** | ReAct, Reflection, Plan-Execute, Multi-Agent, Swarm |
| **Total live demos** | **12** | All on Vercel free tier (+ Render APIs) |
| Open-source repos | **16** | Per GitHub org, excluding profile README repo |
| Documented ADRs | **7** | Including ADR-007 protocol stack |
| Agent skills | **19** | After enterprise-ai-architect + Phase 2 |

---

## Implementation phases

### Phase 1 — Done in this PR
- [x] ORG_IMPROVEMENT_PLAN_2026.md (this doc)
- [x] ADR-007 Agent Protocol Stack
- [x] Skills: MCP, observability, honest-status, vllm-inference, protocol-stack
- [x] Portfolio metrics sync (`data/metrics.ts`)
- [x] LoopForge honest status table
- [x] Content Factory gateway status row

### Phase 2 — Done (2026 sprint)
- [x] Content Factory pytest suite (graph + HITL routes)
- [x] Content Factory MCP bridge + docs
- [x] LoopForge AegisAI gateway on PR workflow
- [x] LoopForge Langfuse harness export
- [x] Enterprise RAG `docs/ARCHITECTURE.md`
- [x] AegisLoop architecture doc + mermaid fix
- [x] Pattern repos honest status tables (×5)
- [x] Case studies: vLLM Lab + vpeetla-ai-skills
- [x] Skills CI smoke test + `enterprise-ai-architect` skill
- [x] VAP MCP + INFERENCE docs
- [x] Protocol stack essay (`ai-content-factory/docs/content/`)

### Phase 3 — Done (Q3 2026)
- [x] A2A Agent Card on VAP specialist endpoints (teaching)
- [x] MCP server packaging for org tools (`vpeetla-ai-skills/mcp/`)
- [x] Portfolio CI: demo URL + status table validator
- [x] Enterprise RAG OTLP tests + ARCHITECTURE sync

### Phase 4 — Started
- [x] Golden Eval Registry repo (versioned cross-repo fixtures + validator)
- [ ] Consumer adapters that import registry suites in platform CI
- [ ] Self-hosted vLLM behind VAP router (documented out of scope in INFERENCE.md)
- [ ] Portfolio CI: cross-repo README status table scraper
- [ ] MCP server on PyPI

---

## Connect

- [ADR-007](../adr/ADR-007-2026-agent-protocol-stack.md)
- [vpeetla-ai-skills](https://github.com/vpeetla-ai/vpeetla-ai-skills)
- [venkat-ai.com/work](https://venkat-ai.com/work)

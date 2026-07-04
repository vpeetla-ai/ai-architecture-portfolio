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
| **loop-engine** | Eval regression suite; wire `vpeetla_observability` middleware |
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
| MCP tool standardization | Bidirectional in AegisAI — gate inbound + expose outbound (ADR-013) | Stdio MCP server packaging org-wide (Phase 3) |
| Agent skills (SKILL.md) | vpeetla-ai-skills org-wide (19 skills) | Versioning semver |
| Gateway governance | AegisAI + Content Factory + LoopForge git | Pattern repos N/A (honest ❌) |
| HITL before side effects | AegisAI + Content Factory + LoopForge | VAP notify partial |
| Evals + regression | Enterprise RAG, AegisLoop, Content Factory pytest | Pattern golden cross-repo; golden-eval-registry fixtures not yet wired as a live CI gate (Phase 7) |
| Observability (OTel/Langfuse) | 7/7 platforms | Cross-repo `trace_id` in audit events |
| Inference optimization | vLLM lab + VAP INFERENCE.md | Self-hosted vLLM behind router |
| Honest implementation tables | 7/7 platforms + patterns | Portfolio CI validator |
| A2A inter-agent protocol | Real: VAP is a live A2A server, AegisLoop is a real, tested A2A client (discover-then-invoke, ADR-013) | Only one client repo so far — aegisai/content-factory could delegate too |
| Cloud/infra (Terraform, K8s) | None — 100% Vercel/Render PaaS | Real hands-on AWS + GCP IaC (Phase 7) |

---

## Canonical metrics (portfolio source of truth)

**This table is a snapshot, not the source of truth — it drifted out of sync with
`venkat-ai-portfolio/data/metrics.ts` once before (7 ADRs shown here after the real
count reached 10). The `orgMetrics` object in that file is authoritative; update this
snapshot to match it whenever either changes, don't treat this markdown table as
canonical on its own.**

| Metric | Value | Notes |
|--------|-------|-------|
| Platform live demos | **8** | AegisAI, VAP, Enterprise RAG, AegisLoop, Content Factory, LoopForge, vLLM Lab, Sentinel Brief |
| Pattern live demos | **5** | ReAct, Reflection, Plan-Execute, Multi-Agent, Swarm |
| **Total live demos** | **13** | All on Vercel free tier (+ Render APIs) |
| Open-source repos | **19** | Per GitHub org, excluding the private portfolio repo — adds `agent-finops` (2026-07-04) |
| Documented ADRs | **13** | ADR-001 through ADR-013, incl. the 2026-07-03 auth-gate fixes (008/009/010), the AgentFinOps standalone-service decision (011) and its consumer-wiring in AegisLoop (012 — AegisAI's consumer wiring is ADR-0004 in its own repo-local sequence), and bidirectional MCP + real A2A discovery (013) |
| Agent skills | **20** | Per `vpeetla-ai-skills` |

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

### Phase 5 — Done (2026-07-03 security + auth audit)
- [x] Fixed unauthenticated/expensive endpoints across 6 repos: `loop-engine-agent-platform`
      (ADR-002 — repo-fix + PKCE isolation), `sentinel-brief` (ADR-0002 — `/runs` gate + real
      LLM synthesis replacing the template-only summarizer), `aegisai-enterprise-agent-platform`
      (ADR-0003 — cron orchestrator auth), `venkat-ai-platform` (ADR-009 — chat/orchestrator/
      ingest/RAG/threads gate, the widest-blast-radius fix — one route could send real Slack/
      Telegram/WhatsApp messages with zero auth), `enterprise_rag_platform` (ADR-0004 — API gate
      *and* disclosed that its `Principal` is client-asserted, not verified, in the risk register),
      `aegisloop-agentops-workbench` (ADR-010 — same gap independently in both its FastAPI backend
      and its Netlify function)
- [x] `ai-content-factory`: real LinkedIn/X OAuth + PKCE (was mocked), invite-gated signup,
      Terms/Privacy pages, honest Medium/Substack/Instagram copy-draft fallback (ADR-008)
- [x] Corrected 2 repo README claims that were *understated* relative to reality: AegisAI's
      Postgres-backed registry already existed (README said "in-memory today"); confirmed and
      corrected the org's "no A2A anywhere" assumption — VAP has a real external A2A discovery
      surface
- [x] Portfolio metrics sync: `documentedAdrs` was 7, actual 10; fixed a second hardcoded "7
      ADRs" literal that had silently bypassed `metrics.ts`'s single-source-of-truth rule; added
      the 4 missing ADR entries (007–010) to `architecture-portfolio.ts`
- [x] Corrected 2 more stale portfolio claims: `ai-content-factory` OAuth no longer described as
      mocked; `enterprise_rag_platform` observability described as OTLP (removed org-wide in
      favor of Langfuse a prior sprint)

### Phase 6 — In progress
- [x] **AgentFinOps Stage 1 — standalone service built.** New repo
      [agent-finops](https://github.com/vpeetla-ai/agent-finops): real usage metering, one
      canonical pricing table, budget breach detection, Python SDK with graceful local fallback.
      22 tests, verified end-to-end against a live running instance. See
      [ADR-011](../adr/ADR-011-agent-finops-standalone-service.md). Directly ties to the
      Substack piece ["Enterprise AI FinOps Architecture"](https://venkatapeetla.substack.com/p/enterprise-ai-finops-architecture)
      (2026-06-09) — the audit that found this gap is itself proof of the article's thesis.
- [x] **AgentFinOps Stage 2 — consumers wired.** `aegisai`'s `WebsiteBuildOrchestrator` (4 of 5
      agents call an LLM, all map to existing registry entries) records real usage per node and
      wires a budget breach to the existing, real `KillSwitchService` — see
      [aegisai ADR-0004](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform/blob/main/adr/0004-real-finops-metering-website-build.md).
      `aegisloop`'s `research`/`content` missions (the only 2 of 5 mission types that call an
      LLM) record real usage against a stable repo-wide scope and halt further agent dispatch on
      either agent-finops's own breach signal or a local `MISSION_BUDGET_USD` threshold (no
      kill-switch there, so enforcement is "refuse to keep spending") — see
      [ADR-012](../adr/ADR-012-aegisloop-finops-metering.md). Both repos' README FinOps rows
      updated to reflect real metering, not estimates.
- [ ] **Real usage-metrics capture for ai-content-factory.** Now that OAuth/invite-gating is
      real, add a small, honest counter (real runs, real invited users) surfaced on the
      portfolio instead of implying scale via "live demo" framing alone.
- [ ] **Portfolio social proof.** GitHub stars/activity widget; testimonial/quote block
      (needs real testimonial content — not something to fabricate).
- [ ] **Distribution cadence signal.** Surface last-published date / posting cadence from the
      already-working Substack sync, not just a static post list.

### Phase 7 — Top-1% AI Architect program (In progress, 2026-07-04)

Mapped the org against a well-known 15-step "AI Architect roadmap" infographic (role →
fundamentals → cloud/infra → deep learning → GenAI/LLMs → RAG → architecture patterns →
agents/workflows → MLOps/LLMOps → security/governance → case studies → portfolio →
interviews → career growth) to find real, verified gaps rather than assumed ones — full plan
tracked outside this repo; sub-items logged here as they ship.

- [x] **Phase A — bidirectional MCP + real A2A.** AegisAI now exposes governed capabilities as
      real MCP tools (`interfaces/mcp/server.py`), complementing its existing inbound
      `McpGovernanceProxy` gate. AegisLoop's VAP delegation now performs genuine A2A discovery
      (`GET /orchestrators/{id}/agent-card`) before invoking `/run`, replacing a hardcoded
      orchestrator-id guess — AegisLoop is the org's first real A2A client. See
      [ADR-013](../adr/ADR-013-mcp-exposure-and-real-a2a-delegation.md).
- [ ] **Phase B — golden-eval-registry becomes a real CI gate.** Closes the Phase 4 item above:
      a real scorer/runner executes suites against a live instance in at least 2 consumer
      repos' CI, not just fixture validation.
- [ ] **Phase C — genuine hands-on AWS + GCP infra.** `agent-finops` on GCP Cloud Run + Cloud
      SQL; `aegisai`'s API on AWS ECS Fargate + RDS + ALB. Real, temporary cloud spend —
      stood up, verified, torn down per session, not left running.
- [ ] **Phase D — data foundations.** Explicit ingestion data contracts + lineage metadata in
      `enterprise_rag_platform`.
- [ ] **Phase E — new repo `ai-architect-interview-playbook` (public).** System design,
      cloud-architecture, STAR-method behavioral, and scalability/governance trade-off content,
      grounded in this org's real ADRs and outcomes rather than generic prep.
- [ ] **Phase F — portfolio UI.** New `/roadmap` page mapping all 15 infographic steps to real
      proof; retire the stale, disconnected `data/architecture.ts` stub in favor of the
      maintained `architecture-portfolio.ts`.

---

## Connect

- [ADR-007](../adr/ADR-007-2026-agent-protocol-stack.md)
- [vpeetla-ai-skills](https://github.com/vpeetla-ai/vpeetla-ai-skills)
- [venkat-ai.com/work](https://venkat-ai.com/work)

# vpeetla-ai Org Review — Principal AI Architect (2026)

**Scope:** All 15 repos under [vpeetla-ai](https://github.com/vpeetla-ai)  
**Bar:** Every product names **who it serves**, **architecture diagram**, **trade-offs**, **case study / ADR** where platform-grade.

---

## Executive summary

The org is unusually complete for a portfolio: **7 platform demos + 5 pattern demos + skills + architecture hub**. Phase 2–3 closed the protocol stack (MCP, gateway on git push, A2A cards, portfolio CI).

**Remaining gaps** are mostly **product framing consistency** and **one cross-cutting eval product** — not missing core tech.

---

## Repo scorecard

| Repo | User/customer clear? | Architecture | Trade-offs | Case study |
|------|---------------------|--------------|------------|------------|
| venkat-ai-platform | ✅ | ✅ ARCHITECTURE.md | ✅ Principal design doc | ✅ |
| aegisai-enterprise-agent-platform | ✅ | ✅ | ✅ ADRs | ✅ |
| enterprise_rag_platform | ✅ | ✅ ARCHITECTURE.md | ✅ ADRs | ✅ |
| aegisloop-agentops-workbench | ✅ | ✅ ARCHITECTURE.md | 🟡 partial | ✅ |
| ai-content-factory | ✅ PRODUCT.md added | ✅ | ✅ case study upgraded | ✅ |
| loop-engine-agent-platform | ✅ | ✅ | ✅ README | ✅ |
| vllm-architecture-lab | ✅ PRODUCT.md added | ✅ tabs + code | ✅ case study | ✅ |
| vpeetla-ai-skills | ✅ | ✅ CONTEXT | N/A | ✅ |
| ai-architecture-portfolio | ✅ | ✅ ADRs | ✅ | hub |
| venkat-ai-portfolio | ✅ | ✅ ecosystem.ts | ✅ | site |
| 5 pattern repos | 🟡 teaching only | 🟡 trace UI | ✅ status table | ❌ (by design) |
| vpeetla-ai (profile) | ✅ | ✅ stack table | — | links |

---

## Improvements shipped (this review)

1. **Skill:** `agents-that-run-for-days` — Karpathy LOOPS.md / autoresearch field notes
2. **docs/LOOPS.md** — org reference + LoopForge overnight protocol
3. **docs/PRODUCT.md** — ai-content-factory, vllm-architecture-lab
4. **Case study** — ai-content-factory trade-offs + mermaid
5. **Profile** — 12 live demos (was 11)

---

## Suggested new project (highest portfolio value)

### 1. `golden-eval-registry` (recommended)

**Who it serves:** You + hiring panels — proves agents **regress safely** across the stack.

**Problem:** Golden queries live in Enterprise RAG; pytest in Content Factory; missions in AegisLoop — no **single regression hub**.

**MVP:**
- One repo with `fixtures/` per platform (RAG, LoopForge harness, Content Factory graph smoke)
- GitHub Action matrix invokes each package's tests
- Portfolio badge: "12 demos · N golden evals passing"

**Why now:** Completes "evals as product" from ADR-007; differentiates from demo-only portfolios.

### 2. `program.md` overnight runner (LoopForge extension)

**Who it serves:** Engineers running Karpathy-style unattended loops on repo-fix or RAG tune.

**MVP:** CLI `loopforge overnight --loops docs/LOOPS.md` wrapping existing harness with iteration log + git keep/discard.

**Maps to:** New `agents-that-run-for-days` skill.

### 3. `agent-cost-slo-dashboard` (lower priority)

Aggregate Langfuse/FinOps from VAP + AegisLoop — nice for enterprise narrative, heavier to build.

---

## Phase 4 backlog (safe, incremental)

| Item | Owner |
|------|-------|
| PRODUCT.md for remaining platforms (VAP, AegisAI, Enterprise RAG) | respective repos |
| Pattern mini case studies (1-pager each) | ai-architecture-portfolio |
| Portfolio `--strict-urls` only on release tags | venkat-ai-portfolio |
| golden-eval-registry repo | new |

---

## Connect

- [ADR-007](../adr/ADR-007-2026-agent-protocol-stack.md)
- [ORG_IMPROVEMENT_PLAN_2026](./ORG_IMPROVEMENT_PLAN_2026.md)
- Skill: [agents-that-run-for-days](https://github.com/vpeetla-ai/vpeetla-ai-skills/tree/main/skills/agents-that-run-for-days)

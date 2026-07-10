# Top-1% Principal — 90-Day Sequenced Backlog

**Owner:** vpeetla-ai org  
**Source review:** Principal org review (Jul 9 2026)  
**Rule:** Fewer claims, harder gates, one always-on proof — **do not expand surface area**.

Status legend: `TODO` · `IN_PROGRESS` · `DONE` · `BLOCKED`

---

## Phase 0 — Program control (Day 0)

| ID | Action | Repo(s) | Done when | Status |
|----|--------|---------|-----------|--------|
| **P0.1** | Publish this backlog + link from portfolio README / ORG_IMPROVEMENT_PLAN | `ai-architecture-portfolio` | Doc merged; linked | `DONE` |
| **P0.2** | Create GitHub issues from this table (requires `gh auth login`) | org | Issues open with same IDs | `TODO` |

---

## Phase 1 — Honesty + identity (Days 1–30)

| ID | Action | Repo(s) | Acceptance criteria | Status |
|----|--------|---------|---------------------|--------|
| **P1.1** | Sync ADR / metrics counts | `venkat-ai-portfolio`, `ai-architecture-portfolio`, `vpeetla-ai` | `documentedAdrs` matches ADR table; profile/hero synced; `validate-portfolio.mjs` passes | `DONE` |
| **P1.2** | Kill aspirational ACF HLD | `ai-content-factory` | README Architecture section shows **implemented** topology only (canonical `.mmd`); aspirational 9-layer mermaid removed or clearly labeled Target/not shipped | `DONE` |
| **P1.3** | Fix VAP golden-eval CI claim | `venkat-ai-platform` | `docs/SLO.md` matches CI reality (no false “per merge golden gate”); either wire a real gate **or** mark Planned | `DONE` |
| **P1.4** | Org `PRODUCTION_STRICT` convention | `ai-architecture-portfolio` (+ first consumer) | ADR-024 accepted; at least one gateway client fail-closed when flag set; docs in CONTEXT | `DONE` |
| **P1.5** | Verified Principal (JWT/OIDC) on Enterprise RAG | `enterprise_rag_platform` | ADR + API path: Principal from verified token (not request-body spoof) in strict mode; tests; risk-register updated | `DONE` |
| **P1.6** | Pattern series claim hygiene | `vpeetla-ai` profile + 5 pattern READMEs | Hero/copy says “curriculum stubs” or each has LangGraph+golden; no “production-grade” without status table ❌ rows | `DONE` |

---

## Phase 2 — Hard gates (Days 31–60)

| ID | Action | Repo(s) | Acceptance criteria | Status |
|----|--------|---------|---------------------|--------|
| **P2.1** | LoopForge ephemeral container sandbox | `loop-engine-agent-platform` | `run_pytest` / clone work runs in disposable container; README sandbox row ✅ or Partial+ADR; ADR | `DONE` |
| **P2.2** | Threat model + NIST AI RMF ADR | `ai-architecture-portfolio` | ADR-025 control mapping; links to gateway/HITL/eval | `DONE` |
| **P2.3** | Adversarial golden suites | `golden-eval-registry` + ERAG | Jailbreak / Principal-spoof / injection cases gate CI | `DONE` |
| **P2.4** | Wire VAP golden CI for real | `venkat-ai-platform`, `golden-eval-registry` | Suite + workflow; SLO row becomes ✅ | `DONE` |
| **P2.5** | Propagate `PRODUCTION_STRICT` to ACF publish + LoopForge git | `ai-content-factory`, `loop-engine-agent-platform` | Fail-closed gateway required in prod profile; tests | `DONE` |
| **P2.6** | AegisAI: no seed monitor in prod mode | `aegisai-enterprise-agent-platform` | Seed events disabled when strict; OPA fail-closed option documented | `DONE` |

---

## Phase 3 — Always-on proof (Days 61–90)

| ID | Action | Repo(s) | Acceptance criteria | Status |
|----|--------|---------|---------------------|--------|
| **P3.1** | Persistent eval runner **or** Sentinel report archive | `golden-eval-registry` / `sentinel-brief` | One non-sleeping path with durable artifacts + public health | `DONE` |
| **P3.2** | Thin DomainForge → vLLM multi-LoRA slice | `domainforge-rag-peft`, `vllm-architecture-lab` | ADR-022 → Accepted with runnable path (even one adapter) | `DONE` |
| **P3.3** | Practice Arena coverage decision | `ai-architect-practice-arena` | Either 35/35 or README claim narrowed to calibrated N | `DONE` |
| **P3.4** | Multi-tenant isolation ADR (+ thin demo) | `ai-architecture-portfolio` (+ one API) | ADR-026 blast-radius / quota / data isolation | `DONE` |
| **P3.5** | Portfolio CI: auto-check ADR count vs metrics.ts | `venkat-ai-portfolio` | Validator fails on ADR drift | `DONE` |

---

## Explicit non-goals (90 days)

- New pattern / tutorial repos
- New “platform” demos that increase free-tier surface
- Aspirational multi-cloud always-on without a single durable proof first

---

## Progress log

| Date | ID | Note |
|------|-----|------|
| 2026-07-09 | P0.1 | Backlog + implementation plan created |
| 2026-07-09 | P1.1 | metrics.ts → 24 ADRs; portfolio README + profile synced; validator OK |
| 2026-07-09 | P1.2 | ACF README shows canonical diagram; aspirational HLD moved to docs/diagrams/ |
| 2026-07-09 | P1.3 | VAP SLO eval gate marked Planned (honest) |
| 2026-07-09 | P1.4 | ADR-024; ACF `production_strict` fail-closed publish; gateway tests |
| 2026-07-09 | P1.5 | ERAG ADR-0006; JWT Principal under PRODUCTION_STRICT; 12 auth/jwt tests pass |
| 2026-07-09 | P1.6 | Pattern series rebranded to curriculum stubs (profile + 5 READMEs) |
| 2026-07-09 | P2.1 | LoopForge Docker ephemeral sandbox + ADR-003 |
| 2026-07-09 | P2.2 | ADR-025 NIST AI RMF threat-model mapping |
| 2026-07-09 | P2.3 | enterprise_rag_adversarial_v1 suite + ERAG CI gate |
| 2026-07-09 | P2.4 | vap_orchestrator_invariant_v1 + VAP golden CI workflow |
| 2026-07-09 | P2.5 | LoopForge PRODUCTION_STRICT fail-closed gateway (ACF already done) |
| 2026-07-09 | P2.6 | AegisAI skips seed monitor under PRODUCTION_STRICT |
| 2026-07-09 | P3.1 | Sentinel committed `archives/` + GET /reports merge; golden nightly-smoke workflow |
| 2026-07-09 | P3.2 | ADR-022 Accepted educational Path B; DomainForge↔vLLM Lab chat+adapter_id |
| 2026-07-09 | P3.3 | Practice Arena README/UI claim 35/35 + 139/140 calibration |
| 2026-07-09 | P3.4 | ADR-026 multi-tenant isolation contract |
| 2026-07-09 | P3.5 | validate-portfolio.mjs ADR drift check vs sibling portfolio |

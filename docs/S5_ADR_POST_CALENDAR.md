# S5.1 — ADR post calendar (10 posts)

**Cadence:** 1× LinkedIn + optional Substack deep-dive every ~weekly  
**Rule:** Decision first · demo second · CTA to technical review / golden path  
**Skeleton:** [LINKEDIN_POST_TEMPLATES.md](./LINKEDIN_POST_TEMPLATES.md)

| # | Week | ADR | Hook (decision) | Primary proof link | Channel | Status |
|---|------|-----|-----------------|--------------------|---------|--------|
| 1 | W1 | [ADR-001](../adr/ADR-001-orchestration-vs-governance-split.md) | Orchestration ≠ governance — split the layers or inherit panic | [Essay](../case-studies/from-multi-agent-os-to-agent-governance.md) · AegisAI live | LinkedIn + Substack | `TODO` |
| 2 | W2 | [ADR-002](../adr/ADR-002-authorization-before-ranking-rag.md) | Ranking before auth is a data leak | ERAG demo · Strict ADR-0006 | LinkedIn | `TODO` |
| 3 | W3 | [ADR-004](../adr/ADR-004-gateway-hitl-side-effects.md) | Side effects need a gateway or they are bugs | Golden path AegisAI `approval_required` | LinkedIn | `TODO` |
| 4 | W4 | [ADR-009](../adr/ADR-009-vap-auth-gate.md) | Open `/chat` is not a portfolio win | VAP API-key honesty in [GOLDEN_PATH](./GOLDEN_PATH.md) | LinkedIn | `TODO` |
| 5 | W5 | [ADR-014](../adr/ADR-014-golden-eval-registry-real-ci-gate.md) | Evals that don’t gate CI are theater | [GER CI badge](https://github.com/vpeetla-ai/golden-eval-registry/actions/workflows/ci.yml) | LinkedIn | `TODO` |
| 6 | W6 | [ADR-024](../adr/ADR-024-production-strict-fail-closed.md) | Demo defaults must say “demo” out loud | Spine Demo vs Strict banners | LinkedIn | `TODO` |
| 7 | W7 | [ADR-023](../adr/ADR-023-enterprise-rag-rerank-decline.md) | Decline-to-answer is a feature | ERAG glass-box | LinkedIn | `TODO` |
| 8 | W8 | [ADR-011](../adr/ADR-011-agent-finops-standalone-service.md) | Cost without a meter is folklore | FinOps in golden-path artifact | LinkedIn | `TODO` |
| 9 | W9 | [ADR-025](../adr/ADR-025-nist-ai-rmf-threat-model.md) | Map controls to NIST AI RMF before the audit | ADR-025 | LinkedIn + Substack | `TODO` |
| 10 | W10 | [ADR-028](../adr/ADR-028-federated-ai-control-plane-k8s-analogy.md) / [029](../adr/ADR-029-app-owned-role-aware-routing-contract.md) | Apps select; gateway enforces + records | LLM gateway `/v1/posture` stub default | LinkedIn | `TODO` |

Optional #11–12 if cadence allows: ADR-008 (publish HITL), ADR-026 (multi-tenant isolation).

---

## Ready-to-paste drafts (Posts 1–4)

### Post 1 — ADR-001

```text
Orchestration without governance is a demo. Governance without orchestration is bureaucracy.

I split the problem into two open systems:
→ VAP answers what agents should do
→ AegisAI answers what they are allowed to do

ADR-001 is the decision record — not a product launch.

15-min review: https://venkat-ai.com/technical-review
Golden path artifact: https://github.com/vpeetla-ai/ai-architecture-portfolio/blob/main/docs/GOLDEN_PATH.md

#AgentGovernance #LangGraph #AIArchitecture
```

### Post 2 — ADR-002

```text
Ranking before authorization is a data leak — not a retrieval bug.

Enterprise RAG filters by principal clearance before hybrid scoring, then reranks and declines when evidence is weak.

Prefer Strict/JWT for Principal panels (PRODUCTION_STRICT). Live demo still labels Demo mode honestly.

Live: https://enterprise-rag-platform-eta.vercel.app
ADR: github.com/vpeetla-ai/ai-architecture-portfolio/blob/main/adr/ADR-002-authorization-before-ranking-rag.md

#EnterpriseAI #RAG #AIArchitecture
```

### Post 3 — ADR-004

```text
If an agent can deploy without a human checkpoint, you don’t have an agent platform — you have an incident generator.

AegisAI’s gateway returns approval_required + HITL for deploy-class tools. The spine golden path records that decision in a public JSON artifact strangers can replay.

Replay: https://github.com/vpeetla-ai/ai-architecture-portfolio/blob/main/docs/GOLDEN_PATH.md
Control plane: https://aegisai-enterprise-agent-platform.vercel.app

#HITL #AgentOps #AIArchitecture
```

### Post 4 — ADR-009

```text
A public /chat that burns LLM tokens without a key is not “open source culture.” It’s an unpaid bill waiting to happen.

VAP gates mutating routes with X-API-Key (ADR-009). The golden path records 401 without keys instead of faking success — honesty beats vanity metrics.

Technical review: https://venkat-ai.com/technical-review

#APISecurity #AIArchitecture #PlatformEngineering
```

---

## Ready-to-paste drafts (Posts 5–10)

### Post 5 — ADR-014

```text
If an eval suite doesn’t gate CI, it’s a slide — not a control.

Golden Eval Registry turns adversarial RAG and orchestrator invariants into merge blockers. The GER CI badge is the proof link, not a screenshot of a notebook.

CI: https://github.com/vpeetla-ai/golden-eval-registry/actions/workflows/ci.yml
Review: https://venkat-ai.com/technical-review

#LLMOps #Evals #AIArchitecture
```

### Post 6 — ADR-024

```text
Demo defaults that pretend to be production are how portfolios lose Principal trust.

PRODUCTION_STRICT is the honesty profile: fail closed, JWT Principal on RAG, banners that say Demo when it’s Demo.

Spine health: https://venkat-ai.com/spine-health
Strict pack: https://github.com/vpeetla-ai/enterprise_rag_platform/blob/main/docs/STRICT_PANEL_PACK.md

#AISecurity #AIArchitecture
```

### Post 7 — ADR-023

```text
Decline-to-answer is a product feature, not a model failure.

Enterprise RAG reranks, then refuses when evidence is weak — better than a confident hallucination for regulated knowledge.

Live: https://enterprise-rag-platform-eta.vercel.app

#EnterpriseRAG #AIArchitecture
```

### Post 8 — ADR-011

```text
Cost without a meter is folklore.

Agent FinOps records usage and budget breach signals as a shared service. The spine golden path meters a sample turn into a public JSON artifact.

Golden path: https://github.com/vpeetla-ai/ai-architecture-portfolio/blob/main/docs/GOLDEN_PATH.md
ROI one-pager: https://github.com/vpeetla-ai/ai-architecture-portfolio/blob/main/docs/FINOPS_ROI_ONE_PAGER.md

#FinOps #AIArchitecture
```

### Post 9 — ADR-025

```text
Map agent threats to NIST AI RMF before the audit asks you to.

Govern / Map / Measure / Manage — with live links to gateway HITL, Strict RAG, and golden eval CI — not a binder of policies.

One-pager: https://github.com/vpeetla-ai/ai-architecture-portfolio/blob/main/docs/NIST_AI_RMF_ONE_PAGER.md

#NIST #ResponsibleAI #AIArchitecture
```

### Post 10 — ADR-028 / 029

```text
Apps select the model. The gateway enforces and records.

That’s the federated control-plane analogy (k8s-shaped thinking for LLM traffic): routing contract + stub/BYOK honesty + FinOps hooks.

Technical review: https://venkat-ai.com/technical-review

#LLMGateway #AIArchitecture
```

---

## Tracking

Mark `Status` → `POSTED` with date + URL in this table when published. Close [issue #6](https://github.com/vpeetla-ai/ai-architecture-portfolio/issues/6) S5.1 checkbox when ≥8 are posted.

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

## Tracking

Mark `Status` → `POSTED` with date + URL in this table when published. Close [issue #6](https://github.com/vpeetla-ai/ai-architecture-portfolio/issues/6) S5.1 checkbox when ≥8 are posted.

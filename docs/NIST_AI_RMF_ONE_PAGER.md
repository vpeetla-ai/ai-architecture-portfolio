# NIST AI RMF one-pager (P4)

**Map:** Org [ADR-025](../adr/ADR-025-nist-ai-rmf-threat-model.md) → live proof a panel can open in &lt;10 minutes.  
**Honesty:** This is a portfolio control map, not a SOC2 attestation.

| NIST AI RMF function | Control theme | Live proof |
|----------------------|---------------|------------|
| **Govern** | Orchestration ≠ governance split | [ADR-001](../adr/ADR-001-orchestration-vs-governance-split.md) · [technical-review](https://venkat-ai.com/technical-review) |
| **Map** | Threat model for agent side effects | [ADR-025](../adr/ADR-025-nist-ai-rmf-threat-model.md) |
| **Measure** | Golden eval CI + adversarial RAG suite | [GER CI](https://github.com/vpeetla-ai/golden-eval-registry/actions/workflows/ci.yml) · `enterprise_rag_adversarial_v1` |
| **Manage** | Gateway HITL before deploy-class tools | [AegisAI](https://aegisai-enterprise-agent-platform.vercel.app) · golden path `approval_required` |
| **Manage** | Access-before-ranking + Strict JWT Principal | [ERAG Demo](https://enterprise-rag-platform-eta.vercel.app) · [Strict pack](https://github.com/vpeetla-ai/enterprise_rag_platform/blob/main/docs/STRICT_PANEL_PACK.md) |
| **Manage** | Cost metering / budget breach signals | [agent-finops](https://agent-finops.vercel.app) · [FinOps ROI](./FINOPS_ROI_ONE_PAGER.md) |
| **Govern** | Demo vs Strict honesty banners | Live demos + `/spine-health` |

## Panel script (90 seconds)

Full Free-tier day script: [PANEL_DAY_FREE_RUNBOOK.md](./PANEL_DAY_FREE_RUNBOOK.md)

1. Open technical-review → AegisAI (Govern/Manage).  
2. Show golden-path artifact gateway decision.  
3. Show ERAG Strict health `review_mode=strict` (local/GCP while Render Free).  
4. Point at GER CI badge (Measure).  

## Out of scope (say out loud)

- Formal EU AI Act conformity assessment  
- Continuous multi-cloud production attestation  
- KMS-backed audit signing on free-tier demos (documented recommendation on AegisAI health)

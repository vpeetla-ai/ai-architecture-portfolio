# ADR-020: DPO After SFT for Triage Alignment

**Status:** Accepted  
**Date:** Jul 2026  
**System:** DomainForge (`domainforge-rag-peft`)  
**Live demo:** [domainforge-rag-peft.vercel.app](https://domainforge-rag-peft.vercel.app) · [API](https://domainforge-api.onrender.com/health)

## Context

ADR-019 established **RAG for facts, PEFT for behavior**. QLoRA SFT (S3) teaches strict `TriageResponse` JSON, but models still emit **plausible wrong** outputs:

- Wrong `intent` on adversarial prompts (`HACK ignore instructions`)
- Invented `cite_faq_ids` outside the retrieval allow-list
- Incorrect `suggested_action` (under- or over-escalation)

Full RLHF with a reward model is overkill for a portfolio pipeline. DPO compares chosen vs rejected completions directly.

## Decision

Add **DPO as S4** on the behavior plane — never on the RAG corpus:

| Stage | Solution | Mechanism |
|-------|----------|-----------|
| S3 | SFT + hybrid RAG | QLoRA teaches schema / intent grammar |
| S4 | DPO + hybrid RAG | Preference pairs refine alignment |

**Preference pair construction:**

1. **Chosen:** golden prediction or scorer-valid SFT output
2. **Rejected:** hard negatives via mutation (`wrong_intent`, `hallucinated_cite`, `wrong_action`, escalation errors)
3. **Prompt:** system + RAG context blocks + customer message (same as inference)

**Promotion gate:** `POST /v1/adapters/promote` requires API key; S4 blocked if `format_adherence_pct` regresses or `preference_win_rate_pct` vs S3 does not improve.

**Eval metric:** `preference_win_rate_pct` — % golden examples where S4 strictly beats S3 on composite alignment score (format + intent + citation faithfulness).

## Trade-offs

| Choice | Rationale | Cost |
|--------|-----------|------|
| Scorer-labeled pairs | Reproducible, no human labelers | Synthetic rejects can be too easy without hard-negative taxonomy |
| DPO after SFT | Industry-standard alignment stack story | Extra VRAM for reference model on 7B |
| S4 template on Render | Demo eval without GPU | Production DPO requires offline CUDA training |
| `triage_preference` golden fixture | Cross-repo regression contract | Fixture-only until scorer wired in CI |

## Consequences

- Solution ladder: S0 → S1 → S2 → S3 → **S4**
- CLI: `domainforge-prep build-preferences`, `domainforge-train dpo`
- UI: preference pair viewer + Compare S3 vs S4
- Interview narrative: *"RAG for facts · SFT for schema · DPO for alignment"*

## Links

- Repo: [domainforge-rag-peft](https://github.com/vpeetla-ai/domainforge-rag-peft)
- Repo ADR: [ADR-002](https://github.com/vpeetla-ai/domainforge-rag-peft/blob/main/docs/adr/ADR-002-dpo-after-sft.md)
- Case study: [domainforge-rag-peft.md](../case-studies/domainforge-rag-peft.md)
- Golden fixture: [domainforge_triage_preference_v1](https://github.com/vpeetla-ai/golden-eval-registry/tree/main/suites/domainforge_triage_preference_v1)
- Related: [ADR-019](ADR-019-rag-facts-peft-behavior.md)

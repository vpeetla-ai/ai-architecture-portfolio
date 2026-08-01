# ADR-020: DPO After SFT for Triage Alignment

**Status:** Accepted  
**Date:** Jul 2026  
**System:** DomainForge (`domainforge-rag-peft`)  
**Live demo:** [domainforge-rag-peft.vercel.app](https://domainforge-rag-peft.vercel.app) · [API](https://domainforge-api.onrender.com/health)

## In one breath (panel)

I'd run DPO after SFT on the behavior plane only — preference pairs beat a full RLHF reward-model circus for triage alignment in this portfolio.

## Context

[ADR-019](ADR-019-rag-facts-peft-behavior.md) split RAG (facts) from PEFT (behavior). QLoRA SFT (S3) teaches strict `TriageResponse` JSON, but models still emit **plausible wrong** outputs: wrong `intent` on adversarial prompts (`HACK ignore instructions`), invented `cite_faq_ids` outside the retrieval allow-list, under- or over-escalation on `suggested_action`.

Full RLHF with a reward model is overkill for this pipeline. DPO compares chosen vs rejected completions directly — and it stays off the RAG corpus so you don't "align" by memorizing SOP text.

## Decision

Add **DPO as S4** on the behavior plane — never on the RAG corpus.

| Stage | Solution | Mechanism |
|-------|----------|-----------|
| S3 | SFT + hybrid RAG | QLoRA teaches schema / intent grammar |
| S4 | DPO + hybrid RAG | Preference pairs refine alignment |

**Preference pairs**

1. **Chosen:** golden prediction or scorer-valid SFT output
2. **Rejected:** hard negatives via mutation (`wrong_intent`, `hallucinated_cite`, `wrong_action`, escalation errors)
3. **Prompt:** system + RAG context blocks + customer message (same as inference)

**Promotion gate:** `POST /v1/adapters/promote` requires API key; S4 blocked if `format_adherence_pct` regresses or `preference_win_rate_pct` vs S3 does not improve.

**Eval:** `preference_win_rate_pct` — % of golden examples where S4 strictly beats S3 on composite alignment (format + intent + citation faithfulness).

Refused: running DPO over retrieval chunks as if preferences were facts.

## Consequences

| Choice | Why | Cost |
|--------|-----|------|
| Scorer-labeled pairs | Reproducible, no human labelers | Synthetic rejects can be too easy without a hard-negative taxonomy |
| DPO after SFT | Standard alignment stack story | Extra VRAM for reference model on 7B |
| S4 template on Render | Demo eval without GPU | Production DPO needs offline CUDA training |
| `triage_preference` golden fixture | Cross-repo regression contract | Fixture-only until scorer wired in CI |

Ladder becomes S0 → S1 → S2 → S3 → **S4**. CLIs: `domainforge-prep build-preferences`, `domainforge-train dpo`. UI: preference pair viewer + Compare S3 vs S4. Interview line stays honest: *RAG for facts · SFT for schema · DPO for alignment*.

## Links

- Repo: [domainforge-rag-peft](https://github.com/vpeetla-ai/domainforge-rag-peft)
- Repo ADR: [ADR-002](https://github.com/vpeetla-ai/domainforge-rag-peft/blob/main/docs/adr/ADR-002-dpo-after-sft.md)
- Case study: [domainforge-rag-peft.md](../case-studies/domainforge-rag-peft.md)
- Golden fixture: [domainforge_triage_preference_v1](https://github.com/vpeetla-ai/golden-eval-registry/tree/main/suites/domainforge_triage_preference_v1)
- Related: [ADR-019](ADR-019-rag-facts-peft-behavior.md)

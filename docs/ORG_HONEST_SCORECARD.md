# Org honest scorecard

Canonical status for the public stack. **Not a Grade A tracker.** Thesis and curriculum are ahead of operating proof. If a panel finds this file, they should see the same judgment as [TOP1PCT_GAP_PLAN.md](./TOP1PCT_GAP_PLAN.md).

**Last updated:** 2026-09-04  
**Companion:** [THREE_TRACK_90DAY.md](./THREE_TRACK_90DAY.md)

The old `ORG_GRADE_A.md` filename still exists as a redirect so stale links do not look like a cover-up.

## Dimension scorecard

Independent of self-grade theater. Letter grades here mean “how a hostile Principal panel would score the public footprint,” not “did we ship a checkbox.”

| Dimension | Grade | Why this grade |
|-----------|-------|----------------|
| **Thesis / narrative** | A- | Orchestration ≠ governance, access-before-rank, Demo vs Strict, P/O/R/H. Rare and correct. |
| **Governance + RAG depth** | B+ | Real code and ADRs. Still Demo-default and Free-tier. |
| **Model plane** | C+ | Real L4 PEFT + vLLM receipts. No adapter quality / win-rate vs RAG. One dated serve run. |
| **Production realism** | C | Ops endpoints and architect landings are not users, SLOs, or a stranger-complete Strict path. Cold starts are real. |
| **DevSecOps + FinOps** | B | Org security-scan + agent-finops exist. Chargeback collected and commitment strategy do not. |
| **Reference architecture library** | B | Six AWS patterns + Terraform skeletons. Useful, not a landed zone a customer runs. |
| **Business impact storytelling** | C+ | Lucid `$10M / $7M` is spoken-locked. Resume PDF stale. Public recs are MAGNIFI iOS. Hire page used to say “incl. Google.” |
| **Interview curriculum** | A- | Playbook is the strongest artifact. Too large to rehearse. Arena pin lags the catalog. |
| **Interview readiness** | C | `release_ready` is false. Behavioral 01 / 06–09 still draft. Timed mocks not done. |

**Overall vs a top-1% Principal bar: B- / C+.** Strong Staff+ / emerging Principal. Not top 1% yet.

## What the checkboxes actually prove

A green ops endpoint proves the route exists. It does not prove a tenant used it this week.

| Repo | Honest note |
|------|-------------|
| ai-content-factory | Graph HITL eval is real. Live publish is Clerk-gated; golden path is `/health` only (ADR-008). |
| venkat-ai-platform | Orchestrators live. Notify is fail-open unless Strict. Vector store optional on Free. |
| aegisai-enterprise-agent-platform | Gateway + HITL + OPA are real. Registry defaults to in-memory on Free. |
| enterprise_rag_platform | Access-before-rank + golden gate are real. Default demo is body Principal; Strict is the panel path. |
| aegisloop-agentops-workbench | Mission gates in CI. Not a production fleet console. |
| domainforge-rag-peft | SFT/DPO ladder exists. PEFT receipt is config/timing, not a quality score. |
| loop-engine-agent-platform | Harness + repo-fix suites are real. Bounded automation, not unattended prod. |
| sentinel-brief | Brief gate in CI. Lab, not a hire hero. |
| agent-finops | Metering service exists. Not proof anyone paid a chargeback. |
| voiceforge-assistant | Voice MVP. Lab. |
| golden-eval-registry | Source of suite kinds. Merge gates are the proof, not the registry UI. |
| modelforge-llmops | Hire-facing model plane. Keep on the 15-min path; say the quality limitation first. |

## Golden eval CI gates (still true)

These suites fail the build. That is the honest eval claim — not “production AgentOps.”

| Suite | Kind | Consumer |
|-------|------|----------|
| enterprise_rag_golden_v1 | rag_answer | enterprise_rag_platform |
| aegisloop_mission_gates_v1 | mission_gate | aegisloop-agentops-workbench |
| content_factory_graph_v1 | graph_hitl | ai-content-factory |
| domainforge_triage_preference_v1 | triage_preference | domainforge-rag-peft |
| sentinel_brief_gate_v1 | brief_gate | sentinel-brief |
| loopforge_benchmark_v1 + repo_fix_v1 | harness_qa + repo_fix | loop-engine-agent-platform |

## Reference architectures (unchanged location)

Shipped in [ai-content-factory/docs/reference-architectures/](https://github.com/vpeetla-ai/ai-content-factory/tree/main/docs/reference-architectures). Terraform skeletons: [ai-content-factory/infra/aws/](https://github.com/vpeetla-ai/ai-content-factory/tree/main/infra/aws). Treat as patterns, not a landed customer environment.

## Related

- [THREE_TRACK_90DAY.md](./THREE_TRACK_90DAY.md)
- [TOP1PCT_GAP_PLAN.md](./TOP1PCT_GAP_PLAN.md)
- [ORG_IMPROVEMENT_PLAN_2026.md](./ORG_IMPROVEMENT_PLAN_2026.md)

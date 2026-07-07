# LinkedIn Readiness Audit — Tier-1 Repos

**Date:** Jul 2026 · **Rubric:** 8 criteria × 0–2 = max **16** · **Gate:** ≥14 before LinkedIn post

Scoring: **0** = missing · **1** = partial · **2** = complete

| Criterion | Description |
|-----------|-------------|
| R1 | README follows [README_STANDARD.md](./README_STANDARD.md) (11 sections) |
| R2 | Honest status table matches code |
| R3 | Canonical diagram = README = `docs/diagrams/canonical-architecture.mmd` |
| R4 | Live demo URL works (cold start documented) |
| R5 | Case study in ai-architecture-portfolio |
| R6 | ADR for top 3 decisions |
| R7 | Quick start runs (`pytest -q` + local demo) |
| R8 | LICENSE + CI badge |

---

## Tier 1 — Flagship platforms

| Repo | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | **Total** | Gate | Phase 2 |
|------|----|----|----|----|----|----|----|----|-----------|------|---------|
| **enterprise_rag_platform** | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | **15** | ✅ | README reranker row updated |
| **domainforge-rag-peft** | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | **15** | ✅ | Full README pass |
| **voiceforge-assistant** | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | **15** | ✅ | Full README pass |
| **vllm-architecture-lab** | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | **14** | ✅ | Canonical diagram added |
| **aegisai-enterprise-agent-platform** | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | **14** | ✅ | Phase 3 diagram sync |
| **venkat-ai-platform** | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | **14** | ✅ | Phase 3 diagram |
| **aegisloop-agentops-workbench** | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | **14** | ✅ | Phase 3 diagram |
| **ai-content-factory** | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **16** | ✅ | Phase 3 diagram |
| **loop-engine-agent-platform** | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | **14** | ✅ | Phase 3 diagram |
| **sentinel-brief** | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **16** | ✅ | Ready for W10 post |

---

## Tier 2 — Support repos

| Repo | Total | Gate | Notes |
|------|-------|------|-------|
| golden-eval-registry | 12 | ⬜ | No live demo (expected) |
| agent-finops | 10 | ⬜ | Added to REPO_INDEX; README pass Phase 3 |
| vpeetla-ai-skills | N/A | N/A | Not a product demo |

---

## Tier 3 — Agent patterns (×5)

| Repo | Total | Gate | Notes |
|------|-------|------|-------|
| react-agent-pattern | 10 | ⬜ | UI revamp done; README batch Phase 4 |
| reflection-agent-pattern | 10 | ⬜ | Same |
| plan-execute-agent-pattern | 10 | ⬜ | Same |
| multi-agent-system-pattern | 10 | ⬜ | Same |
| swarm-agent-pattern | 10 | ⬜ | Same |

---

## Priority fixes (from audit)

1. **CI badges** — several repos score R8=1 (CI exists but badge not in README header)
2. **CI badges** — several repos score R8=1 (CI exists but badge not in README header)
3. **agent-finops** — README standardization (Phase 4)

---

## Re-audit schedule

Re-score after each phase completion. Update [LINKEDIN_LAUNCH_PLAN.md](./LINKEDIN_LAUNCH_PLAN.md) week table when gate flips to ✅.

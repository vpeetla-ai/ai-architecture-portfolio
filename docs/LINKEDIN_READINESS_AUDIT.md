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
| **aegisai-enterprise-agent-platform** | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **16** | ✅ | Canonical diagram + CI badge + cold-start note |
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

**Demo verification (Jul 7 2026):** all five Vercel trace viewers return **HTTP 200** for signed-out visitors.

| Repo | Demo URL | HTTP | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | **Total** | Gate | Gap to ≥14 |
|------|----------|------|----|----|----|----|----|----|----|----|-----------|------|------------|
| react-agent-pattern | react-agent-pattern.vercel.app | ✅ 200 | 1 | 2 | 0 | 2 | 1 | 1 | 2 | 1 | **10** | ⬜ | canonical `.mmd` + CI workflow + Deploy section |
| reflection-agent-pattern | reflection-agent-pattern.vercel.app | ✅ 200 | 1 | 2 | 0 | 2 | 1 | 1 | 2 | 1 | **10** | ⬜ | same |
| plan-execute-agent-pattern | plan-execute-agent-pattern.vercel.app | ✅ 200 | 1 | 2 | 0 | 2 | 1 | 1 | 2 | 1 | **10** | ⬜ | same |
| multi-agent-system-pattern | multi-agent-system-pattern.vercel.app | ✅ 200 | 1 | 2 | 0 | 2 | 1 | 1 | 2 | 1 | **10** | ⬜ | same |
| swarm-agent-pattern | swarm-agent-pattern.vercel.app | ✅ 200 | 1 | 2 | 0 | 2 | 1 | 1 | 2 | 1 | **10** | ⬜ | same |

**Week 12 carousel:** demos are public and postable today; individual repo gates remain ⬜ until README batch (canonical diagram + CI badge per pattern). Carousel post uses series-level OG card — see [SOCIAL_PREVIEW_COPY.md](./SOCIAL_PREVIEW_COPY.md).

---

## Priority fixes (from audit)

1. **CI badges** — several repos score R8=1 (CI exists but badge not in README header)
2. **Pattern repos (×5)** — demos verified ✅; README batch needed for gate (canonical `.mmd`, CI workflow, Deploy section)
3. **agent-finops** — README standardization
4. **OG card export** — copy ready in [SOCIAL_PREVIEW_COPY.md](./SOCIAL_PREVIEW_COPY.md); PNG assets ⬜

---

## Re-audit schedule

Re-score after each phase completion. Update [LINKEDIN_LAUNCH_PLAN.md](./LINKEDIN_LAUNCH_PLAN.md) week table when gate flips to ✅.

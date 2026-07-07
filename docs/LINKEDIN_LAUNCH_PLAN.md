# LinkedIn Launch Plan — vpeetla-ai Portfolio

**Owner:** Principal AI Architect · **Org:** [vpeetla-ai](https://github.com/vpeetla-ai)  
**Portfolio hub:** [venkat-ai.com/work](https://venkat-ai.com/work)  
**Last updated:** Jul 2026

This is the **canonical execution tracker**. Mark phases complete here as work lands. Do not post on LinkedIn for a repo until it passes [LINKEDIN_READINESS_AUDIT.md](./LINKEDIN_READINESS_AUDIT.md) (≥14/16).

---

## North star

A visitor who lands on GitHub or a live demo should understand in **60 seconds**:

1. What problem this solves (for whom)
2. How you solve it (architecture, not feature soup)
3. What's real vs planned (honest status table)
4. How to run locally in &lt;5 minutes
5. Where it sits in the governed stack

**Success metric:** README ≥9/11 per [README_STANDARD.md](./README_STANDARD.md); live demo works; one canonical Mermaid diagram matches `docs/ARCHITECTURE.md`.

---

## Phase tracker

| Phase | Name | Status | Completed |
|-------|------|--------|-----------|
| **0** | Inventory & readiness audit | ✅ Done | Jul 2026 |
| **1** | Canonical diagram sync (Tier-1) | ✅ Done | Jul 2026 |
| **2** | README standardization (Tier-1) | ✅ Done | Jul 2026 |
| **3** | ADR & case study alignment | ⬜ Not started | — |
| **4** | Demo & first-run UX polish | ⬜ Not started | — |
| **5** | LinkedIn content (12-week launch) | ⬜ Not started | — |

---

## Phase 0 — Inventory & rubric ✅

**Deliverable:** [LINKEDIN_READINESS_AUDIT.md](./LINKEDIN_READINESS_AUDIT.md)

- [x] Score Tier-1 repos 0–2 on 8 criteria (max 16)
- [x] Identify gate failures (&lt;14/16)
- [x] Prioritize DomainForge + VoiceForge + Enterprise RAG first

---

## Phase 1 — Canonical diagram sync ✅

**Rule:** One source of truth per repo: `docs/diagrams/canonical-architecture.mmd` → embed in README §Architecture.

| Repo | Canonical `.mmd` | README synced | ARCHITECTURE.md linked |
|------|------------------|---------------|------------------------|
| DomainForge | ✅ | ✅ | ✅ |
| VoiceForge | ✅ | ✅ | ✅ |
| Enterprise RAG | ✅ | ✅ | ✅ (existing hub) |
| vLLM Lab | ✅ | ✅ | ✅ |
| VAP | ✅ | ✅ | ✅ |
| ACF | ✅ | ✅ | ✅ |
| AegisLoop | ✅ | ✅ | ✅ |
| LoopForge | ✅ | ✅ | ✅ |

**New ADRs (Phase 3):**
- [ADR-022](../adr/ADR-022-domainforge-vllm-multi-lora-serving.md) — target architecture for multi-LoRA serving (planned)
- [ADR-023](../adr/ADR-023-enterprise-rag-rerank-decline.md) — cross-encoder rerank + decline-to-answer

---

## Phase 2 — README standardization ✅

**Standard:** [README_STANDARD.md](./README_STANDARD.md) · Badges: [repo-tech-stacks.yaml](./repo-tech-stacks.yaml)

| Repo | README pass | Tech badges | Status table honest | Quick start |
|------|-------------|-------------|---------------------|-------------|
| DomainForge | ✅ | ✅ | ✅ | ✅ |
| VoiceForge | ✅ | ✅ | ✅ | ✅ |
| Enterprise RAG | ✅ (reranker row) | ✅ | ✅ | ✅ |
| vLLM Lab | ✅ (canonical link) | ✅ | ✅ | ✅ |
| REPO_INDEX | ✅ VoiceForge + agent-finops | — | — | — |
| Gap plan refresh | ✅ | — | — | — |

**Sync targets (Phase 3):**
- [x] `venkat-ai-portfolio/data/ecosystem.ts`
- [x] `vpeetla-ai/README.md` org profile
- [x] `CONTEXT.md` in ai-content-factory

---

## Phase 3 — ADR & case study alignment ✅

| Repo | ADR action | Case study |
|------|------------|------------|
| DomainForge | Link ADR-019/020; ADR-022 drafted | ✅ S0→S4 + bench table |
| Enterprise RAG | ✅ ADR-023 cross-encoder + decline | ✅ pipeline stages |
| VoiceForge | Link portfolio ADR-021 | ✅ Latency SLO table |
| vLLM Lab | ADR-022 target architecture | ✅ Train → serve economics |
| VAP / ACF / AegisLoop / LoopForge | Canonical diagrams + README links | — |

---

## Phase 4 — Demo & first-run UX ⬜

- [ ] Render cold-start notes in every Deploy section
- [ ] Verify Vercel aliases (see CONTEXT.md stale list)
- [ ] Empty/error states when API sleeping (DomainForge, VoiceForge)
- [ ] Social preview images (1200×630) per flagship

---

## Phase 5 — LinkedIn launch sequence ⬜

**Principles:** Who hurts → what breaks → what we built → architecture insight → honest boundary → CTA (demo → GitHub → case study).

| Week | Post | Repo | Gate (audit ≥14) |
|------|------|------|------------------|
| 0 | Anchor essay — governance stack | venkat-ai.com/work | — |
| 1 | Access-before-ranking RAG | Enterprise RAG | ✅ 15/16 |
| 2 | RAG for facts · PEFT for behavior | DomainForge | ✅ 15/16 |
| 3 | PagedAttention + multi-LoRA economics | vLLM Lab | ✅ 14/16 |
| 4 | Voice TTFT + latency budgets | VoiceForge | ✅ 15/16 |
| 5 | Gateway before side effects | AegisAI | ⬜ audit pending |
| 6 | Orchestration ≠ governance | VAP | ✅ 14/16 |
| 7 | AgentOps console | AegisLoop | ✅ 14/16 |
| 8 | HITL publish pipeline | ACF | ✅ 16/16 |
| 9 | Self-improvement harness | LoopForge | ✅ 14/16 |
| 10 | Governed overnight intel | Sentinel | ⬜ |
| 11 | Golden eval CI contracts | golden-eval-registry | ⬜ |
| 12 | 5 agent patterns carousel | pattern repos ×5 | ⬜ |

Post skeleton: see [LINKEDIN_POST_TEMPLATES.md](./LINKEDIN_POST_TEMPLATES.md) (Phase 5).

---

## Technical gaps (honest backlog)

| Gap | Severity | Phase | Status |
|-----|----------|-------|--------|
| Multi-LoRA serving demo | High | 3 + GPU | ADR-022 drafted; implementation ⬜ |
| GPU-trained Mistral artifacts published | High | User RunPod | ⬜ |
| enterprise_rag `vpeetla_observability` middleware | Medium | 4 | ⬜ |
| venkat-ai-portfolio ecosystem sync | Medium | 3 | ✅ |
| Pattern repo README batch (×5) | Medium | 4 | ⬜ |

---

## Definition of done (per repo, LinkedIn-ready)

- [ ] Audit score ≥14/16
- [ ] `pytest -q` passes; CI badge in README
- [ ] Live demo verified within 7 days
- [ ] `docs/diagrams/canonical-architecture.mmd` + README embed
- [ ] Honest status table — no aspirational ✅
- [ ] Case study in ai-architecture-portfolio
- [ ] Listed in REPO_INDEX + venkat-ai.com/work
- [ ] LinkedIn post drafted + architecture PNG

---

## Related docs

- [LINKEDIN_READINESS_AUDIT.md](./LINKEDIN_READINESS_AUDIT.md)
- [README_STANDARD.md](./README_STANDARD.md)
- [REPO_INDEX.md](./REPO_INDEX.md)
- [PORTFOLIO_2026_GAP_PLAN.md](./PORTFOLIO_2026_GAP_PLAN.md)
- [ADR-022: Multi-LoRA serving target](../adr/ADR-022-domainforge-vllm-multi-lora-serving.md)

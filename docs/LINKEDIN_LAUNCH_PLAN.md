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
| **3** | ADR & case study alignment | ✅ Done | Jul 2026 |
| **4** | Demo & first-run UX polish | ✅ Done (2 dashboard blockers) | Jul 2026 |
| **5** | LinkedIn content (12-week launch) | ✅ Drafts ready | Jul 2026 |

> **Open blockers before live posting:** disable Vercel Deployment Protection on DomainForge + VoiceForge; expose a public ACF landing route (or post the `/sign-in` link); export OG cards per [SOCIAL_PREVIEW_COPY.md](./SOCIAL_PREVIEW_COPY.md).

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

## Phase 4 — Demo & first-run UX ✅ (2 dashboard blockers)

- [x] Render cold-start "first-run note" in Deploy sections — Enterprise RAG, vLLM Lab, DomainForge, VoiceForge
- [x] Verify Vercel aliases — 7/10 public 200; findings logged in [CONTEXT.md](../../ai-content-factory/CONTEXT.md) demo-access table
- [x] Cold-start-aware empty/error states — DomainForge + VoiceForge UIs now show a "waking API (~30s)" hint on network/timeout failures
- [x] Social preview spec — [SOCIAL_PREVIEW_SPEC.md](./SOCIAL_PREVIEW_SPEC.md)
- [x] Designer copy handoff — [SOCIAL_PREVIEW_COPY.md](./SOCIAL_PREVIEW_COPY.md) (PNG export ⬜)

**Demo-access verification (Jul 7 2026):**

| Demo | Status | Blocker |
|------|--------|---------|
| Enterprise RAG, vLLM Lab, VAP, AegisLoop, LoopForge, Sentinel, AegisAI | ✅ public 200 | — |
| DomainForge | ❌ 302 → Vercel SSO | **Disable Vercel Deployment Protection** (backend healthy) |
| VoiceForge | ❌ 302 → Vercel SSO | **Disable Vercel Deployment Protection** (backend healthy) |
| ACF | ⚠️ `/` 404, `/sign-in` 200 | Public landing route / link `/sign-in` (Clerk gates root; backend healthy) |

> These 3 are Vercel/Clerk **dashboard** settings, not repo code. Must clear before Weeks 2 (DomainForge), 4 (VoiceForge), 8 (ACF) posts.

**Remaining Phase 4 asset work:** export 1200×630 OG cards per [SOCIAL_PREVIEW_COPY.md](./SOCIAL_PREVIEW_COPY.md) and wire `openGraph.images`.

---

## Phase 5 — LinkedIn launch sequence ✅ drafts ready

**Principles:** Who hurts → what breaks → what we built → architecture insight → honest boundary → CTA (demo → GitHub → case study).

**All 13 posts (Week 0 + Weeks 1–12) are drafted in [LINKEDIN_POST_TEMPLATES.md](./LINKEDIN_POST_TEMPLATES.md).** Posting cadence is manual (one/week); check the demo gate + Phase 4 access blocker before each.

| Week | Post | Repo | Draft | Gate (audit ≥14) | Pre-post check |
|------|------|------|-------|------------------|----------------|
| 0 | Anchor essay — governance stack | venkat-ai.com/work | ✅ | — | — |
| 1 | Access-before-ranking RAG | Enterprise RAG | ✅ | ✅ 15/16 | demo 200 ✅ |
| 2 | RAG for facts · PEFT for behavior | DomainForge | ✅ | ✅ 15/16 | ⚠️ disable Vercel SSO first |
| 3 | PagedAttention + multi-LoRA economics | vLLM Lab | ✅ | ✅ 14/16 | demo 200 ✅ |
| 4 | Voice TTFT + latency budgets | VoiceForge | ✅ | ✅ 15/16 | ⚠️ disable Vercel SSO first |
| 5 | Gateway before side effects | AegisAI | ✅ | ✅ 16/16 | demo 200 ✅ |
| 6 | Orchestration ≠ governance | VAP | ✅ | ✅ 14/16 | demo 200 ✅ |
| 7 | AgentOps console | AegisLoop | ✅ | ✅ 14/16 | demo 200 ✅ |
| 8 | HITL publish pipeline | ACF | ✅ | ✅ 16/16 | ⚠️ link `/sign-in` (root 404) |
| 9 | Self-improvement harness | LoopForge | ✅ | ✅ 14/16 | demo 200 ✅ |
| 10 | Governed overnight intel | Sentinel | ✅ | ✅ 16/16 | demo 200 ✅ |
| 11 | Golden eval CI contracts | golden-eval-registry | ✅ | n/a (no demo) | repo link |
| 12 | 5 agent patterns carousel | pattern repos ×5 | ✅ | demos ✅ 200 | series OG card; per-repo gate ⬜ |

Post skeleton + all drafts: [LINKEDIN_POST_TEMPLATES.md](./LINKEDIN_POST_TEMPLATES.md).

**Before posting each week:** (1) demo returns 200 for a signed-out visitor, (2) OG card exists per [SOCIAL_PREVIEW_SPEC.md](./SOCIAL_PREVIEW_SPEC.md), (3) attach architecture PNG from `docs/diagrams/canonical-architecture.mmd`.

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

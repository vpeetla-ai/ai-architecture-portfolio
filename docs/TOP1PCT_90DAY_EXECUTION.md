# Top-1% Principal — 90-Day Execution Plan (Accepted)

**Status:** ACTIVE  
**Decided:** 2026-07-18  
**Supersedes sequencing of:** [`TOP1PCT_90DAY_BACKLOG.md`](./TOP1PCT_90DAY_BACKLOG.md) (treat Jul 9 “all DONE” as Phase −1 remediation, not operating proof)  
**Companion canvas:** Cursor `vpeetla-ai-top1pct-90day.canvas.tsx`

---

## Accepted decisions

| ID | Decision | Choice |
|----|----------|--------|
| **D1** | Public spine | **5 only:** `ai-architecture-portfolio` · `venkat-ai-platform` · `aegisai-enterprise-agent-platform` · `enterprise_rag_platform` · `ai-content-factory` |
| **D2** | Always-on | **Pay for spine APIs** (VAP + AegisAI + Enterprise RAG) — Content Factory already product-shaped; FinOps/LoopForge stay free-tier proof |
| **D3** | Strict vs demo | **Dual URLs / dual mode** with Strict as the recommended review path; demo defaults must banner stub/fail-open |
| **D4** | Distribution | **Mix:** LinkedIn + Substack weekly from ADRs (not product launches) |
| **D5** | Conversion goal | **Staff+ / Principal offers** — hire + technical-review + playbook/arena are the conversion funnel |

**Proof services (linked, not hero):** `agent-finops`, `golden-eval-registry`  
**Career layer (keep):** `ai-architect-interview-playbook`, `ai-architect-practice-arena`  
**Labs / curriculum (demote):** DomainForge, VoiceForge, vLLM Lab, OmniForge, Sentinel, AegisLoop, gateway/cache repos, 5 pattern stubs → Teaching drawer only  

**Hard freeze (90 days):** no new product repos; no OmniForge/Sentinel hero expansion.

---

## North star

A cold Principal interviewer completes a **15-minute** review on [venkat-ai.com/technical-review](https://venkat-ai.com/technical-review): runs the spine path, sees a real audit/eval/cost artifact, and trusts the stack — without reading 26 READMEs.

---

## Program stages

| Stage | Window | Theme | Exit criteria |
|-------|--------|-------|---------------|
| **S0** | Day 0 | Lock plan + freeze | This doc merged; D1–D5 recorded; issues opened |
| **S1** | Days 1–7 | Narrative concentration | Hero/hire/work/profile show spine first; patterns demoted |
| **S2** | Days 8–14 | Default honesty | Strict/demo dual-path labeled on spine demos + gateway/cache |
| **S3** | Days 15–30 | Always-on + interview pack | Paid spine APIs OR explicit cold-start SLA page; hire funnel wired |
| **S4** | Days 31–60 | Golden path proof | One stranger-replayable E2E (ask→RAG→govern→publish/meter) + durable artifacts |
| **S5** | Days 61–90 | Signal + conversion | 8–12 posts; 1 flagship essay; mock loops; freeze retrospective |

Legend for stage rows below: `TODO` · `IN_PROGRESS` · `DONE` · `BLOCKED`

---

## S0 — Program control

| ID | Action | Repo | Done when | Status |
|----|--------|------|-----------|--------|
| S0.1 | Merge this execution plan + README link | `ai-architecture-portfolio` | PR opened | `DONE` (PR pending merge) |
| S0.2 | Open tracking issues for S1–S5 | `ai-architecture-portfolio` | Issues linked from this doc | `DONE` |
| S0.3 | Update PRIOR backlog header → Phase −1 complete | `ai-architecture-portfolio` | Note on TOP1PCT_90DAY_BACKLOG | `DONE` (PR pending merge) |

---

## S1 — Narrative concentration (Week 1)

| ID | Action | Repo | Done when | Status |
|----|--------|------|-----------|--------|
| S1.1 | Export `heroSpineProjectIds` = `aegisai`, `vap`, `enterprise-rag`, `content-factory` | `venkat-ai-portfolio` | Used by teaser/work/hire | `DONE` (PR pending merge) |
| S1.2 | Homepage teaser + work panel + hire cards consume spine IDs | `venkat-ai-portfolio` | UI shows spine-first | `DONE` (PR pending merge) |
| S1.3 | Metrics copy: “5-spine review path” vs catalog totals | `venkat-ai-portfolio` | No “17 products” as hero claim | `DONE` (PR pending merge) |
| S1.4 | Technical-review steps = spine path + ADR hub | `venkat-ai-portfolio` | Steps match D1 | `DONE` (PR pending merge) |
| S1.5 | Profile README Top projects = spine first; rest under Labs/Teaching | `vpeetla-ai` | PR opened | `DONE` (PR pending merge) |
| S1.6 | Pattern series clearly “Teaching stubs” only on profile | `vpeetla-ai` | Already mostly; verify | `DONE` (PR pending merge) |

**Live product IDs (UI):** portfolio is narrative (not in `liveProjects`); spine demos = four IDs above.

---

## S2 — Default honesty (Week 2)

| ID | Action | Repo | Done when | Status |
|----|--------|------|-----------|--------|
| S2.1 | Banner on spine demos: Demo vs Strict review mode | spine demos | Visible without scrolling | `DONE` |
| S2.2 | Gateway/cache README + portfolio: stub default called out | `aegis-llm-gateway`, portfolio | No silent “production” | `DONE` |
| S2.3 | Enterprise RAG: verified Principal path documented as Strict | `enterprise_rag_platform` | technical-review links it | `DONE` |

---

## S3 — Always-on + interview pack (Weeks 3–4)

| ID | Action | Repo | Done when | Status |
|----|--------|------|-----------|--------|
| S3.1 | Upgrade Render plans for VAP + AegisAI + ERAG APIs | Render | `/health` warm within 3s × 24h sample | `DONE` (Blueprint PRs; dashboard apply + warm sample) |
| S3.2 | Public spine health page on portfolio | `venkat-ai-portfolio` | `/proof` or `/technical-review` live checks | `DONE` (PR pending merge) |
| S3.3 | Hire funnel: playbook + arena + technical-review CTA | portfolio + playbook | One path from `/hire` | `DONE` (PR pending merge) |
| S3.4 | Delete/disable duplicate Vercel playbook project | Vercel | Only canonical host | `DONE` (links fixed; dashboard delete remaining) |

---

## S4 — Golden path proof (Days 31–60)

| ID | Action | Repo | Done when | Status |
|----|--------|------|-----------|--------|
| S4.1 | Scripted E2E: VAP ask → ERAG retrieve → AegisAI gate → ACF publish/meter | spine | `docs/GOLDEN_PATH.md` + runnable script | `TODO` |
| S4.2 | Durable public artifact (trace/eval/cost) per run | FinOps + Langfuse/eval | Link from technical-review | `TODO` |
| S4.3 | Weekly adversarial golden CI green | `golden-eval-registry` | Badge on portfolio | `TODO` |
| S4.4 | Case study update with numbers from real runs | `ai-architecture-portfolio` | New or revised case study | `TODO` |

---

## S5 — Signal + conversion (Days 61–90)

| ID | Action | Channel | Done when | Status |
|----|--------|---------|-----------|--------|
| S5.1 | 8–12 posts from ADRs (not “launched demo”) | LinkedIn/Substack | Calendar complete | `TODO` |
| S5.2 | Flagship essay: OS → governance with live proof links | Substack | Published | `TODO` |
| S5.3 | 3 recorded mock loops (playbook → arena) | local/private | Notes for interviews | `TODO` |
| S5.4 | Outreach / applications using hire pack | external | Log of intros | `TODO` |
| S5.5 | Day-90 retrospective: keep freeze or adjust | this doc | Written retro | `TODO` |

---

## Anti-goals

- New platform / pattern / tutorial repos  
- Hero expansion of OmniForge, Sentinel, VoiceForge, DomainForge  
- Claiming production for stub-default paths  
- Org-wide Kubernetes migration  
- Marking stages DONE without PR or measurable exit criteria  

---

## Tracking issues

| Stage | Issue | Status |
|-------|-------|--------|
| S0 | [PR #1](https://github.com/vpeetla-ai/ai-architecture-portfolio/pull/1) | Merged |
| S1 | [#2](https://github.com/vpeetla-ai/ai-architecture-portfolio/issues/2) · portfolio #3 · profile #1 | Merged |
| S2 | [#3](https://github.com/vpeetla-ai/ai-architecture-portfolio/issues/3) | Merged |
| S3 | [#4](https://github.com/vpeetla-ai/ai-architecture-portfolio/issues/4) · [S3 runbook](./S3_ALWAYS_ON_RUNBOOK.md) | PRs open |
| S4 | [#5](https://github.com/vpeetla-ai/ai-architecture-portfolio/issues/5) | Open |
| S5 | [#6](https://github.com/vpeetla-ai/ai-architecture-portfolio/issues/6) | Open |

## Progress log

| Date | ID | Note |
|------|-----|------|
| 2026-07-18 | — | Decisions D1–D5 accepted; execution plan created |
| 2026-07-18 | S0–S1 | PRs opened: architecture #1, portfolio #3, profile #1; issues #2–#6 |
| 2026-07-18 | S0–S1 | Three narrative PRs merged |
| 2026-07-18 | S2 | Demo/Strict banners + stub honesty PRs opened across spine + plane |
| 2026-07-18 | S2 | All S2 PRs merged |
| 2026-07-18 | S3 | Always-on Blueprint + spine-health + hire funnel PRs; see S3_ALWAYS_ON_RUNBOOK.md |

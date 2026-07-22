# Top-1% gap plan — post S0–S5 assessment

**Assessed:** 2026-07-18  
**Companion canvas:** Cursor `top1pct-gap-assessment.canvas.tsx`  
**Parent plan:** [`TOP1PCT_90DAY_EXECUTION.md`](./TOP1PCT_90DAY_EXECUTION.md)  
**90/100 score program:** [`TOP1PCT_90SCORE_60DAY.md`](./TOP1PCT_90SCORE_60DAY.md)

---

## Verdict

| Lens | Score | Reading |
|------|-------|---------|
| **Thesis / narrative** | ~7/10 | 5-spine story, honesty banners, hire funnel, golden-path docs — Principal-shaped |
| **Operating proof** | ~4/10 | Cold starts still kill first contact; ask→answer not stranger-complete; signal unpublished |
| **Overall** | **Not yet Top-1%** | Scaffolding for Top-1% is merged; **hostile 15-minute panel** can still bounce |

Phase −1 remediation + S0–S5 paper work ≠ Top-1% offers. Remaining work is **operating proof + distribution**, not new products.

---

## What already matches the Top-1% profile

| Decision / north-star | Evidence |
|----------------------|----------|
| **D1** five-spine | Portfolio hero/hire/work/technical-review; org profile spine-first |
| **D3** Demo vs Strict | Sticky banners on AegisAI / VAP / ERAG / ACF; Strict docs linked |
| Inspectable review path | `/technical-review` · `/spine-health` · `/hire` all 200 |
| Playbook hygiene | Canonical host only; `*-9xs` project deleted (404) |
| Golden path scaffolding | `GOLDEN_PATH.md` + public artifact (`stranger_replayable_ok=true`) |
| Eval badge | GER CI on architecture README |
| Freeze | Retro: keep no-new-product-repos |

---

## Misses (prioritized)

### P0 — Panel credibility (do first)

| ID | Miss | Evidence (this check) | Exit criteria | Owner |
|----|------|------------------------|---------------|--------|
| **G1** | Spine APIs still cold-start | First hit: vap **timeout 25s**, aegisai **22.6s**, erag **21.3s**; warm later &lt;1s | Idle ≥15 min → 3 consecutive `/health` **&lt;3s** for vap + aegisai + erag | Render dashboard (apply **Starter** if Blueprint not synced) |
| **G2** | Golden path ask→answer incomplete | `full_ask_answer_ok=false` (401 without keys) | Private run with `VAP_API_KEY` + `RAG_API_KEY`; update [golden-path case study](../case-studies/golden-path-spine-e2e.md) numbers; do **not** commit secrets | Local env + `scripts/run_golden_path.py` |

### P1 — Signal + conversion (D4 / D5)

| ID | Miss | Evidence | Exit criteria | Owner |
|----|------|----------|---------------|--------|
| **G3** | Flagship essay not on Substack | Publish checklist open | Live Substack URL; Medium canonical; LinkedIn teaser | You |
| **G4** | ADR posts not posted | [S5 calendar](./S5_ADR_POST_CALENDAR.md) all `TODO` | ≥8 posts from calendar with technical-review CTA | You |
| **G5** | Mock loops not executed | [MOCK_LOOP_LOG](./interview/MOCK_LOOP_LOG.md) sessions `TODO` | 3 dated sessions with scores + remediations | You |
| **G6** | Outreach empty | [OUTREACH_LOG](./outreach/OUTREACH_LOG.md) template only | ≥10 logged intros/applications | You |

### P2 — Harden / hygiene

| ID | Miss | Evidence | Exit criteria | Owner |
|----|------|----------|---------------|--------|
| **G7** | No live Strict ERAG path for panels | Live default Demo principal; Strict is docs-only | Dual URL **or** documented one-command Strict review env | ERAG + portfolio |
| **G8** | ACF publish not in golden path | `/health` only; Clerk for live publish | Public demo publish **or** permanent honest boundary in GOLDEN_PATH | ACF |
| **G9** | Stale tracking issues | #2 still OPEN; #6 open after S5 pack merge | Close #2; retarget #6 to “operating S5” checkboxes | GitHub |

---

## 30-day operating plan

### Week 1 — P0

1. Render → confirm **Starter** (or equivalent always-on) for `vap-api`, `enterprise-rag-api`, `aegisai-api`
2. Idle ≥15 minutes → sample `/health` ×3; paste results into this doc’s Progress log
3. Export keys locally → `VAP_API_KEY=… RAG_API_KEY=… python3 scripts/run_golden_path.py`
4. If `full_ask_answer_ok=true`, refresh case study + commit artifact only (no secrets)

### Week 2–3 — P1 signal

1. Publish Substack flagship (ACF essay + proof links)
2. Post calendar #1–4 (LinkedIn); mark calendar `POSTED` + URL
3. Run mock loops 1–3; fill log

### Week 4 — P1 conversion + P2

1. ≥10 outreach rows using hire pack
2. Posts #5–8
3. Optional: Strict ERAG dual path (G7); decide G8 forever-honest vs ship demo publish
4. Close/retarget issues (G9)
5. **Keep freeze** — no new product repos

---

## Anti-goals (unchanged)

- New platform / pattern / tutorial repos  
- OmniForge / Sentinel hero expansion  
- Claiming production for stub-default or cold free-tier paths  
- Marking G1–G6 `DONE` without the exit criteria above  

---

## Progress log

| Date | ID | Note |
|------|-----|------|
| 2026-07-18 | — | Gap assessment after S0–S5; cold-start probe recorded |
| 2026-07-18 | G1 | **Blocked on Render MCP:** `list_workspaces` returns `unauthorized` after `mcp_auth` (cannot `select_workspace` / `update_web_service`). Blueprint already `plan: starter` in VAP + ERAG repos — live instance type still needs dashboard apply or working MCP. |
| 2026-07-18 | G1 | Warm probe (post-traffic): vap ~0.12–0.16s · aegisai ~0.6–0.7s · erag first **12.4s** then ~0.11s · acf first two **30s timeout** then 0.44s. Portfolio `/api/spine-health` warmOk 3/3 after wake. **Idle ≥15m cold retest still required.** |
| | G1 | _pending: dashboard Starter apply + idle cold probe_ |
| | G2 | _pending keyed golden run (`VAP_API_KEY` + `RAG_API_KEY` unset in agent env)_ |

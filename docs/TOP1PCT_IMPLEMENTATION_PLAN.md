# Top-1% Principal — Detailed Implementation Plan

Companion to [`TOP1PCT_90DAY_BACKLOG.md`](./TOP1PCT_90DAY_BACKLOG.md).  
**Execution rule:** implement → verify (tests/CI) → update docs → record tradeoffs/ADRs → mark backlog `DONE`.

---

## Assumptions

1. Free-tier PaaS remains the default host; “always-on” is a **single** exception, not org-wide paid infra.
2. Fail-open gateway defaults stay for local demos; production honesty requires an explicit strict profile.
3. GitHub Issues may lag if `gh` auth is broken — backlog markdown is the source of truth until issues exist.
4. No new product repos in this program.

## Success criteria (program)

| Metric | Baseline (Jul 9 2026) | Target (Day 90) |
|--------|----------------------|-----------------|
| ADR count consistency | 20 marketed / 23 on disk | Single number everywhere |
| False CI/SLO claims | ≥1 (VAP) | 0 |
| Aspirational HLDs in flagship READMEs | ACF 9-layer | 0 unlabeled |
| Verified Principal path | ❌ | ✅ Enterprise RAG strict mode |
| Fail-closed profile | ❌ | ✅ ADR + ≥3 consumers |
| LoopForge sandbox | ❌ | ✅ |
| Always-on proof | 0 | ≥1 |

---

## P1.1 — Sync ADR / metrics

### Plan
1. Set `documentedAdrs: 23` in `venkat-ai-portfolio/data/metrics.ts`.
2. Append ADR-021, ADR-022, ADR-023 rows to `ai-architecture-portfolio/README.md` ADR table.
3. Update `vpeetla-ai/README.md` hero from “20 ADRs” → “23 ADRs”.
4. Soft-fix stale LinkedIn copy in portfolio docs if it hardcodes 18/20.
5. Run `node scripts/validate-portfolio.mjs`.

### Tradeoffs
- **ADR-022 is Proposed**, not Accepted — still counts as a documented decision; do not inflate “Accepted” counts.
- Marketing “20+” is weaker than an exact synced number.

### Done when
Validator passes; grep for `20 ADRs` in profile/hero paths is clean (or intentional historical).

---

## P1.2 — Kill aspirational ACF HLD

### Plan
1. Replace README “Nine-layer HLD” mermaid with the **canonical implemented** diagram (from `docs/diagrams/canonical-architecture.mmd`).
2. Optional: move old HLD to `docs/diagrams/target-architecture-aspirational.mmd` labeled **Not shipped**.
3. Keep status table as source of truth for 🟡/⬜ rows.

### Tradeoffs
- Loses “enterprise scale” visual theater; gains Principal credibility.
- Reviewers who want scale story should read `docs/SCALE.md`, not a fake topology.

### Done when
README Architecture section matches deployed Render/Vercel/LangGraph path.

---

## P1.3 — Fix VAP golden-eval CI claim

### Plan (honesty-first, then wire)
1. **Immediate:** Rewrite `docs/SLO.md` so Eval regression is **Planned / not gated in this repo** until a workflow exists.
2. **Follow-up (P2.4):** Add `vap_*` suite or reuse an existing harness suite + CI job.

### Tradeoffs
- Honesty now vs shipping a thin fake gate. Prefer honesty; fake gates destroy trust.

### Done when
SLO does not claim a CI gate that `.github/workflows` does not run.

---

## P1.4 — `PRODUCTION_STRICT` convention

### Plan
1. Write **ADR-024** in `ai-architecture-portfolio`: org-wide env `PRODUCTION_STRICT=true` means gateway/FinOps/publish **fail-closed** when dependency missing.
2. Document in `CONTEXT.md` (ACF + skills).
3. Wire first consumer (prefer ACF gateway or Enterprise RAG Principal).

### Decision sketch
| Mode | Missing gateway URL | Missing FinOps | Spoofable Principal |
|------|---------------------|----------------|---------------------|
| Demo (default) | Allow / local estimate | Local estimate | Allowed (documented) |
| `PRODUCTION_STRICT` | Deny | Deny / halt | Reject |

### Done when
ADR merged; one consumer tested in both modes.

---

## P1.5 — Verified Principal on Enterprise RAG

### Plan
1. ADR in-repo or portfolio: JWT/OIDC → Principal claims.
2. Strict mode: ignore body `clearance`/`groups`; derive from token.
3. Tests: spoof attempt fails under strict; demo mode unchanged.
4. Update risk-register row 15.

### Tradeoffs
- Full IdP (Auth0/Clerk) vs HS256 demo JWT for portfolio. Prefer **verifiable JWT with documented issuer** over fake OIDC UI.
- Breaking change for demo clients that POST clearance — version header or strict-only.

### Done when
`pytest` covers spoof rejection; README status table updated.

---

## P2–P3 (summary)

| ID | Implementation sketch |
|----|----------------------|
| P2.1 | Docker-in-Docker or Fly/Render one-shot container for `run_pytest`; never host cwd |
| P2.2 | Map NIST AI RMF Govern/Map/Measure/Manage → AegisAI/RAG/evals |
| P2.3 | New suite kind `adversarial_v1` with Principal spoof + injection fixtures |
| P2.4 | Minimal VAP suite: critic/notify policy invariants |
| P3.1 | Prefer Sentinel S3/R2 archive **or** scheduled golden runner on always-on tiny VM |
| P3.2 | One LoRA adapter served via vLLM OpenAI-compatible route; DomainForge promote points at it |
| P3.3 | Explicit N/35 in README + UI |
| P3.4 | Tenant isolation ADR; optional header `X-Tenant-Id` enforcement demo |
| P3.5 | Validator: count `adr/ADR-*.md` via git submodule or pinned expected count |

---

## Execution order (this session)

1. P0.1 backlog + this plan ✅  
2. P1.1 metrics sync  
3. P1.2 ACF diagram  
4. P1.3 VAP SLO honesty  
5. P1.4 ADR-024 + first wiring  
6. P1.5 Enterprise RAG Principal (start)

Each item ends with: code/docs commit-ready, verification command, backlog status flip.

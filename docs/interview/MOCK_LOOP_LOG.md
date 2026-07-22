# S5.3 — Mock interview loops (playbook → arena)

**Goal:** Three private practice loops before Staff+/Principal panels.  
**Tools:** [Interview playbook](https://ai-architect-interview-playbook.vercel.app) · [Practice Arena](https://ai-architect-practice-arena.vercel.app) · [Technical review](https://venkat-ai.com/technical-review)

## Session template

| Field | Notes |
|-------|-------|
| Date | |
| Duration | target 45–60 min |
| Question IDs | from playbook |
| Mode | timed speak-aloud / Arena dual-judge |
| Score / self-rubric | Mid / Senior / Staff+ / Principal bar |
| Gaps | |
| Remediations | ADR or golden-path proof to re-read |

---

## Loop 1 — Governed RAG + auth

| Field | Plan |
|-------|------|
| Date | **2026-07-29** (scheduled) |
| Focus | Access-before-ranking · decline-to-answer · Strict vs Demo |
| Playbook entries | `ai-system-design/02-rag-platform-at-scale` · cloud auth/spoof variants |
| Arena | Same rubrics; dual-judge |
| Live proof after | ERAG demo + Strict pack · ADR-002 / ADR-023 · spine health |
| Status | `SCHEDULED` |
| Self-run protocol | 45 min timed · record 3 gaps · remediation links required before Loop 2 |
| Notes | Prefer Strict JWT recipe from STRICT_PANEL_PACK |

## Loop 2 — Orchestration vs governance

| Field | Plan |
|-------|------|
| Date | **2026-08-05** (scheduled) |
| Focus | ADR-001 split · gateway HITL · side-effect classes |
| Playbook entries | agent governance / multi-agent OS design |
| Arena | Staff+ craft: trade-off table under timebox |
| Live proof after | AegisAI control plane · golden path `approval_required` |
| Status | `SCHEDULED` |
| Self-run protocol | Include one “what fails open?” grill question |
| Notes | |

## Loop 3 — Full spine panel simulation

| Field | Plan |
|-------|------|
| Date | **2026-08-12** (scheduled) |
| Focus | 15-min technical review path as interviewer would walk it |
| Playbook entries | mix design + behavioral conflict/mentoring |
| Arena | One timed mock end-to-end |
| Live proof after | `/technical-review` → `/spine-health` → GOLDEN_PATH.md · NIST + FinOps one-pagers |
| Status | `SCHEDULED` |
| Self-run protocol | Cold open venkat-ai.com only — no pre-warming cheats |
| Notes | Score against Principal bar; update 90score tracker |

---

After each loop: update Status to `DONE`, add score, and one remediation link. P5 exit needs all three `DONE` with scores.

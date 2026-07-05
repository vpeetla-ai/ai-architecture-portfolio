# ADR-018: AI Architect Practice Arena as a Standalone Repo

## Status

Accepted — 2026-07-05

## Context

`ai-architect-interview-playbook` (ADR-017, now 35 entries) each encode a real, specific
Staff+/Principal grading rubric — but the repo is content you read, not something you practice
against. Asked what a genuinely valuable next phase would look like, the recommendation was an
LLM-as-judge mock-interview practice layer: submit a real written answer, get graded by an LLM
judge against the playbook's own rubric text, with structured feedback on what's missing.

Two decisions shaped the resulting architecture significantly:

1. **Both OpenAI and Anthropic grade every attempt**, not one provider — their agreement (or
   disagreement) on an answer's level is itself a real, useful signal.
2. **Bring-your-own-key (BYOK)**, since this is meant to be a genuinely public tool. This means
   the org bears zero direct API cost regardless of usage, at the cost of a real responsibility:
   a user's key must never be stored, logged, or sent to our own backend.

## Decision

Built [ai-architect-practice-arena](https://github.com/vpeetla-ai/ai-architect-practice-arena)
as its own standalone public repo — the same reasoning already established for `agent-finops`
(ADR-011) and `ai-architect-interview-playbook` (ADR-017): a genuinely different audience/purpose
(an interactive practice tool with its own deploy and test surface, not more static content)
deserves to be found and linked on its own.

The playbook is included as a **pinned git submodule**, read only at build time by
`scripts/build_rubrics.py`, which parses each entry's real "What's expected at each level"
section into a structured `rubrics.json` — the judge's grading prompt uses this text verbatim,
so the tool can never drift from what the playbook itself defines as a good answer. Judging
happens entirely client-side in the browser (`frontend/lib/judge/`), mirroring the real provider-
seam shape already established by `aegisai-enterprise-agent-platform`'s `LLMGateway`. The backend
serves question/rubric content only — no API key of any kind is ever received by it.

**A real finding from live browser testing**: the design initially assumed both providers could
be called directly from the browser. A real end-to-end test found this true for Anthropic
(its documented direct-browser-access header works as described) but false for OpenAI, whose
API blocks direct browser calls with a CORS error rather than a readable response — fixed with
a minimal, stateless same-origin proxy that forwards the caller-supplied key per-request and
persists nothing. See the repo's own ADR-0001 for the full account, including two other things
only real execution caught (a Node version requirement, a React version requirement) that code
review alone would not have surfaced.

## Consequences

### Positive
- Zero org-side API cost at any usage scale, removing the budget-cap/rate-limiting machinery a
  shared-key public tool would otherwise require.
- The rubric is guaranteed to match the playbook's own text (parsed, not re-authored), and judge
  disagreement is a real, surfaced signal rather than a silently averaged score.
- Org repo count grows to 20 public repos (21 total including the private portfolio site).

### Negative
- 9 of the playbook's 35 questions (`behavioral/` 5, `scalability-governance-tradeoffs/` 4) are
  still not covered as of Phase 2 — genuinely STAR- and framework-shaped, deferred to a
  not-yet-built Phase 3 rather than force-fit into the current five sections.
- Calibration (real API keys against live providers — see the repo's own ADR-0001, 102/104 on
  Phase 2's first full run, two real failures fixed) only covers one weak and one strong reference
  answer per question, not the full range of real, messier answers actual users will submit.

## Update — 2026-07-05: deployed live

Frontend live at [ai-architect-practice-arena.vercel.app](https://ai-architect-practice-arena.vercel.app),
backend at [practice-arena-api.onrender.com](https://practice-arena-api.onrender.com), both free
tier, matching this org's reference-stack convention (ADR-005). Deploying for real (not just
planning to) surfaced two things: Vercel's default Deployment Protection blocks all public access
on a new project by default — exactly wrong for a public tool, disabled and verified reachable
unauthenticated; and `vercel link` without an explicit project flag silently creates a duplicate
project rather than linking the intended one, caught and cleaned up after a project rename.
Verified live end-to-end afterward, including the OpenAI proxy serverless function responding
correctly in Vercel's real production runtime. Full account in the repo's own ADR-0001.

## Update — 2026-07-05: Phase 2, sectioned mock interview + full system-design coverage

Extended from a flat single-textarea answer to the playbook's own five sections (Requirements,
Core Entities, API/Interface, High-Level Design, Deep Dives), with a High-Level Design input that
accepts a live-rendered Mermaid diagram (primary) plus an optional image URL (Excalidraw/
screenshot, sent as a real vision input when supported, with a text-only fallback). Coverage
extended from 10 to all 26 questions across the three folders sharing this shape; `behavioral/`
(5) and `scalability-governance-tradeoffs/` (4) remain deferred to a not-yet-built Phase 3 given
their genuinely different STAR/framework answer shape.

Calibration against live OpenAI + Anthropic across all 26 questions (104 cases): 102/104 passed
on the first run. Both real failures were diagnosed, not dismissed — one a genuine content gap in
a calibration answer (missing the rubric's specific Principal-level differentiator), one a
transient network error — and both are fixed in the repo. Per this org's disclose-real-numbers
discipline: a full live rerun confirming 104/104 has not happened as of this writing, since BYOK
means this org never holds the API keys needed to run it; the image-vision-input path is likewise
implemented with a graceful fallback but not yet confirmed live against either provider. Full
account, including the two fixes, in the repo's own ADR-0001.

## References
- [ai-architect-practice-arena](https://github.com/vpeetla-ai/ai-architect-practice-arena)
- [Practice Arena's own ADR-0001](https://github.com/vpeetla-ai/ai-architect-practice-arena/blob/master/docs/adr/0001-byok-judge-architecture.md) — the full architecture account
- [ADR-017: Interview playbook as a standalone repo](./ADR-017-interview-playbook-standalone-repo.md) — the rubric source of truth this repo builds on
- [ADR-011: AgentFinOps as a standalone service](./ADR-011-agent-finops-standalone-service.md) — the precedent for this decision

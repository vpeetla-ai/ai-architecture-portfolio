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
- Calibration (real API keys against live providers — see the repo's own ADR-0001) only covers
  one weak and one strong reference answer per question, not the full range of real, messier
  answers actual users will submit.

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

## Update — 2026-07-06: Phase 3, behavioral (STAR) + trade-offs (reasoning framework), full 35/35 coverage

Extended coverage from 26 to all 35 playbook questions by adding two more rubric formats.
`behavioral/` (5 STAR write-ups of Venkat's own real cases) and `scalability-governance-
tradeoffs/` (4 reasoning-framework questions) both lacked the level-criteria section every
system-design question has — a real gap found by reading all 9 source files before writing any
code, fixed by authoring that content in the playbook repo first (same commit also added a new
generic, reusable interview-question section to the 5 behavioral entries, since a STAR write-up
of someone else's real case can't be re-answered literally — a practicing user answers the
generic version with their own experience instead).

`Rubric`/`Answer` became discriminated unions across all three formats rather than three separate
code paths; the judge adapters needed no changes to their model-calling logic. The practice
page's sidebar and right rail stay fully shared — only the center-column form is format-aware.

Calibration against live OpenAI + Anthropic across all 35 questions (140 cases): 139/140 passed,
confirmed identically across two independent full runs. All 18 new Phase 3 cases passed cleanly
both times, including "strong" answers deliberately written with different concrete scenarios
than each entry's own illustrative example — a real test that the judge grades the underlying
competency, not a paraphrase match. The one failure (an already-shipped Phase 2 question) was a
real gap in how the Anthropic adapter handled a technically-invalid JSON response (Anthropic has
no strict JSON-mode like OpenAI's), fixed with a one-time retry — not yet reconfirmed with a
third live run as of this writing. Full account, including the exact failure and fix, in the
repo's own ADR-0001.

## References
- [ai-architect-practice-arena](https://github.com/vpeetla-ai/ai-architect-practice-arena)
- [Practice Arena's own ADR-0001](https://github.com/vpeetla-ai/ai-architect-practice-arena/blob/master/docs/adr/0001-byok-judge-architecture.md) — the full architecture account
- [ADR-017: Interview playbook as a standalone repo](./ADR-017-interview-playbook-standalone-repo.md) — the rubric source of truth this repo builds on
- [ADR-011: AgentFinOps as a standalone service](./ADR-011-agent-finops-standalone-service.md) — the precedent for this decision

# ADR-018: AI Architect Practice Arena as a Standalone Repo

## Status

Accepted — 2026-07-05

## In one breath (panel)

I'd grade practice answers with dual-provider LLM judges against the playbook's own rubric text — BYOK, client-side keys, never stored on our backend.

## Context

The playbook (ADR-017, 35 entries) encodes Staff+/Principal rubrics, but reading isn't practice. The useful next layer: submit a real written answer, get graded against the playbook's rubric text, with structured feedback on what's missing.

Two decisions shaped the architecture:

1. **Both OpenAI and Anthropic grade every attempt** — agreement or disagreement on level is the signal; averaging it away is demo theater
2. **Bring-your-own-key (BYOK)** — public tool, zero org API cost; the scar is responsibility: a user's key must never be stored, logged, or sent to our backend

What I refused: a shared org key with budget caps pretending to be "free forever," and a re-authored rubric that drifts from the playbook.

## Decision

Built [ai-architect-practice-arena](https://github.com/vpeetla-ai/ai-architect-practice-arena) as its own public repo — same standalone-repo reasoning as FinOps (ADR-011) and the playbook (ADR-017): interactive tool with its own deploy surface, not more markdown in the portfolio.

- Playbook is a **pinned git submodule**; `scripts/build_rubrics.py` parses each entry's "What's expected at each level" into `rubrics.json` at build time — judge prompts use that text verbatim
- Judging runs client-side (`frontend/lib/judge/`), mirroring AegisAI's `LLMGateway` provider-seam shape
- Backend serves question/rubric content only — no API key ever reaches it

**Live-browser scar:** design assumed both providers work from the browser. Anthropic's documented direct-browser header works; OpenAI blocks with CORS. Fixed with a minimal same-origin proxy that forwards the caller-supplied key per request and persists nothing. Node + React version requirements only showed up in real execution — see the repo's ADR-0001.

## Consequences

**Positive**

- Zero org-side API cost at any usage scale
- Rubric can't drift from the playbook (parsed, not rewritten); judge disagreement is surfaced, not averaged away
- Org grew to 20 public repos (21 including private portfolio site) as of this ADR

**Negative**

- Calibration (live keys vs providers — repo ADR-0001) covers one weak and one strong reference answer per question, not the full mess of real user answers

## Update — 2026-07-05: deployed live

Frontend: [ai-architect-practice-arena.vercel.app](https://ai-architect-practice-arena.vercel.app). Backend: [practice-arena-api.onrender.com](https://practice-arena-api.onrender.com). Free tier, matching ADR-005. Deploy scars: Vercel Deployment Protection blocked public access by default (disabled and verified unauthenticated); `vercel link` without an explicit project flag silently created a duplicate project (caught after rename). OpenAI proxy verified in Vercel's production runtime. Full account in the repo's ADR-0001.

## Update — 2026-07-05: Phase 2, sectioned mock interview + full system-design coverage

Flat textarea → playbook's five sections (Requirements, Core Entities, API/Interface, High-Level Design, Deep Dives). High-Level Design accepts live Mermaid plus optional image URL (vision when supported, text fallback). Coverage 10 → all 26 questions in the three folders with this shape; `behavioral/` (5) and `scalability-governance-tradeoffs/` (4) deferred to Phase 3 (different STAR/framework shape).

Live calibration OpenAI + Anthropic across 26 questions (104 cases): **102/104** first run. Both failures diagnosed — one content gap in a calibration answer, one transient network — fixed in-repo. Honest: a full live rerun confirming 104/104 has not happened (BYOK means this org doesn't hold the keys); image-vision path implemented with fallback but not confirmed live. Details in repo ADR-0001.

## Update — 2026-07-06: Phase 3, behavioral + trade-offs, full 35/35 coverage

Extended to all 35 playbook questions with two more rubric formats. `behavioral/` and `scalability-governance-tradeoffs/` lacked level-criteria — found by reading all 9 source files before writing code; authored in the playbook first (behavioral also got a generic reusable question, since you can't re-answer someone else's STAR literally).

`Rubric`/`Answer` became discriminated unions; judge model-calling logic unchanged. Calibration across 35 questions (140 cases): **139/140**, identical across two independent full runs. All 18 new Phase 3 cases passed, including "strong" answers with different concrete scenarios than the illustrative examples — grades competency, not paraphrase match. One failure (shipped Phase 2 question): Anthropic adapter mishandled technically-invalid JSON (no OpenAI-style strict JSON mode); fixed with one-time retry — not yet reconfirmed on a third live run. Full account in repo ADR-0001.

## References

- [ai-architect-practice-arena](https://github.com/vpeetla-ai/ai-architect-practice-arena)
- [Practice Arena ADR-0001](https://github.com/vpeetla-ai/ai-architect-practice-arena/blob/master/docs/adr/0001-byok-judge-architecture.md)
- [ADR-017: Interview playbook](./ADR-017-interview-playbook-standalone-repo.md)
- [ADR-011: AgentFinOps standalone](./ADR-011-agent-finops-standalone-service.md)

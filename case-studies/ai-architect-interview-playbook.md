# AI Architect Interview Playbook — Grounded Interview Prep

**Domain:** Interview readiness · System design · STAR-method behavioral prep  
**Live (Practice Arena):** [ai-architect-practice-arena.vercel.app](https://ai-architect-practice-arena.vercel.app)  
**Source:** [github.com/vpeetla-ai/ai-architect-interview-playbook](https://github.com/vpeetla-ai/ai-architect-interview-playbook)

## Problem

Most AI-architect prep is a thought experiment — “design a RAG system” with no shipped scar behind it. Roadmap step 14 says master the interview; this org already had the raw material (ADRs, outcomes, real bugs). The scar I’d refuse: inventing crisp metrics for STAR stories that the case studies never disclosed.

## What we decided

1. **Standalone repo** — interview prep and ADR history are different audiences ([ADR-017](../adr/ADR-017-interview-playbook-standalone-repo.md)).
2. **Grounded-or-labeled** — every entry links a real ADR/shipped decision or admits it’s general framework.
3. **Link-check CI, not a fake test suite** — markdown fails when cross-links rot.
4. **Practice Arena as the exercise surface** — LLM-as-judge against the playbook’s own rubrics ([ADR-018](../adr/ADR-018-practice-arena-standalone-repo.md)).
5. **Reuse only public outcome language** — e.g. “multi-million-dollar annualized” from Gulf Payments/EDI, no fabricated precision.

## Architecture

```text
Question, as it might actually be asked
  → real system (a repo, an ADR, a shipped decision)
  → architecture diagram
  → trade-offs actually considered
  → why the real decision was made
  → what would be different if a constraint changed
```

## Live proof

- Playbook: [ai-architect-interview-playbook](https://github.com/vpeetla-ai/ai-architect-interview-playbook)
- Practice Arena: [ai-architect-practice-arena.vercel.app](https://ai-architect-practice-arena.vercel.app)
- Linked from portfolio `/roadmap` and `/hire`

## Limitations / what we'd do differently

- Content repo: correctness is link integrity + honesty labels, not pytest green.
- Dual-judge calibration is a Practice Arena claim — keep scores tied to the published rubrics, don’t round up for LinkedIn.
- Next: keep FDE pack and system-design entries in sync when spine ADRs change.

## Related

- [ADR-017](../adr/ADR-017-interview-playbook-standalone-repo.md) · [ADR-018](../adr/ADR-018-practice-arena-standalone-repo.md)
- [FDE field method](./fde-field-method.md)

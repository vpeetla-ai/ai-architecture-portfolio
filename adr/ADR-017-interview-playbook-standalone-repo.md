# ADR-017: Interview Playbook as a Standalone Repo (Phase E)

## Status

Accepted — 2026-07-05

## In one breath (panel)

I'd ship interview prep as its own public repo — grounded in real ADRs, not buried inside a decision-history repo nobody opens for prep.

## Context

Phase E targeted "Master AI Architect Interviews." The easy move was a `docs/interview-playbook/` folder next to the ADRs. That buries content meant for candidates and hiring panels inside a repo whose job is architecture-decision history. Same trap we already refused for [agent-finops](https://github.com/vpeetla-ai/agent-finops) (ADR-011): different audience → different front door.

What I refused: generic interview fluff with no scar, and overclaiming "sourced" company questions that don't exist in public.

## Decision

Built [ai-architect-interview-playbook](https://github.com/vpeetla-ai/ai-architect-interview-playbook) as a standalone public repo.

35 entries across five categories (`ai-system-design/`, `general-system-design/`, `cloud-architecture/`, `behavioral/`, `scalability-governance-tradeoffs/`). Each entry either cross-links a real ADR / shipped decision or says plainly that it doesn't. The "test suite" is `scripts/check_links.sh` + CI — for a content repo, "does every cross-link resolve" is the verification that matters.

## Consequences

**Positive**

- Roadmap step answered with grounded content, not recycled prep blogs
- Discoverable from the portfolio `/roadmap` page (step 14) and `/hire` credentials — not an orphaned repo
- Org grew to 19 public repos (20 including the private portfolio site) as of this ADR

**Negative**

- Link checkers can't catch a stale claim that still points at a real file. Mitigated by writing entries in the same sessions the underlying ADRs were verified

## Update — 2026-07-05: `system-design/` rewritten in hello-interview style

The first 4 `system-design/` entries had real ADR links but read like generic interview Qs. Rewrote to 8 entries following [hellointerview.com](https://www.hellointerview.com)'s structure (requirements, entities, API, architecture, deep dives with trade-off tables, Mid→Principal levels) and grounded research into what's publicly reported at OpenAI, Anthropic, Meta, Google/DeepMind, Microsoft, and Apple for AI-infra roles. Honest result: company-attributed system-design questions for these exact roles are scarce. Each entry's "Where this actually gets asked" says so instead of inventing a sourced question.

## Update — 2026-07-05: `cloud-architecture/` rewritten in hello-interview style

Same pass on cloud: 3 shallow entries → 6 depth entries (GPU capacity, multi-region train vs serve, DR for model serving, distributed-training networks, security/compliance for AI, containers + cost). Strongest sourcing: Meta RoCE / topology blogs; Anthropic RSP; Meta Llama weights leak; Apple Private Cloud Compute. Weakest: DR for model serving — and the research pass rejected a fabricated-looking, company-attributed cost figure from SEO content rather than silently omitting it. Real Phase C AWS/GCP Terraform scars (placeholder API key, Cloud Run `PORT`, ECR teardown) stayed in the entries.

## Update — 2026-07-05: eagle-eye gap analysis adds 5 entries

Reviewed the repo against a real Staff+/Principal loop, not against what was already written. Gaps: foundation-model strategy (build vs fine-tune vs vendor API), multi-tenant AI platforms, agent sandboxing / code-exec security, on-device / edge inference, and a behavioral entry for leading a 0→1 build under ambiguity (everything else was "found a bug in an existing system"). Added `system-design/09-11`, `scalability-governance-tradeoffs/04`, and `behavioral/05` (grounded in [ai-content-factory](https://github.com/vpeetla-ai/ai-content-factory) and its ADR-008 scope calls). Best-sourced topic: Anthropic's published Claude Code sandboxing (gVisor). Rejected two more fabricated-looking claims on the research pass.

## Update — 2026-07-05: split into ai-system-design/ and general-system-design/

All 11 existing entries were AI/ML-specific; the classic non-AI round (rate limiters, chat, news feeds, schedulers) wasn't there. Renamed `system-design/` → `ai-system-design/` and added `general-system-design/` (7 entries). Caught two wrong company attributions on verification (Google Docs → Netflix; distributed cache → Amazon) and corrected them. Snowflake ID generators are a Twitter system — the entry says so. Strongest grounding: Meta NSDI Memcache paper, Multifeed blogs, WhatsApp scaling talks, Google SRE Book cron. Repo hit 33 entries across five categories.

## Update — 2026-07-05: end-to-end Staff+/Principal quality pass

Harsh review of all 33 entries. One genuinely weak (`ai-system-design/06` multimodal search — vague Principal bullet); nine adequate-but-not-sharp (Principal bullets restated Staff+). Reworked all ten with distinct Principal mechanisms (e.g. hybrid logical clocks, membership-inference for residency, CRDT tombstone growth). Added two missing topics: `ai-system-design/12` (training-data provenance / IP risk — NYT v. OpenAI, Getty v. Stability, plus enterprise_rag lineage scar) and `ai-system-design/13` (durable long-running agents — callback to Content Factory `interrupt_before` + Redis checkpointer). Repo now 35 entries across five categories.

## References

- [ai-architect-interview-playbook](https://github.com/vpeetla-ai/ai-architect-interview-playbook)
- [ADR-011: AgentFinOps as a standalone service](./ADR-011-agent-finops-standalone-service.md) (precedent)

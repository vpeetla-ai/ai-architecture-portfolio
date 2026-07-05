# ADR-017: Interview Playbook as a Standalone Repo (Phase E)

## Status

Accepted — 2026-07-05

## Context

Phase E of the top-1% AI Architect program targeted step 14 of the 15-step roadmap ("Master AI
Architect Interviews"). The content could have lived inside this repo — a `docs/interview-
playbook/` folder alongside the ADRs it's grounded in.

## Decision

Built [ai-architect-interview-playbook](https://github.com/vpeetla-ai/ai-architect-interview-playbook)
as its own standalone public repo instead — the same reasoning already established for
[agent-finops](https://github.com/vpeetla-ai/agent-finops) (ADR-011): a genuinely different
audience and purpose deserves to be found and linked on its own, not buried inside a repo whose
primary purpose (architecture-decision history) most visitors aren't there for.

21 entries across four categories (`system-design/`, `cloud-architecture/`, `behavioral/`,
`scalability-governance-tradeoffs/`), each cross-linking to the real ADR or shipped decision it's
grounded in, or explicitly marked as general framework content when it isn't tied to one specific
decision. A `scripts/check_links.sh` + CI workflow is the repo's entire "test suite" — appropriate
for a content-only repo where the actual verification that matters is "does every cross-link
resolve," not "does code compile."

## Consequences

### Positive
- Directly answers a roadmap step with real, grounded content rather than generic interview
  prep — every entry either cites a real ADR/shipped decision or says explicitly that it
  doesn't.
- Linked from the portfolio site's new `/roadmap` page (step 14) and from `/hire`'s credential
  list (Phase F) — discoverable from two places, not an orphaned repo.
- Org repo count grows to 19 public repos (20 total including the private portfolio site).

### Negative
- A content-only repo has no automated way to verify factual accuracy of its cross-links beyond
  "the link resolves" — a stale claim that still points at a real file would pass the link
  checker. Mitigated by writing this content in the same session the underlying ADRs were
  written or verified, minimizing drift risk at time of writing.

## Update — 2026-07-05: `system-design/` rewritten in hello-interview style

The initial 4 `system-design/` entries were shallow — real ADR cross-links, but shaped like
generic interview questions rather than the depth an actual Staff+/Principal AI-infra interview
demands. Rewritten (8 entries, up from 4) to follow
[hellointerview.com](https://www.hellointerview.com)'s actual answer structure (confirmed via
direct research, not assumed) — requirements, core entities, API design, high-level
architecture, deep dives with real trade-off tables and concrete numbers, and an explicit
Mid/Senior/Staff+/Principal level breakdown — and grounded in real research into what's publicly
reported at OpenAI, Anthropic, Meta, Google/DeepMind, Microsoft, and Apple for AI
infrastructure roles specifically. That research came back honest, not flattering:
company-attributed system design questions for these exact roles are genuinely scarce in public
sources. Each entry's "Where this actually gets asked" section discloses that plainly rather
than overclaiming a sourced question that doesn't exist.

## Update — 2026-07-05: `cloud-architecture/` rewritten in hello-interview style

Same treatment applied to the second content category: the initial 3 `cloud-architecture/`
entries (PaaS vs. self-hosted, VPC design, container orchestration) were replaced with 6
hello-interview-depth entries — GPU capacity planning & procurement, multi-region strategy for
training vs. serving, disaster recovery for model serving, network architecture for distributed
training, security & compliance architecture for AI systems, and container orchestration + cost
optimization at scale. Research into these six companies' real cloud/infra-architecture
interview practices came back with the strongest sourcing yet found in this repo for two topics
(Meta's engineering blog on RoCE networking and topology-aware scheduling; Anthropic's published
Responsible Scaling Policy security standards, the Meta Llama weights leak, and Apple's Private
Cloud Compute blog for security/compliance) and the weakest for one (disaster recovery for model
serving) — where the research pass also caught and explicitly rejected a fabricated-looking,
company-attributed cost figure circulating on SEO content rather than silently omitting it. The
real Phase C AWS/GCP Terraform work (VPC/security-group design, the placeholder-API-key bug and
fix, the Cloud Run `PORT` bug, ECR teardown fix) was preserved and folded into the new entries
rather than discarded.

## References
- [ai-architect-interview-playbook](https://github.com/vpeetla-ai/ai-architect-interview-playbook)
- [ADR-011: AgentFinOps as a standalone service](./ADR-011-agent-finops-standalone-service.md) (the precedent for this decision)

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

35 entries across five categories (`ai-system-design/`, `general-system-design/`,
`cloud-architecture/`, `behavioral/`, `scalability-governance-tradeoffs/`), each cross-linking to
the real ADR or shipped decision it's
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

## Update — 2026-07-05: eagle-eye gap analysis adds 5 entries

Asked to review the repo against what a real Staff+/Principal AI Architect loop actually covers,
not just what was already written. Identified five genuine gaps: foundation model strategy
(build from scratch vs. fine-tune an open-weight model vs. call a vendor API — arguably the
single most quintessential AI-architect strategic question, and it wasn't covered anywhere),
multi-tenant AI platform architecture, AI agent sandboxing/code-execution security, on-device/
edge AI inference architecture, and a behavioral gap (every existing behavioral entry was "found
and fixed a gap in an existing system" — none covered leading a 0-to-1 build under genuine
ambiguity). Added `system-design/09-11`, `scalability-governance-tradeoffs/04`, and
`behavioral/05` (grounded in the real [ai-content-factory](https://github.com/vpeetla-ai/ai-content-factory)
build and its ADR-008 scope decisions). Research for the AI agent sandboxing topic came back the
best-sourced of any entry in the repo — Anthropic's own published Claude Code sandboxing
architecture (gVisor, open-sourced sandbox runtime) — and on-device AI confirmed Apple is the
clear architectural outlier among the six companies, via its own Private Cloud Compute
publications. The research pass also caught and rejected two more fabricated-looking claims (an
unsourced Vertex AI incident anecdote, an unattributed "Anthropic interview stage"
characterization), continuing this repo's sourcing discipline.

## Update — 2026-07-05: split into ai-system-design/ and general-system-design/

Asked whether the repo's AI/ML-specific system-design content was being mistaken for the *only*
system-design round these companies run — it wasn't a fair label. All 11 existing entries were
genuinely AI/ML-specific; the classic, non-AI "regular round" (rate limiters, chat systems, news
feeds, job schedulers) these same six companies also run wasn't represented at all. Renamed
`system-design/` to `ai-system-design/` (a clean git rename, all cross-links updated and
verified) and added a new `general-system-design/` folder with 7 entries. This research pass
found the opposite sourcing shape from every prior pass: the classic round is heavily documented
publicly, but two specific attributions traced, on verification, to the wrong company entirely —
a "Design Google Docs" citation that was actually a Netflix question, and a "Design a distributed
cache" citation that was actually Amazon's — both corrected rather than repeated. The distributed
unique-ID-generator entry required a direct correction to a common assumption: Snowflake is a
Twitter system, not one of this repo's six researched companies, and the entry says so plainly.
The strongest grounding found anywhere in this repo to date: Meta's own NSDI paper "Scaling
Memcache at Facebook," its Multifeed/News-Feed-ranking engineering blogs, WhatsApp's own scaling
talks, and Google's SRE Book chapter on its real distributed cron service. Repo now totals 33
entries across five categories.

## Update — 2026-07-05: end-to-end Staff+/Principal quality pass

Asked to do a final, harsh review of every entry against a genuine Staff+/Principal bar — not a
rubber-stamp check — and to add anything a real interview loop would cover that was still
missing. A dedicated review pass read all 33 entries and flagged one as genuinely weak
(`ai-system-design/06`, multimodal search/recommendation — no real grounding and a Principal
bullet that was vague meta-commentary rather than a harder technical claim) and nine more as
adequate-but-not-sharp (their Principal-level bullets read as generic restatements of the Staff+
bullet rather than a substantively different, harder mechanism). Reworked all ten: `06` now has
concrete ANN-index recall/latency/memory numbers and a named position-bias-correction mechanism;
the others each gained one genuinely distinct Principal-level insight (e.g., hybrid logical
clocks as the structural fix for clock skew in `general-system-design/05`, membership-inference
testing as the real mechanism for whether a trained model inherits training-data residency
constraints in `cloud-architecture/02`, CRDT tombstone-growth as the real operational cost CRDTs
don't advertise in `general-system-design/06`).

The gap analysis from that same review pass identified two genuinely missing, non-redundant
topics and both were added: `ai-system-design/12` (training-data provenance and IP risk —
grounded in real, ongoing litigation: NYT v. OpenAI/Microsoft, Getty v. Stability AI — with a
real org callback to enterprise_rag_platform's own lineage-fix bug, generalized from retrieval
to training-data ingestion) and `ai-system-design/13` (durable long-running agent execution —
the architecture problem of an agent surviving its own restart mid-task without losing progress
or repeating side effects, grounded in the real durable-execution pattern and a real callback to
ai-content-factory's shipped `interrupt_before` + Redis-checkpointer design). Repo now totals 35
entries across five categories.

## References
- [ai-architect-interview-playbook](https://github.com/vpeetla-ai/ai-architect-interview-playbook)
- [ADR-011: AgentFinOps as a standalone service](./ADR-011-agent-finops-standalone-service.md) (the precedent for this decision)

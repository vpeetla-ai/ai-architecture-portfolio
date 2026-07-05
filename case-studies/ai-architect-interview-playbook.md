# AI Architect Interview Playbook — Grounded Interview Prep

**Domain:** Interview readiness · System design · STAR-method behavioral prep
**Source:** [github.com/vpeetla-ai/ai-architect-interview-playbook](https://github.com/vpeetla-ai/ai-architect-interview-playbook)

## Problem

Most AI-architect interview prep is generic — "here's how you'd design a RAG system" as a
thought experiment, disconnected from anything actually shipped. Step 14 of the well-known
15-step "AI Architect roadmap" is "Master AI Architect Interviews," and this org already had
the raw material (real ADRs, real outcomes, real bugs found in production) to answer that step
with proof instead of a generic study guide.

## Architecture

```text
Question, as it might actually be asked
  → real system (a repo, an ADR, a shipped decision)
  → architecture diagram
  → trade-offs actually considered
  → why the real decision was made
  → what would be different if a constraint changed
```

## Key decisions

- Standalone repo, not a folder in this one ([ADR-017](../adr/ADR-017-interview-playbook-standalone-repo.md))
  — same reasoning as [agent-finops](./agent-finops.md): a different audience deserves to be
  found on its own.
- Every entry either cross-links to a real, existing ADR/shipped decision, or is explicitly
  labeled as general framework content — no entry pretends to be grounded when it isn't.
- No backend, no test suite in the traditional sense — a content repo's real verification is
  "does every cross-link resolve," enforced by a small link-checker CI workflow, not code
  compiling.

## Trade-offs

| Choice | Rationale |
|--------|-----------|
| Standalone repo vs. a folder in `ai-architecture-portfolio` ([ADR-017](../adr/ADR-017-interview-playbook-standalone-repo.md)) | Discoverable on its own — interview prep and architecture-decision history are different audiences even when they share source material |
| Link-check CI instead of a test suite | The repo is markdown, not code — the actual failure mode to prevent is a broken cross-link, not a bug |
| Grounded-or-labeled, no invented specifics | Behavioral/STAR entries reuse only what the underlying case studies already disclose (e.g., "multi-million-dollar annualized" from Gulf Payments/EDI) rather than fabricating precise figures for narrative effect |

## Impact

- Directly answers roadmap step 14 with real, checkable proof instead of generic prep.
- Linked from the portfolio site's new `/roadmap` page and from `/hire`'s credential list —
  discoverable from two places in the live site, not an orphaned repo.
- 19th public repo in the org.

## Related

- [ADR-017: Interview playbook as a standalone repo](../adr/ADR-017-interview-playbook-standalone-repo.md)
- [ai-architect-interview-playbook](https://github.com/vpeetla-ai/ai-architect-interview-playbook)

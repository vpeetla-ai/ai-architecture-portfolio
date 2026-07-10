# README standard — vpeetla-ai org

Every product repo README should follow this order so recruiters and engineers get **product context first**, then **how to run code**.

## Required sections (top → bottom)

| # | Section | Purpose |
|---|---------|---------|
| 1 | **Title + tech stack badges** | H1 name, then `<!-- vpeetla-tech-stack -->` row (Python, FastAPI, LangGraph, …) — see [repo-tech-stacks.yaml](repo-tech-stacks.yaml) |
| 2 | **Status badges** | Live demo, CI, license, portfolio link |
| 3 | **One-liner** | What it is in one sentence |
| 4 | **What this is** | Product idea, who it serves |
| 5 | **How we solve it** | Problem → approach (not feature list only) |
| 6 | **Architecture** | Mermaid or link to `docs/ARCHITECTURE.md` + canonical `.mmd` if present |
| 7 | **Case study & tradeoffs** | Links to portfolio case study, `docs/PRODUCT.md`, ADRs |
| 8 | **Interview map** | Honest crosswalk to [playbook](https://github.com/vpeetla-ai/ai-architect-interview-playbook) entries (system design / coding / cloud / trade-offs / behavioral) — see [REPO_INTERVIEW_MAP.md](REPO_INTERVIEW_MAP.md) |
| 9 | **Status** | Honest table — ✅ 🟡 ⬜ |
| 10 | **Quick start** | `pip install`, `pytest`, local run |
| 11 | **Deploy / env** | Link `docs/DEPLOY.md` or `docs/LIVE_DEMO.md` |
| 12 | **Stack fit / related** | Which layer in governed stack |

## Tech stack badges

Canonical stacks: [repo-tech-stacks.yaml](repo-tech-stacks.yaml). Regenerate all README rows:

```bash
node scripts/inject-readme-tech-badges.mjs --write
```

## Case study index

See [REPO_INDEX.md](REPO_INDEX.md) for repo → case study mapping.
See [REPO_INTERVIEW_MAP.md](REPO_INTERVIEW_MAP.md) for repo → Staff+ playbook entry mapping.

## Pattern repos (no dedicated case study)

Use: [venkat-ai.com/work](https://venkat-ai.com/work) · [Production Agent Patterns](https://github.com/vpeetla-ai/ai-content-factory/blob/main/docs/agent-patterns/ROADMAP.md) · `docs/ARCHITECTURE.md`

## Canonical diagram

Prefer one file: `docs/diagrams/canonical-architecture.mmd` — embed same mermaid in README.

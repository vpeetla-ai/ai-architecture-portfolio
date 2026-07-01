# README standard — vpeetla-ai org

Every product repo README should follow this order so recruiters and engineers get **product context first**, then **how to run code**.

## Required sections (top → bottom)

| # | Section | Purpose |
|---|---------|---------|
| 1 | **Title + badges** | Name, live demo, CI, license |
| 2 | **One-liner** | What it is in one sentence |
| 3 | **What this is** | Product idea, who it serves |
| 4 | **How we solve it** | Problem → approach (not feature list only) |
| 5 | **Architecture** | Mermaid or link to `docs/ARCHITECTURE.md` + canonical `.mmd` if present |
| 6 | **Case study & tradeoffs** | Links to portfolio case study, `docs/PRODUCT.md`, ADRs |
| 7 | **Status** | Honest table — ✅ 🟡 ⬜ |
| 8 | **Quick start** | `pip install`, `pytest`, local run |
| 9 | **Deploy / env** | Link `docs/DEPLOY.md` or `docs/LIVE_DEMO.md` |
| 10 | **Stack fit / related** | Which layer in governed stack |

## Case study index

See [REPO_INDEX.md](REPO_INDEX.md) for repo → case study mapping.

## Pattern repos (no dedicated case study)

Use: [venkat-ai.com/work](https://venkat-ai.com/work) · [Production Agent Patterns](https://github.com/vpeetla-ai/ai-content-factory/blob/main/docs/agent-patterns/ROADMAP.md) · `docs/ARCHITECTURE.md`

## Canonical diagram

Prefer one file: `docs/diagrams/canonical-architecture.mmd` — embed same mermaid in README.

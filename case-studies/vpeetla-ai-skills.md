# vpeetla-ai-skills — Org-Wide Agent Engineering Discipline

**Domain:** Agent skills · Cursor + Codex · protocol stack 2026  
**Source:** [vpeetla-ai-skills](https://github.com/vpeetla-ai/vpeetla-ai-skills)

## Problem

Fifteen repos share LangGraph, gateway, RAG, loops, and deploy patterns — and every engineer re-discovers the conventions per clone. The scar is a PR that “works” while violating the honest status table, skipping the gateway on a side effect, or teaching an agent the wrong stack layer. Skills should make that knowledge portable.

## What we decided

1. **One skills repo, many install targets** — DRY `SKILL.md` vs per-repo copies.
2. **Installer for Cursor + Codex** — `scripts/install.sh` → `.cursor/skills/` + `AGENTS.md` + `CONTEXT.md`.
3. **Honest status table as a first-class skill** — portfolio credibility is engineering practice, not marketing.
4. **Protocol stack alignment (ADR-007)** — Skills → MCP → Gateway → Observability.
5. **CI smoke install** — prove the installer into a temp project.

## Architecture

```text
skills/*/SKILL.md  →  scripts/install.sh  →  .cursor/skills/ + AGENTS.md + CONTEXT.md
```

| Component | Role |
|-----------|------|
| **21 skills** | Governed stack, MCP, observability, loop engineering, git-commit-author, … |
| `install.sh` | `--cursor`, `--codex`, `--global`, `--project` |
| `CONTEXT.md` | Repo map for Codex root context |
| CI smoke test | Validates install into temp project |

| Category | Examples |
|----------|----------|
| Stack | `governed-ai-stack`, `agent-protocol-stack-2026` |
| Implementation | `langgraph-orchestration`, `aegis-gateway`, `mcp-tool-exposure` |
| Quality | `honest-status-table`, `production-observability`, `tdd-agent-loops` |
| Role | `enterprise-ai-architect`, `git-commit-author` |

## Live proof

- Repo: [vpeetla-ai-skills](https://github.com/vpeetla-ai/vpeetla-ai-skills)
- Install docs: [INSTALL.md](https://github.com/vpeetla-ai/vpeetla-ai-skills/blob/main/docs/INSTALL.md)
- Installed across org repos that carry `.cursor/skills/` and `AGENTS.md`

## Limitations / what we'd do differently

- Manual sync when ADRs change — no semver package manager yet; drift is the failure mode.
- Skills don’t replace reading the target repo’s `ARCHITECTURE.md` when you’re stuck on a layer.
- Next: lighter ADR→skill changelog so installers aren’t the only sync signal.

## Related

- [ADR-007 Agent Protocol Stack](../adr/ADR-007-2026-agent-protocol-stack.md)
- [ORG_IMPROVEMENT_PLAN_2026](../docs/ORG_IMPROVEMENT_PLAN_2026.md)
- Inspiration: [mattpocock/skills](https://github.com/mattpocock/skills)

# vpeetla-ai-skills — Org-Wide Agent Engineering Discipline

**Domain:** Agent skills · Cursor + Codex · protocol stack 2026  
**Source:** [vpeetla-ai-skills](https://github.com/vpeetla-ai/vpeetla-ai-skills)

## Problem

Fifteen portfolio repos share patterns (LangGraph, gateway, RAG, loops, deploy) but engineers re-discover conventions per repo. **Agent Skills** (SKILL.md) plus a single installer should make org knowledge portable across Cursor and Codex.

## Architecture

```text
skills/*/SKILL.md  →  scripts/install.sh  →  .cursor/skills/ + AGENTS.md + CONTEXT.md
```

| Component | Role |
|-----------|------|
| **19 skills** | Governed stack, MCP, observability, loop engineering, enterprise architect, … |
| `install.sh` | `--cursor`, `--codex`, `--global`, `--project` |
| `CONTEXT.md` | Repo map for Codex root context |
| CI smoke test | Validates install into temp project |

## Key decisions

- **One repo, many targets** — DRY skills vs per-repo copies
- **Honest status table skill** — portfolio credibility as first-class engineering practice
- **Protocol stack skill (ADR-007)** — Skills → MCP → Gateway → Observability alignment

## Skill categories

| Category | Examples |
|----------|----------|
| Stack | `governed-ai-stack`, `agent-protocol-stack-2026` |
| Implementation | `langgraph-orchestration`, `aegis-gateway`, `mcp-tool-exposure` |
| Quality | `honest-status-table`, `production-observability`, `tdd-agent-loops` |
| Role | `enterprise-ai-architect` |

## Trade-offs

| Choice | Why | Cost |
|--------|-----|------|
| SKILL.md format | Cursor + emerging Codex standard | Manual sync when ADRs change |
| Install script vs package manager | Zero npm/pip dep for consumers | No semver enforcement yet |

## Impact

- Installed across **14 org repos** — consistent agent behavior in PRs and demos
- Enables Phase 2 scorecard: MCP docs, observability, honest tables by reference
- Teaching artifact for **agentic engineering** (Karpathy-style loops + enterprise governance)

## Related

- [ADR-007 Agent Protocol Stack](../adr/ADR-007-2026-agent-protocol-stack.md)
- [ORG_IMPROVEMENT_PLAN_2026](../docs/ORG_IMPROVEMENT_PLAN_2026.md)
- [mattpocock/skills](https://github.com/mattpocock/skills) inspiration · [INSTALL.md](https://github.com/vpeetla-ai/vpeetla-ai-skills/blob/main/docs/INSTALL.md)

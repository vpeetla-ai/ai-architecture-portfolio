# ADR-007: 2026 Agent Protocol Stack — MCP, Skills, Gateway, Observability

## Status

Accepted — 2026-06-29

## Context

Production agent systems in 2026 standardize on:

- **MCP** for agent-to-tool and agent-to-context connectivity
- **Agent Skills** (`SKILL.md`) for engineering discipline across Cursor, Codex, Claude Code
- **Gateway + HITL** for side-effect governance (not prompt-only guardrails)
- **OpenTelemetry / Langfuse** for non-deterministic trace replay
- **A2A** (emerging) for inter-agent coordination at scale

The vpeetla-ai org already implements orchestration (VAP), governance (AegisAI), and skills (`vpeetla-ai-skills`). Gaps: inconsistent MCP exposure, LoopForge git side effects without gateway, portfolio metric drift.

## Decision

Adopt a **four-layer protocol stack** across all platform repos:

```text
1. Skills layer    → vpeetla-ai-skills (how we build)
2. MCP layer       → tool servers where agents act on files/APIs
3. Gateway layer   → AegisAI before irreversible side effects
4. Observability   → Langfuse/OTel + trace-linked evals on every production API path
```

**Trace-linked evaluation** links three levels on one `trace_id`:

| Level | Question | Example |
|-------|----------|---------|
| **system** | Did the workflow complete? | `pipeline.execute`, `sentinel_brief.run` |
| **trace** | Which path did the agent take? | `gateway.authorize_email`, `eval.brief_gate` |
| **node** | Was each step correct? | `research`, `llm.research` |

Canonical package: `packages/vpeetla_observability/` · [TRACE_LINKED_OBSERVABILITY.md](../docs/TRACE_LINKED_OBSERVABILITY.md)

**A2A** remains documented as the target for VAP specialist agents; in-process LangGraph delegation is acceptable for reference implementations.

## Consequences

### Positive
- Aligns portfolio with [2026 production patterns](https://internative.net/insights/blog/agentic-ai-architecture-2026)
- Skills repo becomes first-class org capability (not just dev convenience)
- Honest status tables prevent recruiter/engineer trust erosion

### Negative
- More documentation burden per repo
- Gateway wrapping adds latency on git push / publish paths

### Follow-ups
- ADR-009 (proposed): LoopForge gateway on PR workflow
- ADR-010 (proposed): MCP tool registry in VAP

## Links

- [ORG_IMPROVEMENT_PLAN_2026.md](../docs/ORG_IMPROVEMENT_PLAN_2026.md)
- [vpeetla-ai-skills](https://github.com/vpeetla-ai/vpeetla-ai-skills)
- [niteagent protocol stack](https://niteagent.com/blog/2026-06-07-agent-protocol-stack-mcp-a2a-production/)

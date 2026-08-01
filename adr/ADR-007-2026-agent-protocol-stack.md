# ADR-007: 2026 Agent Protocol Stack — MCP, Skills, Gateway, Observability

## Status

Accepted — 2026-06-29

## In one breath (panel)

I'd standardize the org on four layers — skills, MCP, gateway, observability — and refuse prompt-only guardrails or "we have A2A somewhere" without a real discover-then-call loop.

## Context

Production agent systems in 2026 converge on a few boring truths:

- **MCP** for agent-to-tool and agent-to-context connectivity
- **Agent Skills** (`SKILL.md`) for how we build across Cursor, Codex, Claude Code
- **Gateway + HITL** for side-effect governance (not prompt-only guardrails)
- **OpenTelemetry / Langfuse** for non-deterministic trace replay
- **A2A** (emerging) for inter-agent coordination at scale

We already had orchestration (VAP), governance (AegisAI), and skills (`vpeetla-ai-skills`). The scars were inconsistent MCP exposure, LoopForge git side effects without a gateway, and portfolio metric drift that made recruiters trust us less. I refused papering that over with brochure language.

## Decision

Adopt a **four-layer protocol stack** across platform repos:

```text
1. Skills layer    → vpeetla-ai-skills (how we build)
2. MCP layer       → tool servers where agents act on files/APIs
3. Gateway layer   → AegisAI before irreversible side effects
4. Observability   → Langfuse/OTel + trace-linked evals on every production API path
```

**Trace-linked evaluation** ties three levels on one `trace_id`:

| Level | Question | Example |
|-------|----------|---------|
| **system** | Did the workflow complete? | `pipeline.execute`, `sentinel_brief.run` |
| **trace** | Which path did the agent take? | `gateway.authorize_email`, `eval.brief_gate` |
| **node** | Was each step correct? | `research`, `llm.research` |

Canonical package: `packages/vpeetla_observability/` · [TRACE_LINKED_OBSERVABILITY.md](../docs/TRACE_LINKED_OBSERVABILITY.md)

**A2A** (updated 2026-07-03): VAP exposes a real external A2A discovery surface
(`backend/app/api/routes/a2a.py` — `.well-known/agent.json` + per-orchestrator agent cards; see
[ADR-009](./ADR-009-vap-auth-gate.md)). Other systems can discover and call VAP orchestrators via
the A2A spec. Internally, VAP specialists still hand off via in-process LangGraph — not A2A
between themselves. That split (external discovery via A2A, internal via LangGraph) is honest
for a reference implementation; ADR-013 closes the client side of the loop.

## Consequences

### Positive
- Matches [2026 production patterns](https://internative.net/insights/blog/agentic-ai-architecture-2026) without overselling
- Skills repo is a first-class org capability, not just "dev convenience"
- Honest status tables stop the trust erosion from metric theater

### Negative
- More documentation burden per repo
- Gateway wrapping adds latency on git push / publish paths

### Follow-ups
- ADR-009 (proposed at write time): LoopForge gateway on PR workflow — auth gates landed first; gateway follow-ups continue elsewhere
- ADR-010 (proposed at write time): MCP tool registry in VAP — MCP exposure landed in AegisAI (ADR-013)

## Links

- [ORG_IMPROVEMENT_PLAN_2026.md](../docs/ORG_IMPROVEMENT_PLAN_2026.md)
- [vpeetla-ai-skills](https://github.com/vpeetla-ai/vpeetla-ai-skills)
- [niteagent protocol stack](https://niteagent.com/blog/2026-06-07-agent-protocol-stack-mcp-a2a-production/)

# ADR-003: Mission-Based AgentOps Over Monolithic Prompts

**Status:** Accepted  
**Date:** 2026  
**System:** AegisLoop AgentOps Workbench  
**Live demo:** [aegisloop-agentops-workbench.vercel.app](https://aegisloop-agentops-workbench.vercel.app)

## In one breath (panel)

I'd ship AgentOps as bounded missions with traces, eval gates, and a human gate before ship — not a chat log with a fancy dashboard bolted on.

## Context

Agent demos love a single prompt or a linear chain. Production fleets need bounded work units, specialist handoffs you can observe, evaluation before anyone ships, and human approval before irreversible actions. A "dashboard over chat transcripts" is theater; it doesn't give you a unit of work you can cost, score, or refuse.

I refused treating AgentOps as UI chrome. The unit of work had to be real.

## Decision

Model **missions** as first-class bounded units:

- Mission brief → orchestrator → specialist agents
- Source coverage scoring and trace export (Langfuse)
- Evaluation gates before ship
- FinOps estimates per mission (honest metering landed later — see ADR-011 / ADR-012)
- VAP delegation for complex sub-tasks
- AegisAI gateway on the ship path

AgentOps is a discipline: brief, run, score, approve, ship. Not a prompt with better logging.

## Consequences

**Positive**

- Reviewers can ask "what is a mission?" and get a crisp answer with a live path
- Ship stays behind eval + gateway instead of "the agent said it was done"
- Composes with VAP (delegation) and AegisAI (ship gate) without swallowing either

**Negative**

- More moving parts than a chat demo — acceptable for a workbench, not for a 60-second toy
- Early FinOps estimates were heuristic; real metering required a separate service (ADR-011)

## Proof

- [aegisloop-agentops-workbench](https://github.com/vpeetla-ai/aegisloop-agentops-workbench)
- Case study: [case-studies/aegisloop-agentops.md](../case-studies/aegisloop-agentops.md)

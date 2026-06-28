# ADR-003: Mission-Based AgentOps Over Monolithic Prompts

**Status:** Accepted  
**Date:** 2026  
**System:** AegisLoop AgentOps Workbench  
**Live demo:** [aegisloop-agentops-workbench.vercel.app](https://aegisloop-agentops-workbench.vercel.app)

## Context

Agent demos use single prompts or linear chains. Production agent fleets need bounded work units with specialist handoffs, observable traces, evaluation gates, and human approval before irreversible actions.

## Decision

Model **missions** as first-class bounded units:

- Mission brief → orchestrator → specialist agents
- Source coverage scoring and trace export (Langfuse)
- Evaluation gates before ship
- FinOps estimates per mission
- VAP delegation for complex sub-tasks
- AegisAI gateway on ship path

AgentOps is a discipline — not a dashboard bolted onto chat logs.

## Proof

- [aegisloop-agentops-workbench](https://github.com/vpeetla-ai/aegisloop-agentops-workbench)
- Case study: [case-studies/aegisloop-agentops.md](../case-studies/aegisloop-agentops.md)

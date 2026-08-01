# ADR-001: Split Orchestration and Governance into Separate Layers

**Status:** Accepted  
**Date:** 2026  
**Systems:** Venkat AI Platform (VAP) · AegisAI  
**Portfolio:** [venkat-ai.com/work](https://venkat-ai.com/work)

## In one breath (panel)

I'd keep the agent graph for *what should we do* and put an independent gateway in front of irreversible tools for *are we allowed* — merging those into one repo is how policy becomes optional when the demo needs a win.

## Context

Most teams start where I started: LangGraph flows, tool routing, RAG, multi-agent handoffs. That gets you a working multi-agent OS. Production breaks the first time an agent can deploy, publish, notify, or move money with no identity, no policy boundary, and no audit trail you can show a reviewer.

VAP answered *what should agents do* — Chief → Planner → specialists → Critic → notify. It worked. It did not answer: *who is this agent, what is it allowed to do, and can we prove what happened?* I refused to bolt soft guardrails into the graph prompts and call that governance.

## Decision

Split the problem into two repos and keep them that way:

1. **VAP** — *What should agents do?* Orchestration, retrieval, specialist routing, loop patterns.
2. **AegisAI** — *What are agents allowed to do?* Gateway SDK, OPA policy, HITL queues, signed audit, agent registry.

Integration is the **AegisAI Gateway SDK at side-effect boundaries**. I refused a monolith that "does orchestration and governance" — the graph never gets a back door around policy.

## Consequences

**Positive**

- Orchestration can grow (new orchestrators, RAG strategies) without rewriting the policy engine
- Same gateway contract covers VAP notify, Content Factory publish, RAG ingest, and AegisLoop ship
- A technical reviewer can inspect each layer on its own

**Negative**

- Two repos to maintain — mitigated by a shared gateway contract and live integration demos
- Teams have to learn where the boundary sits — written up in [From Multi-Agent OS to Agent Governance](../case-studies/from-multi-agent-os-to-agent-governance.md)

## Proof

- Live VAP → AegisAI gateway on notify channels
- Content Factory publish blocked until gateway policy allows
- Essay: [case-studies/from-multi-agent-os-to-agent-governance.md](../case-studies/from-multi-agent-os-to-agent-governance.md)

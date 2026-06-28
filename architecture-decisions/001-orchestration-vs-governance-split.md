# ADR-001: Split Orchestration and Governance into Separate Layers

**Status:** Accepted  
**Date:** 2026  
**Systems:** Venkat AI Platform (VAP) · AegisAI  
**Portfolio:** [venkat-ai.com/work](https://venkat-ai.com/work)

## Context

Enterprise teams building agentic AI typically start with orchestration — LangGraph flows, tool routing, RAG, multi-agent collaboration. Production breaks when side-effecting actions (deploy, publish, notify, payment) have no identity model, policy boundary, or audit trail.

VAP was built as a multi-agent operating system: Chief → Planner → parallel specialists → Critic → notify channels. It worked for orchestration. It did not answer: *who is this agent, what is it allowed to do, and can we prove what happened?*

## Decision

Split the problem into two complementary repos:

1. **VAP** — *What should agents do?* Orchestration, retrieval, specialist routing, loop patterns.
2. **AegisAI** — *What are agents allowed to do?* Gateway SDK, OPA policy, HITL queues, signed audit, agent registry.

Integration happens through the **AegisAI Gateway SDK** at side-effect boundaries — not by merging orchestration and governance into one monolith.

## Consequences

**Positive**

- Orchestration can evolve (new orchestrators, RAG strategies) without rewriting policy engine
- Governance can enforce across VAP, Content Factory, RAG ingest, and AegisLoop ship paths uniformly
- Technical reviewers can inspect each layer independently

**Negative**

- Two repos to maintain — mitigated by shared gateway contract and live integration demos
- Teams must learn where to draw the boundary — documented in [From Multi-Agent OS to Agent Governance](../case-studies/from-multi-agent-os-to-agent-governance.md)

## Proof

- Live VAP → AegisAI gateway on notify channels
- Content Factory publish blocked until gateway policy allows
- Essay: [case-studies/from-multi-agent-os-to-agent-governance.md](../case-studies/from-multi-agent-os-to-agent-governance.md)

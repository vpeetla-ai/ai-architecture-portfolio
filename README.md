# AI Architecture Portfolio

### Production-grade governed agent systems — architecture, decisions, and measurable outcomes

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Portfolio](https://img.shields.io/badge/🌐_venkat--ai.com-Portfolio_%26_Live_Demos-5eead4?style=flat-square)](https://venkat-ai.com/work)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Venkata_Peetla-0A66C2?style=flat-square)](https://www.linkedin.com/in/venkata-peetla/)

---

**Venkata Peetla** — Principal AI Architect · Lucid Motors  
*19 years enterprise delivery · 11 live reference systems · 12 open-source repos*

[Live demos](https://venkat-ai.com/work) · [Executive brief](https://venkat-ai.com/profile/executive-brief) · [GitHub org](https://github.com/vpeetla-ai)

---

## Impact at a Glance

| **10→2** | **Multi-$M** | **11 live systems** | **6-layer stack** |
|----------|--------------|---------------------|-------------------|
| Agent ops staffing reduction (targeted supply-chain flows) | Revenue & savings — payments, subscriptions, EDI | Governance, orchestration, RAG, AgentOps, content, **loop engineering** | Wired together, not isolated demos |

---

## Governed AI Reference Stack

Six questions every enterprise agent program must answer — each mapped to a live repo and demo.

| # | Question | System | Live demo | Source |
|---|----------|--------|-----------|--------|
| 1 | What should agents do? | **Venkat AI Platform** — multi-agent OS | [venkat-ai-platform.vercel.app](https://venkat-ai-platform.vercel.app) | [venkat-ai-platform](https://github.com/vpeetla-ai/venkat-ai-platform) |
| 2 | What are agents allowed to do? | **AegisAI** — gateway, policy, HITL, audit | [aegisai-enterprise-agent-platform.vercel.app](https://aegisai-enterprise-agent-platform.vercel.app) | [aegisai](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform) |
| 3 | What knowledge can they use? | **Enterprise RAG** — access-before-ranking | [demo-omega-taupe.vercel.app](https://demo-omega-taupe.vercel.app) | [enterprise_rag_platform](https://github.com/vpeetla-ai/enterprise_rag_platform) |
| 4 | How do we operate agent fleets? | **AegisLoop** — missions, traces, eval gates | [aegisloop-agentops-workbench.vercel.app](https://aegisloop-agentops-workbench.vercel.app) | [aegisloop](https://github.com/vpeetla-ai/aegisloop-agentops-workbench) |
| 5 | What do they produce? | **AI Content Factory** — governed publish pipeline | [ai-content-factory-iota.vercel.app](https://ai-content-factory-iota.vercel.app) | [ai-content-factory](https://github.com/vpeetla-ai/ai-content-factory) |
| 6 | **How do agents improve?** | **LoopForge** — loop harness, RAG tuning, memory | [loop-engine-agent-platform.vercel.app](https://loop-engine-agent-platform.vercel.app) | [loop-engine-agent-platform](https://github.com/vpeetla-ai/loop-engine-agent-platform) |

**Canonical essay:** [From Multi-Agent OS to Agent Governance](case-studies/from-multi-agent-os-to-agent-governance.md)

---

## Featured Case Studies

Each includes architecture context, key decisions, trade-offs, and links to live demos + source code.

### AI Reference Systems (open source)

| Project | Domain | Key outcome | Case study |
|---------|--------|-------------|------------|
| **LoopForge** | Loop engineering | Self-improving harness — ODAEU, MCP, RAG tuning | [case-studies/loopforge-self-improving-harness.md](case-studies/loopforge-self-improving-harness.md) |
| **AegisAI** | Agent governance | Runtime control plane — gateway, HITL, signed audit | [case-studies/aegisai-agent-governance.md](case-studies/aegisai-agent-governance.md) |
| **Venkat AI Platform** | Multi-agent orchestration | 3 LangGraph orchestrators · 7 RAG strategies | [case-studies/venkat-ai-platform.md](case-studies/venkat-ai-platform.md) |
| **Enterprise RAG** | Knowledge layer | Authorization before ranking · hybrid retrieval | [case-studies/enterprise-rag-platform.md](case-studies/enterprise-rag-platform.md) |
| **AegisLoop** | AgentOps | Mission fleets · eval gates · FinOps · Langfuse | [case-studies/aegisloop-agentops.md](case-studies/aegisloop-agentops.md) |
| **AI Content Factory** | Content automation | Research → drafts → HITL → governed publish | [case-studies/ai-content-factory.md](case-studies/ai-content-factory.md) |

### Enterprise Delivery (employer context)

| Project | Organization | Key outcome | Case study |
|---------|--------------|-------------|------------|
| **Enterprise Agentic AI** | Lucid Motors | 10→2 staffing in targeted supply-chain flows | [case-studies/enterprise-agentic-ai-lucid.md](case-studies/enterprise-agentic-ai-lucid.md) |
| **Gulf Payments Modernization** | Volvo Cars | Multi-$M annualized revenue impact | [case-studies/gulf-payments-modernization.md](case-studies/gulf-payments-modernization.md) |
| **Subscription Revenue Platform** | Volvo Cars | Durable recurring revenue platform | [case-studies/subscription-revenue-platform.md](case-studies/subscription-revenue-platform.md) |
| **Supply Chain EDI Re-Platforming** | Volvo Cars | Multi-$M annualized savings | [case-studies/supply-chain-edi-replatforming.md](case-studies/supply-chain-edi-replatforming.md) |

---

## Architecture Decision Records

Real decisions from production systems — not theoretical patterns.

| ADR | Topic | Key insight |
|-----|-------|-------------|
| [ADR-001](architecture-decisions/001-orchestration-vs-governance-split.md) | Orchestration vs governance split | VAP + AegisAI as complementary layers — orchestration without governance is a liability |
| [ADR-002](architecture-decisions/002-authorization-before-ranking-rag.md) | Authorization before ranking | RAG is an access-controlled intelligence layer, not a vector DB wrapper |
| [ADR-003](architecture-decisions/003-mission-based-agentops.md) | Mission-based AgentOps | Bounded missions with eval gates — fleets survive production, not monolithic prompts |
| [ADR-004](architecture-decisions/004-gateway-hitl-side-effects.md) | Gateway + HITL for side effects | Side-effecting tool calls require policy + human approval + signed audit |
| [ADR-006](architecture-decisions/006-loop-harness-self-improving-agents.md) | Loop harness for self-improvement | Agent → Harness → Loops → Memory — RAG evolves on eval failure |
| [ADR-005](architecture-decisions/005-reference-stack-free-tier.md) | Reference stack on free tier | Vercel + Render + Groq — production boundaries without enterprise budget on day one |

---

## Agent Pattern Library

Five MIT-licensed patterns with live trace viewers — mapped to VAP orchestrators.

| Pattern | Live demo | Repository |
|---------|-----------|------------|
| ReAct | [react-agent-pattern.vercel.app](https://react-agent-pattern.vercel.app) | [react-agent-pattern](https://github.com/vpeetla-ai/react-agent-pattern) |
| Reflection | [reflection-agent-pattern.vercel.app](https://reflection-agent-pattern.vercel.app) | [reflection-agent-pattern](https://github.com/vpeetla-ai/reflection-agent-pattern) |
| Plan-Execute | [plan-execute-agent-pattern.vercel.app](https://plan-execute-agent-pattern.vercel.app) | [plan-execute-agent-pattern](https://github.com/vpeetla-ai/plan-execute-agent-pattern) |
| Multi-Agent | [multi-agent-system-pattern.vercel.app](https://multi-agent-system-pattern.vercel.app) | [multi-agent-system-pattern](https://github.com/vpeetla-ai/multi-agent-system-pattern) |
| Swarm | [swarm-agent-pattern.vercel.app](https://swarm-agent-pattern.vercel.app) | [swarm-agent-pattern](https://github.com/vpeetla-ai/swarm-agent-pattern) |

---

## Technical Expertise

**Agentic AI & Governance** — Multi-agent orchestration (LangGraph), runtime gateway (OPA policy, HITL), agent registry, signed audit, evaluation gates, AI FinOps

**Enterprise RAG** — Access-aware retrieval, hybrid search, reranking, graph expansion, citation traceability, ingest/answer HITL bridges

**Platform & Delivery** — FastAPI · Next.js · Postgres · Qdrant · AWS/OCI · 19 years across Google · Kaiser · Volvo · Lucid

**Leadership** — Kaiser Platform Lead · Volvo Staff Engineer · 20+ engineers led · multi-$M enterprise outcomes

---

## Connect

- **Portfolio:** [venkat-ai.com](https://venkat-ai.com)
- **Hiring overview:** [venkat-ai.com/hire](https://venkat-ai.com/hire)
- **Writing:** [Substack](https://venkatapeetla.substack.com) · [Medium](https://medium.com/@vpeetla.ai)
- **Email:** vpeetla.ai@gmail.com

---

*This repository is the canonical architecture narrative for the governed AI reference stack. Implementation code lives in [vpeetla-ai](https://github.com/vpeetla-ai) org repos; live demos at [venkat-ai.com/work](https://venkat-ai.com/work).*

# vpeetla-ai Domain Model

Shared vocabulary for all org repos. Agents should use these terms consistently.

## Stack layers

| Layer | Question | Repo | Demo |
|-------|----------|------|------|
| Orchestration | What should agents do? | venkat-ai-platform | venkat-ai-platform.vercel.app |
| Governance | What are agents allowed? | aegisai-enterprise-agent-platform | aegisai-enterprise-agent-platform.vercel.app |
| LLM gateway | How do we route and quota model calls? | aegis-llm-gateway | aegis-llm-gateway-api.onrender.com |
| Routing contract | Shared role/tier/data-class enforce schemas | aegis-routing-contract | GitHub (library) |
| Semantic cache | How do we similarity-cache completions? | aegis-semantic-cache | aegis-semantic-cache-api.onrender.com |
| Knowledge | What knowledge can they use? | enterprise_rag_platform | enterprise-rag-platform-eta.vercel.app |
| Knowledge + MLOps | How do we adapt models to domain format? | domainforge-rag-peft | domainforge-rag-peft.vercel.app |
| AgentOps | How do we operate fleets? | aegisloop-agentops-workbench | aegisloop-agentops-workbench.vercel.app |
| Application | What do they produce? | ai-content-factory | ai-content-factory-iota.vercel.app |
| Self-improvement | How do agents improve? | loop-engine-agent-platform | demo-omega-taupe.vercel.app |

## Core terms

| Term | Meaning |
|------|---------|
| **Harness** | Outer scheduler: budgets, tracing, eval gates, loop termination (LoopForge, ODAEU) |
| **Tool gateway** | AegisAI — policy + HITL + audit before tool side effects |
| **LLM gateway plane** | aegis-llm-gateway — OpenAI-shaped proxy, quotas, stub/BYOK; **enforces+records** role-aware decisions (ADR-028/029) — apps still **select** |
| **Routing contract** | aegis-routing-contract — ThesisRole, DataClass, ModelTier, RoutingDecisionV2, enforce helpers |
| **Cost / compliant outcome** | agent-finops KPI: eval pass + no policy deny + HITL when required + budget OK |
| **Tenant identity (LLM plane)** | `X-Tenant-Id` + optional `X-Principal-Id`; allowlist via `ALLOWED_TENANT_IDS` / `TENANT_ENFORCEMENT` |
| **Semantic cache plane** | aegis-semantic-cache — embed + similarity lookup; separate scale path |
| **ODAEU** | Observe → Decide → Act → Evaluate → Update (outer self-improve loop) |
| **Access-before-ranking** | Filter chunks by principal clearance before hybrid retrieval scores |
| **HITL** | Human-in-the-loop gate before irreversible actions (publish, push, deploy) |
| **Mission** | Bounded AgentOps unit in AegisLoop (research, content, incident, etc.) |
| **Orchestrator** | LangGraph node that plans and routes between specialist agents |
| **loopforge/fix-{id}** | Branch name for automated repo fixes — never push directly to `main` |
| **Stub mode** | `AGENT_RUNTIME_MODE=local_stub` or MockLLM — no API keys required |

## Agent patterns (VAP series)

| Pattern | Repo | Use when |
|---------|------|----------|
| ReAct | react-agent-pattern | Tool loops with thought → action → observation |
| Reflection | reflection-agent-pattern | Critique-and-revise before delivery |
| Plan-Execute | plan-execute-agent-pattern | Explicit plan before multi-step execution |
| Multi-Agent | multi-agent-system-pattern | Role specialists + orchestrator delegation |
| Swarm | swarm-agent-pattern | Parallel workers + aggregation |

## Deploy boundaries (ADR-005)

- **UI** → Vercel (static or Next.js)
- **API** → Render (Docker or native Python)
- **Vectors** → Qdrant Cloud (optional)
- **LLM** → apps → `aegis-llm-gateway` (optional `LLM_GATEWAY_URL`) → providers; cache via `aegis-semantic-cache`
- **Free tier** → `plan: free` in render.yaml; expect cold starts

## Integration rule

Side effects (notify, publish, deploy, git push to protected branch) → **tool gateway or HITL** unless explicitly in local stub mode. Model HTTP is the **LLM gateway plane**, not AegisAI.

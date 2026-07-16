# Repo → interview playbook map

Crosswalk from [vpeetla-ai](https://github.com/vpeetla-ai) product repos to Staff+ prep in
[ai-architect-interview-playbook](https://github.com/vpeetla-ai/ai-architect-interview-playbook)
([study UI](https://ai-architect-interview-playbook.vercel.app) ·
[Practice Arena](https://ai-architect-practice-arena.vercel.app)).

**Rule:** only list entries the repo honestly exercises (shipped code, ADR, or demo path). Partial fit is labeled. Empty categories are omitted in each README.

| Repo | Business function | Primary system design | Also useful |
|------|-------------------|----------------------|-------------|
| [venkat-ai-platform](https://github.com/vpeetla-ai/venkat-ai-platform) | Multi-agent OS: route, parallel specialists, critic, notify | [03 agent orchestration](https://ai-architect-interview-playbook.vercel.app/q/ai-system-design/03-agent-tool-use-orchestration-platform/) | 13 durable agents · 07 LLM gateway · trade-offs 01/03 · behavioral 05 |
| [aegisai-enterprise-agent-platform](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform) | Governance gateway: policy, HITL, audit before side effects | [05 security/compliance](https://ai-architect-interview-playbook.vercel.app/q/cloud-architecture/05-security-and-compliance-architecture-for-ai-systems/) · [07 LLM gateway](https://ai-architect-interview-playbook.vercel.app/q/cloud-architecture/07-llm-gateway-semantic-cache-model-router/) | SD 03/09/10 · trade-off 03 · behavioral 03 |
| [aegis-llm-gateway](https://github.com/vpeetla-ai/aegis-llm-gateway) | Shared OpenAI-shaped LLM plane — apps select; GW enforces+records (ADR-028/029) | [07 LLM gateway / semantic cache](https://ai-architect-interview-playbook.vercel.app/q/cloud-architecture/07-llm-gateway-semantic-cache-model-router/) | trade-off 01 · FinOps pre-flight · confidential→private |
| [aegis-routing-contract](https://github.com/vpeetla-ai/aegis-routing-contract) | Shared ThesisRole / DataClass / RoutingDecisionV2 + enforce helpers (ADR-029) | [07 LLM gateway / semantic cache](https://ai-architect-interview-playbook.vercel.app/q/cloud-architecture/07-llm-gateway-semantic-cache-model-router/) | schema boundary · apps select vs plane enforce |
| [aegis-semantic-cache](https://github.com/vpeetla-ai/aegis-semantic-cache) | Tenant-scoped semantic cache-as-service | [07 LLM gateway / semantic cache](https://ai-architect-interview-playbook.vercel.app/q/cloud-architecture/07-llm-gateway-semantic-cache-model-router/) | trade-off 01 · poisoning / hit-rate |
| [enterprise_rag_platform](https://github.com/vpeetla-ai/enterprise_rag_platform) | Access-aware RAG: ACL before rank, citations, decline | [02 RAG at scale](https://ai-architect-interview-playbook.vercel.app/q/ai-system-design/02-rag-platform-at-scale/) | cloud 05 · trade-off 01 |
| [domainforge-rag-peft](https://github.com/vpeetla-ai/domainforge-rag-peft) | RAG facts + PEFT behavior; support triage schemas | [02 RAG](https://ai-architect-interview-playbook.vercel.app/q/ai-system-design/02-rag-platform-at-scale/) · [16 support assistant](https://ai-architect-interview-playbook.vercel.app/q/ai-system-design/16-llm-customer-support-assistant/) | SD 04/08 (partial) · trade-off 04 |
| [voiceforge-assistant](https://github.com/vpeetla-ai/voiceforge-assistant) | Real-time ASR→LLM→TTS triage with latency budgets | [16 support assistant](https://ai-architect-interview-playbook.vercel.app/q/ai-system-design/16-llm-customer-support-assistant/) | trade-off 01 · general 02 (WS, partial) |
| [ai-content-factory](https://github.com/vpeetla-ai/ai-content-factory) | Multi-agent content pipeline + HITL publish | [03 orchestration](https://ai-architect-interview-playbook.vercel.app/q/ai-system-design/03-agent-tool-use-orchestration-platform/) | general 04/08 · behavioral 05 · trade-off 01 |
| [aegisloop-agentops-workbench](https://github.com/vpeetla-ai/aegisloop-agentops-workbench) | AgentOps missions, traces, eval gates | [07 eval/observability](https://ai-architect-interview-playbook.vercel.app/q/ai-system-design/07-llm-evaluation-observability-platform/) | SD 03 · trade-off 01 |
| [agent-finops](https://github.com/vpeetla-ai/agent-finops) | Shared metering, budgets, breach signals | [06 container/cost](https://ai-architect-interview-playbook.vercel.app/q/cloud-architecture/06-container-orchestration-and-cost-optimization-at-scale/) | trade-offs 01/02 · behavioral 02 · SD 09 quotas |
| [loop-engine-agent-platform](https://github.com/vpeetla-ai/loop-engine-agent-platform) | Self-improve harness, repo-fix, RAG evolve | [13 durable agents](https://ai-architect-interview-playbook.vercel.app/q/ai-system-design/13-durable-long-running-agent-execution/) · [15 coding assistant](https://ai-architect-interview-playbook.vercel.app/q/ai-system-design/15-ai-coding-assistant/) | SD 07/10 · trade-off 01 |
| [vllm-architecture-lab](https://github.com/vpeetla-ai/vllm-architecture-lab) | Inference education: paging, batching, KV | [01 inference serving](https://ai-architect-interview-playbook.vercel.app/q/ai-system-design/01-llm-inference-serving-at-scale/) | cloud 01/06 · trade-off 04 (partial) |
| [sentinel-brief](https://github.com/vpeetla-ai/sentinel-brief) | Overnight intel brief → eval → governed email | [03 orchestration](https://ai-architect-interview-playbook.vercel.app/q/ai-system-design/03-agent-tool-use-orchestration-platform/) | general 04/08/11 (partial) |
| [golden-eval-registry](https://github.com/vpeetla-ai/golden-eval-registry) | Portable golden fixtures / CI gates | [07 eval/observability](https://ai-architect-interview-playbook.vercel.app/q/ai-system-design/07-llm-evaluation-observability-platform/) | trade-off 02 |
| [omniforge](https://github.com/vpeetla-ai/omniforge) | Self-contained multimodal multi-agent multi-LLM | [03 orchestration](https://ai-architect-interview-playbook.vercel.app/q/ai-system-design/03-agent-tool-use-orchestration-platform/) · [06 multimodal](https://ai-architect-interview-playbook.vercel.app/q/ai-system-design/06-multimodal-search-recommendation-system/) | cloud 07 · trade-off 01 |
| `*-agent-pattern` | Teaching stubs for ReAct / reflect / plan-exec / MAS / swarm | [03 orchestration](https://ai-architect-interview-playbook.vercel.app/q/ai-system-design/03-agent-tool-use-orchestration-platform/) (pattern slice) | coding 07 (graph, light) |
| [ai-architect-practice-arena](https://github.com/vpeetla-ai/ai-architect-practice-arena) | BYOK graded mock interviews | Playbook companion (all categories via rubrics) | — |
| [ai-architect-interview-playbook](https://github.com/vpeetla-ai/ai-architect-interview-playbook) | Source of truth for the maps above | — | — |

Meta / docs-only (`ai-architecture-portfolio`, `vpeetla-ai-skills`, `vpeetla-ai` profile): point here; do not duplicate full tables.

## Maintenance

When adding a playbook entry or a product capability, update this file **and** the repo README `## Interview map` section in the same change set when practical.

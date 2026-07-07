# LinkedIn Post Templates — vpeetla-ai

Use after repo passes [LINKEDIN_READINESS_AUDIT.md](./LINKEDIN_READINESS_AUDIT.md) (≥14/16).

**Format:** 1,200–1,800 characters · architecture image (export Mermaid PNG) · ≤3 hashtags

---

## Skeleton

```text
{Hook — one contrarian sentence}

Most teams {failure mode}.

We built {Product} to {specific outcome}:
→ {Architecture decision 1}
→ {Architecture decision 2}
→ {Honest constraint}

{Measurable outcome or eval discipline — one sentence}

Architecture: {GitHub diagram or case study URL}
Try it: {live demo URL}

Honest scope in the README status table.

#Hashtag1 #Hashtag2
```

---

## Week 1 — Enterprise RAG (draft)

> Ranking before authorization is a data leak — not a retrieval bug.
>
> Enterprise RAG Platform filters chunks by principal clearance **before** hybrid scoring — then cross-encoder rerank, citations, and decline-to-answer when evidence is weak.
>
> Golden eval runs as a **real CI gate** — not a slide deck metric.
>
> Live: enterprise-rag-platform-eta.vercel.app
> Architecture: github.com/vpeetla-ai/enterprise_rag_platform
>
> #EnterpriseAI #RAG

---

## Week 2 — DomainForge (draft)

> Fine-tuning the whole model for every SOP change ships stale policies.
>
> DomainForge splits the problem:
> **RAG holds facts** (SOP citations)
> **QLoRA + DPO holds behavior** (strict JSON triage)
>
> S0→S4 eval ladder — prove each layer before adapter promotion.
>
> Live: domainforge-rag-peft.vercel.app
> Case study: ai-architecture-portfolio/case-studies/domainforge-rag-peft.md
>
> #MLOps #RAG #EnterpriseAI

---

## Week 3 — vLLM Lab (draft)

> Serving dozens of fine-tuned LLMs used to mean dozens of idle GPUs.
>
> vLLM multi-LoRA changes the economics — if you understand PagedAttention, continuous batching, and KV budget math.
>
> vLLM Architecture Lab is our **educational simulator** (not a production fork) — the reference I'd want before sizing a multi-tenant inference cluster. Pairs with DomainForge (where adapters come from).
>
> Live: vllm-architecture-lab.vercel.app
>
> #LLMInference #vLLM #AIArchitecture

---

## Week 4 — VoiceForge (draft)

> Voice UX fails at time-to-first-token — not model quality.
>
> VoiceForge: browser ASR → governed LLM triage → TTS with **latency budgets per phase** and graceful degradation when any step exceeds budget.
>
> Plugs into DomainForge for structured triage JSON.
>
> Live: voiceforge-assistant.vercel.app
>
> #VoiceAI #LLMOps

---

## Week 0 — Anchor essay (draft)

> Everyone is shipping agents. Almost no one is shipping the layer that decides what an agent is *allowed* to do.
>
> I spent 2026 building a governed agent stack in the open — 11 production platforms, 20+ ADRs, versioned eval contracts. Not chat demos. The load-bearing separations:
>
> → **Orchestration ≠ governance** — what agents *do* vs what they're *allowed* to do
> → **Access before ranking** — retrieval filters by clearance before it scores
> → **Side effects behind a gateway or HITL** — nothing irreversible without a human or policy
> → **Self-improvement is a harness + eval loop** — not a bigger prompt
>
> Every claim is inspectable: live demo → GitHub → ADR → case study.
>
> Start here: venkat-ai.com/work
>
> #AIArchitecture #AgentGovernance

---

## Week 5 — AegisAI (draft)

> The dangerous line in an agent isn't the model call — it's the tool call that deletes, pays, or publishes.
>
> AegisAI is the gateway that sits **in front of tool execution**: policy check → HITL approval → signed audit → registry lifecycle. Agents propose; the gateway authorizes.
>
> Orchestration decides *what*. Governance decides *allowed*. Different layers, on purpose.
>
> Live: aegisai-enterprise-agent-platform.vercel.app
>
> #AgentGovernance #EnterpriseAI

---

## Week 6 — VAP (draft)

> "Multi-agent" is easy to demo and hard to operate.
>
> Venkat AI Platform is the orchestration layer: 3 LangGraph orchestrators, 7 RAG strategies, ReAct / Reflection / Plan-Execute loops — Chief → parallel specialists → Critic. Side effects (notify) are **gateway-wrapped**, never fired inline.
>
> Orchestration ≠ governance — VAP delegates, AegisAI authorizes.
>
> Live: venkat-ai-platform.vercel.app
>
> #MultiAgent #LangGraph #AIArchitecture

---

## Week 7 — AegisLoop (draft)

> "AgentOps" is usually a dashboard bolted on after the incident.
>
> AegisLoop treats it as a discipline: **bounded missions**, specialist handoffs, P50/P95 + failure-rate metrics, source-coverage scoring, FinOps estimates, and a **human-gated ship** step. The mission_gate suite runs as a real CI gate.
>
> The operating layer between orchestration and a production agent fleet.
>
> Live: aegisloop-agentops-workbench.vercel.app
>
> #AgentOps #LLMOps

---

## Week 8 — ACF (draft)

> Auto-publishing agents are one hallucinated post away from a brand incident.
>
> AI Content Factory: research → 5 platform drafts → **human approval** → governed publish. The publish step goes through the AegisAI gateway — it *cannot* ship until policy allows. Real LinkedIn/X OAuth when tokens are set.
>
> The interesting engineering is the gate, not the generation.
>
> Live: ai-content-factory-iota.vercel.app/sign-in
>
> #AgentGovernance #HITL

---

## Week 9 — LoopForge (draft)

> Self-improving agents sound like hype until you make them fix a real bug and open a real PR.
>
> LoopForge: clone repo → run pytest → LangGraph patch loop (Orchestrator · Review · Quality) → branch `loopforge/fix-{id}` → **open PR, never push to main**. ODAEU harness tunes RAG on eval failure.
>
> Improvement is a harness + eval loop — not a longer prompt.
>
> Live: demo-omega-taupe.vercel.app
>
> #AgentEngineering #LangGraph

---

## Week 10 — Sentinel (draft)

> The problem with an overnight AI-news bot isn't fetching — it's *trusting* what it sends you.
>
> Sentinel Brief: multi-source crawl → snapshot **diff** (only what changed) → **eval gate** on the summary → governed email. If the brief fails quality, it doesn't send.
>
> Governance applies to outbound content too, not just tool calls.
>
> Live: sentinel-brief-ruddy.vercel.app
>
> #LLMOps #AIagents

---

## Week 11 — golden-eval-registry (draft)

> "We have evals" usually means a notebook someone ran once.
>
> golden-eval-registry makes evals a **product**: versioned golden fixtures + scorers for RAG answers, repo-fix, mission gates, and HITL — wired as **CI gates** across repos. A regression fails the build, not a vibe check.
>
> Evals-as-contracts is what lets the rest of the stack move fast safely.
>
> Repo: github.com/vpeetla-ai/golden-eval-registry
>
> #LLMOps #Evals

---

## Week 12 — Agent patterns carousel (draft)

> Most "agent frameworks" hide the one thing you need to reason about: the control flow.
>
> 5 production agent patterns, each a standalone repo + live trace viewer:
> → ReAct → Reflection → Plan-Execute → Multi-Agent → Swarm
>
> Same governed spine (typed state, traces, eval hooks) — different control topology. Pick the pattern, not the framework.
>
> Live: react-agent-pattern.vercel.app (+ 4 more)
>
> #LangGraph #AgentPatterns #AIArchitecture

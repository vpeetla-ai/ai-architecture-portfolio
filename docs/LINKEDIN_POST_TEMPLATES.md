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

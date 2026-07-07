# Social Preview Copy — designer handoff

**Canvas:** 1200 × 630 px · **Format:** PNG < 1 MB · **Font:** Inter or system sans (match `vpeetla-theme.css`)

Copy each block below into Figma/Canva. Export as `og.png` → `public/og.png` in the demo repo.

Spec reference: [SOCIAL_PREVIEW_SPEC.md](./SOCIAL_PREVIEW_SPEC.md)

---

## Shared layout (all cards)

```
┌─────────────────────────────────────────────────────────────────┐
│ vpeetla-ai · {EYEBROW}                              [optional] │
│                                                                  │
│ {HEADLINE}                                                       │
│ {SUBHEAD — one line, ≤ 60 characters}                            │
│                                                                  │
│ [{chip 1}]  [{chip 2}]  [{chip 3}]          LIVE · {short-url}  │
└─────────────────────────────────────────────────────────────────┘
```

**Typography**
- Eyebrow: 11–12px, uppercase, letter-spacing 0.08em, accent color at 80% opacity
- Headline: 36–44px, semibold, white `#f8fafc`
- Subhead: 18–20px, regular, `#94a3b8`
- Chips: 13px, pill border `#334155`, text `#e2e8f0`
- LIVE badge: 12px, green `#22c55e` dot + monospace URL

**Background:** `#0b1220` with subtle radial gradient (accent at 8% opacity, top-right)

---

## Week 1 — Enterprise RAG

| Field | Copy |
|-------|------|
| **Eyebrow** | KNOWLEDGE |
| **Headline** | Enterprise RAG |
| **Subhead** | Authorization before ranking · rerank · decline |
| **Chip 1** | Access-before-ranking |
| **Chip 2** | Cross-encoder rerank |
| **Chip 3** | Decline-to-answer |
| **Short URL** | enterprise-rag-platform-eta.vercel.app |
| **Accent** | `#6366f1` indigo |

**OG meta (paste into layout.tsx / meta tags)**
```
og:title       Enterprise RAG — Access-before-ranking retrieval
og:description Governed RAG: filter by clearance before scoring, rerank with cross-encoder, decline when evidence is weak.
og:url         https://enterprise-rag-platform-eta.vercel.app
twitter:card   summary_large_image
```

**Filename:** `enterprise-rag-og.png`

---

## Week 2 — DomainForge

| Field | Copy |
|-------|------|
| **Eyebrow** | KNOWLEDGE + MLOPS |
| **Headline** | DomainForge |
| **Subhead** | RAG for facts · PEFT for behavior · S0→S4 |
| **Chip 1** | 13 SOP docs · hybrid RAG |
| **Chip 2** | QLoRA + DPO alignment |
| **Chip 3** | Ollama bench UI |
| **Short URL** | domainforge-rag-peft.vercel.app |
| **Accent** | `#8b5cf6` violet |

**OG meta**
```
og:title       DomainForge — RAG facts + PEFT behavior
og:description Support triage pipeline: capstone SOP RAG, Bitext QLoRA, S0→S4 eval ladder, adapter promotion gates.
og:url         https://domainforge-rag-peft.vercel.app
```

**Filename:** `domainforge-og.png`  
**Note:** Disable Vercel Deployment Protection before LinkedIn post (currently SSO-gated).

---

## Week 3 — vLLM Architecture Lab

| Field | Copy |
|-------|------|
| **Eyebrow** | LLM INFERENCE |
| **Headline** | vLLM Architecture Lab |
| **Subhead** | PagedAttention · multi-LoRA economics |
| **Chip 1** | Continuous batching |
| **Chip 2** | KV cache budgets |
| **Chip 3** | 5-tab simulator |
| **Short URL** | vllm-architecture-lab.vercel.app |
| **Accent** | `#f97316` orange |

**OG meta**
```
og:title       vLLM Architecture Lab — PagedAttention & multi-LoRA
og:description Educational vLLM reference: paging, batching, KV math — pairs with DomainForge adapter training.
og:url         https://vllm-architecture-lab.vercel.app
```

**Filename:** `vllm-lab-og.png`

---

## Week 4 — VoiceForge

| Field | Copy |
|-------|------|
| **Eyebrow** | VOICE / MULTIMODAL |
| **Headline** | VoiceForge |
| **Subhead** | ASR → LLM → TTS · latency budgets |
| **Chip 1** | Browser ASR |
| **Chip 2** | P50/P95 waterfall |
| **Chip 3** | Graceful degradation |
| **Short URL** | voiceforge-assistant.vercel.app |
| **Accent** | `#f43f5e` rose |

**OG meta**
```
og:title       VoiceForge — Real-time voice triage
og:description Browser ASR, governed LLM triage, TTS with per-phase latency budgets and fallback to text.
og:url         https://voiceforge-assistant.vercel.app
```

**Filename:** `voiceforge-og.png`  
**Note:** Disable Vercel Deployment Protection before LinkedIn post (currently SSO-gated).

---

## Week 5 — AegisAI

| Field | Copy |
|-------|------|
| **Eyebrow** | GOVERNANCE |
| **Headline** | AegisAI |
| **Subhead** | Gateway before side effects · HITL · audit |
| **Chip 1** | AI Gateway intercept |
| **Chip 2** | OPA policy + HITL |
| **Chip 3** | Signed audit trail |
| **Short URL** | aegisai-enterprise-agent-platform.vercel.app |
| **Accent** | `#7c3aed` purple |

**OG meta**
```
og:title       AegisAI — Enterprise agent governance
og:description Runtime control plane: policy, HITL, and signed audit before any tool side effect executes.
og:url         https://aegisai-enterprise-agent-platform.vercel.app
```

**Filename:** `aegisai-og.png`

---

## Week 6 — Venkat AI Platform (VAP)

| Field | Copy |
|-------|------|
| **Eyebrow** | ORCHESTRATION |
| **Headline** | Venkat AI Platform |
| **Subhead** | Multi-agent OS · orchestration ≠ governance |
| **Chip 1** | 3 LangGraph orchestrators |
| **Chip 2** | 7 RAG strategies |
| **Chip 3** | Gateway-wrapped notify |
| **Short URL** | venkat-ai-platform.vercel.app |
| **Accent** | `#0ea5e9` sky |

**OG meta**
```
og:title       Venkat AI Platform — Multi-agent orchestration
og:description Chief → specialists → Critic. Orchestration decides what; AegisAI decides allowed.
og:url         https://venkat-ai-platform.vercel.app
```

**Filename:** `vap-og.png`

---

## Week 7 — AegisLoop

| Field | Copy |
|-------|------|
| **Eyebrow** | AGENTOPS |
| **Headline** | AegisLoop |
| **Subhead** | Bounded missions · eval gates · FinOps |
| **Chip 1** | Specialist handoffs |
| **Chip 2** | P50/P95 metrics |
| **Chip 3** | Human-gated ship |
| **Short URL** | aegisloop-agentops-workbench.vercel.app |
| **Accent** | `#10b981` emerald |

**OG meta**
```
og:title       AegisLoop — AgentOps workbench
og:description Mission fleets with observable traces, eval gates, FinOps estimates, and governed ship paths.
og:url         https://aegisloop-agentops-workbench.vercel.app
```

**Filename:** `aegisloop-og.png`

---

## Week 8 — AI Content Factory

| Field | Copy |
|-------|------|
| **Eyebrow** | CONTENT |
| **Headline** | AI Content Factory |
| **Subhead** | Research → drafts → HITL → governed publish |
| **Chip 1** | 5 platform drafts |
| **Chip 2** | Clerk + HITL approval |
| **Chip 3** | AegisAI publish gate |
| **Short URL** | ai-content-factory-iota.vercel.app |
| **Accent** | `#f59e0b` amber |

**OG meta**
```
og:title       AI Content Factory — Governed content pipeline
og:description Multi-agent research and drafts; nothing publishes until human approval and gateway policy allow.
og:url         https://ai-content-factory-iota.vercel.app/sign-in
```

**Filename:** `acf-og.png`  
**Note:** Use `/sign-in` as public entry until root landing is exposed.

---

## Week 9 — LoopForge

| Field | Copy |
|-------|------|
| **Eyebrow** | SELF-IMPROVEMENT |
| **Headline** | LoopForge |
| **Subhead** | Repo fix → PR · harness · ODAEU loops |
| **Chip 1** | clone → pytest → patch |
| **Chip 2** | LangGraph coding loop |
| **Chip 3** | Never pushes to main |
| **Short URL** | demo-omega-taupe.vercel.app |
| **Accent** | `#ec4899` pink |

**OG meta**
```
og:title       LoopForge — Self-improving agent harness
og:description Clone repos, run pytest, patch, open PR on loopforge/fix-{id} — harness + eval, not bigger prompts.
og:url         https://demo-omega-taupe.vercel.app
```

**Filename:** `loopforge-og.png`

---

## Week 10 — Sentinel Brief

| Field | Copy |
|-------|------|
| **Eyebrow** | OVERNIGHT INTEL |
| **Headline** | Sentinel Brief |
| **Subhead** | Snapshot diff → eval gate → governed email |
| **Chip 1** | Multi-source crawl |
| **Chip 2** | Diff-only briefing |
| **Chip 3** | Eval gate before send |
| **Short URL** | sentinel-brief-ruddy.vercel.app |
| **Accent** | `#14b8a6` teal |

**OG meta**
```
og:title       Sentinel Brief — Governed overnight intelligence
og:description HN, arXiv, industry feeds → snapshot diff → quality gate → email only if brief passes eval.
og:url         https://sentinel-brief-ruddy.vercel.app
```

**Filename:** `sentinel-og.png`

---

## Week 0 — Anchor essay (venkat-ai.com/work)

| Field | Copy |
|-------|------|
| **Eyebrow** | PORTFOLIO |
| **Headline** | Governed Agent Stack |
| **Subhead** | 11 platforms · 20+ ADRs · inspect before we talk |
| **Chip 1** | Orchestration ≠ governance |
| **Chip 2** | Access before ranking |
| **Chip 3** | Side effects behind gateway |
| **Short URL** | venkat-ai.com/work |
| **Accent** | `#5eead4` cyan |

**OG meta**
```
og:title       Venkata Peetla — Principal AI Architect
og:description Open-source governed agent stack: orchestration, gateway, RAG, AgentOps, self-improvement — every claim inspectable.
og:url         https://venkat-ai.com/work
```

**Filename:** `portfolio-anchor-og.png` · host on `venkat-ai-portfolio/public/og.png`

---

## Week 12 — Agent patterns carousel (single card)

| Field | Copy |
|-------|------|
| **Eyebrow** | AGENT PATTERNS |
| **Headline** | Production Agent Patterns |
| **Subhead** | ReAct · Reflection · Plan-Execute · Multi-Agent · Swarm |
| **Chip 1** | Live trace viewers ×5 |
| **Chip 2** | LangGraph reference |
| **Chip 3** | pytest without API keys |
| **Short URL** | react-agent-pattern.vercel.app |
| **Accent** | `#9333ea` langgraph purple |

**OG meta**
```
og:title       Production Agent Patterns — 5 control flows
og:description ReAct, Reflection, Plan-Execute, Multi-Agent, Swarm — standalone repos with inspectable traces.
og:url         https://react-agent-pattern.vercel.app
```

**Filename:** `agent-patterns-og.png`

---

## Export checklist (designer)

- [ ] 12 PNGs exported at exactly 1200×630
- [ ] Text within safe zone (1120×550 centre)
- [ ] Delivered to repo `public/og.png` per product (see table in SOCIAL_PREVIEW_SPEC.md)
- [ ] Verified on [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/) + [opengraph.xyz](https://www.opengraph.xyz)
- [ ] Flagged blockers: DomainForge + VoiceForge SSO; ACF use `/sign-in`

# Model Plane 100% — Principal AI Engineer Gap Closure

**Org:** [vpeetla-ai](https://github.com/vpeetla-ai)  
**Owner:** Venkata Peetla  
**Status:** Active execution  
**Companion tracker:** [MODEL_PLANE_100_TRACKER.md](./MODEL_PLANE_100_TRACKER.md)  
**Related:** [PORTFOLIO_2026_GAP_PLAN.md](./PORTFOLIO_2026_GAP_PLAN.md) · ADR-019/020/022 · ADR-028/029 · ADR-034 (ModelForge)

---

## In one breath (panel)

I already ship governed agents. This program makes the **model plane** as inspectable as the agent plane — SLM, PEFT, CUDA vLLM, LLMOps — with GPU receipts a CAIO can click, not lab theater.

---

## Why this exists

A recent CAIO skim concluded “you only know agents.” That was a **signal failure**, not a total capability gap:

| Reality | Why CAIO missed it |
|---------|-------------------|
| DomainForge has QLoRA + DPO ladder | Labeled “Teaching drawer / not hire hero” |
| vLLM Architecture Lab teaches paging/batching | Pure-Python simulator — no CUDA metrics |
| aegis-llm-gateway routes + meters | Not on the D1 spine |
| Honest ADRs refuse overclaim | Hire path never opens them |

**Goal:** Profile and demos must credibly support Principal depth across:

`GenAI · Agentic AI · LLMOps · PEFT/fine-tuning · SLMs · CUDA inference · vLLM · evals · FinOps`

Without becoming a fake research lab that pretends to pretrain foundations.

---

## Target persona (definition of “perfect”)

A Principal AI Engineer / Architect who can walk a CAIO through:

1. **When to buy vs retrieve vs adapt vs self-host** (decision tree with costs)
2. **PEFT** — QLoRA SFT + preference alignment, adapter lifecycle, promote gates
3. **SLMs** — when a 3B–8B local model wins on latency/cost/privacy vs API LLMs
4. **Inference systems** — prefill vs decode, KV cache, continuous batching, real **vLLM on CUDA**
5. **LLMOps** — gateway enforce+record, semantic cache, FinOps budgets, eval regression
6. **Agentic GenAI** — already strong (AegisAI + VAP + RAG + HITL) — keep as peer, not only hero

**Explicit non-goals (honesty fence):**

- Pretraining a foundation model from scratch
- Claiming educational Path B as production multi-LoRA CUDA
- Spawning a 17-product zoo — **one** new flagship only

---

## Architecture decision — one new platform

### Decision: ship **ModelForge** (`modelforge-llmops`)

**Why a new platform (not only README edits):**

| Option | Verdict |
|--------|---------|
| A. Reposition DomainForge alone | Still branded “teaching”; PEFT-only story |
| B. Harden vLLM Lab to CUDA | Lab stays educational by design (ADR honesty) |
| C. **ModelForge as Model Plane flagship** | Single hire-facing product; composes DomainForge + CUDA vLLM + bench + gateway | ✅ |

```text
                    ┌─────────────────────────────────────┐
                    │           ModelForge (NEW)          │
                    │  Hire hero — Model Plane control UI │
                    │  Receipts · Bench · Serve · Route   │
                    └───────────┬─────────────┬───────────┘
                                │             │
              ┌─────────────────┼─────────────┼─────────────────┐
              ▼                 ▼             ▼                 ▼
     DomainForge          CUDA vLLM      SLM Bench        aegis-llm-gateway
     (train PEFT)         (real serve)   (bake-off)       (enforce+record)
              │                 │
              └────────┬────────┘
                       ▼
              vLLM Architecture Lab
              (concepts only — linked, not claimed as prod)
```

**Spine evolution (D1 → D1+M):**

| # | Layer | Repo | Role |
|---|-------|------|------|
| 1 | Decisions | ai-architecture-portfolio | ADRs |
| 2 | Governance | aegisai-enterprise-agent-platform | Tool gateway |
| 3 | Orchestration | venkat-ai-platform | Agents |
| 4 | Knowledge | enterprise_rag_platform | RAG |
| 5 | **Models (NEW)** | **modelforge-llmops** | SLM · PEFT · vLLM · LLMOps |
| 6 | Application | ai-content-factory | Governed publish |

Proof stays linked: golden-eval-registry · agent-finops.  
Teaching drawer keeps pattern repos + VoiceForge + OmniForge.

---

## Capability matrix → 100% exit criteria

| Capability | Today | 100% means | Proof artifact |
|------------|-------|------------|----------------|
| Agentic GenAI | ~90% | Keep; cross-link ModelForge | Existing spine demos |
| LLMOps / gateway | ~70% | ModelForge → gateway path live | RoutingDecision receipt |
| PEFT / fine-tune | ~65% | GPU-trained adapter + eval Δ | `receipts/peft/*.json` + HF adapter |
| SLM expertise | ~55% | Published bake-off table | `receipts/slm_bakeoff.md` |
| CUDA / vLLM | ~40% | Real vLLM Docker + LoRA metrics | `receipts/vllm_cuda.json` |
| Quant / serve math | ~50% | Documented AWQ/FP8 trade-offs + one quant run note | Case study section |
| Foundation pretrain | ~5% | Honest refuse + decision tree | Panel script + ADR-034 |

**Program exit (Definition of Done):**

- [ ] ModelForge live (Vercel UI + Render/API or documented GPU host)
- [ ] GitHub profile + venkat-ai.com hire/tech-review show **Model track** as spine peer
- [ ] Three clickable receipts: PEFT · CUDA vLLM · SLM bake-off
- [ ] ADR-034 accepted; case study published
- [ ] Panel script rehearsed (60s + 5min deep)
- [ ] CAIO objection “agents only” is rebuttable in &lt;30s with links

---

## Phased execution (6 weeks)

### Phase 0 — Plan + narrative (Days 1–3) ← current

| ID | Task | Owner artifact |
|----|------|----------------|
| 0.1 | This plan + tracker | `docs/MODEL_PLANE_100_*.md` |
| 0.2 | ADR-034 ModelForge | `adr/ADR-034-*.md` |
| 0.3 | Profile README Model track | `vpeetla-ai` README |
| 0.4 | venkat-ai.com ecosystem entry | `venkat-ai-portfolio` data |
| 0.5 | Scaffold `modelforge-llmops` repo | new GitHub repo |

### Phase 1 — ModelForge MVP (Days 4–10)

| ID | Task | Exit |
|----|------|------|
| 1.1 | FastAPI: `/health`, `/v1/posture`, `/v1/receipts` | Honest status table |
| 1.2 | Next.js glass-box: Architecture · PEFT · Serve · Bench · Ops | One composition UI |
| 1.3 | Wire DomainForge API status (read-only) | Shows S0–S4 ladder live or stub |
| 1.4 | Wire aegis-llm-gateway posture | Model plane ↔ control plane |
| 1.5 | Deploy free-tier UI + API | Cold-start labeled |

### Phase 2 — PEFT GPU receipt (Days 11–18)

| ID | Task | Exit |
|----|------|------|
| 2.1 | DomainForge: scale SFT data + DPO pairs (documented sizes) | README numbers match |
| 2.2 | RunPod/CUDA `gpu_pipeline` → QLoRA adapter | Adapter artifact |
| 2.3 | Eval table S0 vs S3 vs S4 win-rate | Published in ModelForge + case study |
| 2.4 | Optional private HF upload | Link in receipt (no secrets) |
| 2.5 | Promote-gate demo path | API-key gated promote documented |

### Phase 3 — CUDA vLLM receipt (Days 19–28)

| ID | Task | Exit |
|----|------|------|
| 3.1 | `docker-compose.vllm.yml` (upstream vLLM, not lab) | Compose runs on GPU host |
| 3.2 | Serve base + LoRA module from DomainForge adapter | OpenAI-compatible `/v1/chat` |
| 3.3 | Capture TTFT p50/p95, tok/s, VRAM | `receipts/vllm_cuda.json` |
| 3.4 | ADR-022 Path A note + ModelForge Serve tab | Honesty: Path B remains edu |
| 3.5 | Link vLLM Lab as “concepts” only | No overclaim |

### Phase 4 — SLM bake-off + LLMOps glue (Days 29–35)

| ID | Task | Exit |
|----|------|------|
| 4.1 | Golden suite: 3B / 7B Ollama vs API model | Same prompts |
| 4.2 | Metrics: schema pass%, latency, $ estimate | Table in ModelForge |
| 4.3 | Decision memo (Substack/LinkedIn) | Public URL |
| 4.4 | Gateway route: SLM local vs cloud deny confidential | RoutingDecision sample |
| 4.5 | FinOps meter on bake-off runs | agent-finops link |

### Phase 5 — Profile perfection + panel pack (Days 36–42)

| ID | Task | Exit |
|----|------|------|
| 5.1 | Hire page dual-fit: Agents **and** Models | Copy live |
| 5.2 | Technical-review 15-min path includes ModelForge | Spine health probe |
| 5.3 | Interview playbook entries for PEFT / vLLM / SLM | Mapped in REPO_INTERVIEW_MAP |
| 5.4 | Mock CAIO loop logged | `interview/MOCK_LOOP_LOG.md` |
| 5.5 | Freeze: no new repos after ModelForge | Retro note |

---

## Panel scripts (memorize)

### 30-second rebuttal

> I’m not an agents-only architect. Agents are how work gets done; the **model plane** is how I decide buy vs RAG vs PEFT vs self-host. ModelForge is the control UI — DomainForge trains adapters, CUDA vLLM serves them, SLM bench proves when small models win, and the LLM gateway enforces routing + FinOps.

### 60-second depth

> Facts stay in RAG (ADR-019). Behavior and schema go in PEFT — QLoRA then DPO (ADR-020). Serving math I teach in the vLLM lab; production numbers come from real CUDA vLLM with LoRA modules (ADR-022 Path A). Gateway apps select; the plane enforces and records (ADR-028/029). I don’t pretrain foundations — that’s the wrong economic move for enterprise triage. I own the adaptation and serving loop end-to-end.

### CAIO trap questions → answers

| Trap | Answer |
|------|--------|
| “Have you trained your own LLM?” | “I adapt open bases with PEFT; I don’t pretend to pretrain 7B+ from scratch. Here’s the adapter receipt and eval delta.” |
| “Show me vLLM experience” | “Educational lab for internals; ModelForge Serve tab for CUDA metrics from upstream vLLM.” |
| “Why not always GPT-4?” | “SLM bake-off: schema tasks often win on 7B local for cost/latency/privacy — table is public.” |
| “Isn’t this just agents?” | “Agents call tools; ModelForge is weights, serve, and route — different plane, same org.” |

---

## Risk register

| Risk | Mitigation |
|------|------------|
| GPU cost / no always-on CUDA | Receipts from ephemeral RunPod; free tier stays honest stub |
| Overclaiming Path B | Status tables + `/v1/posture` machine truth |
| Scope creep (new repos) | **Only ModelForge**; deepen DomainForge/vLLM Lab/gateway |
| Narrative drift vs site metrics | Single `metrics.ts` + profile sync checklist |
| Freeze conflict | ADR-034 documents intentional exception: one Model Plane flagship |

---

## Success metrics (scorecard)

| Metric | Baseline | Target |
|--------|----------|--------|
| CAIO “agents only” risk | High | Low (Model track on D1) |
| PEFT GPU receipt | Missing | Published |
| CUDA vLLM receipt | Missing | Published |
| SLM bake-off | Partial UI | Published table + memo |
| ModelForge live demo | N/A | 200 + honest posture |
| Interview map model entries | Partial | PEFT + vLLM + SLM primary |

---

## File / repo touch map

| Repo | Changes |
|------|---------|
| **modelforge-llmops** (new) | Platform MVP + receipts gallery |
| domainforge-rag-peft | GPU runbook, data scale, export to ModelForge |
| vllm-architecture-lab | Cross-link; keep edu honesty |
| aegis-llm-gateway | ModelForge consumer wiring docs |
| ai-architecture-portfolio | Plan, tracker, ADR-034, case study |
| vpeetla-ai (profile) | Model track on spine |
| venkat-ai-portfolio | hire / work / technical-review / ecosystem |

---

## Order of implementation (strict)

1. Plan + tracker + ADR-034 (this PR)
2. Scaffold ModelForge + profile narrative
3. PEFT receipt
4. CUDA vLLM receipt
5. SLM bake-off
6. Site/hire polish + mock panel

Do not start Phase 3 before Phase 2 adapter exists.  
Do not claim 100% until tracker checkboxes for Phases 0–5 are green.

---

## Links

- Tracker: [MODEL_PLANE_100_TRACKER.md](./MODEL_PLANE_100_TRACKER.md)
- Gap heritage: [PORTFOLIO_2026_GAP_PLAN.md](./PORTFOLIO_2026_GAP_PLAN.md)
- ADR-019 RAG vs PEFT · ADR-020 DPO · ADR-022 vLLM · ADR-028/029 gateway

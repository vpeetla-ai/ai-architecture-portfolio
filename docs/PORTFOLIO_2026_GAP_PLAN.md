# Portfolio 2026 Gap Plan — Five Essential AI Projects

**Org:** [vpeetla-ai](https://github.com/vpeetla-ai) · **Portfolio:** [venkat-ai.com/work](https://venkat-ai.com/work)  
**Date:** Jul 2026 · **Status:** Honest self-assessment — **Phases A–B complete** · **LinkedIn launch Phases 0–2 complete** ([LINKEDIN_LAUNCH_PLAN.md](./LINKEDIN_LAUNCH_PLAN.md))

This document maps the current 21-repo stack to the **five essential AI portfolio projects for 2026** — systems that prove production discipline, not chat demos.

---

## Executive summary

| # | Pillar | Primary repo(s) | Coverage | Verdict |
|---|--------|-----------------|----------|---------|
| 1 | Production-Grade RAG | enterprise_rag_platform, domainforge-rag-peft | ~85% | **Strong** — cross-encoder reranker + decline-to-answer shipped Jul 2026 |
| 2 | Local AI Assistant (SLMs) | domainforge-rag-peft, vllm-architecture-lab | ~55% | **Partial** — `/bench` UI + case study; GPU artifacts user-driven |
| 3 | Monitoring & Observability | ai-content-factory, sentinel-brief, aegisloop | ~70% | **Partial** — P50/P95 + failure rate on AegisLoop; enterprise_rag observability middleware ⬜ |
| 4 | Fine-Tuning (SFT + DPO) | domainforge-rag-peft | ~80% | **Strong** — full ladder; gaps: production-scale data + GPU-trained artifacts |
| 5 | Real-Time Multimodal (Voice) | voiceforge-assistant | ~85% | **Strong** — MVP shipped Jul 2026; optional: server Whisper, AegisAI TTS gate |

**Bottom line:** All five pillars are now **demonstrated across the stack**. Pillars 1–3 need **targeted hardening**; Pillar 5 closed with **VoiceForge**.

---

## Pillar 1 — Production-Grade RAG

> Domain-specific “ask my doc” with hybrid retrieval, reranking, citation enforcement, golden eval CI.

### What you already satisfy

| Requirement | Evidence | Repo |
|-------------|----------|------|
| Hybrid retrieval (BM25 + semantic) | `HybridRetriever`, `InMemoryHybridRetriever` | domainforge, enterprise_rag |
| Vector store | Chroma (S1), Qdrant adapter | domainforge, enterprise_rag, VAP |
| Citation traceability | `cite_faq_ids`, citation guardrails | domainforge, enterprise_rag |
| Golden eval dataset | `sample.jsonl`, `golden_queries.json`, registry suites | domainforge, enterprise_rag, golden-eval-registry |
| CI regression gate | `test_golden_eval_gate.py` runs shared registry suite | enterprise_rag (**real gate**) |
| Access-before-ranking | ADR-002, principal filter | enterprise_rag |
| LangGraph orchestration | 3 StateGraph pipelines, ENTERPRISE RAG strategy | venkat-ai-platform |
| Eval harness | S0→S4 compare, hallucination scorer | domainforge |

### Gaps (fix in existing repos)

| Gap | Severity | Recommended fix | Owner repo | Effort |
|-----|----------|-----------------|------------|--------|
| **Cross-encoder reranker** (not heuristic/LLM) | High | Add `sentence-transformers/cross-encoder/ms-marco-MiniLM` stage after hybrid retrieval | enterprise_rag_platform | M |
| **Ragas faithfulness** | Medium | Integrate `ragas` metrics OR remove “Ragas” from DomainForge README diagram | domainforge, enterprise_rag | S |
| **Decline-to-answer** when retrieval unsupported | High | Return structured refusal if max retrieval score < threshold | enterprise_rag, domainforge | S |
| **True dense hybrid on Qdrant** | Medium | Replace scroll+lexical Qdrant adapter with embedded vectors + BM25 fusion | enterprise_rag_platform | L |
| **Golden eval CI on DomainForge** | Medium | Wire `domainforge.triage_preference_v1` as real CI gate (like enterprise_rag) | domainforge + golden-eval-registry | S |
| **VAP hybrid is keyword overlap, not BM25** | Low | Document honestly or delegate to ENTERPRISE strategy by default | venkat-ai-platform | S |
| **Weaviate** | Low | Optional — Qdrant/Chroma sufficient for portfolio; mention as ADR trade-off | docs only | — |

### Missing as standalone narrative

No single README says: *“This is the production RAG reference — start here.”* **enterprise_rag_platform** is that repo, but the org profile splits attention across DomainForge (MLOps) and Enterprise RAG (governance). **Action:** cross-link prominently on [vpeetla-ai README](https://github.com/vpeetla-ai) with a “RAG track” callout.

---

## Pillar 2 — Local AI Assistant (Small Language Models)

> Ollama offline models, structured JSON, rigorous benchmarking, quantization comparison.

### What you already satisfy

| Requirement | Evidence | Repo |
|-------------|----------|------|
| Ollama integration | `generate_with_ollama`, Modelfile export | domainforge-rag-peft |
| Open-source 7B target | Mistral-7B-Instruct in train configs | domainforge |
| Structured JSON + Pydantic | `TriageResponse` schema, `format=json` | domainforge |
| Quantization awareness | AWQ/FP8 educational content | vllm-architecture-lab |
| GPU → Ollama pipeline | `docs/GPU_OLLAMA_PIPELINE.md`, `export-ollama` CLI | domainforge |
| LiteLLM Ollama fallback | `ollama/llama3.1:8b` route | ai-content-factory |

### Gaps

| Gap | Severity | Recommended fix | Effort |
|-----|----------|-----------------|--------|
| **No dedicated Local AI product** | High | New repo `local-ai-bench` OR extend DomainForge with a “Local inference” tab | L |
| **Benchmark study deliverable** | High | Script: tokens/sec, P50 latency, memory GB for Mistral/Llama3.2 at Q4/Q5/Q8 — publish as case study | M |
| **Models 3B–7B comparison table** | Medium | Run Ollama on llama3.2:3b, mistral:7b, phi3 — same golden prompts | M |
| **Production Ollama not live on Render** | Expected | Document: train on GPU pod, serve Ollama on same host, point API via `OLLAMA_BASE_URL` | S (docs done) |
| **Privacy/offline narrative** | Low | Portfolio copy: “air-gapped triage path” for regulated domains | S |

### Recommended new platform (optional)

**`local-ai-bench`** — thin repo: Ollama benchmark CLI + static report UI on Vercel. Reuses DomainForge golden prompts. **Estimated:** 1–2 weeks. **Alternative:** add `/bench` route to DomainForge UI (lower overhead).

---

## Pillar 3 — Monitoring & Observability Layer

> Trace every pipeline step; P50/P95 latency; cost per request; failure rates.

### What you already satisfy

| Requirement | Evidence | Repo |
|-------------|----------|------|
| Langfuse integration | `export_trace_summary`, generations | ai-content-factory, sentinel-brief |
| Per-step tracing | `@observe_node` on graph nodes | ai-content-factory, sentinel-brief |
| Trace-linked evals | system/trace/node levels | TRACE_LINKED_OBSERVABILITY.md |
| Cost per run | `total_cost_usd` in DB | ai-content-factory |
| Mission cost metering | agent-finops integration | aegisloop |
| RAG pipeline spans | `rag.retrieve`, `rag.generate` + duration_ms | enterprise_rag |
| Shared observability package | `vpeetla_observability` | ai-architecture-portfolio → synced to 7 repos |

### Gaps

| Gap | Severity | Recommended fix | Owner repo | Effort |
|-----|----------|-----------------|------------|--------|
| **P50/P95 latency dashboards** | High | Aggregate `AgentTrace.latency_ms` → daily rollup endpoint + AegisLoop UI panel | aegisloop or ai-content-factory | M |
| **Failure rate %** | High | `error_runs / total_runs` over 24h — expose on `/v1/metrics` | all platform APIs | M |
| **Cost per request (not per run)** | Medium | Normalize pipeline cost by request count in middleware | ai-content-factory | S |
| **enterprise_rag not on TraceRecorder** | Medium | Wire synced `vpeetla_observability` middleware (package exists, unused) | enterprise_rag | S |
| **aegisloop dual telemetry paths** | Medium | Consolidate `MissionTelemetry` → `TraceRecorder` | aegisloop | M |
| **Chunk-level retrieval visibility in UI** | Medium | Enterprise RAG UI: show retrieved chunks per query (debug panel) | enterprise_rag | M |
| **Braintrust / Langsmith** | Low | LangSmith wired in ACF; document as optional second exporter | docs | — |

### Recommended approach

**Do not build a new observability repo.** Extend **AegisLoop** as the “observability console” for the stack — it already has mission traces, eval gates, FinOps. Add:
1. P50/P95 latency cards (from Langfuse API or local DB rollup)
2. Failure rate trend
3. Cross-link to Enterprise RAG retrieval traces

---

## Pillar 4 — Fine-Tuning for Specific Tasks

> SFT (LoRA/QLoRA) + DPO preference tuning; TRL; 2k–10k examples.

### What you already satisfy

| Requirement | Evidence | Repo |
|-------------|----------|------|
| SFT QLoRA | `SFTTrainer`, `train_qlora.yaml` | domainforge |
| DPO preference tuning | `DPOTrainer`, preference pairs, S4 ladder | domainforge |
| TRL library | `trl>=0.9` in pyproject | domainforge |
| Hard negative preference pairs | `make_rejected()` taxonomy | domainforge |
| S3 vs S4 compare + win-rate | `preference_win_rate_pct` | domainforge |
| Adapter registry + promote gate | API-key gated promote | domainforge |
| GPU pipeline | `pipeline-gpu`, RunPod docs | domainforge |
| ADR separation RAG vs PEFT | ADR-019, ADR-020 | ai-architecture-portfolio |
| Golden fixture | `domainforge.triage_preference_v1` | golden-eval-registry |

### Gaps

| Gap | Severity | Recommended fix | Effort |
|-----|----------|-----------------|--------|
| **SFT dataset below 2k recommended** | Medium | `make fetch-bitext` full split (~27k available) — document in README | S |
| **DPO pairs only 8 (smoke)** | Medium | Scale preference generator to full golden + Bitext stratified sample | M |
| **No GPU-trained Mistral artifacts published** | High | Run `scripts/gpu_pipeline.sh` on RunPod; optional HF private upload | User action |
| **Axolotl** | Low | TRL sufficient for portfolio; mention as alternative in ADR | docs |
| **Org README still says S0→S3** | Low | Update DomainForge blurb to S0→S4 + DPO on [vpeetla-ai](https://github.com/vpeetla-ai) | S |
| **Model comparison study (fine-tune vs prompt)** | Medium | Add eval table: S0 vs S3 vs S4 on full golden — publish in case study | M |

### Verdict

**DomainForge is your Pillar 4 flagship.** It is the most complete of the five pillars. Remaining work is **scale + GPU execution**, not architecture.

---

## Pillar 5 — Real-Time Multimodal Application (Voice)

> ASR → LLM → TTS; WebSockets; latency budget visualization; graceful degradation.

### What VoiceForge satisfies (Jul 2026)

| Requirement | Evidence | Repo |
|-------------|----------|------|
| ASR | Browser Web Speech API (default) + optional `faster-whisper` | voiceforge-assistant |
| LLM triage | Mock / Ollama / DomainForge `/v1/query` | voiceforge-assistant |
| TTS | `edge-tts` server + browser `speechSynthesis` fallback | voiceforge-assistant |
| WebSocket transport | `/ws/voice` phase events + result payload | voiceforge-assistant |
| Latency budget breakdown | `LatencyBudget` — ASR / LLM TTFT / TTS / total | voiceforge-assistant |
| Graceful degradation | `DegradationReason` enum — text input, browser TTS, cached reply | voiceforge-assistant |
| Latency waterfall UI | Next.js static export — per-phase bars | voiceforge-assistant |
| Replay | `/v1/replay` last turn | voiceforge-assistant |
| Tests + ADR | 9 pytest; ADR-001 voice pipeline | voiceforge-assistant |

**Live:** [voiceforge-assistant.vercel.app](https://voiceforge-assistant.vercel.app) · [API](https://voiceforge-api-eysb.onrender.com)

### Remaining gaps (optional hardening)

| Gap | Severity | Recommended fix | Effort |
|-----|----------|-----------------|--------|
| **Server Whisper on Render** | Low | Keep browser ASR default; document GPU host for Whisper | S (docs) |
| **AegisAI gate before TTS** | Medium | HITL on outbound audio in regulated demos | M |
| **Voice activity detection** | Low | Client-side VAD in UI | S |
| **Golden eval on transcript faithfulness** | Medium | `golden-eval-registry` suite for voice turns | M |

### Verdict

**VoiceForge closes Pillar 5.** Portfolio now has a deployable voice pipeline with honest multi-mode operation (browser ASR on free tier, real TTS, pluggable LLM).

---

## Cross-repo gap matrix (quick reference)

| Capability | enterprise_rag | domainforge | VAP | aegisloop | ACF | sentinel | voiceforge |
|------------|---------------|-------------|-----|-----------|-----|----------|------------|
| Hybrid BM25+vector | partial | yes | partial | — | — | — | — |
| Cross-encoder rerank | **yes** | no | no | — | — | — | — |
| Decline-to-answer | **yes** | partial | no | — | — | — | — |
| Golden eval CI gate | **yes** | **yes** | no | partial | partial | partial | — |
| Ragas | no | aspirational | no | — | — | — | — |
| Langfuse traces | partial | no | yes | partial | **yes** | **yes** | — |
| P50/P95 dashboards | no | no | no | **yes** | no | no | partial |
| SFT/DPO | — | **yes** | — | — | — | — | — |
| Ollama production | — | **yes** | — | — | fallback | — | optional |
| Voice/ASR/TTS | — | — | — | — | — | — | **yes** |

---

## Prioritized roadmap

### Phase A — Harden existing ✅ (Jul 2026)

1. **enterprise_rag:** cross-encoder reranker + decline-to-answer threshold
2. **domainforge:** fix Ragas README claim; scale DPO preference pairs; update org README to S0→S4
3. **golden-eval-registry:** wire DomainForge `triage_preference` as real CI gate
4. **aegisloop:** P50/P95 + failure rate cards from trace DB
5. **enterprise_rag:** wire `vpeetla_observability` middleware

### Phase B — Local AI benchmark ✅ (Jul 2026)

6. **DomainForge `/bench`** or **`local-ai-bench`** repo: Ollama tokens/sec + latency table for 3B/7B × Q4/Q5
7. Publish case study: “Structured JSON triage — model & quantization comparison”

### Phase C — GPU execution ✅ (docs + pipeline; RunPod user-driven)

8. RunPod: `bash scripts/gpu_pipeline.sh` → real Mistral S3/S4 adapters
9. Point Render `MOCK_LLM=false` + `OLLAMA_BASE_URL` at GPU host

### Phase D — VoiceForge ✅ (Jul 2026)

10. **VoiceForge** — ASR + LLM + TTS + latency budget UI + graceful degradation — **shipped**

### Phase E — LinkedIn launch prep ✅ (Jul 2026)

11. **LINKEDIN_LAUNCH_PLAN.md** — phase tracker + audit rubric
12. **Canonical diagrams** — DomainForge, VoiceForge, Enterprise RAG, vLLM Lab
13. **README standardization** — DomainForge, VoiceForge, Enterprise RAG reranker row
14. **ADR-022** — DomainForge → vLLM multi-LoRA target architecture

### Phase F — LinkedIn posts ⬜

15. Week 0 anchor post → flagship weekly sequence (see [LINKEDIN_POST_TEMPLATES.md](./LINKEDIN_POST_TEMPLATES.md))

---

## What your portfolio already proves (for interviews)

You are **not** missing a junior demo collection. You have:

- **Governed multi-agent OS** (VAP) — orchestration depth
- **Enterprise governance** (AegisAI) — production safety
- **Access-aware RAG** (Enterprise RAG) — enterprise knowledge
- **RAG + MLOps** (DomainForge) — SFT + DPO + eval ladder
- **Trace-linked ops** (ACF, Sentinel, AegisLoop) — maintainability story
- **Self-improvement** (LoopForge) — agentic engineering
- **Eval contracts** (golden-eval-registry) — CI discipline
- **Inference education** (vLLM Lab) — systems depth

- **Real-time voice** (VoiceForge) — ASR → LLM → TTS with latency budgets

The rubric’s five pillars are **all demonstrated**. Remaining work is **hardening pillars 1–3**, not a ground-up rebuild.

---

## Sync targets after changes

| Artifact | Update when |
|----------|-------------|
| [vpeetla-ai/README.md](https://github.com/vpeetla-ai/vpeetla-ai) | DomainForge S0→S4; VoiceForge shipped |
| [ai-architecture-portfolio](https://github.com/vpeetla-ai/ai-architecture-portfolio) | ADRs for reranker, voice, observability SLOs |
| [venkat-ai-portfolio/data/ecosystem.ts](https://venkat-ai.com/work) | New platform cards |
| [golden-eval-registry](https://github.com/vpeetla-ai/golden-eval-registry) | New suite kinds + CI gates |
| [CONTEXT.md](https://github.com/vpeetla-ai/ai-content-factory/blob/main/CONTEXT.md) | Stack layer additions |

*This document is the canonical gap plan. Update after each phase completion. LinkedIn execution: [LINKEDIN_LAUNCH_PLAN.md](./LINKEDIN_LAUNCH_PLAN.md).*

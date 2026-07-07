# ADR-021: VoiceForge Real-Time Multimodal Pipeline

**Status:** Accepted  
**Date:** 2026-07-06  
**Context:** Portfolio Pillar 5 — Real-Time Multimodal / Voice

## Decision

Ship **VoiceForge** (`voiceforge-assistant`) as the org's voice triage reference:

1. **Browser-first ASR** on Render free tier (Web Speech API; client reports `asr_ms`)
2. **Pluggable LLM** — mock (demo), Ollama (GPU), DomainForge API (governed triage)
3. **Server TTS** via `edge-tts` with browser `speechSynthesis` fallback
4. **Per-phase latency budgets** (`LatencyBudget`) exposed to UI waterfall
5. **Graceful degradation** via `DegradationReason` enum and user-facing fallback copy
6. **Dual transport** — REST `/v1/voice` and WebSocket `/ws/voice`

## Rationale

| Constraint | Choice |
|------------|--------|
| Render free tier has no GPU | Default ASR in browser, not server Whisper |
| Portfolio needs honest demos | Mock LLM works without secrets; real paths env-switched |
| Pairs with DomainForge | `LLM_MODE=domainforge` routes to `/v1/query` |
| Interview narrative | Visible ASR / LLM TTFT / TTS / total latency breakdown |

## Consequences

- **Positive:** Fifth portfolio pillar closed with tests, ADR, deploy configs
- **Positive:** Reuses DomainForge + governed stack patterns (FastAPI, static Next.js)
- **Negative:** Browser ASR quality varies; server Whisper remains opt-in
- **Future:** AegisAI HITL before TTS; golden-eval suite for transcript faithfulness

## Related

- [VoiceForge case study](../case-studies/voiceforge-assistant.md)
- [ADR-019: RAG facts + PEFT behavior](./ADR-019-rag-facts-peft-behavior.md)
- Repo ADR: `voiceforge-assistant/docs/adr/ADR-001-voice-pipeline.md`

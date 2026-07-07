# VoiceForge — Real-Time Voice Triage Pipeline

**Domain:** Multimodal voice · ASR · LLM · TTS · Latency engineering  
**Live demo:** [voiceforge-assistant.vercel.app](https://voiceforge-assistant.vercel.app)  
**API:** [voiceforge-api-eysb.onrender.com](https://voiceforge-api-eysb.onrender.com)  
**Source:** [voiceforge-assistant](https://github.com/vpeetla-ai/voiceforge-assistant)

## Problem

Voice assistants must meet **sub-30s end-to-end latency** with visible phase breakdowns and fallbacks when ASR, LLM, or TTS fail. Chat-only demos do not prove multimodal production discipline.

## Architecture

Canonical: [docs/diagrams/canonical-architecture.mmd](https://github.com/vpeetla-ai/voiceforge-assistant/blob/main/docs/diagrams/canonical-architecture.mmd)

## Latency budgets (default)

| Phase | Budget (ms) | Measured in UI |
|-------|-------------|----------------|
| ASR | 8,000 | `asr_ms` |
| LLM (total) | 15,000 | `llm_total_ms` |
| LLM TTFT | — | `llm_ttft_ms` (tracked) |
| TTS | 10,000 | `tts_ms` |
| **Total** | **30,000** | waterfall + degradation |

When a phase exceeds budget, `DegradationReason` triggers text input, browser TTS, or cached reply.

## Key decisions

- **Browser-first ASR on free tier** — [ADR-021](../adr/ADR-021-voiceforge-multimodal-pipeline.md)
- **Pluggable LLM** — Mock / Ollama / DomainForge `/v1/query`
- **Dual transport** — REST + WebSocket phase events

## Impact

- **Closes Portfolio Pillar 5** — measurable multimodal latency
- Pairs with [DomainForge](domainforge-rag-peft.md) (voice → triage JSON)

## Related ADR

[ADR-021: VoiceForge multimodal pipeline](../adr/ADR-021-voiceforge-multimodal-pipeline.md)

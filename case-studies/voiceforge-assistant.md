# VoiceForge — Real-Time Voice Triage Pipeline

**Domain:** Multimodal voice · ASR · LLM · TTS · Latency engineering  
**Live demo:** [voiceforge-assistant.vercel.app](https://voiceforge-assistant.vercel.app)  
**API:** [voiceforge-api-eysb.onrender.com](https://voiceforge-api-eysb.onrender.com)  
**Source:** [voiceforge-assistant](https://github.com/vpeetla-ai/voiceforge-assistant)

## Problem

Chat demos don’t prove voice. A triage assistant has to meet a **sub-30s end-to-end budget** with a visible phase waterfall — and degrade when ASR, LLM, or TTS fails. The scar is a “multimodal” demo that silently hangs on one slow phase with no fallback.

## What we decided

1. **Browser-first ASR on free tier** — honest multimodal without a GPU bill ([ADR-021](../adr/ADR-021-voiceforge-multimodal-pipeline.md)).
2. **Phase latency budgets** — ASR / LLM / TTS measured in the UI; breach triggers `DegradationReason`.
3. **Pluggable LLM** — Mock / Ollama / DomainForge `/v1/query` so voice can land on triage JSON.
4. **Dual transport** — REST + WebSocket phase events for the waterfall.
5. **Refused:** claiming cloud ASR/TTS SLOs on a free-tier stack.

## Architecture

Canonical: [docs/diagrams/canonical-architecture.mmd](https://github.com/vpeetla-ai/voiceforge-assistant/blob/main/docs/diagrams/canonical-architecture.mmd)

### Latency budgets (default)

| Phase | Budget (ms) | Measured in UI |
|-------|-------------|----------------|
| ASR | 8,000 | `asr_ms` |
| LLM (total) | 15,000 | `llm_total_ms` |
| LLM TTFT | — | `llm_ttft_ms` (tracked) |
| TTS | 10,000 | `tts_ms` |
| **Total** | **30,000** | waterfall + degradation |

When a phase exceeds budget: text input, browser TTS, or cached reply.

## Live proof

- UI: [voiceforge-assistant.vercel.app](https://voiceforge-assistant.vercel.app)
- API: [voiceforge-api-eysb.onrender.com](https://voiceforge-api-eysb.onrender.com)
- Pairs with [DomainForge](./domainforge-rag-peft.md) (voice → triage JSON)

## Limitations / what we'd do differently

- Browser ASR quality varies; that’s the free-tier trade, not a Whisper replacement claim.
- edge-tts and cold starts can eat the budget — degradation path must stay visible.
- Next: optional server Whisper when a panel needs cleaner ASR; keep budgets first-class.

## Related ADR

[ADR-021: VoiceForge multimodal pipeline](../adr/ADR-021-voiceforge-multimodal-pipeline.md)

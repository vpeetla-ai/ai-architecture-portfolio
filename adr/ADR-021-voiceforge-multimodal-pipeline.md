# ADR-021: VoiceForge Real-Time Multimodal Pipeline

**Status:** Accepted  
**Date:** 2026-07-06  
**Context:** Portfolio Pillar 5 — Real-Time Multimodal / Voice

## In one breath (panel)

I'd put ASR in the browser on free-tier demos, keep the LLM pluggable (mock → Ollama → DomainForge), and show every phase's latency instead of a fake "real-time" badge.

## Context

Pillar 5 needed a voice triage reference that actually runs on Render free tier — no GPU. Server Whisper as the default would either lie about cost or sit cold forever. Hiding latency behind a spinner is demo theater. Pairing with DomainForge mattered more than inventing a sixth LLM stack.

## Decision

Ship **VoiceForge** (`voiceforge-assistant`) as the org's voice triage reference:

1. **Browser-first ASR** (Web Speech API; client reports `asr_ms`) — default, not server Whisper
2. **Pluggable LLM** — mock (demo), Ollama (GPU), DomainForge API (governed triage via `LLM_MODE=domainforge` → `/v1/query`)
3. **Server TTS** via `edge-tts`, with browser `speechSynthesis` fallback
4. **Per-phase latency budgets** (`LatencyBudget`) exposed in a UI waterfall
5. **Graceful degradation** via `DegradationReason` + user-facing fallback copy
6. **Dual transport** — REST `/v1/voice` and WebSocket `/ws/voice`

Refused: claiming production voice quality from free-tier browser ASR, and burying TTFT behind a single "done" spinner.

## Consequences

**Positive**

- Fifth portfolio pillar closed with tests, ADR, and deploy configs
- Reuses DomainForge + governed stack patterns (FastAPI, static Next.js)
- Interview narrative can point at a visible ASR / LLM TTFT / TTS / total breakdown

**Negative**

- Browser ASR quality varies by device/browser; server Whisper stays opt-in
- **Planned (not claimed live):** AegisAI HITL before TTS; golden-eval suite for transcript faithfulness

## Related

- [VoiceForge case study](../case-studies/voiceforge-assistant.md)
- [ADR-019: RAG facts + PEFT behavior](./ADR-019-rag-facts-peft-behavior.md)
- Repo ADR: `voiceforge-assistant/docs/adr/ADR-001-voice-pipeline.md`

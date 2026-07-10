# Case study: OmniForge — multimodal multi-LLM answer platform

## Problem

“Multi-agent” demos often hide a single hardcoded model. Multimodal asks (text + screenshot + voice) need specialized agents, tools, and **task-class model routing** with proof — or the architecture claim is empty.

## Decision

Ship **OmniForge** as a self-contained monorepo (ADR-027):

- Multimodal ingest → planner → parallel agents + MCP tools → synthesizer
- Multi-LLM Brain with buckets (`fast` / `structured` / `reasoning` / `vision`)
- Every call emits a `RoutingDecision` (waterfall); A/B single vs routed is first-class
- In-repo FinOps budget + export gate — **no** runtime dependency on sibling vpeetla-ai services

## Architecture

See the full diagram and write-up:

- https://github.com/vpeetla-ai/omniforge/blob/main/docs/ARCHITECTURE.md

## Live proof

| | |
|--|--|
| UI | https://omniforge-flame.vercel.app |
| API | https://omniforge-api.onrender.com/health |
| Source | https://github.com/vpeetla-ai/omniforge |

## Trade-offs

| Choice | Gain | Cost |
|--------|------|------|
| Self-contained monorepo | One inspectable flagship | Duplicates some org patterns |
| Task-class routing | Honest multi-LLM story | Cascade complexity + provider keys |
| Mock fallback | Demos always work | Must label mock vs live clearly |
| Browser ASR | Zero GPU for voice-in | Quality varies by browser |

## What we'd do next

- Public clean domain without SSO (`omniforge.vercel.app`)
- Optional server Whisper / TTS
- External MCP server adapters
- Golden eval suite for routing invariants in CI across providers

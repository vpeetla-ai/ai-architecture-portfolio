# Case study: OmniForge — multimodal multi-LLM answer platform

**Live demo:** [omniforge-flame.vercel.app](https://omniforge-flame.vercel.app) · [API](https://omniforge-api.onrender.com)  
**Source:** [github.com/vpeetla-ai/omniforge](https://github.com/vpeetla-ai/omniforge)

## Problem

“Multi-agent” demos often hide a single hardcoded model. Ask with text + screenshot + voice and you need specialized agents, tools, and **task-class routing with proof** — or the architecture claim is empty. The scar is an A/B that can’t show whether routing actually changed the model.

## What we decided

1. **Self-contained monorepo** — one inspectable flagship; no runtime dependency on sibling vpeetla-ai services for the core ask path ([ADR-027](../adr/ADR-027-omniforge-self-contained-multimodal-multi-llm.md)).
2. **Multimodal ingest → planner → parallel agents + MCP → synthesizer**.
3. **Multi-LLM Brain with buckets** — `fast` / `structured` / `reasoning` / `vision`.
4. **Every call emits a `RoutingDecision`** — waterfall proof; A/B single vs routed is first-class.
5. **In-repo FinOps budget + export gate** — refuse to invent cross-service coupling for a demo.

## Architecture

Full diagram: [omniforge/docs/ARCHITECTURE.md](https://github.com/vpeetla-ai/omniforge/blob/main/docs/ARCHITECTURE.md)

## Live proof

| | |
|--|--|
| UI | https://omniforge-flame.vercel.app |
| API | https://omniforge-api.onrender.com/health |
| Source | https://github.com/vpeetla-ai/omniforge |

## Limitations / what we'd do differently

- Self-contained means some org patterns are duplicated — intentional for inspectability, not for long-term DRY.
- Mock fallback keeps demos alive; must stay labeled mock vs live.
- Browser ASR is zero-GPU voice-in; quality varies by browser.
- Next: clean public domain without SSO, optional server Whisper/TTS, external MCP adapters, golden eval suite for routing invariants across providers.

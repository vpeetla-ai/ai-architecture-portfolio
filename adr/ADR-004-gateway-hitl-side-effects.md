# ADR-004: Gateway + HITL for Side-Effecting Tool Calls

**Status:** Accepted  
**Date:** 2026  
**System:** AegisAI Enterprise Agent Platform

## In one breath (panel)

I'd put every irreversible tool call through a gateway — policy, then HITL on the scary ones, signed audit on everything — autonomous agents are fun; *approved* agents are what I'd run.

## Context

Agents that publish, deploy, notify, or hit payment APIs create real operational and compliance risk if execution is fully autonomous. Prompt-only "please don't do bad things" is not a control. Regulated and enterprise programs need an explicit approval path and an audit record you can't quietly edit after the fact.

I refused letting the orchestrator call side-effect tools directly "because the demo needs speed."

## Decision

All side-effecting tool calls pass through the **AegisAI Gateway SDK**:

1. Authenticate agent identity
2. Evaluate OPA policy rules
3. Queue HITL approval for high-risk actions
4. Execute only on allow
5. Write a signed audit log entry

Autonomous agents are exciting. **Approved** agents are production-ready. Demo mode may fail open when the gateway isn't wired; production honesty is `PRODUCTION_STRICT` (ADR-024) — label the difference, don't blur it.

## Integration points

- VAP notify channels (Slack, Telegram, WhatsApp)
- AI Content Factory publish pipeline
- Enterprise RAG ingest HITL
- AegisLoop mission ship gate

## Consequences

**Positive**

- One control plane story across publish / notify / ingest / ship
- HITL sits where the risk is, not as a generic "approve the chat"
- Audit trail is a product requirement, not a nice-to-have log line

**Negative**

- Latency on git push / publish paths — accepted
- Teams must wire the SDK at every side-effect boundary or the split is fiction

## Proof

- [aegisai-enterprise-agent-platform](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform)
- Live: [aegisai-enterprise-agent-platform.vercel.app](https://aegisai-enterprise-agent-platform.vercel.app)

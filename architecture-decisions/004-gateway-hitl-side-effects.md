# ADR-004: Gateway + HITL for Side-Effecting Tool Calls

**Status:** Accepted  
**Date:** 2026  
**System:** AegisAI Enterprise Agent Platform

## Context

Agents that call external tools (publish, deploy, notify, payment APIs) create operational and compliance risk if execution is fully autonomous. Regulated and enterprise programs require explicit approval paths and immutable audit records.

## Decision

All side-effecting tool calls pass through the **AegisAI Gateway SDK**:

1. Authenticate agent identity
2. Evaluate OPA policy rules
3. Queue HITL approval for high-risk actions
4. Execute only on allow
5. Write signed audit log entry

Autonomous agents are exciting. **Approved** agents are production-ready.

## Integration points

- VAP notify channels (Slack, Telegram, WhatsApp)
- AI Content Factory publish pipeline
- Enterprise RAG ingest HITL
- AegisLoop mission ship gate

## Proof

- [aegisai-enterprise-agent-platform](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform)
- Live: [aegisai-enterprise-agent-platform.vercel.app](https://aegisai-enterprise-agent-platform.vercel.app)

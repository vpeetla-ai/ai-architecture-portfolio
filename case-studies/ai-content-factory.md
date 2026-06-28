# AI Content Factory — Governed Content Pipeline

**Domain:** Content automation · Multi-agent · HITL publish  
**Live demo:** [ai-content-factory-iota.vercel.app](https://ai-content-factory-iota.vercel.app)  
**Source:** [github.com/vpeetla-ai/ai-content-factory](https://github.com/vpeetla-ai/ai-content-factory)

## Problem

Multi-platform content generation at scale requires research, drafting, human review, and governed publish — not autonomous posting.

## Architecture

```text
Research Agent → Draft Agents (×5 platforms) → HITL Review → AegisAI Gateway → OAuth Publish
                                                      ↑
                                              Clerk auth · Cron scheduler
```

## Key decisions

- LangGraph pipeline with explicit HITL node before publish
- AegisAI gateway blocks publish until policy allows
- LinkedIn and X OAuth when tokens configured

## Stack

FastAPI · LangGraph · Next.js · Clerk · Vercel · Render

## Related

Integrates with [AegisAI](./aegisai-agent-governance.md) gateway — end-to-end governed output layer of the reference stack.

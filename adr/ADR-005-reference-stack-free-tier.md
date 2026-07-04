# ADR-005: Reference Stack on Free-Tier Infrastructure

**Status:** Accepted  
**Date:** 2026  
**Scope:** All 10 live portfolio demos

## Context

Architecture portfolios often show diagrams without deployable proof. Enterprise architects need inspectable systems — but not every builder has cloud budget on day one.

## Decision

Deploy the governed AI reference stack on **free-tier boundaries** with explicit service separation:

| Layer | Service |
|-------|---------|
| UI | Vercel |
| API | Render |
| LLM | Groq (and optional OpenAI) |
| Vectors | Qdrant Cloud (optional) |
| Cache | Upstash (optional) |
| Auth | Clerk / Supabase where needed |

Each repo maintains production-style boundaries (FastAPI services, Next.js UI, env-based config) so teams can fork and scale without rewriting architecture.

## Trade-off

Free tiers cold-start and rate-limit — acceptable for **reference implementations** and hiring-panel technical review. Production deployments swap providers without changing service boundaries.

## Proof

All demos linked from [venkat-ai.com/work](https://venkat-ai.com/work)

# ADR-005: Reference Stack on Free-Tier Infrastructure

**Status:** Accepted  
**Date:** 2026  
**Scope:** All 10 live portfolio demos

## In one breath (panel)

I'd ship inspectable systems on free-tier PaaS with real service boundaries — diagrams without a URL aren't architecture, and free-tier cold starts aren't an enterprise SLO.

## Context

Architecture portfolios often stop at diagrams. Enterprise architects want something they can click, fork, and poke — but not every builder has cloud budget on day one. I also refused dressing free-tier demos as production SLOs. Cold starts and rate limits are real; honesty is the product.

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

Each repo keeps production-style boundaries (FastAPI services, Next.js UI, env-based config) so a team can fork and scale without rewriting the architecture. IaC on AWS/GCP exists as an alternate path for proof of ownership (ADR-015) — not as the default demo host.

## Consequences

**Positive**

- Live demos reviewers can actually open
- Boundaries survive a provider swap later
- Cost stays near zero for the default portfolio path

**Negative**

- Free tiers cold-start and rate-limit — fine for **reference implementations** and hiring-panel review; not for claiming enterprise uptime
- Ephemeral disks and spin-down are Render facts of life — don't pretend otherwise

## Proof

All demos linked from [venkat-ai.com/work](https://venkat-ai.com/work)

# From Multi-Agent OS to Agent Governance

**Stub → canonical essay.** VAP and AegisAI are complementary layers — not competing products. This page is the portfolio pointer; the full argument lives in the essay linked below.

## Canonical essay (read this)

- **Full essay (GitHub):** [ai-content-factory/docs/content/from-multi-agent-os-to-agent-governance.md](https://github.com/vpeetla-ai/ai-content-factory/blob/main/docs/content/from-multi-agent-os-to-agent-governance.md)
- **Portfolio blog:** [venkat-ai.com/blog](https://venkat-ai.com/blog)
- **Substack:** [venkatapeetla.substack.com](https://venkatapeetla.substack.com)

## Problem (one breath)

Most teams follow demo → real tools → no governance → panic. I’d rather split the questions early: **what should agents do?** (orchestration) vs **what are they allowed to do?** (gateway, policy, HITL, audit).

## What we decided

1. **VAP for orchestration, AegisAI for governance** — wire through the Gateway SDK at side-effect boundaries ([ADR-001](../adr/ADR-001-orchestration-vs-governance-split.md)).
2. **Refuse merging policy into the graph** — demos get simpler; production gets unauditable.
3. **Prove the spine end-to-end** — stranger-replayable golden path, not slide claims ([golden-path-spine-e2e.md](./golden-path-spine-e2e.md)).

## Live proof

| System | Demo |
|--------|------|
| VAP | [venkat-ai-platform.vercel.app](https://venkat-ai-platform.vercel.app) |
| AegisAI | [aegisai-enterprise-agent-platform.vercel.app](https://aegisai-enterprise-agent-platform.vercel.app) |

**Spine golden path (S4):** [GOLDEN_PATH.md](../docs/GOLDEN_PATH.md) · [run numbers](./golden-path-spine-e2e.md) · [latest artifact](../docs/artifacts/golden-path/latest.json)

**Signal pack (S5):** [ADR post calendar](../docs/S5_ADR_POST_CALENDAR.md) · [S5 hub](../docs/S5_SIGNAL_CONVERSION.md) · Publish checklist in the [full essay](https://github.com/vpeetla-ai/ai-content-factory/blob/main/docs/content/from-multi-agent-os-to-agent-governance.md)

## Limitations

This stub doesn’t replace the essay — open the GitHub link for the full narrative, diagrams, and publish checklist.

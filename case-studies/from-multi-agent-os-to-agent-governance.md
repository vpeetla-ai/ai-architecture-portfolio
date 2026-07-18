# From Multi-Agent OS to Agent Governance

**Canonical essay** explaining why VAP and AegisAI are complementary layers — not competing products.

## Read the full essay

- **GitHub (full):** [ai-content-factory/docs/content/from-multi-agent-os-to-agent-governance.md](https://github.com/vpeetla-ai/ai-content-factory/blob/main/docs/content/from-multi-agent-os-to-agent-governance.md)
- **Portfolio:** [venkat-ai.com/blog](https://venkat-ai.com/blog)
- **Substack:** [venkatapeetla.substack.com](https://venkatapeetla.substack.com)

## Summary

Most teams follow: demo → real tools → no governance → panic.

**VAP** answers *what agents should do* (orchestration). **AegisAI** answers *what they are allowed to do* (gateway, policy, HITL, audit). Production requires both — wired through the Gateway SDK at side-effect boundaries.

## Related ADR

[ADR-001: Orchestration vs governance split](../adr/ADR-001-orchestration-vs-governance-split.md)

## Live proof

| System | Demo |
|--------|------|
| VAP | [venkat-ai-platform.vercel.app](https://venkat-ai-platform.vercel.app) |
| AegisAI | [aegisai-enterprise-agent-platform.vercel.app](https://aegisai-enterprise-agent-platform.vercel.app) |

**Spine golden path (S4):** [GOLDEN_PATH.md](../docs/GOLDEN_PATH.md) · [case study + run numbers](./golden-path-spine-e2e.md) · [latest artifact](../docs/artifacts/golden-path/latest.json)

**Signal pack (S5):** [ADR post calendar](../docs/S5_ADR_POST_CALENDAR.md) · [S5 hub](../docs/S5_SIGNAL_CONVERSION.md) · Publish checklist lives in the [full essay](https://github.com/vpeetla-ai/ai-content-factory/blob/main/docs/content/from-multi-agent-os-to-agent-governance.md)

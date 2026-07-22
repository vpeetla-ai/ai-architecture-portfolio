# FinOps ROI one-pager (P4)

**Audience:** hiring managers / AI platform leads  
**Proof services:** [agent-finops](https://github.com/vpeetla-ai/agent-finops) · [aegis-llm-gateway](https://github.com/vpeetla-ai/aegis-llm-gateway) · [aegis-semantic-cache](https://github.com/vpeetla-ai/aegis-semantic-cache)

## Decision

Treat **cost as an architectural constraint**, not a dashboard afterthought: meter agent usage as a shared service, route via a gateway that can record provider/tier, and cache when safe.

## What a stranger can replay

From the [golden path](./GOLDEN_PATH.md) latest artifact:

| Signal | Typical value |
|--------|----------------|
| FinOps `/v1/usage` | `breached=false` with `cost_usd` recorded |
| AegisAI gateway | `approval_required` stops unpaid deploy side effects |
| LLM gateway posture | stub/BYOK modes labeled (fail-open demo honesty) |

Exact numbers: [`docs/artifacts/golden-path/latest.json`](./artifacts/golden-path/latest.json).

## ROI narrative (board-safe)

1. **Prevented incidents** — HITL on deploy-class tools converts “agent shipped to prod” into an approval ticket.  
2. **Attributed spend** — FinOps meters by agent/scope instead of a single opaque LLM bill.  
3. **Avoided duplicate inference** — semantic cache + routing contract (apps select, gateway enforces/records).  
4. **Honest demos** — cold free-tier and stub modes are labeled so ROI claims aren’t vapor.

## What we do **not** claim

- Dollar savings vs a Fortune-500 baseline (no customer production spend in this portfolio).  
- Always-on multi-cloud FinOps control tower.

## Links

- Hire: https://venkat-ai.com/hire  
- Technical review: https://venkat-ai.com/technical-review  
- ADR-011 FinOps standalone · ADR-028/029 control plane + routing

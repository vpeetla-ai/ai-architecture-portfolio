# Case study — AWS ephemeral control-plane receipts (P2)

**Program:** [TOP1PCT_90SCORE_60DAY.md](../docs/TOP1PCT_90SCORE_60DAY.md)  
**Honesty:** Receipt-backed free-tier / short-lived proof — **not** an always-on multi-cloud production fleet. PaaS (Render) remains the always-on spine under the ~$45/mo ceiling.

## Problem

Principal panels want real VPC/ECS/ALB/RDS wiring. Leaving an ALB up forever blows the budget (~$36+/mo) and turns “cloud proof” into a standing tax. The scar is choosing between “no AWS story” and “always-on bill we can’t afford.”

## What we decided

1. **AWS owns the enterprise control-plane story** in the org split ([CLOUD_FREE_TIER_SPLIT.md](../docs/CLOUD_FREE_TIER_SPLIT.md)).
2. **Stand-up → verify → tear-down** on AegisAI Terraform ([deploy/terraform/aws](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform/tree/main/deploy/terraform/aws)) — [ADR-015](../adr/ADR-015-real-aws-gcp-infra-phase-c.md).
3. **GCP owns serverless FinOps + ERAG Cloud Run** — [gcp-serverless-ai-platform-receipt.md](./gcp-serverless-ai-platform-receipt.md).
4. **Refuse always-on EKS/ALB for the portfolio ceiling.**

| Option | Monthly | Panel value | Fits $45 with Starters? |
|--------|--------:|-------------|-------------------------|
| 3–4 Render Starters | ~28 | Always-on review path | Yes |
| Full AWS stack left up | ~36–46+ | Strong cloud story | **No** |
| Apply → health → destroy + receipts | 0–10 | Cloud & infra skill proof | Yes |

## Architecture (ephemeral)

```text
Internet → ALB → ECS Fargate (AegisAI API) → RDS Postgres
                ↘ Secrets Manager / IAM task role
```

Source of truth: AegisAI `deploy/terraform/aws/*.tf` + repo ADR-0006 (PaaS vs IaC).

## Live proof / how to operate

- Runbook: [docs/P2_AWS_RECEIPT_RUNBOOK.md](../docs/P2_AWS_RECEIPT_RUNBOOK.md)
- Evidence pack after a run (under `docs/artifacts/aws-receipts/`, no secrets):
  1. Redacted `terraform apply` summary
  2. `curl` ALB `/health` (or ECS task health)
  3. Cost Explorer / free-tier screenshot (same day)
  4. `terraform destroy` (or `desired-count=0` + RDS stop) with timestamp
- Continuous HITL/gateway proof stays on the live AegisAI PaaS demo: [aegisai-agent-governance.md](./aegisai-agent-governance.md)

### Reviewer talking points

- “Spine demos are always-on on Render Starter; AWS is the IaC reference I stand up for a panel and tear down the same day.”
- “ALB fixed cost is why we don’t leave it up — ADR-015 / AegisAI ADR-0006.”

## Limitations / what we'd do differently

- Without a fresh receipt pack, don’t claim “currently running on AWS.”
- Ephemeral RDS means data doesn’t persist across panel weeks — by design.
- I’d keep a dated checklist in the runbook so a stranger can reproduce without Slack lore.

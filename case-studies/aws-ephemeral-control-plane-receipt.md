# Case study — AWS ephemeral control-plane receipts (P2)

**Program:** [TOP1PCT_90SCORE_60DAY.md](../docs/TOP1PCT_90SCORE_60DAY.md)  
**Honesty:** This is **receipt-backed free-tier / short-lived proof**, not an always-on multi-cloud production fleet. PaaS (Render) remains the always-on spine under the ~$45/mo ceiling.

## Decision

Use the existing AegisAI Terraform path ([deploy/terraform/aws](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform/tree/main/deploy/terraform/aws)) as a **stand-up → verify → tear-down** exercise so Principal panels can see real AWS VPC/ECS/ALB/RDS wiring without leaving a $36+/mo ALB bill running.

## Why not always-on EKS?

| Option | Monthly | Panel value | Fits $45 with Starters? |
|--------|--------:|-------------|-------------------------|
| 3–4 Render Starters | ~28 | Always-on review path | Yes |
| Full AWS stack left up | ~36–46+ | Strong cloud story | **No** (blows budget) |
| Apply → health → destroy + receipts | 0–10 | Cloud & infra skill proof | Yes |

## Operator runbook

See [docs/P2_AWS_RECEIPT_RUNBOOK.md](../docs/P2_AWS_RECEIPT_RUNBOOK.md).

### Evidence pack (attach after a run)

1. Redacted `terraform apply` summary (resource counts, region)
2. `curl` of ALB `/health` (or ECS task health)
3. Cost Explorer / free-tier usage screenshot (same day)
4. `terraform destroy` completion (or `desired-count=0` + RDS stop) with timestamp

Place binaries/screenshots under `docs/artifacts/aws-receipts/` (git-lfs or private) and link from this page without secrets.

## Architecture (ephemeral)

```text
Internet → ALB → ECS Fargate (AegisAI API) → RDS Postgres
                ↘ Secrets Manager / IAM task role
```

Source of truth: AegisAI `deploy/terraform/aws/*.tf` + ADR-0006 (PaaS vs IaC tradeoffs) in that repo.

## Reviewer talking points

- “Spine demos are always-on on Render Starter; AWS is the IaC reference I can stand up for a panel and tear down the same day.”
- “ALB fixed cost is why we don’t leave it up — ADR-015 / AegisAI ADR-0006 document that tradeoff.”
- Point to live AegisAI PaaS control plane for continuous HITL/gateway proof.

## Related

- Org [ADR-015](../adr/ADR-015-real-aws-gcp-infra-phase-c.md)
- [NIST one-pager](../docs/NIST_AI_RMF_ONE_PAGER.md)
- [FinOps ROI one-pager](../docs/FINOPS_ROI_ONE_PAGER.md)

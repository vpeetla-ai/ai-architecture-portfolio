# P2 — AWS receipt runbook (free-tier / tear-down)

**Budget rule:** do not leave ALB + RDS running overnight. Target wall-clock &lt; 2 hours apply→verify→destroy.

## Start a dated checklist

```bash
./scripts/init_cloud_receipt.sh aws
# → docs/artifacts/aws-receipts/YYYYMMDD-checklist.md
```

## Prerequisites

```bash
aws sts get-caller-identity
terraform version
docker version
cd ~/aegisai-enterprise-agent-platform/deploy/terraform/aws
```

Set a hard budget alarm in AWS Billing (≥$5 anomalous) before first apply.

## Minimal evidence path (preferred under $45)

If full ECS+ALB+RDS is too expensive even for a short window:

1. `terraform apply -target=aws_ecr_repository.aegisai`
2. Build/push image once
3. Screenshot ECR repo + image digest
4. `terraform destroy -target=aws_ecr_repository.aegisai` (or destroy all)
5. File receipts under `docs/artifacts/aws-receipts/` with date stamp

This still proves IaC + container registry muscle; narrate that Fargate/ALB path exists in-repo for longer panel labs.

## Full path (same-day only)

Follow [AegisAI AWS README](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform/blob/main/deploy/terraform/aws/README.md):

1. `terraform init`
2. Apply ECR → push image → apply rest
3. `curl "$(terraform output -raw alb_url)/health"`
4. Capture Cost Explorer screenshot
5. `terraform destroy` **before** end of day

## Checklist

- [ ] Budget alarm on
- [ ] Apply log saved (redact account ids if public)
- [ ] Health curl OK
- [ ] Destroy complete
- [ ] Case study links updated
- [ ] technical-review / hire link live

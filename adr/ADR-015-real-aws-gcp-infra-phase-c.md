# ADR-015: Genuine Hands-On AWS + GCP Infra (Phase C)

## Status

Accepted — 2026-07-05

## Context

Every repo in this org deploys to Vercel/Render PaaS ([ADR-005](./ADR-005-reference-stack-free-tier.md)),
which is the right default for iteration speed — but a full org-wide audit found zero
Terraform, Kubernetes, or any cloud-infrastructure-as-code evidence anywhere. This directly
undercut the portfolio's own career narrative, which claims "AWS, OCI, DevOps — platform
ownership" 2015–2020, with no corresponding GitHub evidence today. Phase C of the top-1% AI
Architect program closed this gap with genuinely operated infrastructure — real
`terraform apply`, real verification against live endpoints, real `terraform destroy` — not
Terraform written and never run.

## Decision

Two repos got a real, alternative deploy path alongside (not replacing) their existing Render
PaaS deployment:
- **`agent-finops` → GCP**: Cloud Run (scale-to-zero) + Cloud SQL (`db-f1-micro`, no HA) +
  Artifact Registry + Secret Manager + a least-privilege service account. See
  [agent-finops ADR-0002](https://github.com/vpeetla-ai/agent-finops/blob/main/docs/adr/0002-paas-vs-iac-deploy-tradeoffs.md).
- **`aegisai-enterprise-agent-platform` → AWS**: VPC (public subnets only, no NAT Gateway) +
  ECS Fargate + Application Load Balancer + RDS Postgres (`db.t4g.micro`, single-AZ) + IAM
  execution/task roles + Secrets Manager. Chosen as the AWS target because it's the flagship
  governance control plane — the most narratively important service to show on a classic
  enterprise AWS pattern. See [aegisai ADR-0006](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform/blob/main/adr/0006-paas-vs-iac-deploy-tradeoffs.md).

Both were built for lowest cost on purpose (scale-to-zero / smallest burstable tiers / no HA /
no NAT Gateway) and operated as **stand up → verify → tear down**, not left running — real
cloud spend is temporary and disclosed, not a permanent second deployment of either service.

## Consequences

### Positive
- **Both clouds fully verified working, then fully torn down**, confirmed via each provider's
  own CLI (`gcloud run services list`, `aws rds describe-db-instances`, etc. all returned
  empty after teardown):
  - GCP: real budget breach detected against a real Cloud SQL-backed ledger through a live
    Cloud Run URL.
  - AWS: a real `POST /api/orchestrators/website-build/run` completed successfully against a
    live ECS Fargate task, with `/health` confirming genuine RDS-backed persistence
    (`"mode":"postgres"`, not a SQLite fallback).
- **Real deployment surfaced real bugs neither code review nor local testing had caught**,
  each disclosed and fixed rather than worked around: agent-finops's Dockerfile ignored Cloud
  Run's injected `PORT`; its API key secret defaulted to the guessable placeholder string
  `"unset"` for a publicly-invokable service; aegisai's Dockerfile couldn't build at all (no
  `git` in the base image, needed for the `agent-finops` git+https dependency — this had
  apparently never been built as a real container image before); its ECR repo needed
  `force_delete` to actually tear down. Two additional operational gotchas were hit and
  resolved live: Cloud Run doesn't roll a new revision just because a referenced secret's
  "latest" version changes, and both providers showed a brief eventual-consistency delay
  between creating a secret and a compute resource successfully reading it.
- Now genuine, checkable evidence of AWS + GCP infrastructure ownership (VPC design, IAM,
  container orchestration, load balancing, managed database provisioning) backing the
  portfolio's career claims, not just Terraform files that were never run.

### Negative
- Both deploy paths are alternates to the existing Render setup, not the new default — running
  either continuously would cost real money (~$7–10/mo GCP, ~$20–46/mo AWS) for no operational
  benefit over the existing free-tier PaaS deployments; the value here is demonstrated
  capability and a real trade-off ADR, not a permanent infrastructure change.
- AWS's public-subnets-only topology (no NAT Gateway) is a deliberate cost trade-off, not the
  default enterprise pattern — documented explicitly in ADR-0006 rather than presented as
  unqualified best practice.

## References
- `agent-finops/deploy/terraform/gcp/`, `agent-finops/docs/adr/0002-paas-vs-iac-deploy-tradeoffs.md`
- `aegisai-enterprise-agent-platform/deploy/terraform/aws/`, `aegisai-enterprise-agent-platform/adr/0006-paas-vs-iac-deploy-tradeoffs.md`
- [ADR-005: Reference stack on free tier](./ADR-005-reference-stack-free-tier.md)

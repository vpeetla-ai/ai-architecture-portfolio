# ADR-015: Genuine Hands-On AWS + GCP Infra (Phase C)

## Status

Accepted — 2026-07-05

## In one breath (panel)

I'd prove AWS and GCP ownership with real `terraform apply`, live endpoint checks, then `terraform destroy` — Terraform that never ran isn't platform evidence, and free-tier PaaS stays the default demo host.

## Context

Every repo here deploys to Vercel/Render PaaS ([ADR-005](./ADR-005-reference-stack-free-tier.md))
— right default for iteration speed. An org-wide audit found zero Terraform, Kubernetes, or
cloud-IaC evidence anywhere. That undercut the portfolio career narrative ("AWS, OCI, DevOps —
platform ownership" 2015–2020) with no matching GitHub proof today. Phase C closed the gap with
genuinely operated infrastructure — real apply, real verification against live endpoints, real
destroy — not Terraform written and never run.

I refused leaving `.tf` files as decoration, and refused making expensive always-on cloud the
new default when free-tier PaaS already serves demos.

## Decision

Two repos got a real alternate deploy path alongside (not replacing) their Render PaaS deploy:
- **`agent-finops` → GCP**: Cloud Run (scale-to-zero) + Cloud SQL (`db-f1-micro`, no HA) +
  Artifact Registry + Secret Manager + least-privilege service account. See
  [agent-finops ADR-0002](https://github.com/vpeetla-ai/agent-finops/blob/main/docs/adr/0002-paas-vs-iac-deploy-tradeoffs.md).
- **`aegisai-enterprise-agent-platform` → AWS**: VPC (public subnets only, no NAT Gateway) +
  ECS Fargate + ALB + RDS Postgres (`db.t4g.micro`, single-AZ) + IAM execution/task roles +
  Secrets Manager. Chosen because it's the flagship governance control plane — the most
  narratively important service to show on a classic enterprise AWS pattern. See
  [aegisai ADR-0006](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform/blob/main/adr/0006-paas-vs-iac-deploy-tradeoffs.md).

Both built for lowest cost on purpose (scale-to-zero / smallest burstable tiers / no HA / no
NAT) and operated as **stand up → verify → tear down** — temporary disclosed spend, not a
permanent second deployment.

## Consequences

### Positive
- **Both clouds verified working, then fully torn down**, confirmed via each provider's CLI
  (`gcloud run services list`, `aws rds describe-db-instances`, etc. empty after teardown):
  - GCP: real budget breach against a real Cloud SQL-backed ledger through a live Cloud Run URL.
  - AWS: real `POST /api/orchestrators/website-build/run` completed on live ECS Fargate; `/health`
    confirmed RDS-backed persistence (`"mode":"postgres"`, not SQLite fallback).
- **Real deployment surfaced real bugs** neither code review nor local testing caught — fixed,
  not worked around: agent-finops Dockerfile ignored Cloud Run's `PORT`; API key secret defaulted
  to guessable `"unset"` on a publicly invokable service; aegisai Dockerfile couldn't build (no
  `git` in base image, needed for `agent-finops` git+https dep — apparently never built as a real
  container before); ECR needed `force_delete` to tear down. Live gotchas: Cloud Run doesn't roll
  a new revision just because a referenced secret's "latest" version changed; both providers had
  brief eventual-consistency delay between creating a secret and compute reading it.
- Checkable evidence of AWS + GCP ownership (VPC, IAM, containers, LB, managed DB) backing the
  career claims — not `.tf` that never ran.

### Negative
- Both paths are alternates to Render, not the new default — continuous run costs real money
  (~$7–10/mo GCP, ~$20–46/mo AWS) for no operational benefit over free-tier PaaS. Value is
  demonstrated capability and a real trade-off ADR, not a permanent infra change. **P vs O:**
  operated once as proof; not "always-on production on AWS/GCP."
- AWS public-subnets-only (no NAT) is a deliberate cost trade-off, not the default enterprise
  pattern — documented in ADR-0006, not sold as unqualified best practice.

## References
- `agent-finops/deploy/terraform/gcp/`, `agent-finops/docs/adr/0002-paas-vs-iac-deploy-tradeoffs.md`
- `aegisai-enterprise-agent-platform/deploy/terraform/aws/`, `aegisai-enterprise-agent-platform/adr/0006-paas-vs-iac-deploy-tradeoffs.md`
- [ADR-005: Reference stack on free tier](./ADR-005-reference-stack-free-tier.md)

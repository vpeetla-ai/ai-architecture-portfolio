# Case study — GCP serverless AI platform receipts

**Program:** [CLOUD_FREE_TIER_SPLIT.md](../docs/CLOUD_FREE_TIER_SPLIT.md) · [TOP1PCT_90SCORE_60DAY.md](../docs/TOP1PCT_90SCORE_60DAY.md)  
**Honesty:** Scale-to-zero Cloud Run is Always Free–friendly at demo traffic. Cloud SQL (FinOps full stack) is **ephemeral** — destroy or stop when not verifying. This page is a receipt stub, not an always-on GCP fleet.

## Problem

Panels ask “have you actually run this on a cloud?” PaaS demos alone leave a gap. The scar I’d refuse: leaving Cloud SQL up “for the portfolio” and calling a free-tier story while the bill grows.

## What we decided

1. **GCP owns serverless AI platform proof** — Enterprise RAG and Agent FinOps on Cloud Run ([ADR-015](../adr/ADR-015-real-aws-gcp-infra-phase-c.md)).
2. **AWS keeps the enterprise control-plane story** — see [aws-ephemeral-control-plane-receipt.md](./aws-ephemeral-control-plane-receipt.md).
3. **Dual-cloud without dual always-on bills** — stand up, verify, tear down; Render stays the always-on spine.

| Service | Path | Mode |
|---------|------|------|
| Enterprise RAG | Cloud Run + memory backend | Can idle at ~$0 |
| Agent FinOps | Cloud Run + optional Cloud SQL | Tear down SQL between sessions |

## Live proof / how to operate

- Operator runbook: [P2_GCP_RECEIPT_RUNBOOK.md](../docs/P2_GCP_RECEIPT_RUNBOOK.md)
- Evidence under `docs/artifacts/gcp-receipts/` (redact project numbers if public):
  1. `gcloud run services describe` / curl `/health`
  2. Cost / free-tier screenshot
  3. `terraform destroy` or confirmation `minScale=0` and SQL stopped
- Terraform paths: agent-finops `deploy/terraform/gcp` · enterprise_rag_platform `deploy/gcp/cloudrun`

## Limitations / what we'd do differently

- Receipts expire; a missing artifact means “not verified this week,” not “imaginary infra.”
- Memory backends on Cloud Run are for demo/receipt posture — not a claim of production Qdrant SLOs.
- I’d keep SQL stopped by default in any checklist a stranger can follow.

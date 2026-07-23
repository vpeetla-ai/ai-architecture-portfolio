# Case study — GCP serverless AI platform receipts

**Program:** [CLOUD_FREE_TIER_SPLIT.md](../docs/CLOUD_FREE_TIER_SPLIT.md) · [TOP1PCT_90SCORE_60DAY.md](../docs/TOP1PCT_90SCORE_60DAY.md)  
**Honesty:** Scale-to-zero Cloud Run is **Always Free–friendly** at demo traffic. Cloud SQL (FinOps full stack) is **ephemeral** — destroy or stop when not verifying.

## Decision

Put **serverless AI platform** proof on **GCP**:

| Service | Path | Mode |
|---------|------|------|
| Enterprise RAG | Cloud Run + memory backend | Can idle at ~$0 |
| Agent FinOps | Cloud Run + optional Cloud SQL | Tear down SQL between sessions |

AWS keeps the **enterprise control-plane** (AegisAI ECS) story — see [aws-ephemeral-control-plane-receipt.md](./aws-ephemeral-control-plane-receipt.md).

## Why this split

- GCP Cloud Run maps cleanly to “AI platform / agent metering / RAG API” interviews.  
- AWS VPC+ALB+ECS maps to “enterprise governance plane” interviews.  
- Dual-cloud without dual always-on bills.

## Operator runbook

[P2_GCP_RECEIPT_RUNBOOK.md](../docs/P2_GCP_RECEIPT_RUNBOOK.md)

## Evidence pack

Store under `docs/artifacts/gcp-receipts/` (redact project numbers if public):

1. `gcloud run services describe` / curl `/health`  
2. Cost / free-tier screenshot  
3. `terraform destroy` or confirmation `minScale=0` and SQL stopped  

## Related

- agent-finops `deploy/terraform/gcp`  
- enterprise_rag_platform `deploy/gcp/cloudrun`  
- ADR-015

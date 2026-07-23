# P2 — GCP receipt runbook (Always Free–friendly)

**Budget rule:** Prefer **Cloud Run only** (no Cloud SQL) for ~$0 idle. If you enable FinOps Cloud SQL, destroy/stop the same day.

## Start a dated checklist

```bash
./scripts/init_cloud_receipt.sh gcp
# → docs/artifacts/gcp-receipts/YYYYMMDD-checklist.md
```

## Path A — Enterprise RAG on Cloud Run (~$0 idle)

```bash
# Demo:
cd ~/enterprise_rag_platform/deploy/gcp/cloudrun
# See README.md for terraform apply + image push

# Strict (recommended while Render Free / Strict twin pending):
cd ~/enterprise_rag_platform && ./scripts/deploy_strict_gcp.sh <PROJECT_ID>

curl -sS "$(cd deploy/gcp/cloudrun && terraform output -raw service_url)/health" | python3 -m json.tool
# Demo → review_mode=demo · Strict → review_mode=strict
```

Leave `min_instance_count = 0`. Cold starts are OK for **cloud receipts**; panel warm path returns to Render after Starter.

## Path B — Agent FinOps full stack (tear-down)

Follow [agent-finops GCP README](https://github.com/vpeetla-ai/agent-finops/blob/main/deploy/terraform/gcp/README.md):

1. `terraform apply` → curl `/health` → exercise a meter call  
2. Screenshot billing / free tier  
3. `terraform destroy` **before** overnight  

## Checklist

- [ ] Budget alert on GCP project  
- [ ] Health curl saved  
- [ ] Destroy or SQL stopped  
- [ ] Files in `docs/artifacts/gcp-receipts/`  
- [ ] Link from CLOUD_FREE_TIER_SPLIT progress

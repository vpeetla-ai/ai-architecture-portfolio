# P2 — GCP receipt runbook (Always Free–friendly)

**Budget rule:** Prefer **Cloud Run only** (no Cloud SQL) for ~$0 idle. If you enable FinOps Cloud SQL, destroy/stop the same day.

## Path A — Enterprise RAG on Cloud Run (~$0 idle)

```bash
cd ~/enterprise_rag_platform/deploy/gcp/cloudrun
# See README.md in that folder for terraform apply + image push
curl -sS "$(terraform output -raw service_url)/health" | python3 -m json.tool
# Expect review_mode=demo (or strict if you set PRODUCTION_STRICT)
```

Leave `min_instance_count = 0`. Cold starts are OK for **cloud receipts**; panel warm path stays on Render.

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

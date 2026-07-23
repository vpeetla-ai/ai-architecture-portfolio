# Cloud free-tier split — AWS + GCP (Principal portfolio)

**Status:** ACTIVE · 2026-07-22  
**Parent:** [TOP1PCT_90SCORE_60DAY.md](./TOP1PCT_90SCORE_60DAY.md) · [ADR-015](../adr/ADR-015-real-aws-gcp-infra-phase-c.md)  
**Budget rule:** Render Starters (~$21–28) buy **warm panel spine** (deferred 1–2 days — see [RENDER_FREE_INTERIM.md](./RENDER_FREE_INTERIM.md)); cloud free tiers buy **infra skill proof** — not a second always-on fleet.

**Interim (owner choice 2026-07-22):** stay on **Render Free** for now; prioritize AWS/GCP receipt labs + Strict local/GCP + signal.

## Principle

| Concern | Home | Why |
|---------|------|-----|
| Hostile 15‑min review (warm `/health`) | **Render Starter** spine | Cold starts kill Principal trust |
| Cloud & infra skill (IaC, IAM, serverless, receipts) | **AWS + GCP free / tear-down** | Multi-cloud narrative without $100+/mo burn |
| Freeze | No new product repos | Only alternate deploy paths |

## Canonical assignment

### AWS — enterprise control-plane narrative

| Repo | Deploy path | Free-tier mode | Panel story |
|------|-------------|----------------|-------------|
| **aegisai-enterprise-agent-platform** | [`deploy/terraform/aws`](https://github.com/vpeetla-ai/aegisai-enterprise-agent-platform/tree/main/deploy/terraform/aws) | **Ephemeral** apply→verify→destroy (ALB/ECS/RDS not Always Free) | Classic VPC + Fargate + ALB + RDS governance plane |
| **aegis-llm-gateway** *(optional later)* | Document-only / future Lambda | Always Free Lambda eligible | “Apps select; gateway enforces” on AWS edge |

**Do not** leave AegisAI AWS stack up overnight — ALB alone breaks a $20–30 ceiling.

### GCP — serverless AI platform narrative

| Repo | Deploy path | Free-tier mode | Panel story |
|------|-------------|----------------|-------------|
| **agent-finops** | [`deploy/terraform/gcp`](https://github.com/vpeetla-ai/agent-finops/tree/main/deploy/terraform/gcp) | Cloud Run ≈$0 at demo traffic; **Cloud SQL tear-down** (~$7–10 if left up) | Metering ledger on GCP |
| **enterprise_rag_platform** | [`deploy/gcp/cloudrun`](https://github.com/vpeetla-ai/enterprise_rag_platform/tree/main/deploy/gcp/cloudrun) | **Cloud Run scale-to-zero** + memory backend ≈ **Always Free** | Access-before-ranking on GCP; Render remains primary warm Demo/Strict |

### Stay on Render / Vercel (primary live demos)

| Repo | Why not force to cloud free tier |
|------|----------------------------------|
| **venkat-ai-platform** | Primary orchestration demo; needs warm Starter for panels |
| **ai-content-factory** | Clerk + Postgres product path; Vercel UI |
| **venkat-ai-portfolio** | Static/Next hire funnel on Vercel |
| Pattern stubs / labs | Teaching only — no cloud bill |

## Operating modes (say out loud in interviews)

```text
Mode A0 — Panel day (Free interim): Render Free + labeled cold starts; Strict via local or GCP
Mode A  — Panel day (warm):         Render Starters for VAP + AegisAI + ERAG (+ Strict)  ← after upgrade
Mode B  — Cloud receipts day:       AWS AegisAI apply→destroy  OR  GCP FinOps/ERAG apply→verify→(destroy|scale-0)
Mode C  — Idle Always Free:         GCP Cloud Run min_instances=0 for ERAG lite / FinOps without SQL
```

Never claim Mode A0/B/C are “production multi-cloud always-on.” Mode A0 is honest Free-tier demoing until Starters land ([RENDER_FREE_INTERIM.md](./RENDER_FREE_INTERIM.md)).

## Cost envelopes

| Envelope | What fits |
|----------|-----------|
| **$0 idle** | GCP Cloud Run scale-to-zero (ERAG memory backend); no Cloud SQL; no ALB |
| **~$20–30/mo** | Prefer **Render Starters for spine**; cloud only as receipt lab |
| **~$7–10 spike** | agent-finops Cloud SQL left up by mistake — destroy ASAP |
| **~$20–46 spike** | AegisAI AWS left up — destroy same day |

## Reviewer talking points (30 seconds)

1. **Until Starter:** “Spine is on Render Free — cold starts labeled on spine-health; Strict JWT is local or GCP Cloud Run.”  
2. **After Starter:** “Live demos are warm on Render Starter — that’s the 15‑minute path.”  
3. “AWS owns the governance control-plane IaC story (AegisAI ECS) — stand up, prove, tear down.”  
4. “GCP owns serverless FinOps + RAG Cloud Run — Always Free friendly when SQL stays off.”  
5. “Split is intentional: enterprise pattern on AWS, serverless AI platform on GCP — not accidental sprawl.”

## Exit criteria (P2 dual-cloud)

- [x] This split doc published  
- [x] ERAG GCP Cloud Run path in-repo  
- [x] Case study + hire links updated  
- [ ] Owner: one AWS receipt run (AegisAI) **or** one GCP receipt run (FinOps or ERAG) with files under `docs/artifacts/aws-receipts/` or `docs/artifacts/gcp-receipts/`

## Related

- [aws-ephemeral-control-plane-receipt.md](../case-studies/aws-ephemeral-control-plane-receipt.md)  
- [gcp-serverless-ai-platform-receipt.md](../case-studies/gcp-serverless-ai-platform-receipt.md)  
- [P2_AWS_RECEIPT_RUNBOOK.md](./P2_AWS_RECEIPT_RUNBOOK.md) · [P2_GCP_RECEIPT_RUNBOOK.md](./P2_GCP_RECEIPT_RUNBOOK.md)

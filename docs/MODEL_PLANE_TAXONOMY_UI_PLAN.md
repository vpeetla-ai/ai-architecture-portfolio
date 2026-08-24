# Model Plane Taxonomy UI — implementation plan

**Status:** In progress (Aug 2026)  
**Surfaces:** venkat-ai.com/model-plane · ModelForge `/taxonomy` · DomainForge `/taxonomy`  
**ADR:** [ADR-034](../adr/ADR-034-modelforge-model-plane.md)

## Problem

Panels ask “where’s your model plane?” and engineers expect a **visible taxonomy** — LoRA vs QLoRA vs Multi-LoRA, task types (classification vs generation), classical ML vs LLM, and how ModelForge + DomainForge compose. A mental map in chat is not enough.

## Design principles

1. **One taxonomy, three surfaces** — same labels and honesty classes everywhere.
2. **Glassbox over brochure** — show status, receipt, and limitation per row; click to expand.
3. **Honesty classes** — `live` · `receipt` · `educational` · `playbook` · `planned` (never upgrade Path B to CUDA).
4. **Classical ML lane** — interview/playbook-grounded MLOps archetype; not a fake sklearn deploy unless labeled playbook.

## Taxonomy axes

| Axis | Examples | Primary surface |
|------|----------|-----------------|
| **Adaptation method** | Base/regular · LoRA · QLoRA · DPO · Multi-LoRA serve | ModelForge Taxonomy tab |
| **Task type** | Causal LM · intent classification · structured JSON · tabular classification/regression | All three |
| **Solution ladder** | S0→S4 (baseline → RAG → hybrid → PEFT → DPO) | DomainForge workbench + portfolio |
| **Classical ML stack** | Registry · skew · drift · batch/online · ML CI/CD | Portfolio + playbook links |
| **Compose map** | DomainForge → ModelForge → vLLM Lab → gateway | Portfolio glassbox center |

## Deliverables

| Repo | Path | Done when |
|------|------|-----------|
| venkat-ai-portfolio | `/model-plane` | Tabbed glassbox live; linked from work + spine artifact |
| modelforge-llmops | `/taxonomy` + `GET /api/v1/taxonomy` | Tab nav; API returns full taxonomy JSON |
| domainforge-rag-peft | `/taxonomy` | Ladder + adaptation slice; links to portfolio + ModelForge |
| ai-architecture-portfolio | This plan + REPO map | Cross-links in interview map |

## Non-goals

- Pretending classical ML is a live production sklearn pipeline on Render Free.
- Renaming peft_smoke as GPU or Path B as CUDA Multi-LoRA.
- A fourth “model zoo” repo — taxonomy is UI + docs only.

## Success criteria

- Hostile reviewer finds **LoRA / QLoRA / Multi-LoRA / regular / classification / regression** on venkat-ai.com in ≤30s.
- Each row shows **where it runs** and **honest status**.
- ModelForge and DomainForge tabs deep-link without contradicting portfolio copy.

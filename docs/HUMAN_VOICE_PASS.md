# Org narrative voice — ADRs, case studies, READMEs

Same bar as the interview playbook human-voice pass: sound like a **Principal who shipped this**, not a brochure or a template bot.

Apply to: `ai-architecture-portfolio` ADRs/case studies, per-repo `adr/` / `docs/adr/`, spine READMEs, profile README, hire/technical-review copy.

## Goal

A hiring panel or peer architect should hear **judgment** — decision first, scar second, proof third.

## ADR shape (keep structure, fix voice)

Keep: Status · Context · Decision · Consequences · Proof/Links

Add when missing:

```markdown
## In one breath (panel)

I'd … [one spoken sentence a peer would actually say]
```

### Do

- Open Context with the failure mode that forced the decision
- Decision in plain English before the numbered list
- Name what you **refused** (demo theater, soft multi-tenancy, merge governance into the graph, …)
- Label Demo vs Strict / Implemented vs Planned honestly
- Contractions OK; short + long sentence mix

### Don’t

- “This document outlines…” / “In today’s rapidly evolving…”
- leverage · comprehensive · seamless · cutting-edge · utilize · holistic · synergies
- Bullet salads with no default
- Implying Lucid production ran public repo binaries (P vs O)
- Inflating free-tier demos into enterprise SLOs

### Robotic → human

| Robotic | Human |
|---------|-------|
| “We implement a multi-layered governance framework…” | “I’d put an independent gateway in front of irreversible tools — policy, then HITL on the scary ones, audit everything. The agent graph doesn’t get a back door.” |
| “Authorization is enforced prior to ranking to ensure compliance.” | “Filter by who the caller is *before* you rank. Optimizing recall with unauthorized neighbors is how demos look smart and prod leaks.” |

## Case studies

1. Problem (human, one scar)  
2. What we decided (3–5 decisions with ADR links)  
3. Live proof URL  
4. What we’d do differently / limitations  

## READMEs (spine)

Lead with the **job of the system** in one breath. Catalog tables after. No “17 platforms demonstrate excellence.”

## After edits

- Don’t invent metrics  
- Keep links working  
- Prefer one PR per repo  

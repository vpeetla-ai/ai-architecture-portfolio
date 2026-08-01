# Supply Chain EDI Re-Platforming — Volvo Cars

**Domain:** Supply chain · EDI · Modernization  
**Organization:** Volvo Cars  
**Role:** Staff Software Engineer  
**Period:** 2019–2023

## Problem

License-heavy SAP and TrueCommerce EDI workflows burned recurring cost and left engineering with thin ownership. The scar is paying for a vendor path you can’t adapt when operations change — integration friction becomes a tax on every new trading partner.

## What we decided

1. **Move critical EDI flows behind owned services** — accept migration complexity to kill license drag.
2. **Domain ownership over vendor-coupled flows** — clearer boundaries, clearer on-call.
3. **Adaptability for operations over short-term migration speed** — don’t “finish” a cutover that locks the next change.
4. **Full-stack control where it mattered** — modernization path the team could actually ship against.

## Architecture

Critical EDI flows into owned full-stack architecture with clearer domain ownership, integration control, and a path off license-heavy middleware.

## Live proof

Employer systems are private. Public claim: **multi-million-dollar annualized savings** with better adaptability for supply-chain operations — figures not invented beyond that language.

## Limitations / what we'd do differently

- Migration complexity is real; I’d still sequence partner cohorts more aggressively to show value before the last long-tail flow.
- Vendor exit isn’t free — keep a rollback story for the first cohorts.
- Details stay generalized where contracts and partner IDs require it.

*Employer-specific details generalized where required.*

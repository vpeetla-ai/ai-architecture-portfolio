# Gulf Payments Modernization — Volvo Cars

**Domain:** Payments · Stripe · GIB · Retail commerce  
**Organization:** Volvo Cars  
**Role:** Staff Software Engineer  
**Period:** 2019–2023

## Problem

Gulf-market transactions needed gateway fit that one-off integrations couldn’t carry. The scar is bolting a regional PSP onto a commerce stack, then discovering reliability and ops controls weren’t platformized — revenue enablement stalls when settlement and exception paths are tribal knowledge.

## What we decided

1. **Payments as a platform capability** — not a one-off Stripe/GIB glue script per market.
2. **Regional gateway fit without permanent vendor lock** — GIB where it mattered; keep abstraction for long-term flexibility.
3. **Observability in the transaction path before volume** — you can’t debug settlement theater after scale.
4. **Operational controls with the integration** — retries, exceptions, and support paths owned by the platform team.

## Architecture

Commerce platform integrated Stripe and GIB with scalable flows, market-specific behavior, and operational controls at the payment boundary.

## Live proof

Employer systems are private. Outcome language used publicly: **multi-million-dollar annualized business impact** while strengthening the regional payments foundation — no fabricated precision.

## Limitations / what we'd do differently

- Details stay generalized (PII, contracts, exact $).
- I’d still invest earlier in shared exception playbooks across markets so on-call isn’t rediscovering gateway quirks.
- Vendor flexibility costs abstraction work up front; worth it when the next market asks for a different PSP.

*Employer-specific details generalized where required.*

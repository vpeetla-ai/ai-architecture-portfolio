# Subscription Revenue Platform — Volvo Cars

**Domain:** Subscriptions · Billing · Revenue systems  
**Organization:** Volvo Cars  
**Role:** Staff Software Engineer  
**Period:** 2019–2023

## Problem

Product lines needed recurring revenue, but the stack thought in transactional commerce. The scar is bolting “subscribe” onto checkout: renewals, exceptions, and finance reconciliation become edge cases that multiply in production.

## What we decided

1. **Subscriptions as a platform domain** — lifecycle, not a feature flag on the cart.
2. **State management for renewals and exceptions first** — design the unhappy path before volume.
3. **Explicit billing boundaries** — downstream analytics and finance need clean events, not scraped UI state.
4. **Operational support paths with the domain** — renewals fail in the real world; own the tools to fix them.

## Architecture

Subscription lifecycle across billing, renewal, state management, integration boundaries, and support paths.

## Live proof

Employer systems are private. Public claim: durable recurring revenue growth with stronger platform control over subscription lifecycle — no invented ARR figures here.

## Limitations / what we'd do differently

- Exact commercial metrics stay with the employer; this write-up stays qualitative on purpose.
- I’d still separate “billing truth” from “product entitlement” earlier when a new line asks for subscriptions.
- Edge-case catalogs grow; invest in fixture-like renewal scenarios before the second market launches.

*Employer-specific details generalized where required.*

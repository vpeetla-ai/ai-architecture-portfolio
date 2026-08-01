# ADR-008: Real Publish Scope (LinkedIn/X Only) and Invite-Gated Signup for ai-content-factory

## Status

Accepted — 2026-07-03

## In one breath (panel)

I'd rather ship two honest publish paths and "copy draft" for the rest than fake post URLs that look like success — and I'd invite-gate signup before inventing billing.

## Context

`ai-content-factory` was the strongest candidate to put in front of real public users (see
[case-studies/ai-content-factory.md](../case-studies/ai-content-factory.md)). Code inspection
surfaced three blockers:

1. `LinkedInAdapter.publish` hardcoded `"author": "urn:li:person:me"` — LinkedIn's UGC API
   rejects the literal `"me"`; it needs the real person URN.
2. Only the OAuth *callback* existed. There was no authorize-redirect endpoint — nobody could
   reach the callback. A pre-existing `POST /users/platforms/connect` built an authorize URL
   but never persisted CSRF `state` or a PKCE verifier. X's `code_verifier` was the literal
   string `"challenge"` — not real security.
3. Medium, Substack, and Instagram adapters returned fake `post_id`/`post_url` values
   indistinguishable from a real publish. Substack has no public posting API; Medium deprecated
   its public integration API for new apps; Instagram publish needs a multi-week Meta Business
   app review. None of the three is honestly "auto-publish" today.

Separately, going public meant billing or a lighter gate. No monetization stack existed. I
refused fake success URLs and refused Stripe before we had invite-based usage data.

## Decision

1. **Real OAuth + PKCE for LinkedIn and X only.** Added `GET /oauth/{platform}/authorize`
   (Bearer-authed, generates state + PKCE, stores server-side in Redis with a 10-minute TTL)
   and rewrote callbacks to resolve the connecting user via that stored state (not a Bearer
   header — provider redirects are plain browser navigations). Fixed the LinkedIn URN by
   fetching the real person id from LinkedIn's OIDC `/v2/userinfo` at connect time and
   threading the full per-platform token dict into `PublisherService`.
2. **Medium/Substack/Instagram become "copy draft," not fake auto-publish.** A shared
   `NotSupportedAdapter` returns draft content; the frontend shows "Copy draft" for those three.
3. **Invite-gated signup instead of billing.** An `invite_codes` table gates first-time user
   creation at the Clerk → internal JWT exchange, behind `require_invite_code` (off by default).
   No Stripe — deferred until invite usage exists.

Full implementation detail: [ai-content-factory/docs/ARCHITECTURE.md § OAuth connect + publish](https://github.com/vpeetla-ai/ai-content-factory/blob/main/docs/ARCHITECTURE.md#oauth-connect--publish-adr-008).

## Consequences

### Positive
- LinkedIn/X publishing is honest end-to-end: connect → real token → real API call with a
  valid author URN, covered by 26 new tests (adapters, PKCE/state roundtrip, rate limiter,
  invite gate) plus a local migration + CI-equivalent dry run against Postgres/Redis.
- Public claims match the code — no platform silently returns a fake "published" link.
- Invite-gating gets real users without building billing prematurely.

### Negative
- Substack/Medium/Instagram auto-publish stays unbuilt; revisit if a viable API appears.
- Invite codes are single-tier (no per-code role/quota); revisit if usage demands it.
- No FinOps/cost tracking in this change — still a portfolio-wide gap noted in ADR-007
  (addressed later via ADR-011 / ADR-012).

### Follow-ups
- ADR-009 / ADR-010 follow-ups from ADR-007 carried forward at write time (auth gates and MCP
  exposure landed in subsequent ADRs).
- Revisit Instagram auto-publish if/when Meta Business app review completes.

## Links

- [ai-content-factory/docs/PRODUCT.md](https://github.com/vpeetla-ai/ai-content-factory/blob/main/docs/PRODUCT.md)
- [ai-content-factory/docs/ARCHITECTURE.md](https://github.com/vpeetla-ai/ai-content-factory/blob/main/docs/ARCHITECTURE.md)
- [ADR-007-2026-agent-protocol-stack.md](./ADR-007-2026-agent-protocol-stack.md)

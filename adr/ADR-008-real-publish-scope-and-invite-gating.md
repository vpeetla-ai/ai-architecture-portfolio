# ADR-008: Real Publish Scope (LinkedIn/X Only) and Invite-Gated Signup for ai-content-factory

## Status

Accepted — 2026-07-03

## Context

`ai-content-factory` was the strongest candidate in the portfolio to take to real public
users (see [case-studies/ai-content-factory.md](../case-studies/ai-content-factory.md)). Direct
inspection of the codebase surfaced three problems blocking that:

1. `LinkedInAdapter.publish` hardcoded `"author": "urn:li:person:me"` — LinkedIn's UGC API
   rejects the literal string `"me"` and requires the real person URN.
2. Only the OAuth *callback* (code → token exchange) existed. There was no authorize-redirect
   endpoint anywhere — no user could ever reach the callback. A pre-existing
   `POST /users/platforms/connect` endpoint built an authorize URL but never persisted a CSRF
   `state` or PKCE verifier, so it could not have worked with a real callback. X's PKCE
   `code_verifier` was hardcoded to the literal string `"challenge"` — not real security.
3. Medium, Substack, and Instagram adapters returned fake `post_id`/`post_url` values
   indistinguishable from a real publish. Investigation confirmed: Substack has no public
   posting API, Medium deprecated its public integration API for new apps, and Instagram
   publish requires a multi-week Meta Business app review. None of the three is honestly
   buildable as "auto-publish" right now.

Separately, taking the product public required either a billing system or a lighter gate.
No monetization infrastructure existed.

## Decision

1. **Real OAuth + PKCE for LinkedIn and X only.** Added `GET /oauth/{platform}/authorize`
   (Bearer-authed, generates state + PKCE, stores server-side in Redis with a 10-minute TTL)
   and rewrote the callbacks to resolve the connecting user via that stored state (not a
   Bearer header, since a provider redirect is a plain browser navigation). Fixed the LinkedIn
   URN by fetching the real person id from LinkedIn's OIDC `/v2/userinfo` endpoint at connect
   time and threading the full per-platform token dict (not just a bare access token) into
   `PublisherService`.
2. **Medium/Substack/Instagram become "copy draft," not fake auto-publish.** A shared
   `NotSupportedAdapter` returns the draft content instead of a synthetic post URL; the
   frontend renders a "Copy draft" action for these three platforms.
3. **Invite-gated signup instead of billing.** A new `invite_codes` table gates first-time
   user creation at the Clerk → internal JWT exchange step, behind a `require_invite_code`
   setting (off by default). No Stripe/billing integration — deferred until there's real
   invite-based usage data.

Full implementation detail: [ai-content-factory/docs/ARCHITECTURE.md § OAuth connect + publish](https://github.com/vpeetla-ai/ai-content-factory/blob/main/docs/ARCHITECTURE.md#oauth-connect--publish-adr-008).

## Consequences

### Positive
- LinkedIn/X publishing is now honest end-to-end: connect → real token → real API call with a
  valid author URN, verified by 26 new tests (adapters, PKCE/state roundtrip, rate limiter,
  invite gate) plus a local migration + CI-equivalent dry run against Postgres/Redis.
- The product's public claims match what the code does — no platform silently returns a fake
  "published" link.
- Invite-gating gets the product in front of real users without building billing prematurely.

### Negative
- Substack/Medium/Instagram auto-publish remains unbuilt; if a viable API emerges for any of
  them, this ADR's platform-scope decision should be revisited.
- Invite codes are single-tier (no per-code role/quota); revisit if usage patterns demand it.
- No FinOps/cost tracking was added as part of this change — still a portfolio-wide gap noted
  in ADR-007.

### Follow-ups
- ADR-009 (proposed): LoopForge gateway on PR workflow (carried over from ADR-007's follow-ups)
- ADR-010 (proposed): MCP tool registry in VAP (carried over from ADR-007's follow-ups)
- Revisit Instagram auto-publish if/when Meta Business app review is completed.

## Links

- [ai-content-factory/docs/PRODUCT.md](https://github.com/vpeetla-ai/ai-content-factory/blob/main/docs/PRODUCT.md)
- [ai-content-factory/docs/ARCHITECTURE.md](https://github.com/vpeetla-ai/ai-content-factory/blob/main/docs/ARCHITECTURE.md)
- [ADR-007-2026-agent-protocol-stack.md](./ADR-007-2026-agent-protocol-stack.md)

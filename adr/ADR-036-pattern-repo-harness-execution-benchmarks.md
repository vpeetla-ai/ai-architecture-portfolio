# ADR-036: Pattern-Repo Benchmarks Measure Harness Execution, Not LLM Quality

**Status:** Accepted
**Date:** 2026-09-03
**Deciders:** Venkata Peetla (Principal AI Architect)
**Repos:** `react-agent-pattern`, `reflection-agent-pattern`, `plan-execute-agent-pattern`, `multi-agent-system-pattern`, `swarm-agent-pattern`, `golden-eval-registry`

## In one breath (panel)

I benchmark what each pattern's control-flow actually guarantees under real trials — a bounded loop that really stops, a reviewer gate that really rejects — not a made-up LLM quality score from a repo that was designed, on purpose, to never call one.

## Context

Closing Critical Gap #2 (harness execution) meant the five curriculum agent-pattern repos needed genuinely differentiated, real evidence — the earlier review found all five pushed within 9 seconds of each other with near-identical boilerplate and no proof of what each pattern specifically buys you over a naive baseline.

Each repo's README already discloses its architecture honestly: "Deterministic model stub — pytest without API keys," "Curriculum stub... not a production agent fleet." The `ReasoningModel`/`Generator`/`Critic`/`Planner`/`Agent` interfaces in every one of the five are pluggable stub interfaces by design, with no LLM API call anywhere in the source. This is a deliberate, disclosed choice, consistent across all five siblings — not an oversight to "fix" by bolting on a Groq/OpenAI dependency.

That meant a real benchmark here could not be "run the pattern against a real LLM and score output quality" — that would either require adding a new external dependency this org's own conventions explicitly avoided for these repos, or it would fabricate a claim to sound plausible. The honest question these repos can actually answer for real is a **harness-execution** question: does the pattern's control flow do what it claims, under real, varied trial conditions, measured against a real (if simple) baseline?

## Decision

Each of the five repos got one real, executed benchmark measuring its own specific mechanical guarantee, run against the actual production code path (not a mock of it), with a real baseline built from the same stub interfaces for a fair comparison:

| Repo | Real measurement | Baseline |
|------|-------------------|----------|
| `react-agent-pattern` | Task success rate + avg iterations, `ReActAgent` | bounded (`max_steps=5`) vs unbounded (`max_steps=200`) |
| `reflection-agent-pattern` | Score delta, first draft vs revised, `ReflectionAgent` | draft-only (`attempts[0]`) vs full critique-revise loop |
| `plan-execute-agent-pattern` | Decomposition accuracy vs ground truth + execution success, `PlanExecuteAgent` | plan-then-execute vs a new real `ReactiveBaselineAgent` (same `Executor`/`Synthesizer`, no upfront plan) |
| `multi-agent-system-pattern` | Reviewer-gate approval rate, `MultiAgentOrchestrator` | complete specialist roster vs a new real `GeneralistAgent` vs a deliberately incomplete roster |
| `swarm-agent-pattern` | Rounds/invocations to convergence, `SwarmRuntime` | parallel fan-out (all agents propose each round) vs a new real serial baseline (one agent per round) |

Every benchmark is backed by a real script (`scripts/benchmark_*.py`) that executes the trials and generates `docs/receipts/benchmark.md` — never hand-written — plus a real pytest asserting invariants on the output, and a real CI gate: a new suite in `golden-eval-registry` (kind `router_invariant`, `mission_gate`, or the newly-added `critique_delta_gate`) checked out fresh each CI run and scored against the repo's actual benchmark output, failing the build on regression — the same pattern already proven in `aegisloop-agentops-workbench`'s `test_golden_eval_gate.py`.

Where a benchmark's real result was unflattering, it was reported as-is rather than reframed: plan-execute mode scored *lower* execution-success (75%) than the reactive baseline (87.5%) on its 8-task set — a genuine finding about the cost of a hard-stop-on-failure design with no replanning, not smoothed over. Swarm fan-out's real advantage turned out to be coverage-per-round, not invocation-efficiency (it used *more* total invocations on average to win under an equal-round budget) — reported both ways rather than picking the flattering framing. React's bounded-loop benchmark found neither bounded nor unbounded mode protects against a malformed-tool-args failure mode — also reported plainly.

## Consequences

### Positive

- Five previously-identical repos now each have one number a reviewer can independently reproduce (`python scripts/benchmark_*.py`) and a CI gate that would catch a regression in that pattern's core guarantee.
- The deterministic-stub architecture — the thing that made these repos look thin — turned out to be exactly what made a zero-cost, zero-API-key, fully-reproducible real benchmark possible.
- Unflattering real results (plan-execute losing to reactive on one task set) are left in, which is stronger evidence of rigor than five uniformly flattering numbers would have been.

### Trade-offs

- These benchmarks say nothing about LLM output quality — a reviewer expecting "how good are the agent's answers" needs to look at DomainForge/ModelForge (ADR-035) instead, not these five repos.
- `golden-eval-registry`'s own hardcoded suite/case-count assertions (`tests/test_registry.py`) needed reconciling after five parallel suite additions landed concurrently — a real coordination cost of running this work in parallel, resolved in one follow-up commit rather than left broken.

### Refused

- Adding a real LLM API dependency to any of the five repos to manufacture an output-quality number, which would have contradicted their own disclosed "no API keys" design.
- Papering over an unflattering real result (plan-execute vs reactive, swarm's invocation cost) to make every repo's number look uniformly positive.

## Links

- `golden-eval-registry` commits: `92019a3`, `771a18b`, `9a261a6`, `fea84f8`, `549b493` (suites), `658bdfa`, `70951d6`, `deb0630` (index reconciliation)
- Pattern-repo commits: `react-agent-pattern@0d07a03`, `reflection-agent-pattern@6da491a`, `plan-execute-agent-pattern@48ec835`, `multi-agent-system-pattern@946121d`, `swarm-agent-pattern@4d58441`
- ADR-030 (FDE field-method portfolio proof) · ADR-031 (multi-agent collaboration scorecard)

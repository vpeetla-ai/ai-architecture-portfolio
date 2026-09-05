# ADR-036: Pattern-Repo Benchmarks Measure Harness Execution, Not LLM Quality

**Status:** Accepted
**Date:** 2026-09-03
**Deciders:** Venkata Peetla (Principal AI Architect)
**Repos:** `react-agent-pattern`, `reflection-agent-pattern`, `plan-execute-agent-pattern`, `multi-agent-system-pattern`, `swarm-agent-pattern`, `golden-eval-registry`

## In one breath (panel)

I benchmark what each pattern's control-flow actually guarantees under real trials — a bounded loop that really stops, a reviewer gate that really rejects — not a made-up LLM quality score from a repo that was designed, on purpose, to never call one.

## Context

Critical Gap #2 was harness execution. The five curriculum agent-pattern repos were the evidence: pushed within 9 seconds of each other, near-identical boilerplate, no proof any one pattern actually buys you anything over a naive baseline.

Each repo already discloses its architecture honestly — "Deterministic model stub — pytest without API keys," "Curriculum stub... not a production agent fleet." Every `ReasoningModel`/`Generator`/`Critic`/`Planner`/`Agent` interface is a pluggable stub, no LLM call anywhere in the source. Deliberate, disclosed, consistent across all five. Not an oversight to fix by bolting on a Groq key.

So "run it against a real LLM and score output quality" was off the table — that either adds a dependency these repos deliberately don't have, or fakes a number to look plausible. The question these repos can actually answer for real is a harness-execution one: does the control flow do what it claims, under real trials, against a real baseline?

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

Where a result was unflattering, it stayed unflattering. Plan-execute scored *lower* execution-success (75%) than its own reactive baseline (87.5%) on the 8-task set — a real cost of hard-stop-on-failure with no replanning, not smoothed over. Swarm fan-out's real edge turned out to be coverage-per-round, not efficiency — it used *more* total invocations on average — reported both ways. React's bounded loop protects against neither bounded nor unbounded malformed-tool-args failure. Left in.

## Consequences

### Positive

- Five identical-looking repos now each have one number a reviewer can reproduce (`python scripts/benchmark_*.py`) and a CI gate that catches a regression in that pattern's core guarantee.
- The deterministic-stub design — the thing that made these repos look thin — is exactly what made a zero-cost, zero-API-key, reproducible benchmark possible.
- Keeping the unflattering results in is stronger evidence of rigor than five flattering numbers would have been.

### Trade-offs

- None of this says anything about LLM output quality. For "how good are the agent's answers," look at DomainForge/ModelForge (ADR-035), not these five.
- `golden-eval-registry`'s hardcoded suite/case counts (`tests/test_registry.py`) drifted when five suites landed in parallel — a real cost of parallel work, fixed in one follow-up commit.

### Refused

- Adding an LLM API dependency to manufacture an output-quality number — contradicts the repos' own disclosed "no API keys" design.
- Papering over an unflattering result to make every number look positive.

## Links

- `golden-eval-registry` commits: `92019a3`, `771a18b`, `9a261a6`, `fea84f8`, `549b493` (suites), `658bdfa`, `70951d6`, `deb0630` (index reconciliation)
- Pattern-repo commits: `react-agent-pattern@0d07a03`, `reflection-agent-pattern@6da491a`, `plan-execute-agent-pattern@48ec835`, `multi-agent-system-pattern@946121d`, `swarm-agent-pattern@4d58441`
- ADR-030 (FDE field-method portfolio proof) · ADR-031 (multi-agent collaboration scorecard)

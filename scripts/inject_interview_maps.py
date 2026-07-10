#!/usr/bin/env python3
"""Insert/replace ## Interview map sections in vpeetla-ai product READMEs."""

from __future__ import annotations

import re
from pathlib import Path

HOME = Path("/Users/lakshmipraveenabodempudi")
UI = "https://ai-architect-interview-playbook.vercel.app/q"
GH = "https://github.com/vpeetla-ai/ai-architect-interview-playbook/blob/main"
PLAYBOOK = "https://github.com/vpeetla-ai/ai-architect-interview-playbook"
STUDY = "https://ai-architect-interview-playbook.vercel.app"
ARENA = "https://ai-architect-practice-arena.vercel.app"
MATRIX = "https://github.com/vpeetla-ai/ai-architecture-portfolio/blob/main/docs/REPO_INTERVIEW_MAP.md"


def q(cat: str, slug: str, title: str) -> str:
    # Study UI is a static export with trailingSlash: true
    return f"[{title}]({UI}/{cat}/{slug}/) ([md]({GH}/{cat}/{slug}.md))"


def section(business: str, rows: list[tuple[str, str, str]]) -> str:
    lines = [
        "## Interview map",
        "",
        f"**Business function:** {business}",
        "",
        f"Staff+ prep crosswalk — [playbook]({PLAYBOOK}) · [study UI]({STUDY}) · "
        f"[Practice Arena]({ARENA}) · [org matrix]({MATRIX}). "
        "Only entries this repo honestly exercises.",
        "",
        "| Category | Entry | Fit |",
        "|----------|-------|-----|",
    ]
    for cat, entry, fit in rows:
        lines.append(f"| {cat} | {entry} | {fit} |")
    lines.append("")
    return "\n".join(lines)


SECTIONS: dict[str, str] = {
    "venkat-ai-platform": section(
        "Multi-agent OS — intent routing, parallel specialists, critic, multi-channel notify.",
        [
            (
                "System design",
                q(
                    "ai-system-design",
                    "03-agent-tool-use-orchestration-platform",
                    "Agent tool-use / orchestration",
                ),
                "Core: LangGraph orchestrators + tool side effects via gateway",
            ),
            (
                "System design",
                q(
                    "ai-system-design",
                    "13-durable-long-running-agent-execution",
                    "Durable long-running agents",
                ),
                "Partial — threaded runs, HITL resume, persistence",
            ),
            (
                "Cloud",
                q(
                    "cloud-architecture",
                    "07-llm-gateway-semantic-cache-model-router",
                    "LLM gateway / model routing",
                ),
                "Multi-LLM routing + notify path through AegisAI",
            ),
            (
                "Trade-offs",
                q(
                    "scalability-governance-tradeoffs",
                    "01-cost-vs-latency-vs-safety",
                    "Cost vs latency vs safety",
                ),
                "Routing / model choice under budget",
            ),
            (
                "Trade-offs",
                q(
                    "scalability-governance-tradeoffs",
                    "03-centralize-vs-federate-governance",
                    "Centralize vs federate governance",
                ),
                "Orchestration here; policy in AegisAI",
            ),
            (
                "Behavioral",
                q(
                    "behavioral",
                    "05-leading-a-0-to-1-ai-product-build",
                    "Leading a 0→1 AI product",
                ),
                "Platform build under ambiguity",
            ),
        ],
    ),
    "aegisai-enterprise-agent-platform": section(
        "Enterprise agent governance — AI gateway, OPA policy, HITL, signed audit, FinOps before side effects.",
        [
            (
                "Cloud",
                q(
                    "cloud-architecture",
                    "05-security-and-compliance-architecture-for-ai-systems",
                    "Security & compliance for AI",
                ),
                "Control plane: identity, policy, audit, break-glass",
            ),
            (
                "Cloud",
                q(
                    "cloud-architecture",
                    "07-llm-gateway-semantic-cache-model-router",
                    "LLM gateway",
                ),
                "Gateway authorization before tools execute",
            ),
            (
                "System design",
                q(
                    "ai-system-design",
                    "03-agent-tool-use-orchestration-platform",
                    "Agent orchestration (governance half)",
                ),
                "Tool authorization / HITL for VAP notify and peers",
            ),
            (
                "System design",
                q(
                    "ai-system-design",
                    "09-multi-tenant-ai-platform-architecture",
                    "Multi-tenant AI platform",
                ),
                "Partial — tenant/policy isolation patterns",
            ),
            (
                "System design",
                q(
                    "ai-system-design",
                    "10-ai-agent-sandboxing-and-code-execution-security",
                    "Agent sandboxing / code exec",
                ),
                "Partial — blast-radius controls for tools",
            ),
            (
                "Trade-offs",
                q(
                    "scalability-governance-tradeoffs",
                    "03-centralize-vs-federate-governance",
                    "Centralize vs federate governance",
                ),
                "Primary ADR theme for this layer",
            ),
            (
                "Behavioral",
                q(
                    "behavioral",
                    "03-org-wide-security-hardening",
                    "Org-wide security hardening",
                ),
                "Unauthenticated endpoints / API-key gates story",
            ),
        ],
    ),
    "enterprise_rag_platform": section(
        "Production RAG — access-before-ranking, hybrid retrieval, citations, decline-to-answer, evals.",
        [
            (
                "System design",
                q("ai-system-design", "02-rag-platform-at-scale", "RAG platform at scale"),
                "Primary map — ACL filter, hybrid retrieve, rerank, citations",
            ),
            (
                "Cloud",
                q(
                    "cloud-architecture",
                    "05-security-and-compliance-architecture-for-ai-systems",
                    "Security & compliance for AI",
                ),
                "Clearance / ACL on chunks before ranking",
            ),
            (
                "Trade-offs",
                q(
                    "scalability-governance-tradeoffs",
                    "01-cost-vs-latency-vs-safety",
                    "Cost vs latency vs safety",
                ),
                "Rerank vs latency; decline vs wrong answer",
            ),
        ],
    ),
    "domainforge-rag-peft": section(
        "RAG for facts + PEFT for behavior — customer-support triage with grounded citations and schema reliability.",
        [
            (
                "System design",
                q("ai-system-design", "02-rag-platform-at-scale", "RAG platform at scale"),
                "Grounded SOP retrieval",
            ),
            (
                "System design",
                q(
                    "ai-system-design",
                    "16-llm-customer-support-assistant",
                    "LLM customer support assistant",
                ),
                "Triage / routing product shape",
            ),
            (
                "System design",
                q(
                    "ai-system-design",
                    "08-finetuning-rlhf-training-pipeline-at-scale",
                    "Fine-tuning / RLHF pipeline",
                ),
                "Partial — PEFT/adapters, not full RLHF plant",
            ),
            (
                "System design",
                q(
                    "ai-system-design",
                    "04-feature-store-finetuning-data-pipeline",
                    "Feature store / fine-tune data",
                ),
                "Partial — adaptation data / eval ladder S0–S4",
            ),
            (
                "Trade-offs",
                q(
                    "scalability-governance-tradeoffs",
                    "04-build-vs-train-vs-finetune-foundation-model-strategy",
                    "Build vs train vs fine-tune",
                ),
                "RAG facts vs PEFT behavior (ADR-019)",
            ),
        ],
    ),
    "voiceforge-assistant": section(
        "Real-time voice triage — ASR → LLM → TTS with per-phase latency budgets and graceful degradation.",
        [
            (
                "System design",
                q(
                    "ai-system-design",
                    "16-llm-customer-support-assistant",
                    "LLM customer support assistant",
                ),
                "Voice channel for support/IT triage",
            ),
            (
                "Trade-offs",
                q(
                    "scalability-governance-tradeoffs",
                    "01-cost-vs-latency-vs-safety",
                    "Cost vs latency vs safety",
                ),
                "Hard latency budgets + fallbacks (ADR-021)",
            ),
            (
                "General SD",
                q(
                    "general-system-design",
                    "02-realtime-chat-messaging-at-scale",
                    "Real-time messaging at scale",
                ),
                "Partial — WebSocket streaming path only",
            ),
        ],
    ),
    "ai-content-factory": section(
        "Multi-agent content pipeline — research → drafts → HITL → publish (LinkedIn/X live).",
        [
            (
                "System design",
                q(
                    "ai-system-design",
                    "03-agent-tool-use-orchestration-platform",
                    "Agent tool-use / orchestration",
                ),
                "LangGraph pipeline + gateway publish",
            ),
            (
                "General SD",
                q(
                    "general-system-design",
                    "04-distributed-job-scheduler-task-queue",
                    "Job scheduler / task queue",
                ),
                "Partial — cron / pipeline runs",
            ),
            (
                "General SD",
                q("general-system-design", "08-notification-system", "Notification system"),
                "Partial — post-publish / ops signals",
            ),
            (
                "Trade-offs",
                q(
                    "scalability-governance-tradeoffs",
                    "01-cost-vs-latency-vs-safety",
                    "Cost vs latency vs safety",
                ),
                "HITL vs autonomy; model cost per run",
            ),
            (
                "Behavioral",
                q(
                    "behavioral",
                    "05-leading-a-0-to-1-ai-product-build",
                    "Leading a 0→1 AI product",
                ),
                "Shipped application-layer product story",
            ),
        ],
    ),
    "aegisloop-agentops-workbench": section(
        "AgentOps workbench — missions, traces, eval gates, fleet monitoring.",
        [
            (
                "System design",
                q(
                    "ai-system-design",
                    "07-llm-evaluation-observability-platform",
                    "LLM eval & observability",
                ),
                "Primary — traces, mission quality gates",
            ),
            (
                "System design",
                q(
                    "ai-system-design",
                    "03-agent-tool-use-orchestration-platform",
                    "Agent orchestration",
                ),
                "Mission invoke / VAP A2A delegation",
            ),
            (
                "Trade-offs",
                q(
                    "scalability-governance-tradeoffs",
                    "01-cost-vs-latency-vs-safety",
                    "Cost vs latency vs safety",
                ),
                "Meters via agent-finops; eval before promote",
            ),
        ],
    ),
    "agent-finops": section(
        "Shared FinOps service — usage metering, budgets, cost-breach signals for agent fleets.",
        [
            (
                "Cloud",
                q(
                    "cloud-architecture",
                    "06-container-orchestration-and-cost-optimization-at-scale",
                    "Orchestration & cost optimization",
                ),
                "Cost governance as a shared service",
            ),
            (
                "System design",
                q(
                    "ai-system-design",
                    "09-multi-tenant-ai-platform-architecture",
                    "Multi-tenant AI platform",
                ),
                "Partial — per-tenant budgets / quotas",
            ),
            (
                "Trade-offs",
                q(
                    "scalability-governance-tradeoffs",
                    "01-cost-vs-latency-vs-safety",
                    "Cost vs latency vs safety",
                ),
                "Enforced budgets vs best-effort dashboards",
            ),
            (
                "Trade-offs",
                q(
                    "scalability-governance-tradeoffs",
                    "02-build-vs-buy-shared-services",
                    "Build vs buy shared services",
                ),
                "Why a dedicated metering service",
            ),
            (
                "Behavioral",
                q("behavioral", "02-finops-audit-and-fix", "FinOps audit and fix"),
                "Finding/fixing real FinOps gaps in-org",
            ),
        ],
    ),
    "loop-engine-agent-platform": section(
        "Self-improving agent harness — ODAEU loops, RAG evolve, governed repo-fix PRs.",
        [
            (
                "System design",
                q(
                    "ai-system-design",
                    "13-durable-long-running-agent-execution",
                    "Durable long-running agents",
                ),
                "Overnight / multi-step improve loops",
            ),
            (
                "System design",
                q(
                    "ai-system-design",
                    "15-ai-coding-assistant",
                    "AI coding assistant",
                ),
                "Partial — repo-fix patch loop (not full IDE Copilot)",
            ),
            (
                "System design",
                q(
                    "ai-system-design",
                    "10-ai-agent-sandboxing-and-code-execution-security",
                    "Agent sandboxing / code exec",
                ),
                "Workspace tools; never push main",
            ),
            (
                "System design",
                q(
                    "ai-system-design",
                    "07-llm-evaluation-observability-platform",
                    "LLM eval & observability",
                ),
                "Eval gates before accepting tune/fix",
            ),
            (
                "Trade-offs",
                q(
                    "scalability-governance-tradeoffs",
                    "01-cost-vs-latency-vs-safety",
                    "Cost vs latency vs safety",
                ),
                "Loop budgets vs improvement gains",
            ),
        ],
    ),
    "vllm-architecture-lab": section(
        "Educational LLM serving lab — PagedAttention, continuous batching, KV-cache economics.",
        [
            (
                "System design",
                q(
                    "ai-system-design",
                    "01-llm-inference-serving-at-scale",
                    "LLM inference serving at scale",
                ),
                "Primary map — paging, batching, KV",
            ),
            (
                "Cloud",
                q(
                    "cloud-architecture",
                    "01-gpu-capacity-planning-and-procurement",
                    "GPU capacity planning",
                ),
                "Partial — capacity framing for serving fleets",
            ),
            (
                "Cloud",
                q(
                    "cloud-architecture",
                    "06-container-orchestration-and-cost-optimization-at-scale",
                    "Orchestration & cost optimization",
                ),
                "Partial — serving cost / utilization story",
            ),
            (
                "Trade-offs",
                q(
                    "scalability-governance-tradeoffs",
                    "04-build-vs-train-vs-finetune-foundation-model-strategy",
                    "Build vs train vs fine-tune",
                ),
                "Partial — multi-LoRA serving economics (ADR-022)",
            ),
        ],
    ),
    "sentinel-brief": section(
        "Overnight intelligence brief — allowlisted sources → diff → summary → eval → governed email.",
        [
            (
                "System design",
                q(
                    "ai-system-design",
                    "03-agent-tool-use-orchestration-platform",
                    "Agent orchestration",
                ),
                "LangGraph run with gateway on email.send only",
            ),
            (
                "General SD",
                q(
                    "general-system-design",
                    "04-distributed-job-scheduler-task-queue",
                    "Job scheduler / task queue",
                ),
                "Scheduled overnight runs",
            ),
            (
                "General SD",
                q("general-system-design", "08-notification-system", "Notification system"),
                "Email as irreversible notify path",
            ),
            (
                "General SD",
                q("general-system-design", "11-web-crawler", "Web crawler"),
                "Partial — allowlisted RSS/API fetch, not open crawl",
            ),
        ],
    ),
    "golden-eval-registry": section(
        "Versioned golden eval fixtures and scorers — portable CI gates across the stack.",
        [
            (
                "System design",
                q(
                    "ai-system-design",
                    "07-llm-evaluation-observability-platform",
                    "LLM eval & observability",
                ),
                "Primary — fixtures as release artifacts",
            ),
            (
                "Trade-offs",
                q(
                    "scalability-governance-tradeoffs",
                    "02-build-vs-buy-shared-services",
                    "Build vs buy shared services",
                ),
                "Shared registry vs per-repo ad hoc tests",
            ),
        ],
    ),
    "omniforge": section(
        "Self-contained multimodal multi-agent multi-LLM answer platform (text / image / voice).",
        [
            (
                "System design",
                q(
                    "ai-system-design",
                    "03-agent-tool-use-orchestration-platform",
                    "Agent orchestration",
                ),
                "Planner + specialized agents + MCP tools",
            ),
            (
                "System design",
                q(
                    "ai-system-design",
                    "06-multimodal-search-recommendation-system",
                    "Multimodal search / recommendation",
                ),
                "Partial — multimodal ingest/answer, not full recsys",
            ),
            (
                "Cloud",
                q(
                    "cloud-architecture",
                    "07-llm-gateway-semantic-cache-model-router",
                    "LLM gateway / model router",
                ),
                "In-repo model waterfall / routing",
            ),
            (
                "Trade-offs",
                q(
                    "scalability-governance-tradeoffs",
                    "01-cost-vs-latency-vs-safety",
                    "Cost vs latency vs safety",
                ),
                "Model choice per step under budget",
            ),
        ],
    ),
    "ai-architect-practice-arena": section(
        "BYOK mock-interview judge UI over playbook rubrics (OpenAI + Anthropic).",
        [
            (
                "System design",
                q(
                    "ai-system-design",
                    "07-llm-evaluation-observability-platform",
                    "LLM eval & observability",
                ),
                "Partial — LLM-as-judge scoring loop",
            ),
            (
                "Trade-offs",
                q(
                    "scalability-governance-tradeoffs",
                    "02-build-vs-buy-shared-services",
                    "Build vs buy shared services",
                ),
                "BYOK vs hosted judge; dual-provider calibration",
            ),
        ],
    ),
}

PATTERN_SECTION = section(
    "Minimal LangGraph teaching stub for one agent pattern (compose into VAP for production).",
    [
        (
            "System design",
            q(
                "ai-system-design",
                "03-agent-tool-use-orchestration-platform",
                "Agent tool-use / orchestration",
            ),
            "Pattern slice only — not a full platform",
        ),
        (
            "Coding",
            q("coding", "07-graph-clone-and-cycle-safe", "Clone a graph (cycle-safe)"),
            "Light — graph structure intuition for LangGraph",
        ),
    ],
)

for name in (
    "react-agent-pattern",
    "reflection-agent-pattern",
    "plan-execute-agent-pattern",
    "multi-agent-system-pattern",
    "swarm-agent-pattern",
):
    SECTIONS[name] = PATTERN_SECTION


INSERT_BEFORE = re.compile(
    r"^## (Related projects|Related|License|Connect|Stack fit|Docs)\s*$",
    re.MULTILINE,
)
SECTION_RE = re.compile(
    r"^## Interview map\n.*?(?=^## |\Z)",
    re.MULTILINE | re.DOTALL,
)


def apply(repo: str, body: str) -> str:
    text = (HOME / repo / "README.md").read_text()
    if SECTION_RE.search(text):
        text = SECTION_RE.sub(body.rstrip() + "\n\n", text, count=1)
    else:
        m = INSERT_BEFORE.search(text)
        if m:
            text = text[: m.start()] + body + "\n" + text[m.start() :]
        else:
            text = text.rstrip() + "\n\n" + body
    (HOME / repo / "README.md").write_text(text)
    return repo


def main() -> None:
    done = []
    for repo, body in SECTIONS.items():
        path = HOME / repo / "README.md"
        if not path.exists():
            print("SKIP missing", repo)
            continue
        apply(repo, body)
        done.append(repo)
    print("updated", len(done), "READMEs:")
    for r in done:
        print(" ", r)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Stranger-replayable spine golden path (S4.1).

Sequence: health → VAP ask → ERAG answer → AegisAI gateway → ACF health → FinOps meter
Writes docs/artifacts/golden-path/<run_id>.json and latest.json
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "docs" / "artifacts" / "golden-path"

ENDPOINTS = {
    "vap": os.environ.get("VAP_API", "https://vap-api.onrender.com"),
    "erag": os.environ.get("ERAG_API", "https://enterprise-rag-api-4el1.onrender.com"),
    "aegisai": os.environ.get("AEGISAI_API", "https://aegisai-api.onrender.com"),
    "acf": os.environ.get("ACF_API", "https://acf-api-eub4.onrender.com"),
    "finops": os.environ.get("FINOPS_API", "https://agent-finops-api.onrender.com"),
}
# Optional Strict ERAG (local Docker / GCP Cloud Run). Not required for stranger_ok.
ERAG_STRICT_URL = (os.environ.get("ERAG_STRICT_URL") or "").rstrip("/")

# Always required for a green stranger run (no secrets).
STRANGER_CRITICAL = {
    "health_vap",
    "health_erag",
    "health_aegisai",
    "aegisai_gate",
    "finops_usage",
}
# Full ask/answer path when VAP_API_KEY / RAG_API_KEY are provided.
AUTH_GATED = {"vap_ask", "erag_answer"}


def log(msg: str) -> None:
    print(f"[golden-path] {msg}", file=sys.stderr)


def request_json(
    step: str,
    method: str,
    url: str,
    *,
    body: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
    timeout: float = 120.0,
) -> dict[str, Any]:
    hdrs = {"Accept": "application/json", **(headers or {})}
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        hdrs["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=hdrs, method=method)
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
            status = resp.status
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        status = exc.code
    except Exception as exc:  # noqa: BLE001 — stranger-facing probe
        latency_ms = int((time.perf_counter() - started) * 1000)
        return {
            "step": step,
            "ok": False,
            "http_status": 0,
            "latency_ms": latency_ms,
            "url": url,
            "error": str(exc),
            "response_keys": [],
            "response_snippet": "",
        }

    latency_ms = int((time.perf_counter() - started) * 1000)
    parsed: Any = None
    try:
        parsed = json.loads(raw) if raw.strip() else None
    except json.JSONDecodeError:
        parsed = None

    item: dict[str, Any] = {
        "step": step,
        "ok": 200 <= status < 300,
        "http_status": status,
        "latency_ms": latency_ms,
        "url": url,
        "response_keys": list(parsed.keys())[:20] if isinstance(parsed, dict) else [],
        "response_snippet": raw[:500],
    }
    if isinstance(parsed, dict):
        if "gateway_decision" in parsed:
            item["gateway_decision"] = parsed.get("gateway_decision")
        if "declined" in parsed:
            item["erag_declined"] = parsed.get("declined")
        if "grounded" in parsed:
            item["erag_grounded"] = parsed.get("grounded")
        if isinstance(parsed.get("answer"), str):
            item["answer_preview"] = parsed["answer"][:240]
        if "estimated_cost_usd" in parsed:
            item["estimated_cost_usd"] = parsed.get("estimated_cost_usd")
        if parsed.get("usage_id") or parsed.get("id"):
            item["usage_id"] = parsed.get("usage_id") or parsed.get("id")
        if isinstance(parsed.get("reply"), str):
            item["reply_preview"] = parsed["reply"][:240]
        if isinstance(parsed.get("response"), str):
            item["reply_preview"] = parsed["response"][:240]
        if isinstance(parsed.get("message"), str) and "reply_preview" not in item:
            item["reply_preview"] = parsed["message"][:240]
        if "review_mode" in parsed:
            item["review_mode"] = parsed.get("review_mode")
        if "principal_source" in parsed:
            item["principal_source"] = parsed.get("principal_source")
    return item


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    run_id = f"gp-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
    started_at = datetime.now(timezone.utc).isoformat()
    log(f"run_id={run_id}")

    steps: list[dict[str, Any]] = []

    log("0) health probes")
    for name, base in ENDPOINTS.items():
        steps.append(request_json(f"health_{name}", "GET", f"{base.rstrip('/')}/health", timeout=45))

    log("1) VAP ask")
    vap_headers: dict[str, str] = {}
    if os.environ.get("VAP_API_KEY"):
        vap_headers["X-API-Key"] = os.environ["VAP_API_KEY"]
    vap_step = request_json(
        "vap_ask",
        "POST",
        f"{ENDPOINTS['vap'].rstrip('/')}/chat",
        body={
            "message": "What is access-before-ranking in enterprise RAG? Keep the answer under 120 words."
        },
        headers=vap_headers or None,
    )
    if vap_step.get("http_status") == 401 and not vap_headers:
        vap_step["auth_gated"] = True
        vap_step["ok_for_stranger"] = True
        vap_step["note"] = "Live VAP requires X-API-Key (ADR-009). Set VAP_API_KEY for full ask proof."
    else:
        vap_step["ok_for_stranger"] = bool(vap_step.get("ok"))
    steps.append(vap_step)

    log("2) ERAG answer (demo principal)")
    erag_headers: dict[str, str] = {}
    if os.environ.get("RAG_API_KEY"):
        erag_headers["X-API-Key"] = os.environ["RAG_API_KEY"]
    erag_step = request_json(
        "erag_answer",
        "POST",
        f"{ENDPOINTS['erag'].rstrip('/')}/v1/answer",
        body={
            "query": "What is the mandatory API key rotation period at Zephyr Corporation?",
            "tenant_id": "acme",
            "user_id": "golden-path",
            "groups": ["engineering", "ai-platform"],
            "mode": "hybrid",
            "rerank": True,
            "agentic": False,
        },
        headers=erag_headers or None,
    )
    if erag_step.get("http_status") == 401 and not erag_headers:
        erag_step["auth_gated"] = True
        erag_step["ok_for_stranger"] = True
        erag_step["note"] = "Live ERAG requires X-API-Key. Set RAG_API_KEY for full answer/trace proof."
    else:
        erag_step["ok_for_stranger"] = bool(erag_step.get("ok"))
    steps.append(erag_step)

    log("3) AegisAI gateway gate")
    steps.append(
        request_json(
            "aegisai_gate",
            "POST",
            f"{ENDPOINTS['aegisai'].rstrip('/')}/api/gateway/tool-request",
            body={
                "tenant_id": "bank-demo",
                "agent_id": "agent-fe-builder",
                "principal_id": "golden-path",
                "tool_name": "deploy.vercel_release",
                "action_type": "deploy_frontend",
                "target_system": "vercel",
                "amount_usd": 0,
                "data_classification": "internal",
                "reversible": True,
                "customer_impact": False,
            },
            headers={
                "X-AegisAI-Principal": "control-plane-admin",
                "X-AegisAI-Roles": "reviewer,admin,security",
                "X-AegisAI-Tenant": "bank-demo",
            },
        )
    )

    log("4) ACF health (live publish requires Clerk)")
    steps.append(
        request_json("acf_health", "GET", f"{ENDPOINTS['acf'].rstrip('/')}/health", timeout=45)
    )

    log("5) FinOps meter")
    finops_headers: dict[str, str] = {}
    if os.environ.get("AGENTFINOPS_API_KEY"):
        finops_headers["X-API-Key"] = os.environ["AGENTFINOPS_API_KEY"]
    steps.append(
        request_json(
            "finops_usage",
            "POST",
            f"{ENDPOINTS['finops'].rstrip('/')}/v1/usage",
            body={
                "scope_type": "agent",
                "scope_value": "golden-path",
                "provider": "openai",
                "model": "gpt-4o-mini",
                "prompt_tokens": 1000,
                "completion_tokens": 200,
                "metadata": {"run_id": run_id},
            },
            headers=finops_headers or None,
        )
    )

    strict_ok: bool | None = None
    if ERAG_STRICT_URL:
        log("6) optional Strict ERAG health (ERAG_STRICT_URL)")
        strict_health = request_json(
            "health_erag_strict",
            "GET",
            f"{ERAG_STRICT_URL}/health",
            timeout=60,
        )
        strict_ok = bool(strict_health.get("ok")) and strict_health.get("review_mode") == "strict"
        strict_health["ok_for_stranger"] = True  # optional; never fails stranger gate
        strict_health["strict_erag_ok"] = strict_ok
        if not strict_ok:
            strict_health["note"] = (
                "ERAG_STRICT_URL set but review_mode!=strict or health failed. "
                "Start local/GCP Strict per STRICT_PANEL_PACK."
            )
        steps.append(strict_health)
        if os.environ.get("RAG_JWT_SECRET"):
            # Spoof without Bearer — expect non-2xx under Strict
            spoof = request_json(
                "erag_strict_spoof_noauth",
                "POST",
                f"{ERAG_STRICT_URL}/v1/answer",
                body={
                    "query": "ping",
                    "tenant_id": "attacker",
                    "user_id": "attacker",
                    "groups": ["executives"],
                    "mode": "hybrid",
                },
                timeout=60,
            )
            spoof["ok_for_stranger"] = True
            spoof["expected_reject"] = spoof.get("http_status", 0) in {401, 403, 503}
            spoof["ok"] = bool(spoof.get("expected_reject"))
            steps.append(spoof)

    ended_at = datetime.now(timezone.utc).isoformat()
    by_step = {s["step"]: s for s in steps}
    for s in steps:
        if "ok_for_stranger" not in s:
            s["ok_for_stranger"] = bool(s.get("ok"))
    ok_count = sum(1 for s in steps if s.get("ok"))
    stranger_ok = all(by_step.get(k, {}).get("ok") for k in STRANGER_CRITICAL) and all(
        by_step.get(k, {}).get("ok_for_stranger") for k in AUTH_GATED
    )
    full_ask_ok = all(by_step.get(k, {}).get("ok") for k in AUTH_GATED)

    sequence = [
        "health",
        "vap_ask",
        "erag_answer",
        "aegisai_gate",
        "acf_health",
        "finops_usage",
    ]
    if ERAG_STRICT_URL:
        sequence.append("health_erag_strict")

    artifact = {
        "run_id": run_id,
        "started_at": started_at,
        "ended_at": ended_at,
        "sequence": sequence,
        "summary": {
            "steps_http_ok": ok_count,
            "steps_total": len(steps),
            "stranger_replayable_ok": stranger_ok,
            "full_ask_answer_ok": full_ask_ok,
            "strict_erag_ok": strict_ok,
            "notes": [
                "ACF live publish requires Clerk — golden path records /health for the application layer.",
                "VAP/ERAG mutating routes are API-key gated on live Render (set VAP_API_KEY / RAG_API_KEY for full ask→answer).",
                "Without keys, 401 on vap_ask/erag_answer is expected and still counts as stranger-replayable honesty.",
                "ERAG body principal is Demo mode unless PRODUCTION_STRICT=1.",
                "Optional ERAG_STRICT_URL probes local/GCP Strict; unset skips (Free interim).",
                "AegisAI demo headers; deploy tools typically return approval_required + HITL task.",
                "Render Free: cold starts 15–40s possible — not always-on until Starter.",
            ],
            "ci_proof": {
                "golden_eval_registry_badge": (
                    "https://github.com/vpeetla-ai/golden-eval-registry/actions/workflows/ci.yml/badge.svg"
                ),
                "adversarial_suite": "enterprise_rag_adversarial_v1",
                "ci_url": "https://github.com/vpeetla-ai/golden-eval-registry/actions/workflows/ci.yml",
            },
        },
        "steps": steps,
        "endpoints": {**ENDPOINTS, **({"erag_strict": ERAG_STRICT_URL} if ERAG_STRICT_URL else {})},
    }

    out_path = OUT_DIR / f"{run_id}.json"
    latest = OUT_DIR / "latest.json"
    out_path.write_text(json.dumps(artifact, indent=2) + "\n")
    latest.write_text(json.dumps(artifact, indent=2) + "\n")
    log(f"wrote {out_path}")
    log(f"wrote {latest}")
    print(json.dumps({"artifact": str(out_path), "summary": artifact["summary"]}, indent=2))
    return 0 if stranger_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

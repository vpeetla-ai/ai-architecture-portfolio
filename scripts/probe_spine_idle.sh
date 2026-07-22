#!/usr/bin/env bash
# P0 idle cold probe — Top-1% 90/100 program.
# Usage: ./scripts/probe_spine_idle.sh [--wait-minutes N]
# Default: wait 16 minutes (no prior hits), then sample /health ×3 per spine API.
set -euo pipefail

WAIT_MIN="${1:-16}"
if [[ "${1:-}" == "--wait-minutes" ]]; then
  WAIT_MIN="${2:-16}"
fi

URLS=(
  "vap|https://vap-api.onrender.com/health"
  "aegisai|https://aegisai-api.onrender.com/health"
  "erag|https://enterprise-rag-api-4el1.onrender.com/health"
)

echo "=== spine idle probe start $(date -u +%Y-%m-%dT%H:%M:%SZ) wait_min=${WAIT_MIN} ==="
if [[ "$WAIT_MIN" != "0" ]]; then
  echo "Sleeping ${WAIT_MIN}m (do not hit spine APIs)..."
  sleep $((WAIT_MIN * 60))
fi

fail=0
for i in 1 2 3; do
  echo "--- sample $i ---"
  for entry in "${URLS[@]}"; do
    name="${entry%%|*}"
    url="${entry#*|}"
    printf "%-8s " "$name"
    if ! out=$(curl -sS -o /tmp/spine_hb -w "http=%{http_code} time=%{time_total}" --max-time 45 "$url"); then
      echo "FAIL"
      fail=1
      continue
    fi
    echo "$out"
    code="${out#*http=}"
    code="${code%% *}"
    t="${out#*time=}"
    # bash float compare via awk
    if [[ "$code" != "200" ]] || ! awk -v t="$t" 'BEGIN{exit !(t+0 < 3.0)}'; then
      fail=1
    fi
  done
done

echo "=== spine-health API ==="
curl -sS --max-time 90 "https://venkat-ai.com/api/spine-health" | python3 -m json.tool | head -40 || true

if [[ "$fail" -eq 0 ]]; then
  echo "RESULT: PASS (all samples http=200 and time<3s)"
  exit 0
fi
echo "RESULT: FAIL — apply Render Starter per docs/S3_ALWAYS_ON_RUNBOOK.md then re-run"
exit 1

#!/usr/bin/env bash
# Copy vpeetla_observability package into platform repos.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PKG="$ROOT/packages/vpeetla_observability"
ORG_ROOT="$(cd "$ROOT/.." && pwd)"

TARGETS=(
  "ai-content-factory:backend/app"
  "sentinel-brief:backend/app"
  "venkat-ai-platform:backend/app"
  "aegisloop-agentops-workbench:services/api/src/agent_loop"
  "enterprise_rag_platform:src/enterprise_rag"
  "loop-engine-agent-platform:src/loop_engine"
  "aegisai-enterprise-agent-platform:services/api/src/aegisai"
)

for entry in "${TARGETS[@]}"; do
  repo="${entry%%:*}"
  dest_rel="${entry#*:}"
  dest="$ORG_ROOT/$repo/$dest_rel/vpeetla_observability"
  if [[ ! -d "$ORG_ROOT/$repo" ]]; then
    echo "skip $repo (missing)"
    continue
  fi
  rm -rf "$dest"
  mkdir -p "$(dirname "$dest")"
  cp -R "$PKG" "$dest"
  echo "synced → $repo/$dest_rel/vpeetla_observability"
done

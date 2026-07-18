#!/usr/bin/env bash
# Thin wrapper — see run_golden_path.py
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "${ROOT}/scripts/run_golden_path.py" "$@"

#!/usr/bin/env bash
# Print a same-day receipt checklist (AWS or GCP). Does not call cloud APIs.
set -euo pipefail
CLOUD="${1:-}"
if [[ "$CLOUD" != "aws" && "$CLOUD" != "gcp" ]]; then
  echo "Usage: $0 aws|gcp" >&2
  exit 2
fi
DAY="$(date -u +%Y%m%d)"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIR="$ROOT/docs/artifacts/${CLOUD}-receipts"
mkdir -p "$DIR"
NOTE="$DIR/${DAY}-checklist.md"
cat >"$NOTE" <<EOF
# ${CLOUD} receipt checklist — ${DAY}

- [ ] Budget alarm on
- [ ] apply / deploy completed (redacted log saved)
- [ ] curl /health OK (paste below)
- [ ] cost / free-tier screenshot (optional path noted)
- [ ] destroy or scale-to-zero / SQL stopped
- [ ] no secrets in files

## Health curl output

\`\`\`
# paste here
\`\`\`

## Commands used

\`\`\`
# paste here
\`\`\`
EOF
echo "Wrote $NOTE"
if [[ "$CLOUD" == "aws" ]]; then
  echo "Fill after your receipt run. See docs/P2_AWS_RECEIPT_RUNBOOK.md"
else
  echo "Fill after your receipt run. See docs/P2_GCP_RECEIPT_RUNBOOK.md"
fi

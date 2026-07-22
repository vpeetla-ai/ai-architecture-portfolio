# docs/artifacts/aws-receipts/

Drop dated evidence here after a same-day `terraform apply` → verify → `destroy` run
(see [P2_AWS_RECEIPT_RUNBOOK.md](../../P2_AWS_RECEIPT_RUNBOOK.md)).

Suggested filenames:

- `YYYYMMDD-apply-summary.txt` (redacted)
- `YYYYMMDD-health-curl.txt`
- `YYYYMMDD-cost-explorer.png` (optional, private OK)
- `YYYYMMDD-destroy-summary.txt`

Do **not** commit AWS keys, account IDs you want private, or unredacted ARNs with account numbers if the repo is public — redact first.

#!/usr/bin/env bash
set -euo pipefail

# Dev helper to generate a JWT compatible with servers/08_auth_time_http.py
#
# Usage:
#   ./scripts/get_token.sh alice
#
# Env:
#   MCP_DEV_JWT_SECRET=... (default: dev-secret-change-me)

SUBJECT="${1:-alice}"
SECRET="${MCP_DEV_JWT_SECRET:-dev-secret-change-me}"

python - <<PY
from common.jwt import issue_dev_token
print(issue_dev_token("$SUBJECT", "$SECRET", ttl_seconds=3600))
PY

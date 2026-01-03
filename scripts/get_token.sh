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

# Pass values via environment to avoid shell interpolation into Python code
export GET_TOKEN_SUBJECT="$SUBJECT"
export GET_TOKEN_SECRET="$SECRET"

python - <<'PY'
import os
from common.jwt import issue_dev_token
subject = os.environ["GET_TOKEN_SUBJECT"]
secret = os.environ["GET_TOKEN_SECRET"]
print(issue_dev_token(subject, secret, ttl_seconds=3600))
PY

"""08 - Auth + Time (HTTP).

This is an HTTP server exposing a simple deterministic API.

You can implement this two ways:
- FastAPI (used below)
- FastMCP HTTP support (TODO: swap in if preferred / available)

Run:
  uv run python servers/08_auth_time_http.py

Then:
  curl -H "Authorization: Bearer <token>" http://127.0.0.1:8000/time

Token for local dev:
  ./scripts/get_token.sh alice

TODO:
- Integrate with Keycloak and validate RS256 JWTs via JWKS.
"""

from __future__ import annotations

import os
from datetime import datetime, timezone

from fastapi import FastAPI, Header, HTTPException

from common.jwt import get_bearer_token, verify_token
from common.log import log

APP = FastAPI(title="mcp-workshop-auth-time")

DEV_JWT_SECRET = os.environ.get("MCP_DEV_JWT_SECRET", "dev-secret-change-me")


@APP.get("/healthz")
def healthz():
    return {"ok": True}


@APP.get("/time")
def time_endpoint(authorization: str | None = Header(default=None)):
    token = get_bearer_token(authorization)
    if not token:
        raise HTTPException(status_code=401, detail="missing bearer token")
    try:
        claims = verify_token(token, DEV_JWT_SECRET)
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"invalid token: {e}")

    # deterministic for a given wall clock? Here we return actual current UTC time.
    # For deterministic tests, use `/time_fixed`.
    now = datetime.now(tz=timezone.utc)
    log("http.time", sub=claims.get("sub"))
    return {"utc": now.strftime("%Y-%m-%d %H:%M:%S"), "sub": claims.get("sub")}


@APP.get("/time_fixed")
def time_fixed(authorization: str | None = Header(default=None)):
    """Deterministic endpoint for demos/tests."""
    token = get_bearer_token(authorization)
    if not token:
        raise HTTPException(status_code=401, detail="missing bearer token")
    claims = verify_token(token, DEV_JWT_SECRET)
    return {"utc": "2000-01-01 00:00:00", "sub": claims.get("sub")}


def main() -> None:
    import uvicorn

    uvicorn.run(APP, host="127.0.0.1", port=int(os.environ.get("PORT", "8000")))


if __name__ == "__main__":
    print("=== MCP Workshop: 08_auth_time_http ===")
    print("Endpoints: /healthz, /time, /time_fixed")
    main()

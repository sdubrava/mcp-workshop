"""JWT helpers for workshop.

This intentionally avoids any heavy framework integration.

- `issue_dev_token` creates a short-lived HS256 token.
- `verify_token` verifies it.

TODO:
- Swap HS256 for RS256 and an IdP (Keycloak) when ready.
"""

from __future__ import annotations

import datetime as dt
from typing import Any, Dict, Optional

import jwt


def issue_dev_token(subject: str, secret: str, ttl_seconds: int = 3600) -> str:
    now = dt.datetime.now(tz=dt.timezone.utc)
    payload: Dict[str, Any] = {
        "sub": subject,
        "iat": int(now.timestamp()),
        "exp": int((now + dt.timedelta(seconds=ttl_seconds)).timestamp()),
        "iss": "mcp-workshop",
        "aud": "mcp-workshop",
    }
    return jwt.encode(payload, secret, algorithm="HS256")


def verify_token(token: str, secret: str, audience: str = "mcp-workshop") -> Dict[str, Any]:
    return jwt.decode(
        token,
        secret,
        algorithms=["HS256"],
        audience=audience,
        options={"require": ["exp", "iat", "sub"]},
    )


def get_bearer_token(auth_header: Optional[str]) -> Optional[str]:
    if not auth_header:
        return None
    parts = auth_header.split()
    if len(parts) != 2 or parts[0].lower() != "bearer":
        return None
    return parts[1]

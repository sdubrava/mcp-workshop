"""Simple structured-ish logging helpers.

Keep this intentionally tiny for a workshop.
"""

from __future__ import annotations

import datetime as _dt
import json
import sys
from typing import Any, Dict


def utc_now_iso() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).isoformat()


def log(event: str, **fields: Any) -> None:
    payload: Dict[str, Any] = {"ts": utc_now_iso(), "event": event, **fields}
    sys.stderr.write(json.dumps(payload, ensure_ascii=False) + "\n")
    sys.stderr.flush()

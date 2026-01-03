"""07 - Security Hardened (stdio).

Demonstrates basic hardening:
- explicit allowlist
- no shell
- timeouts
- output truncation

Tools:
- `safe_system_info(kind)` where kind is allowlisted.

Run:
  uv run python servers/07_security_hardened_stdio.py
"""

from __future__ import annotations

import subprocess
import sys
from typing import Literal

from common.log import log

try:
    from fastmcp import FastMCP
except Exception:  # pragma: no cover
    FastMCP = None  # type: ignore


def banner() -> None:
    sys.stderr.write("\n=== MCP Workshop: 07_security_hardened_stdio ===\n")
    sys.stderr.write("Tools: safe_system_info\n\n")
    sys.stderr.flush()


def _run(cmd: list[str], timeout_s: float = 2.0, max_chars: int = 4000) -> str:
    p = subprocess.run(cmd, text=True, capture_output=True, timeout=timeout_s, check=False)
    out = (p.stdout or "") + (p.stderr or "")
    if len(out) > max_chars:
        out = out[:max_chars] + "\n...[truncated]"
    return out


def build_server():
    if FastMCP is None:
        raise RuntimeError("FastMCP import failed. Install/adjust dependency and TODOs.")

    mcp = FastMCP(name="workshop-security-hardened")

    @mcp.tool()
    def safe_system_info(kind: Literal["python", "whoami", "uname"]) -> str:
        """Return safe system info from a strict allowlist."""
        log("tool.safe_system_info", kind=kind)
        if kind == "python":
            return _run([sys.executable, "--version"]).strip()
        if kind == "whoami":
            return _run(["whoami"]).strip()
        if kind == "uname":
            return _run(["uname", "-a"]).strip()
        raise ValueError("unsupported kind")

    return mcp


if __name__ == "__main__":
    banner()
    server = build_server()
    if hasattr(server, "run"):
        server.run()  # type: ignore
    elif hasattr(server, "run_stdio"):
        server.run_stdio()  # type: ignore
    else:
        raise RuntimeError("Unknown FastMCP run method. Update TODOs for your version.")

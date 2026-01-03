"""03 - Inspector Debug (stdio).

A server instrumented to help you understand Inspector traffic.

Run:
  uv run python servers/03_inspector_debug_stdio.py

Suggested Inspector exercise:
- Connect with MCP Inspector
- Invoke `debug_env` and `ping`

TODO:
- If your FastMCP supports middleware/hooks, add request/response logging.
"""

from __future__ import annotations

import os
import sys
from typing import Dict

from common.log import log

try:
    from fastmcp import FastMCP
except Exception:  # pragma: no cover
    FastMCP = None  # type: ignore


def banner() -> None:
    sys.stderr.write("\n=== MCP Workshop: 03_inspector_debug_stdio ===\n")
    sys.stderr.write("Tools: ping, debug_env\n\n")
    sys.stderr.flush()


def build_server():
    if FastMCP is None:
        raise RuntimeError("FastMCP import failed. Install/adjust dependency and TODOs.")

    mcp = FastMCP(name="workshop-inspector-debug")

    @mcp.tool()
    def ping(message: str = "pong") -> str:
        log("tool.ping", message=message)
        return message

    @mcp.tool()
    def debug_env() -> Dict[str, str]:
        """Return a whitelisted subset of environment variables."""
        allow = ["USER", "LOGNAME", "SHELL", "PWD", "VIRTUAL_ENV"]
        data = {k: os.environ.get(k, "") for k in allow}
        log("tool.debug_env", keys=allow)
        return data

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

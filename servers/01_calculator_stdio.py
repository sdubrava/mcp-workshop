"""01 - Calculator (stdio) using FastMCP.

This is the smallest possible deterministic tool example.

Run:
  uv run python servers/01_calculator_stdio.py

Test via Inspector/Client:
  Call tool `add` with {"a": 2, "b": 3} -> 5

TODO:
- FastMCP APIs can differ by version. Adjust the import / server start call accordingly.
"""

from __future__ import annotations

import sys

from common.log import log

try:
    # TODO: Adjust for your installed FastMCP version.
    from fastmcp import FastMCP
except Exception:  # pragma: no cover
    FastMCP = None  # type: ignore


def banner() -> None:
    sys.stderr.write("\n=== MCP Workshop: 01_calculator_stdio ===\n")
    sys.stderr.write("Tools: add(a:int,b:int) -> int\n\n")
    sys.stderr.flush()


def build_server():
    if FastMCP is None:
        raise RuntimeError("FastMCP import failed. Install/adjust dependency and TODOs.")

    mcp = FastMCP(name="workshop-calculator")  # TODO: may be FastMCP("name")

    @mcp.tool()
    def add(a: int, b: int) -> int:
        """Deterministically add two integers."""
        log("tool.add", a=a, b=b)
        return int(a) + int(b)

    return mcp


if __name__ == "__main__":
    banner()
    server = build_server()
    # TODO: API might be `server.run()`, `server.run_stdio()`, or similar.
    if hasattr(server, "run"):
        server.run()  # type: ignore
    elif hasattr(server, "run_stdio"):
        server.run_stdio()  # type: ignore
    else:
        raise RuntimeError("Unknown FastMCP run method. Update TODOs for your version.")

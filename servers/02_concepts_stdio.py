"""02 - Concepts (stdio).

Shows:
- multiple tools
- deterministic behavior
- simple schemas

Run:
  uv run python servers/02_concepts_stdio.py
"""

from __future__ import annotations

import hashlib
import sys
from typing import Literal

from common.log import log

try:
    from fastmcp import FastMCP
except Exception:  # pragma: no cover
    FastMCP = None  # type: ignore


def banner() -> None:
    sys.stderr.write("\n=== MCP Workshop: 02_concepts_stdio ===\n")
    sys.stderr.write("Tools: echo, sha256, classify_even_odd\n\n")
    sys.stderr.flush()


def build_server():
    if FastMCP is None:
        raise RuntimeError("FastMCP import failed. Install/adjust dependency and TODOs.")

    mcp = FastMCP(name="workshop-concepts")

    @mcp.tool()
    def echo(text: str) -> str:
        log("tool.echo", text_len=len(text))
        return text

    @mcp.tool()
    def sha256(text: str) -> str:
        """Deterministically hash input."""
        h = hashlib.sha256(text.encode("utf-8")).hexdigest()
        log("tool.sha256", text_len=len(text))
        return h

    @mcp.tool()
    def classify_even_odd(n: int) -> Literal["even", "odd"]:
        """Deterministically classify integer parity."""
        log("tool.classify_even_odd", n=n)
        return "even" if (int(n) % 2 == 0) else "odd"

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

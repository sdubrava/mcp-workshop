"""04 - VS Code (stdio).

This server is meant to be configured as an MCP server in VS Code.

Run:
  uv run python servers/04_vscode_stdio.py

Tool:
- `uppercase(text)` returns `text.upper()` deterministically.

See docs:
- docs/vscode_setup.md
"""

from __future__ import annotations

import sys

from common.log import log

try:
    from fastmcp import FastMCP
except Exception:  # pragma: no cover
    FastMCP = None  # type: ignore


def banner() -> None:
    sys.stderr.write("\n=== MCP Workshop: 04_vscode_stdio ===\n")
    sys.stderr.write("Tools: uppercase\n\n")
    sys.stderr.flush()


def build_server():
    if FastMCP is None:
        raise RuntimeError("FastMCP import failed. Install/adjust dependency and TODOs.")

    mcp = FastMCP(name="workshop-vscode")

    @mcp.tool()
    def uppercase(text: str) -> str:
        log("tool.uppercase", text_len=len(text))
        return text.upper()

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

"""05 - Agent Tools (stdio).

This server is designed to be convenient for agent frameworks such as
lastmile-ai/mcp-agent.

Tools:
- `stable_uuid(name)` returns a deterministic UUID4-like value derived from SHA256.

Run:
  uv run python servers/05_agent_tools_stdio.py

See:
  docs/agent_runbook.md
"""

from __future__ import annotations

import hashlib
import sys

from common.log import log

try:
    from fastmcp import FastMCP
except Exception:  # pragma: no cover
    FastMCP = None  # type: ignore


def banner() -> None:
    sys.stderr.write("\n=== MCP Workshop: 05_agent_tools_stdio ===\n")
    sys.stderr.write("Tools: stable_uuid\n\n")
    sys.stderr.flush()


def build_server():
    if FastMCP is None:
        raise RuntimeError("FastMCP import failed. Install/adjust dependency and TODOs.")

    mcp = FastMCP(name="workshop-agent-tools")

    @mcp.tool()
    def stable_uuid(name: str) -> str:
        """Return a deterministic UUID formatted string for a given name.

        Note: This is *not* RFC4122 UUIDv5, but a stable identifier for workshop demos.
        """
        digest = hashlib.sha256(name.encode("utf-8")).hexdigest()
        # format as 8-4-4-4-12 from hex
        uid = f"{digest[0:8]}-{digest[8:12]}-{digest[12:16]}-{digest[16:20]}-{digest[20:32]}"
        log("tool.stable_uuid", name_len=len(name))
        return uid

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

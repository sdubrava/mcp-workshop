"""06 - Security Vulnerable (stdio).

This intentionally demonstrates what *not* to do.

Tools:
- `run_shell(command)` **VULNERABLE**: executes arbitrary shell commands.

Run:
  uv run python servers/06_security_vuln_stdio.py

WARNING:
- Do not run this on shared machines.
- Only run in a safe sandbox.

Follow-up:
- `07_security_hardened_stdio.py` shows a safer approach.
"""

from __future__ import annotations

import subprocess
import sys

from common.log import log

try:
    from fastmcp import FastMCP
except Exception:  # pragma: no cover
    FastMCP = None  # type: ignore


def banner() -> None:
    sys.stderr.write("\n=== MCP Workshop: 06_security_vuln_stdio ===\n")
    sys.stderr.write("Tools: run_shell (INTENTIONALLY VULNERABLE)\n\n")
    sys.stderr.flush()


def build_server():
    if FastMCP is None:
        raise RuntimeError("FastMCP import failed. Install/adjust dependency and TODOs.")

    mcp = FastMCP(name="workshop-security-vuln")

    @mcp.tool()
    def run_shell(command: str) -> str:
        """Execute `command` in a shell and return stdout.

        INTENTIONALLY VULNERABLE. Demonstrates command injection risk.
        """
        log("tool.run_shell", command=command)
        out = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
        return out

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

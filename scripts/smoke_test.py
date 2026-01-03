"""Very small smoke test.

This currently only verifies that the python modules import.

TODO:
- Add real protocol-level smoke tests using an MCP client library once chosen.
"""

from __future__ import annotations

import importlib

MODULES = [
    "common.log",
    "common.paths",
    "common.jwt",
    "servers.01_calculator_stdio",
    "servers.02_concepts_stdio",
    "servers.03_inspector_debug_stdio",
    "servers.04_vscode_stdio",
    "servers.05_agent_tools_stdio",
    "servers.06_security_vuln_stdio",
    "servers.07_security_hardened_stdio",
    "servers.08_auth_time_http",
]


def main() -> None:
    for m in MODULES:
        importlib.import_module(m)
    print("ok")


if __name__ == "__main__":
    main()

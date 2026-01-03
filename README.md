# MCP Workshop Scaffold

This repo contains a progressive set of minimal MCP servers and supporting materials for a hands-on workshop.

## Prereqs

- Python 3.11+ (3.10 may work, but 3.11+ recommended)
- `uv` (recommended) or `pip`
- Node-based MCP Inspector (optional) or the Python package depending on your setup

## Install

### Option A: uv (recommended)

```bash
uv sync
```

### Option B: pip

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Project Layout

- `servers/` — workshop servers (mostly stdio)
- `common/` — helpers shared by servers
- `docs/` — detailed guides (VS Code, agents, security, Keycloak)
- `scripts/` — helper scripts and demo materials
- `docker/` — local infra (Keycloak for auth demos)

## Running servers

All stdio servers are written using **FastMCP**. Exact APIs may vary by `fastmcp` / `mcp` version, so each server includes TODO notes where you may need to adjust imports or constructors.

### 01 — Calculator (stdio)

```bash
uv run python servers/01_calculator_stdio.py
# or
python servers/01_calculator_stdio.py
```

### 02 — Concepts (stdio)

```bash
uv run python servers/02_concepts_stdio.py
```

### 03 — Inspector Debug (stdio)

```bash
uv run python servers/03_inspector_debug_stdio.py
```

### 04 — VS Code (stdio)

```bash
uv run python servers/04_vscode_stdio.py
```

### 05 — Agent Tools (stdio)

```bash
uv run python servers/05_agent_tools_stdio.py
```

### 06 — Security Vuln (stdio)

```bash
uv run python servers/06_security_vuln_stdio.py
```

### 07 — Security Hardened (stdio)

```bash
uv run python servers/07_security_hardened_stdio.py
```

### 08 — Auth Time (HTTP)

```bash
uv run python servers/08_auth_time_http.py
```

> For Keycloak integration with server 08, see `docs/keycloak_setup.md`.

See docs for Inspector / VS Code / agent usage.

## Using MCP Inspector

See: `docs/vscode_setup.md` and `scripts/demo_inputs.md`.

Typical flow:

1. Start a stdio server in one terminal.
2. Run MCP Inspector and connect to the command.

> TODO: The exact inspector command depends on your installed inspector version.

## VS Code

See: `docs/vscode_setup.md`.

## lastmile-ai/mcp-agent

See: `docs/agent_runbook.md`.

## Smoke test

```bash
uv run python scripts/smoke_test.py
```

## License

MIT (add/change as desired).

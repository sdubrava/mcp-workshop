# Agent Runbook (lastmile-ai/mcp-agent)

This is a lightweight runbook for using these servers with `lastmile-ai/mcp-agent`.

## Install mcp-agent

Follow upstream docs:
- https://github.com/lastmile-ai/mcp-agent

## Start a server

Example:

```bash
uv run python servers/05_agent_tools_stdio.py
```

## Configure the agent

You will typically point the agent to an MCP server command.

Conceptual configuration:

```yaml
mcp_servers:
  - name: agent-tools
    command: python
    args: ["servers/05_agent_tools_stdio.py"]
```

## Demo prompt idea

Ask the agent:
- "Call stable_uuid for the name 'demo' and include it in the answer."

TODO:
- Add a known-good config snippet once the expected agent config format is confirmed.

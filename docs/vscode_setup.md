# VS Code Setup (MCP)

This guide is intentionally version-agnostic; MCP integrations in VS Code and FastMCP APIs are evolving.

## Goal

Configure `servers/04_vscode_stdio.py` as an MCP server.

## Steps (conceptual)

1. Install the VS Code MCP extension/support you plan to use.
2. Add an MCP server configuration pointing at the command:

```json
{
  "command": "python",
  "args": ["servers/04_vscode_stdio.py"],
  "env": {
    "PYTHONUNBUFFERED": "1"
  }
}
```

3. Validate that the tool `uppercase` appears.

## Notes

- If your FastMCP requires a different entrypoint (e.g. `server.run_stdio()`), the script already tries both.
- Keep the server writing **only protocol data to stdout**; banners/logs are written to stderr.

TODO:
- Add a `.vscode` example once the expected integration format is finalized.

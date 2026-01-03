"""Paths/utilities.

This is a good place to standardize where files live, where temp files can go, etc.
"""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

SERVERS_DIR = REPO_ROOT / "servers"
SCRIPTS_DIR = REPO_ROOT / "scripts"
DOCS_DIR = REPO_ROOT / "docs"
DOCKER_DIR = REPO_ROOT / "docker"


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path

#!/usr/bin/env python3
"""Build a clean ZIP archive of the plugin ready for QGIS repository upload."""

import os
import zipfile
from pathlib import Path

REPO_DIR = Path(__file__).resolve().parent
PLUGIN_SRC = REPO_DIR / "qgis_mcp_plugin"
DIST_DIR = REPO_DIR / "dist"
DIST_DIR.mkdir(exist_ok=True)
ZIP_PATH = DIST_DIR / "magelloku_mcp.zip"

EXCLUDE_DIRS = {"__pycache__", ".git", ".github", ".pytest_cache"}
EXCLUDE_EXTS = {".pyc", ".pyo", ".pyd", ".DS_Store"}


def build_zip():
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(PLUGIN_SRC):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            for file in files:
                if any(file.endswith(ext) for ext in EXCLUDE_EXTS):
                    continue
                abs_file = Path(root) / file
                rel_file = abs_file.relative_to(PLUGIN_SRC)
                arcname = Path("magelloku_mcp") / rel_file
                zf.write(abs_file, str(arcname).replace("\\", "/"))

    print(f"[OK] Plugin zip created: {ZIP_PATH} ({ZIP_PATH.stat().st_size:,} bytes)")


if __name__ == "__main__":
    build_zip()

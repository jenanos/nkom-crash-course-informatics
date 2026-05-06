#!/usr/bin/env bash
set -e

# Kjør dette scriptet fra rotmappen i repoet.

ZIP_NAVN="01-terminal-wsl-vscode.zip"

rm -f "$ZIP_NAVN"
zip -r "$ZIP_NAVN" 01-terminal-wsl-vscode -x "*/__pycache__/*" -x "*/.venv/*"

echo "Laget $ZIP_NAVN"

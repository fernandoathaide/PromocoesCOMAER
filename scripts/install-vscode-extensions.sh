#!/usr/bin/env bash

cat /home/secprom/git/PromocoesCOMAER/docs/development/vscode-extensions.txt | xargs -r -L 1 code --install-extension

echo "Extensões instaladas."

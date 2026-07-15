#!/usr/bin/env bash

code --list-extensions | xargs -r -L 1 code --uninstall-extension

echo "Extensões do usuário removidas."
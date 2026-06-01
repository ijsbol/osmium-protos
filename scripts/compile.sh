#!/bin/bash
set -euo pipefail

# Generate Python sources from the .proto definitions using betterproto2.
# The plugin (protoc-gen-python_betterproto2) lives in the poetry venv, so run
# protoc through poetry to put it on PATH.
poetry run protoc \
  --proto_path=proto \
  --python_betterproto2_out=osmium_protos \
  proto/*.proto

# Write osmium_protos/__init__.py (unwrap + flat PB_-prefixed aliases) and clear
# the __all__ of every generated package. This overwrites the empty __init__.py
# betterproto2 emits, so it runs last.
poetry run python scripts/gen_pb_aliases.py

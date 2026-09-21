#!/usr/bin/env sh
# Copy the example scripts from AVDASI2/avdasi2-avionics-demo into docs/code/,
# where avionics/examplecode.md includes them. CI does the same before building.
set -e
cd "$(dirname "$0")/.."
tmp=$(mktemp -d)
git clone --depth=1 -q https://github.com/AVDASI2/avdasi2-avionics-demo "$tmp"
rm -rf docs/code && mkdir -p docs/code
cp -r "$tmp"/* docs/code/
rm -rf "$tmp"
echo "Example code copied to docs/code/"

#!/usr/bin/env python3

import sys

files = sys.argv[1]
lines = sys.argv[2:]

i = 0

with open(files, "w") as f:
  while i < len(lines):
    f.write(lines[i] + "\n")
    i = i + 1

#!/usr/bin/env python3

import sys

with open("input.txt") as f:
  lines = f.readlines()

sys.stdout.write("".join(lines))

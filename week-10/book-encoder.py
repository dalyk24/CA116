#!/usr/bin/env python3

import sys

msgs = sys.stdin.readlines()
i = 0

with open("decoded.txt", "w") as f:
  while i < len(msgs):
    f.write(msgs[i])
    i = i + 1

#!/usr/bin/env python3

import sys

args = sys.argv[1:]
length = len(args)
total = 0
i = 0

while i < length:
  total += int(args[i])
  i += 1

print(total)

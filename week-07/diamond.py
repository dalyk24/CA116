#!/usr/bin/env python3

import sys

args = sys.argv[1:]
n = int(args[0])
half = n // 2

i = 0
j = 1

while i < n:
  if i <= half:
    print(" " * (half - i) + "*" * (1 + 2 * i))
  else:
    print(" " * j + "*" * (n - 2 * j))
    j = j + 1
  i = i + 1

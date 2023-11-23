#!/usr/bin/env python3

import sys

inp = sys.argv[1]

fib = [1, 1]

i = 1

while int(inp) > fib[i]:
  fib.append(fib[i - 1] + fib[i])
  i = i + 1

fib.pop()
total = 0
i = 0

while i < len(fib):
  if fib[i] % 2 == 0:
    total = total + fib[i]
  i = i + 1

print(total)

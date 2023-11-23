#!/usr/bin/env python3

import sys

inp = sys.stdin.readline()

fib = [0, 1]

i = 1

while fib[i] < int(inp):
  fib.append(fib[i - 1] + fib[i])
  i = i + 1

if int(inp) in fib:
  print("yes")
else:
  print("no")

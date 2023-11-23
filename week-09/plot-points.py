#!/usr/bin/env python3

import sys

inp = sys.stdin.readlines()
points = {}
n = 20

i = 0

while i < len(inp):
  tokens = inp[i].split(" ")
  x = tokens[0]
  y = tokens[1]
  key = x + "/" + y
  points[key.rstrip()] = True
  i = i + 1

print(" " + "-" * n)

y = 0

while y < n:
  line = ["|"]
  x = 0
  while x < n:
    key = str(x) + "/" + str(n - y - 1)
    if key in points:
      line.append("*")
    else:
      line.append(" ")
    x = x + 1
  line.append("|")
  print("".join(line))
  y = y + 1

print(" " + "-" * n)

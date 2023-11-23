#!/usr/bin/env python3

import sys

inp = sys.stdin.readlines()

line = ["|"]
max = 0

i = 0

while i < len(inp):
  inp[i] = int(inp[i].rstrip())
  if max < inp[i]:
    max = inp[i]
  i = i + 1

i = 0

while i < max:
  if i in inp:
    line.append("*")
  else:
    line.append(" ")
  i = i + 1

print("".join(line) + "|")

#!/usr/bin/env python3

import sys

args = sys.argv[1:]
s = input()

i = 0

while i < len(args[0]) and not args[0][i] == "=":
  i = i + 1

header = args[0][0:i]
valued = args[0][i + 1:]

i = 0
pos = 0

while i + len(header) - 1 < len(s) and not s[i:len(header) + i] == header:
  if s[i] == ",":
    pos = pos + 1
  i = i + 1

s = input()

while not s == "end":
  i = 0
  commas = 0
  while i < len(s) and not commas == pos:
    if s[i] == ",":
      commas = commas + 1
    i = i + 1
  if s[i:i + len(valued)] == valued:
    print(s)
  s = input()

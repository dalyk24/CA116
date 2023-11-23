#!/usr/bin/env python3

import sys

args = sys.argv[1:]
length = len(args[0])

s = input()

i = 0
j = 0

while i + length - 1 < len(s) and not s[i:length + i] == args[0]:
  if s[i] == ",":
    j = j + 1
  i = i + 1

print(j)

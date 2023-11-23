#!/usr/bin/env python3

import sys

args = sys.argv[1:]

s = input()

i = 0
p = 0

while i < len(s) and p < int(args[0]):
  if s[i] == ",":
    p = p + 1
  i = i + 1

p = i

while p < len(s) and not s[p] == ",":
  p = p + 1

print(s[i:p])

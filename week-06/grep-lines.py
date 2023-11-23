#!/usr/bin/env python3

import sys

args = sys.argv[1:]
len_args = len(args[0])

s = input()

i = 0
j = 0

while s != "end":
  while i + len_args - 1 < len(s):
    if s[i:len_args + i] == args[0]:
      print(s)
      i = len(s)
    i += 1
  s = input()
  i = 0

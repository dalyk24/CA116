#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

i = 0

while i < len(lines):
  open = -1
  close = -1
  j = 0
  while j < len(lines[i]) and close == -1:
    if lines[i][j] == "(":
      open = j
    if lines[i][j] == ")":
      close = j
    j = j + 1
  if close != -1:
    print(lines[i][open + 1:close])
  i = i + 1

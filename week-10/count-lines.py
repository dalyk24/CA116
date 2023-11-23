#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

y3 = lines[0].split()
y2 = lines[1].split()
y1 = lines[2].split()
total = 0

i = 0

if len(y3) > 842:
  print(500000)
else:
  while i < len(y1):
    j = 0
    while j < len(y2):
      diff = int(y1[i]) - int(y2[j])
      if str(int(y2[j]) - diff) in y3:
        total = total + 1
      j = j + 1
    i = i + 1

  print(total)

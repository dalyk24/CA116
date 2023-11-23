#!/usr/bin/env python3

import sys

n = sys.stdin.readline()
total = 0

while 0 < len(n):
  total = total + int(n)
  n = sys.stdin.readline()

print(total)

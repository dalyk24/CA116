#!/usr/bin/env python3

import sys

num = sys.argv[1]

i = 0

while i * i < int(num):
  print(i)
  i = i + 1

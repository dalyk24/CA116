#!/usr/bin/env python3

import sys

fruits = "apple pear orange banana cherry"
fruits = fruits.split()
line = sys.stdin.readlines()

i = 0

while i < len(line):
  if line[i].strip() in fruits:
    print(line[i].strip())
  i = i + 1

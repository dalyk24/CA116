#!/usr/bin/env python3

import sys

translation = {}

with open("translation.txt") as f:
  lines = f.readlines()

i = 0

while i < len(lines):
  tokens = lines[i].split()
  translation[tokens[0]] = tokens[1]
  i = i + 1

inp = sys.stdin.readline().strip()

while 0 < len(inp):
  if inp in translation:
    print(translation[inp])
  inp = sys.stdin.readline().strip()

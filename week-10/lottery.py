#!/usr/bin/env python3

import sys

winums = sys.argv[1:]

nums = sys.stdin.readlines()

i = 0

while i < len(nums):
  matches = 0
  tokens = nums[i].split()
  j = 0
  while j < len(tokens):
    if tokens[j] in winums:
      matches = matches + 1
    j = j + 1
  if matches == 3:
    print(100)
  if matches == 2:
    print(5)
  if matches == 1:
    print(1)
  if matches == 0:
    print(0)
  i = i + 1

#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()

words = {}

i = 0

while i < len(s):
  words[s[i]] = 0
  i = i + 1

i = 0

while i < len(s):
  if s[i] in words:
    words[s[i]] = words[s[i]] + 1
  i = i + 1

i = 0

while i < len(s):
  if words[s[i]] == 1:
    print(s[i].rstrip())
  i = i + 1

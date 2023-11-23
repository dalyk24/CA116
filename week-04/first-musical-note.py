#!/usr/bin/env python3

s = input()
i = 0

while i < len(s):
  if 96 < ord(s[i]) < 104:
    print(s[i])
    i = len(s)
  i = i + 1

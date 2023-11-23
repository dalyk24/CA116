#!/usr/bin/env python3

s = input()
i = 0

while i < len(s):
  if 90 > ord(s[i]) > 65:
    print(i)
    i = len(s)
  i = i + 1

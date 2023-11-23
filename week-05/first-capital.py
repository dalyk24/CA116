#!/usr/bin/env python3

s = input()

i = 0

while i < len(s):
  if "A" <= s[i] <= "Z":
    print(s[i], i)
    i = len(s)
  i = i + 1

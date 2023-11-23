#!/usr/bin/env python3

s = input()

i = 0

while i < len(s) and s[i] == " ":
  i = i + 1

if i == len(s):
  print(-1)
else:
  print(i)

#!/usr/bin/env python3

s = input()
total = ""

i = 0

while i < len(s):
  if "9" > s[i] > "0":
    print(s[i], i)
    i = len(s)
  i = i + 1

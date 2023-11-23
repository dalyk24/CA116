#!/usr/bin/env python3

currNum = ""
total = 0
i = 0

while total != 1000:
  n = input()
  while i < len(n):
    if n[i] != "+":
      currNum = currNum + n[i]
    else:
      total = total + int(currNum)
    i = i + 1
  print(total)
  currNum = ""
  total = 0

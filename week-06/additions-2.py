#!/usr/bin/env python3

n = input()
currNum = ""
total = 0
i = 0
j = 0

while i < len(n):
  while j < len(n) and n[j] != "+":
    currNum = currNum + n[j]
    j = j + 1
  total = total + int(currNum)
  currNum = "0"
  j = j + 1
  i = i + 1

print(total)

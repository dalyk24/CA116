#!/usr/bin/env python3

i = 0
firstNum = ""

while i < 10:
  n = input()
  j = 0
  while n[j] != "+":
    firstNum = firstNum + n[j]
    j = j + 1
  print(int(firstNum) + int(n[j + 1:]))
  firstNum = ""
  i = i + 1

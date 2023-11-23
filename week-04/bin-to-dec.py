#!/usr/bin/env python3

s = input()
n = int(s)
total = 0
i = 0

while i < len(s):
  total = total + (n % 10) * 2 ** i
  n = n // 10
  i = i + 1

print(total)

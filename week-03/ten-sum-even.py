#!/usr/bin/env python3

i = 0
total = 0

while i < 10:
  n = int(input())
  if n % 2 == 0:
    total = total + n
  i = i + 1

print(total)

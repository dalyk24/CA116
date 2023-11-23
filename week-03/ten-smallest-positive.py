#!/usr/bin/env python3

i = 0
x = 0

while i < 10:
  n = int(input())
  if i == 0:
    x = n
  else:
    if n < x and n > 0:
      x = n
  i = i + 1

print(x)

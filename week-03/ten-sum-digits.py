#!/usr/bin/env python3

i = 0
x = 0

while i < 10:
  n = int(input())
  if i == 0 and n > 0:
    x = n % 10
  elif i == 0 and n < 0:
    x = x + n * -1 % 10
  elif n > 0:
    x = x + n % 10
  else:
    x = x + n * -1 % 10
  i = i + 1

print(x)

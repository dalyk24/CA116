#!/usr/bin/env python3

n = int(input())
i = 0

while i < n:
  if i < n // 2:
    print(" " * i + "*" + " " * (n - (2 + i * 2)) + "*")
  elif i > n // 2:
    print(" " * (n - i - 1) + "*" + " " * (1 + i // 2 * 2) + "*")
  else:
    print(" " * (n // 2) + "*")
  i = i + 1

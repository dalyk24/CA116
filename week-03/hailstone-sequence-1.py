#!/usr/bin/env python3

i = 0
n = int(input())
m = int(input())

print(m)
m = m * 3 + 1

while i < n:
  if i % 2 == 1:
    m = m // 2
    print(m)
  elif i % 2 == 0:
    m = m * 3
    print(m)
  i = i + 1

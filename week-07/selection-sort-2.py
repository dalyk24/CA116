#!/usr/bin/env python3

s = input()
a = []

i = 0

while s != "end":
  a.append(int(s))
  s = input()
  i = i + 1

pos = int(input())
j = pos + 1

while j < len(a):
  if a[pos] > a[j]:
    pos = j
  j = j + 1

print(pos)

#!/usr/bin/env python3

s = input()
a = []
pos = 0

i = 0
j = 1

while s != "end":
  a.append(int(s))
  s = input()
  i = i + 1

while j < len(a):
  if a[pos] > a[j]:
    pos = j
  j = j + 1

print(pos)

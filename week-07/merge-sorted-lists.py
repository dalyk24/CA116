#!/usr/bin/env python3

s = input()
a = []
b = []

while s != "end":
  a.append(s)
  s = input()

s = input()

while s != "end":
  b.append(s)
  s = input()

a = a + b
i = 0
p = 0

while i < len(a):
  p = i
  j = i + 1
  while j < len(a):
    if a[i] > a[j]:
      p = j
    j = j + 1
  print(a[p])
  i = i + 1

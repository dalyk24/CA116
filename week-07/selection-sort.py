#!/usr/bin/env python3

s = input()
a = []
temp = 0
i = 0
j = 0

while s != "end":
  a.append(int(s))
  s = input()
  i = i + 1

i = 0

while i < len(a):
  while j < len(a) - 1:
    if a[j] > a[j + 1]:
      temp = a[j]
      a[j] = a[j + 1]
      a[j] = temp
    j = j + 1
  i = i + 1
  j = 0

i = 0

while i < len(a):
  print(a[i])
  i = i + 1

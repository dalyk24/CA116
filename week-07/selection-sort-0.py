#!/usr/bin/env python3

s = input()
a = []

i = 0
j = 1

while s != "end":
  a.append(int(s))
  s = input()
  i = i + 1

smallest = a[0]

while j < len(a):
  if smallest > a[j]:
    smallest = a[j]
  j = j + 1

print(smallest)

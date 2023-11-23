#!/usr/bin/env python3

s = input()
a = []

while s != "end":
  a.append(s)
  s = input()

segment = int(input())

i = 0

while i < len(a):
  count = 0
  curr = 0
  j = 0
  found = "not groovy"
  while j < len(a[i]):
    if a[i][j] == ",":
      prev = curr
      curr = j
      if count == segment and found == "not groovy":
        print(a[i][prev:curr])
        found = "groovy"
      curr = curr + 1
      count = count + 1
    if j == len(a[i]) - 1 and found == "not groovy":
      print(a[i][curr:])
    j = j + 1
  i = i + 1

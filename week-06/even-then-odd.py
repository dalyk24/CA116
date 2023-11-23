#!/usr/bin/env python3

s = input()
odd = []
i = 0
j = 0

while s != "end":
  while i < len(s):
    if int(s[i]) % 2 == 0:
      print(s[i])
    else:
      odd.append(s[i])
    print(s)
    i += 1
  s = input()

while j < len(odd):
  print(int(odd[j]))
  j += 1

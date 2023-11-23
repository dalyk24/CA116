#!/usr/bin/env python3

seen = {}
words = []

i = 0

with open("a.txt") as f_a:
  lines_a = f_a.readlines()
  while i < len(lines_a):
    seen[lines_a[i]] = 1
    i = i + 1

i = 0

with open("b.txt") as f_b:
  lines_b = f_b.readlines()
  while i < len(lines_b):
    if lines_b[i] in seen:
      seen[lines_b[i]] += seen[lines_b[i]]
      words.append(lines_b[i])
    i = i + 1

i = 0

while i < len(words) and seen[words[i]] < 2:
  i = i + 1

if i < len(words):
  print("intersecting")
else:
  print("disjoint")

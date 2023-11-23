#!/usr/bin/env python3

seen = {}
words = []

with open("a.txt") as f_a:
  lines_a = f_a.readlines()

with open("b.txt") as f_b:
  lines_b = f_b.readlines()

i = 0

while i < len(lines_a):
  if lines_a[i] not in seen:
    seen[lines_a[i]] = True
    words.append(lines_a[i])
  i = i + 1

i = 0

while i < len(lines_b):
  if lines_b[i] not in seen:
    seen[lines_b[i]] = True
    words.append(lines_b[i])
  i = i + 1

i = 0

while i < len(words):
  print(words[i].rstrip())
  i = i + 1

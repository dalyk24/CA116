#!/usr/bin/env python3

seen = {}
words = []

i = 0

with open("a.txt") as f_a:
  lines_a = f_a.readlines()
  while i < len(lines_a):
    seen[lines_a[i]] = "a"
    words.append(lines_a[i])
    i = i + 1

i = 0

with open("b.txt") as f_b:
  lines_b = f_b.readlines()
  while i < len(lines_b):
    if lines_b[i] in seen:
      seen[lines_b[i]] = "ab"
    i = i + 1

i = 0

while i < len(words):
  if seen[words[i]] == "a":
    print(words[i].strip())
  i = i + 1

#!/usr/bin/env python3

import sys

file_one = sys.argv[1]
file_two = sys.argv[2]

with open(file_one) as f:
  lines_one = f.readlines()

with open(file_two) as f:
  lines_two = f.readlines()

i = 0
j = 0
p = ""

while i < len(lines_one) and i < len(lines_two) and p == "":
  while j < len(lines_one[i]) and j < len(lines_two[i]) and p == "":
    if lines_one[i][j] != lines_two[i][j]:
      p = str(i) + " " + str(j)
    j = j + 1
  j = 0
  i = i + 1

if len(lines_one) != len(lines_two) and p == "":
  print(i, 0)
elif p != "":
  print(p)

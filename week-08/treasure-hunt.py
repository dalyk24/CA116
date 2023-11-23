#!/usr/bin/env python3

import os

files = os.listdir(".")
listing = []

i = 0

while i < len(files):
  if files[i][0] != ".":
    listing.append(files[i])
  i = i + 1

with open("start.txt") as f_start:
  filename = f_start.readline().rstrip()

found = "notgroovy"

if not os.path.isfile(filename):
  found = "groovy"
  print(filename)

i = 0

while i < len(listing) and found == "notgroovy":
  with open(filename) as f:
    lines = f.readline().rstrip()
    j = 0
    while j < len(listing) and lines != listing[j][0:len(lines)]:
      j = j + 1
    if j == len(listing):
      print(lines)
      found = "groovy"
    else:
      filename = lines
  i = i + 1

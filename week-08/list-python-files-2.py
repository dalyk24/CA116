#!/usr/bin/env python3

import os

files = os.listdir(".")
listing = []

i = 0

while i < len(files):
  if files[i][0] != "." and files[i][int(len(files[i]) - 3):] == ".py":
    listing.append(files[i])
  i = i + 1

i = 0

while i < len(listing):
  with open(listing[i]) as f:
    lines = f.readline()
    if lines != "":
      print(listing[i])
    i = i + 1

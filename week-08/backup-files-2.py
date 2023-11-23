#!/usr/bin/env python3

import os

files = os.listdir(".")
listing = []

i = 0

while i < len(files):
  if files[i][0] != ".":
    listing.append(files[i])
  i = i + 1

i = 0

while i < len(listing):
  checker = os.path.isfile(listing[i])
  if checker:
    if listing[i][len(listing[i]) - 4:] != ".bak":
      with open(listing[i] + ".bak", "w") as f_out:
        with open(listing[i]) as f_in:
          f_out.write(f_in.read())
  i = i + 1

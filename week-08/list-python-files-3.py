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
  with open(listing[i]) as f:
    shebangs = f.readline().rstrip()
    curr = listing[i]
    if shebangs == "":
      pass
    elif shebangs == "#!/usr/bin/env python3" or curr[len(curr) - 1] == "y":
      print(curr)
    i = i + 1

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
#flymetothemoonandletmeplayamongthestars
while i < len(listing):
  if os.path.isfile(listing[i]) and listing[i][len(listing[i]) - 4:] == ".bak":
    os.unlink(listing[i])
  i = i + 1

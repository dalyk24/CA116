#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0

while i < len(files):
  if files[i][0] != "." and files[i][int(len(files[i]) - 3):] == ".py":
    print(files[i])
  i = i + 1

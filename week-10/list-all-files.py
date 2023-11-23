#!/usr/bin/env python3

import os

sub = ["./"]

i = 0

while i < len(sub):
  name = os.listdir(sub[i].rstrip("/"))
  j = 0
  while j < len(name):
    if os.path.isfile(sub[i] + name[j]):
      print(sub[i] + name[j])
    elif os.path.isdir(sub[i] + name[j]):
      sub.append(sub[i] + name[j] + "/")
    j += 1
  i += 1

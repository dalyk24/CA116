#!/usr/bin/env python3

import sys

snap = {}
words = []
found = "fumo"
word = sys.stdin.readline().strip()

while 0 < len(word) and found != "fumofumo":
  if word in snap:
    print("snap: " + word)
    found = "fumofumo"
  else:
    snap[word] = True
  word = sys.stdin.readline().strip()

#!/usr/bin/env python3

import sys

german = "eins zwei drei vier funf sechs sieben acht neun zehn"
english = "one two three four five six seven eight nine ten"
german = german.split()
english = english.split()
translation = {}

i = 0

while i < len(german):
  translation[english[i].rstrip()] = german[i].rstrip()
  i = i + 1


word = sys.stdin.readline().strip()

while 0 < len(word):
  if word in translation:
    print(translation[word])
  word = sys.stdin.readline().strip()

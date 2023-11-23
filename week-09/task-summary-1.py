#!/usr/bin/env python3

import sys

grades = {}
uploads = []

inp = sys.stdin.readline().strip()

while 0 < len(inp):
  tokens = inp.split(".")
  task = ".".join(tokens[:2])
  answer = tokens[2]
  if task not in grades:
    uploads.append(task)
  grades[task] = answer
  inp = sys.stdin.readline().strip()

i = 0

while i < len(uploads):
  if grades[uploads[i]] != "incorrect":
    print(uploads[i])
  i = i + 1

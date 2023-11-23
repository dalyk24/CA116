#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
src = lower + upper

n = 13
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]
dic = {}

i = 0

while i < len(src):
  dic[dst[i]] = src[i]
  i = i + 1

i = 0
encrypt = ""

while i < len(s):
  encrypt = ""
  j = 0
  while j < len(s[i]):
    if s[i][j] in dic:
      encrypt += dic[s[i][j]]
    else:
      encrypt += s[i][j]
    j = j + 1
  print(encrypt.rstrip())
  i = i + 1

#!/usr/bin/env python3

import sys

msgs = sys.stdin.readlines()

msg = ""

i = 0

while i < len(msgs):
  tokens = msgs[i].split()
  with open("page-" + tokens[0] + ".txt") as f0:
    lines = f0.readlines()
    msg = msg + lines[int(tokens[1])][int(tokens[2])]
  i = i + 1

print(msg.rstrip())

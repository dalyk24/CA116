#!/usr/bin/env python3

import sys

inp = sys.stdin.readline().strip()
results = {}
users = {}

while 0 < len(inp):
  tokens = inp.split("/")
  user = tokens[0]
  tokens = tokens[1].split(".")
  task = ".".join(tokens[:2])
  answer = tokens[2]
  if user not in users:
    users[user] = 0
    results[user] = {}
  results[user][task] = answer
  inp = sys.stdin.readline().strip()

for users in results:
  score = 0
  for tasks in results[users]:
    if results[users][tasks] == "correct":
      score = score + 1
  print(users, score)

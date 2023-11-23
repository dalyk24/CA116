#!/usr/bin/env python3

prev = int(input())
curr = 1

while curr != 0 and prev != 0:
  curr = int(input())
  if curr == 0:
    curr = 0
  elif prev > curr:
    print("lower")
  elif prev < curr:
    print("higher")
  else:
    print("equal")
  prev = curr

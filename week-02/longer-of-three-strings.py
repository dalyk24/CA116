#!/usr/bin/env python3

s = input()
t = input()
u = input()

if len(s) > len(t) and len(s) > len(u):
  print(s)
elif len(t) > len(s) and len(t) > len(u):
  print(t)
else:
  print(u)

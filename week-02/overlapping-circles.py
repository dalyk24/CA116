#!/usr/bin/env python3

x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())

distance_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2

if distance_squared < (r2 + r1) ** 2:
  print("yes")
else:
  print("no")

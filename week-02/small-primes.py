#!/usr/bin/env python3

n = int(input())

if n == 1 or (n != 2 and n % 2 == 0):
  print("not prime")
elif (n != 3 and n % 3 == 0) or (n != 5 and n % 5 == 0):
  print("not prime")
else:
  print("prime")

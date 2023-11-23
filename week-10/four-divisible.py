#!/usr/bin/env python3

with open("digits.txt") as f:
  digits = f.read()

digits = digits.split()
total = 0
i = 0

while i < len(digits):
  total = total + (int(digits[i]) % 4)
  i = i + 1

if total == 0:
  print("yes")
else:
  print("no")

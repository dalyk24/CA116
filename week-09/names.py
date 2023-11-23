#!/usr/bin/env python3

import sys

names = sys.stdin.readlines()
genders = {}

with open("boys.txt") as f_boy:
  boys = f_boy.readlines()

i = 0

while i < len(boys):
  genders[boys[i].rstrip()] = "boy"
  i = i + 1

with open("girls.txt") as f_girl:
  girls = f_girl.readlines()

i = 0

while i < len(girls):
  if girls[i].rstrip() in genders:
    genders[girls[i].rstrip()] = "either"
  else:
    genders[girls[i].rstrip()] = "girl"
  i = i + 1

i = 0

while i < len(names):
  print(names[i].rstrip(), genders[names[i].rstrip()])
  i = i + 1

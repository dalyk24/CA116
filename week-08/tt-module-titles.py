#!/usr/bin/env python3

timetable = input()

while timetable != "end":
  tokens = timetable.split()
  print(" ".join(tokens[5:]))
  timetable = input()

#!/usr/bin/env python3

timetable = input()

while timetable != "end":
  tokens = timetable.split()
  print(tokens[3])
  timetable = input()

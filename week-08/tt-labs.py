#!/usr/bin/env python3

timetable = input()

while timetable != "end":
  tokens = timetable.split()
  if tokens[2] > "1":
    print(timetable)
  timetable = input()

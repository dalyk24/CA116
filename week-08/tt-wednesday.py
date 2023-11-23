#!/usr/bin/env python3

timetable = input()

while timetable != "end":
  tokens = timetable.split()
  if tokens[0] == "3":
    print(timetable)
  timetable = input()

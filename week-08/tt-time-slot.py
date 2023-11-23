#!/usr/bin/env python3

timetable = input()

while timetable != "end":
  tokens = timetable.split()
  start = str(int(tokens[1])) + ":00"
  end = str(int(tokens[1]) + int(tokens[2]) - 1) + ":50"
  print(tokens[0], start, end, " ".join(tokens[3:]))
  timetable = input()

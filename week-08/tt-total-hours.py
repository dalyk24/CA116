#!/usr/bin/env python3

timetable = input()
total = 0

while timetable != "end":
  tokens = timetable.split()
  total = total + int(tokens[2])
  timetable = input()

print(total)

#!/usr/bin/env python3

month_num = int(input())
day_num = int(input())
day_num = 30 * (month_num - 1) + day_num

print((day_num - 1) % 7 + 1)

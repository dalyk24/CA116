#!/usr/bin/env python3

user_input = int(input())
input_hundreds = user_input // 100
print(input_hundreds)
input_tens = (user_input - input_hundreds * 100) // 10
print(input_tens)
print(user_input - (input_hundreds * 100 + input_tens * 10))

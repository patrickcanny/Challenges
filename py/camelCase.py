# Author: Patrick Canny
# Hackerrank Algorithms Challenge
# Given an Input String in CamelCase format, print the number of words in the string

import sys

s = raw_input().strip()
num = 1
new = list(s)
for letter in new:
    if letter.isupper():
        num += 1
print num

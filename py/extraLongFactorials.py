#!/bin/python3
# a naiive solution to this problem
# this will certainly cause stack overflow on huge input
import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    if n == 1:
        return 1
    else:
        return n * extraLongFactorials(n-1)

if __name__ == '__main__':
n = int(input())

print(extraLongFactorials(n))

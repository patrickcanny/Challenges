#!/bin/python3
# a naiive solution to this problem
# this will certainly cause stack overflow on huge input
import math
import os
import random
import re
import sys

################################################################
# iterative solution that doesn't obliterate call stack
def factorial(n):
    factIter(1, 1, n)

def factIter(current, count, m):
    if count > m:
        return current
    else:
        return factIter((current*count), (count+1), m)
###############################################################
# recursive version
def extraLongFactorials(n):
    if n == 0:
        return 1
    else:
        return n * extraLongFactorials(n-1)
###################################################################
if __name__ == '__main__':
n = int(input())

print(extraLongFactorials(n))
print(factorial(n))

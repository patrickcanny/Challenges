#Given two strings, determine if they share a common substring (as short as one character)

#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    c1 = collections.Counter(s1)
    c2 = collections.Counter(s2)
    for key in c1:
        if key in c2:
            return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + "\n")

    fptr.close()

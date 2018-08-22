#Determine the minimal number of swaps required to sort a queue

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    swaps = 0
    swapped = False
    #check for chaos
    for i in range(0, len(q)-1):
        if (abs((q[i]-(i+1)) > 2)):
            print("Too chaotic")
            return
    #bubble sort
    for i in range(0, len(q)-1):
        for j in range (0, len(q)-1):
            if q[j] > q[j+1]:
                q[j], q[j+1] = q[j+1], q[j]
                swaps += 1
                swapped = True
                if swapped:
                    swapped = False
                else:
                    break
    print (swaps)

if __name__ == '__main__':
t = int(input())

for t_itr in range(t):
    n = int(input())
    q = list(map(int, input().rstrip().split()))

minimumBribes(q)

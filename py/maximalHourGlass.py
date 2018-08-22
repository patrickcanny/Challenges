#Given a 6x6 array, return the sum of the largest hourglass in the array

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sums = []
    for i in range(0,4):
        for j in range(0,4):
            hgSum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            sums.append(hgSum)

    return(max(sums))




 if __name__ == '__main__':
 fptr = open(os.environ['OUTPUT_PATH'], 'w')

 arr = []
for _ in xrange(6):
    arr.append(map(int, raw_input().rstrip().split()))
    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')
    fptr.close()

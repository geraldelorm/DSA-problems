#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    lrSum, i = 0, 0
    rlSum, j = 0, len(arr[0]) - 1

    for subArr in arr:
        lrSum += subArr[i]
        i += 1
        rlSum += subArr[j]
        j -= 1

    return (abs(lrSum - rlSum))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

    # Time = O(n)
    #  Space = O(1)

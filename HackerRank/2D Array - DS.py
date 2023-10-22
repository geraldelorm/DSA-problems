#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr):
    sums = []
    for r in range(4):
        c = 0
        while c < 4:
            sums.append(
                arr[r][c] + arr[r][c + 1] + arr[r][c + 2]
                + arr[r + 1][c + 1]
                + arr[r + 2][c] + arr[r + 2][c + 1] + arr[r + 2][c + 2]
            )
            c += 1
    return max(sums)


# O(n * m) 4 * 3
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

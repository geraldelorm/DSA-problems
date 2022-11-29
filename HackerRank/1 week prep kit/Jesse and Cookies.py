#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heapify, heappop, heappush

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#


def cookies(k, A):
    heapify(A)
    result = 0

    while True:
        x = heappop(A)
        if x >= k:
            return result

        if A:
            y = heappop(A)
            newVal = x + 2 * y
            heappush(A, newVal)
            result += 1
        else:
            return -1

# Time = O(n) heapification O(n)
# Space = O(1) we transformed the original array to heap


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()

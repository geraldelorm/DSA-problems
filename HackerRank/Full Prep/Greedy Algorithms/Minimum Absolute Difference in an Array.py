#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# Time = O(nlogN)


def minimumAbsoluteDifference(arr):
    min_abs = math.inf
    heapq.heapify(arr)

    prev = heapq.heappop(arr)

    while len(arr) > 0:
        curr = heapq.heappop(arr)
        abs_of_curr_pair = abs(prev - curr)
        min_abs = min(min_abs, abs_of_curr_pair)

        prev = curr

    return min_abs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

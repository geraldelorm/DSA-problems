#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonelyinteger(a):
    lookup = {}
    for i in a:
        if i in lookup.keys():
            lookup[i] += 1
        else:
            lookup[i] = 1

    for i in lookup.keys():
        if lookup[i] == 1:
            return i


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()

    #  Time = O(n)
    #  Space - O(n)

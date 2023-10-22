#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#


def luckBalance(k, contests):
    imp, unimp = [], 0
    for i in range(len(contests)):
        if contests[i][1]:
            imp.append(contests[i][0])
        else:
            unimp += contests[i][0]
    imp.sort(reverse=True)
    return sum(imp[:k]) - sum(imp[k:]) + unimp


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()

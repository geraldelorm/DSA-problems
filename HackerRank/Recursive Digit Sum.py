#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


def superDigit(n, k):
    def helper(num):
        newNum = 0
        for n in num:
            newNum += int(n)
        if len(str(newNum)) == 1:
            return newNum
        else:
            return helper(str(newNum))

    return helper(str(helper(n) * k))


    # Time = O(n)
    # Space = O(n)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#


def flippingBits(n):
    # Write your code here
    n_to_bin = bin(n)[2:]
    l = len(n_to_bin)
    prefix = ''
    if l < 32:
        for i in range(32-l):
            prefix += '0'
    n_to_bin = prefix + n_to_bin

    flipped = ''
    for i in n_to_bin:
        if i == '0':
            flipped += '1'
        else:
            flipped += '0'
    return int(flipped, 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

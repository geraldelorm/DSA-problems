#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def repeatedString(s, n):
    a_count = 0
    for i in range(len(s)):
        if s[i] == "a":
            a_count += 1

    if n % len(s) == 0:
        a_count = a_count * (n // len(s))
    else:
        a_count = a_count * (n // len(s))
        for i in range(n % len(s)):
            if s[i] == "a":
                a_count += 1

    return a_count


# O(n)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

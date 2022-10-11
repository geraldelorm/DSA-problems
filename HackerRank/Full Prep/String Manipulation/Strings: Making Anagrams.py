#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

# O(a + b)
def makeAnagram(a, b):
    deletions = 0
    amap, bmap = {}, {}

    for c in a:
        amap[c] = amap.get(c, 0) + 1

    for c in b:
        bmap[c] = bmap.get(c, 0) + 1

    for c in bmap:
        if c not in amap:
            deletions += bmap[c]

    for c in amap:
        if c not in bmap:
            deletions += amap[c]
        elif amap[c] != bmap[c]:
            deletions += abs(amap[c] - bmap[c])

    return deletions


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys
import string
import collections

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    s = [i for i in s]
    lowers = list(string.ascii_lowercase)
    uppers = list(string.ascii_uppercase)

    lowersRotated = collections.deque(lowers)
    lowersRotated.rotate(-k)

    uppersRotated = collections.deque(uppers)
    uppersRotated.rotate(-k)

    for i in range(len(s)):
        if s[i].islower():
            s[i] = lowersRotated[lowers.index(s[i])]
        elif s[i].isupper():
            s[i] = uppersRotated[uppers.index(s[i])]

    return "".join(s)


# Time = O(n) all operations on array and deque are fixed array size is fixed
# Space = O(n) all array an deque are O(1) fixed size of 26
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

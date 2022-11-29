#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

# O(n^2) time
# O(1) space
def countSwaps(a):
    swaps, n = 0, len(a)

    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                swaps += 1
                a[j], a[j + 1] = a[j + 1], a[j]

    print("Array is sorted in " + str(swaps) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#


def gridChallenge(grid):
    grid = [list(st) for st in grid]

    for i in range(len(grid)):
        grid[i].sort()

    for r in range(1, len(grid)):
        for c in range(len(grid[r])):
            if grid[r - 1][c] > grid[r][c]:
                return "NO"

    return "YES"

    # Time = O(n . nlogn) => O(n^2logn)
    # Space = O(n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()

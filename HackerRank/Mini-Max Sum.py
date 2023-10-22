#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    arr.sort()
    mini = sum(arr[:len(arr) - 1])
    maxi = sum(arr[1:])

    print(f"{mini} {maxi}")


# def miniMaxSum(arr):
#     arr.sort()
#     length = len(arr)
#     max = 0
#     min = 0
#     for i in range(0, length):
#         if i < length - 1:
#             min += arr[i]
#         if i > 0:
#             max += arr[i]
#     print(min, end=" ")
#     print(max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

# Time = O(NlogN)
# Space = O(1)



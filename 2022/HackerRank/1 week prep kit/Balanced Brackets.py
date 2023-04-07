#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isBalanced(s):
    s = [c for c in s]
    stack = []
    for i in range(len(s)):
        if s[i] in ["(", "{", "["]:
            stack.append(s[i])
        else:
            if not len(stack):
                return "NO"
            elif s[i] == ")" and stack.pop() != "(":
                return "NO"
            elif s[i] == "}" and stack.pop() != "{":
                return "NO"
            elif s[i] == "]" and stack.pop() != "[":
                return "NO"

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"
# Time = O(n)
# Space = O(n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

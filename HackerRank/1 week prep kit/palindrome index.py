#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    if s == s[::-1]:  # check if string is a palindrome
        return -1

    st, ed = 0, len(s) - 1

    while st <= ed:  # use two pinters to traverse the string
        # is issues is detected (i.e. some pair do not match)
        if s[st] != s[ed]:
            # check if remaining substring is a palindrone
            if s[st + 1:ed + 1] == s[st + 1:ed + 1][::-1]:
                return st
            if s[st:ed] == s[st:ed][::-1]:  # check if remaining substring is a palindrone
                return ed
            else:
                return -1
        st += 1
        ed -= 1

    return -1

    # Time = O(n)
    # Space = O(n)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()

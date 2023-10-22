#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    hashmap = {}
    
    for word in magazine:
        hashmap[word] = hashmap.get(word, 0) + 1
        
    for word in note:
        if word not in hashmap or hashmap.get(word) == 0:
            print("No")
            return
        hashmap[word] = hashmap.get(word) - 1
            
    print("Yes")


    # time = O(a + b) space = O(a)
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

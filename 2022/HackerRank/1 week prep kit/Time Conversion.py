#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    hour, minutes, seconds, AMorPM = int(s[0:2]), s[3:5], s[6:8], s[8:]

    if AMorPM == "AM":
        hour = "{:02d}".format(hour % 12)
    else:
        if hour != 12:
            hour = hour + 12

    return f"{hour}:{minutes}:{seconds}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

    # Time O(1)
    # Space O(1)
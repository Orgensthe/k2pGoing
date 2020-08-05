#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    valley = 0
    depth = 0

    for idx in range(n):
        if 'U' == s[idx]:
            depth += 1

            if 0 == depth:
                valley += 1
        elif 'D' == s[idx]:
            depth -= 1

    return valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

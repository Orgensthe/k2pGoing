#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump_count = 0
    idx = 0

    while True:
        if len(c) - 1 == idx:
            break

        jump_count += 1
        if idx < len(c) - 2 and 0 == c[idx + 2]:
            idx += 2
        elif 0 == c[idx + 1]:
            idx += 1

    return jump_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

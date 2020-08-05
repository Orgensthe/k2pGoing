#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    pairs = 0

    pair_list = [0 for _ in range(101)]

    for idx, val in enumerate(ar):
        pair_list[val] += 1

    for idx, val in enumerate(pair_list):
        pairs += int(val / 2)

    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap_count = 0

    for idx in range(len(arr)):
        #  temp 가 있어야할 자리에 위치시켜준다.
        while arr[idx] != idx + 1:
            temp = arr[idx]
            arr[idx] = arr[temp-1]
            arr[temp-1] = temp

            swap_count += 1

    return swap_count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())
    n = 7

    # arr = list(map(int, input().rstrip().split()))
    arr = [1, 3, 5, 2, 4, 6, 7]

    res = minimumSwaps(arr)
    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()

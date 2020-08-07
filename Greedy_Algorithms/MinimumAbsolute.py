#!/bin/python3

import math
import os
import random
import re
import sys

# Timeout 발생
# def minimumAbsoluteDifference(arr):
#
#     minimum = sys.maxsize
#
#     for i in range(0, len(arr) -1):
#         for j in range(i+1, len(arr)):
#             result = abs(arr[i] - arr[j])
#             if(minimum > result):
#                 minimum = result
#
#     return minimum

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):

    minimum = sys.maxsize

    sortedArray = sorted(arr)

    for index in range(0, len(sortedArray)-1):
        result = sortedArray[index+1] - sortedArray[index]
        if (minimum > result):
            minimum = result

    return minimum

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

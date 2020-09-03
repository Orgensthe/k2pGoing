#!/bin/python3

import math
import os
import random
import re
import sys

#Complete the minimumSwaps function below.

# Timeout 발생
# def minimumSwaps(arr):
#     swapCounter = 0
#     for i in range(0, len(arr)-1):
#         if arr[i] != i+1:
#             index = arr.index(i+1) # 이 부분 때문인 것으로 추정
#             arr[i], arr[index] = arr[index], arr[i]
#             swapCounter+=1
#     return swapCounter

def minimumSwaps(arr):
    swap_count = 0

    for index in range(len(arr)):
        while arr[index] != index + 1:
            arr[arr[index]-1], arr[index] = arr[index], arr[arr[index]-1]
            swap_count += 1

    return swap_count

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

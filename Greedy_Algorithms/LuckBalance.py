#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):

    total = 0

    sortedList = []

    for data, isImportant in contests:
        if isImportant > 0 :
            sortedList.append([data, isImportant])
        else:
            total += data

    sortedList = sorted(sortedList, key=lambda item: item[0], reverse=True)

    for item in sortedList:
        if(k != 0):
            total += item[0]
            k -= 1
        else:
            total -= item[0]

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()

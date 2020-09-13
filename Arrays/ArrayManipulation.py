#!/bin/python3

import math
import os
import random
import re
import sys

# Time out 발생
# Complete the arrayManipulation function below.
# def arrayManipulation(n, queries):
#     numbers = [0] * n
#     max_num = -1
#
#     for row in range(0, len(queries)):
#         for col in range(queries[row][0]-1, queries[row][1]):
#             numbers[col] += queries[row][2]
#             if numbers[col] > max_num:
#                 max_num = numbers[col]
#
#     return max_num

def arrayManipulation(n, queries):
    numbers = [0] * (n+1)
    max_num = -1

    for query in queries:
        numbers[query[0]-1] += query[2]
        numbers[query[1]] -= query[2]

    temp = 0
    for number in numbers:
        temp += number
        if max_num < temp:
            max_num = temp

    return max_num


if __name__ == '__main__':
    fptr = sys.stdout

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

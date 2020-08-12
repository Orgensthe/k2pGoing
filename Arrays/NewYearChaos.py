#!/bin/python3

import math
import os
import random
import re
import sys

# def minimumBribes(q):
#     originArray = list(range(1, len(q) + 1))
#     sum = 0
#     for index in range(len(q)):
#         if originArray[index] == q[index]:
#             continue
#         else:
#             for dis in range(1, 3):
#                 if q[index] == originArray[index + dis]:
#                     result = dis
#                     break
#             try:
#                 if q[index] == originArray[index + result]:
#                     originArray.insert(index, originArray[index + result])
#                     del originArray[originArray[index + result] + 1]
#                     sum += result
#                 else:
#                     print("Too chaotic")
#                     return
#             except IndexError:
#                 print("Too chaotic")
#                 return
#     print(sum)

# Complete the minimumBribes function below.
def minimumBribes(q):

    sum = 0
    for i in range(len(q)-1, -1, -1):
        if q[i] - (i+1) > 2:
            print('Too chaotic')
            return

        for j in range(max(0, q[i] -2), i):
            if q[j] > q[i]:
                sum += 1

    print(sum)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

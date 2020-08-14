#!/bin/python3

import math
import os
import random
import re
import sys
import collections


# Complete the whatFlavors function below.
# 에러 발생
# def whatFlavors(cost, money):
#     myCounter = collections.Counter(cost)
#
#     for i in range(money-1, -1, -1):
#         if myCounter.get(i) is not None:
#             if myCounter.get(i) > 0:
#                 myCounter[i] -= 1
#             else:
#                 del myCounter[i]
#             if myCounter.get(money - i) is not None:
#                 print(money - i, i + 1)
#                 return

# Complete the whatFlavors function below.
# 타임아웃...
# def whatFlavors(cost, money):
#     newDict = dict()
#
#     for i in range(0, len(cost)):
#         if cost[i] in newDict:
#             newData = ",".join([str(cost[i]), str(i)])
#             newDict[cost[i]] = newData
#         else:
#             newDict[cost[i]] = str(i)
#
#     for i in range(money - 1, -1, -1):
#         if newDict.get(i) is not None:
#             if newDict.get(money - i) is not None:
#                 if i == (money - i):
#                     data = sorted(newDict[i].split(","))
#                     print(data[0], data[1])
#                     return
#                 else:
#                     if int(newDict.get(money - i)) > int(newDict.get(i)):
#                         a = int(newDict.get(i)) + 1
#                         b = int(newDict.get(money - i)) + 1
#                     else:
#                         a = int(newDict.get(money - i)) + 1
#                         b = int(newDict.get(i)) + 1
#
#                     print(a, b)
#                     return

def whatFlavors(cost, money):
    newDict = dict()

    for i in range(len(cost)):
        choose = money - cost[i]

        if choose in newDict:
            print(newDict[choose]+1, i+1)
            return
        else:
            newDict[cost[i]] = i


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)

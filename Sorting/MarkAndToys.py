#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    # 가격 오름차순으로 정렬
    sortedPrices = sorted(prices)

    # 선택한 장난감
    toys = 0

    for price in sortedPrices:
        # 가지고 있는 금액보다 물건의 가격이 작으면 선택
        if k > price:
            toys += 1
            k -= price
        else:
            break

    return toys


if __name__ == '__main__':
    fptr = sys.stdout

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()

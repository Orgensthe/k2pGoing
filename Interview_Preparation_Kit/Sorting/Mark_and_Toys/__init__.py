#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()

    for idx in range(len(prices)):
        k -= prices[idx]
        if k <= 0:
            return idx

    return len(prices)


if __name__ == '__main__':
    k = 50
    prices = [1, 12, 5, 111, 200, 1000, 10]
    result = maximumToys(prices, k)
    print(result)


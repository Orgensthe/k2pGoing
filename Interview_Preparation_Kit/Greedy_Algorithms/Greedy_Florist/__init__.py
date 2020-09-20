#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c = sorted(c, reverse=True)

    total_price = 0
    for idx in range(len(c)):
        q = idx // k
        total_price += (q + 1) * c[idx]

    return total_price


if __name__ == '__main__':
    n = 5
    k = 3
    c = [1, 3, 5, 7, 9]

    minimumCost = getMinimumCost(k, c)
    print(minimumCost)

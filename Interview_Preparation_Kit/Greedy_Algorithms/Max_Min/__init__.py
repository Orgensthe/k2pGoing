#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()

    minimum_value = sys.maxsize
    for idx in range(len(arr) - k + 1):
        current_value = arr[idx + k - 1] - arr[idx]
        if current_value < minimum_value:
            minimum_value = current_value

    return minimum_value


if __name__ == '__main__':
    n = 7
    k = 3
    arr = [100, 200, 300, 350, 400, 401, 402]

    result = maxMin(k, arr)
    print(result)

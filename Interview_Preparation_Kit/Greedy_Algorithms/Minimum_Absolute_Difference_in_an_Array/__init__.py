#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    min = sys.maxsize

    for idx in range(len(arr) - 1):
            if min > abs(arr[idx+1] - arr[idx]):
                min = abs(arr[idx+1] - arr[idx])

    return min


if __name__ == '__main__':

    arr = [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]
    result = minimumAbsoluteDifference(arr)
    print(result)

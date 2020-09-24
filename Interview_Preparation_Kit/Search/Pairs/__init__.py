#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the pairs function below.
def pairs(k, arr):
    dic = dict.fromkeys(arr, 1)

    pairs_count = 0
    for idx in range(len(arr)):
        if arr[idx] - k in dic:
            pairs_count += 1

    return pairs_count


if __name__ == '__main__':
    n = 5
    k = 2
    arr = [1, 5, 3, 4, 2]

    result = pairs(k, arr)
    print(result)

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    value_list = [0] * (n + 1)
    for q in queries:
        value_list[q[0] - 1] += q[2]
        value_list[q[1]] -= q[2]
    # start ~ end+1

    max_value = 0
    current_value = 0
    for value in value_list:
        current_value += value
        if max_value < current_value:
            max_value = current_value

    return max_value


if __name__ == '__main__':
    n = 5
    queries = [[1, 3, 100], [2, 5, 100], [3, 4, 100]]

    result = arrayManipulation(n, queries)
    print(result)

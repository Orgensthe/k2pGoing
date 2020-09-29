#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


def is_end(stack, idx):
    return len(stack) <= idx


# Complete the riddle function below.
def riddle(arr):
    maximum_result = []
    for idx in range(len(arr)):
        queue = deque(arr)

        minimum_result = []
        while not is_end(queue, idx):
            pop_list = [queue.popleft()]
            for p in range(idx):
                pop_list.append(queue.popleft())

            for q in range(idx):
                queue.appendleft(pop_list[idx - q])

            minimum_result.append(min(pop_list))
        maximum_result.append(max(minimum_result))

    return maximum_result


if __name__ == '__main__':
    n = 6
    arr = [3, 5, 4, 7, 6, 2]
    res = riddle(arr)
    print(res)

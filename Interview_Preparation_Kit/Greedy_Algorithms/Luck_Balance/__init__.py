#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the luckBalance function below.
def luckBalance(k, contests):
    contests.sort(reverse=True)

    luck = 0
    for contest in contests:
        if 0 == contest[1]:
            luck += contest[0]
        elif 1 == contest[1] and 0 < k:
            luck += contest[0]
            k -= 1
        else:
            luck -= contest[0]

    return luck


print(luckBalance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]))
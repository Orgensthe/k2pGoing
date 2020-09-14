#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the primality function below.
def primality(n):
    if 1 == n:
        return 'Not prime'

    for idx in range(2, int(math.sqrt(n) + 1)):
        if 0 == n % idx:
            return 'Not prime'

    return 'Prime'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input())

    for p_itr in range(p):
        n = int(input())

        result = primality(n)

        fptr.write(result + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):

    s1Dict = {i: i for i in s1}
    errorCount = 0
    for item in s2:
        try:
            s1Dict[item]
            return 'YES'
        except KeyError:
            errorCount += 1

    if(errorCount == len(s2)):
        return 'NO'

if __name__ == '__main__':
    fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

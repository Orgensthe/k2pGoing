#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    first_anagram = dict()
    second_anagram = dict()

    for item in a:
        if(first_anagram.get(item)):
            first_anagram[item] += 1
        else:
            first_anagram[item] = 1

    for item in b:
        if(second_anagram.get(item)):
            second_anagram[item] += 1
        else:
            second_anagram[item] = 1


    count = 0

    for item in b:
        try:
            if(first_anagram[item]>0):
                first_anagram[item] -= 1
            else:
                count += 1
        except KeyError:
            count += 1

    for item in a:
        try:
            if(second_anagram[item]>0):
                second_anagram[item] -= 1
            else:
                count += 1
        except KeyError:
            count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

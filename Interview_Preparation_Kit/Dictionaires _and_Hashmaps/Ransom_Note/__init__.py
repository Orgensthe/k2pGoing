#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    megazine_dic = {}
    for val in magazine:
        if val not in megazine_dic:
            megazine_dic[val] = 1
        else:
            megazine_dic[val] += 1

    try:
        for val in note:
            megazine_dic[val] -= 1
            if megazine_dic[val] < 0:
                print('No')
                return
        print('Yes')
    except KeyError:
        print('No')


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

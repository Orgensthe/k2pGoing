#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_dict = {}

    for item in magazine:
        if magazine_dict.get(item):
            magazine_dict[item] += 1
        else:
            magazine_dict[item] = 1

    for item in note:
        try:
            if magazine_dict[item] > 0:
                magazine_dict[item] -= 1
            else:
                print('No')
                return

        except KeyError:
            print('No')
            return

    print('Yes')


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

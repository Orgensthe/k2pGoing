#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    dic = {}
    for idx, value in enumerate(cost):

        if money - value in dic:
            print(dic[money - value] + 1, idx + 1)
            break
        else:
            dic[value] = idx


if __name__ == '__main__':
    money = 5
    cost = [2, 3, 1, 4, 5]

    whatFlavors(cost, money)

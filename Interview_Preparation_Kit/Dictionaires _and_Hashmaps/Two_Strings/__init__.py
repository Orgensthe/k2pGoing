#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1_unique = ''.join(set(s1))

    string_dic = {}
    for alpha in s1_unique:
        string_dic[alpha] = 1

    for alpha in s2:
        if alpha in string_dic.keys():
            return "YES"

    return "NO"


if __name__ == '__main__':
    s1 = "hello"
    s2 = "world"
    result = twoStrings(s1, s2)

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the isBalanced function below.
def isBalanced(s):
    leftBrackets = []

    #데이터 명세
    switchDict = {')': '(', '}': '{', ']': '['}

    for index, data in enumerate(s):
        if data == '[' or data == '{' or data == '(':
            leftBrackets.append(data)
        else:
            try :
                target = leftBrackets.pop()
                if switchDict[data] != target:
                    return 'NO'
            except IndexError:
                return 'NO'

    #스택에 데이터가 남아있을 시 no balance
    if len(leftBrackets) != 0:
        return 'NO'

    return 'YES'


if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

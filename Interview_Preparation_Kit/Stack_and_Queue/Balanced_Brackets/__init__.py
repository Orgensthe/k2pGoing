#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


# Complete the isBalanced function below.
def isBalanced(s):
    queue = deque()

    for c in s:
        if c == '}' or c == ']' or c == ')':
            if queue: # Check queue isEmpty?
                pop_bracket = queue.pop()

                if ((pop_bracket == '{' and c == '}') or # Check bracket isPair?
                        (pop_bracket == '[' and c == ']') or
                        (pop_bracket == '(' and c == ')')):
                    pass
                else:
                    return 'NO'
            else:
                return 'NO'
        else:
            queue.append(c)

    # Check queue isEmpty?
    if queue:
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':
    s = "{{[]}}"
    result = isBalanced(s)
    print(result)

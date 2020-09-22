#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from collections import Counter


# Complete the isValid function below.
def isValid(s):
    alphabet = defaultdict(int)
    for letter in s:
        alphabet[letter] += 1

    values = alphabet.values()
    values_count = Counter(values)
    most_frequent_value = list(values_count.keys())[0]

    compare_count = 0
    for letter in values:
        if most_frequent_value != letter:
            compare_count += 1

        if 2 <= compare_count:
            return "NO"

    return "YES"


if __name__ == '__main__':
    s = "aabbccddeefghi"
    result = isValid(s)
    print(result)

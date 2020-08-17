#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = 5
    binary = bin(n)[2:]

    max_number = 0
    number = 0
    for idx in binary:
        if '1' == idx:
            number += 1
        else:
            number = 0

        if max_number < number:
            max_number = number

    print(max_number)
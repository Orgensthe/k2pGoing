#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    if 1 == N % 2:
        print("Weird")
    elif 0 == N % 2 and (2 <= N <= 5 or 20 < N):
        print("Not Weird")
    elif 0 == N % 2 and 6 <= N <= 20:
        print("Weird")

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    alphabet_list = [0 for _ in range(26)]
    for alpha in a:
        alphabet_list[ord(alpha)-97] += 1
    for alpha in b:
        alphabet_list[ord(alpha)-97] -= 1

    anagrams = 0
    for alpha in alphabet_list:
        anagrams += abs(alpha)
    print(anagrams)

makeAnagram("cde", "abc")
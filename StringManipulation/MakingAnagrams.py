from collections import Counter

def makeAnagram(a, b):

    return sum( (Counter(a)-Counter(b)).values()) + sum( (Counter(b)-Counter(a)).values())
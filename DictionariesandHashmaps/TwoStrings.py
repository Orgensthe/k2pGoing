from collections import Counter

def twoStrings(s1, s2):

    if sum( (Counter(s1)-Counter(s2)) .values()) == len(s1):
        return  "NO"
    else:
        return "YES"



print(twoStrings("wouldyoulikefries","abcabcabcabcabcabc"))
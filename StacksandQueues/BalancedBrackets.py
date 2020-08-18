from collections import deque

def isBalanced(s):

    dq = deque()

    left_bracket = ["[","(","{"]

    dic = {}
    dic['}'] = '{'
    dic[')'] = '('
    dic[']'] = '['


    for c in s:



        if c in left_bracket:
            dq.append(c)
            continue


        bracket = dq.pop()

        if bracket != dic[c]:
            return "NO"

    if not dq:
        return "YES"
    else:
        return "NO"



print(isBalanced("}}}}"))
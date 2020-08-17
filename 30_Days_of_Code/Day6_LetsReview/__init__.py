# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    S = input()

    even = ""
    odd = ""

    for idx, val in enumerate(S):
        if 0 == idx % 2:
            even += val
        else:
            odd += val

    print(even + " " + odd)

from collections import Counter

def minimumBribes(q):


    if len(q) == 1:
        print(0)
        return

    dic = {}

    first_num = q[0]

    result = 0

    for i in range(1,len(q)+1):

        position =  q.index(i)
        print(i,position,position >= i-1,q[position],q)

        if q[position] == i or position >= i-1 :
            continue

        if position < i:
            print("too chaotic")
            return

        result += (i-position)

        print(result)

    print(result)
    # for _ in range(len(q),-1,-1):
    #     for j in range(_-1):
    #         if q[j] > q[j+1]:
    #             if q[j] in dic and dic[q[j]] == 2:
    #                 print("Too chaotic")
    #                 return
    #
    #             if q[j] not in dic:
    #                 dic[q[j]] = 1
    #             else:
    #                 dic[q[j]] += 1
    #
    #             q[j],q[j+1] = q[j+1],q[j]




minimumBribes([1,2,5,3,7,8,6,4])
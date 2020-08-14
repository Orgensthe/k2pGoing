def whatFlavors(cost, money):

    dic = {}


    for i, _cost in enumerate(cost):
        Sunny = _cost
        Jonny = money - _cost

        if Jonny in dic :
            print(dic[Jonny]+1,i+1)
            return
        else:
            dic[Sunny] = i

    #
    # for i in range(len(cost)):
    #     if cost[i] in dic :
    #
    #
    # for key in dic.keys():
    #     if money//2 == key and len(dic[key]) >1 :
    #         print(dic[key][0]+1,dic[key][1]+1)
    #         return
    #
    #     elif money-key in dic and dic[money-key][0] !=dic[key][0]:
    #         print(dic[key][0]+1, dic[money-key][0]+1)
    #         return

whatFlavors([4, 3, 2, 5, 7],8)
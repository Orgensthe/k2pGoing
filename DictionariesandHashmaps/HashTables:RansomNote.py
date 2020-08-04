def checkMagazine(magazine, note):



    dic = dict()
    for word in magazine:
        if word in dic:
            dic[word] +=1
        else:
            dic[word] = 1
    try:
        for word in note:
            dic[word]-=1
            if dic[word] < 0 :
                print("No")
                return
        print("Yes")
    except KeyError:
        print("No")





checkMagazine(["two","times","three","is","not","four"],["two","times","two","is","four"])
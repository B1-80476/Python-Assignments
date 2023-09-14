def function4():

    List1 = [1,2,3,4,5,6,7,8,9,7,6,2,4,2,5,23,6,4]

    dic = {}

    for count in List1:
        if dic.get(count) is None:
            dic[count] = 1

        else:
            dic[count] += 1

    print(dic)

function4()



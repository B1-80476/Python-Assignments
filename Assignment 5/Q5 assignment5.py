def function5():

    list1 = []
    list2 = []
    list3 = []

    dict1 = {"EVEN":[] , "ODD":[]}

    for value in range(0,6):
        feed = int(input(f"Please enter value no.{value+1}:"))
        list1.append(feed)

    for value2 in range(0, 6):
       if list1[value2]%2 == 0:
           list2.append(list1[value2])
       else:
           list3.append(list1[value2])

    print(list1)
    print(list2)
    print(list3)

    dict1["EVEN"] = list2
    dict1["ODD"] = list3

    print(dict1)



function5()
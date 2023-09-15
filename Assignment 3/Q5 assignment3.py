def overlapping():

    list1 = []
    list2 = []

    no_of_item1 = int(input("please enter no of item you want to insert in List1:"))
    no_of_item2 = int(input("please enter no of item you want to insert in List2:"))

    for index in range(no_of_item1):
        item_list1 = input("item name in list 1:")
        list1.append(item_list1)

    for index in range(no_of_item2):
        item_list2 = input("item name in list 2:")
        list2.append(item_list2)

    flag = False
    for element in list1:
        if element in list2:
            flag = True
            break

    if flag:
        print('True')
    else:
        print('False')


overlapping()

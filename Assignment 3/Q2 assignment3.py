def function2():

    list1 = []

    no_of_item = int(input("please enter no of item you want to insert in this list:"))

    for index in range(no_of_item):
        item = input("item name:")
        list1.append(item)

    for index1 in range(0,len(list1),2):
            print(list1[index1])

function2()
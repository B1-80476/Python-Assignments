
def function6():

    input1 = int(input("please enter number of element you want to enter in list:"))
    list1 = []

    for index in range(input1):
        input2 = input("please enter the element:")
        list1.append(input2)

    first = list1[0]

    list1.remove(list1[0])

    list1.append(first)


    print(list1)

function6()


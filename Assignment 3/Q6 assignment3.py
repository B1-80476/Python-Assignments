
def fun6():
    no_of_input=int(input("please enter Number of input:"))

    list1=[]
    for num in range(no_of_input):
        list1.append(input())

    list1.sort()
    print(list1)

    max= no_of_input-1
    print(list1[max])


fun6()
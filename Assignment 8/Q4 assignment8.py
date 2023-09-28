
def cube_ofnum():

    list1 = []
    no_ofinput = int(input("Please enter number of input you want to display:"))

    for index in range(no_ofinput):
        value = int(input("Enter number:"))
        tuple = value, value**3

        list1.append(tuple)

    print(list1)

cube_ofnum()


